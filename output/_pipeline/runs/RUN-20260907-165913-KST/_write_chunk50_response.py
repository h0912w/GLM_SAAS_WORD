import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk50_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk50_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "직원 교육 처리 물량 관리는 실제 인사 운영 지표 - 명확"),
}

REJECT_REASON = {
    1: "리노베이션 공사 온도는 시공 사양으로 읽혀 SaaS 불일치",
    2: "정산 압박은 의미 불명",
    4: "기능 밝기는 의미 불명",
    5: "적성 발생 빈도는 의미 불명",
    6: "생산 높이는 의미 불명",
    7: "수확 폭은 의미 불명",
}

assert len(REJECT_REASON) == 6
assert not (set(REJECT_REASON) & set(APPROVE))
decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in APPROVE:
        conf, reason = APPROVE[i]
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": conf, "reason": reason})
    else:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": False, "duplication": True, "trademark": True},
                          "confidence": 0.7,
                          "reason": REJECT_REASON.get(i, "clarity 탈락 - 의미 불명")})

assert len(decisions) == len(req["items"])
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
print(f"approve={approved} reject={len(decisions)-approved}")
