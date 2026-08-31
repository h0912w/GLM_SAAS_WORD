from __future__ import annotations

from pathlib import Path

import yaml


def load_keyword_metrics_config(project_root: Path) -> dict:
    """avg_monthly_searches_min/competition_index_exact 필터 기준값과 Google Ads
    API 런타임 설정 (memory/ACTIVE_ISSUES.md GKP-001). 이 파일의 두 기준값만
    바꾸면 필터 동작이 바뀐다 - 코드는 이 값을 읽기만 한다."""
    return yaml.safe_load((project_root / "config" / "keyword_metrics.yaml").read_text(encoding="utf-8"))


def load_judgment_quality_config(project_root: Path) -> dict:
    """저지능 모델 호환 강화 구조 2단계(2026-09-01)의 조정 가능 값 -
    청크 크기, 구조 검증/재요청 임계값, 탐색 쿼터, 원칙 재검증 주기.
    `config/judgment_quality.yaml`이 없으면 안전한 기본값으로 동작한다."""
    path = project_root / "config" / "judgment_quality.yaml"
    defaults = {
        "review_titles_chunk_size": 200,
        "structural_invalid_ratio_for_full_retry": 0.3,
        "structural_retry_max": 1,
        "expand_word_bank_min_valid_ratio": 0.5,
        "exploration_quota_pct": 0.3,
        "expand_word_bank_retry_max": 1,
        "principle_reverification_every_n_rounds": 10,
    }
    if not path.exists():
        return defaults
    loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {**defaults, **loaded}
