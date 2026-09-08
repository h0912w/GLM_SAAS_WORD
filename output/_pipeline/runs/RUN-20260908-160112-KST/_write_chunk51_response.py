import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk50_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk50_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "근태 사직 결합은 Resignation 결합 불성립",
    2: "도면 위험 결합은 Hazard 결합 불성립",
    3: "상품옵션 보증인 결합은 Guarantor 결합 불성립",
    4: "투숙객 조율기 결합은 Tuner 결합 불성립",
    5: "기타 넥서스 결합은 Nexus 불성립과 악기 자체 대상 불성립",
    6: "바이올린 초안 결합은 Draft 문서와 악기 자체 대상 불성립",
    7: "드럼 번호 결합은 Number 속성과 악기 자체 대상 불성립",
}

n = len(req["items"])
assert n == 7, n
assert len(APPROVE) == 0, len(APPROVE)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 7, len(REJECT_REASON)
covered = set(APPROVE) | set(DUP_REJECT) | set(REJECT_REASON)
missing = sorted(set(range(1, n + 1)) - covered)
extra = sorted(covered - set(range(1, n + 1)))
assert covered == set(range(1, n + 1)), f"missing={missing} extra={extra}"
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
