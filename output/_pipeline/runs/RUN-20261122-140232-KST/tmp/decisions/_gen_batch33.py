import json, os

req = json.load(open('output/_pipeline/runs/RUN-20261122-140232-KST/judgment/review_titles_recheck_round1_request.json', encoding='utf-8'))
items = req['items'][6600:6800]

# --- Per-title judgments decided by the reviewing agent; script only formats/writes ---
# flips: idx -> (conf, reason)
flips = {
 33: (0.65, "refuted: 'Tournament' is an event fragment with no readable product or service demand on an acai anchor - unclear what a searcher would actually find (eating contest? sponsorship?); fails title clarity"),
 38: (0.70, "refuted: 'Names' on a food anchor is a vague fragment (brand naming? name list?) with no clear business reading; established dead pattern on food anchors"),
 41: (0.70, "refuted: 'Visits' is a dead fragment on a food anchor - visits to what, by whom, is undefined; no plausible borscht-related operation named"),
 42: (0.60, "refuted: 'Checkups' reads as a medical/health fragment attached to a dish anchor - no plausible food-service operation or product called 'Gumbo Checkups'"),
 45: (0.60, "refuted: 'Screenings' has no readable pairing with a bread anchor (film screening? health screening?); unresolved fragment, fails clarity"),
 49: (0.60, "refuted: 'Albums' is a vague fragment on a dish anchor - unlike 'Portraits' it names no established food-photography or menu product; the demand reading is unclear"),
 57: (0.70, "refuted: 'trip' is a trivially spelled generic word with no orthographic dispute and no plausible spelling-debate demand; anchor-function pairing defective"),
 66: (0.70, "refuted: 'chef' has no real orthographic dispute or spelling-debate demand; no plausible audience for 'Chef Orthography'"),
 82: (0.70, "refuted: 'bite' is trivially spelled with no spelling-debate demand; no plausible reader for 'Bite Orthography'"),
 85: (0.70, "refuted: 'Workbook' on a food anchor is a vague fragment (established dead pattern) - no clear workbook product exists for a dish"),
 100: (0.70, "refuted: 'sink' has no orthographic dispute and no plausible spelling-debate demand; pairing defective"),
 131: (0.70, "refuted: 'Names' fragment on a food anchor - no clear business reading (naming service? name generator?); established dead pattern"),
 148: (0.65, "refuted: 'speaker' has no real spelling-debate demand, same defect family as the Driver/Repair Orthography flips; pairing defective"),
 156: (0.55, "sustained: 'supplement' is a frequently misspelled word (suplement, dropped p); plausible spelling demand"),
 166: (0.60, "refuted: 'noodle' has no established orthographic dispute beyond generic guesswork; no plausible spelling-debate demand for this anchor"),
 168: (0.70, "refuted: 'Workbook' vague fragment on a food anchor, established dead pattern; no clear demand reading"),
}

# special sustains: idx -> (conf, reason)
special = {
 0: (0.55, "sustained: 'Tzatziki Portraits' reads clearly as food photography / dish portraiture, an established genre; no duplication or trademark defect"),
 8: (0.60, "sustained: vocal orthography is a real linguistics/phonetics topic (how vocalic sounds are spelled) plus vocal-music term spelling; plausible demand"),
 16: (0.60, "sustained: 'kennel' is frequently misspelled (kenel/kennle), so a spelling-debate demand is plausible"),
 24: (0.60, "sustained: 'simultaneous' is a commonly misspelled long word (simultanous); plausible spelling demand"),
 32: (0.55, "sustained: compound spelling ambiguity (barbell vs bar bell) plus double-letter misspelling gives plausible orthography demand"),
 34: (0.55, "sustained: reads as a bruschetta recipe/ordering app - clear app-category reading, unlike software-context Guacamole trademark flips"),
 35: (0.55, "sustained: portion/ordering quantity for edamame is a readable restaurant-ops reading"),
 36: (0.60, "sustained: nutritional/food-cost analysis of ceviche is a clear restaurant-ops reading"),
 37: (0.65, "sustained: 'Empanada Ideas' is the natural recipe-idea query; clear and defect-free"),
 39: (0.55, "sustained: ingredient/dish substitutes ('gyro alternatives') is a real query pattern; no clarity or trademark defect"),
 40: (0.55, "sustained: 'Quinoa Examples' reads as dish/usage examples - readable, though weak"),
 43: (0.65, "sustained: Refills on a food anchor is an established restaurant-ops reading"),
 44: (0.65, "sustained: Appointments on a food anchor is an established restaurant-ops reading"),
 46: (0.55, "sustained: cooking walkthroughs for arepa preparation is a readable content reading"),
 47: (0.55, "sustained: 'Goulash Portraits' reads as food photography/dish portraiture, an established genre"),
 48: (0.55, "sustained: 'Goulash Portraits' reads as food photography/dish portraiture, an established genre; no duplication or trademark defect"),
 65: (0.55, "sustained: Speaker Chords reads in the audio/music-hardware category (like the sustained Smartphone Chords) - speakers reproduce chords; music-context defense"),
 74: (0.60, "sustained: 'pinning vs pining' is a real double-letter/homophone spelling confusion; plausible orthography demand"),
 83: (0.65, "sustained: Flyer on a food anchor is an established restaurant-marketing reading"),
 84: (0.65, "sustained: Tips on a food anchor is an established restaurant-ops reading"),
 86: (0.55, "sustained: kitchen spec sheets (recipe specifications) are real restaurant practice; 'Tabbouleh Spec' reads as prep standardization"),
 87: (0.60, "sustained: Coach on a food anchor reads as cooking coach; established reading"),
 88: (0.65, "sustained: cooking basics for empanada making; clear reading"),
 89: (0.55, "sustained: FAQ-style 'questions about bratwurst' content reading; readable though weak"),
 90: (0.65, "sustained: recipe steps for escargot; clear reading"),
 91: (0.60, "sustained: cooking courses featuring/teaching gyro; clear reading"),
 92: (0.65, "sustained: Refills on a food anchor is an established restaurant-ops reading"),
 93: (0.65, "sustained: Appointments on a food anchor is an established restaurant-ops reading"),
 108: (0.55, "sustained: Speaker Lyrics reads in the audio/music category (like sustained Smartphone/Broadcast Lyrics) - lyrics through/about speakers, karaoke; music-context defense"),
 109: (0.60, "sustained: 'emission' is commonly misspelled (emision, double-m confusion); plausible spelling demand"),
 117: (0.55, "sustained: 'dampner' is a frequent real-world misspelling of damper; plausible spelling demand"),
 125: (0.60, "sustained: Parade Chords reads in a music context - marching-band/parade-song guitar and band chords are a real demand; music-context defense per established lines"),
 164: (0.65, "sustained: Graduation Chords is a strong music reading - guitar/piano chords for graduation songs are a well-known search demand; music-context defense per established lines"),
 165: (0.60, "sustained: Parade Lyrics reads in a music context - lyrics of parade/marching songs; music-context defense per established lines"),
 126: (0.60, "sustained: 'ferret' double-r misspelling (feret/ferrit) gives plausible spelling demand"),
 127: (0.55, "sustained: reads as an acai-bowl shop ordering/recipe app; clear app-category reading"),
 128: (0.55, "sustained: portion/ordering quantity for tabbouleh is a readable restaurant-ops reading"),
 129: (0.60, "sustained: nutritional/food-cost analysis of edamame; clear restaurant-ops reading"),
 130: (0.65, "sustained: recipe ideas for guacamole; kitchen-context reading sustained per established lines"),
 132: (0.55, "sustained: ingredient/dish substitutes ('escargot alternatives') is a real query pattern"),
 133: (0.65, "sustained: Refills on a food anchor is an established restaurant-ops reading"),
 134: (0.65, "sustained: Appointments on a food anchor is an established restaurant-ops reading"),
 140: (0.60, "sustained: 'upholstery' is a commonly misspelled long word (upholstry); plausible spelling demand"),
 167: (0.65, "sustained: Tips on a food anchor is an established restaurant-ops reading"),
 169: (0.55, "sustained: kitchen spec sheet reading (recipe standardization) is plausible"),
 170: (0.60, "sustained: Coach on a food anchor reads as cooking coach; established reading"),
 171: (0.65, "sustained: cooking basics for guacamole; kitchen-context reading sustained"),
 172: (0.55, "sustained: FAQ-style 'questions about empanadas' content reading; readable though weak"),
 173: (0.65, "sustained: recipe steps for bratwurst; clear reading"),
 174: (0.60, "sustained: cooking courses featuring escargot; clear reading"),
 175: (0.65, "sustained: Appointments on a food anchor is an established restaurant-ops reading"),
 180: (0.65, "sustained: 'unpacking' is a gerund/verb anchor, so Conjugations is on solid verb-usage ground per established line"),
 182: (0.60, "sustained: 'algae' has a very common misspelling (algea) plus loanword spelling debates; plausible demand"),
 190: (0.70, "sustained: résumé/resume accent orthography (resume vs résumé vs summary spelling) is a genuine, well-known orthographic dispute"),
 197: (0.65, "sustained: 'squat' is a verb, so Conjugations sits on verb-usage ground per established line"),
 199: (0.60, "sustained: 'consultation' is commonly misspelled (consulation - dropped t); plausible spelling demand"),
}

# query-clause templates by function word
tmpl = {
 'Syllables': "sustained: mirrors the natural query 'how many syllables in {a}'; no clarity, duplication, or trademark defect found on re-examination",
 'Rhymes': "sustained: mirrors the natural query 'words that rhyme with {a}'; no defect found on re-examination",
 'Synonyms': "sustained: mirrors the natural query 'synonyms for {a}'; no defect found on re-examination",
 'Antonyms': "sustained: mirrors the natural query 'antonyms of {a}'; no defect found on re-examination",
 'Sentences': "sustained: mirrors the natural query 'sentences with {a}'; no defect found on re-examination",
 'Translations': "sustained: mirrors the natural query 'translate {a}'; no defect found on re-examination",
 'Anagrams': "sustained: mirrors the natural query 'anagrams of {a}'; no defect found on re-examination",
}

decisions = []
for i, it in enumerate(items):
    title = it['title']
    a, fw = title.split()
    if i in flips:
        c, r = flips[i]
        decisions.append({"title": title, "approve": False, "confidence": c, "reason": r})
    elif i in special:
        c, r = special[i]
        decisions.append({"title": title, "approve": True, "confidence": c, "reason": r})
    else:
        t = tmpl.get(fw)
        assert t, (i, title)
        decisions.append({"title": title, "approve": True, "confidence": 0.70, "reason": t.format(a=a)})

out = 'output/_pipeline/runs/RUN-20261122-140232-KST/tmp/decisions/_recheck_batch33.json'
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, 'w', encoding='utf-8') as f:
    json.dump(decisions, f, ensure_ascii=False, indent=1)

# verify
d = json.load(open(out, encoding='utf-8'))
assert len(d) == 200, len(d)
assert [x['title'] for x in d] == [it['title'] for it in items], "order mismatch"
assert all(x['reason'] for x in d)
assert all(0 <= x['confidence'] <= 1 for x in d)
flipped = sum(1 for x in d if not x['approve'])
print("entries:", len(d), "sustained:", 200 - flipped, "flipped:", flipped)
print("path:", os.path.abspath(out))
