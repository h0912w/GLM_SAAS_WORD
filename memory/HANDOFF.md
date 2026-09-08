# HANDOFF

- 상태: `RUNNING`(사용자 지시 "단어 생성 작업을 사용자 중단 시까지 무한 반복 진행" 이행 중 — 라운드 연속 수행, 2026-09-09 시작)
- 직전 실행: run RUN-20260908-214143-KST (mode=production, round-size 10000) — **정상 종료 EXIT=0**
- 직전 라운드: 신규생성 10000개, 1차 AI승인 1697개 → 레드팀 재검증 109건 기각 → 최종 AI승인 1588개, backlog반영 0개, Keyword Planner통과 1개(Immunization Handbook 6600/월·경쟁지수0)
- [2026-09-09 세션 시작 조치] 원칙 재검증 보고서 5건 반영 완료(memory/WORD_GENERATION_LEARNINGS.md): (a) 원칙 14 → **validated 승격**(Questionnaire 2건 + Tutorial/Handbook 첫 실측 통과, 반례 없음) (b) 원칙 2 교란 주석 추가 — 일상어 한정 재시험 전 확정 근거 인용 금지 (c) 원칙 7/15 순환성 복원 결정 — "실재 도구를 지시하는 속성 결합은 세 기준 통과 시 승인, 블랭킷 기각 금지"(GOLDEN-002 재정렬 라인의 속성 축 확장, 다음 청크부터 적용) (d) 원칙 16 Load 명확성 전제 명시 개정 (e) 핵심 원칙 전체 재도출은 **유예** — 사용자 지시상 라운드 연속 수행이 우선이며, 라운드 연속 수행이 중단되는 시점에 최우선 검토.
- [원칙 재계산 권장(누적 80라운드, 계속 유효)] memory/WORD_GENERATION_LEARNINGS.md '핵심 원칙' 전체 재도출 — 위 (e)에 따라 유예 중.
- [골든셋 카나리아] 직전 라운드 6/7 일치 (85.7%), 불일치 1건 — **golden_set.csv 유지/갱신은 사용자 결정 사항**(GOLDEN-002), 임의 갱신 금지. 재정렬 라인 적용 후 골든셋 7/7 회복 여부가 재정렬 타당성의 1차 실측 신호.
- [승인율 이상탐지] 직전 라운드 정상: 17.0% vs 기준선 평균 66.8%(표준편차 33.4, z=-1.49, 임계 ±3.0)
- [학습 정체 점검] 직전 라운드 저하: 최근 1라운드(생성 10000개) 통과율 0.01% vs 이전 1라운드(생성 5108개) 0.16% (상대변화 -93.6%, 임계값 ±10%) — 해석: 능력 저하 아님, 신규 확장어(niche B2C) 후보 쏠림 + 재검증 109건 기각 + 직전 라운드 금융 고점 대비의 기계적 결과(WORD_GENERATION_LEARNINGS 라운드 로그 참고)

## 이어지는 라운드의 핵심 검증 과제(직전 라운드 HANDOFF에서 승계)

1. **dental 확장 양축 KP 실측 비교**: everyday_wellness_noun 12건(Toothbrush/Smile/Floss 등) vs b2c_clinical_search_term 10건(Tartar/Fluoride/Gingivitis 등) — 원칙 13의 B2C 역전 단서 직접 시험. backlog(AI승인·KP미확인)가 실행 시작 시 자동 스윕되므로 별도 조치 불필요.
2. **신규 기능어 후속 실측**: Tutorial/Handbook(첫 실측 즉시 통과)·Timetable/Opinion/Recommendation/Seminar 후속 확인. Gift/Retreat/Tournament는 재검증에서 결합 불성립 다수 기각 — KP 실측 기대치 하향.
3. **판정 라인 유지**: 재검증 109건 기각 라인(Booth/Registry/Journal/Summary/List/Tracker 추상/Tournament/Fee 속성/다의어 계열) 동일 적용 + 속성 결합 복원 경로(시작 조치 (c)) 신규 적용.
4. HANDOFF 등재 과제(계속 유예 중): 저장 시점 중복 경고 코드화 검토.

## 중단 시점 컨텍스트(직전 세션)

- 직전 세션 사용자 지시: "이번 라운드까지만 돌리자" → 라운드 EXIT=0 완료 확인 후 "일단 작업 중단, 진행기록 저장"으로 종료. 이번 세션에서 사용자가 무한 반복 진행을 지시해 재개함.
- 직전 라운드 expand_word_bank: 신규 74건 확장(dental 22 + food_service 22 + travel_tourism 20 + 기능어 10) — config/word_bank_expansions.csv에 기록됨. 라운드 로그·원칙 재검증 결과 요약은 memory/WORD_GENERATION_LEARNINGS.md 말미 참고.
- 재검증 109건 기각 라인(Booth/Registry/Journal/Summary/List/Tracker 추상/Tournament/Fee 속성/다의어 계열)은 다음 라운드 판정 시 동일 기준 유지할 것.
