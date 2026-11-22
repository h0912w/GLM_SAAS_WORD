# HANDOFF

- 상태: `PAUSED` (사용자 지시 "이번 라운드까지만 진행하고 멈춤" — 라운드 완료 후 세션 중단)
- 현재 단계: update_memory_and_git_checkpoint (word_pipeline) — 라운드 완료·커밋까지 끝냄
- 마지막 실행: run RUN-20261122-140232-KST (mode=production, round-size 10000)
- 이번 라운드: 신규생성 10000개, 1차 AI승인 7108개(71.0%) → recheck 트리거(저신뢰 0.55 승인 45건) → 전수 반박 7105건 유지 6487/반전 618(8.7%) → Keyword Planner통과 505개(5.05%)
- [학습 정체 점검] 향상 중: 최근 1라운드(생성 10000개) 통과율 5.05% vs 이전 2라운드(생성 7224개) 3.04% (상대변화 +65.8%, 임계값 ±10%) — 직전 declining 신호는 반등으로 해소. 해석: 이번 라운드 통과 주력은 쿼리절(Synonyms/Antonyms)×범용 앵커 + 음악 맥락 유지(Vocal Chords 110,000/월)로, 이전 라운드의 Pronunciation/Memes/Definitions 첫계측 이상치 영향이 벗어나 정상 궤도 복귀.
- [골든셋 카나리아] 7/7 일치 (100.0%)
- [승인율 이상탐지] 정상: 이번 라운드 71.0% vs 기준선 평균 56.6%(표준편차 33.8, z=0.43, 임계 ±3.0)
- [recheck 실측] 반전 618건의 집중 패턴: 죽은 패턴 조각(Date/Sensor/Guarantor/Names/Checkin 등 음식 앵커)·근동의쌍(Advice↔Tips, Help↔Tips/Coach, Opinion↔Review, Clock↔Time, Load/Utilization↔Usage, Correction↔Revision)·상표(Keynote×Apple 5건+, Kayak 여행 맥락)·비음악 Chords/Lyrics·명사우세 Conjugations(Crew/Waitlist/Fixture류)·무철자분쟁 Orthography. 저신뢰 45건 중 상당수 반전 — 2026-08-31 저신뢰 게이트 첫 대규모 실효 확인.
- [2026-11-22 배치 요약] RUN-20261117 지침("food×Kit 제외 전부 거절")과 1차 판정 청크 1~17 다수 실측(음식×업무운영어 승인)이 충돌 → 다수 라인 채택 후 recheck가 검증(업무운영 유지군이 KP통과 주력). 지침 텍스트와 다수 판정의 불일치는 memory/WORD_GENERATION_LEARNINGS.md 라운드 로그에 기록 — 다음 라운드에서 같은 방향 재관측 시 validated 승격 검토. recheck 36배치 병렬 위임(동시성 6) 429 0건·malformed 0. 미러 동기화 첫 정상 라운드 UPDATED 확인(5,122단어 마스터+스냅샷 푸시, github-dudreat SSH 별명).
- 다음 원자 작업: 새 세션에서 새 run 실행(목표 수량 개념 없음). expand_word_bank는 조합공간 소진 시 자동 트리거 — 그때 Spelling/Pronunciation류 인접 쿼리절 우선 제안(원칙 20 승격 시험 계속).
