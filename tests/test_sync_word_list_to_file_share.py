import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync_word_list_to_file_share as script


def init_bare_remote(path: Path) -> None:
    path.mkdir(parents=True)
    subprocess.run(["git", "init", "-q", "--bare", str(path)], check=True)


def make_project_root(path: Path, master_content: str) -> Path:
    final_words = path / "output" / "deliverables" / "final_words"
    final_words.mkdir(parents=True, exist_ok=True)
    (final_words / "passed_words_latest.txt").write_text(master_content, encoding="utf-8")
    return path


def set_git_identity(repo: Path) -> None:
    subprocess.run(["git", "config", "user.name", "test"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)


def test_is_valid_snapshot_name_accepts_pipeline_format():
    assert script.is_valid_snapshot_name("passed_words_20261121_090000_KST.txt")


def test_is_valid_snapshot_name_rejects_other_formats():
    assert not script.is_valid_snapshot_name("passed_words_latest.txt")
    assert not script.is_valid_snapshot_name("../passed_words_20261121_090000_KST.txt")
    assert not script.is_valid_snapshot_name("passed_words_20261121_KST.txt")
    assert not script.is_valid_snapshot_name("")


def test_plan_sync_writes_master_when_missing_or_changed():
    files = script.plan_sync("A\nB\n", None, None, frozenset())
    assert files == {"passed_words_latest.txt": "A\nB\n"}
    files = script.plan_sync("A\nB\n", "A\n", None, frozenset())
    assert files == {"passed_words_latest.txt": "A\nB\n"}


def test_plan_sync_no_change_when_identical():
    files = script.plan_sync("A\nB\n", "A\nB\n", None, frozenset())
    assert files == {}


def test_plan_sync_adds_new_snapshot_only():
    files = script.plan_sync(
        "A\n", "A\n", "passed_words_20261121_090000_KST.txt", frozenset()
    )
    assert files == {"snapshots/passed_words_20261121_090000_KST.txt": "A\n"}


def test_plan_sync_skips_existing_snapshot():
    files = script.plan_sync(
        "A\n",
        "A\n",
        "passed_words_20261121_090000_KST.txt",
        frozenset({"passed_words_20261121_090000_KST.txt"}),
    )
    assert files == {}


def test_plan_sync_rejects_invalid_snapshot_name():
    with pytest.raises(ValueError):
        script.plan_sync("A\n", "A\n", "../evil.txt", frozenset())


def test_sync_word_list_end_to_end_with_local_remote(tmp_path):
    remote = tmp_path / "remote.git"
    init_bare_remote(remote)
    root = make_project_root(tmp_path / "project", "Access Map\nFurnace Tracker\n")
    mirror = tmp_path / "mirror"

    result = script.sync_word_list(root, mirror_dir=str(mirror), remote=str(remote))
    assert result.status == "UPDATED"
    assert (mirror / "saas-words" / "passed_words_latest.txt").read_text(encoding="utf-8") == (
        "Access Map\nFurnace Tracker\n"
    )
    assert (mirror / "saas-words" / "README.md").exists()

    # 같은 내용 재동기화 - NO_CHANGE (변경 없는 커밋 낭비 방지)
    result = script.sync_word_list(root, mirror_dir=str(mirror), remote=str(remote))
    assert result.status == "NO_CHANGE"

    # 마스터 갱신 + 새 스냅샷 - 스냅샷이 미러에 추가된다
    make_project_root(root, "Access Map\nFurnace Tracker\nAccess List\n")
    result = script.sync_word_list(
        root,
        mirror_dir=str(mirror),
        remote=str(remote),
        snapshot_name="passed_words_20261121_100000_KST.txt",
    )
    assert result.status == "UPDATED"
    assert result.files_written == (
        "passed_words_latest.txt",
        "snapshots/passed_words_20261121_100000_KST.txt",
    )
    snapshot = mirror / "saas-words" / "snapshots" / "passed_words_20261121_100000_KST.txt"
    assert snapshot.read_text(encoding="utf-8") == "Access Map\nFurnace Tracker\nAccess List\n"


def test_sync_word_list_fails_cleanly_without_source(tmp_path):
    remote = tmp_path / "remote.git"
    init_bare_remote(remote)
    root = tmp_path / "empty_project"
    root.mkdir()
    result = script.sync_word_list(root, mirror_dir=str(tmp_path / "mirror"), remote=str(remote))
    assert result.status == "FAILED"
    assert "원본 마스터 없음" in result.detail
