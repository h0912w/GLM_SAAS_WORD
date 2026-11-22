"""Verify all recheck batch decision files and seal the combined response.

Usage: python -I verify_and_seal_recheck.py [--seal]
Without --seal: only verifies. With --seal: verifies and writes the final
review_titles_recheck round-1 response via judgment.write_response.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
RUN = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from saas_words_two import judgment  # noqa: E402

req_path = RUN / "judgment" / "review_titles_recheck_round1_request.json"
req = json_load = __import__("json").loads(req_path.read_text(encoding="utf-8"))
items = req["items"]
titles = [it["title"] for it in items]

dec_dir = RUN / "tmp" / "decisions"
batch_files = sorted(dec_dir.glob("_recheck_batch*.json"),
                     key=lambda p: int(p.stem.replace("_recheck_batch", "")))
if not batch_files:
    print("NO BATCH FILES FOUND")
    sys.exit(1)

merged = []
seen = set()
order_ok = True
for bf in batch_files:
    decs = __import__("json").loads(bf.read_text(encoding="utf-8"))
    for d in decs:
        t = d["title"]
        if t in seen:
            print(f"DUPLICATE in merged: {t} ({bf.name})")
            order_ok = False
        seen.add(t)
        merged.append(d)

missing = [t for t in titles if t not in seen]
extra = [t for t in seen if t not in set(titles)]
bad = [d["title"] for d in merged
       if not isinstance(d.get("approve"), bool)
       or (not d["approve"] and not str(d.get("reason", "")).strip())]

print(f"batches={len(batch_files)} merged={len(merged)} request_items={len(titles)}")
print(f"missing={len(missing)} extra={len(extra)} malformed={len(bad)}")
if missing:
    print("missing sample:", missing[:5])
if extra:
    print("extra sample:", extra[:5])
if bad:
    print("bad sample:", bad[:5])

if "--seal" in sys.argv:
    if missing or extra or bad:
        print("NOT SEALING - verification failed")
        sys.exit(1)
    # keep request order
    by_title = {d["title"]: d for d in merged}
    ordered = [by_title[t] for t in titles]
    flipped = sum(1 for d in ordered if not d["approve"])
    path = judgment.write_response(
        RUN, "review_titles_recheck", ordered, round_no=1,
        judged_at="2026-11-22T17:30:00+09:00", judged_by="main-session",
    )
    n_approve = len(ordered) - flipped
    print(f"SEALED {path} approve={n_approve} flipped={flipped}")
