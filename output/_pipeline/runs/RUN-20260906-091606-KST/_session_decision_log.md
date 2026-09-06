# RUN-20260906-091606-KST 세션 판정 결정 로그

작성: main-orchestrator (2026-09-06, 라운드 DONE 직후)
범위: 이 라운드에서 현재 세션이 내린 모든 AI 판정·해석 결정과 그 근거

## 1. 라운드 수치 확정

- 생성·판정 총 9,772건(49개 배치: 비청크 `review_titles` 200건 + 청크1~47 각 200건
  + 청크48 172건). 이 중 골든셋 카나리아 7건 포함(ledger 미기록) → 실제 후보
  9,765건(round_history `generated`와 일치).
- 1차 승인 응답 604건 = **실제 승인 602건 + 카나리아 승인 2건**(Falcon Ledger,
  Ledger Sentinel — 정답이 승인인 카나리아, ledger·recheck 대상 아님 — 정상).
- 승인율 6.2%(602/9,765). 콘솔 승인율 이상탐지: 정상(z=-2.46, 임계 ±3.0).
- `review_titles_recheck`(반박 전담) 602건 전부 재검증 → **602/602 확인 유지**.
  트리거는 골든셋 불일치 1건(아래 §3).
- Keyword Planner 통과 18건, 라운드 통과율 0.1843%(직전 0.3100% 대비 -40.5%,
  정체 점검 판정 `declining`). 누적 통과 표 2,367행.

## 2. 판정 기준 적용 결정(1차 + recheck 공통)

- 패밀리 앵커(도메인당 1승인): Hub≈Center≈Portal, Checkin≈Register≈Registry≈
  Roster≈Counter≈Entry≈Check, Tracker≈Radar≈Watch≈Monitor≈Detector≈Guardian≈
  Keeper, Atlas≈Finder≈Lookup≈Locator≈Directory≈Map≈Chart≈Compass,
  Planner≈Assistant≈Scheduler≈Calendar≈Ops≈Manager≈Office≈Plan≈Helper≈
  Companion, Diary≈Log≈Note≈Memo≈Record≈Journal≈Ledger≈Recorder,
  Alert≈Notification≈Reminder≈Message, Calculator≈Estimator≈Quote≈Comparison,
  Route≈Trail. Checker·Timer는 앵커 아님(Curtain Timer, Barbecue Timer를
  Hiking Timer 선례로 승인).
- Type-follows-Size 연쇄: Size가 실제 규격으로 승인된 도메인의 Type/Length 등
  속성 후보를 0.65로 승인 — Trailer/Lighting/Meter/Padlock/Softener/Harvest/
  Blower/Bucket/Production/Opening/Landscaping/Freight/Driver/Mowing/Archive/
  Creative(광고 소재)/Sofa 등.
- 배치 청킹 게이트: 각 청크 응답 작성 전 사전 게이트(사전 내 중복 키·사전 간
  교차 중복·누락/과잉 검사)를 실행 — c44/c47/c48에서 실제로 결함을 잡아 수정 후
  제출(§4). 대량 사전을 한 번에 쓸 때의 낙방·복사 실수를 구조적으로 차단.
- 이번 라운드 신규 선례: Curtain Calculator(원단 치수), Aquarium Ticket/Festival
  Entry/Festival Plan, Implant Size(치과 소비자 — 임상 내부자 예외), Hiking
  Forecast, Aquarium Sample(수질), Skiing Inventory(렌탈 재고), Furniture Check
  (검수), Mattress Trial(sleep trial 업계 표준), Safari Calendar, Aquarium Pass,
  Museum Card, Vocabulary/Bulk/Coloring/Naptime/Storytime/Nutrition/Soil Size,
  License Type.
- **Collocation-strength 예외**: Transmission Speed는 승인(전송 속도 독해가
  지배)하되 Transmission Size/Type은 거절(다의) — 같은 도메인어라도 조합별
  독해 강도로 판단한다는 원칙의 첫 명시적 적용.

## 3. 골든셋 불일치 1건 — 원인과 조치

- **Quantum Notary**(정답: 승인)를 1차에서 clarity 실패(0.85)로 거절 — "기술
  유행어+공증 조합, 제품 불명확"이라 판독. 카나리아 근거(명확·비중복·상표 무관)
  과 충돌 → 6/7 일치로 레드팀 재검증이 자동 트리거됨(설계대로 작동).
- 해석: 신기술 도메인어(quantum 등)를 "유행어"로 읽어 clarity를 과도하게 엄격
  적용한 판정 드리프트. 나머지 6개 카나리아는 전부 정답과 일치.
- 조치: 본 로그에 기록 + 판정 기준 정정 — **clarity 거절은 "합리적 제품 추론이
  아예 불가능"한 경우로 한정하고, 실재하는 기술 카테고리를 가리키는 단어는
  그 카테고리로 읽어준다**(Data Thing류 진짜 추상어와 구별). 재판정은 하지
  않음(1차 거절은 확정, 카나리아는 ledger에 기록되지 않음).

## 4. 응답 구조 결함과 게이트(자기 검증 기록)

- c44: 교차 사전 중복 1건(Blower Size가 approve와 reject_clarity 양쪽) → 수정.
- c47: 교차 중복 1건 + 사전 내 중복 3건 + 미존재 제목 1건(Mowing Length 환각)
  → 게이트 전 자체 발견, 5건 수정. 이후 MISSING 1건(Combination Weight)
  추가 발견 → 보강.
- c48: 교차 중복 4건 + 누락 3건(Driver Clock, Freight Time, Roaming Time)
  → 5건 수정.
- 교훈(재확인): 200건짜리 판정 사전을 한 번에 작성하면 누락·복사 실수가 발생
  한다 — 실행 전 게이트가 매번 결함을 잡았으므로 절차로 유지.

## 5. 원칙 재검증(principle_reverification) 해석·반영

보고서 15개 원칙 전수 반박 검토 결과, 이번 배치에서 문서에 반영한 것:

- **원칙1 재정리**: "소량·금융거래 표면형 기본전략" 하위 규칙을 기본전략에서
  강등(누적 20시도 중 4적중=16~20%, Profit/Toll 즉시은퇴). 기본 축을
  속성/식별 관용구(원칙7·15)로 교체하고 금융 명사는 차선책으로 재분류.
- **원칙7 승격(candidate→validated)**: RUN-20260823-030806 최초 관측 +
  RUN-20260906-022120 재현(31통과 전부가 Type/Size/Length/Range/Weight/Time)
  — 2라운드 방향 관측 + 반례 없음. 원칙15와 통합 서술로 정리.
- **원칙10 범위 축소**: Flowchart 은퇴(0/300+)로 시각 구조 계열이 "시각 문서
  전반"이 아니라 diagram/graph 단일어 관용구로 좁아짐을 명시(Diagram 누적
  8.18% 상위권은 유지).
- **원칙13 단서 추가**: B2C 소비자가 전문용어를 그대로 검색하는 업계(부동산
  Escrow류)에서는 역전 가능성 — 반례 감시 대상으로 명시.
- **원칙6 정정**: 보고서가 제안한 "기존 전체 단어 목록 코드 주입"은 **이미
  구현돼 있음**(`word_pipeline._write_expand_word_bank_request`가
  `existing_domain_words`/`existing_function_words`를 요청에 포함,
  word_pipeline.py:683-704 실측 확인). 2회 연속 중복등록(RUN-20260821
  Reserve/Audit/Gate, 직전 라운드 Kitchen)은 데이터 부재가 아니라 판정자가
  주입된 목록을 실제로 대조하지 않은 **실행 실패** → 원칙6을 "제안 확정 전
  주입된 풀에 각 후보를 기계적으로 대조" 절차로 재작성. 저장 시점 중복 경고
  코드화는 별도 배치에서 QA와 함께 검토(HANDOFF 등재).

## 6. 정체 신호(declining) 해석

- 18통과 vs 직전 31통과: 절대 수가 작아 표본 noise가 크고(포아송 기준 ±편차가
  통과율 변동의 상당 부분 설명), 승인율도 6.2%로 소폭 하락, 승인 1건당 KP
  통과율도 3.0%(18/602)로 하락(직전 4.3%).
- 해석: 승자 기능어(속성 계열) 조합이 빠르게 소진되며 남은 조합 풀의 기대
  품질이 낮아지는 방향 + 이번 라운드 신규 기능어 부재(기존 풀 소모 라운드).
- 대응: (a) 다음 라운드에서 속성 계열 인접 후보(Count/Level/Depth/Capacity —
  원칙15 승격 조건)의 독립 시험 기회가 오면 우선 설계, (b) 코드 권고(누적
  70라운드 도달, 원칙 전체 재도출 검토)를 HANDOFF에 등재해 다음 긴 정지 구간에서
  실행, (c) KP 게이트 임계값은 건드리지 않음(§4 학습 루프 조정 대상 아님).

## 7. 미결 항목

- expand_word_bank 발생 없음(조합공간 소진 없이 9,765건 생성) → 라운드별 로그
  append 의무 없음.
- 원칙 전체 재도출(드리프트 방지, 70라운드 도달 권고) → HANDOFF에 다음 정지
  구간 작업으로 등재.
- 저장 시점 중복 경고(원칙6 구조 개선 후보) → HANDOFF에 별도 배치 작업으로 등재.
