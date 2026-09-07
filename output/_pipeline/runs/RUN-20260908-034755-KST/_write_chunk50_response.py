import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk50_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk50_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "입소 등록 이용 통계는 실제 보육 운영 지표 - 명확"),
    6: (0.6, "선박 입항 승인은 실제 해운 운영 항목 - 명확"),
}

DUP_REJECT = {}

REJECT_REASON = {
    1: "목공 허브 결합은 Hub 앵커 미확정으로 불성립",
    2: "자산 릴레이 결합은 불성립",
    4: "주문 분해 결합은 Order 앵커 미확정으로 불성립",
    5: "장례 센서 결합은 불명확",
    7: "항공편 행렬 결합은 성립 대상이 불분명",
}

n = len(req["items"])
assert n == 7, n
assert len(APPROVE) == 2
assert len(DUP_REJECT) == 0
assert len(REJECT_REASON) == 5, len(REJECT_REASON)
covered = set(APPROVE) | set(DUP_REJECT) | set(REJECT_REASON)
assert covered == set(range(1, n + 1)), f"coverage mismatch: missing={sorted(set(range(1,n+1))-covered)} extra={sorted(covered-set(range(1,n+1)))}"
overlap = (set(APPROVE) & set(DUP_REJECT)) | (set(APPROVE) & set(REJECT_REASON)) | (set(DUP_REJECT) & set(REJECT_REASON))
assert not overlap, f"overlapping indices: {sorted(overlap)}"

decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in APPROVE:
        conf, reason = APPROVE[i]
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": conf, "reason": reason})
    elif i in DUP_REJECT:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": True, "duplication": False, "trademark": True},
                          "confidence": 0.7, "reason": DUP_REJECT[i]})
    else:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": False, "duplication": True, "trademark": True},
                          "confidence": 0.7, "reason": REJECT_REASON[i]})

assert len(decisions) == n
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
print(f"approve={approved} reject={len(decisions)-approved} (dup={len(DUP_REJECT)})")
