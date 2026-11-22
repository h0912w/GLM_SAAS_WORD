import json

req_path = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST\judgment\review_titles_chunk30_round1_request.json"
out_path = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST\tmp\decisions\_chunk30_decisions.json"

with open(req_path, encoding="utf-8") as f:
    req = json.load(f)

V = {}

def A(t, c=0.74):
    V[t] = (True, c, "")

def R(t, c, reason):
    V[t] = (False, c, reason)

# ---- query-clause grid approvals (review stage; market decided by KP gate) ----
for t, c in [
    ("Hydrangea Sentences", 0.74), ("Surgery Translations", 0.74), ("Notary Anagrams", 0.74),
    ("Lapse Orthography", 0.72), ("Driveway Syllables", 0.74), ("Wildlife Rhymes", 0.74),
    ("Drums Synonyms", 0.76), ("Genealogy Antonyms", 0.74), ("Suture Sentences", 0.74),
    ("Waiver Translations", 0.74), ("Writing Conjugations", 0.78), ("Ornament Anagrams", 0.74),
    ("Dispensing Syllables", 0.74), ("Fuel Synonyms", 0.74), ("Shift Antonyms", 0.74),
    ("Filtration Sentences", 0.74), ("Masterkey Translations", 0.74), ("Terminology Conjugations", 0.76),
    ("Storage Anagrams", 0.74), ("Renewal Orthography", 0.72), ("Orchard Syllables", 0.74),
    ("Election Rhymes", 0.74), ("Writer Synonyms", 0.74), ("Commute Antonyms", 0.74),
    ("Hotspot Sentences", 0.74), ("Phishing Translations", 0.74), ("Request Anagrams", 0.74),
    ("Alignment Orthography", 0.72), ("Gasket Syllables", 0.74), ("Fitting Rhymes", 0.74),
    ("Festival Synonyms", 0.74), ("Recital Antonyms", 0.76), ("Crossword Sentences", 0.74),
    ("Hydrangea Translations", 0.74), ("Bond Anagrams", 0.74), ("Foreclosure Orthography", 0.72),
    ("Garbage Syllables", 0.74), ("Driveway Rhymes", 0.74), ("Wildlife Synonyms", 0.74),
    ("Drums Antonyms", 0.76), ("Genealogy Sentences", 0.74), ("Suture Translations", 0.74),
    ("Writing Anagrams", 0.74), ("Goldfish Orthography", 0.72), ("Commission Syllables", 0.74),
    ("Dispensing Rhymes", 0.74), ("Fuel Antonyms", 0.74), ("Shift Sentences", 0.74),
    ("Filtration Translations", 0.74), ("Terminology Anagrams", 0.74), ("Prototype Syllables", 0.74),
    ("Orchard Rhymes", 0.74), ("Election Synonyms", 0.74), ("Writer Antonyms", 0.74),
    ("Commute Sentences", 0.74), ("Hotspot Translations", 0.74), ("Database Anagrams", 0.74),
    ("Parking Syllables", 0.74), ("Gasket Rhymes", 0.74), ("Fitting Synonyms", 0.74),
    ("Festival Antonyms", 0.74), ("Recital Sentences", 0.76), ("Crossword Translations", 0.74),
    ("Hygienist Syllables", 0.74), ("Garbage Rhymes", 0.74), ("Driveway Synonyms", 0.74),
    ("Wildlife Antonyms", 0.74), ("Drums Sentences", 0.76), ("Genealogy Translations", 0.74),
    ("Waiver Anagrams", 0.74), ("Cupcake Orthography", 0.72), ("Cemetery Syllables", 0.74),
    ("Commission Rhymes", 0.74), ("Dispensing Synonyms", 0.74), ("Fuel Sentences", 0.74),
    ("Shift Translations", 0.74), ("Masterkey Anagrams", 0.74), ("Semester Syllables", 0.74),
    ("Prototype Rhymes", 0.74), ("Orchard Synonyms", 0.74), ("Election Antonyms", 0.74),
    ("Writer Sentences", 0.74), ("Commute Translations", 0.74), ("Phishing Anagrams", 0.74),
    ("Applicant Orthography", 0.72), ("Slideshow Syllables", 0.74), ("Parking Rhymes", 0.74),
    ("Gallery Orthography", 0.72), ("Florist Orthography", 0.72), ("Weighbridge Orthography", 0.72),
    ("Floss Orthography", 0.72),
]:
    A(t, c)

# ---- Conjugations with non-grammar anchors: clarity rejects ----
R("Bond Conjugations", 0.7, "Clarity: financial bonds are not a conjugated grammar form; 'bond conjugations' names no verb-conjugation product a finance buyer would recognize.")
R("Surgery Conjugations", 0.7, "Clarity: surgical procedures take no grammatical conjugation; the pairing names no recognizable product.")
R("Waiver Conjugations", 0.7, "Clarity: a waiver is a document, not a conjugated verb form; no grammar-product reading survives.")
R("Hydrangea Conjugations", 0.7, "Clarity: plant names have no grammatical conjugation; unclear what product this pairing names.")
R("Suture Conjugations", 0.7, "Clarity: sutures are not conjugated; the combination suggests no coherent SaaS product.")
R("Filtration Conjugations", 0.7, "Clarity: filtration is a process, not a conjugated verb; no grammar reading exists for an HVAC buyer.")
R("Masterkey Conjugations", 0.7, "Clarity: 'masterkey' has no grammatical conjugation; the pairing names nothing recognizable.")
R("Hotspot Conjugations", 0.7, "Clarity: hotspots are not conjugated verb forms; unclear what a telecom buyer would receive.")
R("Phishing Conjugations", 0.7, "Clarity: phishing has no grammatical conjugation; the combination names no coherent product.")
R("Database Conjugations", 0.7, "Clarity: a database is not a conjugated grammar form; no verb-conjugation product reading.")

# ---- Chords / Lyrics with clearly non-music anchors: clarity rejects ----
R("Weighbridge Chords", 0.72, "Clarity: weighbridges are industrial scales with no musical-chord reading; names no recognizable product.")
R("Cupcake Chords", 0.72, "Clarity: a bakery anchor carries no musical-chord reading; 'cupcake chords' names nothing a stranger can identify.")
R("Notary Chords", 0.72, "Clarity: notarization has no musical-chord meaning; unclear what product this names.")
R("Ornament Chords", 0.72, "Clarity: decor ornaments have no chord reading; the pairing names no coherent tool.")
R("Gallery Chords", 0.72, "Clarity: a photo-gallery anchor gives no musical-chord product reading.")
R("Applicant Chords", 0.72, "Clarity: job applicants have no musical-chord reading; unclear what this SaaS would do.")
R("Storage Chords", 0.72, "Clarity: storage services have no chord meaning; the combination names no recognizable product.")
R("Request Chords", 0.72, "Clarity: support requests have no musical-chord reading; names nothing identifiable.")
R("Writing Chords", 0.72, "Clarity: writing is a text activity, not a chord-based music one; the pairing is unclear as a product.")
R("Terminology Chords", 0.72, "Clarity: terminology management has no musical-chord reading; unclear what this names.")
R("Database Chords", 0.72, "Clarity: databases have no musical-chord reading; the combination names no product.")
R("Bond Chords", 0.72, "Clarity: financial bonds have no musical-chord meaning; unclear what this SaaS is.")
R("Foreclosure Lyrics", 0.72, "Clarity: foreclosure processing has no lyric reading; a stranger cannot tell what product this is.")
R("Goldfish Lyrics", 0.72, "Clarity: a veterinary/pet anchor gives no lyrics reading; names no recognizable tool.")
R("Cupcake Lyrics", 0.72, "Clarity: a bakery anchor carries no lyric meaning; unclear what this product does.")
R("Florist Lyrics", 0.72, "Clarity: floristry has no lyric reading; the pairing names no coherent SaaS.")
R("Gallery Lyrics", 0.72, "Clarity: photo galleries have no lyric meaning; unclear what a buyer would get.")
R("Storage Lyrics", 0.72, "Clarity: storage services have no lyric reading; the combination names nothing identifiable.")
R("Request Lyrics", 0.72, "Clarity: support requests carry no lyric meaning; names no recognizable product.")
R("Applicant Lyrics", 0.72, "Clarity: recruiting applicants have no lyric reading; unclear what this SaaS is.")
R("Keynote Lyrics", 0.72, "Clarity: a keynote is a speech, not sung lyrics; the pairing names no coherent product.")
R("Ornament Lyrics", 0.72, "Clarity: decor ornaments have no lyric reading; the combination is unidentifiable.")
R("Weighbridge Lyrics", 0.72, "Clarity: industrial weighing has no lyric reading; names nothing a stranger recognizes.")
R("Notary Lyrics", 0.72, "Clarity: notarization has no lyric meaning; unclear what product this names.")

# ---- Keynote Orthography: Apple Keynote trademark ----
R("Keynote Orthography", 0.68, "Trademark similarity: Keynote is Apple's famous presentation software; the pairing reads as that brand rather than a generic spelling tool.")

# ---- food_service grid ----
R("Acai Claim", 0.62, "Clarity: no clear reading of what an acai bowl shop would 'claim'; claim adjustment reads as insurance, not a visible product function.")
A("Bruschetta Checkin", 0.66)
R("Prosciutto Length", 0.62, "Clarity: 'length of prosciutto' names no tool; bare attribute fragment, same family as the rejected Pierogi Width.")
R("Tabbouleh Distance", 0.62, "Clarity: distance of what? no measurable business object is named; reads as an unanchored fragment.")
A("Edamame Limit", 0.64)
R("Ceviche Clock", 0.65, "Clarity: a clock is not a function a ceviche kitchen buys; matches the rejected Tzatziki Clock pattern.")
R("Guacamole Speed", 0.7, "Trademark similarity: Guacamole is Apache's remote-access software (chunk-24 precedent); a speed-metric pairing reads as that brand context, not a food product.")
R("Empanada Height", 0.65, "Clarity: height of an empanada is a meaningless product attribute; no tool reading survives.")
A("Bratwurst Temperature", 0.7)
R("Escargot Load", 0.62, "Clarity: load of what? no recognizable kitchen or business object is anchored; bare fragment.")
R("Gyro Wattage", 0.65, "Clarity: wattage of a gyro is absurd; no appliance or equipment reading attaches to the pairing.")
R("Quinoa Frequency", 0.62, "Clarity: frequency of what? no object is named; reads as a bare attribute fragment, not a tool.")
R("Mochi Compatibility", 0.62, "Clarity: compatibility of mochi with what is unspecified; unreadable fragment with no product meaning.")
A("Satay Capacity", 0.66)
A("Moussaka Usage", 0.62)
A("Borscht Condition", 0.6)
R("Gumbo Humidity", 0.65, "Clarity: humidity is not a measurable business object for a gumbo kitchen; unreadable pairing.")
R("Jambalaya Episode", 0.65, "Clarity: 'jambalaya episode' suggests a TV episode, not a product; no SaaS reading.")
A("Shawarma Cycle", 0.6)
A("Naan Breakdown", 0.62)
R("Arepa Sensor", 0.62, "Clarity: a sensor for what? no kitchen object is named; reads as an absurd IoT fragment.")
R("Pierogi Reception", 0.62, "Clarity: reception of what? no front-desk or signal reading attaches to pierogi; fragment.")
A("Goulash Followup", 0.63)
A("Tzatziki Approval", 0.62)
A("Acai Onboarding", 0.62)
R("Bruschetta Size", 0.6, "Clarity: size of what is unspecified; unanchored attribute fragment rather than a named tool.")
A("Prosciutto Weight", 0.63)
R("Tabbouleh Range", 0.62, "Clarity: range of what - price, temperature, menu? nothing is anchored; fragment.")
R("Edamame Type", 0.62, "Clarity: type of edamame is a catalog field, not a product; no tool reading.")
A("Ceviche Time", 0.65)
R("Guacamole Depth", 0.72, "Trademark similarity: reads as an Apache Guacamole (remote-desktop brand) metric rather than a food product; 'depth of guacamole' is also meaningless on its own.")
R("Empanada Width", 0.65, "Clarity: width of an empanada is absurd; matches the rejected Pierogi Width pattern.")
R("Bratwurst Pressure", 0.62, "Clarity: pressure of what? no cooking or business object is anchored; fragment.")
R("Escargot Voltage", 0.65, "Clarity: voltage of escargot is absurd; no appliance reading survives.")
R("Gyro Brightness", 0.65, "Clarity: brightness of a gyro is meaningless; no screen or light object is anchored.")
R("Quinoa Compatibility", 0.62, "Clarity: compatibility of quinoa names no feature or tool; bare attribute fragment.")
A("Mochi Capacity", 0.62)
A("Satay Usage", 0.62)
A("Moussaka Condition", 0.6)
R("Borscht Humidity", 0.65, "Clarity: humidity of borscht is meaningless; no storage or climate object is named.")
R("Gumbo Episode", 0.65, "Clarity: 'gumbo episode' names a show segment, not a product; unclear what this SaaS is.")
A("Jambalaya Cycle", 0.6)
A("Shawarma Breakdown", 0.62)
R("Naan Sensor", 0.62, "Clarity: a sensor for what is unspecified; no readable kitchen tool emerges.")
R("Arepa Reception", 0.62, "Clarity: reception is unanchored here; no desk or signal reading attaches to arepa.")
A("Pierogi Followup", 0.63)
A("Goulash Approval", 0.62)
R("Tzatziki Matrix", 0.62, "Clarity: a matrix of what? abstract fragment with no feature or object meaning.")
A("Acai Checkin", 0.66)
R("Bruschetta Length", 0.62, "Clarity: length of bruschetta names no tool; bare attribute fragment like the rejected Pierogi Width.")
R("Prosciutto Distance", 0.62, "Clarity: distance of prosciutto is meaningless; no delivery-radius or measurement object is anchored.")
A("Tabbouleh Limit", 0.63)
R("Edamame Clock", 0.65, "Clarity: a clock is not a function an edamame kitchen buys; matches the rejected Tzatziki Clock pattern.")
A("Ceviche Speed", 0.61)
R("Guacamole Height", 0.72, "Trademark similarity: collides with Apache Guacamole software branding per chunk-24 precedent; 'height of guacamole' also names no product.")
A("Empanada Temperature", 0.7)
R("Bratwurst Load", 0.62, "Clarity: load of what? grill load is not explicitly anchored; unreadable fragment.")
R("Escargot Wattage", 0.65, "Clarity: wattage of escargot names no tool; absurd fragment.")
R("Gyro Frequency", 0.62, "Clarity: frequency of what? no object is named; unreadable fragment.")
A("Quinoa Capacity", 0.62)
A("Mochi Usage", 0.62)
A("Satay Condition", 0.6)
R("Moussaka Humidity", 0.65, "Clarity: humidity control is not anchored to any moussaka object; unreadable pairing.")
R("Borscht Episode", 0.65, "Clarity: reads as a TV episode title, not a SaaS product; no tool reading.")
A("Gumbo Cycle", 0.6)
A("Jambalaya Breakdown", 0.62)
R("Shawarma Sensor", 0.62, "Clarity: sensor of what is unspecified; no probe or kitchen object is anchored to make it readable.")
R("Naan Reception", 0.62, "Clarity: reception of what? no front-desk or signal reading attaches to naan; fragment.")
A("Arepa Followup", 0.63)
A("Pierogi Approval", 0.62)
R("Goulash Matrix", 0.62, "Clarity: matrix of what? no object or feature is anchored; unidentifiable fragment.")
R("Tzatziki Evaluation", 0.62, "Clarity: evaluation of what? no assessment object is anchored; bare fragment.")
A("Surgery Anagrams", 0.74)
A("Gasket Synonyms", 0.74)

decisions = []
missing = []
for it in req["items"]:
    t = it["title"]
    if t not in V:
        missing.append(t)
        continue
    ap, c, reason = V[t]
    if ap:
        checks = {"clarity": True, "duplication": True, "trademark": True}
    else:
        fail = "trademark" if "Trademark" in reason else "clarity"
        checks = {"clarity": fail != "clarity", "duplication": True, "trademark": fail != "trademark"}
    decisions.append({"title": t, "approve": ap, "confidence": c, "reason": reason, "checks": checks})

assert not missing, "missing verdicts: %s" % missing
assert len(decisions) == len(req["items"]), (len(decisions), len(req["items"]))
assert [d["title"] for d in decisions] == [it["title"] for it in req["items"]]
for d in decisions:
    if d["approve"]:
        assert d["checks"] == {"clarity": True, "duplication": True, "trademark": True}
        assert d["confidence"] >= 0.6
    else:
        assert not all(d["checks"].values())
        assert d["reason"].strip()

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(decisions, f, ensure_ascii=False, indent=1)

ap = sum(1 for d in decisions if d["approve"])
print("items=%d approve=%d reject=%d" % (len(decisions), ap, len(decisions) - ap))
print("written:", out_path)
