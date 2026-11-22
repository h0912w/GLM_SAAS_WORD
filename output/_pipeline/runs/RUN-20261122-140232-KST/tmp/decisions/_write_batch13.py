import json, io

base = r'C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST'
items = json.load(open(base + r'\tmp\decisions\_slice13_raw.json', encoding='utf-8'))
assert len(items) == 200

low = set()
for line in open(base + r'\tmp\recheck_low_conf.txt', encoding='utf-8'):
    p = line.rstrip('\n').split('\t')
    if len(p) == 2:
        low.add(p[0])
print('low-conf in slice:', [(i, it['title']) for i, it in enumerate(items) if it['title'] in low])

# Authored decisions (individual judgment by the reviewing agent)
flips = {
    'Edamame Validation': (0.75, 'flipped: dead-pattern fragment - Validation is abstract tech jargon with no readable food-business capability for a dish anchor; vague metric/product fragment family (Validation/Eligibility/Detector), not concrete restaurant operations'),
    'Naan Predictor': (0.7, 'flipped: clarity - Predictor is predictive-analytics jargon producing an absurd product fragment for a bread anchor (same dead family as Detector/Forecast/Model); no concrete naan-related operation is communicated'),
    'Guacamole Eligibility': (0.75, 'flipped: dead-pattern fragment - Eligibility reads as a vague criteria metric with no readable product for a dish anchor; abstract jargon fragment family, unclear what the product does'),
    'Moussaka Revision': (0.7, 'flipped: semantic duplication - Moussaka Revision duplicates Moussaka Correction on the same anchor (Correction/Revision near-synonym pair), same product intent'),
    'Tzatziki Diary': (0.65, 'flipped: clarity - Diary on a dish anchor reads as a personal food-journal fragment with no business capability; unclear what a tzatziki diary SaaS would be'),
    'Satay Revision': (0.7, 'flipped: semantic duplication - Satay Revision duplicates Satay Correction on the same anchor (Correction/Revision near-synonym pair), same product intent'),
    'Pierogi Diary': (0.65, 'flipped: clarity - Diary on a dish anchor reads as a personal food-journal fragment with no business capability; unclear product fragment'),
    'Goulash Diary': (0.65, 'flipped: clarity - Diary on a dish anchor reads as a personal food-journal fragment with no business capability; unclear product fragment'),
    'Ceviche Eligibility': (0.75, 'flipped: dead-pattern fragment - Eligibility is a vague abstract metric fragment with no readable food-business capability for a dish anchor'),
    'Mochi Revision': (0.7, 'flipped: semantic duplication - Mochi Revision duplicates Mochi Correction on the same anchor (Correction/Revision near-synonym pair), same product intent'),
}

query_clause = [0,1,101,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199]
food_ops = [2,3,4,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,53,54,55,56,58,59,60,61,62,64,65,66,67,68,69,102,103,104,105,106,107,108,110,111,112,113,114,115,117,149,150,151,153,154,155,156,157,159,160,161,162,163,164,166,167]

special = {
    'Tabbouleh Lookup': (0.5, 'sustained (low-conf): Lookup is a concrete search/retrieval operation in the sustained food-ops family (ingredient/allergen/menu lookup is a real restaurant tool function), not a dead jargon fragment'),
    'Pickup Chords': (0.55, 'sustained: music-context defense - pickup ensembles (pickup band/jam session) and guitar pickups are real music terms, so the Chords pairing is not a non-music anchor defect'),
    'Tortoise Lyrics': (0.6, 'sustained: Tortoise is a known band name and a generic animal word; lyrics search context is defensible, no trademark-conflict defect'),
    'Tortoise Orthography': (0.6, 'sustained: spelling-of-word query-clause, generic anchor, no defect'),
    'Gingivitis Orthography': (0.6, 'sustained: how-do-you-spell queries for medical terms are real; query-clause pairing intact'),
    'Recurring Orthography': (0.7, 'sustained: famously misspelled word, spelling query-clause is genuinely strong'),
    'Vitals Orthography': (0.55, 'sustained: vitals is a generic healthcare word (vital signs), generic-word dominance; spelling query-clause intact'),
    'Roots Syllables': (0.55, 'sustained: roots is maximally generic (genealogy), generic-word dominance over the TV-series mark; query-clause intact'),
    'Roots Rhymes': (0.55, 'sustained: maximally generic word, query-clause intact'),
    'Verification Syllables': (0.6, 'sustained: syllable-count query-clause works on any word; anchor generic'),
    'Arepa Seal': (0.45, 'sustained: Seal reads as certification/tamper-seal management for packaged food producers, a concrete food-industry concept; borderline but no grounded trademark or duplication defect'),
    'Naan Seal': (0.45, 'sustained: Seal reads as certification/tamper-seal management for packaged food producers, a concrete food-industry concept; borderline but no grounded trademark or duplication defect'),
    'Shawarma Seal': (0.45, 'sustained: Seal reads as certification/tamper-seal management for packaged food producers, a concrete food-industry concept; borderline but no grounded trademark or duplication defect'),
    'Jambalaya Seal': (0.45, 'sustained: Seal reads as certification/tamper-seal management for packaged food producers, a concrete food-industry concept; borderline but no grounded trademark or duplication defect'),
    'Prosciutto Account': (0.5, 'sustained: wholesale/loyalty customer-account management is a real food-business reading of Account; weak but no grounded defect'),
    'Bruschetta Account': (0.5, 'sustained: wholesale/loyalty customer-account management is a real food-business reading of Account; weak but no grounded defect'),
    'Jambalaya Verification': (0.55, 'sustained: order/quality verification is concrete food-business operations; no same-anchor synonym collision in this slice'),
    'Gumbo Verification': (0.55, 'sustained: order/quality verification is concrete food-business operations; no same-anchor synonym collision in this slice'),
    'Borscht Verification': (0.55, 'sustained: order/quality verification is concrete food-business operations; no same-anchor synonym collision in this slice'),
    'Moussaka Verification': (0.55, 'sustained: order/quality verification is concrete food-business operations; no same-anchor synonym collision in this slice'),
}

qc_reason = 'sustained: standard query-clause pairing (spelling/synonym/rhyme/sentence searches), generic anchor, no trademark or anchor-pairing defect found'
fo_reason = 'sustained: concrete restaurant/food-business operations reading, consistent with sustained function-word family; no trademark or duplication defect'

decisions = []
for i, it in enumerate(items):
    t = it['title']
    if t in flips:
        c, r = flips[t]
        decisions.append({'title': t, 'approve': False, 'confidence': c, 'reason': r})
    elif t in special:
        c, r = special[t]
        decisions.append({'title': t, 'approve': True, 'confidence': c, 'reason': r})
    elif i in query_clause:
        decisions.append({'title': t, 'approve': True, 'confidence': 0.6, 'reason': qc_reason})
    elif i in food_ops:
        decisions.append({'title': t, 'approve': True, 'confidence': 0.6, 'reason': fo_reason})
    else:
        raise SystemExit('unjudged index %d: %s' % (i, t))

assert len(decisions) == 200
assert all(d['title'] == it['title'] for d, it in zip(decisions, items))
assert all(d['reason'] for d in decisions)
assert all(0.0 <= d['confidence'] <= 1.0 for d in decisions)
flipped = sum(1 for d in decisions if not d['approve'])
print('sustained:', 200 - flipped, 'flipped:', flipped)

out = base + r'\tmp\decisions\_recheck_batch13.json'
with io.open(out, 'w', encoding='utf-8') as f:
    json.dump(decisions, f, ensure_ascii=False, indent=1)
print('wrote', out)

back = json.load(open(out, encoding='utf-8'))
print('reparse ok, entries:', len(back), 'order ok:', [d['title'] for d in back] == [it['title'] for it in items])
print('flipped titles:', [d['title'] for d in back if not d['approve']])
