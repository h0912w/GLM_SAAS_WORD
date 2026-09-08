import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_recheck_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_recheck_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

# 반박 수용(승인 뒤집기): index -> (title, reason, failed_check)
FLIPS = {
    103: ("Camp Registry", "반박 수용: register와 registry는 동일한 등록 대장을 가리키는 동의어 - Camp Register와 의미 중복(1차 산출물 설명도 동일한 '등록 명부'로 기재)", "duplication"),
    146: ("Choir Registry", "반박 수용: register와 registry는 동일한 등록 대장 의미 - Choir Register와 의미 중복", "duplication"),
    330: ("Harmonica Registry", "반박 수용: register와 registry는 동일한 등록 대장 의미 - Harmonica Register와 의미 중복", "duplication"),
    493: ("Orchestra Registry", "반박 수용: register와 registry는 동일한 등록 대장 의미 - Orchestra Register와 의미 중복", "duplication"),
    641: ("Retirement Registry", "반박 수용: register와 registry는 동일한 등록 대장 의미 - Retirement Register와 의미 중복", "duplication"),
    533: ("Piano Register", "반박 수용: 음역(register)을 '관리'하는 운영 항목은 불성립하고 register는 등록으로도 읽히는 다의어 - 명확성 결함", "clarity"),
    407: ("Lesson Memo", "반박 수용: 강사 메모와 수업 기록은 동일 산출물 - Lesson Note와 의미 중복", "duplication"),
    458: ("Nap Evaluation", "반박 수용: nap과 naptime은 같은 낮잠 관리 도구를 가리킴 - Naptime Evaluation과 의미 중복", "duplication"),
    771: ("Traveler Evaluation", "반박 수용: traveler와 tourist는 동일 대상 - Tourist Evaluation과 의미 중복", "duplication"),
    841: ("Waiter Evaluation", "반박 수용: waiter와 server는 동일 직무 - Server Evaluation과 의미 중복", "duplication"),
}

n = len(req["items"])
assert n == 869, n
assert len(FLIPS) == 10, len(FLIPS)
for idx, (title, _reason, _check) in FLIPS.items():
    actual = req["items"][idx - 1]["title"]
    assert actual == title, f"index {idx}: expected {title}, got {actual}"

decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in FLIPS:
        _title, reason, failed = FLIPS[i]
        checks = {"clarity": True, "duplication": True, "trademark": True}
        checks[failed] = False
        decisions.append({"title": title, "approve": False, "checks": checks,
                          "confidence": 0.7, "reason": reason})
    else:
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": 0.8,
                          "reason": "재검증 확인: 반박 근거 없음 - 1차 라인 근거 유지"})

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
print(f"approve={approved} refuted={n-approved}")
