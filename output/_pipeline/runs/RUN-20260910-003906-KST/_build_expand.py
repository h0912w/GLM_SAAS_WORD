import csv
import json
import sys
from pathlib import Path

root = Path(r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD")
run = root / "output/_pipeline/runs/RUN-20260910-003906-KST"

items = json.loads((run / "_items_full.json").read_text(encoding="utf-8"))
global_domain = set()
for it in items:
    if "industry" in it:
        global_domain.update(it["existing_domain_words"])
func_item = next(it for it in items if "existing_function_words" in it)
existing_funcs = set(func_item["existing_function_words"])
retired = {r["word"] for r in csv.DictReader(open(root / "config/retired_function_words.csv", encoding="utf-8"))}

# 원칙 1(2026-09-06 개정) 기본 축: 속성/식별 관용구 + 원칙 7(범용 결합력·구체적
# 식별 대상) + 원칙 14(소비자 실검색 콘텐츠 형식) + 원칙 15(속성 명사) 연장.
# 동의어 상호 배제(원칙 4), 은퇴·사망 태그 회피(원칙 5/8), 전업계 대조(원칙 6).
FUNCTIONS = [
    ("App", "consumer_platform_idiom"),
    ("Tips", "searchable_content_format_noun"),
    ("Advice", "searchable_content_format_noun"),
    ("Workbook", "searchable_content_format_noun"),
    ("Mode", "operating_mode_attribute"),
    ("Spec", "attribute_spec_idiom"),
    ("Quantity", "dimension_measure_noun"),
    ("Login", "client_access_idiom"),
    ("Analysis", "analysis_output_noun"),
    ("Coach", "personal_coach_role"),
    ("Habit", "behavior_pattern_noun"),
]

# 대조 실험: 원칙 13("내부자 전문용어 도메인어는 죽는다")의 B2C 역전 단서
# (2026-09-06 개정) — 소비자가 진단명을 그대로 검색하는 임상 용어는 별개일
# 수 있다는 가설을 healthcare에서 독립 시험.
HEALTHCARE_CLINICAL = [
    "Migraine", "Insomnia", "Acne", "Eczema", "Psoriasis", "Vertigo",
    "Arthritis", "Menopause", "Pregnancy", "Fertility", "Thyroid",
    "Cholesterol", "Hypertension", "Anemia", "Heartburn", "Constipation",
    "Concussion", "Sprain", "Fracture", "Insulin",
]

TRAVEL_ACTIVITIES = [
    "Skydiving", "Snowboarding", "Ziplining", "Sledding", "Diving",
    "Sailing", "Rafting", "Climbing", "Biking", "Golf", "Fishing",
    "Camping", "Glamping", "Stargazing", "Birdwatching",
]

TRAVEL_NATURE = [
    "Canyon", "Geyser", "Fjord", "Savanna", "Tundra", "Prairie", "Marsh",
    "Cove", "Cliff", "Cavern", "Oasis", "Dune", "Whale", "Dolphin",
    "Penguin", "Flamingo", "Turtle", "Moose", "Bison", "Reindeer",
]

LEGAL_EVERYDAY = [
    "Lawyer", "Attorney", "Court", "Judge", "Jury", "Lawsuit", "Divorce",
    "Custody", "Immigration", "Testament", "Notary", "Mediation",
    "Guardianship", "Trademark", "Patent", "Copyright",
]

problems = []
seen = set()
for word, _ in FUNCTIONS:
    for pool, name in ((global_domain, "domain"), (existing_funcs, "function"), (retired, "retired")):
        if word in pool:
            problems.append(f"function {word} 충돌({name})")
    if not (word.isalpha() and word == word.capitalize()):
        problems.append(f"function {word} 형식 불량")
    if word in seen:
        problems.append(f"{word} 중복 제안")
    seen.add(word)
for word_list, industry, tag in (
    (HEALTHCARE_CLINICAL, "healthcare", "b2c_clinical_search_term"),
    (TRAVEL_ACTIVITIES, "travel_tourism", "outdoor_activity_term"),
    (TRAVEL_NATURE, "travel_tourism", "nature_landform_noun"),
    (LEGAL_EVERYDAY, "legal", "everyday_legal_consumer_term"),
):
    for word in word_list:
        for pool, name in ((global_domain, "domain-any"), (existing_funcs, "function"), (retired, "retired")):
            if word in pool:
                problems.append(f"domain {word}({industry}) 충돌({name})")
        if not (word.isalpha() and word == word.capitalize()):
            problems.append(f"domain {word} 형식 불량")
        if word in seen:
            problems.append(f"{word} 중복 제안")
        seen.add(word)

if problems:
    print("PROBLEMS:")
    for p in problems:
        print(" -", p)
    sys.exit(1)

decisions = []
for word, tag in FUNCTIONS:
    decisions.append({"type": "function", "word": word, "pattern_tag": tag})
for word_list, industry, tag in (
    (HEALTHCARE_CLINICAL, "healthcare", "b2c_clinical_search_term"),
    (TRAVEL_ACTIVITIES, "travel_tourism", "outdoor_activity_term"),
    (TRAVEL_NATURE, "travel_tourism", "nature_landform_noun"),
    (LEGAL_EVERYDAY, "legal", "everyday_legal_consumer_term"),
):
    for word in word_list:
        decisions.append({"type": "domain", "word": word, "industry": industry, "pattern_tag": tag})

req = json.loads((run / "judgment/expand_word_bank_round1_request.json").read_text(encoding="utf-8"))
doc = {
    "stage": "expand_word_bank",
    "run_id": req["run_id"],
    "round": 1,
    "request_hash": req["request_hash"],
    "judged_at": "2026-09-10T01:05:00+09:00",
    "judged_by": "main-orchestrator",
    "decisions": decisions,
}
out = run / "judgment/expand_word_bank_round1_response.json"
out.write_text(json.dumps(doc, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")

new_tags = {"consumer_platform_idiom", "operating_mode_attribute", "attribute_spec_idiom",
            "client_access_idiom", "analysis_output_noun", "personal_coach_role",
            "behavior_pattern_noun", "outdoor_activity_term", "nature_landform_noun",
            "everyday_legal_consumer_term"}
n_new = sum(1 for d in decisions if d["pattern_tag"] in new_tags)
print(f"decisions={len(decisions)} functions={len(FUNCTIONS)} domains={len(decisions)-len(FUNCTIONS)} new_tag_ratio={n_new/len(decisions):.1%}")
