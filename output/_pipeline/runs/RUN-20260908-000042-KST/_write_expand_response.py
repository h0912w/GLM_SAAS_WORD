import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "expand_word_bank_round1_request.json")
RESP = os.path.join(JDIR, "expand_word_bank_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

# 제안 설계 근거:
# - 기능어 12개는 각기 다른 기능(수용량/사용량/상태/습도/회차/주기/내역/감지/접수/후속연락/승인/매트릭스)을 대표 - 동의어 클러스터 없음.
# - Capacity: 원칙 15(속성 명사) 승격 조건의 미시도 항목(Count/Level/Depth 다음).
# - Matrix: 원칙 7(구체 식별 > 추상 스키마)에 대한 의도적 대조 실험 - validated
#   원칙이 여전히 성립하는지 이번 라운드 실측으로 확인.
# - 도메인어는 finance(기존 15개, 소비자 뱅킹 일상어)와 construction(기존 14개,
#   주거 개보수 일상어)에 각 22개 - 원칙 13(일상 어휘 우선) 준수, 기존 단어와 0 중복.
# - dead_pattern_tags(visual_structure_document) 미사용, 은퇴 기능어 재제안 없음.
FUNCTIONS = [
    ("Capacity", "dimension_measure_noun"),
    ("Usage", "performance_measure_noun"),
    ("Condition", "type_category_noun"),
    ("Humidity", "dimension_measure_noun"),
    ("Episode", "searchable_content_format_noun"),
    ("Cycle", "time_reference_noun"),
    ("Breakdown", "detail_breakdown_noun"),
    ("Sensor", "physical_measuring_device_noun"),
    ("Reception", "concrete_place_noun"),
    ("Followup", "outbound_communication_noun"),
    ("Approval", "workflow_approval_noun"),
    ("Matrix", "abstract_schema_term"),
]

FINANCE = [
    "Credit", "Debit", "Savings", "Withdrawal", "Remittance", "Wire",
    "Trading", "Stock", "Portfolio", "Bond", "Insurance", "Mortgage",
    "Installment", "Foreclosure", "Bankruptcy", "Inheritance", "Creditor",
    "Debtor", "Payee", "Insolvency", "Trust", "Wealth",
]

CONSTRUCTION = [
    "Remodel", "Electrical", "Plumbing", "Roofing", "Flooring", "Painting",
    "Siding", "Gutter", "Foundation", "Framing", "Concrete", "Demolition",
    "Excavation", "Paving", "Insulation", "Waterproofing", "Deck", "Patio",
    "Cabinetry", "Countertop", "Masonry", "Carpentry",
]

assert len(FUNCTIONS) == 12
assert len(FINANCE) == 22 and len(set(FINANCE)) == 22
assert len(CONSTRUCTION) == 22 and len(set(CONSTRUCTION)) == 22

req_inds = {}
for it in req["items"]:
    if it.get("industry"):
        req_inds[it["industry"]] = set(it.get("existing_domain_words", []))
fn_item = next(it for it in req["items"] if "existing_function_words" in it)
existing_fn = set(fn_item["existing_function_words"])
retired_item = next(
    it for it in req["items"] if "function_word_performance" in it
)
retired_fn = set(retired_item["function_word_performance"].get("retired_function_words", []))

for word, _ in FUNCTIONS:
    assert word not in existing_fn, f"function dup: {word}"
    assert word not in retired_fn, f"retired reuse: {word}"
    assert word.isalpha() and word == word.capitalize(), f"format: {word}"
for ind, words in (("finance", FINANCE), ("construction", CONSTRUCTION)):
    for w in words:
        assert w not in req_inds[ind], f"domain dup in {ind}: {w}"
        assert w.isalpha() and w == w.capitalize(), f"format: {w}"

EXISTING_TAGS = set(req_inds.get("__none__", set()))
tag_item = next(it for it in req["items"] if "pattern_tag_performance" in it)
EXISTING_TAGS = set(tag_item["pattern_tag_performance"].keys())
DEAD_TAGS = set(next(it for it in req["items"] if "dead_pattern_tags" in it)["dead_pattern_tags"])

decisions = []
for word, tag in FUNCTIONS:
    assert tag not in DEAD_TAGS, f"dead tag reuse: {tag}"
    decisions.append({
        "type": "function", "word": word, "industry": "", "pattern_tag": tag,
    })
for word in FINANCE:
    decisions.append({
        "type": "domain", "word": word, "industry": "finance",
        "pattern_tag": "consumer_banking_noun",
    })
for word in CONSTRUCTION:
    decisions.append({
        "type": "domain", "word": word, "industry": "construction",
        "pattern_tag": "home_improvement_trade_noun",
    })

tagged = [d for d in decisions if d["pattern_tag"]]
new_tag_ratio = sum(1 for d in tagged if d["pattern_tag"] not in EXISTING_TAGS) / len(tagged)
assert new_tag_ratio >= 0.30, f"exploration quota fail: {new_tag_ratio}"

assert len(decisions) == 56
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
print(f"decisions={len(decisions)} (function=12 domain=44) new_tag_ratio={new_tag_ratio:.2%}")
