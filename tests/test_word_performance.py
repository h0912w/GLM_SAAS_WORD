"""word_performance(학습 루프) 테스트 - 운영 함수를 직접 호출한다."""

from __future__ import annotations

import csv

from saas_words_two import word_performance


def cache_row(title, gate_passed):
    return {
        "title": title,
        "avg_monthly_searches": "1000",
        "competition_index": "0",
        "api_status": "success",
        "gate_passed": "True" if gate_passed else "False",
        "checked_at": "t0",
    }


def write_cache(project_root, rows):
    path = word_performance.metrics_cache_path(project_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def test_function_word_stats_counts_pass_and_total_by_second_word():
    rows = [
        cache_row("Claim Portal", True),
        cache_row("Fuel Portal", False),
        cache_row("Fuel Sync", False),
        cache_row("malformed-single-token", True),  # 2단어가 아니면 무시
    ]
    stats = word_performance.function_word_stats(rows)
    assert stats == {"Portal": (1, 2), "Sync": (0, 1)}


def test_domain_word_stats_counts_by_first_word():
    rows = [cache_row("Fuel Portal", True), cache_row("Fuel Sync", False)]
    assert word_performance.domain_word_stats(rows) == {"Fuel": (1, 2)}


def test_retirement_candidates_requires_zero_pass_and_min_attempts():
    stats = {
        "Sync": (0, 300),      # 은퇴 대상
        "Toolkit": (0, 299),   # 시도 부족 -> 제외
        "Portal": (1, 300),    # 통과 있음 -> 제외
    }
    assert word_performance.retirement_candidates(stats) == [("Sync", 0, 300)]


def test_merge_retired_function_words_appends_and_dedupes(tmp_path):
    added = word_performance.merge_retired_function_words(tmp_path, [("Sync", 0, 300)], "t0")
    assert added == 1
    # 같은 단어 재병합은 no-op, 새 단어만 추가
    added = word_performance.merge_retired_function_words(
        tmp_path, [("Sync", 0, 310), ("Toolkit", 0, 305)], "t1"
    )
    assert added == 1
    retired = word_performance.load_retired_function_words(tmp_path)
    assert retired == {"Sync", "Toolkit"}
    with word_performance.retired_function_words_path(tmp_path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert rows[0] == {"word": "Sync", "passed": "0", "attempts": "300", "retired_at": "t0"}


def test_load_retired_function_words_missing_file_is_empty(tmp_path):
    assert word_performance.load_retired_function_words(tmp_path) == set()


def test_write_report_renders_stats_and_retired(tmp_path):
    write_cache(tmp_path, [cache_row("Claim Portal", True)] * 100 + [cache_row("Fuel Sync", False)] * 300)
    word_performance.merge_retired_function_words(tmp_path, [("Sync", 0, 300)], "t0")

    path = word_performance.write_report(tmp_path, __import__("saas_words_two.ids", fromlist=["ids"]).now_kst())
    assert path == word_performance.report_path(tmp_path)
    content = path.read_text(encoding="utf-8")
    assert "| Portal | 100 | 100 | 100.00% |" in content
    assert "Sync" in content  # 은퇴 대상 목록


def test_write_report_noop_when_cache_missing(tmp_path):
    from saas_words_two import ids

    assert word_performance.write_report(tmp_path, ids.now_kst()) is None


def round_stats(generated, ai_approved, backlog_carried, kp_passed):
    return {
        "generated": generated,
        "ai_approved": ai_approved,
        "backlog_carried": backlog_carried,
        "kp_passed": kp_passed,
    }


def test_append_round_history_writes_row_and_computes_pass_rate(tmp_path):
    row = word_performance.append_round_history(
        tmp_path, "RUN-1", "production", "t0", round_stats(1000, 50, 0, 7)
    )
    assert row["generated"] == "1000"
    assert row["kp_passed"] == "7"
    assert row["round_pass_rate_pct"] == "0.7000"
    history = word_performance.load_round_history(tmp_path)
    assert len(history) == 1


def test_append_round_history_blank_pass_rate_when_generated_zero(tmp_path):
    # backlog만 처리한 라운드는 신규 생성이 없어 라운드 통과율을 정의할 수 없다
    row = word_performance.append_round_history(
        tmp_path, "RUN-X", "production", "t0", round_stats(0, 0, 20, 3)
    )
    assert row["round_pass_rate_pct"] == ""


def test_append_round_history_is_idempotent_per_run_id(tmp_path):
    first = word_performance.append_round_history(tmp_path, "RUN-1", "qa", "t0", round_stats(10, 1, 0, 1))
    second = word_performance.append_round_history(tmp_path, "RUN-1", "qa", "t1", round_stats(999, 999, 0, 999))
    assert first == second
    assert len(word_performance.load_round_history(tmp_path)) == 1


def test_detect_stagnation_insufficient_data_with_no_history():
    result = word_performance.detect_stagnation([])
    assert result["status"] == "insufficient_data"


def test_detect_stagnation_insufficient_data_when_only_recent_window_filled():
    rows = [
        {"run_id": "R1", "generated": "600", "kp_passed": "6"},
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "insufficient_data"


def test_detect_stagnation_improving_when_recent_rate_up_over_threshold():
    rows = [
        {"run_id": "R1", "generated": "1000", "kp_passed": "5"},   # prior: 0.5%
        {"run_id": "R2", "generated": "1000", "kp_passed": "10"},  # recent: 1.0% (+100%)
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "improving"
    assert result["recent_pass_rate_pct"] == 1.0
    assert result["prior_pass_rate_pct"] == 0.5


def test_detect_stagnation_declining_when_recent_rate_drops_over_threshold():
    rows = [
        {"run_id": "R1", "generated": "1000", "kp_passed": "10"},  # prior: 1.0%
        {"run_id": "R2", "generated": "1000", "kp_passed": "5"},   # recent: 0.5% (-50%)
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "declining"


def test_detect_stagnation_stagnant_when_change_within_threshold():
    rows = [
        {"run_id": "R1", "generated": "1000", "kp_passed": "10"},  # prior: 1.0%
        {"run_id": "R2", "generated": "1000", "kp_passed": "10"},  # recent: 1.0% (0%)
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "stagnant"


def test_detect_stagnation_stagnant_when_both_windows_zero_pass():
    rows = [
        {"run_id": "R1", "generated": "1000", "kp_passed": "0"},
        {"run_id": "R2", "generated": "1000", "kp_passed": "0"},
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "stagnant"


def test_detect_stagnation_skips_zero_generated_backlog_only_rounds():
    # generated=0인 backlog 전용 라운드는 구간 계산에서 건너뛴다
    rows = [
        {"run_id": "R1", "generated": "1000", "kp_passed": "5"},   # prior: 0.5%
        {"run_id": "R2", "generated": "0", "kp_passed": "3"},      # 스킵 대상
        {"run_id": "R3", "generated": "1000", "kp_passed": "10"},  # recent: 1.0%
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "improving"
    assert result["recent_generated"] == 1000
    assert result["recent_kp_passed"] == 10


def test_detect_stagnation_combines_multiple_small_rounds_into_one_window():
    rows = [
        {"run_id": f"R{i}", "generated": "200", "kp_passed": "2"} for i in range(3)  # prior: 3 rounds -> 600 gen
    ] + [
        {"run_id": "R-recent", "generated": "600", "kp_passed": "12"},  # recent: 1 round -> 600 gen, 2.0%
    ]
    result = word_performance.detect_stagnation(rows, min_generated=500)
    assert result["status"] == "improving"
    assert result["prior_rounds"] == 3
    assert result["prior_generated"] == 600
    assert result["recent_rounds"] == 1


def test_format_stagnation_message_insufficient_data():
    msg = word_performance.format_stagnation_message({"status": "insufficient_data", "min_generated": 500})
    assert "[학습 정체 점검]" in msg
    assert "500" in msg


def test_format_stagnation_message_reports_direction_and_numbers():
    result = word_performance.detect_stagnation(
        [
            {"run_id": "R1", "generated": "1000", "kp_passed": "5"},
            {"run_id": "R2", "generated": "1000", "kp_passed": "10"},
        ],
        min_generated=500,
    )
    msg = word_performance.format_stagnation_message(result)
    assert "향상 중" in msg
    assert "1.00%" in msg
    assert "0.50%" in msg


# ---------------------------------------------------------------------------
# 저지능 모델 호환 강화 구조 (2026-08-31): 골든셋 카나리아 회귀 검사,
# 승인율 이상탐지(circuit breaker), 패턴 태그 실측 성과.
# ---------------------------------------------------------------------------


def write_golden_set(tmp_path, rows):
    path = word_performance.golden_set_path(tmp_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=word_performance.GOLDEN_SET_COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


GOLDEN_ROWS = [
    {"title": "Falcon Ledger", "industry": "canary", "expected_approve": "True", "rationale": "clear", "added_at": "t0"},
    {"title": "Slack Messenger", "industry": "canary", "expected_approve": "False", "rationale": "trademark", "added_at": "t0"},
]


def test_load_golden_set_missing_file_is_empty(tmp_path):
    assert word_performance.load_golden_set(tmp_path) == {}
    assert word_performance.golden_set_titles(tmp_path) == set()


def test_load_golden_set_parses_expected_approve_and_normalizes_key(tmp_path):
    write_golden_set(tmp_path, GOLDEN_ROWS)
    golden = word_performance.load_golden_set(tmp_path)
    assert golden["falcon ledger"]["expected_approve"] is True
    assert golden["slack messenger"]["expected_approve"] is False
    assert word_performance.golden_set_titles(tmp_path) == {"falcon ledger", "slack messenger"}


def test_evaluate_golden_set_counts_agreement_and_mismatches(tmp_path):
    write_golden_set(tmp_path, GOLDEN_ROWS)
    golden = word_performance.load_golden_set(tmp_path)
    decisions = [
        {"title": "Falcon Ledger", "approve": True},  # agrees
        {"title": "Slack Messenger", "approve": True},  # mismatch - expected False
    ]
    result = word_performance.evaluate_golden_set(decisions, golden)
    assert result == {
        "checked": 2,
        "agreed": 1,
        "agreement_pct": 50.0,
        "mismatches": [
            {
                "title": "Slack Messenger",
                "expected_approve": False,
                "actual_approve": True,
                "rationale": "trademark",
            }
        ],
    }


def test_evaluate_golden_set_ignores_decisions_not_in_golden_set(tmp_path):
    write_golden_set(tmp_path, GOLDEN_ROWS)
    golden = word_performance.load_golden_set(tmp_path)
    result = word_performance.evaluate_golden_set([{"title": "Some Real Candidate", "approve": True}], golden)
    assert result["checked"] == 0
    assert result["agreement_pct"] is None


def approval_history_row(generated, ai_approved):
    return {"generated": str(generated), "ai_approved": str(ai_approved), "kp_passed": "0"}


def test_detect_approval_rate_anomaly_insufficient_data_with_no_new_generation():
    result = word_performance.detect_approval_rate_anomaly([], generated=0, ai_approved=0)
    assert result["status"] == "insufficient_data"


def test_detect_approval_rate_anomaly_insufficient_data_with_few_historical_rounds():
    history = [approval_history_row(100, 50)] * 2  # fewer than min_rounds
    result = word_performance.detect_approval_rate_anomaly(history, generated=100, ai_approved=50, min_rounds=5)
    assert result["status"] == "insufficient_data"
    assert result["sample_rounds"] == 2


def test_detect_approval_rate_anomaly_normal_within_threshold():
    # 50% 승인율이 반복된 안정적 이력 대비 이번 라운드도 50% -> 정상
    history = [approval_history_row(100, 50)] * 6
    result = word_performance.detect_approval_rate_anomaly(history, generated=100, ai_approved=50, min_rounds=5)
    assert result["status"] == "normal"


def test_detect_approval_rate_anomaly_flags_extreme_high():
    # 이력은 항상 승인율 정확히 50% (표준편차 0) - 이번 라운드 100% 승인은
    # stdev=0일 때 z_score 계산의 0-division을 특별 취급해야 극단치로 잡힌다.
    history = [approval_history_row(100, 50)] * 6
    result = word_performance.detect_approval_rate_anomaly(history, generated=100, ai_approved=100, min_rounds=5)
    assert result["status"] == "anomalous_high"


def test_detect_approval_rate_anomaly_skips_backlog_only_rounds_in_baseline():
    history = [approval_history_row(0, 0)] * 3 + [approval_history_row(100, 50)] * 6
    result = word_performance.detect_approval_rate_anomaly(history, generated=100, ai_approved=50, min_rounds=5)
    assert result["sample_rounds"] == 6  # generated=0 라운드는 기준선에서 제외


def test_format_golden_set_message_no_canaries_checked():
    assert "카나리아 판정 없음" in word_performance.format_golden_set_message({})


def test_format_golden_set_message_reports_mismatch_trigger():
    msg = word_performance.format_golden_set_message(
        {"checked": 2, "agreed": 1, "agreement_pct": 50.0, "mismatches": [{"title": "x"}]}
    )
    assert "1/2" in msg
    assert "레드팀 재검증 트리거" in msg


def test_format_approval_anomaly_message_insufficient_data():
    assert "데이터 부족" in word_performance.format_approval_anomaly_message({"status": "insufficient_data"})


def expansion_row(word_type, word, pattern_tag):
    return {"type": word_type, "word": word, "industry": "", "pattern_tag": pattern_tag}


def test_pattern_tag_performance_aggregates_words_sharing_a_tag(tmp_path):
    cache_rows = [cache_row("Fuel Portal", True)] * 5 + [cache_row("Fuel Map", False)] * 5
    expansions = [
        expansion_row("function", "Portal", "specific_place_noun"),
        expansion_row("function", "Map", "specific_place_noun"),
    ]
    perf = word_performance.pattern_tag_performance(expansions, cache_rows)
    assert perf["specific_place_noun"] == {"passed": 5, "attempts": 10, "word_count": 2, "pass_rate_pct": 50.0}


def test_pattern_tag_performance_ignores_rows_without_a_tag():
    cache_rows = [cache_row("Fuel Portal", True)]
    expansions = [expansion_row("function", "Portal", "")]
    assert word_performance.pattern_tag_performance(expansions, cache_rows) == {}


def test_dead_pattern_tags_requires_zero_pass_and_min_attempts():
    cache_rows = [cache_row("Fuel Portal", False)] * 300 + [cache_row("Fuel Sync", True)] * 300
    expansions = [
        expansion_row("function", "Portal", "dead_strategy"),
        expansion_row("function", "Sync", "alive_strategy"),
    ]
    assert word_performance.dead_pattern_tags(expansions, cache_rows) == ["dead_strategy"]


def test_dead_pattern_tags_excludes_under_sampled_tags():
    cache_rows = [cache_row("Fuel Portal", False)] * 50  # 300 미만 - 판정 보류
    expansions = [expansion_row("function", "Portal", "too_early_to_tell")]
    assert word_performance.dead_pattern_tags(expansions, cache_rows) == []


def test_least_tried_pattern_tags_orders_by_ascending_attempts():
    cache_rows = [cache_row("Fuel Portal", True)] * 10 + [cache_row("Fuel Map", True)] * 2
    expansions = [
        expansion_row("function", "Portal", "well_tried_tag"),
        expansion_row("function", "Map", "fresh_tag"),
    ]
    assert word_performance.least_tried_pattern_tags(expansions, cache_rows) == ["fresh_tag", "well_tried_tag"]


def test_principle_refresh_reminder_fires_only_on_multiples_of_n():
    assert word_performance.principle_refresh_reminder(9) is None
    assert word_performance.principle_refresh_reminder(0) is None
    reminder = word_performance.principle_refresh_reminder(10)
    assert reminder is not None
    assert "10라운드" in reminder


def test_performance_summary_for_expansion_includes_top_and_retired(tmp_path):
    write_cache(
        tmp_path,
        [cache_row("Claim Portal", True)] * 10 + [cache_row("Fuel Portal", False)] * 90
        + [cache_row("Fuel Sync", False)] * 300,
    )
    word_performance.merge_retired_function_words(tmp_path, [("Sync", 0, 300)], "t0")

    summary = word_performance.performance_summary_for_expansion(tmp_path)
    assert summary["retired_function_words"] == ["Sync"]
    top_words = [entry["word"] for entry in summary["top_function_words"]]
    assert "Portal" in top_words
    portal = next(e for e in summary["top_function_words"] if e["word"] == "Portal")
    assert portal == {"word": "Portal", "passed": 10, "attempts": 100, "pass_rate_pct": 10.0}
