# RUN-20260906-124747-KST 세션 판정 결정 로그

작성: main-orchestrator (2026-09-07, 라운드 DONE 직후)
범위: 이 라운드에서 현재 세션이 내린 모든 AI 판정·해석 결정과 그 근거

## 1. 라운드 수치 확정

- 생성·판정 총 10,007건(51개 판정 단위: 비청크 `review_titles` 200건 — 골든셋
  카나리아 7건 포함 — + 청크1~49 각 200건 + 청크50 7건). 실제 후보 10,000건
  (round_history `generated`와 일치).
- 1차 승인 573건 = **실제 승인 570건 + 카나리아 승인 3건**(Falcon Ledger,
  Quantum Notary, Ledger Sentinel — 정답이 승인인 카나리아, ledger·recheck
  대상 아님 — 정상).
- `review_titles_recheck`(반박 전담) 570건 전부 재검증 → **105건 뒤집기,
  465건 유지**. 최종 승인율 4.65%(465/10,000).
- 재검증 트리거: 골든셋 불일치 0건, 승인율 이상탐지 정상(z=-2.36) —
  **낮은 confidence 승인 26건**(chunk 30~31, 0.55)이 트리거. 3종 OR 게이트
  중 confidence 경로의 실발동 사례.
- Keyword Planner 통과 5건(Lighting Frequency 6,600 / Truck Height 1,900 /
  Truck Width 1,900 / Password Status 2,400 / Tractor Status 1,300), 라운드
  통과율 0.0500%(직전 0.1843% 대비 -72.9%, 정체 점검 판정 `declining`).
  누적 통과 표 2,372행. 누적 통과율 0.92%(2,372/258,915).

## 2. 판정 기준 적용 결정(1차 + recheck 공통)

- 명확성 승인 하한: "합리적 제품 추론이 가능한가" — 운영 모니터링 항목
  (콜드체인 온도·설비 압력/부하/전압·급여/보정/온보딩 주기·수술 시행 빈도 등)은
  승인, 정적 사양·규격(카야크 길이·격납고 중량·데드볼트 폭 등)과
  "구체 제품을 추론할 수 없는 추상 조합"은 기각.
- 기능어 계열별 처리: Frequency/Load/Compatibility/Temperature는 운영 지표
  문맥에서 0.6~0.65 승인, Voltage/Wattage/Brightness는 사양서 항목으로 읽혀
  사실상 전면 기각(승인 각 3/3/1건), Depth/Height/Width는 물체 치수 문맥
  기각 + 상한 관리 문맥(Truck Height/Width 등)만 승인.
- Type-follows-Size 등 직전 라운드 선례는 이번 라운드 후보 성격(속성·정격
  계열)에 맞게 제한적으로만 적용.
- recheck 반박 판정: 570건 각각을 명확성·의미중복·상표유사 기준으로 재독립
  검토. 뒤집기 105건 = clarity 뒤집기(정적 사양 치수 오판: Pallet Depth/
  Width, Wardrobe/Hinge/Coping/Curtain/Denture/Ductless 치수, Runway
  Authorization 등) + duplication 뒤집기(패밀리 앵커 중복: Donation
  Recorder→Donation Log, Ferry Radar/Watch→Ferry Tracker, Password/
  Router Check→Checker, Tractor Recorder/History→Tractor Log, Donation
  Log→History, Yoga Price→Cost 등). 유지 465건은 "반박 불성립 - …" 개별
  근거를 confidence 0.65로 기록.

## 3. 이번 라운드 신규 선례(1차 승인 중 대표)

- 운영 정격/속성: Building Wattage(전력 소비 모니터링), Pump Frequency(가동
  빈도), Truck Load(적재량), Surgery Frequency(수술 시행 빈도), Nursing Load
  (간호 배치 비율), Clearance Tracker(클리어런스 행사 주기).
- 규제 상한 치수: Truck Height/Width(적재 상한 관리 — KP통과로 실증).
- 도메인어: Amortization(상각 스케줄), Donation(세액공제 예측), Phishing(
  의심 메일 검증), Welding(조건·자재 소요), Prototype(RFQ 견적), Quarry(
  채굴권 인가) 등 일상·운영 자산 계열 전반.

## 4. 응답 구조 무결성

- 모든 청크 응답: 요청 순서 보장, 200건(청크50은 7건) 개수 일치, approve/
  checks/confidence/reason 스키마 준수, request_hash·stage·run_id 원본 복사.
- recheck 응답: 570건 전원 기입, 뒤집기 105건의 checks 재계산(clarity 또는
  duplication=false), 유지 465건 개별 반박 불성립 근거.
- 재집계 검증: 전체 응답 재집계 1차 승인 573 = 실제 570 + 카나리아 3 —
  파이프라인 최종 집계(465)와 정합.

## 5. 세션 해석 결정

- `declining` -72.9% 해석: ① recheck 반박 105건으로 승인 풀을 의도적으로
  줄인 선택의 결과(순도 유지 — 직전 라운드 관측과 같은 방향), ② 이번 확장
  계열(정격·치수)이 직전 계열(Type/Size 분류·규격)보다 시장 적합이 약했다는
  두 요인의 복합. 통과 5개 중 3개가 신규 기능어 조합이므로 확장이 무효였던
  것은 아님.
- 은퇴 반영 실행: 신규 0개 — 은퇴 판정의 "시도"는 KP캐시 기준이므로 1차
  승인이 적은 신규 기능어는 300회 도달까지 여러 라운드가 필요(구조상 정상).
- 원칙 15 `candidate` 유지: 승격 조건이 지목한 Depth 0통과로 "상위권 재현"
  미달. Frequency(주기)/Height·Width(규제 상한) 통과는 속성 계열 내 성립
  하위 패턴이 더 좁다는 1회 관측 — 원칙 본문 갱신은 다음 라운드 재관측 후.
- 라운드 로그를 `memory/WORD_GENERATION_LEARNINGS.md`에 append 완료(위
  내용의 학습 문서 버전).

## 6. 남은 과제(다음 세션/라운드)

- 다음 확장에서 Count/Level/Capacity를 사전기각 없이 클린하게 시험해 원칙 15
  승격 여부 재판단.
- "정적 치수 vs 상한 관리 치수" 대조의 반복 관측(원칙 등재 요건: 2회 이상).
- Voltage/Wattage/Brightness는 승인 표본이 쌓일 때까지 은퇴 판정 보류 상태 —
  300 KP조회 도달 시 자동 판정.
