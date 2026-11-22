import json, sys
from pathlib import Path
ROOT = Path(r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD")
sys.path.insert(0, str(ROOT / "src"))
from saas_words_two import judgment, word_pipeline  # noqa: E402

run_dir = ROOT / "output/_pipeline/runs/RUN-20261122-140232-KST"
run_id = "RUN-20261122-140232-KST"
state_doc = json.loads((run_dir / "run_state.json").read_text(encoding="utf-8"))
all_items = state_doc["context"]["review_all_items"]
chunk_size = 200
chunks = [all_items[i:i + chunk_size] for i in range(0, len(all_items), chunk_size)]
instructions = word_pipeline._review_titles_instructions(ROOT)
made = []
for i, items in enumerate(chunks):
    stage = "review_titles" if i == 0 else f"review_titles_chunk{i}"
    p = judgment.request_path(run_dir, stage, 1)
    if not p.exists():
        judgment.write_request(run_dir, stage, run_id, instructions, items, round_no=1, generated_at="2026-11-22T14:02:44.269538+09:00")
        made.append(stage)
print("chunks:", len(chunks), "pre-generated:", len(made))
# dump chunk0 titles for direct judgment
titles0 = [it["title"] for it in chunks[0]]
(Run_dir0 := run_dir / "tmp" / "chunk0_titles.txt").write_text("\n".join(titles0), encoding="utf-8")
print("chunk0 dumped:", len(titles0))
