from __future__ import annotations

from saas_words_two import config


def test_load_judgment_quality_config_defaults_when_file_missing(tmp_path):
    cfg = config.load_judgment_quality_config(tmp_path)
    assert cfg["review_titles_chunk_size"] == 200
    assert cfg["structural_invalid_ratio_for_full_retry"] == 0.3
    assert cfg["principle_reverification_every_n_rounds"] == 10


def test_load_judgment_quality_config_overrides_merge_with_defaults(tmp_path):
    (tmp_path / "config").mkdir()
    (tmp_path / "config" / "judgment_quality.yaml").write_text(
        "review_titles_chunk_size: 5\n", encoding="utf-8"
    )
    cfg = config.load_judgment_quality_config(tmp_path)
    assert cfg["review_titles_chunk_size"] == 5
    # 나머지는 여전히 기본값
    assert cfg["expand_word_bank_min_valid_ratio"] == 0.5
