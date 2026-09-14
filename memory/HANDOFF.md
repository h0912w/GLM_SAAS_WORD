# HANDOFF

- 상태: `PAUSED` (사용자 지시로 세션 중단 — 다음 세션에서 이어서)
- 현재 단계: generate_and_review_titles — recheck 완료·ledger 반영 완료, **Keyword Planner 게이트 직전에서 OAuth 토큰 만료로 중단**
- 마지막 실행: run RUN-20260910-153852-KST (mode=production, 2026-09-10 생성 → 2026-09-15 재개 시도)

## 완료된 것 (이 run 기준)
- review_titles 10,007건(카나리아 7 포함, 51청크) 판정 완료 → 골든셋/신뢰도/승인율 이상탐지 중 트리거로 recheck 진입
- recheck 751건 판정 완료: **승인 741 / 반박 뒤집기 10** — Realtor App·Realtor Tips·Classroom App(상표), Conditioner App·Coping App(명확성), Divorce Alert·Immigration Message·Lawsuit Reminder·Vertigo Record·Testament Manual(의미중복; Testament Manual은 세션 직접 판정)
- 10개 청크 판정은 병렬 서브에이전트(76건×9+67)로 수행, 사후 검증 3종(형식·거절사유 반복도·사유-제목 대응) 전부 통과 — AI-JUDGMENT-001 예방책 3종 실측 적용 성공
- recheck 최종 판정 ledger 반영 완료: `generated_candidates.csv` 458,820행(뒤집기 10건 `redteam_recheck_rejected`, 생존 741건 `approved=True`, backlog 0)
- recheck 응답: `output/_pipeline/runs/RUN-20260910-153852-KST/judgment/review_titles_recheck_round1_response.json`

## 막힌 지점 (확정)
`.env.local`의 GOOGLE_ADS_REFRESH_TOKEN이 `invalid_grant`(Token has been expired or revoked). 원인 두 가능성:
1. **7일 Testing 만료(가장 유력)**: 09-05 18:06 재발급분 → 예상 만료 ~09-12 → 현재 사망과 정확히 일치. 7일 만료는 두 번 실측됨(08-26 기록, 09-05 재발급분).
2. **계정 잠금(08-27 전례)**: 08-27엔 invalid_grant가 잠금 때문이었고 재발급 없이 몇 시간 뒤 자가 해소됐다(0569cc7 커밋 기록). 이 경우 기다리면 같은 토큰이 살아난다.

## 다음 세션 할 일 (순서대로)
1. **토큰 상태 확인**: `.venv/Scripts/python.exe -X utf8 tools/get_refresh_token.py --verify` — 성공이면 즉시 4번으로.
2. **(여전히 죽어 있으면) 부활 감시 재시작**: 계정 잠금 자가 해소 가능성 대비. `output/_pipeline/runs/RUN-20260910-153852-KST/_check_token.py`를 30분 간격으로 도는 Monitor 루프(이전 세션 실측 스크립트) 재가동 → 성공 시 자동 재개.
3. **사용자 결정 대기(이미 조사 완료, HANDOFF 이전 세션 노트/문서 참고)**:
   - 권장: Cloud Console → Google Auth Platform → Audience → "Publish App"(심사 없는 즉시 토글) → 7일 만료 영구 해소. 검증 기각돼도 unverified-프로덕션 토큰 무기한 유효(공식 문서 확인). 폰 브라우저로 가능.
   - 대안: 테스트 상태 유지 + 7일마다 폰 재발급.
   - 장기 옵션: 서비스 계정(SA) 전환 — 만료 원천 제거, JWT 서명 의존성 추가+클라이언트 수정+QA 필요(미구현).
4. **폰(Termius) 재발급 절차**(tools/get_refresh_token.py 2026-09-15 확장·실측 완료):
   `--print-url` → 폰 브라우저 승인 → "연결할 수 없음" 화면 주소창의 code 복사(10분 유효) → `--code "4/0A..."` → `--verify`. 상세는 `docs/operations/15-google-ads-credential-setup.md` "휴대폰(Termius)만으로 재발급하기" 절.
5. **라운드 완결**: 재발급 확인 후 `.venv/Scripts/python.exe -X utf8 run.py --mode production --resume --run-id RUN-20260910-153852-KST` → KP 게이트 741건 → 문서②③④ 갱신 → 체크포인트(HANDOFF 자동 갱신·커밋) → push.
6. **무한 루프 재개**: 이어서 새 production 라운드(사용자 지시: 10,000개씩, 중단 지시까지 무한 반복).
7. **미수 QA**: tools/get_refresh_token.py(--print-url/--code/--verify 추가)·doc 15 갱신은 파이프라인 외부 변경이라 자격증명 복구 전 QA 불가 — 5번 완결 후 final-qa-runner로 소화할 것.

## 재개 안전성 (검증됨)
resume은 stage 'generate_and_review_titles'부터 재시작: 청크 루프 51/51 no-op, recheck 응답 재적용 멱등, ledger 업서트 방식이라 중복 없음 — word_pipeline.py 1028~1249행 실측 확인.

## 진행 통계 참고
- 최근 라운드(RUN-20260910-003906-KST)까지 누적: ledger 448,821행 → 현재 458,820행(이번 run 10,000건 판정 반영), KP 통과 누적 2,483
- 이번 run 승인 741/10,000(7.4%) — 1차 판정 753 중 recheck로 10건 뒤집힘(1.3%)
