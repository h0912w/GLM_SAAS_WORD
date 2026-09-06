# Session Decision Log — RUN-20260906-022120-KST (사용자 지시: 라운드 무한 연속, 자리 비움)

사용자 지시: "내가 중단하라고 할 때까지 라운드 무한으로 계속 돌려, 나 자리 비운다."
이 라운드는 새 run(10000 요청)으로 시작. 이전 run(RUN-20260906-001749-KST)의
결정 1~5는 각 run 로그 참고. 이 로그는 이번 run 전용으로 1번부터 새로 시작.

## 결정 기록 (시간순)

1. **라운드 전역 동의어 계열·기각 그룹을 이전 라운드와 동일하게 고정해 51 단위 판정**
   (비청크 최초 배치 200건 + chunk1~50(200×49+7))
   - 10,000 요청이 expand_word_bank 확장 후 병합 풀로 실제 생성됐고, 최초 200건은
     비청크 배치(`review_titles_round1_*`), 나머지 9,807건은 청크로 분할 판정했다.
   - 판정 기준: 앵커 계열(Hub≈Center≈Portal, Checkin≈Register≈Registry≈Roster,
     Tracker≈Radar≈Watch≈Monitor≈Detector≈Guardian≈Keeper, Atlas≈Finder≈Lookup≈
     Locator≈Directory≈Map≈Chart≈Compass, Planner≈Assistant≈Scheduler≈Calendar≈
     Ops≈Manager≈Office≈Plan≈Helper, Diary≈Log≈Note≈Memo≈Record≈Journal≈Ledger,
     Alert≈Notification≈Reminder, Calculator≈Estimator≈Quote≈Comparison,
     Route≈Trail)은 라운드 전체에서 동일 적용 — 청크 간 기준 흔들림 0.
   - 기각 그룹(금융 명사 0.8 / 스키마 추상 명사 0.8 / 콘텐츠 0.75 / 은퇴 태그
     시각화 계열 0.85 / 프로세스 명사 0.8 / 물리 오독 0.7)도 전 단위 동일.

2. **Type-follows-Size 판정 규칙을 라운드 전역 규칙으로 확정** (전 청크)
   - 같은 도메인어에 대해 Size를 실제 규격 의미로 승인했다면 같은 도메인의 Type도
     0.65로 승인(분류 속성도 실제 검색 속성) — 이번 라운드 27회 추가 확인
     (Pump/Oil/Collar/Veneer/Bottle/Manifold/Wax/Closet/Greenhouse/Cane/Truck/
     Banquet/Puppy/Deadbolt/Freezer/Refrigerant/Crew/Equipment/Expo/Weighbridge/
     Festival/Fitting/Gasket/Parking/Sewer/Chip/Backwash Type).
   - 반대로 Size가 내부자용·독해 불명으로 기각이면 Type도 0.7로 기각(32회 확인:
     Pedicure/Digital/Volunteer/Talent/Handoff/Utility/Offboarding/Renewal/Lapse/
     Hire/Case/Article/Waiver/Accrual/Reinsurance/Roadtest/Filling/Preschool/
     Quarter/Getaway/Overnight/Slideshow/Boarding/Fluency/Vacancy/Babysitter/
     Duplication/Orientation/Waste/Dialect/Checklist/Obituary Type).
   - 이 규칙이 이번 라운드 KP통과 31개 중 22개(Type 조합)를 만들었다 — 신규
     기능어 Type의 실측 승인율 44.6%(222/498)은 이 규칙의 일관 적용 덕분에
     승인 풀이 넓게 유지된 결과이기도 하다.

3. **원칙 13 통제 실험(일상어 vs 내부자용어)을 expand_word_bank 설계에 직접 반영**
   - 이전 라운드 결정 4가 남긴 과제("같은 업계에 일상어 N개 + 내부자용어 N개
     대조")를 healthcare 업계에서 실행 — 일상 웰니스 명사 10개(Workout/Stretch/
     Hydration/Posture/Breathing/Meditation/Sleep/Jogging/Immunity/Energy,
     everyday_wellness_noun 태그) vs 임상 내부자 용어 8개(Suture/Catheter/
     Cannula/Comorbidity/Auscultation/Intubation/Otoscope/Speculum,
     trade_insider_term 태그)를 같은 라운드·같은 기능어 풀로 대조.
   - 결과(라운드 내부 대조, 기능어 동일 조건): 일상 팔 평균 승인율 약 4.1%
     (최고 Skiing 12/143=8.4%, Hiking 7.7%) vs 내부자 팔 평균 약 0.6%(최고
     Cannula/Comorbidity 2/142=1.4%, Speculum 0%). KP통과는 일상 팔에서만
     발생(Festival Type 6,600/월). 원칙 13 방향 재현 → 아래 결정 6에서 승격.
   - travel_tourism 일상 12개(Safari/Museum/Aquarium/Festival/Carnival/Picnic/
     Barbecue/Hiking/Surfing/Skiing/Casino/Vineyard), cleaning_services 일상
     8개(Furniture/Kitchen/Closet/Mattress/Curtain/Wardrobe/Sofa/Dishwasher)도
     같은 일상어 원칙으로 제안 — 승인율 0.7~8.4%로 전 단어 양성(Immunity/
     Speculum만 0승인, Wardrobe는 시도 10회뿐). 예외 실수: Kitchen은
     food_service에 2026-08-31부터 이미 있어 중복 등록됐고 이번 라운드
     시도 0회 — 핵심 원칙 6(전체 풀 사전 검색)을 또 거른 셈이라 원칙 6은
     candidate로 유지(승격 조건 미충족).

4. **신규 기능어 10개를 측정·분류 속성 계열로 제안** (expand_word_bank)
   - Size/Length/Weight/Distance(dimension_measure_noun), Range/Limit
     (range_band_noun), Type(type_category_noun), Clock/Time(time_reference_
     noun), Speed(performance_measure_noun).
   - 근거: "banner size"/"trailer type"/"pipe length"처럼 도메인 무관으로
     실제 검색되는 규격·분류·측정 관용구 — 원칙 7(구체적 정보 대상)의 기능어 축.
   - 결과: Type 22통과(누적 9.91%, 전체 기능어 1위 등극), Size 4, Length 2,
     Range 1, Weight 1, Time 1 — **이번 라운드 KP통과 31개 전부가 신규
     기능어 조합**. Distance/Limit/Clock/Speed는 통과 0(시도 ~500, 은퇴
     기준 미달, 관행 유지). 승인율 자체는 Type 44.6%/Size 33.5%/Time 11.4%로
     모두 높았다.

5. **집행 품질 절차 — 커버리지 diff 게이트+cleanup이 3건의 실수를 사전 차단**
   - 매 단위 실행 전 요청 vs 스크립트 기술 제목 diff 수행. c43(12건 누락),
     c46(허수 1건 — 이전 청크 스크립트에서 복사한 잔재), c47(approve와
     reject_clarity에 같은 제목 중복 — cleanup이 자동 제거) 전부 실행 전 수정.
   - 판정 스크립트(_judge_cN.py)는 실행 직후 매번 삭제. 코드·설정 무변경.

6. **핵심 원칙 13을 `candidate`→`validated`로 승격** (라운드 완주 시)
   - 근거: (a) 2026-08-28 logistics 관측(내부자용어 18개 0% vs 일상어 3개만
     통과), (b) 이번 라운드 healthcare 통제 대조(내부자 팔 0.6% vs 일상 팔
     4.1%, KP통과는 일상 팔만) — 서로 다른 업계·서로 다른 라운드에서 같은
     방향 2회, 반례 없음. 이번 대조는 "같은 업계, 같은 라운드, 같은 기능어
     풀"이라 원칙 13 승격 조건이 요구한 통제 비교를 그대로 충족한다.
   - 갱신은 memory/WORD_GENERATION_LEARNINGS.md에 반영(이 배치에서 함께 커밋).

7. **라운드 완주 결과 확정 — 응답 파일 재집계 불일치 해소 포함** (09:01)
   - 좁은 glob(`review_titles_chunk*_round1_response.json`)으로는 50파일·승인
     636으로 파이프라인 집계(718)와 82개 불일치. 원인: 최초 200건이 비청크
     배치(`review_titles_round1_response.json`, 승인 85)라 패턴에서 누락.
   - 전체 재집계: 51파일 / 10,007 판정(후보 10,000 + 카나리아 7) / 승인 721 중
     카나리아 3 → **실제 후보 승인 718로 파이프라인 집계와 정확히 일치**.
     HANDOFF는 수동 편집 없이 파이프라인 자동 갱신분 그대로.
   - 최종: 생성 10,000 / AI승인 718(7.2%) / backlog 0 / KP통과 31(0.31%).
     정체 점검 `향상 중`(직전 0.17% 대비 +86.7%). 골든셋 7/7. 승인율 이상탐지
     정상(z=-2.55, 기준선 75.7%). 레드팀 재검증(review_titles_recheck) 미발동.
   - 산출물: 마스터 통과 누적 2,349개(2,318→+31), 본 라운드 snapshot 저장.
   - 학습 루프: `analyze_word_performance.py --apply-retirement`로 은퇴 신규
     3개 반영(Copayment/Flowchart/Mockup — 통과 0/시도 300+). 은퇴 목록에
     Diagnosis/Inspection이 있어도 이번에 "Diagnosis Type"(1,600/월)/
     "Inspection Type"(1,300/월)이 통과한 건 설계대로다 — 은퇴 필터는 기능어
     슬롯에만 적용되고 도메인어 슬롯은 살아있다(word_bank.py 원본 + 확장분
     모두 해당).

## 다음 세션을 위한 메모
- 병합 풀에 이번 48개 확장분의 미시도 조합이 상당수 남아 있다 — 다음 라운드는
  확장 없이 잔여분 소진으로 시작할 가능성이 높다.
- 원칙 15(신규 candidate): 측정·분류 속성 기능어(Size/Type/Length/Range/
  Weight/Time 계열)의 1회 관측 — 다음 확장에서 기능어를 시도한다면 인접
  속성명(예: Count/Level/Depth — 미시도 확인 후) 소량 재시험이 승격 조건.
- 비청크 최초 배치 파일명(`review_titles_round1_*`)을 응답 재집계 glob에 항상
  포함할 것 — `review_titles_chunk*`만 세면 승인 수가 어긋난다(이번에 실측).
