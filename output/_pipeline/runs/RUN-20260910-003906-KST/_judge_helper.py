import json, sys
from pathlib import Path

base = Path(__file__).parent
rd = base / "judgment"
req_name, res_name, dec_file = sys.argv[1], sys.argv[2], sys.argv[3]
req = json.loads((rd / req_name).read_text(encoding="utf-8"))
decs = {}
for line in (base / dec_file).read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    title, approve, c, d, t, conf, reason = line.split("\t")
    decs[title] = {
        "title": title,
        "approve": approve == "A",
        "checks": {"clarity": c == "T", "duplication": d == "T", "trademark": t == "T"},
        "confidence": float(conf),
        "reason": reason,
    }
items = req["items"]
titles = [it["title"] for it in items]
missing = [x for x in titles if x not in decs]
extra = [x for x in decs if x not in set(titles)]
if missing or extra:
    print("MISSING:", missing)
    print("EXTRA:", extra)
    sys.exit(1)
out = {
    "request_hash": req["request_hash"],
    "decisions": [decs[x] for x in titles],
}
(rd / res_name).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("written", len(items), "decisions; approve =", sum(1 for d in out["decisions"] if d["approve"]))
