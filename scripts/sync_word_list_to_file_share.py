"""통과 단어 리스트(문서 ④)를 외부 미러 저장소(dudreat/File_share)에 동기화한다.

2026-11-21 사용자 지시로 도입. 매 라운드 체크포인트 단계
(word_pipeline._stage_update_memory_and_git_checkpoint)에서 호출되며:

- 마스터: <mirror>/saas-words/passed_words_latest.txt (항상 최신 전체 누적)
- 스냅샷: <mirror>/saas-words/snapshots/passed_words_<KST타임스탬프>.txt

미러는 공식 산출물 4개 문서의 부차 복제본일 뿐이며 계약을 바꾸지 않는다.
미러 푸시 실패는 라운드를 막지 않는다 - 호출측이 종료코드를 보고 경고 한 줄만
남긴다. 단독 실행도 가능하다:
    python scripts/sync_word_list_to_file_share.py [--snapshot passed_words_....txt]
미러 로컬 클론 경로는 --mirror-dir 또는 환경변수 FILE_SHARE_MIRROR_DIR로
바꿀 수 있다(기본: 프로젝트 루트의 형제 디렉토리 File_share).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from saas_words_two import ids
from saas_words_two.contracts import atomic_write_text

# github.com이 아닌 ~/.ssh/config의 github-dudreat 호스트 별명을 쓴다 -
# 이 저장소는 dudreat 계정(id_ed25519_dudreat)으로만 접근 가능하다.
FILE_SHARE_REMOTE = "git@github-dudreat:dudreat/File_share.git"
MIRROR_SUBDIR = "saas-words"
SNAPSHOT_NAME_RE = re.compile(r"^passed_words_\d{8}_\d{6}_KST\.txt$")


def is_valid_snapshot_name(name: str) -> bool:
    return bool(SNAPSHOT_NAME_RE.match(name))


def resolve_mirror_dir(project_root: Path, explicit: str | None = None) -> Path:
    if explicit:
        return Path(explicit)
    env = os.environ.get("FILE_SHARE_MIRROR_DIR")
    if env:
        return Path(env)
    return project_root.parent / "File_share"


def run_git(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=False)


def plan_sync(
    master_content: str,
    existing_master: str | None,
    snapshot_name: str | None,
    existing_snapshot_names: frozenset[str],
) -> dict[str, str]:
    """미러에 써야 할 파일(상대경로 -> 내용)을 결정하는 순수 함수.

    - 마스터가 미러와 다르면 갱신
    - 스냅샷 이름이 유효하고 미러에 아직 없으면 추가(내용은 그 라운드의
      마스터와 동일 - 파이프라인이 같은 content로 둘 다 쓰기 때문)
    - 바뀔 것이 없으면 빈 dict (NO_CHANGE)
    """
    files: dict[str, str] = {}
    if existing_master != master_content:
        files["passed_words_latest.txt"] = master_content
    if snapshot_name:
        if not is_valid_snapshot_name(snapshot_name):
            raise ValueError(f"스냅샷 파일명 형식 오류: {snapshot_name!r}")
        if snapshot_name not in existing_snapshot_names:
            files[f"snapshots/{snapshot_name}"] = master_content
    return files


def build_readme(when) -> str:
    stamp = when.strftime("%Y-%m-%d %H:%M:%S KST")
    return (
        "# saas-words\n\n"
        "SAAS_WORDS_TWO 파이프라인(GitHub: h0912w/GLM_SAAS_WORD)이 Keyword Planner\n"
        "게이트를 통과시킨 영어 2단어 제목(단어)의 누적 리스트다.\n\n"
        "- `passed_words_latest.txt` — 항상 최신 전체 누적 (한 줄 한 단어, UTF-8 LF)\n"
        "- `snapshots/` — 라운드별 시점 스냅샷 (`passed_words_<KST타임스탬프>.txt`)\n\n"
        f"미러 최초 구축: {stamp}. 파이프라인 라운드 체크포인트 때마다 자동 갱신된다.\n"
    )


@dataclass(frozen=True)
class SyncResult:
    status: str  # UPDATED | NO_CHANGE | FAILED
    detail: str
    files_written: tuple[str, ...] = ()


def prepare_mirror(mirror: Path, remote: str) -> tuple[bool, str]:
    """미러 로컬 클론을 준비한다. 성공 시 (True, 현재브랜치), 실패 시 (False, 사유)."""
    if (mirror / ".git").exists():
        fetch = run_git(mirror, "fetch", "origin")
        if fetch.returncode != 0:
            return False, f"fetch 실패: {fetch.stderr.strip()}"
        branch = run_git(mirror, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        reset = run_git(mirror, "reset", "--hard", f"origin/{branch}")
        if reset.returncode != 0:
            return False, f"reset 실패: {reset.stderr.strip()}"
        return True, branch
    if mirror.exists() and any(mirror.iterdir()):
        return False, f"미러 경로가 빈 디렉토리도 git 저장소도 아님: {mirror}"
    mirror.parent.mkdir(parents=True, exist_ok=True)
    clone = run_git(mirror.parent, "clone", remote, str(mirror))
    if clone.returncode != 0:
        return False, f"clone 실패: {clone.stderr.strip()}"
    branch = run_git(mirror, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    return True, branch


def sync_word_list(
    project_root: Path,
    mirror_dir: str | None = None,
    remote: str = FILE_SHARE_REMOTE,
    snapshot_name: str | None = None,
) -> SyncResult:
    source_master = (
        project_root / "output" / "deliverables" / "final_words" / "passed_words_latest.txt"
    )
    if not source_master.exists():
        return SyncResult("FAILED", f"원본 마스터 없음: {source_master}")
    master_content = source_master.read_text(encoding="utf-8")

    mirror = resolve_mirror_dir(project_root, mirror_dir)
    ok, detail = prepare_mirror(mirror, remote)
    if not ok:
        return SyncResult("FAILED", detail)
    branch = detail

    target = mirror / MIRROR_SUBDIR
    (target / "snapshots").mkdir(parents=True, exist_ok=True)
    readme = target / "README.md"
    if not readme.exists():
        atomic_write_text(readme, build_readme(ids.now_kst()))

    master_path = target / "passed_words_latest.txt"
    existing_master = master_path.read_text(encoding="utf-8") if master_path.exists() else None
    existing_snapshots = frozenset(p.name for p in (target / "snapshots").glob("*.txt"))
    try:
        files = plan_sync(master_content, existing_master, snapshot_name, existing_snapshots)
    except ValueError as exc:
        return SyncResult("FAILED", str(exc))
    if not files:
        return SyncResult("NO_CHANGE", f"미러가 이미 최신(브랜치 {branch})")

    for rel, content in files.items():
        atomic_write_text(target / rel, content)
    run_git(mirror, "add", MIRROR_SUBDIR)
    staged = run_git(mirror, "diff", "--cached", "--name-only")
    if not any(line.strip() for line in staged.stdout.splitlines()):
        return SyncResult("NO_CHANGE", f"기록할 변경 없음(브랜치 {branch})")

    words = len(master_content.splitlines()) if master_content else 0
    stamp = ids.now_kst().strftime("%Y%m%d_%H%M%S")
    commit = run_git(
        mirror,
        "commit",
        "-m",
        f"sync: passed words update ({words} words, {stamp} KST)",
    )
    if commit.returncode != 0:
        return SyncResult("FAILED", f"commit 실패: {commit.stderr.strip()}")
    push = run_git(mirror, "push", "origin", branch)
    if push.returncode != 0:
        return SyncResult("FAILED", f"push 실패: {push.stderr.strip()}")
    return SyncResult(
        "UPDATED",
        f"{len(files)}개 파일 푸시 완료({words}단어, 브랜치 {branch})",
        tuple(files),
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--snapshot", default=None, help="이번 라운드 스냅샷 파일명 (passed_words_<ts>_KST.txt)")
    parser.add_argument("--mirror-dir", default=None, help="미러 로컬 클론 경로 (기본: 프로젝트 형제 File_share)")
    parser.add_argument("--remote", default=FILE_SHARE_REMOTE, help="미러 원격 저장소 URL")
    args = parser.parse_args(argv)

    # 상대경로(.)가 들어와도 resolve하지 않으면 project_root.parent가 자기
    # 자신이 되어 미러 클론이 프로젝트 내부에 생기는 사고가 난다(2026-11-21
    # 실측) - 반드시 절대경로로 정규화한다.
    project_root = args.project_root.resolve()

    result = sync_word_list(
        project_root,
        mirror_dir=args.mirror_dir,
        remote=args.remote,
        snapshot_name=args.snapshot,
    )
    print(
        f"FILE SHARE MIRROR SYNC: status={result.status} "
        f"files={','.join(result.files_written) or '-'} detail={result.detail}"
    )
    return 0 if result.status in ("UPDATED", "NO_CHANGE") else 1


if __name__ == "__main__":
    raise SystemExit(main())
