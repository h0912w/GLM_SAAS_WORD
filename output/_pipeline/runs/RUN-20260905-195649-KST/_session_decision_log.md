# Session Decision Log — RUN-20260905-195649-KST (사용자 지시: 10k 사이클 자율 운영)

사용자 지시: "실제로 만 개씩 돌리면서 동작 테스트, 문제는 AI가 스스로 판단해 해결,
전체 라운드 끝나면 AI 판단 정리 보고, 1만 개씩 한 사이클."

결정 1~3은 전 run `RUN-20260905-190009-KST/_session_decision_log.md` 참고.
이 로그는 그 번호를 이어받는다(4번부터).

## 결정 기록 (시간순)

4. **expand_word_bank 확장 제안 — 도메인어 20 + 기능어 11 (19:56)**
   - 상황: 190009 라운드가 병합 풀 잔여분 1,022개로 완주하며 조합공간 소진 →
     194309 라운드에서 `expand_word_bank` 판정 개방.
   - 결정: 도메인어 20개는 전부 일상 여행 어휘(everyday_travel_leisure_noun)로
     구성 — 원칙 13(내부자 전문용어 회피)·원칙 2(니치 확장 위험)에 따라
     Itinerary/Boarding Pass류 실무 용어 배제. 기능어 11개는 의도적으로 이질적
     패턴 태그 7종에 분산(Review/Recipe/Video/Diary, Refund/Expense, Newsletter,
     Inventory, Claim, Onboarding, Checkin) — 태그 단위 사후 분해 가능하게.
   - 31개 전부 채택. `config/word_bank_expansions.csv` append는 다음 실행이
     수행(19:58). 코드·설정 무변경(§2 규칙10 준수).

5. **"X Review" 대량 승인 판단 기준 수립** (51청크 판정 중)
   - 판단: "X Review"는 X마다 별개의 실제 검색 쿼리다(Tax Review ≠ Fraud
     Review ≠ Podcast Review — 서로 다른 소비자 의도). 따라서 서로 다른 X의
     Review 제목끼리 의미중복이 아니며, 라운드 전역 동의어 계열 기준과 충돌하지
     않는다.
   - 결과로 정당화됨: 이번 라운드 KP통과 19개 중 16개가 X Review(Dispatch
     Review 9,900/월·경쟁지수 0 등). 이 관측은 핵심 원칙 14(candidate)로 등재.
     반대로 동일 X 안의 유의 기능어(Hub/Center/Portal류)는 종전대로 중복 기각.

6. **라운드 전역 동의어 계열 중복 기준의 기계적 일관 적용** (51청크 판정 중)
   - 결정: 만 건을 51개 청크로 나눠 판정하는 동안 청크마다 기준이 흔들리면
     승인 풀 순도가 무너진다 — 계열 앵커(Hub≈Center≈Portal→Tourist Hub,
     Diary≈Log≈Note≈Journal≈Memo≈Record→Trip Diary, Tracker≈Radar≈Watch≈
     Monitor→Tourist Tracker, Atlas≈Finder≈Locator≈Map→Vacation Atlas,
     Planner≈Scheduler≈Manager≈Helper→Tourist Planner, Alert≈Notification≈
     Reminder, Calculator vs Estimator/Quote, Passport→Tourist 등)를 라운드
     시작 전에 고정하고 전 청크에 동일 적용했다. per-domain 승인 가족(Review
     ~100+ 도메인어, Checkin의 Excursion/Resort/Luggage, Calculator/Estimate/
     Comparison의 per-domain 멤버, 신규 가족 Desk)도 동일 원칙으로 운영.
   - 결과: AI승인율 8.3%를 유지하며 승인 풀 순도가 유지됐고(190009 대비 승인율
     하락은 후보 구성 차이), 승인 풀에서 KP통과 19개가 나왔다. 승인율 확대보다
     승인 순도 유지가 통과율에 유리하다는 방향 재확인(1회 관측, 원칙 미등재).

7. **사망/약세 패턴 사전기각 정책 유지 — 단, 한계를 자진 기록** (51청크 판정 중)
   - 결정: Recipe(0.85), 콘텐츠 열람 명사(Video/Newsletter/Diary 등, 0.75),
     은퇴 확정 태그(Mockup/Flowchart/Simulator, 0.85), 회계 항목 명사(Fee/Tax/
     Invoice류, 0.8), 추상 스키마 접미 명사(Token/Field/Tag류, 0.8)는 종전
     라운드 실측에 따라 일관 기각 — 청크별 예외를 두지 않았다.
   - 자진 기록: 이 정책 때문에 Recipe는 0승인(시장 검증 전 세션 선입견 개입),
     Video/Newsletter는 표본이 오염됐다. WORD_GENERATION_LEARNINGS 195649 항목에
     "Recipe의 0%는 시장 결과가 아니라 판정 사전기각의 결과"로 명시했고, 다음
     확장에서 사전기각 없는 깨끗한 재시험 여지를 남겼다.

8. **51청크 판정 집행 절차** (19:57~22:58)
   - 파이프라인이 청크 단위로 exit 3(AWAITING_JUDGMENT) → 현재 세션이 요청을
     판정해 응답 기록 → `--resume`로 다음 청크. 51회 반복(200×50+7).
   - 집행 품질 절차: 매 청크 실행 전 커버리지 diff(누락 0 확인)를 수행 — 실제로
     c45(5건)·c46(1건)·c49(3건)에서 사전 작성 누락을 발견해 실행 전 수정했다.
     판정 스크립트(_judge_cN.py)는 실행 직후 매번 삭제. 코드·설정 무변경.
   - 골든셋 카나리아 7개는 첫 청크(`review_titles`)에 형식상 구분 없이 섞임 —
     7/7 일치(승인 3·거절 4 전부 정답 일치), 불일치 0.

9. **세션 내부 카운트 불일치 발견 → 실데이터 재집계로 정정** (라운드 완주 직후)
   - 사실: 문맥 압축을 거친 세션의 청크별 승인 러닝 카운트 합계(938)가 ledger
     최종치(828)와 110 어긋났다.
   - 조치: 응답 파일 51개를 디스크에서 직접 재집계 — `review_titles` 74승인
     (이 중 카나리아 승인 3건 제외 시 71) + `chunk1~50` 757승인 = **828**로
     ledger와 정확히 일치. 근본 원인은 세션의 러닝 카운트가 문맥 압축 과정에서
     어긋난 것(추적 오류)이며, 파이프라인·ledger·골든셋 평가는 전 구간 정확했다.
   - 교훈: 문맥 압축을 건넨 러닝 카운트는 신뢰할 수 없다 — 최종 보고는 반드시
     응답 파일/ledger/round_history.csv에서 재집계한다(러닝 카운트는 중간
     진행 표시 용도로만). 이 조치는 사람 개입 없이 세션이 스스로 검증·정정했다.

10. **라운드 완주 결과 확정 + 원칙 갱신** (22:58)
    - 생성 10,000 / AI승인 828(8.3%) / backlog 0 / KP통과 19(0.19%). 정체
      점검 `향상 중`(직전 0.00% → 0.19%). 골든셋 7/7. 승인율 이상탐지 z=-2.84
      정상(레드팀 재검증 미발동).
    - 핵심 원칙 갱신(WORD_GENERATION_LEARNINGS): 신규 원칙 14 `candidate` 등재
      (실제 검색되는 콘텐츠 형식 명사 — Review류 강세, 1회 관측). 원칙 13은
      `candidate` 유지 — 이번 확장이 일상어만으로 구성돼 내부자용어 대조군이
      없어 통제 재현 조건 미충족(방향은 지지). pattern_tag 사후 분해가 교란
      라운드에서도 태그별 결론을 분리함을 첫 실증(Inventory 51승인·0통과 vs
      Review 559승인·16통과).
    - 산출물: 마스터 통과 누적 2,309개(문서③④), 본 라운드 snapshot 4종 저장.
      HANDOFF는 파이프라인이 자동 갱신(수동 편집 없음).
