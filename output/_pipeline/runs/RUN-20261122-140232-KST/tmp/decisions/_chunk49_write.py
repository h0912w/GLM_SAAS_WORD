import json

req_path = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST\judgment\review_titles_chunk49_round1_request.json"
out_path = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST\tmp\decisions\_chunk49_decisions.json"

with open(req_path, encoding="utf-8") as f:
    req = json.load(f)
items = req["items"]


def ap(conf):
    return {"approve": True, "confidence": conf, "reason": "",
            "checks": {"clarity": True, "duplication": True, "trademark": True}}


def rj(conf, why):
    return {"approve": False, "confidence": conf,
            "reason": "Clarity: " + why,
            "checks": {"clarity": False, "duplication": True, "trademark": True}}


D = {}

# --- Block A: query-clause pairs (non-exempt words approved at review stage) ---
D["Berth Antonyms"] = ap(0.65)
D["Compressor Conjugations"] = rj(0.8, "a compressor is a mechanical noun with no verb form to conjugate; the pair names no recognizable grammar or language product")
D["Cylinder Anagrams"] = ap(0.6)
D["Proofing Chords"] = rj(0.8, "translation/document proofing has no chord or music reading; a stranger cannot identify any SaaS product here")
D["Unpacking Lyrics"] = rj(0.8, "moving/unpacking services carry no lyrics or song-content reading; the pair names no identifiable product")
D["Proof Orthography"] = ap(0.7)
D["Barcode Syllables"] = ap(0.6)
D["Valet Rhymes"] = ap(0.6)
D["Homework Synonyms"] = ap(0.7)
D["Welding Antonyms"] = ap(0.6)
D["Tractor Sentences"] = ap(0.6)
D["Donation Translations"] = ap(0.65)
D["Vote Conjugations"] = ap(0.6)
D["Reader Anagrams"] = ap(0.6)
D["Carpool Chords"] = rj(0.75, "carpooling has no chord or music-notation reading; no recognizable product is named")
D["Router Lyrics"] = rj(0.8, "a network router has no lyrics or song-content reading; the pair names no identifiable product")
D["Password Orthography"] = ap(0.65)
D["Public Syllables"] = ap(0.6)
D["Column Rhymes"] = ap(0.6)
D["Hold Synonyms"] = ap(0.6)
D["Job Antonyms"] = ap(0.6)
D["Seating Sentences"] = ap(0.6)
D["Brake Translations"] = ap(0.6)
D["Pizzeria Conjugations"] = rj(0.8, "pizzeria is a place noun with no verb form to conjugate; the pair names no recognizable grammar product")
D["Cage Anagrams"] = ap(0.6)
D["Extraction Chords"] = rj(0.8, "dental extraction has no chord or music reading; the pair names no recognizable product")
D["Squat Lyrics"] = rj(0.8, "squat training has no lyrics or song-content reading; a stranger cannot identify a product")
D["Daycare Orthography"] = ap(0.6)
D["Taco Syllables"] = ap(0.6)
D["Fish Rhymes"] = ap(0.6)
D["Snoring Synonyms"] = ap(0.6)
D["Triathlon Antonyms"] = ap(0.6)
D["Bathtub Sentences"] = ap(0.6)
D["Landlord Translations"] = ap(0.6)
D["Beachfront Conjugations"] = rj(0.8, "beachfront is a place noun with no verb form to conjugate; the pair names no clear language product")
D["Melody Anagrams"] = ap(0.7)
D["Leatherworking Chords"] = rj(0.8, "leatherworking has no chord or music reading; no recognizable product is named")
D["Sleep Lyrics"] = rj(0.75, "sleep healthcare has no lyrics reading (the lullaby association is too indirect); a stranger cannot tell what SaaS this is")

D["Acquittal Orthography"] = ap(0.65)

# --- Block A food (restaurant-ops / food-content readings approved; dead patterns rejected) ---
D["Acai Spec"] = ap(0.7)
D["Bruschetta Login"] = rj(0.75, "a bruschetta kitchen has no account-login reading; Login is a dead SaaS-pattern fragment here, naming no recognizable product (same failure as Gyro Login)")
D["Prosciutto Coach"] = ap(0.65)
D["Tabbouleh Help"] = ap(0.7)
D["Edamame Basics"] = ap(0.7)
D["Ceviche Questions"] = ap(0.65)
D["Guacamole Steps"] = ap(0.7)
D["Empanada Courses"] = ap(0.7)
D["Bratwurst Repairs"] = rj(0.75, "bratwurst has no repair reading; equipment repair is a service, not a product this title names, so the fragment pairing is unreadable")
D["Escargot Walking"] = rj(0.75, "escargot has no walking reading; Walking is a dead-pattern fragment here and a stranger cannot tell what SaaS this is")
D["Gyro Checkups"] = ap(0.62)
D["Quinoa Appointments"] = ap(0.65)
D["Mochi Screenings"] = ap(0.6)
D["Satay Walkthroughs"] = ap(0.65)
D["Moussaka Designs"] = ap(0.6)
D["Borscht Portraits"] = ap(0.6)
D["Gumbo Albums"] = ap(0.6)
D["Jambalaya Collages"] = ap(0.6)
D["Shawarma Stickers"] = ap(0.65)
D["Naan Printables"] = ap(0.65)
D["Arepa Hours"] = ap(0.7)
D["Pierogi Stores"] = ap(0.7)
D["Goulash Suppliers"] = ap(0.7)
D["Tzatziki Interviews"] = ap(0.65)

# --- Block B: query-clause pairs ---
D["Service Rhymes"] = ap(0.6)
D["Retail Synonyms"] = ap(0.6)
D["Adherence Antonyms"] = ap(0.6)
D["Berth Sentences"] = ap(0.6)
D["Compressor Anagrams"] = ap(0.6)
D["Cylinder Chords"] = rj(0.8, "a lock cylinder has no chord or music reading; the pair names no recognizable product")
D["Proofing Lyrics"] = rj(0.8, "translation proofing has no lyrics reading; a stranger cannot identify any SaaS product")
D["Unpacking Orthography"] = ap(0.6)
D["Scaffold Syllables"] = ap(0.6)
D["Barcode Rhymes"] = ap(0.6)
D["Valet Synonyms"] = ap(0.6)
D["Homework Antonyms"] = ap(0.65)
D["Welding Sentences"] = ap(0.6)
D["Tractor Translations"] = ap(0.6)
D["Donation Conjugations"] = rj(0.8, "donation is a noun with no verb-conjugation product reading; a stranger cannot identify what this SaaS does")
D["Vote Anagrams"] = ap(0.6)
D["Reader Chords"] = rj(0.75, "a publication reader has no chord-sheet or music reading; no recognizable product is named")
D["Carpool Lyrics"] = rj(0.7, "beyond the indirect carpool-karaoke association the pair does not name an identifiable lyrics product a stranger would recognize")
D["Router Orthography"] = ap(0.6)
D["Internship Syllables"] = ap(0.65)
D["Public Rhymes"] = ap(0.6)
D["Column Synonyms"] = ap(0.6)
D["Hold Antonyms"] = ap(0.6)
D["Job Sentences"] = ap(0.6)
D["Seating Translations"] = ap(0.6)
D["Brake Conjugations"] = rj(0.8, "brake is a mechanical noun with no conjugation reading; the pair names no recognizable product")
D["Pizzeria Anagrams"] = ap(0.6)
D["Cage Chords"] = rj(0.8, "an animal cage has no chord or music reading; no recognizable product is named")
D["Extraction Lyrics"] = rj(0.8, "dental extraction has no lyrics reading; the pair names no identifiable product")
D["Squat Orthography"] = ap(0.6)
D["Birthday Syllables"] = ap(0.65)
D["Taco Rhymes"] = ap(0.6)
D["Fish Synonyms"] = ap(0.6)
D["Snoring Antonyms"] = ap(0.6)
D["Triathlon Sentences"] = ap(0.6)
D["Bathtub Translations"] = ap(0.6)
D["Landlord Conjugations"] = rj(0.8, "landlord is a person noun with no grammar reading; no identifiable product is named")
D["Beachfront Anagrams"] = ap(0.6)
D["Melody Chords"] = ap(0.85)
D["Leatherworking Lyrics"] = rj(0.8, "leatherworking has no lyrics or song-content reading; a stranger cannot identify a product")
D["Sleep Orthography"] = ap(0.6)

# --- Block B food ---
D["Acai Quantity"] = ap(0.7)
D["Bruschetta Analysis"] = ap(0.7)
D["Prosciutto Habit"] = rj(0.7, "'prosciutto habit' names no recognizable habit-tracking or operations product for a food business; the fragment pairing is unreadable")
D["Tabbouleh Ideas"] = ap(0.65)
D["Edamame Names"] = ap(0.6)
D["Ceviche Date"] = ap(0.6)
D["Guacamole Alternatives"] = ap(0.7)
D["Empanada Examples"] = ap(0.65)
D["Bratwurst Sitting"] = rj(0.75, "bratwurst has no sitting reading; Sitting is a dead-pattern fragment here, naming no identifiable product")
D["Escargot Visits"] = ap(0.6)
D["Gyro Refills"] = ap(0.65)
D["Quinoa Screenings"] = ap(0.6)
D["Mochi Walkthroughs"] = ap(0.65)
D["Satay Designs"] = ap(0.6)
D["Moussaka Portraits"] = ap(0.6)
D["Borscht Albums"] = ap(0.6)
D["Gumbo Collages"] = ap(0.6)
D["Jambalaya Stickers"] = ap(0.65)
D["Shawarma Printables"] = ap(0.65)
D["Naan Hours"] = ap(0.7)
D["Arepa Stores"] = ap(0.7)
D["Pierogi Suppliers"] = ap(0.7)
D["Goulash Interviews"] = ap(0.65)
D["Tzatziki Stories"] = ap(0.65)

# --- Block C: query-clause pairs ---
D["Supply Syllables"] = ap(0.6)
D["Service Synonyms"] = ap(0.6)
D["Retail Antonyms"] = ap(0.6)
D["Adherence Sentences"] = ap(0.6)
D["Berth Translations"] = ap(0.6)
D["Compressor Chords"] = rj(0.8, "an HVAC compressor has no chord or music reading; the pair names no recognizable product")
D["Cylinder Lyrics"] = rj(0.8, "a lock cylinder has no lyrics reading; a stranger cannot identify a product")
D["Proofing Orthography"] = ap(0.6)
D["Overtime Syllables"] = ap(0.65)
D["Scaffold Rhymes"] = ap(0.6)
D["Barcode Synonyms"] = ap(0.6)
D["Valet Antonyms"] = ap(0.6)
D["Homework Sentences"] = ap(0.65)
D["Welding Translations"] = ap(0.6)
D["Tractor Conjugations"] = rj(0.8, "tractor is a machine noun with no verb-conjugation reading; a stranger cannot tell what this SaaS is")
D["Donation Anagrams"] = ap(0.6)
D["Vote Chords"] = rj(0.75, "voting has no chord or music reading; the pair names no recognizable product")
D["Reader Lyrics"] = rj(0.7, "'reader lyrics' does not identify any specific lyrics tool or product for a stranger; the reading is too vague to name a SaaS")
D["Carpool Orthography"] = ap(0.6)
D["Foundation Syllables"] = ap(0.65)
D["Internship Rhymes"] = ap(0.6)
D["Public Synonyms"] = ap(0.6)
D["Column Antonyms"] = ap(0.6)
D["Hold Sentences"] = ap(0.6)
D["Job Translations"] = ap(0.6)
D["Seating Conjugations"] = ap(0.6)
D["Brake Anagrams"] = ap(0.6)
D["Pizzeria Chords"] = rj(0.8, "a pizzeria has no chord or music-notation reading; no identifiable product is named")
D["Cage Lyrics"] = rj(0.8, "an animal cage has no lyrics content reading; a stranger cannot identify a SaaS here")
D["Extraction Orthography"] = ap(0.6)
D["Degree Syllables"] = ap(0.65)
D["Birthday Rhymes"] = ap(0.6)
D["Taco Synonyms"] = ap(0.6)
D["Fish Antonyms"] = ap(0.6)
D["Snoring Sentences"] = ap(0.6)
D["Triathlon Translations"] = ap(0.6)
D["Bathtub Conjugations"] = rj(0.8, "bathtub is an object noun with no conjugation reading; the pair names no recognizable product")
D["Landlord Anagrams"] = ap(0.6)
D["Beachfront Chords"] = rj(0.8, "beachfront tourism has no chord or music reading; no identifiable product is named")
D["Melody Lyrics"] = ap(0.85)
D["Leatherworking Orthography"] = ap(0.6)

# --- Block C food ---
D["Acai Login"] = rj(0.75, "an acai shop has no account-login reading; Login is a dead SaaS-pattern fragment here (same failure as Gyro Login)")
D["Bruschetta Coach"] = ap(0.65)
D["Prosciutto Help"] = ap(0.7)
D["Tabbouleh Basics"] = ap(0.7)
D["Edamame Questions"] = ap(0.65)
D["Ceviche Steps"] = ap(0.7)
D["Guacamole Courses"] = ap(0.65)
D["Empanada Repairs"] = rj(0.75, "empanada has no repair reading; equipment repair is not a product this title names, so the pairing is unreadable")
D["Bratwurst Walking"] = rj(0.75, "bratwurst has no walking reading; Walking is a dead-pattern fragment here, naming no identifiable product")
D["Escargot Checkups"] = ap(0.6)
D["Gyro Appointments"] = ap(0.65)
D["Quinoa Walkthroughs"] = ap(0.65)
D["Mochi Designs"] = ap(0.6)
D["Satay Portraits"] = ap(0.6)
D["Moussaka Albums"] = ap(0.6)
D["Borscht Collages"] = ap(0.6)
D["Gumbo Stickers"] = ap(0.65)
D["Jambalaya Printables"] = ap(0.65)
D["Shawarma Hours"] = ap(0.7)
D["Naan Stores"] = ap(0.7)
D["Arepa Suppliers"] = ap(0.7)
D["Pierogi Interviews"] = ap(0.65)
D["Goulash Stories"] = ap(0.65)
D["Tzatziki Lessons"] = ap(0.7)

# --- Final block ---
D["Irrigation Syllables"] = ap(0.6)
D["Supply Rhymes"] = ap(0.6)
D["Service Antonyms"] = ap(0.6)
D["Retail Sentences"] = ap(0.6)
D["Adherence Translations"] = ap(0.6)
D["Berth Conjugations"] = rj(0.8, "berth is a place noun with no verb form to conjugate; the pair names no clear language product")
D["Compressor Lyrics"] = rj(0.8, "an HVAC compressor has no lyrics reading; a stranger cannot tell what product this names")

# verification: 1:1 coverage in exact order, no missing/extra
titles = [it["title"] for it in items]
missing = [t for t in titles if t not in D]
extra = [t for t in D if t not in set(titles)]
dupes = [t for t in set(titles) if titles.count(t) > 1]
assert not missing, "missing decisions: %s" % missing
assert not extra, "extra decisions: %s" % extra
assert not dupes, "duplicate titles in batch: %s" % dupes

out = []
for t in titles:
    d = D[t]
    out.append({"title": t, "approve": d["approve"], "confidence": d["confidence"],
                "reason": d["reason"], "checks": d["checks"]})

# logical consistency: approve iff all checks true; reject has >=1 false; rejects have reason
for d in out:
    c = d["checks"]
    assert set(c.keys()) == {"clarity", "duplication", "trademark"}
    if d["approve"]:
        assert all(c.values()) and d["confidence"] >= 0.6
    else:
        assert not all(c.values()) and d["reason"].strip()

with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print("items:", len(items), "written:", len(out))
print("approve:", sum(1 for d in out if d["approve"]), "reject:", sum(1 for d in out if not d["approve"]))
