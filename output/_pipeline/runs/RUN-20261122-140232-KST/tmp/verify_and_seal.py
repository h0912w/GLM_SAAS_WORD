import json, sys
from pathlib import Path
ROOT = Path(r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD")
sys.path.insert(0, str(ROOT / "src"))
from saas_words_two import judgment, word_pipeline  # noqa: E402

run_dir = ROOT / "output/_pipeline/runs/RUN-20261122-140232-KST"
chunks = [int(a) for a in sys.argv[1:]]
for n in chunks:
    stage = "review_titles" if n == 0 else f"review_titles_chunk{n}"
    req = json.loads(judgment.request_path(run_dir, stage, 1).read_text(encoding="utf-8"))
    items = req["items"]
    dec_path = run_dir / "tmp" / "decisions" / f"_chunk{n}_decisions.json"
    if not dec_path.exists():
        print(f"chunk{n}: DECISIONS MISSING"); continue
    decisions = json.loads(dec_path.read_text(encoding="utf-8"))
    # 1:1 title-set check
    req_titles = [it["title"] for it in items]
    dec_titles = [d.get("title") for d in decisions]
    exact_order = dec_titles == req_titles
    set_match = sorted(map(str, dec_titles)) == sorted(req_titles)
    # schema validation (same code path as pipeline)
    accepted, malformed = word_pipeline._validate_review_decisions(items, decisions)
    invalid_ratio = len(malformed) / len(items)
    n_ap = sum(1 for d in decisions if d.get("approve") is True)
    low_conf = sum(1 for d in decisions if d.get("approve") is True and isinstance(d.get("confidence"), (int, float)) and d["confidence"] < 0.6)
    print(f"chunk{n}: n={len(decisions)} order_ok={exact_order} set_ok={set_match} malformed={len(malformed)} ratio={invalid_ratio:.3f} approve={n_ap} reject={len(decisions)-n_ap} low_conf_appr={low_conf}")
    if malformed:
        for t, r in malformed[:5]:
            print(f"   e.g. {t}: {r}")
    if set_match and len(malformed) == 0:
        judgment.write_response(run_dir, stage, decisions, round_no=1, judged_at="2026-11-22T14:30:00+09:00", judged_by="main-session")
        print(f"chunk{n}: response SEALED")
