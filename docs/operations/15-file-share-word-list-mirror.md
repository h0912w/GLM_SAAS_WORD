# 15 — 외부 미러: dudreat/File_share 단어 리스트 동기화 (2026-11-21)

## 목적

사용자 지시(2026-11-21): `github.com/dudreat/File_share` 저장소에 적절한 폴더
구조를 만들고, 이 프로젝트가 식별한 전체 통과 단어 리스트를 **매 라운드 계속
업데이트해서 올린다**. 사람 개입 없이 파이프라인이 스스로 하도록 체크포인트
스테이지에 연결돼 있다.

## 폴더 구조 (미러 저장소 쪽)

```
File_share/
└── saas-words/
    ├── README.md                                  # 최초 1회 자동 생성
    ├── passed_words_latest.txt                    # 문서④ 마스터 복제본 (누적 전체)
    └── snapshots/
        └── passed_words_<KST타임스탬프>.txt        # 문서④ 라운드 스냅샷 복제본
```

## 동작 방식

1. `_export_final_words_and_history_snapshots`가 이번 라운드 스냅샷 파일명을
   반환하고, `word_pipeline`이 `state.context["final_words_snapshot"]`에 기록한다.
2. `_stage_update_memory_and_git_checkpoint`가 HANDOFF 기록 **전에**
   `_sync_file_share_mirror`을 호출한다 — 실패 경고가 같은 배치의 HANDOFF에
   함께 커밋되기 위함이다.
3. `scripts/sync_word_list_to_file_share.py`가 미러 로컬 클론(기본: 프로젝트
   루트의 형제 디렉토리 `File_share`, 환경변수 `FILE_SHARE_MIRROR_DIR` 또는
   `--mirror-dir`로 변경 가능)을 `fetch`+`reset --hard origin/<branch>`로
   최신화한 뒤, 바뀐 파일만 원자적 쓰기로 기록하고 커밋·푸시한다.
   원격 URL은 `git@github-dudreat:dudreat/File_share.git`이다 — `github.com`
   별명(h0912w 키)이 아니라 `~/.ssh/config`의 `github-dudreat` 별명
   (`id_ed25519_dudreat` 키)을 써야 이 저장소에 접근된다.
4. 바뀔 것이 없으면 커밋하지 않고 `NO_CHANGE`로 끝난다(변경 없는 커밋 낭비 방지).

## 실패 처리

- 미러는 공식 산출물 4개 문서의 **부차 복제본**이므로, 푸시 실패는 라운드를
  실패로 만들지 않는다(2026-11-21 사용자 선택).
- 실패 시 콘솔에 `FILE SHARE MIRROR SYNC: status=FAILED ...`이 출력되고
  HANDOFF에 `[File_share 미러] 동기화 실패: <사유>` 한 줄이 남는다 — 실패는
  항상 눈에 보인다(§8 실패 은폐 금지).
- 타임아웃은 300초다. 다음 라운드에서 자동으로 재시도된다(미러가 이미 최신이면
  그때는 `NO_CHANGE`).

## 단독 실행

```bash
python scripts/sync_word_list_to_file_share.py --project-root .
# 스냅샷을 명시할 때:
python scripts/sync_word_list_to_file_share.py --snapshot passed_words_20261121_090000_KST.txt
```

## 역할 분리 (CLAUDE.md §5)

이 기능은 전부 코드 몫이다 — 파일 복제·중복 감지·커밋·푸시 모두 순수 기계
작업이라 판단이 개입하지 않는다. 미러에 올라가는 단어 자체의 선정은 기존과
동일하게 AI 판정 + Keyword Planner 게이트(코드)가 이미 끝낸 결과다.
