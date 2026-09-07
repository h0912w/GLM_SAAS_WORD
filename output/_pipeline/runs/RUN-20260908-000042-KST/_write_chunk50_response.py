import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk50_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk50_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    6: (0.65, "하객 명단 정원 관리는 실제 예식 운영 항목 - 명확"),
}

DUP_REJECT = {}

REJECT_REASON = {
    1: "우회 주기는 보안 우회 오독으로 의미 불명",
    2: "촬영 패키지 접수처·리셉션 오독으로 불명확",
    3: "리허설 후속 관리가 무엇을 뜻하는지 불분명",
    4: "풀 청소기 매트릭스는 물건 오독으로 불명확",
    5: "리모델링 뉴스레터는 콘텐츠로 읽혀 제품 불명확",
    7: "사다리 상태는 물건 오독으로 불명확",
}

assert len(APPROVE) == 1
assert len(DUP_REJECT) == 0
assert len(REJECT_REASON) == 6, len(REJECT_REASON)
covered = set(APPROVE) | set(DUP_REJECT) | set(REJECT_REASON)
assert covered == set(range(1, 8)), f"coverage mismatch: missing={sorted(set(range(1,8))-covered)} extra={sorted(covered-set(range(1,8)))}"
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

assert len(decisions) == len(req["items"]) == 7
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
