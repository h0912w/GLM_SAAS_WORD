import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "expand_word_bank_round1_request.json")
RESP = os.path.join(JDIR, "expand_word_bank_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

DENTAL_EVERYDAY = ["Toothbrush", "Toothpaste", "Mouthwash", "Mouthguard", "Smile", "Breath",
                   "Snoring", "Bite", "Dentist", "Orthodontist", "Hygienist", "Floss"]
DENTAL_CLINICAL = ["Tartar", "Fluoride", "Sealant", "Gingivitis", "Bruxism", "Halitosis",
                   "Periodontitis", "Malocclusion", "Endodontics", "Periodontics"]
FOOD = ["Cafe", "Diner", "Bistro", "Pizzeria", "Deli", "Dessert", "Takeout", "Brunch",
        "Bakery", "Pastry", "Bagel", "Donut", "Espresso", "Latte", "Cocktail", "Barista",
        "Pub", "Steakhouse", "Sushi", "Taco", "Noodle", "Seafood"]
TRAVEL = ["Snorkeling", "Kayaking", "Waterfall", "Sunset", "Waterfront", "Boardwalk",
          "Beachfront", "Skyline", "Backpacker", "Parasailing", "Wildlife", "Lagoon",
          "Glacier", "Volcano", "Daytrip", "Yacht", "Promenade", "Rainforest", "Desert", "Winery"]
FN = [("Tutorial", "searchable_content_format_noun"),
      ("Handbook", "searchable_content_format_noun"),
      ("Timetable", "published_schedule_noun"),
      ("Opinion", "expert_opinion_noun"),
      ("Recommendation", "expert_opinion_noun"),
      ("Seminar", "skill_building_program_noun"),
      ("Gift", "everyday_gifting_noun"),
      ("Retreat", "everyday_travel_leisure_noun"),
      ("Tournament", "everyday_travel_leisure_noun"),
      ("Flyer", "everyday_promo_print_noun")]

decisions = []
for w in DENTAL_EVERYDAY:
    decisions.append({"type": "domain", "word": w, "industry": "dental",
                      "pattern_tag": "everyday_wellness_noun"})
for w in DENTAL_CLINICAL:
    decisions.append({"type": "domain", "word": w, "industry": "dental",
                      "pattern_tag": "b2c_clinical_search_term"})
for w in FOOD:
    decisions.append({"type": "domain", "word": w, "industry": "food_service",
                      "pattern_tag": "everyday_food_dining_noun"})
for w in TRAVEL:
    decisions.append({"type": "domain", "word": w, "industry": "travel_tourism",
                      "pattern_tag": "everyday_travel_leisure_noun"})
for w, tag in FN:
    decisions.append({"type": "function", "word": w, "pattern_tag": tag})

alldom = {}
for it in req["items"]:
    if "industry" in it:
        for w in it["existing_domain_words"]:
            alldom.setdefault(w.lower(), []).append(it["industry"])
allfn = set()
for it in req["items"]:
    if "existing_function_words" in it:
        allfn = {w.lower() for w in it["existing_function_words"]}
seen = set()
for d in decisions:
    lw = d["word"].lower()
    assert lw not in alldom, f"{d['word']} collides with domain in {alldom[lw]}"
    assert lw not in allfn, f"{d['word']} collides with existing function words"
    assert lw not in seen, f"batch-internal duplicate: {d['word']}"
    seen.add(lw)

existing_tags = set()
for it in req["items"]:
    if "pattern_tag_performance" in it:
        existing_tags = set(it["pattern_tag_performance"].keys())
new_tag_words = sum(1 for d in decisions if d["pattern_tag"] not in existing_tags)
quota = 30.0
for it in req["items"]:
    if "exploration_quota_pct" in it:
        quota = it["exploration_quota_pct"]
ratio = 100.0 * new_tag_words / len(decisions)
assert ratio >= quota, f"exploration quota {quota}% not met: {ratio:.1f}%"
retired = set()
for it in req["items"]:
    if "function_word_performance" in it:
        retired = set(it["function_word_performance"].get("retired_function_words", []))
assert not (seen & {w.lower() for w in retired}), f"retired word proposed: {seen & {w.lower() for w in retired}}"

dom_count = sum(1 for d in decisions if d["type"] == "domain")
fn_count = sum(1 for d in decisions if d["type"] == "function")
assert dom_count >= 20 and fn_count >= 10, (dom_count, fn_count)

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
print(f"domain={dom_count} function={fn_count} total={len(decisions)} new_tag_ratio={ratio:.1f}% (quota {quota}%)")
