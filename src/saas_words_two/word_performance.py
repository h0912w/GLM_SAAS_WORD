"""단어 성과 분석·학습 루프 (2026-08-18, 사용자 지시).

10,000개 라운드에서 Keyword Planner 통과가 12개(0.12%)에 그친 것을 계기로,
누적 캐시(문서②)의 실측 통과/탈락 데이터를 매 라운드 분석해 다음 생성에
반영하는 구조를 도입했다. 실측 분석(2026-08-18, 30,263건 기준) 요지:

- 기능어가 승부를 결정한다: Portal 5.85%/Map 5.68% vs. Suite/Sync/Dashboard/
  Toolkit/Workbench 등 28개 기능어는 각 300회+ 시도에 통과 0건.
- 그 28개 죽은 기능어에 전체 API 조회의 32%(9,797회)가 낭비됐다.
- 패턴: 사람들이 실제로 검색하는 구체적 명사(portal, map, hub)는 통과하고,
  SaaS 업계 전문용어풍 합성어(suite, sync, dashboard)는 전멸한다.

이 모듈이 제공하는 세 가지:
1. 통계 계산(순수 함수) - 기능어/도메인어별 통과율.
2. 은퇴 목록(`config/retired_function_words.csv`) - 충분히 시도됐는데 통과
   0건인 기능어를 조합 생성에서 제외(`word_pipeline._merged_word_bank`가
   로드). 은퇴된 단어는 더 시도되지 않으므로 통계가 동결되어 되살아날 수
   없다 - 의도된 단방향 설계(수동으로 CSV에서 지우면 복귀 가능).
3. 성과 리포트(`output/_pipeline/analysis/word_performance_latest.md`) -
   매 라운드 종료 시 자동 갱신되고, `expand_word_bank` 판정 요청에 요약이
   직접 포함되어 새 단어 제안이 실측 승자 패턴을 따르도록 강제한다.

Keyword Planner 게이트 자체(임계값·비교 로직)는 이 학습 루프의 대상이
아니다 - 게이트는 시장 신호이며 약화하면 가짜 데이터만 늘어난다(설계 문서
`docs/design/15-continuous-word-quality-improvement.md` 참고).
"""

from __future__ import annotations

import csv
import io
from pathlib import Path

from .contracts import atomic_write_text, normalize_title

# 은퇴 기준: 이만큼 시도했는데 통과 0건이면 "죽은 기능어"로 판정.
# 실측 근거: 2026-08-18 분석에서 300회+ 시도 기능어의 통과율 분포는
# 0.00%(28개)와 1%+(승자군)로 양분됐고 그 사이가 비어 있었다 - 300회 시도에
# 0건이면 통과율 1%였을 때 관측될 확률이 (0.99)^300 ≈ 4.9%로 충분히 낮다.
RETIREMENT_MIN_ATTEMPTS = 300

RETIRED_COLUMNS = ("word", "passed", "attempts", "retired_at")

# 리포트/판정 요약에서 "충분히 표본이 쌓인" 기능어만 순위에 올리는 기준.
MIN_ATTEMPTS_FOR_RANKING = 100


def metrics_cache_path(project_root: Path) -> Path:
    return project_root / "output" / "deliverables" / "history" / "keyword_metrics_cache.csv"


def report_path(project_root: Path) -> Path:
    return project_root / "output" / "_pipeline" / "analysis" / "word_performance_latest.md"


def retired_function_words_path(project_root: Path) -> Path:
    return project_root / "config" / "retired_function_words.csv"


def load_cache_rows(project_root: Path) -> list[dict]:
    path = metrics_cache_path(project_root)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _split_two_word_title(title: str) -> tuple[str, str] | None:
    parts = title.split()
    if len(parts) != 2:
        return None
    return parts[0], parts[1]


def function_word_stats(rows: list[dict]) -> dict[str, tuple[int, int]]:
    """기능어(제목의 두 번째 단어) -> (통과 수, 시도 수)."""
    stats: dict[str, list[int]] = {}
    for row in rows:
        split = _split_two_word_title(row.get("title", ""))
        if split is None:
            continue
        _, fn = split
        entry = stats.setdefault(fn, [0, 0])
        entry[1] += 1
        if row.get("gate_passed") == "True":
            entry[0] += 1
    return {word: (p, t) for word, (p, t) in stats.items()}


def domain_word_stats(rows: list[dict]) -> dict[str, tuple[int, int]]:
    """도메인어(제목의 첫 번째 단어) -> (통과 수, 시도 수)."""
    stats: dict[str, list[int]] = {}
    for row in rows:
        split = _split_two_word_title(row.get("title", ""))
        if split is None:
            continue
        dom, _ = split
        entry = stats.setdefault(dom, [0, 0])
        entry[1] += 1
        if row.get("gate_passed") == "True":
            entry[0] += 1
    return {word: (p, t) for word, (p, t) in stats.items()}


def retirement_candidates(
    stats: dict[str, tuple[int, int]], *, min_attempts: int = RETIREMENT_MIN_ATTEMPTS
) -> list[tuple[str, int, int]]:
    """통과 0건이면서 시도 수가 기준 이상인 기능어. (word, passed, attempts)."""
    return sorted(
        (word, p, t) for word, (p, t) in stats.items() if p == 0 and t >= min_attempts
    )


def load_retired_function_words(project_root: Path) -> set[str]:
    path = retired_function_words_path(project_root)
    if not path.exists():
        return set()
    with path.open("r", encoding="utf-8", newline="") as f:
        return {row["word"] for row in csv.DictReader(f) if row.get("word")}


def merge_retired_function_words(
    project_root: Path, candidates: list[tuple[str, int, int]], when: str
) -> int:
    """은퇴 후보를 `config/retired_function_words.csv`에 병합(기존 행 유지,
    중복 제외). 새로 추가된 개수를 반환한다."""
    path = retired_function_words_path(project_root)
    rows: list[dict] = []
    seen: set[str] = set()
    if path.exists():
        with path.open("r", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                word = row.get("word", "")
                if word and word.lower() not in seen:
                    seen.add(word.lower())
                    rows.append(row)
    added = 0
    for word, passed, attempts in candidates:
        if word.lower() in seen:
            continue
        seen.add(word.lower())
        rows.append({"word": word, "passed": str(passed), "attempts": str(attempts), "retired_at": when})
        added += 1
    if added == 0 and not rows:
        return 0

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=RETIRED_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    atomic_write_text(path, buffer.getvalue())
    return added


def _ranked(stats: dict[str, tuple[int, int]], *, min_attempts: int) -> list[tuple[str, int, int, float]]:
    rows = [
        (word, p, t, (100.0 * p / t) if t else 0.0)
        for word, (p, t) in stats.items()
        if t >= min_attempts
    ]
    return sorted(rows, key=lambda x: (-x[3], -x[1], x[0]))


def performance_summary_for_expansion(project_root: Path, *, top_n: int = 10) -> dict:
    """`expand_word_bank` 판정 요청에 직접 포함되는 실측 성과 요약. 새 단어
    제안이 파일을 따로 찾아 읽지 않아도 승자/사망 패턴을 알 수 있게 한다."""
    rows = load_cache_rows(project_root)
    fn_stats = function_word_stats(rows)
    retired = sorted(load_retired_function_words(project_root))
    top = _ranked(fn_stats, min_attempts=MIN_ATTEMPTS_FOR_RANKING)[:top_n]
    return {
        "function_word_performance_note": (
            "누적 Keyword Planner 실측 통과율. 새 기능어는 아래 top_function_words의 "
            "패턴(사람들이 실제 검색하는 구체적 장소/사물 명사)을 닮게 제안하고, "
            "retired_function_words의 패턴(SaaS 전문용어풍 합성어)은 제안 금지."
        ),
        "top_function_words": [
            {"word": w, "passed": p, "attempts": t, "pass_rate_pct": round(r, 2)}
            for w, p, t, r in top
        ],
        "retired_function_words": retired,
    }


def render_report(
    fn_stats: dict[str, tuple[int, int]],
    dom_stats: dict[str, tuple[int, int]],
    retired: set[str],
    when: str,
) -> str:
    total_pass = sum(p for p, _ in fn_stats.values())
    total = sum(t for _, t in fn_stats.values())
    overall = (100.0 * total_pass / total) if total else 0.0

    lines = [
        "# 단어 성과 리포트 (자동 생성)",
        "",
        f"- 생성 시각: {when}",
        f"- 누적 통과율: {total_pass}/{total} = {overall:.2f}%",
        f"- 은퇴 기능어: {len(retired)}개 (`config/retired_function_words.csv`)",
        "",
        f"## 기능어 통과율 상위 (시도 {MIN_ATTEMPTS_FOR_RANKING}회 이상)",
        "",
        "| 기능어 | 통과 | 시도 | 통과율 |",
        "|---|---|---|---|",
    ]
    for word, p, t, r in _ranked(fn_stats, min_attempts=MIN_ATTEMPTS_FOR_RANKING)[:20]:
        lines.append(f"| {word} | {p} | {t} | {r:.2f}% |")

    zero = retirement_candidates(fn_stats)
    lines += [
        "",
        f"## 은퇴 대상(통과 0 / 시도 {RETIREMENT_MIN_ATTEMPTS}회 이상)",
        "",
        ", ".join(w for w, _, _ in zero) if zero else "(없음)",
        "",
        "## 도메인어 통과율 상위 (시도 30회 이상)",
        "",
        "| 도메인어 | 통과 | 시도 | 통과율 |",
        "|---|---|---|---|",
    ]
    for word, p, t, r in _ranked(dom_stats, min_attempts=30)[:20]:
        lines.append(f"| {word} | {p} | {t} | {r:.2f}% |")
    lines += [
        "",
        "> 해석 가이드: 새 기능어를 제안할 때는 상위 표의 패턴(실제 검색되는 구체적",
        "> 명사)을 닮게, 은퇴 목록의 패턴(전문용어풍 합성어)은 피한다. Keyword",
        "> Planner 게이트 임계값 자체는 조정 대상이 아니다.",
        "",
    ]
    return "\n".join(lines)


def write_report(project_root: Path, when) -> Path | None:
    """누적 캐시가 있으면 성과 리포트를 갱신하고 경로를 반환. 없으면 no-op."""
    rows = load_cache_rows(project_root)
    if not rows:
        return None
    fn_stats = function_word_stats(rows)
    dom_stats = domain_word_stats(rows)
    retired = load_retired_function_words(project_root)
    path = report_path(project_root)
    atomic_write_text(path, render_report(fn_stats, dom_stats, retired, when.isoformat()))
    return path


# ---------------------------------------------------------------------------
# 라운드별 정체 점검 (2026-08-19, 사용자 지시): "라운드가 끝날 때마다 단어
# 생성 능력이 정말 향상됐는지, 정체되고 있는 건 아닌지" 자동으로 더블체크하는
# 루틴. 위의 기능어/도메인어 통계는 "누적 스냅샷"이라 라운드를 거듭해도 추세를
# 알 수 없다 - 이 절이 라운드마다 한 줄씩 쌓는 이력(`round_history.csv`)과
# 그 이력을 최근/이전 구간으로 나눠 비교하는 정체 감지를 더한다.
# ---------------------------------------------------------------------------

ROUND_HISTORY_COLUMNS = (
    "run_id",
    "mode",
    "completed_at",
    "generated",
    "ai_approved",
    "backlog_carried",
    "kp_passed",
    "round_pass_rate_pct",
)

# 정체/개선/저하를 가르는 상대 변화 임계값(%)과, 정체 판단에 묶는 한 구간
# (최근/이전)의 최소 누적 생성 수.
#
# 2026-08-19 정직한 주의사항: 이 두 값은 RETIREMENT_MIN_ATTEMPTS(아래, 실측
# 34,000여 건에서 이항분포로 역산됨)와 달리 통계적으로 검증되지 않은 잠정
# 어림값이다 - 이 정체 점검 메커니즘 자체가 도입 시점에 라운드 이력이 전혀
# 없었기 때문에(round_history.csv가 이제 막 쌓이기 시작) 역산할 데이터가
# 없었다. "500개면 통과 1건 차이가 0.2%p"는 단순 산수이지 그 0.2%p가
# 판정을 얼마나 자주 오판하게 하는지는 계산하지 않았다. round_history.csv가
# 수천~수만 개 생성 규모로 쌓이면(수 회의 production 라운드 후) 은퇴 기준과
# 같은 방식(이항검정)으로 재검증하고 이 주석을 갱신할 것 - 그전까지는
# "그럴듯한 기본값"으로만 취급한다.
STAGNATION_DECLINE_THRESHOLD_PCT = 10.0
STAGNATION_MIN_GENERATED_PER_WINDOW = 500


def round_history_path(project_root: Path) -> Path:
    return project_root / "output" / "_pipeline" / "analysis" / "round_history.csv"


def load_round_history(project_root: Path) -> list[dict]:
    path = round_history_path(project_root)
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def append_round_history(project_root: Path, run_id: str, mode: str, when: str, round_stats: dict) -> dict:
    """라운드 완료 시 정확히 한 번 호출된다(`_stage_update_memory_and_git_checkpoint`).
    같은 run_id가 이미 기록돼 있으면 재기록하지 않고 기존 행을 반환한다 -
    이미 DONE인 run을 실수로 다시 --resume해도 이력이 중복되지 않는다."""
    rows = load_round_history(project_root)
    existing = next((r for r in rows if r["run_id"] == run_id), None)
    if existing is not None:
        return existing

    generated = int(round_stats.get("generated", 0) or 0)
    kp_passed = int(round_stats.get("kp_passed", 0) or 0)
    row = {
        "run_id": run_id,
        "mode": mode,
        "completed_at": when,
        "generated": str(generated),
        "ai_approved": str(int(round_stats.get("ai_approved", 0) or 0)),
        "backlog_carried": str(int(round_stats.get("backlog_carried", 0) or 0)),
        "kp_passed": str(kp_passed),
        "round_pass_rate_pct": f"{100.0 * kp_passed / generated:.4f}" if generated else "",
    }
    rows.append(row)

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=ROUND_HISTORY_COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    atomic_write_text(round_history_path(project_root), buffer.getvalue())
    return row


def _stagnation_windows(rows: list[dict], min_generated: int) -> list[dict]:
    """가장 최근 라운드부터 거꾸로, generated>0인 라운드만 누적해 min_generated
    이상 채워질 때마다 하나의 구간으로 묶는다(최대 2개: 최근/이전).
    backlog만 처리한 라운드(generated=0)는 신규 생성 능력에 대한 신호가 없으므로
    구간 계산에서 제외한다(이력에는 그대로 남아 감사 추적용으로 보존됨)."""
    usable = [r for r in reversed(rows) if int(r["generated"] or 0) > 0]
    windows: list[dict] = []
    i = 0
    while i < len(usable) and len(windows) < 2:
        gen_sum = passed_sum = rounds = 0
        while i < len(usable) and gen_sum < min_generated:
            gen_sum += int(usable[i]["generated"])
            passed_sum += int(usable[i]["kp_passed"])
            rounds += 1
            i += 1
        windows.append({"generated": gen_sum, "kp_passed": passed_sum, "rounds": rounds})
    return windows


def detect_stagnation(
    rows: list[dict],
    *,
    min_generated: int = STAGNATION_MIN_GENERATED_PER_WINDOW,
    decline_threshold_pct: float = STAGNATION_DECLINE_THRESHOLD_PCT,
) -> dict:
    """최근 구간과 그 직전 구간의 통과율을 비교해 improving/stagnant/declining을
    판정한다. 두 구간을 채울 이력이 아직 없으면 insufficient_data."""
    windows = _stagnation_windows(rows, min_generated)
    if len(windows) < 2 or windows[1]["generated"] < min_generated:
        return {
            "status": "insufficient_data",
            "min_generated": min_generated,
        }

    recent, prior = windows[0], windows[1]
    recent_rate = 100.0 * recent["kp_passed"] / recent["generated"]
    prior_rate = 100.0 * prior["kp_passed"] / prior["generated"]

    if prior_rate == 0.0 and recent_rate == 0.0:
        status = "stagnant"
        delta_relative = 0.0
    elif prior_rate == 0.0:
        status = "improving"
        delta_relative = float("inf")
    else:
        delta_relative = 100.0 * (recent_rate - prior_rate) / prior_rate
        if delta_relative <= -decline_threshold_pct:
            status = "declining"
        elif delta_relative >= decline_threshold_pct:
            status = "improving"
        else:
            status = "stagnant"

    return {
        "status": status,
        "recent_generated": recent["generated"],
        "recent_kp_passed": recent["kp_passed"],
        "recent_pass_rate_pct": round(recent_rate, 3),
        "recent_rounds": recent["rounds"],
        "prior_generated": prior["generated"],
        "prior_kp_passed": prior["kp_passed"],
        "prior_pass_rate_pct": round(prior_rate, 3),
        "prior_rounds": prior["rounds"],
        "delta_relative_pct": delta_relative,
    }


def format_stagnation_message(result: dict) -> str:
    """`detect_stagnation`의 결과를 콘솔·HANDOFF에 바로 쓸 수 있는 한 줄로."""
    if result["status"] == "insufficient_data":
        return (
            f"[학습 정체 점검] 데이터 부족 - 최근/이전 구간 각각 생성 "
            f"{result['min_generated']}개 이상 쌓여야 판단 가능"
        )
    label = {"improving": "향상 중", "stagnant": "정체", "declining": "저하"}[result["status"]]
    delta = result["delta_relative_pct"]
    delta_str = "+∞%" if delta == float("inf") else f"{delta:+.1f}%"
    return (
        f"[학습 정체 점검] {label}: 최근 {result['recent_rounds']}라운드"
        f"(생성 {result['recent_generated']}개) 통과율 {result['recent_pass_rate_pct']:.2f}% "
        f"vs 이전 {result['prior_rounds']}라운드(생성 {result['prior_generated']}개) "
        f"{result['prior_pass_rate_pct']:.2f}% (상대변화 {delta_str}, "
        f"임계값 ±{STAGNATION_DECLINE_THRESHOLD_PCT:.0f}%)"
    )


# ---------------------------------------------------------------------------
# 저지능 모델 호환 강화 구조 (2026-08-31, 사용자 지시): "사람 개입 없이 AI가
# 스스로 도는 게 핵심"이라는 제약 아래, 판단 자체는 여전히 전량 AI가 하되
# (코드로 판단을 떠넘기지 않는다) 그 판단이 틀렸을 확률이 높은 순간을 코드가
# 순수 통계로 감지해서 "같은 라운드 안에서 즉시 AI 재검증(레드팀)"을 자동
# 트리거하는 안전망 세 가지: ① 골든셋 카나리아 회귀 검사, ② 승인율 이상탐지,
# ③ 패턴 태그별 실측 성과(가설-검증 루프, 자가확장 판정에 주입). 코드는 감지만
# 하고, 재검증 자체는 word_pipeline이 여는 새 판정 라운드(review_titles_recheck)
# 에서 다시 AI가 수행한다 - 사람에게 넘기지 않는다. 상세 배경은
# `docs/design/15-continuous-word-quality-improvement.md`의 같은 날짜 개정 참고.
# ---------------------------------------------------------------------------

GOLDEN_SET_COLUMNS = ("title", "industry", "expected_approve", "rationale", "added_at")


def golden_set_path(project_root: Path) -> Path:
    return project_root / "config" / "golden_set.csv"


def load_golden_set(project_root: Path) -> dict[str, dict]:
    """정답이 고정된 카나리아 후보(`config/golden_set.csv`)를 정규화된 제목
    -> {expected_approve: bool, ...} 형태로 반환한다. 이 후보들은 실제
    산출물이 아니라 판정 품질을 매 라운드 확인하기 위한 미끼로, review_titles
    요청에 실제 후보와 구분 없이 섞여 들어간다(판정 대상이 미끼인지 알아채면
    검사 의미가 없으므로 형식상 실제 후보와 동일하게 취급됨)."""
    path = golden_set_path(project_root)
    if not path.exists():
        return {}
    result: dict[str, dict] = {}
    with path.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            title = row.get("title", "").strip()
            if not title:
                continue
            result[normalize_title(title)] = {
                "title": title,
                "expected_approve": row.get("expected_approve", "").strip().lower() == "true",
                "rationale": row.get("rationale", ""),
            }
    return result


def golden_set_titles(project_root: Path) -> set[str]:
    """정규화된 카나리아 제목 집합 - 실제 후보 생성이 이 제목들과 우연히
    겹치지 않도록 `word_pipeline._excluded_normalized`가 제외 집합에 합친다."""
    return set(load_golden_set(project_root).keys())


def evaluate_golden_set(canary_decisions: list[dict], golden: dict[str, dict]) -> dict:
    """카나리아 판정 결과와 고정 정답을 비교한다. `canary_decisions`는 이번
    라운드 판정 응답 중 카나리아 제목만 골라낸 것(호출자 책임)."""
    checked = 0
    agreed = 0
    mismatches: list[dict] = []
    for decision in canary_decisions:
        row = golden.get(normalize_title(decision.get("title", "")))
        if row is None:
            continue
        checked += 1
        expected = row["expected_approve"]
        actual = bool(decision.get("approve"))
        if expected == actual:
            agreed += 1
        else:
            mismatches.append(
                {
                    "title": row["title"],
                    "expected_approve": expected,
                    "actual_approve": actual,
                    "rationale": row["rationale"],
                }
            )
    return {
        "checked": checked,
        "agreed": agreed,
        "agreement_pct": round(100.0 * agreed / checked, 2) if checked else None,
        "mismatches": mismatches,
    }


# 승인율 이상탐지(circuit breaker) - 2026-08-31 정직한 주의사항: 실측
# round_history.csv(60개 라운드, 2026-08-19~08-31)의 라운드별 AI 승인율은
# 9.5%~99.6% 사이를 오간다 - 이미 자연 변동폭 자체가 극단적으로 크다. 좁은
# 임계값(예: 평균±1표준편차)은 거의 매 라운드 "이상"으로 판정해버려 신호로서
# 무의미해진다. 그래서 z_threshold를 넉넉하게 잡아 "진짜 극단적인" 경우만
# 잡아내는 용도로 제한한다 - STAGNATION 임계값과 마찬가지로 이 값도 표본이
# 더 쌓이면 재검증 대상인 잠정치다.
APPROVAL_ANOMALY_MIN_ROUNDS = 5
APPROVAL_ANOMALY_Z_THRESHOLD = 3.0


def _historical_approval_rates(history_rows: list[dict]) -> list[float]:
    return [
        100.0 * int(r["ai_approved"]) / int(r["generated"])
        for r in history_rows
        if int(r.get("generated") or 0) > 0
    ]


def detect_approval_rate_anomaly(
    history_rows: list[dict],
    *,
    generated: int,
    ai_approved: int,
    min_rounds: int = APPROVAL_ANOMALY_MIN_ROUNDS,
    z_threshold: float = APPROVAL_ANOMALY_Z_THRESHOLD,
) -> dict:
    """이번 라운드 AI 승인율이 과거 라운드들 대비 통계적으로 극단적인지
    (z-score 기준) 판정한다. 표본 부족·이번 라운드 신규생성 0건이면
    insufficient_data - 정체 점검(`detect_stagnation`)과 마찬가지로 순수
    수치 비교만 하고 원인 해석은 하지 않는다(§5)."""
    if generated <= 0:
        return {"status": "insufficient_data", "reason": "no_new_generation_this_round"}
    rates = _historical_approval_rates(history_rows)
    if len(rates) < min_rounds:
        return {"status": "insufficient_data", "sample_rounds": len(rates), "min_rounds": min_rounds}

    mean = sum(rates) / len(rates)
    variance = sum((r - mean) ** 2 for r in rates) / len(rates)
    stdev = variance**0.5
    current_rate = 100.0 * ai_approved / generated

    if stdev == 0:
        # 과거 승인율의 변동이 전혀 없었던 기준선 - 조금이라도 벗어나면 그
        # 자체로 전례 없는 사건이므로 z-score 나눗셈 없이 방향만 본다.
        if current_rate == mean:
            status, z_score = "normal", 0.0
        elif current_rate > mean:
            status, z_score = "anomalous_high", float("inf")
        else:
            status, z_score = "anomalous_low", float("-inf")
    else:
        z_score = (current_rate - mean) / stdev
        if z_score >= z_threshold:
            status = "anomalous_high"
        elif z_score <= -z_threshold:
            status = "anomalous_low"
        else:
            status = "normal"

    return {
        "status": status,
        "current_rate_pct": round(current_rate, 2),
        "baseline_mean_pct": round(mean, 2),
        "baseline_stdev_pct": round(stdev, 2),
        "z_score": round(z_score, 2),
        "sample_rounds": len(rates),
    }


# 패턴 태그 실측 성과 (가설-검증 루프, 2026-08-31): `expand_word_bank` 제안이
# 각 신규 단어에 붙인 pattern_tag(예: "specific_place_noun")별로 실측
# 통과율을 코드가 자동 집계한다 - "이 패턴이 통했는지"를 세션이 라운드 로그를
# 다시 읽고 일반화할 필요 없이 숫자로 바로 확인 가능하게 한다.


def pattern_tag_performance(expansion_rows: list[dict], cache_rows: list[dict]) -> dict[str, dict]:
    """expansion_rows: `config/word_bank_expansions.csv` 행(pattern_tag 포함).
    cache_rows: `load_cache_rows`로 얻은 Keyword Planner 누적 캐시 행.
    반환: pattern_tag -> {passed, attempts, word_count, pass_rate_pct}."""
    fn_stats = function_word_stats(cache_rows)
    dom_stats = domain_word_stats(cache_rows)
    totals: dict[str, list[int]] = {}
    for row in expansion_rows:
        tag = (row.get("pattern_tag") or "").strip()
        if not tag:
            continue
        stats = fn_stats if row.get("type") == "function" else dom_stats
        passed, attempts = stats.get(row.get("word", ""), (0, 0))
        entry = totals.setdefault(tag, [0, 0, 0])
        entry[0] += passed
        entry[1] += attempts
        entry[2] += 1
    return {
        tag: {
            "passed": p,
            "attempts": a,
            "word_count": n,
            "pass_rate_pct": round(100.0 * p / a, 2) if a else None,
        }
        for tag, (p, a, n) in totals.items()
    }


def least_tried_pattern_tags(expansion_rows: list[dict], cache_rows: list[dict], *, top_n: int = 5) -> list[str]:
    """실측 시도 횟수가 가장 적은 패턴 태그 순 - `expand_word_bank` 판정에서
    "이미 우려먹은 패턴"에 안주하지 않고 새 축을 시도하도록 유도하는 데 쓴다
    (탐색-활용 균형, 정체 방지)."""
    perf = pattern_tag_performance(expansion_rows, cache_rows)
    return sorted(perf.keys(), key=lambda t: perf[t]["attempts"])[:top_n]


def format_golden_set_message(result: dict) -> str:
    """`evaluate_golden_set`의 결과를 콘솔·HANDOFF에 바로 쓸 수 있는 한 줄로."""
    if not result or result.get("checked", 0) == 0:
        return "[골든셋 카나리아] 이번 라운드 카나리아 판정 없음"
    line = f"[골든셋 카나리아] {result['agreed']}/{result['checked']} 일치 ({result['agreement_pct']:.1f}%)"
    if result["mismatches"]:
        line += f", 불일치 {len(result['mismatches'])}건 -> 레드팀 재검증 트리거"
    return line


# 주기적 원칙 재계산 리마인더(2026-08-31): "핵심 원칙"을 매번 증분 수정만
# 하면 오래된 원칙이 낡은 채 누적되며 실제와 어긋나는(드리프트) 문제가 생긴다.
# 코드는 "지금이 재계산 권장 시점"이라는 리마인더만 표면화하고, 실제 재계산
# (전체 실측 데이터로 처음부터 다시 도출)은 의미 해석이라 세션의 몫이다(§5).
PRINCIPLE_REFRESH_REMINDER_EVERY_N_ROUNDS = 10


def principle_refresh_reminder(round_count: int) -> str | None:
    if round_count and round_count % PRINCIPLE_REFRESH_REMINDER_EVERY_N_ROUNDS == 0:
        return (
            f"[원칙 재계산 권장] 누적 {round_count}라운드 도달 - "
            "memory/WORD_GENERATION_LEARNINGS.md의 '핵심 원칙'을 증분 수정 대신 지금까지 "
            "전체 실측 데이터로 처음부터 다시 도출하는 걸 고려하라(드리프트 방지)."
        )
    return None


def format_approval_anomaly_message(result: dict) -> str:
    """`detect_approval_rate_anomaly`의 결과를 콘솔·HANDOFF에 바로 쓸 수 있는 한 줄로."""
    if result.get("status") == "insufficient_data":
        return "[승인율 이상탐지] 데이터 부족"
    label = {
        "normal": "정상",
        "anomalous_high": "이상(과도하게 관대)",
        "anomalous_low": "이상(과도하게 엄격)",
    }[result["status"]]
    return (
        f"[승인율 이상탐지] {label}: 이번 라운드 {result['current_rate_pct']:.1f}% vs "
        f"기준선 평균 {result['baseline_mean_pct']:.1f}%(표준편차 {result['baseline_stdev_pct']:.1f}, "
        f"z={result['z_score']:.2f}, 임계 ±{APPROVAL_ANOMALY_Z_THRESHOLD:.1f})"
    )
