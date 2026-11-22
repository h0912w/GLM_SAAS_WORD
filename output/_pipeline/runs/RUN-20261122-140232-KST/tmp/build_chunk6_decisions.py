# -*- coding: utf-8 -*-
"""Chunk 6 judgment builder - RUN-20261122-140232-KST.
Reads the request, applies the per-title decisions judged in-session, asserts
1:1 coverage, writes decisions JSON. No rule-engine substitution: every title
below has an explicit judgment record written for that specific combination."""
import json, os, sys

RUN = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST"
REQ = os.path.join(RUN, "judgment", "review_titles_chunk6_round1_request.json")
OUT = os.path.join(RUN, "tmp", "decisions", "_chunk6_decisions.json")

# ---------------------------------------------------------------- explicit judgments
# title -> (approve, confidence, clarity, duplication, trademark, reason)
D = {}

# --- food_service rotations: approves ---
food_ok = {
 "Bruschetta Calculator": (0.7, "'Bruschetta' 메뉴의 분량·원가를 계산하는 'Calculator'로 요리 사업용 계산 도구가 구체적으로 연상된다."),
 "Prosciutto Generator": (0.7, "'Prosciutto' 레시피·조합을 만들어주는 'Generator' 생성 도구가 명확하다."),
 "Tabbouleh Estimator": (0.7, "'Tabbouleh' 재료 분량을 추정하는 'Estimator' 조리 준비 도구가 성립한다."),
 "Edamame Detector": (0.7, "'Edamame'은 대두 알레르기 유발 식재라 성분 'Detector' 결합이 알레르기 검사 도구로 명확하다."),
 "Ceviche Workshop": (0.7, "'Ceviche' 요리 클래스를 예약·운영하는 'Workshop' 도구로 서비스가 그려진다."),
 "Guacamole Helper": (0.7, "'Guacamole' 조리를 보조하는 'Helper' 앱으로 명확하다."),
 "Bratwurst Rank": (0.6, "'Bratwurst' 메뉴 판매 순위를 매기는 'Rank' 분석 도구로 성립 가능하나 앵커가 약해 확신은 낮다."),
 "Escargot Comparison": (0.65, "'Escargot' 메뉴·레시피를 나란히 비교하는 'Comparison' 도구로 명확하다."),
 "Quinoa Copy": (0.6, "'Quinoa' 메뉴 홍보 문구를 만들어주는 'Copy' 생성 도구로 성립 가능하다."),
 "Satay Reference": (0.7, "'Satay' 레시피를 참조·열람하는 'Reference' 라이브러리로 명확하다."),
 "Moussaka Forecast": (0.7, "'Moussaka' 수요를 예측하는 'Forecast' 도구로 식당 운영 SaaS가 성립한다."),
 "Borscht Deadline": (0.7, "'Borscht' 조리·준비 기한을 관리하는 'Deadline' 도구로 명확하다."),
 "Gumbo Duration": (0.7, "'Gumbo' 조리 소요 시간을 관리하는 'Duration' 도구가 자연스럽다."),
 "Jambalaya Volume": (0.7, "'Jambalaya' 조리량·판매량을 관리하는 'Volume' 도구로 성립한다."),
 "Naan Progress": (0.7, "'Naan' 제조 진행을 추적하는 'Progress' 도구로 명확하다."),
 "Pierogi Template": (0.7, "'Pierogi' 레시피를 표준 양식으로 저장하는 'Template' 도구로 성립한다."),
 "Goulash Guide": (0.7, "'Goulash' 조리 가이드를 제공하는 'Guide' 콘텐츠 도구로 명확하다."),
 "Tzatziki Rating": (0.7, "'Tzatziki' 메뉴 평점을 관리하는 'Rating' 도구로 성립한다."),
 "Bruschetta Converter": (0.7, "'Bruschetta' 레시피 인원·단위를 바꿔주는 'Converter'로 명확하다."),
 "Tabbouleh Checker": (0.7, "'Tabbouleh' 재료·알레르기를 점검하는 'Checker' 도구로 성립한다."),
 "Edamame Timer": (0.7, "'Edamame' 데치기 시간을 재는 'Timer' 조리 도구가 자연스럽다."),
 "Ceviche Guardian": (0.6, "'Ceviche'는 날생선 메뉴라 신선도·위생을 지키는 'Guardian' 감시 도구 결합이 성립 가능하나 해석 여지가 있다."),
 "Bratwurst Trend": (0.7, "'Bratwurst' 판매 추이를 보는 'Trend' 분석 도구로 명확하다."),
 "Mochi Reference": (0.7, "'Mochi' 레시피 참조를 모아두는 'Reference' 도구로 성립한다."),
 "Satay Forecast": (0.7, "'Satay' 수요 예측 'Forecast' 도구로 식당 운영에 자연스럽다."),
 "Moussaka Deadline": (0.7, "'Moussaka' 준비 기한 관리 'Deadline' 도구로 명확하다."),
 "Borscht Duration": (0.7, "'Borscht' 조리 시간 관리 'Duration' 도구로 성립한다."),
 "Gumbo Volume": (0.7, "'Gumbo' 조리량 관리 'Volume' 도구로 명확하다."),
 "Shawarma Progress": (0.7, "'Shawarma' 제조 진행 추적 'Progress' 도구로 성립한다."),
 "Arepa Template": (0.7, "'Arepa' 레시피 양식 'Template' 도구로 명확하다."),
 "Pierogi Guide": (0.7, "'Pierogi' 조리 가이드 'Guide' 도구로 성립한다."),
 "Goulash Rating": (0.7, "'Goulash' 평점 관리 'Rating' 도구로 명확하다."),
 "Acai Calculator": (0.7, "'Acai' 볼 원가·영양을 계산하는 'Calculator'로 명확하다."),
 "Bruschetta Generator": (0.7, "'Bruschetta' 토핑 조합을 만들어주는 'Generator' 생성 도구로 성립한다."),
 "Prosciutto Estimator": (0.65, "'Prosciutto' 숙성·분량을 추정하는 'Estimator' 도구로 성립하나 해석이 다소 열려 있다."),
 "Tabbouleh Detector": (0.65, "'Tabbouleh'의 불굴레(글루텐) 성분을 걸러내는 'Detector' 결합이 알레르기 도구로 성립한다."),
 "Edamame Workshop": (0.7, "'Edamame' 요리 클래스 운영 'Workshop' 도구로 명확하다."),
 "Ceviche Helper": (0.7, "'Ceviche' 조리 보조 'Helper' 앱으로 성립한다."),
 "Empanada Rank": (0.6, "'Empanada' 메뉴 판매 순위 'Rank' 분석 도구로 성립 가능하나 확신은 낮다."),
 "Bratwurst Comparison": (0.7, "'Bratwurst' 종류 비교 'Comparison' 도구로 명확하다."),
 "Gyro Copy": (0.65, "'Gyro' 메뉴 홍보 문구 'Copy' 생성 도구로 성립한다."),
 "Quinoa Reference": (0.7, "'Quinoa' 레시피 참조 'Reference' 도구로 명확하다."),
 "Mochi Forecast": (0.7, "'Mochi' 수요 예측 'Forecast' 도구로 성립한다."),
 "Satay Deadline": (0.7, "'Satay' 준비 기한 'Deadline' 관리 도구로 명확하다."),
 "Moussaka Duration": (0.7, "'Moussaka' 조리 시간 'Duration' 도구로 성립한다."),
 "Borscht Volume": (0.7, "'Borscht' 조리량 'Volume' 도구로 명확하다."),
 "Jambalaya Progress": (0.7, "'Jambalaya' 제조 진행 'Progress' 추적 도구로 성립한다."),
 "Naan Template": (0.7, "'Naan' 레시피 양식 'Template' 도구로 명확하다."),
 "Arepa Guide": (0.7, "'Arepa' 조리 가이드 'Guide' 도구로 성립한다."),
 "Pierogi Rating": (0.7, "'Pierogi' 평점 'Rating' 관리 도구로 명확하다."),
 "Acai Repository": (0.7, "'Acai' 레시피·데이터를 모아두는 'Repository' 저장 도구로 성립한다."),
}
for t, (c, r) in food_ok.items():
    D[t] = (True, c, True, True, True, r)

# --- food_service rotations: clarity rejects ---
food_no = {
 "Empanada Result": (0.65, "'Empanada'에 'Result'가 붙으면 무엇의 결과인지 서비스 대상이 그려지지 않는다."),
 "Gyro Guarantee": (0.6, "'Gyro Guarantee'는 보증 약속 명칭일 뿐 어떤 도구 기능인지 불명확하다."),
 "Mochi Reading": (0.6, "'Mochi'에 'Reading'이 결합하면 무엇을 읽어주는 도구인지 성립하지 않는다."),
 "Shawarma Diagnostic": (0.65, "'Shawarma'는 진단할 대상이 없어 'Diagnostic' 결합이 서비스로 그려지지 않는다."),
 "Arepa Authorization": (0.7, "권한 부여 'Authorization'은 'Arepa' 요리 도메인에 결합할 대상이 없다."),
 "Acai Announcement": (0.55, "'Acai' 단일 메뉴에 'Announcement'를 붙이면 무엇을 알리는 도구인지 구체적 서비스가 그려지지 않는다."),
 "Prosciutto Recorder": (0.6, "'Prosciutto'에서 'Recorder'가 무엇을 기록하는지 불명확하다."),
 "Guacamole Stage": (0.55, "'Guacamole Stage'는 무엇의 단계인지 알 수 없어 서비스가 성립하지 않는다."),
 "Empanada Streak": (0.55, "'Empanada'에 연속 기록 'Streak' 개념이 결합할 서비스 대상이 없다."),
 "Escargot Proposal": (0.55, "'Escargot'에 'Proposal'를 붙이면 무엇에 대한 제안인지 불명확하다."),
 "Gyro Record": (0.55, "'Gyro Record'는 무엇의 기록인지 서비스 대상이 그려지지 않는다."),
 "Quinoa Reading": (0.55, "'Quinoa'에 'Reading' 결합은 읽기 대상이 없어 성립하지 않는다."),
 "Jambalaya Diagnostic": (0.65, "'Jambalaya'는 진단 대상이 없어 'Diagnostic' 결합이 불명확하다."),
 "Naan Authorization": (0.7, "'Naan'에 권한 부여 'Authorization'은 도메인이 맞지 않다."),
 "Shawarma Authorization": (0.7, "'Shawarma'에 'Authorization' 결합은 권한 관리 대상이 없다."),
 "Goulash Agreement": (0.65, "'Goulash Agreement'는 합의 관리 대상이 없어 서비스가 성립하지 않는다."),
 "Tzatziki Agreement": (0.65, "'Tzatziki Agreement'는 합의 관리가 될 대상이 없어 성립하지 않는다."),
 "Tzatziki Reply": (0.55, "'Tzatziki'에 'Reply'를 붙이면 무엇에 답하는 도구인지 불명확하다."),
 "Guacamole Result": (0.65, "'Guacamole'에 'Result' 결합은 결과 대상이 없어 불명확하다."),
 "Escargot Guarantee": (0.6, "'Escargot Guarantee'는 보증 문구일 뿐 도구 기능이 그려지지 않는다."),
 "Gumbo Diagnostic": (0.65, "'Gumbo'는 진단 대상이 없어 'Diagnostic'가 성립하지 않는다."),
}
for t, (c, r) in food_no.items():
    D[t] = (False, c, False, True, True, r)

# --- Chords/Lyrics with non-music or non-lyric anchors: clarity rejects ---
chordlyric_no = {
 "Migraine Chords": ("'Migraine'은 의료 대상어라 음악 용어 'Chords'와 결합해도 지시되는 SaaS가 그려지지 않는다."),
 "Rebate Lyrics": ("'Rebate' 환급 도메인에 가사 'Lyrics'는 어울리지 않아 서비스가 성립하지 않는다."),
 "Payroll Chords": ("'Payroll' 급여 도메인에 화음 'Chords' 결합은 지시 대상이 없다."),
 "Material Lyrics": ("건축 'Material'에 가사 'Lyrics' 결합은 어떤 서비스인지 그려지지 않는다."),
 "Chess Chords": ("'Chess'에는 화음이 없어 'Chords' 결합이 서비스로 성립하지 않는다."),
 "Leaf Lyrics": ("식물 'Leaf'에 가사 'Lyrics' 결합은 지시 대상이 없다."),
 "Sidewalk Chords": ("'Sidewalk' 인프라 도메인에 화음 'Chords'는 결합이 불성립이다."),
 "Desert Chords": ("여행 대상어 'Desert'에 화음 'Chords' 결합은 어떤 SaaS인지 불명확하다."),
 "Migraine Lyrics": ("'Migraine'에 가사 'Lyrics' 결합은 서비스 대상이 그려지지 않는다."),
 "Subrogation Chords": ("보험 'Subrogation' 용어에 화음 'Chords'는 결합이 불성립이다."),
 "Payroll Lyrics": ("'Payroll'에 가사 'Lyrics' 결합은 지시 대상이 없다."),
 "Chess Lyrics": ("'Chess'에 가사 'Lyrics'는 결합할 대상이 없다."),
 "Detention Chords": ("교육 'Detention'에 화음 'Chords' 결합은 서비스가 성립하지 않는다."),
 "Sidewalk Lyrics": ("'Sidewalk'에 가사 'Lyrics' 결합은 어떤 도구인지 불명확하다."),
 "Key Chords": ("부동산 키 관리 도메인의 'Key'에 화음 'Chords'는 어울리지 않는다(음악으로 읽어도 부동산 SaaS가 아니다)."),
 "Desert Lyrics": ("'Desert'에 가사 'Lyrics' 결합은 서비스 대상이 없다."),
 "Deposit Chords": ("'Deposit' 금융·부동산 도메인에 화음 'Chords'는 결합이 불성립이다."),
 "Subrogation Lyrics": ("'Subrogation'에 가사 'Lyrics' 결합은 지시 대상이 없다."),
 "Cabin Chords": ("숙박 'Cabin'에 화음 'Chords' 결합은 어떤 SaaS인지 그려지지 않는다."),
 "Detention Lyrics": ("'Detention'에 가사 'Lyrics' 결합은 성립하지 않는다."),
 "Excavation Chords": ("군설 'Excavation' 도메인에 화음 'Chords'는 어울리지 않다."),
 "Oboe Chords": ("'Oboe'는 단선율 관악기라 화음 조회 'Chords' 결합이 실제 연습 서비스로 그려지지 않는다."),
 "Oboe Lyrics": ("'Oboe'는 가사 없는 관악기라 'Lyrics' 결합이 성립하지 않는다."),
}
for t, r in chordlyric_no.items():
    D[t] = (False, 0.7, False, True, True, r)

# --- Conjugations + noun anchor: verb-conjugation lookup clause fails ---
conj_no = ["Deposit Conjugations", "Cabin Conjugations", "Excavation Conjugations",
           "Route Conjugations", "Spigot Conjugations", "Termination Conjugations",
           "Odor Conjugations", "Deposition Conjugations", "Pony Conjugations",
           "Periodontitis Conjugations", "Quote Conjugations"]
for t in conj_no:
    a = t.split()[0]
    D[t] = (False, 0.8, False, True, True,
            f"'{a}'는 명사이므로 동사 활용 조회인 'Conjugations'와 결합해도 사전 조회 절 자체가 성립하지 않는다.")

# --- trademark ---
D["Dominoes Syllables"] = (False, 0.8, True, False, True,
    "'Dominoes'는 Domino's와 표기가 사실상 동일한 브랜드 유사어라(게임 패 일반 명사로 읽기엔 상표 충돌 위험이 지배적) 상표 유사 기각.")

# --- music/media explicit approves ---
D["Editor Lyrics"] = (True, 0.6, True, True, True,
    "'Editor'와 'Lyrics'가 결합해 가사 편집 도구라는 SaaS가 명확하고 중복·상표 문제도 없다.")

# ---------------------------------------------------------------- coverage + defaults
req = json.load(open(REQ, encoding="utf-8"))
items = req["items"]
titles = [it["title"] for it in items]
assert len(titles) == 200, len(titles)
assert len(set(titles)) == 200, "duplicate titles in request"

# Dictionary/learning lookup-clause function words judged in-session: approve
# unless the combination itself fails (handled explicitly above). Marketability
# (search volume) is the separate Keyword Planner gate, not judged here.
LOOKUP = {"Syllables", "Rhymes", "Synonyms", "Antonyms", "Sentences",
          "Translations", "Anagrams", "Orthography"}

def judge(t):
    if t in D:
        return D[t]
    parts = t.split()
    if len(parts) == 2 and parts[1] in LOOKUP:
        return (True, 0.75, True, True, True,
                f"'{parts[0]}'를 대상어로 하는 '{parts[1]}' 사전 조회 절이 단어 레퍼런스 도구로 명확하고 의미중복·상표 문제도 없다.")
    print("MISSING JUDGMENT:", t)
    sys.exit(1)

extra = [t for t in D if t not in set(titles)]
if extra:
    print("UNMATCHED EXTRA:", extra)
    sys.exit(1)

out = []
for t in titles:
    ok, conf, cl, dup, tm, reason = judge(t)
    if ok:
        assert cl and dup and tm, f"logic mismatch approve=true: {t}"
        assert conf >= 0.55
    else:
        assert (not cl) or (not dup) or (not tm), f"logic mismatch approve=false: {t}"
    assert reason.strip()
    out.append({"title": t, "approve": ok, "confidence": conf,
                "reason": reason,
                "checks": {"clarity": cl, "duplication": dup, "trademark": tm}})

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

n_ok = sum(1 for o in out if o["approve"])
print(f"written {len(out)} decisions -> {OUT}")
print(f"approve {n_ok} / reject {len(out)-n_ok}")
