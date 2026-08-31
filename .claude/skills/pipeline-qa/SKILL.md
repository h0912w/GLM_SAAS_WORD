---
name: pipeline-qa
description: 동일 파이프라인 QA
---

# pipeline-qa

## 실행 순서
1. run.py 사용(round-size만 소규모로, 그 외 production과 동일 경로)
2. DONE/CAPABILITY_STAGNATION/RETRYING 중 하나로 정직하게 끝나는지 확인(목표 개수 없음)
3. 4개 문서(ledger/캐시/통과표/단어리스트)가 스키마대로 갱신되는지 확인
4. 골든셋 카나리아·승인율 이상탐지 안전망이 필요시 `review_titles_recheck`를
   실제로 트리거하고 그 결과가 ledger에 반영되는지 확인(2026-08-31)
5. 응답 구조 결함 시 재요청→안전 기본값 확정, 청크 분할, expand_word_bank
   유효율/탐색쿼터 게이트, `principle_reverification` 주기 트리거 확인(2026-09-01)
6. 필수 회귀 판정(`qa/regression/REQUIRED_CASES.md`)

## 완료 조건
- 결과가 파일/로그/체크섬으로 재현 가능함
- 관련 QA가 PASS함
- 실패를 성공으로 숨기지 않음

## 참조
- `/CLAUDE.md`
- 관련 `docs/` 정책 문서
