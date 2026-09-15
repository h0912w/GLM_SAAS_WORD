# ACTIVE ISSUES

> **아카이브 규칙(2026-09-15, 사용자 지시)**: OPEN 이슈 전문만 이 파일에 유지하고,
> RESOLVED·역사적 이슈의 전문은 `memory/archive/ACTIVE_ISSUES_ARCHIVE.md`로
> 무변경 이동했다. 세션 시작 시 아카이브를 읽을 필요는 없다 — 아래 요약 인덱스로
> 충분하고, 전문이 필요할 때 해당 섹션만 찾아 읽는다. 새 이슈가 해결되면 전문을
> 아카이브에 append하고 이 파일의 요약을 갱신한다.

## DATA-001 — ledger에 역순 중복 1건 잔존(`Grid Terminal`/`Terminal Grid`), 현재 코드로는 재현 불가한 과거 유물
- 상태: OPEN(낮은 우선순위 — 데이터 정리만 필요, 코드 결함 아님)
- 발견: 2026-08-29, `final-qa-runner`가 QA-20260829-165706-KST 스모크 회귀 중
  `output/deliverables/history/generated_candidates.csv`(당시 250,358행) 전체를
  정확/대소문자/역순 중복 기준으로 스캔해 발견. 유일한 위반 사례:
  - `Grid Terminal` (industry=energy_utilities, ai_approved=False, judged_at
    2026-08-18T07:43:20+09:00)
  - `Terminal Grid` (industry 빈칸, ai_approved=True, judged_at
    2026-08-17T23:06:14+09:00)
  둘 다 이번 QA 세션이 시작(2026-08-29)하기 10일 이상 전, 자가확장 단어뱅크
  도입 직후(2026-08-17~18) 생성된 행이다 — 이번 QA가 만든 게 아니다.
- 원인 추정: `Grid`/`Terminal` 둘 다 특정 업계 도메인어(각각 energy_utilities/
  transportation)이면서 동시에 범용 기능어 목록에도 있는 "이중 역할" 단어라,
  `Terminal`(도메인)+`Grid`(기능) = "Terminal Grid"가 먼저 ledger에 들어간
  뒤 다음날 `Grid`(도메인)+`Terminal`(기능) = "Grid Terminal"이 생성됐다.
  당시(08-17/18) `_excluded_normalized`가 ledger 전체를 정확히 로드하지
  못했거나 역순중복 로직이 아직 지금 형태로 다듬어지기 전이었을 가능성이
  높다.
- **현재 코드는 이 클래스의 버그를 재현하지 않음을 직접 검증**: `Terminal
  Grid`를 exclude 집합에 넣고 `word_generation.generate_combinations(...,
  domain_words={"energy_utilities": ["Grid"]}, function_words=["Terminal"])`를
  호출하면 결과가 빈 리스트 — `reverse_normalized_title` 기반 역순 차단이
  두 단어의 도메인/기능 이중 역할과 무관하게 정상 동작한다(2026-08-29
  라이브 확인). `qa/regression/REQUIRED_CASES.md`의 역순 중복 케이스도
  `tests/test_regression_required_cases.py::
  test_history_exact_case_and_reverse_duplicates_rejected`로 커버되어 이번
  pytest 144개 전체 통과에 포함됨.
- 남은 작업(후속 세션): ledger·캐시·통과표에서 이 1건(정확히 어느 쪽을
  남길지 — `Terminal Grid`가 먼저 생성됐고 backlog/KP 처리 이력이 있을 수
  있으니 실제 영향(§4 4개 문서에 이 페어가 몇 군데 더 등장하는지)을 먼저
  확인한 뒤) 정리하는 일회성 데이터 정합 패치. 코드 수정은 불필요 — 위
  라이브 검증대로 생성 단계 차단은 이미 정상.

---

## 아카이브 이슈 요약 인덱스 (전문: `memory/archive/ACTIVE_ISSUES_ARCHIVE.md`)

## AI-JUDGMENT-001 (2026-09-01) — production 10,000개 판정을 포크 하나에 통째로
위임했다가 규모 압박으로 규칙 엔진(고정 기능어 블록리스트)으로 대체된 사고(§5
실질 위반). 예방책 3종(청크 병렬 분산, 거절사유 반복도 게이트, "방법 자체 변경
금지+즉시 보고" 위임 지시) 구현 완료 — 2026-09-10 recheck 751건 병렬 위임에서
사후검증 3종(형식·거절사유 반복도·사유-제목 대응) 전부 통과로 첫 실측 성공.
`memory/PROJECT_PLAYBOOK.md` candidate 규칙의 근거. 오염 라운드
(RUN-20260901-002857-KST)의 ledger/캐시 데이터는 실제 API 예산으로 얻은 시장
데이터 보존을 위해 유지 중(되돌리기 미실시).

## GKP-001 (2026-08-17, RESOLVED) — §2.3을 개정해 공식 Google Ads API
(`KeywordPlanIdeaService.generateKeywordIdeas`, OAuth 정식 인증) 연동을 예외
허용. 게이트 기준값은 `config/keyword_metrics.yaml`(`avg_monthly_searches_min`,
`competition_index_exact`)만 바꾸면 조정된다. "검색량 높음 AND 경쟁지수 정확히
0"의 실측 통과율 1~3%는 버그가 아니라 이 필터의 본질이다. 자격증명 시행착오
5종은 `docs/operations/15-google-ads-credential-setup.md`로 이관돼 있다.

## DEMAND-001 (2026-08-10~11, 보류→역사 기록) — HN 단독 → GH Archive 추가 →
TF-IDF → 5개 데이터원 전부 활성화 → 알고리즘 정밀 튜닝 → 업계 전문용어 확보,
일곱 차례 실측 시도 모두 수요 관문(독립 사용자 5명) 통과 군집 0건. 2026-08-11
프로젝트 1차 전환(수요·공급 계산 폐기)의 직접 근거. 관련 파이프라인은
2026-08-18 완전 삭제됨(`git log` 커밋 `d1ca668` 이후로 복원 가능).

## PROJECT-002 (2026-08-18, RESOLVED) — 2차 정의 전환: "정확히 500개" 목표·완료
개념 폐기 → 4문서 산출 체계(CLAUDE.md §4), round-size 기반 "한 실행=한 라운드",
수요/공급 파이프라인 완전 삭제. ledger 스윕 기반 backlog 설계(AI 승인·KP 미확인
후보 유실 방지)도 여기서 도입됨.

## PROJECT-003 (2026-08-18, RESOLVED) — 단어뱅크 소진 문제의 구조적 해결:
자가확장(`expand_word_bank` 판정 → `config/word_bank_expansions.csv` append →
병합 풀로 재시도). 실제 자격증명 라이브 검증 완료(`Furnace Tracker` 통과).

## PROJECT-004 (2026-08-23, RESOLVED) — 외부 자동화(NVIDIA 백엔드
`fcc-server.exe`)가 판정 주체가 되어 12,725건 무조건 승인(빈 도장) + run
디렉토리 1,309개 오염 사고 → `git revert`로 복구. 재발 방지 규칙: 판정은 반드시
현재 세션/서브에이전트가 직접 수행하고, 무인 루프에 미리 정해진 도장을
맡기지 않는다.

## PROCESS-001 (2026-08-27, RESOLVED) — Termius SSH 세션에서 git push가
실패하던 문제(Windows 세션 0 비대화형 구조 한계)를 SSH 키 인증 도입
(`docs/operations/14-remote-ssh-github-authentication.md` 실제 적용)으로 근본
해소. "SSH 세션에서는 push를 미룬다" 예외 정책 폐기, §10 원칙 복원.

## BOOTSTRAP-001 (RESOLVED) — 1차 구현(수집→필터→군집→수요→공급→제목) 완료
기록(240개 테스트). 해당 파이프라인은 PROJECT-002로 삭제됐다 — 역사 기록.

---

## GOLDEN-002 — 골든셋 승인 기준선 3건 전부 기각: "추상 결합 불성립" 기각 템플릿이 판정 라인을 골든셋과 어긋나게 확장
- 상태: OPEN(판정 라인 재정렬은 세션 판정 권한 내에서 2026-09-08부터 적용;
  `config/golden_set.csv` 자체의 변경은 §2 규칙10상 문서·회귀 QA·인수 기준
  동시 수정이 필요한 계약 변경이라 사용자 결정 사항으로 보류)
- 발견: 2026-09-08, RUN-20260908-160112-KST 라운드 종료 시 골든셋 카나리아
  4/7 일치(57.1%) → recheck 트리거(절차상 정상 작동). 불일치 3건이 모두
  승인 기준선(기대 승인, 실제 기각):
  - `Falcon Ledger` — 기각 사유 "팔콘 장부 결합은 Falcon 추상 결합 불성립"
  - `Quantum Notary` — 기각 사유 "퀀텀 공증인 결합은 Quantum 추상 결합 불성립"
  - `Ledger Sentinel` — 기각 사유 "장부 파수꾼 결합은 Sentinel 추상 기각 계열 불성립"
- 구조적 이상 신호(이 사례의 핵심): `Ledger Sentinel`(승인 기준)과
  `Ledger Watchman`(의미중복 기각 기준)은 한 대조쌍인데 둘 다 기각됐고,
  사유가 "장부 파수꾼 결합은 X 추상 기각 계열 불성립"으로 영어 단어만
  바뀐 동일 문맥이었다. 대조쌍의 승인 쪽이 먼저 기각되면 Watchman의 기각
  근거(Sentinel과의 의미 중복)도 함께 무의미해진다 — 승인/기각의 구분 없이
  같은 템플릿을 둘 다에 적용한 것. 이것은 PROJECT-004 재발 방지 계획 2번
  (거절 사유 고유 개수 대비 거절 건수 비율 게이트 — 아직 미구현)이
  노리던 "규칙 엔진화" 신호가 외부 위임이 아닌 세션 자체 판정에서
  관측된 첫 사례다.
- 방향 비대칭(구조적 공백): `review_titles_recheck`는 이번 라운드의
  "승인"만 재검토한다 — 과잉기각 방향은 카나리아 불일치 검사가 유일한
  탐지기이고, 카나리아가 기각되면 재검증망 없이 불일치로만 남는다.
  이번 라운드가 정확히 이 경로였다.
- 해석: Evaluation 라인(실측 승자 패턴) 중심으로 판정이 좁혀지는 과정에서
  "X 추상 결합 불성립" 기각 템플릿이 골든셋 합격 기준선의 정의("명확·
  비중복·상표 무관이면 승인")보다 앞서 확장됐다. 기능어가 구체 서비스를
  지시하면(Ledger=회계, Notary=공증, Tracker=추적) 도메인어가 은유·수식어
  (Falcon, Quantum, Sentinel)여도 제목은 명확하다. KP 통과 실측도 이를
  뒷받침한다 — Furnace Tracker(3600/월), Practice Certification(2900/월)은
  모두 "구체 기능어 + 직관적 도메인어" 결합이다.
- 세션 권한 내 대응(2026-09-08부터 적용, `memory/HANDOFF.md`에도 기록):
  ① 기능어가 구체 서비스를 지시하는 은유·수식어 결합은 명확·비중복·상표
  무관이면 승인(골든셋 기준선 정합). ② 불성립 기각은 결합이 실제 서비스
  대상을 만들지 못할 때로 한정(Guitar Nexus, Guest Tuner 등 — 이번
  라운드 기각분은 유지). ③ 거절 사유가 상표·중복이면 checks의 해당 필드를
  정확히 false로 표기 — 이번 라운드 Slack Messenger 기각이 reason에는
  "유명 상표 Slack 유사"라 쓰고 trademark:true로 제출된 불일치 관측.
- 사용자 결정 사항: golden_set.csv를 현재 기준으로 유지하고 판정 라인이
  기준선에 맞춰 재정렬되게 할지(현재 적용한 방향), 골든셋 자체를 갱신할지
  (§2 규칭10 절차 필요). 재정렬 적용 후 다음 라운드 골든셋 7/7 회복
  여부가 재정렬이 올바른지의 1차 실측 신호다.
