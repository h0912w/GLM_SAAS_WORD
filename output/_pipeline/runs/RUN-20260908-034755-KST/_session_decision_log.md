# RUN-20260908-034755-KST 세션 결정 로그 (2026-09-08)

## 라운드 요약
- 생성 10,000 / 1차 승인 1,152(청크 50개) / 레드팀 재검증 1,150건 전면 반박 →
  45건 반박 성립(3.9%) → 최종 승인 1,105 / KP조회 1,105 / KP통과 13(0.13%).
- 정체 점검 `stagnant`(직전 0.12% 대비 +8.3%). 승인율 이상탐지 정상(z=-1.87).
- 은퇴 신규 0건. 자가확장(expand_word_bank) 미발동 라운드.

## 결정 1 — 골든셋 카나리아 불일치(Ledger Sentinel)를 세션 판정 드리프트로 판정
- **현상**: 카나리아 `Ledger Sentinel`(골든셋 정답 승인)을 첫 청크에서
  "Sentinel은 Monitor/Tracker와 의미 중복"으로 기각 → 6/7 일치(85.7%)로
  재검증 트리거.
- **분석**: 의미중복 기준의 오적용. 의미중복은 배치·ledger 내 실제 기존 승인
  제목과의 실질 중복이 기준이고, 추상적 유의어 관계만으로 기각하는 것은
  기준선(74라운드 누적)에서의 이탈이다. Sentinel은 파수·감시 도구 은유로
  독립 성립하며 실제 제품명 관례(Microsoft Sentinel)도 있다.
- **결정**: 세션 판정을 골든셋에 맞춰 정렬한다. Sentinel/Watcher/Guardian
  계열은 동의어 접기(DUP fold) 대상에서 제외하고 독립 도구 은유로 판정.
  `memory/WORD_GENERATION_LEARNINGS.md` 라운드 로그에 판정 프로토콜 정정
  기록. 골든셋 파일 자체는 수정하지 않는다(고정 카나리아 원칙).

## 결정 2 — 재검증 45건 반박(초기 청크 판정 정정)
- 반박 근거별 분류: 자격증명군(Biometric 2), 건축 Account/Agreement/
  Eligibility 앵커 미확정 9건, 증상군(Cavity 2), 구조물(Column 2), 수식
  형용사(Consecutive/Prior/Public 6), 기간 개념(Quarter/Excess 4), 해충군
  (Rodent 2), 문서 산출물(Obituary 1, Syllabus 2), 정크 패턴(Igniter
  Followup 1), 물질군(Oil/Refrigerant/Refill Usage 3), follower 위반
  (Gate/Recipe/Ticket Usage 3), Flow 앵커(Stock Flow 1).
- **의의**: 반박 관점이 같은 라운드 초반부의 느슨한 승인을 후반부에서 확립된
  가족 규칙으로 정정했다. 2026-08-31 도입 재검증 구조의 실측 효과 첫 확인.
- 유지 1,105건은 가족 규칙 정합 판정으로 반박 불성립 확인(전수 재독립 검토).

## 결정 3 — recheck 요청 1,150건 vs 세션 집계 1,152건 차이(2건) 처리
- 원인: 카나리아 7종 중 세션 청크 집계에 섞였던 항목과 중복 제거 차이로
  추정. 응답은 요청 `items`의 실제 title 집합 기준으로 작성해 구조 검증 통과.
- 교훈: 판정 응답은 세션의 내부 집계가 아니라 요청 파일의 실제 항목 집합을
  기준으로 커버리지를 단언(assert)해야 한다.

## KP통과 13건
Debit Note 33,100 / Debit Memo 5,400 / Application Usage 5,400 /
Electrical History 3,600 / Concrete History 2,400 / Formula Capacity 2,400 /
Loading Capacity 2,900 / Payload Capacity 2,900 / Remittance Tax 2,900 /
Prior Approval 1,300 / Ceramic Usage 1,300 / Class Usage 1,300 /
Material Usage 1,900 — 전부 경쟁지수 0.
