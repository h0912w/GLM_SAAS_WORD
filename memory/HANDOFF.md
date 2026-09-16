# HANDOFF

- 상태: `PAUSED`(사용자 지시로 작업 중단, 세션 인수인계)
- 현재 단계: review_titles 청크 판정 진행 중 — **12/33 청크 완료, 파이프라인은 AWAITING_JUDGMENT 일시정지 상태(프로세스 없음)**
- 마지막 실행: run RUN-20260916-192833-KST (mode=production)
- 이번 라운드: 신규생성 6,513개(요청 10,000 미달 — 병합 단어뱅크의 미시도 조합 부분 소진) → 청크 33개, 판정 완료 12청크 2,400건(승인 1,082/기각 1,318), ledger 미기록
- 저신뢰 승인(confidence<0.6) 241건 확인 → 전체 판정 완료 후 `review_titles_recheck` 트리거 확실
- 골든셋 카나리아: 청크 0 에이전트 보고 7/7 일치(파이프라인 집계는 집계 단계에서 확정 예정)

## 다음 세션 할 일(순서대로)
1. 남은 청크 12-32(21개, 4,200건) 판정 — 요청 파일이 이미 모두 생성돼 있음
   (`output/_pipeline/runs/RUN-20260916-192833-KST/judgment/review_titles_chunkN_round1_request.json`,
   N=12..32). 파이프라인 코드 경로로 사전 생성된 것이므로 `--resume` 시 요청 재작성 없이
   기존 파일의 request_hash로 응답을 소비한다. 판정은 포크 에이전트 6개씩 병렬 위임
   (429 방지), 각 에이전트가 `{stage}_round1_response.json`을 직접 작성 — 선례 템플릿은
   이전 세션 대화 또는 `docs/architecture/06-agents-and-role-separation.md` 참고.
   이미 완료된 청크 0-11(12개)은 응답 파일 존재 + 해시 검증 통과 상태라 재판정 불필요.
2. 전부 완료되면 `.venv/Scripts/python.exe run.py --mode production --resume` 실행
   (백그라운드) → 청크 순차 소비 → 집계 → recheck 요청 나오면(예상됨) 200건 단위로
   분할해 반박 전담 병렬 위임 후 병합(RUN-20260915 라운드에서 확립된 절차) → KP 게이트
   → 4문서 갱신 → 정체 점검 확인.
3. 라운드 완료(DONE) 후 커밋·푸시, 그 다음 `python run.py --mode production`으로 다음
   라운드. 이때 신규 생성이 0개면 `expand_word_bank` 판정이 열리는 정상 경로다.
4. 이 라운드에 `expand_word_bank`는 없었으므로 `WORD_GENERATION_LEARNINGS.md` 로그
   append 대상 아님.

## 판정 경향(이번 라운드 관측, 다음 세션 위임 프롬프트에 반영済)
- 기능·속성 라벨 결합(Mode/Login/Spec/Tab/Item/Unit/Quota/Quantity)과 요금 속성
  결합(Fee/Cost/Price/Tax/Fare/Loan/Sum/Debt)은 대량 명확성 기각 — 승인율 31~55%대.
- 구체 서비스형 기능어(Analysis/Workbook/Report/Coach/Journal/Pass/Calendar/
  Tracker/Notary) 결합은 승인. 동일 앵커 유의어쌍(Advice↔Tips, Finder↔Locator,
  Report↔Log, Planner↔Scheduler 등)은 선출 1건 유지·후행 의미중복 기각 —
  GOLDEN-002 재정렬 라인과 Frequency/Load 규칙 준수 확인됨.
