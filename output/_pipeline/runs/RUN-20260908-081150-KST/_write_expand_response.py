import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "expand_word_bank_round1_request.json")
RESP = os.path.join(JDIR, "expand_word_bank_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

INSTRUMENTS = ["Piano", "Guitar", "Violin", "Drum", "Vocal", "Ukulele", "Flute",
               "Cello", "Saxophone", "Trumpet", "Clarinet", "Bass", "Organ", "Harp",
               "Oboe", "Viola", "Trombone", "Percussion", "Mandolin", "Accordion",
               "Harmonica"]
EDUCATION = ["Lesson", "Practice", "Recital", "Audition", "Tuning", "Theory", "Chord",
             "Tempo", "Repertoire", "Ensemble", "Accompanist", "Metronome", "Songbook",
             "Method", "Camp", "Choir", "Orchestra", "Melody", "Rhythm", "Beat", "Pitch"]

decisions = []
for w in INSTRUMENTS:
    decisions.append({"type": "domain", "word": w, "industry": "music_lessons",
                      "pattern_tag": "musical_instrument_noun"})
for w in EDUCATION:
    decisions.append({"type": "domain", "word": w, "industry": "music_lessons",
                      "pattern_tag": "music_education_noun"})
for w in ["Retirement", "Estate"]:
    decisions.append({"type": "domain", "word": w, "industry": "finance",
                      "pattern_tag": "finance_lifecycle_noun"})
decisions.append({"type": "domain", "word": "Probate", "industry": "legal",
                  "pattern_tag": "legal_estate_process_noun"})
decisions.append({"type": "domain", "word": "Deed", "industry": "real_estate",
                  "pattern_tag": "property_title_document_noun"})

FUNCTIONS = [
    ("Evaluation", "evaluation_assessment_noun"),
    ("Questionnaire", "questionnaire_form_noun"),
    ("Utilization", "utilization_efficiency_noun"),
    ("Benefit", "benefit_entitlement_noun"),
    ("Requirement", "requirement_criterion_noun"),
    ("Depreciation", "depreciation_valuation_noun"),
    ("Resignation", "resignation_offboarding_noun"),
    ("Hazard", "hazard_safety_noun"),
    ("Guarantor", "guarantor_credit_noun"),
    ("Tuner", "device_calibration_noun"),
]
for w, tag in FUNCTIONS:
    decisions.append({"type": "function", "word": w, "industry": "",
                      "pattern_tag": tag})

domains_music = sum(1 for d in decisions if d["industry"] == "music_lessons")
funcs = sum(1 for d in decisions if d["type"] == "function")
assert domains_music >= 20, domains_music
assert funcs >= 10, funcs
words = [d["word"] for d in decisions]
assert len(words) == len(set(words)), "duplicate words"
for d in decisions:
    assert d["type"] in ("domain", "function")
    assert d["word"] and d["word"][0].isupper() and " " not in d["word"]
    assert d["pattern_tag"]

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
print(f"total={len(decisions)} domain_music={domains_music} functions={funcs}")
print("new pattern tags:", len({d['pattern_tag'] for d in decisions}))
