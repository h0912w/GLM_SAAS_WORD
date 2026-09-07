import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_recheck_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_recheck_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

FLIP = {
    "Biometric Capacity": "생체 인증은 자격 증명 절차로 Password 준용 탈락 - 생체정보 자체의 정원은 불성립",
    "Biometric Usage": "자격 증명군 정원 반박에 따라 follower 규칙상 이용 통계도 불성립",
    "Cabinetry Account": "가구 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Cabinetry Agreement": "가구 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Carpentry Account": "목공 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Carpentry Agreement": "목공 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Cavity Capacity": "충치는 진단명·증상군이라 Toothache 준용, 정원 불성립",
    "Cavity Usage": "증상군 정원 반박에 따라 이용 통계도 불성립",
    "Column Capacity": "기둥은 구조물로 Stairs 준용, 정원 불성립",
    "Column Usage": "구조물 정원 반박에 따라 이용 통계도 불성립",
    "Consecutive Capacity": "Consecutive는 수식 형용사라 정원 대상 불분명",
    "Consecutive Usage": "수식 형용사 결합이라 이용 통계 대상도 불분명",
    "Countertop Account": "조정대 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Countertop Agreement": "조정대 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Countertop Eligibility": "조정대 시공 자격은 Eligibility 앵커 미확정으로 불성립",
    "Excess Capacity": "Excess는 면책금·개념어라 정원 대상 불분명(Grace 준용)",
    "Excess Usage": "개념어 정원 반박에 따라 이용 통계도 불성립",
    "Gate Usage": "게이트 이용 통계는 성립 대상 불분명 - 이번 라운드 승인된 Gate Capacity 없음(follower 위반)",
    "Gutter Account": "홈통 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Gutter Agreement": "홈통 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Igniter Followup": "Followup 정크 패턴 - 점화장치 후속 결합은 불성립(초기 판정 오류 정정)",
    "Masonry Account": "석공 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Masonry Agreement": "석공 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Masonry Eligibility": "석공 시공 자격은 Eligibility 앵커 미확정으로 불성립",
    "Obituary Capacity": "부고는 산출물(문서)이라 문서 정원 불성립(Declarations 준용)",
    "Oil Usage": "오일은 물질·소모품이라 이용 통계 결합 불성립 - 이번 라운드 승인된 Oil Capacity 없음(follower 위반)",
    "Patio Account": "파티오 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Patio Agreement": "파티오 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Prior Capacity": "Prior는 수식어라 선행 정원은 불성립(Consecutive 준용)",
    "Prior Usage": "수식어 결합이라 이용 통계 대상도 불분명",
    "Public Capacity": "Public는 모호 개념어라 정원 대상 불분명",
    "Public Usage": "모호 개념어 결합이라 이용 통계 대상도 불분명",
    "Quarter Capacity": "분기는 기간 개념이라 Grace 준용, 정원 불성립",
    "Quarter Usage": "기간 개념 정원 반박에 따라 이용 통계도 불성립",
    "Recipe Usage": "레시피 이용 통계는 이번 라운드 승인된 Recipe Capacity 없이 불성립(follower 위반)",
    "Refill Usage": "재충전 이용 통계는 이번 라운드 승인된 Refill Capacity 없이 불성립(follower 위반)",
    "Refrigerant Usage": "냉매는 물질이라 이용 통계 결합 불성립 - 이번 라운드 승인된 Refrigerant Capacity 없음(follower 위반)",
    "Rodent Capacity": "설치류는 해충군으로 Mosquito 준용, 정원 불성립",
    "Rodent Usage": "해충군 정원 반박에 따라 이용 통계도 불성립",
    "Siding Account": "사이딩 시공에 계정 결합은 Account 앵커 미확정(Deck Account 준용)으로 불성립",
    "Siding Agreement": "사이딩 시공 계약은 Agreement 앵커 미확정(Deck Agreement 준용)으로 불성립",
    "Stock Flow": "자금 흐름 결합은 Flow 앵커 미확정(Trading·Wealth Flow 준용)으로 불성립",
    "Syllabus Capacity": "강의계획서는 문서 산출물이라 정원 불성립",
    "Syllabus Usage": "문서 정원 반박에 따라 이용 통계도 불성립",
    "Ticket Usage": "티켓 이용 통계는 Ticket 앵커 반복 탈락(Ticketing 준용)으로 불성립",
}
assert len(FLIP) == 45, len(FLIP)

req_titles = [it["title"] for it in req["items"]]
assert len(req_titles) == 1150, len(req_titles)
assert len(set(req_titles)) == len(req_titles)
missing = [t for t in FLIP if t not in set(req_titles)]
assert not missing, f"flip titles not in request: {missing}"

decisions = []
applied = 0
for it in req["items"]:
    title = it["title"]
    if title in FLIP:
        applied += 1
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": False, "duplication": True, "trademark": True},
                          "confidence": 0.7,
                          "reason": "반박 성립: " + FLIP[title]})
    else:
        base = it.get("original_reason", "")
        reason = "반박 불성립 - 1차 승인 유지" + (f": {base}" if base else "")
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": 0.6, "reason": reason})

assert applied == 45, applied
assert len(decisions) == len(req["items"])
assert {d["title"] for d in decisions} == set(req_titles)
approved = sum(1 for d in decisions if d["approve"])

kst = timezone(timedelta(hours=9))
resp = {
    "decisions": decisions,
    "judged_at": datetime.now(kst).isoformat(),
    "judged_by": "main-orchestrator",
    "request_hash": req["request_hash"],
    "round": req["round"],
    "run_id": req["run_id"],
    "stage": req["stage"],
}
with open(RESP, "w", encoding="utf-8", newline="\n") as f:
    json.dump(resp, f, ensure_ascii=False, indent=2)
print(f"written: {RESP}")
print(f"approve={approved} flipped={applied} total={len(decisions)}")
