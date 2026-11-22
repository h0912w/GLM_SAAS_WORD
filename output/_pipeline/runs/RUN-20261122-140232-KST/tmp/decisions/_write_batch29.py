import json

req = json.load(open(r'output/_pipeline/runs/RUN-20261122-140232-KST/judgment/review_titles_recheck_round1_request.json', encoding='utf-8'))
items = req['items'][5800:6000]

# Per-index explicit decisions made by me after reading each title individually.
# approve=False = refuted (flip); approve=True = sustained on individual inspection.
D = {}

def F(i, conf, reason): D[i] = (False, conf, reason)
def S(i, conf, reason): D[i] = (True, conf, reason)

# --- flips: food anchor + dead/vague fragment families (established flip lines) ---
F(5819, 0.65, "Utilization on a dish anchor is abstract analytics jargon (resource/capacity-utilization reporting), unreadable as a concrete restaurant operation for bruschetta; same corporate-fragment family as flipped Requirement/Reception on food anchors.")
F(5820, 0.7, "Requirement is a dead HR/procurement fragment on a food anchor - reads as software requirements-doc jargon, no dish-operations reading survives; matches batch-22 Requirement fragment flips.")
F(5821, 0.7, "Resignation is an HR-employment fragment on a food anchor; no readable restaurant operation ('tabbouleh resignation' names nothing); matches established Depreciation/Resignation HR-fragment flips.")
F(5826, 0.7, "Mode is an established dead fragment on food anchors (flip family: Mode); 'quinoa mode' names no product or operation.")
F(5827, 0.65, "Spec is software-engineering jargon (spec sheet/spec doc); on a dessert anchor it reads as a dead tech fragment with no food-operations meaning, same family as flipped Widget/Model on food anchors.")
F(5829, 0.75, "Login is an established dead SaaS fragment on food anchors (flip family: Login); 'moussaka login' is pure auth-screen jargon.")
F(5837, 0.7, "Date is an established dead fragment on food anchors (flip family: Date) - calendar-date jargon with no concrete tzatziki operation.")
F(5867, 0.7, "Depreciation is an accounting/HR fragment on a dish anchor (flip family, batches 22/23); even the equipment-costing reading is a stretch for a single dish and round 1 gave no concrete operation.")
F(5870, 0.6, "Opinion on a food anchor is vague - it names no concrete product or restaurant operation (commentary? polls? reviews?); round 1 gave no readable anchor-specific meaning, so it stays a floating abstract noun.")
F(5874, 0.65, "Spec is software-engineering jargon; 'quinoa spec' is a dead tech fragment with no recipe/menu operation, same family as flipped Widget/Model on food anchors.")
F(5878, 0.7, "Habit is an established dead fragment on food anchors (flip family: Habit); 'gumbo habit' names no business operation.")
F(5884, 0.7, "Date is an established dead fragment on food anchors (flip family: Date); 'goulash date' is calendar jargon.")
F(5915, 0.65, "Utilization on a dish anchor is abstract analytics jargon, unreadable as a concrete acai-shop operation; same corporate-fragment family as flipped Requirement/Reception.")
F(5916, 0.7, "Requirement is a dead HR/procurement fragment on a food anchor; no dish-operations reading; matches batch-22 Requirement fragment flips.")
F(5917, 0.7, "Resignation is an HR-employment fragment on a dish anchor; names no restaurant operation; matches established Resignation HR-fragment flips.")
F(5926, 0.7, "Habit is an established dead fragment on food anchors (flip family: Habit); 'borscht habit' names no operation.")
F(5932, 0.7, "Date is an established dead fragment on food anchors (flip family: Date); 'pierogi date' is calendar jargon.")
F(5966, 0.7, "Benefit is a dead benefits/HR fragment on a food anchor (batch-22 flip family); 'acai benefit' is vague marketing filler with no concrete operation.")
F(5967, 0.7, "Depreciation is an accounting/HR fragment on a dish anchor (flip family, batches 22/23); no concrete dish-level operation survives scrutiny.")
F(5970, 0.6, "Opinion on a dish anchor is vague - no concrete product or operation is named (reviews? commentary?); floating abstract noun, same defect as Guacamole Opinion.")
F(5974, 0.65, "Spec is software-engineering jargon; 'gyro spec' is a dead tech fragment, same family as flipped Widget/Model on food anchors.")
F(5977, 0.7, "Habit is an established dead fragment on food anchors (flip family: Habit); 'moussaka habit' names no operation.")
F(5983, 0.7, "Date is an established dead fragment on food anchors (flip family: Date); 'arepa date' is calendar jargon.")

# --- sustained: query-clause family (established approval line) ---
QC = "sustained: query-clause combo ({fn} as search-modifier second word), generic/domain anchor dominates, no famous-mark reading, no near-synonym duplicate"
qcl = [5800,5801,5802,5803,5804,5805,5806,5807,5808,5809,5810,5811,5812,5813,5814,5815,5816,5817,
 5838,5839,5840,5841,5842,5843,5844,5845,5846,5847,5848,5849,5850,5851,5852,5853,5854,5855,5856,5857,
 5858,5859,5860,5861,5862,5863,5864,5865,5886,5887,5888,5889,5891,5892,5893,5894,5895,5896,5897,5898,
 5899,5900,5901,5902,5903,5904,5905,5906,5907,5908,5909,5910,5911,5912,5913,5914,5935,5936,5937,5939,
 5940,5941,5942,5943,5944,5945,5946,5947,5948,5949,5950,5951,5952,5953,5954,5955,5956,5957,5958,5959,
 5960,5961,5962,5964,5965,5987,5988,5989,5990,5991,5992,5993,5994,5995,5996,5997,5999]
fns = {i: items[i-5800]['title'].split()[1] for i in qcl}
for i in qcl:
    S(i, 0.72, QC.format(fn=fns[i]))

# verb/gerund-anchor conjugations sustained
S(5890, 0.75, "sustained: 'change' is a verb anchor - verb conjugation is the natural grammar reading (established verb-usage line: Permit/Briefing/Request/Commute Conjugations sustained)")
S(5938, 0.75, "sustained: 'leave' has a dominant verb reading (to leave) and an HR grammar-exercise reading; matches established verb-anchor Conjugation defenses")
S(5963, 0.6, "sustained: kindergarten sits in the education/grammar-learning domain where conjugation worksheets are grade-keyed ('kindergarten grammar' is a real learner-level category), unlike the flipped non-grammar anchors (Crew/Waitlist/Terminology)")
S(5998, 0.75, "sustained: 'stain' is a verb (to stain) - conjugation practice reading is natural, matching established verb-anchor Conjugation defenses")

# sustained: food anchor + approved business-operations function words
FOOD_OK = {
 5818: "Evaluation", 5822: "Tutorial", 5823: "Gift", 5824: "Tournament", 5825: "App",
 5828: "Quantity", 5830: "Analysis", 5831: "Coach", 5832: "Help", 5833: "Ideas",
 5834: "Basics", 5835: "Names", 5836: "Questions", 5866: "Questionnaire",
 5868: "Hazard", 5869: "Handbook", 5871: "Flyer", 5872: "Tips", 5873: "Workbook",
 5875: "Quantity", 5876: "Analysis", 5877: "Coach", 5879: "Help", 5880: "Ideas",
 5881: "Basics", 5882: "Names", 5883: "Questions", 5885: "Steps",
 5918: "Tutorial", 5919: "Timetable", 5920: "Gift", 5921: "Tournament", 5922: "App",
 5923: "Quantity", 5924: "Analysis", 5925: "Coach", 5927: "Help", 5928: "Ideas",
 5929: "Basics", 5930: "Names", 5931: "Questions", 5933: "Steps",
 5934: "Alternatives", 5968: "Hazard", 5969: "Handbook", 5971: "Flyer",
 5972: "Tips", 5973: "Workbook", 5975: "Analysis", 5976: "Coach",
 5978: "Help", 5979: "Ideas", 5980: "Basics", 5981: "Names", 5982: "Questions",
 5984: "Steps", 5985: "Alternatives", 5986: "Courses",
}
DEF = {
 "Hazard": "HACCP food-safety hazard reading is concrete",
 "Help": "help/guidance content for making the dish is a real content category",
 "Workbook": "practice workbook (cookbook-adjacent learning book) is a concrete object",
 "App": "recipe/menu app is an established real product category for dishes",
 "Names": "variety/naming list for the dish is a readable content category",
 "Questions": "FAQ-style Q&A content about the dish is readable",
 "Gift": "food gift box/basket category is a real retail concept",
 "Tournament": "cook-off/eating tournament is a real event category",
 "Quantity": "portion/order quantity is concrete catering operations",
 "Alternatives": "substitutes/alternatives for the dish is a real query category",
 "Steps": "recipe steps is the concrete cooking reading",
 "Courses": "cooking courses or menu courses both give a concrete reading",
}
for i, fn in FOOD_OK.items():
    extra = DEF.get(fn, "concrete business-operation reading in the approved food-ops line")
    S(i, 0.7, "sustained: food anchor + '%s' reads as restaurant/food-content operations (%s), in the established approved line" % (fn, extra))

assert set(D) == set(range(5800, 6000)), len(D)
dec = [{"title": items[i-5800]['title'], "approve": D[i][0], "confidence": D[i][1], "reason": D[i][2]} for i in range(5800, 6000)]
out = r'output/_pipeline/runs/RUN-20261122-140232-KST/tmp/decisions/_recheck_batch29.json'
with open(out, 'w', encoding='utf-8') as f:
    json.dump(dec, f, ensure_ascii=False, indent=1)
print("written", len(dec), "sustained", sum(1 for d in dec if d['approve']), "flipped", sum(1 for d in dec if not d['approve']))
