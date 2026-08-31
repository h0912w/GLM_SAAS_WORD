"""단어뱅크 기반 제목 생성 파이프라인 (2026-08-18 두 번째 프로젝트 정의 전환).

`run.py`의 유일한 진입점. "정확히 500개 선정·발행" 계약과 업계 30% 분산 상한은
폐기됐다 - 산출물은 목표 개수 없이 계속 누적되는 4개 문서(원시 생성 전체 /
Keyword Planner OK+NG 전체 / OK만 정리된 표 / OK 단어 리스트) 모델이다. 실행
모델도 "한 번의 CLI 실행 = 한 라운드"로 단순화됐다(더 이상 MAX_ROUNDS/
shortfall*2 재생성 루프가 없다). 수요/공급(demand/supply) 파이프라인은 이
전환으로 완전히 삭제됐으므로, `RunOptions`/판정 예외 클래스는 더 이상 다른
모듈과 공유하지 않고 이 파일이 직접 소유한다.
"""

from __future__ import annotations

import csv
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from . import config, ids, judgment, run_state, word_bank, word_generation, word_performance
from .contracts import atomic_write_text, normalize_title

# 저지능 모델 호환 강화 구조(2026-08-31)에서 낮은 confidence로 스스로 신고된
# 승인 판정을 자동 레드팀 재검증에 회부하는 기준값.
CONFIDENCE_RECHECK_THRESHOLD = 0.6
from .judgment import JudgmentRequired
from .keyword_metrics_client import (
    ApiRuntimeConfig,
    KeywordMetricsBudgetExceeded,
    KeywordMetricsClient,
    KeywordMetricsCredentialsError,
    credentials_from_env,
    load_env_file,
)

__all__ = [
    "ImplementationPendingError",
    "JudgmentRequired",
    "RecoveryRequired",
    "RetryRequired",
    "RunOptions",
    "run_pipeline",
]

STAGES = (
    "load_state",
    "generate_and_review_titles",
    "update_memory_and_git_checkpoint",
)

# 모드별 round-size 기본값(명시적으로 --round-size를 안 주면 이 값 사용).
# QA=소규모 스모크 테스트, production=실제 대량 배치 - 두 모드의 유일한 차이.
DEFAULT_ROUND_SIZE = {"qa": 50, "production": 10000}


# ---------------------------------------------------------------------------
# 판정 예외 클래스 (2026-08-18 이전엔 pipeline.py에서 재사용했으나, 그 모듈이
# 수요/공급 삭제로 없어져서 이 파일이 직접 소유한다)
# ---------------------------------------------------------------------------


class ImplementationPendingError(RuntimeError):
    pass


class RetryRequired(RuntimeError):
    """판정 대기가 아닌, 제어된 중단. 예: 이번 라운드에 신규 후보가 전혀 없거나
    Keyword Planner API 예산이 소진된 경우. 최종 산출물은 갱신되지 않는다.

    status는 기본 RETRYING이지만 CAPABILITY_STAGNATION(단어뱅크 조합공간이
    진짜로 소진되어 이 실행/설정으로는 더 진행 불가)일 수도 있다 - 둘 다 이
    예외 타입으로 발생하며, HANDOFF/ACTIVE_ISSUES 기록 목적으로만 구분된다.
    """

    def __init__(self, reason: str, *, status: str = "RETRYING"):
        self.reason = reason
        self.status = status
        super().__init__(f"{status}: {reason}")


class RecoveryRequired(RuntimeError):
    """원자적 쓰기 자체의 사후 검증이 실패한 경우(예: 캐시 파일의 병합 결과가
    방금 쓴 내용과 다름) - 자동 재시도가 안전하지 않아 수동 점검을 위해 멈춘다."""

    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(f"RECOVERY_REQUIRED: {reason}")


@dataclass(frozen=True)
class RunOptions:
    mode: str
    project_root: Path
    resume: bool = False
    run_id: str | None = None
    round_size: int | None = None

    def validate(self) -> None:
        if self.mode not in {"production", "qa"}:
            raise ValueError("mode must be production or qa")
        if self.round_size is not None and self.round_size <= 0:
            raise ValueError("round_size, if given, must be positive")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _run_dir(project_root: Path, state: run_state.RunState) -> Path:
    return run_state.run_dir(project_root, state.run_id)


def _read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines() if path.exists() else []


def _pause_for_judgment(project_root: Path, state: run_state.RunState, stage_name: str, request_path: Path) -> None:
    state.status = "RUNNING"
    state.awaiting_judgment = stage_name
    state.updated_at = ids.now_kst().isoformat()
    run_state.save(project_root, state)
    raise JudgmentRequired(stage_name, request_path)


def _run_or_raise(project_root: Path, script_name: str, *extra_args: str) -> subprocess.CompletedProcess:
    script_path = project_root / "scripts" / script_name
    result = subprocess.run(
        [sys.executable, str(script_path), "--project-root", str(project_root), *extra_args],
        cwd=project_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"{script_name} exited {result.returncode}\nstdout: {result.stdout}\nstderr: {result.stderr}")
    return result


# ---------------------------------------------------------------------------
# 문서 ① 원시 생성 전체 ledger (2026-08-18 신규): 생성+판정된 모든 후보를
# verdict(승인/거절)와 무관하게 기록한다. 이게 있어야 (a) 같은 조합이 다시
# 생성/판정되는 낭비를 막고, (b) AI 승인은 됐지만 아직 Keyword Planner로 확인
# 안 된 후보("backlog")가 다음 실행에서 유실되지 않고 자동으로 이어진다.
# keyword_metrics_cache.csv와 동일한 "정규화 키로 병합 후 전체 재기록" 패턴.
# ---------------------------------------------------------------------------

_LEDGER_COLUMNS = ("title", "industry", "ai_approved", "ai_reason", "judged_at")


def _generated_ledger_path(project_root: Path) -> Path:
    return project_root / "output" / "deliverables" / "history" / "generated_candidates.csv"


def _load_generated_ledger(project_root: Path) -> dict[str, dict]:
    path = _generated_ledger_path(project_root)
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8", newline="") as f:
        return {normalize_title(row["title"]): row for row in csv.DictReader(f)}


def _append_generated_ledger_rows(project_root: Path, new_rows: list[dict]) -> None:
    if not new_rows:
        return
    ledger = _load_generated_ledger(project_root)
    for row in new_rows:
        ledger[normalize_title(row["title"])] = row
    ordered = sorted(ledger.values(), key=lambda r: r["title"])

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=_LEDGER_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(ordered)
    atomic_write_text(_generated_ledger_path(project_root), buffer.getvalue())


def _export_generated_ledger_snapshot(project_root: Path, when) -> None:
    src_path = _generated_ledger_path(project_root)
    if not src_path.exists():
        return
    stamp = when.strftime("%Y%m%d_%H%M%S") + "_KST"
    atomic_write_text(
        _history_snapshots_dir(project_root) / f"generated_candidates_{stamp}.csv",
        src_path.read_text(encoding="utf-8"),
    )


def _excluded_normalized(project_root: Path, state: run_state.RunState) -> set[str]:
    blocklist = _read_lines(project_root / "input" / "blocklist.txt")
    excluded = {normalize_title(t) for t in blocklist if t.strip()}
    # 한 번 생성+판정된 조합은 승인/거절과 무관하게 다시 생성하지 않는다 -
    # 승인분 중 아직 Keyword Planner 미확인인 것은 backlog로 별도 처리된다
    # (_stage_load_state 참고), 재생성 대상에서는 제외되지만 유실되지 않는다.
    excluded |= set(_load_generated_ledger(project_root).keys())
    # 골든셋 카나리아(config/golden_set.csv)는 실제 산출물이 아니라 판정 품질
    # 확인용 미끼이므로, 실제 후보 생성이 우연히 같은 문구를 만들어 혼동을
    # 일으키지 않도록 제외한다(2026-08-31 강화 구조).
    excluded |= word_performance.golden_set_titles(project_root)
    return excluded


# ---------------------------------------------------------------------------
# Stage: load_state - backlog 스윕(AI 승인은 됐지만 Keyword Planner 미확인인
# 후보를 다음 게이트 실행에 먼저 태운다)
# ---------------------------------------------------------------------------


def _stage_load_state(project_root: Path, options: RunOptions, state: run_state.RunState) -> None:
    ledger = _load_generated_ledger(project_root)
    cache = _load_metrics_cache(project_root)
    backlog = [
        {"title": row["title"], "industry": row["industry"]}
        for norm, row in ledger.items()
        if row["ai_approved"] == "True" and norm not in cache
    ]
    state.context["backlog"] = backlog


# ---------------------------------------------------------------------------
# Keyword Planner filter gate (변경 없음 - CLAUDE.md §4, memory/ACTIVE_ISSUES.md
# GKP-001) - 순수 수치 비교라 코드 전담, 판정은 이 함수 호출 전에 이미 끝나 있다.
# ---------------------------------------------------------------------------


def _keyword_metrics_settings(project_root: Path) -> tuple[float, float, ApiRuntimeConfig, Path]:
    cfg = config.load_keyword_metrics_config(project_root)
    api_cfg = cfg.get("api", {})
    runtime = ApiRuntimeConfig(
        batch_size=api_cfg.get("batch_size", 20),
        free_tier_budget=api_cfg.get("free_tier_budget", 1000),
        min_request_interval_ms=api_cfg.get("min_request_interval_ms", 500),
        geo_target_constants=api_cfg.get("geo_target_constants", ""),
        language=api_cfg.get("language", "languageConstants/1000"),
        keyword_plan_network=api_cfg.get("keyword_plan_network", "GOOGLE_SEARCH"),
    )
    credentials_path = Path(api_cfg.get("credentials_env_path", ".env.local"))
    if not credentials_path.is_absolute():
        credentials_path = project_root / credentials_path
    return cfg["avg_monthly_searches_min"], cfg["competition_index_exact"], runtime, credentials_path


# ---------------------------------------------------------------------------
# 문서 ②③ Keyword Planner 조회 결과(전체/OK만) - 기존 로직 그대로 유지.
# ---------------------------------------------------------------------------

_CACHE_COLUMNS = ("title", "avg_monthly_searches", "competition_index", "api_status", "gate_passed", "checked_at")


def _metrics_cache_path(project_root: Path) -> Path:
    return project_root / "output" / "deliverables" / "history" / "keyword_metrics_cache.csv"


def _metrics_passed_path(project_root: Path) -> Path:
    return project_root / "output" / "deliverables" / "history" / "keyword_metrics_passed.csv"


def _load_metrics_cache(project_root: Path) -> dict[str, dict]:
    path = _metrics_cache_path(project_root)
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8", newline="") as f:
        return {normalize_title(row["title"]): row for row in csv.DictReader(f)}


def _record_to_cache_row(title: str, record, gate_passed: bool, checked_at: str) -> dict:
    return {
        "title": title,
        "avg_monthly_searches": "" if record.avg_monthly_searches is None else record.avg_monthly_searches,
        "competition_index": "" if record.competition_index is None else record.competition_index,
        "api_status": record.api_status,
        "gate_passed": str(gate_passed),
        "checked_at": checked_at,
    }


def _append_metrics_cache_rows(project_root: Path, new_rows: list[dict]) -> None:
    if not new_rows:
        return
    cache = _load_metrics_cache(project_root)
    for row in new_rows:
        cache[normalize_title(row["title"])] = row
    ordered = sorted(cache.values(), key=lambda r: r["title"])

    full_buffer = io.StringIO()
    writer = csv.DictWriter(full_buffer, fieldnames=_CACHE_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(ordered)
    atomic_write_text(_metrics_cache_path(project_root), full_buffer.getvalue())

    passed_buffer = io.StringIO()
    passed_writer = csv.DictWriter(passed_buffer, fieldnames=_CACHE_COLUMNS, lineterminator="\n")
    passed_writer.writeheader()
    passed_writer.writerows([r for r in ordered if r["gate_passed"] == "True"])
    atomic_write_text(_metrics_passed_path(project_root), passed_buffer.getvalue())


def _final_words_dir(project_root: Path) -> Path:
    return project_root / "output" / "deliverables" / "final_words"


def _history_snapshots_dir(project_root: Path) -> Path:
    return project_root / "output" / "deliverables" / "history" / "snapshots"


def _export_final_words_and_history_snapshots(project_root: Path, when) -> None:
    """문서 ④(OK 단어 리스트)의 마스터(`passed_words_latest.txt`, 항상 최신
    전체 누적)와 날짜시간 스냅샷을 쓰고, 문서 ②③의 날짜시간 스냅샷도 함께
    쓴다. `words.txt`는 더 이상 존재하지 않으므로 스냅샷 소스에서 제외됐다
    (2026-08-18 전환). 라운드당 1회 호출(_apply_keyword_metrics_filter 종료 시)."""
    stamp = when.strftime("%Y%m%d_%H%M%S") + "_KST"

    passed_path = _metrics_passed_path(project_root)
    if passed_path.exists():
        with passed_path.open("r", encoding="utf-8", newline="") as f:
            titles = [row["title"] for row in csv.DictReader(f)]
        content = "\n".join(titles) + "\n" if titles else ""
        atomic_write_text(_final_words_dir(project_root) / f"passed_words_{stamp}.txt", content)
        atomic_write_text(_final_words_dir(project_root) / "passed_words_latest.txt", content)

    snapshot_sources = (
        (_metrics_cache_path(project_root), "keyword_metrics_cache", "csv"),
        (_metrics_passed_path(project_root), "keyword_metrics_passed", "csv"),
    )
    for src_path, prefix, ext in snapshot_sources:
        if not src_path.exists():
            continue
        atomic_write_text(
            _history_snapshots_dir(project_root) / f"{prefix}_{stamp}.{ext}",
            src_path.read_text(encoding="utf-8"),
        )


def _build_keyword_metrics_client(project_root: Path) -> KeywordMetricsClient:
    searches_min, competition_exact, runtime, credentials_path = _keyword_metrics_settings(project_root)
    env = load_env_file(credentials_path)
    creds = credentials_from_env(env)

    def _persist_batch(records: list) -> None:
        checked_at = ids.now_kst().isoformat()
        rows = []
        for record in records:
            gate_passed = (
                record.avg_monthly_searches is not None
                and record.competition_index is not None
                and record.avg_monthly_searches >= searches_min
                and record.competition_index == competition_exact
            )
            rows.append(_record_to_cache_row(record.word, record, gate_passed, checked_at))
        _append_metrics_cache_rows(project_root, rows)

    return KeywordMetricsClient(creds, runtime, on_batch_fn=_persist_batch)


def _write_metrics_evidence(project_root: Path, state: run_state.RunState, evidence: list[dict]) -> None:
    path = project_root / "output" / "_pipeline" / "intermediate" / f"{state.run_id}_keyword_metrics_evidence.jsonl"
    existing = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    lines = existing + [json.dumps(entry, ensure_ascii=False, sort_keys=True) for entry in evidence]
    atomic_write_text(path, "\n".join(lines) + "\n" if lines else "")


def _apply_keyword_metrics_filter(
    project_root: Path, state: run_state.RunState, candidates: list[dict]
) -> list[dict]:
    """avg_monthly_searches>=임계값 AND competition_index==임계값(기본 0)인
    후보만 통과시킨다. NULL competition_index는 항상 탈락(메트릭 자체가 없는
    "죽은 단어"). pass/fail 전부 run별 evidence(jsonl)와 누적 캐시(문서②③)에
    기록된다. 캐시에 이미 있는 후보는 API 재조회 없이 재사용."""
    if not candidates:
        return []

    searches_min, competition_exact, _, _ = _keyword_metrics_settings(project_root)
    cache = _load_metrics_cache(project_root)

    cached_hits: dict[str, dict] = {}
    uncached_titles: list[str] = []
    for candidate in candidates:
        row = cache.get(normalize_title(candidate["title"]))
        if row is not None:
            cached_hits[candidate["title"]] = row
        else:
            uncached_titles.append(candidate["title"])

    fresh_records_by_title = {}
    if uncached_titles:
        client = _build_keyword_metrics_client(project_root)
        fresh_records_by_title = {record.word: record for record in client.fetch_metrics(uncached_titles)}
        # already persisted incrementally per-batch via on_batch_fn above

    checked_at = ids.now_kst().isoformat()
    passed: list[dict] = []
    evidence: list[dict] = []
    for candidate in candidates:
        title = candidate["title"]
        if title in cached_hits:
            row = cached_hits[title]
            avg = None if row["avg_monthly_searches"] == "" else float(row["avg_monthly_searches"])
            competition_index = None if row["competition_index"] == "" else float(row["competition_index"])
            api_status = row["api_status"]
            gate_passed = row["gate_passed"] == "True"
            source = "cache"
        else:
            record = fresh_records_by_title.get(title)
            avg = record.avg_monthly_searches if record else None
            competition_index = record.competition_index if record else None
            api_status = record.api_status if record else "failed"
            gate_passed = (
                avg is not None
                and competition_index is not None
                and avg >= searches_min
                and competition_index == competition_exact
            )
            source = "api"
        evidence.append(
            {
                "title": title,
                "avg_monthly_searches": avg,
                "competition_index": competition_index,
                "api_status": api_status,
                "passed": gate_passed,
                "source": source,
                "checked_at": checked_at,
            }
        )
        if gate_passed:
            passed.append(candidate)

    _write_metrics_evidence(project_root, state, evidence)
    # 스냅샷 생성은 호출자에게 위임(finally 블록에서 처리) - 예외 안전성 확보
    return passed


# ---------------------------------------------------------------------------
# 자가확장 단어뱅크 (2026-08-18, 사용자 지시): 조합공간이 완전히 소진되면(단어
# 자체가 없어진 게 아니라 손으로 고른 목록이 작았을 뿐 - 사용자 지적), 실행을
# CAPABILITY_STAGNATION으로 정직하게 끝내는 대신 현재 세션이 그 자리에서 직접
# 새 도메인어/기능어를 제안하는 별도 판정 라운드(`expand_word_bank`)를 한 번
# 연다. 제안은 word_bank.py 원본을 고치지 않고 `config/word_bank_expansions.csv`
# (누적, git 추적)에만 append되고, `_merged_word_bank`가 매 실행마다 원본과
# 병합해 후보 생성에 넘긴다 - word_bank.py 자체의 큐레이션 이력은 그대로 보존.
# ---------------------------------------------------------------------------

# pattern_tag(2026-08-31 추가): 새 단어가 어떤 승자 패턴 가설을 대표하는지
# 표시하는 자유 태그(예: "specific_place_noun"). 기존 파일(80KB+)에는 이
# 컬럼이 없으므로 `_append_word_bank_expansion_rows`가 DictWriter의 restval
# 로 하위호환 기본값("")을 채운다 - 별도 마이그레이션 스크립트 불필요.
_EXPANSION_COLUMNS = ("type", "word", "industry", "added_at", "added_by_run_id", "pattern_tag")


def _word_bank_expansions_path(project_root: Path) -> Path:
    return project_root / "config" / "word_bank_expansions.csv"


def _load_word_bank_expansion_rows(project_root: Path) -> list[dict]:
    path = _word_bank_expansions_path(project_root)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _load_dynamic_word_bank(project_root: Path) -> tuple[dict[str, list[str]], list[str]]:
    domain_words: dict[str, list[str]] = {}
    function_words: list[str] = []
    for row in _load_word_bank_expansion_rows(project_root):
        if row["type"] == "domain":
            domain_words.setdefault(row["industry"], []).append(row["word"])
        elif row["type"] == "function":
            function_words.append(row["word"])
    return domain_words, function_words


def _merged_word_bank(project_root: Path) -> tuple[dict[str, tuple[str, ...]], tuple[str, ...]]:
    """`word_bank.py`(정적 원본) + `config/word_bank_expansions.csv`(세션이
    누적 제안한 것) 병합, 중복 제거. 반환 형태는 `word_bank.DOMAIN_WORDS`/
    `FUNCTION_WORDS`와 동일해서 `word_generation.generate_combinations`에
    그대로 넘길 수 있다.

    2026-08-18 학습 루프: `config/retired_function_words.csv`(실측으로 통과
    0건이 확정된 기능어, word_performance 참고)에 오른 기능어는 병합 풀에서
    제외한다 - 이미 시도된 조합은 ledger가 재생성을 막지만, 이 필터가 없으면
    앞으로 추가될 새 도메인어가 죽은 기능어와 계속 짝지어져 API 예산을
    낭비한다(실측: 전체 조회의 32%가 통과 0건 기능어에 소모됨)."""
    dyn_domain, dyn_function = _load_dynamic_word_bank(project_root)
    merged_domain: dict[str, list[str]] = {
        industry: list(words) for industry, words in word_bank.DOMAIN_WORDS.items()
    }
    for industry, words in dyn_domain.items():
        existing = merged_domain.setdefault(industry, [])
        for w in words:
            if w not in existing:
                existing.append(w)
    merged_function = list(word_bank.FUNCTION_WORDS)
    for w in dyn_function:
        if w not in merged_function:
            merged_function.append(w)
    retired = word_performance.load_retired_function_words(project_root)
    if retired:
        merged_function = [w for w in merged_function if w not in retired]
    return {industry: tuple(words) for industry, words in merged_domain.items()}, tuple(merged_function)


def _append_word_bank_expansion_rows(project_root: Path, new_rows: list[dict]) -> None:
    if not new_rows:
        return
    path = _word_bank_expansions_path(project_root)
    rows: list[dict] = []
    seen: set[tuple[str, str, str]] = set()

    def _key(row: dict) -> tuple[str, str, str]:
        return (row["type"], row["word"].strip().lower(), row.get("industry", "").strip().lower())

    if path.exists():
        with path.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                key = _key(row)
                if key not in seen:
                    seen.add(key)
                    rows.append(row)
    for row in new_rows:
        key = _key(row)
        if key in seen:
            continue
        seen.add(key)
        rows.append(row)

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=_EXPANSION_COLUMNS, lineterminator="\n", restval="")
    writer.writeheader()
    writer.writerows(rows)
    atomic_write_text(path, buffer.getvalue())


def _consume_word_bank_expansion(
    response: dict, run_id: str, when: str, *, retired: frozenset[str] | set[str] = frozenset()
) -> list[dict]:
    """판정 응답의 decisions(각 {type, word, industry?})를 검증해 유효한
    것만 반환한다 - 단일 Title Case 영단어, type은 domain/function, domain이면
    industry 필수. 형식이 안 맞는 제안은 조용히 버린다(예산 낭비 방지 목적의
    관대한 검증 - 나머지 review_titles 판정이 최종 필터 역할을 한다).

    2026-08-18 학습 루프: 은퇴 목록(`retired`)에 있는 기능어를 다시 제안하면
    버린다 - 실측 통과 0건이 확정된 단어의 재유입 방지."""
    rows = []
    for decision in response.get("decisions", []):
        word = str(decision.get("word", "")).strip()
        word_type = decision.get("type")
        industry = str(decision.get("industry", "")).strip()
        if word_type not in ("domain", "function"):
            continue
        if not word.isalpha() or word != word.capitalize():
            continue
        if word_type == "function" and word in retired:
            continue
        if word_type == "domain" and not industry:
            continue
        rows.append(
            {
                "type": word_type,
                "word": word,
                "industry": industry if word_type == "domain" else "",
                "added_at": when,
                "added_by_run_id": run_id,
                # 2026-08-31 강화 구조: 이 단어가 대표하는 승자 패턴 가설(자유
                # 태그). 세션이 안 남기면 빈 문자열 - 필수는 아니고, 태그가
                # 있어야 `word_performance.pattern_tag_performance`가 그
                # 가설의 실측 통과율을 집계할 수 있다.
                "pattern_tag": str(decision.get("pattern_tag", "")).strip(),
            }
        )
    return rows


_EXPAND_WORD_BANK_INSTRUCTIONS = (
    "[누적 노하우 - 반드시 먼저 읽을 것] 입력에 포함된 accumulated_learnings는 "
    "과거 라운드들의 시행착오를 현재 세션(들)이 memory/WORD_GENERATION_LEARNINGS.md에 "
    "직접 기록해 쌓아온 핵심 원칙이다. 각 원칙에는 candidate 또는 validated 표시가 "
    "있다 - validated 원칙은 반드시 지켜라. candidate 원칙(관측 1건뿐이거나 여러 "
    "변수가 동시에 바뀐 라운드로만 뒷받침됨)은 참고하되 맹신하지 말고, 가능하면 "
    "이번 제안이 그 원칙 하나만(다른 변수는 그대로 두고) 독립적으로 테스트하는 "
    "기회가 되도록 설계해서 교란을 풀어라. 이 라운드의 제안은 validated 원칙과 "
    "모순되지 않아야 한다 - 특히 과거에 실패로 확인된 패턴(예: 특정 업종 전문용어, "
    "특정 발명 단어 유형)을 반복하지 마라. 이번 라운드 결과가 나온 뒤(같은 실행 "
    "종료 시점) 현재 세션은 이번에 제안한 단어들과 그 결과(통과율 변화, 새로 은퇴된 "
    "단어 유무)를 memory/WORD_GENERATION_LEARNINGS.md의 라운드별 로그에 append하고, "
    "일반화 가능한 교훈이면 '핵심 원칙' 절도 갱신해야 한다(승격 조건을 충족했으면 "
    "candidate를 validated로 승격) - 이 기록이 다음 expand_word_bank 라운드에 다시 "
    "자동으로 주입된다. "
    "현재 단어뱅크(word_bank.py + 이미 제안된 확장분) 조합공간이 완전히 소진됐다 - "
    "영어 단어 자체가 부족한 게 아니라 손으로 고른 목록이 작아서다. 새 도메인어(업무 "
    "대상·문서·프로세스를 연상시키는 명사, 특정 업계 최소 20개 이상)와 새 기능어(업계에 "
    "무관하게 '이 도구가 무엇을 하는지' 연상시키는 동작·역할 명사, 최소 10개 이상)를 "
    "제안하라. 완전히 새로운 업계를 제안해도 좋다. Terminal/Ring처럼 특정 업계에서만 "
    "말이 되는 단어는 기능어로 제안하지 말 것(과거 실측으로 문제였음). "
    "[학습 루프 - 반드시 준수] 입력에 포함된 function_word_performance(누적 Keyword "
    "Planner 실측)를 먼저 읽어라: 새 기능어는 top_function_words의 패턴(Portal/Map/Hub처럼 "
    "사람들이 실제로 검색하는 구체적 장소·사물 명사)을 닮게 제안하고, "
    "retired_function_words(각 300회 이상 시도에 통과 0건으로 확정된 죽은 단어)와 그 "
    "패턴(Suite/Sync/Dashboard류 SaaS 전문용어풍 합성어)은 절대 제안하지 마라. "
    "[동의어 다양성 - 반드시 준수] 이번에 제안하는 기능어 목록 안에서 서로 뜻이 겹치는 "
    "동의어를 피하라(2026-08-19 실측 문제: Yard/Bay/Post/Outpost/Plaza/Harbor/Tower/"
    "Shelf/Locker/Booth/Kiosk를 한 번에 제안했더니 전부 '보관 장소'라는 같은 뜻이라 "
    "도메인어와 조합할 때마다 사실상 같은 문구가 11번 반복돼 AI 승인률이 21%로 급락함). "
    "제안하는 기능어들은 서로 다른 기능(추적/일정관리/문서보관/소통/분석 등)을 각각 "
    "대표해야 한다 - 한 기능당 비슷한 단어를 여러 개 넣지 말 것. "
    "[범용 결합력 - 반드시 준수, 동의어 다양성과는 별개 조건] 동의어가 아니어도 특정 "
    "의미 카테고리의 도메인어와만 자연스러운 기능어는 피하라(2026-08-19 실측: Inbox/"
    "Passport/Lobby/Bin/Line/Window/Ticker/Roll 10개를 서로 겹치지 않게 제안했지만 "
    "그 서브셋만의 승인률이 2.7%(112/4152)에 그침 - Inbox는 메시지·요청성 도메인어와만, "
    "Passport는 신원·자격증성 도메인어와만 자연스러워 나머지 도메인어 대다수와는 "
    "어색했음). Portal/Map/Hub/Tracker/Point/Station/Center/Register/Panel/Counter가 "
    "성공한 이유는 단어가 독특해서가 아니라 도메인어의 의미 카테고리에 관계없이 거의 "
    "모든 명사 뒤에 자연스럽게 붙는 범용 메타포이기 때문이다 - 새 기능어도 이 성질(특정 "
    "업계·특정 의미군에 국한되지 않고 폭넓게 결합됨)을 우선 고려해 제안하라. "
    "기존 word_bank.py와 이미 제안된 확장분(입력으로 함께 제공됨)과 겹치지 않게. "
    "[가설 태그 - 반드시 준수, 2026-08-31 강화 구조] 각 제안 단어에 pattern_tag를 붙여라 - "
    "개별 단어의 별명이 아니라 **재사용 가능한 전략 카테고리**여야 한다(예: "
    "\"specific_place_noun\", \"action_verb_noun\" - 이번에 제안하는 여러 단어가 같은 "
    "카테고리면 같은 태그를 공유해야 다음 라운드부터 pattern_tag_performance가 그 전략의 "
    "실측 통과율을 의미 있게 집계한다). 입력의 least_tried_pattern_tags는 아직 실측이 적어 "
    "검증이 덜 된 태그 목록이고, dead_pattern_tags는 **이미 반증돼 죽은 전략**이다(원 단어와 "
    "다른 단어를 골라도 같은 전략 방향이면 재제안하지 마라 - 예: dead_pattern_tags에 "
    "\"promo_incentive_noun\"이 있으면 그 계열의 새 단어를 또 시도하지 말 것). "
    "[2026-09-01 강화 구조 - 탐색 쿼터] 입력의 exploration_quota_pct(기본 30%) 이상의 "
    "제안은 pattern_tag_performance에 아직 없는(=한 번도 안 써본) 완전히 새로운 태그여야 "
    "한다 - 이미 검증된 태그만 우려먹으면 코드가 이 라운드를 거부하고 더 엄격한 지침으로 "
    "재요청한다(무한 재시도는 아니고 1회 한도). "
    "[2026-09-01 강화 구조 - 원칙 자체가 틀렸을 수 있다] accumulated_learnings의 validated "
    "원칙들도 이 문서 로그를 보면 여러 번 반증되며 재정의된 이력이 있다(예: '범용 결합력' "
    "원칙, '도메인어 단독 확장' 원칙 모두 한 번은 성공처럼 보였다가 다음 독립 라운드에서 "
    "뒤집혔다) - 지금 validated라고 표시된 것도 영구히 맞다고 가정하지 마라. 이번 제안 중 "
    "최소 1개는 의도적으로 현재 validated 원칙 중 하나와 반대 방향(대조 실험)으로 설계해서, "
    "그 원칙이 여전히 맞는지 다음 라운드 실측으로 확인할 수 있게 하라. "
    "각 항목을 "
    '{"type": "domain"|"function", "word": "Title Case 단일 영단어", "industry": '
    '"domain일 때만 필수, function이면 생략", "pattern_tag": "이 단어가 대표하는 재사용 '
    '가능한 전략 카테고리"} 형태로 응답하라.'
)

# 2026-09-01: expand_word_bank 응답이 형식(유효 제안 비율)이나 탐색 쿼터를
# 충족하지 못했을 때 재요청에 덧붙이는 보강 지침.
_EXPAND_WORD_BANK_RETRY_SUFFIX = (
    "\n\n[재요청 - 이전 응답 품질 미달] 이전 제안 중 {invalid_pct:.0f}%가 형식을 지키지 "
    "않았거나(단일 Title Case 영단어가 아님, industry 누락 등) 탐색 쿼터(최소 "
    "{quota_pct:.0f}%는 완전히 새로운 pattern_tag)를 충족하지 못했다. 이번엔 더 적은 개수를 "
    "제안하더라도 형식과 탐색 쿼터를 정확히 지켜라."
)


def _word_generation_learnings_path(project_root: Path) -> Path:
    return project_root / "memory" / "WORD_GENERATION_LEARNINGS.md"


def _load_word_generation_learnings_principles(project_root: Path) -> str:
    """`memory/WORD_GENERATION_LEARNINGS.md`의 "## 핵심 원칙" 섹션만 추출해 반환한다.

    2026-08-19 사용자 지시: 세션이 매번 이 문서를 "읽으려는 의지"에 기대지 않고,
    `expand_word_bank` 판정 요청을 만드는 이 코드가 매번 강제로 끼워 넣는다 -
    `function_word_performance`와 동일한 패턴(구조적 전달, 세션의 선택 사항이 아님).
    전체 문서(라운드별 로그 포함)를 매번 넣으면 로그가 쌓일수록 요청이 무한정
    커지므로, "지금 유효한 원칙" 요약만 담는 이 섹션만 추출한다. 파일이 없거나
    섹션이 없으면(아직 아무것도 기록되지 않았으면) 빈 문자열."""
    path = _word_generation_learnings_path(project_root)
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    # 줄 시작(^)에 오는 실제 헤딩만 매칭 - 본문 설명 중 백틱 안에 같은 문자열이
    # 그대로 등장해도(예: "`## 핵심 원칙` 섹션은...") 오매칭되지 않도록 함
    # (2026-08-19 실측으로 발견된 버그: 단순 문자열 탐색은 첫 등장 위치인 설명
    # 문단을 헤딩으로 착각했다).
    match = re.search(r"^## 핵심 원칙\s*\n", text, flags=re.MULTILINE)
    if match is None:
        return ""
    start = match.end()
    next_match = re.search(r"^## ", text[start:], flags=re.MULTILINE)
    section = text[start : start + next_match.start()] if next_match else text[start:]
    return section.strip()


def _write_expand_word_bank_request(
    project_root: Path, run_dir: Path, state: run_state.RunState, *, round_no: int = 1, extra_instructions: str = ""
) -> Path:
    existing_domain, existing_function = _merged_word_bank(project_root)
    expansion_rows = _load_word_bank_expansion_rows(project_root)
    cache_rows = word_performance.load_cache_rows(project_root)
    cfg = config.load_judgment_quality_config(project_root)
    items = [
        {"industry": industry, "existing_domain_words": list(words)}
        for industry, words in existing_domain.items()
    ] + [
        {"existing_function_words": list(existing_function)},
        {"function_word_performance": word_performance.performance_summary_for_expansion(project_root)},
        {"accumulated_learnings": _load_word_generation_learnings_principles(project_root)},
        # 2026-08-31/09-01 강화 구조: 가설(pattern_tag)-검증 루프 + 탐색-활용 균형 +
        # 죽은 전략(카테고리 단위 은퇴) + 탐색 쿼터.
        {"pattern_tag_performance": word_performance.pattern_tag_performance(expansion_rows, cache_rows)},
        {"least_tried_pattern_tags": word_performance.least_tried_pattern_tags(expansion_rows, cache_rows)},
        {"dead_pattern_tags": word_performance.dead_pattern_tags(expansion_rows, cache_rows)},
        {"exploration_quota_pct": cfg["exploration_quota_pct"] * 100},
    ]
    return judgment.write_request(
        run_dir,
        "expand_word_bank",
        state.run_id,
        _EXPAND_WORD_BANK_INSTRUCTIONS + extra_instructions,
        items,
        round_no=round_no,
        generated_at=ids.now_kst().isoformat(),
    )


# ---------------------------------------------------------------------------
# Stage: generate_and_review_titles - "한 번의 CLI 실행 = 한 라운드"(2026-08-18
# 전환). backlog(load_state에서 적재) + 이번에 새로 생성/판정한 승인분을 합쳐
# Keyword Planner 게이트에 태우고 끝난다. 더 이상 target_count를 추격하는
# 다중 라운드 루프가 없다 - 더 하고 싶으면 다시 실행(새 run 또는 --resume).
# 조합공간이 소진되면 즉시 포기하지 않고, 자가확장(위 섹션) 판정을 한 번 거친
# 뒤에도 여전히 신규 후보가 없을 때만 진짜 CAPABILITY_STAGNATION으로 처리한다.
# ---------------------------------------------------------------------------


def _review_titles_few_shot_examples(project_root: Path, *, n: int = 3) -> str:
    """ledger에서 실제 승인/거절 사례 몇 개를 뽑아 판정 지침에 구체적 예시로
    붙인다(2026-08-31 강화 구조) - 저지능 모델은 추상적 규칙 설명보다 구체적
    사례의 패턴매칭에서 더 정확하다."""
    ledger = _load_generated_ledger(project_root)
    approved: list[dict] = []
    rejected: list[dict] = []
    for row in ledger.values():
        if len(approved) >= n and len(rejected) >= n:
            break
        if row.get("ai_approved") == "True" and len(approved) < n:
            approved.append(row)
        elif row.get("ai_approved") == "False" and row.get("ai_reason") and len(rejected) < n:
            rejected.append(row)
    if not approved and not rejected:
        return ""
    lines = ["", "[참고 사례 - 과거 실제 판정]"]
    for row in approved:
        lines.append(f'- 승인: "{row["title"]}" (업계: {row.get("industry", "")})')
    for row in rejected:
        lines.append(f'- 거절: "{row["title"]}" - 사유: {row.get("ai_reason", "")}')
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 저지능 모델 호환 강화 구조 (2026-08-31, 사용자 지시) - 판단은 여전히 전량
# AI가 하되(코드로 판단을 떠넘기지 않는다), 판단 오류 확률이 높은 신호를 코드가
# 감지해 같은 라운드 안에서 자동으로 AI 재검증(레드팀)을 트리거한다. 사람에게
# 넘기지 않는다. 트리거 신호 셋:
#   ① 골든셋 카나리아(config/golden_set.csv) 불일치 - 판정 기준 자체가 흔들렸다는
#      직접 증거.
#   ② 판정 응답의 confidence가 낮은 승인 - 판정자 스스로 신고한 불확실성.
#   ③ 이번 라운드 AI 승인율이 과거 대비 통계적 극단치(승인율 이상탐지) -
#      간접 신호라 z_threshold를 넉넉히 잡아 오탐을 줄인다.
# 셋 중 하나라도 걸리면 이번 라운드의 '승인' 판정들만(거절은 이미 확정) 별도
# 판정 라운드(review_titles_recheck)에서 다시 검토시키고, 그 결과가 최종
# ai_approved로 ledger에 반영된다. 상세 배경은
# docs/design/15-continuous-word-quality-improvement.md 참고.
# ---------------------------------------------------------------------------

_REVIEW_TITLES_RECHECK_INSTRUCTIONS = (
    "아래 후보들은 1차 판정에서 이미 approve=true를 받았다. 당신의 역할은 그 판정에 "
    "동의하는 게 아니라 반박(refute)을 시도하는 것이다 - 명확성·의미중복·상표유사 "
    "세 기준을 다시 처음부터 독립적으로 적용하고, 1차 판정이 놓쳤을 만한 결함을 "
    "적극적으로 찾아라. 결함을 찾지 못하면(정말로 반박할 근거가 없으면)만 approve=true를 "
    "유지하고, 조금이라도 근거 있는 의심이 들면 approve=false로 뒤집고 reason에 무엇을 "
    "반박했는지 남겨라. original_reason 필드는 1차 판정자가 남긴 근거(있다면)이니 그것도 "
    "비판적으로 검토하라."
)


# ---------------------------------------------------------------------------
# 저지능 모델 호환 강화 구조 2단계 (2026-09-01, 사용자 지시) - "판단이 아니라
# 형식·절차 자체를 못 따라간" 경우를 코드가 기계적으로 걸러서, 그 상태로는
# 절대 다음 스테이지로 넘어가지 못하게 한다. 판단 자체(코드가 대신 판정)가
# 아니라 구조 검증(응답이 요청한 스키마를 지켰는가)만 code가 전담한다(§5).
# ---------------------------------------------------------------------------


def _load_judgment_quality_config(project_root: Path) -> dict:
    return config.load_judgment_quality_config(project_root)


def _validate_review_decisions(items: list[dict], decisions: list[dict]) -> tuple[dict[str, dict], list[tuple[str | None, str]]]:
    """`items`(요청에 보낸 후보 목록)에 대한 `decisions`(응답)가 구조적으로
    온전한지 검사한다. 반환: (title -> 유효한 decision dict, [(title_or_None, 결함사유)]).

    판단(approve가 맞았는지)은 검사하지 않는다 - 오직 "응답이 요청한 스키마를
    지켰는가"만 본다: 모든 항목에 결정이 있는가·중복 없는가·title이 실제
    후보와 일치하는가·approve가 boolean인가·confidence가 0.0~1.0인가·거절이면
    reason이 있는가·(있다면) checks 필드가 approve와 논리적으로 앞뒤가
    맞는가. 하나라도 어긋나면 그 항목은 "구조 결함"으로 분류돼 이후
    (재요청 또는 안전 기본값 자동거절) 처리 대상이 된다."""
    item_titles = {it["title"] for it in items}
    accepted: dict[str, dict] = {}
    malformed: list[tuple[str | None, str]] = []
    seen: set[str] = set()

    for decision in decisions:
        title = decision.get("title")
        if not isinstance(title, str) or title not in item_titles:
            malformed.append((title if isinstance(title, str) else None, "unknown_or_missing_title"))
            continue
        if title in seen:
            malformed.append((title, "duplicate_decision"))
            continue
        approve = decision.get("approve")
        if not isinstance(approve, bool):
            malformed.append((title, "approve_not_boolean"))
            continue
        confidence = decision.get("confidence")
        if confidence is not None and not (isinstance(confidence, (int, float)) and 0.0 <= confidence <= 1.0):
            malformed.append((title, "confidence_out_of_range"))
            continue
        if not approve and not str(decision.get("reason", "")).strip():
            malformed.append((title, "missing_reason_for_rejection"))
            continue
        checks = decision.get("checks")
        if isinstance(checks, dict) and {"clarity", "duplication", "trademark"} <= checks.keys():
            all_pass = all(bool(checks[k]) for k in ("clarity", "duplication", "trademark"))
            if approve and not all_pass:
                malformed.append((title, "checks_inconsistent_with_approve_true"))
                continue
            if not approve and all_pass:
                malformed.append((title, "checks_inconsistent_with_approve_false"))
                continue
        seen.add(title)
        accepted[title] = decision

    for missing_title in item_titles - seen:
        if missing_title not in {t for t, _ in malformed}:
            malformed.append((missing_title, "no_decision_for_item"))

    return accepted, malformed


_STRUCTURAL_RETRY_NOTE = (
    "\n\n[재요청 - 이전 응답 구조 결함] 이전 응답의 항목 중 상당수({invalid_pct:.0f}%)가 "
    "형식을 지키지 않았다(제목 불일치, approve가 boolean이 아님, confidence 범위 이탈, "
    "거절인데 reason 누락, checks와 approve 불일치 등). 이번엔 아래 스키마를 정확히 지켜라: "
    '{{"title": "요청에 있던 제목 그대로", "approve": true|false, "confidence": 0.0~1.0, '
    '"reason": "거절 시 필수"}}. 모든 항목에 정확히 하나씩 답하고, 같은 제목을 두 번 "'
    "답하지 마라."
)


def _process_review_chunk(
    project_root: Path, run_dir: Path, state: run_state.RunState, stage_name: str, chunk_items: list[dict], instructions: str
) -> dict[str, dict]:
    """review_titles 배치를 청크 단위로 판정시키고, 구조 결함이 과도하면(코드가
    기계적으로 판정) 같은 청크를 더 엄격한 지침으로 1회 재요청한다 - 판단 자체는
    항상 AI가 하고, 코드는 "응답 형식이 온전한가"만 게이트로 사용한다(§5)."""
    cfg = _load_judgment_quality_config(project_root)
    retry_max = cfg["structural_retry_max"]
    invalid_threshold = cfg["structural_invalid_ratio_for_full_retry"]

    attempts = state.context.setdefault("review_attempts", {})
    round_no = attempts.get(stage_name, 1)

    if not judgment.has_response(run_dir, stage_name, round_no):
        request_path = judgment.write_request(
            run_dir, stage_name, state.run_id, instructions, chunk_items,
            round_no=round_no, generated_at=ids.now_kst().isoformat(),
        )
        _pause_for_judgment(project_root, state, stage_name, request_path)

    response = judgment.read_response(run_dir, stage_name, round_no)
    accepted, malformed = _validate_review_decisions(chunk_items, response["decisions"])
    invalid_ratio = (len(malformed) / len(chunk_items)) if chunk_items else 0.0

    if invalid_ratio > invalid_threshold and round_no <= retry_max:
        attempts[stage_name] = round_no + 1
        state.context["review_attempts"] = attempts
        retry_instructions = instructions + _STRUCTURAL_RETRY_NOTE.format(invalid_pct=invalid_ratio * 100)
        request_path = judgment.write_request(
            run_dir, stage_name, state.run_id, retry_instructions, chunk_items,
            round_no=round_no + 1, generated_at=ids.now_kst().isoformat(),
        )
        _pause_for_judgment(project_root, state, stage_name, request_path)

    # 재시도 한도 도달 또는 결함률이 임계 이하 - 남은 개별 결함은 안전
    # 기본값(자동 거절)으로 확정하고 계속 진행한다(무한 대기 금지).
    for title, reason in malformed:
        if title and title not in accepted:
            accepted[title] = {
                "title": title,
                "approve": False,
                "reason": f"structural_validation_failed: {reason}",
            }
    return accepted


_PRINCIPLE_REVERIFICATION_INSTRUCTIONS = (
    "입력의 accumulated_learnings에 있는 '핵심 원칙' 각각(특히 validated 표시된 것)에 "
    "대해 반박을 시도하라 - 지금까지 맞았다고 동의하는 게 목적이 아니라, 이 원칙이 여전히 "
    "유효한지 의심하는 게 목적이다. 각 원칙에 대해 decisions 배열의 한 항목으로 "
    '{"title": "원칙을 한 문장으로 요약(추적용, 자유 서술)", "approve": true(여전히 유효)|'
    'false(반증/재검증 필요), "reason": "판단 근거", "confidence": 0.0~1.0} 형태로 응답하라. '
    "이 응답은 ledger나 산출물에 반영되지 않는다 - 다음 세션이 memory/"
    "WORD_GENERATION_LEARNINGS.md의 '핵심 원칙' 절을 갱신할 때 참고할 별도 보고서로만 "
    "저장된다."
)


def _principle_reverification_report_path(project_root: Path, run_id: str) -> Path:
    return project_root / "output" / "_pipeline" / "analysis" / f"principle_reverification_{run_id}.json"


def _maybe_trigger_principle_reverification(project_root: Path, run_dir: Path, state: run_state.RunState) -> None:
    """N라운드마다 한 번(기본 10), 지금까지 쌓인 '핵심 원칙'을 전담 반박 역할로
    재검증하는 판정을 강제로 연다(2026-09-01) - `principle_refresh_reminder`가
    콘솔에 권고만 하던 것을 실제 판정 게이트로 격상한 것. 응답은 코드가 결론을
    대신 반영하지 않고 보고서 파일로만 저장한다 - '핵심 원칙' 문서 갱신은 여전히
    세션의 해석 몫이다(§5)."""
    cfg = _load_judgment_quality_config(project_root)
    every_n = cfg["principle_reverification_every_n_rounds"]
    if every_n <= 0:
        return

    upcoming_round_number = len(word_performance.load_round_history(project_root)) + 1
    if upcoming_round_number % every_n != 0:
        return
    if state.context.get("principle_reverification_done_for_round") == upcoming_round_number:
        return

    stage = "principle_reverification"
    if judgment.has_response(run_dir, stage, 1):
        response = judgment.read_response(run_dir, stage, 1)
        atomic_write_text(
            _principle_reverification_report_path(project_root, state.run_id),
            json.dumps(response, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        )
        state.context["principle_reverification_done_for_round"] = upcoming_round_number
        return

    principles = _load_word_generation_learnings_principles(project_root)
    if not principles:
        state.context["principle_reverification_done_for_round"] = upcoming_round_number
        return

    request_path = judgment.write_request(
        run_dir, stage, state.run_id, _PRINCIPLE_REVERIFICATION_INSTRUCTIONS,
        [{"accumulated_learnings": principles}], round_no=1, generated_at=ids.now_kst().isoformat(),
    )
    _pause_for_judgment(project_root, state, stage, request_path)


def _process_expand_word_bank_response(project_root: Path, run_dir: Path, state: run_state.RunState) -> None:
    """expand_word_bank 응답을 소비하기 전에 두 가지 객관 지표를 코드가 검사한다
    (2026-09-01): ① 유효 제안 비율(형식을 지킨 제안/전체 제안) ② 탐색 쿼터(새
    pattern_tag 비율). 둘 다 판단이 아니라 순수 집계라 코드 역할(§5)이다. 미달이면
    1회 한도로 더 엄격한 지침으로 재요청하고, 그래도 미달이면 있는 그대로
    받아들이고 계속 진행한다(무한 재시도 금지)."""
    cfg = _load_judgment_quality_config(project_root)
    round_no = state.context.get("expand_word_bank_round_no", 1)
    response = judgment.read_response(run_dir, "expand_word_bank", round_no)

    retired = word_performance.load_retired_function_words(project_root)
    new_rows = _consume_word_bank_expansion(response, state.run_id, ids.now_kst().isoformat(), retired=retired)

    total_proposed = len(response.get("decisions", []))
    if total_proposed == 0:
        # 아예 제안이 없는 것은 "형식을 못 지킨 것"이 아니라 세션이 정직하게
        # "제안할 게 없다"고 답한 정상 케이스일 수 있다(예: QA 테스트, 정말로
        # 소진). 품질 게이트 대상이 아니다 - 그대로 진행하면 candidates가 계속
        # 비어 CAPABILITY_STAGNATION으로 정직하게 끝난다.
        _append_word_bank_expansion_rows(project_root, new_rows)
        return

    valid_ratio = len(new_rows) / total_proposed

    expansion_rows = _load_word_bank_expansion_rows(project_root)
    cache_rows = word_performance.load_cache_rows(project_root)
    already_tried_tags = set(word_performance.pattern_tag_performance(expansion_rows, cache_rows).keys())
    tagged_rows = [r for r in new_rows if r.get("pattern_tag")]
    new_tag_ratio = (
        sum(1 for r in tagged_rows if r["pattern_tag"] not in already_tried_tags) / len(tagged_rows)
        if tagged_rows
        else 1.0  # 태그가 아예 없으면 탐색 쿼터를 판단할 근거가 없다 - 유효 비율 게이트가 이미 걸러줌
    )

    quality_ok = valid_ratio >= cfg["expand_word_bank_min_valid_ratio"] and new_tag_ratio >= cfg["exploration_quota_pct"]
    retry_count = state.context.get("expand_word_bank_quality_retries", 0)

    if not quality_ok and retry_count < cfg["expand_word_bank_retry_max"]:
        state.context["expand_word_bank_quality_retries"] = retry_count + 1
        new_round_no = round_no + 1
        state.context["expand_word_bank_round_no"] = new_round_no
        invalid_pct = (1.0 - valid_ratio) * 100
        extra = _EXPAND_WORD_BANK_RETRY_SUFFIX.format(
            invalid_pct=invalid_pct, quota_pct=cfg["exploration_quota_pct"] * 100
        )
        request_path = _write_expand_word_bank_request(
            project_root, run_dir, state, round_no=new_round_no, extra_instructions=extra
        )
        _pause_for_judgment(project_root, state, "expand_word_bank", request_path)

    _append_word_bank_expansion_rows(project_root, new_rows)


def _review_titles_instructions(project_root: Path) -> str:
    return (
        "각 후보를 아래 세 기준으로 각각 독립적으로 평가한 뒤 종합하라(하나로 뭉뚱그려 "
        "판단하지 말 것 - 복합판단에서는 항목을 놓치기 쉽다):\n"
        "1) 명확성: 어떤 SaaS인지 짐작 가능한가\n"
        "2) 의미 중복: 이번 배치의 다른 후보와 뜻이 겹치는가\n"
        "3) 상표 유사: 유명 서비스·브랜드와 동일/유사한가\n"
        "세 기준 중 하나라도 실패하면 approve=false로 판정하고 reason에 어떤 기준을 왜 "
        "실패했는지 남겨라. 모두 통과하면 approve=true. [2026-08-31 강화 구조 - 반드시 "
        "포함] 각 판정에 스스로 이 판단이 얼마나 확실한지 0.0~1.0 사이 confidence를 반드시 "
        "포함하라 - 애매하거나 근거가 약하면 낮게 매겨라(낮은 confidence는 자동으로 별도 "
        "재검증 라운드에 회부되므로 정직하게 매기는 편이 유리하다). [2026-09-01 강화 구조 - "
        "권장] 가능하면 각 판정에 checks 필드도 포함하라: "
        '{"clarity": true|false, "duplication": true|false, "trademark": true|false} - '
        "세 값이 모두 true일 때만 approve=true여야 하고, 하나라도 false면 approve=false여야 "
        "한다(이 논리가 어긋나면 코드가 구조 결함으로 보고 재검증에 회부한다). 이 배치에는 "
        "판정 품질을 확인하기 위한 고정 정답 카나리아 후보가 실제 후보와 형식상 구분 없이 "
        "섞여 있다 - 어떤 항목이 카나리아인지 추측하거나 다르게 취급하려 하지 말고 모든 "
        "항목을 동일한 기준으로 판정하라. industry 필드는 참고용 맥락이다."
        + _review_titles_few_shot_examples(project_root)
    )


def _stage_generate_and_review_titles(project_root: Path, options: RunOptions, state: run_state.RunState) -> None:
    run_dir = _run_dir(project_root, state)
    backlog = state.context.get("backlog", [])

    # 2026-09-01 강화 구조: N라운드마다 지금까지의 '핵심 원칙'을 반박 전담으로
    # 재검증하는 판정을 강제로 연다 - 매 호출마다 확인하되, 이번 라운드에 이미
    # 처리됐으면 즉시 no-op이다.
    _maybe_trigger_principle_reverification(project_root, run_dir, state)

    if "review_all_items" not in state.context:
        excluded = _excluded_normalized(project_root, state)
        round_size = options.round_size or DEFAULT_ROUND_SIZE[options.mode]
        domain_words, function_words = _merged_word_bank(project_root)
        candidates = word_generation.generate_combinations(
            round_size, exclude=excluded, domain_words=domain_words, function_words=function_words
        )

        if not candidates:
            expand_stage = "expand_word_bank"
            expand_round_no = state.context.get("expand_word_bank_round_no", 1)
            if judgment.has_response(run_dir, expand_stage, expand_round_no):
                _process_expand_word_bank_response(project_root, run_dir, state)
                domain_words, function_words = _merged_word_bank(project_root)
                candidates = word_generation.generate_combinations(
                    round_size, exclude=excluded, domain_words=domain_words, function_words=function_words
                )
            elif not state.context.get("word_bank_expansion_attempted"):
                state.context["word_bank_expansion_attempted"] = True
                expand_request_path = _write_expand_word_bank_request(project_root, run_dir, state)
                _pause_for_judgment(project_root, state, expand_stage, expand_request_path)

        if not candidates:
            if not backlog:
                state.status = "CAPABILITY_STAGNATION"
                run_state.save(project_root, state)
                raise RetryRequired(
                    "word bank exhausted even after a self-expansion attempt - "
                    "no new combinations and no pending backlog",
                    status="CAPABILITY_STAGNATION",
                )
            try:
                approved = _apply_keyword_metrics_filter(project_root, state, backlog)
            except (KeywordMetricsCredentialsError, KeywordMetricsBudgetExceeded) as exc:
                state.status = "RETRYING"
                run_state.save(project_root, state)
                raise RetryRequired(f"keyword metrics filter unavailable: {exc}", status="RETRYING")
            state.context["approved"] = approved
            state.context["round_stats"] = {
                "generated": 0,
                "ai_approved": 0,
                "backlog_carried": len(backlog),
                "kp_passed": len(approved),
            }
            state.status = "DONE"
            run_state.save(project_root, state)
            return

        candidate_industry = state.context.setdefault("candidate_industry", {})
        for item in candidates:
            candidate_industry[item["title"]] = item["industry"]
        state.context["candidate_industry"] = candidate_industry

        golden = word_performance.load_golden_set(project_root)
        canary_items = [{"title": row["title"], "industry": "canary"} for row in golden.values()]
        state.context["review_all_items"] = canary_items + [
            {"title": c["title"], "industry": c["industry"]} for c in candidates
        ]
        state.context["review_chunk_index"] = 0
        state.context["review_chunk_decisions"] = {}
        run_state.save(project_root, state)

    # ------------------------------------------------------------------
    # 2026-09-01 강화 구조: 배치를 청크로 쪼개 순차 판정한다(기본 청크 크기는
    # 커서 QA 기본 규모에선 청크 1개=기존 동작과 동일 - 지능이 더 낮은 모델을
    # 붙였다면 config/judgment_quality.yaml의 chunk_size를 낮춰서 실제로
    # 쪼개지게 한다). 각 청크는 구조 검증(_process_review_chunk)을 통과해야만
    # 다음 청크로 넘어간다 - 통과 못 하면 그 청크에서 재요청하며 멈춘다.
    # ------------------------------------------------------------------
    all_items = state.context["review_all_items"]
    cfg = _load_judgment_quality_config(project_root)
    chunk_size = max(1, cfg["review_titles_chunk_size"])
    chunks = [all_items[i : i + chunk_size] for i in range(0, len(all_items), chunk_size)]
    decisions_by_title: dict[str, dict] = state.context.setdefault("review_chunk_decisions", {})
    chunk_index = state.context.get("review_chunk_index", 0)
    review_instructions = _review_titles_instructions(project_root)

    while chunk_index < len(chunks):
        stage_name = "review_titles" if chunk_index == 0 else f"review_titles_chunk{chunk_index}"
        accepted = _process_review_chunk(project_root, run_dir, state, stage_name, chunks[chunk_index], review_instructions)
        decisions_by_title.update(accepted)
        chunk_index += 1
        state.context["review_chunk_decisions"] = decisions_by_title
        state.context["review_chunk_index"] = chunk_index
        run_state.save(project_root, state)

    candidate_industry = state.context.get("candidate_industry", {})
    judged_at = ids.now_kst().isoformat()

    golden = word_performance.load_golden_set(project_root)
    real_decisions = []
    canary_decisions = []
    for decision in decisions_by_title.values():
        if normalize_title(decision.get("title", "")) in golden:
            canary_decisions.append(decision)
        else:
            real_decisions.append(decision)
    golden_eval = word_performance.evaluate_golden_set(canary_decisions, golden)

    ledger_rows: list[dict] = []
    pending_approved: list[dict] = []
    low_confidence_titles: list[str] = []
    for decision in real_decisions:
        title = decision["title"]
        approve = bool(decision.get("approve"))
        confidence = decision.get("confidence")
        if approve:
            pending_approved.append(
                {
                    "title": title,
                    "industry": candidate_industry.get(title, ""),
                    "original_reason": decision.get("reason", ""),
                }
            )
            if isinstance(confidence, (int, float)) and confidence < CONFIDENCE_RECHECK_THRESHOLD:
                low_confidence_titles.append(title)
        else:
            ledger_rows.append(
                {
                    "title": title,
                    "industry": candidate_industry.get(title, ""),
                    "ai_approved": "False",
                    "ai_reason": decision.get("reason", ""),
                    "judged_at": judged_at,
                }
            )

    approval_anomaly = word_performance.detect_approval_rate_anomaly(
        word_performance.load_round_history(project_root),
        generated=len(real_decisions),
        ai_approved=len(pending_approved),
    )
    needs_recheck = (
        bool(golden_eval["mismatches"])
        or bool(low_confidence_titles)
        or approval_anomaly["status"] in ("anomalous_high", "anomalous_low")
    )

    recheck_stage = "review_titles_recheck"
    if needs_recheck and pending_approved:
        if judgment.has_response(run_dir, recheck_stage, 1):
            recheck_response = judgment.read_response(run_dir, recheck_stage, 1)
            recheck_by_title = {d["title"]: d for d in recheck_response["decisions"]}
            fresh_approved = []
            for item in pending_approved:
                verdict = recheck_by_title.get(item["title"])
                survived = bool(verdict.get("approve")) if verdict else False
                reason = ""
                if not survived:
                    refute_reason = verdict.get("reason", "") if verdict else "no_recheck_response"
                    reason = f"redteam_recheck_rejected: {refute_reason}"
                ledger_rows.append(
                    {
                        "title": item["title"],
                        "industry": item["industry"],
                        "ai_approved": str(survived),
                        "ai_reason": reason,
                        "judged_at": judged_at,
                    }
                )
                if survived:
                    fresh_approved.append({"title": item["title"], "industry": item["industry"]})
        else:
            recheck_items = [
                {"title": c["title"], "industry": c["industry"], "original_reason": c["original_reason"]}
                for c in pending_approved
            ]
            request_path = judgment.write_request(
                run_dir, recheck_stage, state.run_id, _REVIEW_TITLES_RECHECK_INSTRUCTIONS, recheck_items,
                round_no=1, generated_at=ids.now_kst().isoformat(),
            )
            _pause_for_judgment(project_root, state, recheck_stage, request_path)
    else:
        fresh_approved = [{"title": c["title"], "industry": c["industry"]} for c in pending_approved]
        for c in pending_approved:
            ledger_rows.append(
                {
                    "title": c["title"],
                    "industry": c["industry"],
                    "ai_approved": "True",
                    "ai_reason": "",
                    "judged_at": judged_at,
                }
            )

    _append_generated_ledger_rows(project_root, ledger_rows)
    _export_generated_ledger_snapshot(project_root, ids.now_kst())

    combined = backlog + fresh_approved
    try:
        approved = _apply_keyword_metrics_filter(project_root, state, combined)
    except (KeywordMetricsCredentialsError, KeywordMetricsBudgetExceeded) as exc:
        state.status = "RETRYING"
        run_state.save(project_root, state)
        raise RetryRequired(f"keyword metrics filter unavailable: {exc}", status="RETRYING")
    finally:
        # 판정/API 조회 후 모든 스냅샷 생성 - 명시적 호출로 누락 방지
        _export_final_words_and_history_snapshots(project_root, ids.now_kst())
        # 학습 루프: 매 라운드 성과 리포트 자동 갱신(캐시 없으면 no-op)
        word_performance.write_report(project_root, ids.now_kst())
    state.context["approved"] = approved
    state.context["round_stats"] = {
        "generated": len(real_decisions),
        "ai_approved": len(fresh_approved),
        "backlog_carried": len(backlog),
        "kp_passed": len(approved),
    }
    # 2026-08-31 강화 구조: 이번 라운드의 판정 품질 신호를 체크포인트
    # 단계(HANDOFF)에서도 보이도록 상태에 남긴다.
    state.context["golden_eval"] = golden_eval
    state.context["approval_anomaly"] = approval_anomaly
    state.status = "DONE"
    run_state.save(project_root, state)


# ---------------------------------------------------------------------------
# Stage: update_memory_and_git_checkpoint
# ---------------------------------------------------------------------------


def _stage_update_memory_and_git_checkpoint(project_root: Path, options: RunOptions, state: run_state.RunState) -> None:
    # 이 스테이지에 도달했다는 것 자체가 generate_and_review_titles가 예외
    # 없이 끝났다는 뜻이다(RetryRequired/CAPABILITY_STAGNATION은 그 안에서
    # 즉시 예외로 전파되어 여기까지 오지 않는다) - 그래서 state.status를
    # 다시 읽지 않고(run_pipeline의 스테이지 루프가 각 스테이지 성공 후
    # "RUNNING"으로 되돌려놓으므로 신뢰할 수 없다) 항상 DONE으로 기록한다.
    stats = state.context.get("round_stats", {})
    approved = state.context.get("approved", [])

    # 학습 정체 점검(2026-08-19, 사용자 지시): 이 스테이지가 라운드 완료를
    # 확정하는 유일한 지점이므로 여기서 정확히 한 번 이력에 기록한다.
    word_performance.append_round_history(
        project_root, state.run_id, state.mode, ids.now_kst().isoformat(), stats
    )
    history = word_performance.load_round_history(project_root)
    stagnation = word_performance.detect_stagnation(history)
    stagnation_line = word_performance.format_stagnation_message(stagnation)
    print(stagnation_line)

    # 저지능 모델 호환 강화 구조(2026-08-31): 이번 라운드의 판정 품질 안전망
    # 신호(골든셋 카나리아 일치율, 승인율 이상탐지)를 정체 점검과 같은 방식으로
    # 콘솔·HANDOFF에 남긴다 - 순수 수치 보고이고 원인 해석은 세션의 몫이다(§5).
    golden_line = word_performance.format_golden_set_message(state.context.get("golden_eval") or {})
    anomaly_line = word_performance.format_approval_anomaly_message(
        state.context.get("approval_anomaly") or {"status": "insufficient_data"}
    )
    print(golden_line)
    print(anomaly_line)

    principle_reminder = word_performance.principle_refresh_reminder(len(history))
    if principle_reminder:
        print(principle_reminder)

    handoff_lines = [
        "# HANDOFF",
        "",
        "- 상태: `DONE`",
        "- 현재 단계: update_memory_and_git_checkpoint (word_pipeline)",
        f"- 마지막 실행: run {state.run_id} (mode={state.mode})",
        f"- 이번 라운드: 신규생성 {stats.get('generated', 0)}개, "
        f"AI승인 {stats.get('ai_approved', 0)}개, "
        f"backlog반영 {stats.get('backlog_carried', 0)}개, "
        f"Keyword Planner통과 {stats.get('kp_passed', len(approved))}개",
        f"- {stagnation_line}",
        f"- {golden_line}",
        f"- {anomaly_line}",
    ]
    if principle_reminder:
        handoff_lines.append(f"- {principle_reminder}")
    handoff_lines.append("- 다음 원자 작업: 필요하면 다시 실행(같은 run_id --resume 또는 새 run)")

    atomic_write_text(
        project_root / "memory" / "HANDOFF.md",
        "\n".join(handoff_lines) + "\n",
    )
    _run_or_raise(project_root, "git_checkpoint.py", "--message", f"chore: word pipeline checkpoint for {state.run_id}")


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

_STAGE_HANDLERS = {
    "load_state": _stage_load_state,
    "generate_and_review_titles": _stage_generate_and_review_titles,
    "update_memory_and_git_checkpoint": _stage_update_memory_and_git_checkpoint,
}


def _load_or_create_state(options: RunOptions) -> run_state.RunState:
    project_root = options.project_root
    now = ids.now_kst()

    if options.resume:
        run_id = options.run_id or run_state.latest_run_id(project_root, options.mode)
        if run_id is None:
            raise ValueError(f"--resume given but no existing {options.mode} run was found")
        state = run_state.load(project_root, run_id)
        if state.mode != options.mode:
            raise ValueError(f"run {run_id} was started as mode={state.mode}; --mode {options.mode} does not match")
        return state

    run_id = options.run_id or ids.format_run_id(options.mode, now)
    if run_state.exists(project_root, run_id):
        raise ValueError(f"run {run_id} already exists; pass --resume to continue it")
    return run_state.RunState(
        run_id=run_id,
        mode=options.mode,
        status="RUNNING",
        stage=STAGES[0],
        created_at=now.isoformat(),
        updated_at=now.isoformat(),
        context={},
    )


def run_pipeline(options: RunOptions) -> int:
    options.validate()
    project_root = options.project_root
    state = _load_or_create_state(options)
    run_state.save(project_root, state)

    stage_index = STAGES.index(state.stage)
    for stage in STAGES[stage_index:]:
        state.stage = stage
        state.awaiting_judgment = None
        handler = _STAGE_HANDLERS.get(stage)
        if handler is None:
            raise ImplementationPendingError(f"no handler registered for stage: {stage}")
        try:
            handler(project_root, options, state)
        except (JudgmentRequired, RetryRequired, RecoveryRequired):
            raise
        except Exception as exc:
            state.status = "FAILED"
            state.updated_at = ids.now_kst().isoformat()
            run_state.save(project_root, state)
            raise RuntimeError(f"stage '{stage}' failed: {exc}") from exc
        state.status = "RUNNING"
        state.updated_at = ids.now_kst().isoformat()
        run_state.save(project_root, state)

    state.status = "DONE"
    state.updated_at = ids.now_kst().isoformat()
    run_state.save(project_root, state)
    return 0
