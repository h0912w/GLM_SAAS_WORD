# RUN-20260907-165913-KST 세션 판정 결정 로그

작성: main-orchestrator (2026-09-07, 라운드 DONE 직후)
범위: 이 라운드에서 현재 세션이 내린 모든 AI 판정·해석 결정과 그 근거

## 1. 라운드 수치 확정

- 생성·판정 총 10,007건(51개 판정 단위: 비청크 `review_titles` 200건 — 골든셋
  카나리아 7건 포함 — + 청크1~50 각 200건 + 청크51 7건). 실제 후보 10,000건
  (round_history `generated`와 일치).
- 1차 승인 813건(8.13% — 전원이 실제 후보, 카나리아 승인 0건).
- `review_titles_recheck`(반박 전담) 813건 전부 재검증 → **105건 뒤집기
  (clarity 31 + trademark 2 + duplication 72), 708건 유지**. 최종 승인율
  7.08%(708/10,000).
- 재검증 트리거: **골든셋 카나리아 불일치 3건**(4/7 일치). 승인율 이상탐지는
  정상(z=-2.17), 낮은 confidence 승인 없음 — 3종 OR 게이트 가운데 골든셋
  경로의 실발동 사례(직전 라운드는 confidence 경로 — 경로가 매번 다르게
  발동되는 중).
- Keyword Planner 통과 14건(누적 표 2,386행, 누적 통과율 0.92% = 2,386/
  259,623), 라운드 통과율 0.1400%(직전 0.0500% 대비 +180%, 정체 점검
  `improving`). 은퇴 반영 실행: 신규 0개.

## 2. 재검증(반박 판정) 결정 — 105건 뒤집기의 구성

- **사유-제목 불일치 31건(clarity)**: 1차 승인 사유가 전혀 다른 제목의 내용을
  서술(예: Accreditation Pressure의 사유가 심야 이사 물량 서술). 불일치
  승인은 무효로 보고 제목을 독립 재판정 — 대부분 "의미 불명/장비·시공 사양"
  (Airflow Depth, Equipment Width, Snake Pressure, Terminal Brightness,
  Slideshow Voltage/Wattage, Mulch Duration, Orchard Nomination 등)으로
  뒤집혔다. 유효한 제목은 유지(예: Equipment Temperature, Hotspot
  Simulator — 통신 업계 맥락 성립).
- **동일 앵커 Frequency→Load 소급 귀속 50건(duplication)**: 1차 판정이
  동일 앵커의 Frequency+Load 쌍을 둘 다 승인한 것을, 청크 선례 30건 이상
  (Callback chunk48 등 — 전부 "Frequency가 Load로 귀속", 역방향 0건)에 따라
  Load 앵커를 남기고 Frequency를 의미중복 처리. Admission/Alarm/Applicant/
  Arbitration/Assignment/Bike/Checkout/Client/Compensation/Custodian/
  Database/Daycare/Diagnosis/Disclosure/Doctor/Emergency/Endorsement/
  Endpoint/Equipment/Excursion/Exhibitor/Extraction/Feedback/Filing/
  Fluency/Funnel/Grazing/Interaction/Interview/Job/Licensing/Locksmith/
  Medication/Monitoring/Motor/Museum/Offboarding/Orchard/Phishing/
  Plumbing/Punchlist/Reimbursement/Request/Resort/Transfer/Underwriting/
  Venue/Vet/Waybill + Hold Frequency→Hold Depth(대기열 앵커는 Depth —
  chunk13/28 선례).
  - **예외 판정(귀속하지 않고 유지)**: Frequency가 물리 수량이나 주기
    설정 의미인 조합 — Grid Frequency(전기 주파수 Hz), Battery/Evaporator
    병존(충전 패턴 vs 전기 부하), Payroll/Renewal/Amortization/Greenhouse/
    Compost/Crew/Menu/Election/Advisor/Vaccination/Ventilation/Voyage/
    Vesting Frequency(급이·수거·교대·지급·갱신 등 주기 설정), Vitals
    (측정 주기), Prototype(하중 시험 vs 제작 횟수), Headcount(인원 변동
    빈도 vs 수용 부하 — 별개 HR 지표).
- **가족 앵커·상표 뒤집기 24건(duplication)**: Dumbbell Planner→Scheduler,
  Ferry Planner→Scheduler(각 가족의 일정 앵커 — chunk16/13 선례), Inquiry
  Load→Request Load(chunk14), Medicine 3종→Medication 앵커, Toddler 2종→
  Infant 앵커, Cloud Temperature→Database Temperature(chunk16 서버실 온도
  계열), Heater Temperature→Filter Temperature(chunk16 수온 계열), Cloud
  Ping→Cloud Diagnostic(chunk13 Router Ping 선례), Cremation/Donation/
  Welding Volume→Load(Volume~Load 동의어 귀속), Tractor Estimator→Quote,
  Tractor/Welding Guarantee→Warranty, Stain Diagnostic→Stain Type,
  Welding Detector→Diagnostic, Welding Recorder→Tracker, Marina Lookup→
  Availability, Truck Frequency→Haul Frequency(동일 업계 동일 의미),
  Clearance Monitor→Alert(같은 가격 하락 감시 — chunk35 앵커).
- **상표 뒤집기 2건(trademark)**: Cloud Forecast(CloudForecast 동명 FinOps
  서비스 — Cloud Trail→AWS CloudTrail 선례와 동일 기준), Phishing Lab
  (PhishLabs 보안 회사). 대응 조정: Cloud Predictor는 Cloud Forecast가
  뒤집힌 뒤 가족의 생존 대표로 유지, Phishing Simulator는 훈련 앵커(Lab)
  소멸 후 독립 성립으로 유지.

## 3. 골든셋 카나리아 불일치 분석(3건 — 이번 재검증 트리거)

- **"Data Thing" 오승인(expected reject)**: 어떤 SaaS인지 추론 불가능한
  의도적 추상 조합을 승인 — 대량 청크 후반부 판정 기준이 느슨해진 흔적.
  실제 후보에 같은 기준 미끄러짐이 있었을 가능성(사유-제목 불일치 31건과
  같은 후반부 피로대)이 높다.
- **"Ledger Sentinel"·"Quantum Notary" 오기각(expected approve)**: 명확·
  비중복·상표 무관인 조합을 의미 불명으로 기각 — 낯선 도메인어 조합에
  "익숙한 업계 패턴이 아니다"라는 과잉 엄격이 작동. 1차 판정이 동시에
  양방향(느슨함+과잉 엄격)으로 표류했음을 보여준다.
- 대응: 다음 라운드 1차 판정에서 명확성 기준을 "합리적 제품 추론 가능"
  으로 재고정하고, 낯선 조합에 대한 기각은 "추론 불가능" 근거를 사유에
  명시할 것. 카나리아 3불일치는 ledger에 기록되지 않으며 판정 품질 신호로만
  사용(설계대로).

## 4. 승인 유지 판정의 대표 선례(708건 중)

- 재검증에서 살아남은 앵커 군: 각 업계의 Hub(8개), Monitor/Tracker 병존
  (Database/Hotspot/Phishing/Orchard — 감시 vs 추적 별개 앵커), Paycheck
  가족 12종(Alert=지급일 캘린더 vs Monitor=소득 변동 감시로 트리거가
  달라 병존 판정), Marina 가족 13종.
- KP통과 14건: Breathing Frequency 90,500 / Distribution Frequency 27,100 /
  Response Frequency 6,600 / Donation Progress 3,600 / Commute Time 2,900 /
  Marina Appointment 2,900 / Hotspot Tracker 2,400 / Snow Depth 2,400 /
  Amortization Expense 1,900 / Transfer Load 1,600 / Hotspot Status 1,300 /
  Rodent Type 1,300 / Ticket Load 1,300 / Utility Frequency 1,000.
  재검증에서 Load 앵커로 남은 Ticket/Transfer Load가 통과하고 소급 귀속된
  Frequency 쪽은 전무 — Load 앵커 우위 재관측.

## 5. 응답 구조 무결성

- 청크 응답 51개: 요청 순서 보장, 개수 일치(200/200/…/7), approve/checks/
  confidence/reason 스키마 준수, request_hash·stage·run_id 원본 복사 —
  파이프라인 구조 게이트 전부 통과(재요청 0건).
- recheck 응답: 813건 전원 기입, 뒤집기 105건의 checks 재계산(해당 기준만
  false), 유지 708건 "반박 불성립 - <1차 사유>" 기록, confidence 0.65/
  0.7. 파이프라인이 그대로 수용 → ledger 반영·KP게이트 진행 확인.

## 6. 세션 해석 결정

- `improving` +180% 해석: ① 승인 풀 순도 가설(재검증 반박으로 승인을 줄일
  수록 통과율 상승)이 3라운드 연속 같은 방향(465→5 / 602·718→31·18 /
  708→14 — 순위는 뒤섞이지만 "반박 비율 높은 라운드가 통과율 상위" 패턴),
  ② Breathing Frequency 90,500 같은 대형 조합의 운 효과가 크다. 단일
  변수 실험이 아니므로 원칙 승격 근거로 쓰지 않는다.
- 신규 `candidate` 2건 등재(원칙 16: 동일 앵커 F/L 즉시 귀속, 원칙 17:
  사유-제목 대조 절차) — 둘 다 이번 라운드 1회 관측이므로 candidate.
  다음 라운드에서 1차 판정에 적용해 재관측 후 승격 판단.
- 라운드 로그를 `memory/WORD_GENERATION_LEARNINGS.md`에 append 완료.

## 7. 남은 과제(다음 세션/라운드)

- 원칙 16·17을 다음 라운드 1차 판정에서 즉시 적용 → validated 승격 여부.
- 카나리아 오기각 2건 방향의 재발 여부 관찰(명확성 기준 재고정 효과).
- Depth 미시도(Capacity/Count/Level) 클린 시험은 여전히 미수행 — 다음
  확장 라운드에서 원칙 15 승격 판단용으로 소량 시험.
