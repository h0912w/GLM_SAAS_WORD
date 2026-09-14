# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk41_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Timeline App": (0.55, "타임라인 작성·관리 앱(실재)"),
 "Timeline Tips": (0.55, "Timeline App 승인 선례의 Tips 평행"),
 "Termination App": (0.55, "고용·계약 해지 절차 관리 앱(실재)"),
 "Termination Tips": (0.55, "Termination App 승인 선례의 Tips 평행"),
 "Signage App": (0.55, "디지털 사이니지 콘텐츠 관리 앱(실재)"),
 "Signage Tips": (0.55, "Signage App 승인 선례의 Tips 평행"),
 "Retouching App": (0.55, "사진 보정 앱(실재)"),
 "Quote App": (0.55, "견적서 작성 앱(실재)"),
 "Excavation Tips": (0.55, "Excavation App 승인 선례의 Tips 평행"),
 "Glamping Tips": (0.55, "Glamping App 승인 선례의 Tips 평행"),
 "Trademark Watch": (0.55, "상표 출원 감시 서비스(실재, Trademark Tracker 평행)"),
}

R_DUP = {
 "Pump Advice": "이번 배치 승인 Pump Tips와 동일 기능 의미 중복",
 "Campsite Advice": "이번 배치 승인 Campsite Tips와 동일 기능 의미 중복",
 "Excavation Advice": "이번 배치 승인 Excavation Tips와 동일 기능 의미 중복",
 "Glamping Advice": "이번 배치 승인 Glamping Tips와 동일 기능 의미 중복",
}

R = {
 "Reindeer Base": "선례 기각(App 기각) 계열(Base 기각 라인)", "Utility Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Wax Workbook": "워크북 대상 불분명", "Drain Mode": "기능 토글로 읽혀 제품 불분명",
 "Cruise Spec": "사양 참조로 제품 불분명", "Violin Quantity": "수량 대상 불분명",
 "Expense Analysis": "분석 대상 불분명", "Clause Coach": "코칭 대상 불분명",
 "Retainer Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Title Workbook": "선례 기각(App 기각) 계열",
 "Actuary Mode": "선례 기각(App 기각) 계열", "Jobsite Quantity": "수량 대상 불분명",
 "Markdown Login": "제품 불분명", "Itinerary Analysis": "분석 대상 불분명",
 "Scholarship Coach": "코칭 대상 불분명", "Supplier Habit": "결합 불성립",
 "Lawyer Correction": "수정 지칭으로 제품 불분명(Notary Correction 기각 평행)", "Attorney Usage": "사용 지칭으로 제품 불분명",
 "Shine App": "자기관리 앱 상표(Shine) 중의로 불분명", "Nozzle Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Viola Workbook": "워크북 대상 불분명", "Symptom Mode": "기능 토글로 읽혀 제품 불분명",
 "Debit Spec": "사양 참조로 제품 불분명", "Court Quantity": "선례 기각(App 기각) 계열",
 "Shipper Login": "제품 불분명", "Counteroffer Analysis": "분석 대상 불분명",
 "Peril Coach": "선례 기각(App 기각) 계열", "Deduction Habit": "결합 불성립",
 "Judge Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Jury Counter": "계수기·조리대 중의로 불분명",
 "Lawsuit Draft": "초안 지칭으로 제품 불분명", "Divorce Unit": "단위 지칭으로 제품 불분명",
 "Custody Marker": "마커 지칭으로 제품 불분명", "Immigration Calculator": "계산 기능 지칭으로 제품 불분명",
 "Testament Rating": "평점 지칭으로 제품 불분명", "Notary Recipe": "결합 불성립",
 "Mediation Compatibility": "상태 명사로 제품명 부자연", "Guardianship Gift": "결합 불성립",
 "Detention Advice": "선례 기각(App 기각) 계열", "Editor Mode": "기능 토글로 읽혀 제품 불분명",
 "Contact Spec": "사양 참조로 제품 불분명", "Portfolio Quantity": "수량 대상 불분명",
 "Headlight Analysis": "분석 대상 불분명", "Brunch Coach": "코칭 대상 불분명",
 "Shelter Habit": "결합 불성립", "Trademark Signal": "선례 기각(App 기각) 계열(Signal 기각 라인)",
 "Patent Route": "선례 기각(App 기각) 계열(Route 기각 라인)", "Copyright Office": "공공기관명(저작권청) 중의로 불분명",
 "Migraine Expense": "결합 불성립", "Insomnia Checkin": "결합 불성립",
 "Skydiving Distance": "결합 불성립", "Acne Range": "결합 불성립",
 "Snowboarding Time": "결합 불성립", "Eczema Speed": "결합 불성립",
 "Ziplining Width": "결합 불성립", "Psoriasis Temperature": "결합 불성립",
 "Sledding Voltage": "결합 불성립", "Vertigo Wattage": "결합 불성립",
 "Diving Compatibility": "상태 명사로 제품명 부자연", "Arthritis Capacity": "상태 명사로 제품명 부자연",
 "Sailing Humidity": "결합 불성립", "Menopause Episode": "결합 불성립",
 "Rafting Sensor": "결합 불성립", "Pregnancy Reception": "리셉션·수신 중의로 불분명",
 "Climbing Matrix": "행렬·매트릭스 중의로 불분명", "Fertility Evaluation": "평가 대상 불분명",
 "Biking Benefit": "혜택 지칭으로 제품 불분명", "Thyroid Requirement": "요건 지칭으로 제품 불분명",
 "Golf Hazard": "결합 불성립", "Cholesterol Guarantor": "보증인 명사 결합 불성립",
 "Fishing Handbook": "terrain 대상 결합 불성립", "Hypertension Timetable": "terrain 대상 결합 불성립",
 "Camping Retreat": "terrain 대상 결합 불성립", "Anemia Tournament": "terrain 대상 결합 불성립",
 "Heartburn Advice": "선례 기각(App 기각) 계열", "Compensation Workbook": "워크북 대상 불분명",
 "Locksmith Mode": "기능 토글로 읽혀 제품 불분명", "Stargazing Spec": "사양 참조로 제품 불분명",
 "Constipation Quantity": "선례 기각(App 기각) 계열", "Testimony Login": "제품 불분명",
 "Birdwatching Coach": "코칭 대상 불분명", "Concussion Habit": "선례 기각(App 기각) 계열",
 "Canyon Flow": "선례 기각(App 기각) 계열", "Sprain Hub": "선례 기각(App 기각) 계열",
 "Geyser Desk": "선례 기각(App 기각) 계열", "Fracture Radar": "선례 기각(App 기각) 계열",
 "Fjord Relay": "선례 기각(App 기각) 계열", "Insulin Vault": "선례 기각(App 기각) 계열",
 "Savanna Compass": "선례 기각(App 기각) 계열", "Tundra Beacon": "선례 기각(App 기각) 계열",
 "Prairie Forge": "선례 기각(App 기각) 계열", "Marsh Cascade": "선례 기각(App 기각) 계열",
 "Cove Bridge": "선례 기각(App 기각) 계열", "Cliff Signal": "선례 기각(App 기각) 계열",
 "Cavern Watch": "선례 기각(App 기각) 계열", "Oasis Scope": "선례 기각(App 기각) 계열",
 "Dune Loop": "선례 기각(App 기각) 계열", "Whale Grid": "선례 기각(App 기각) 계열",
 "Dolphin Wave": "선례 기각(App 기각) 계열", "Penguin Path": "선례 기각(App 기각) 계열",
 "Flamingo Point": "선례 기각(App 기각) 계열", "Turtle Map": "선례 기각(App 기각) 계열",
 "Moose Frame": "선례 기각(App 기각) 계열", "Bison Base": "선례 기각(App 기각) 계열",
 "Reindeer Core": "선례 기각(App 기각) 계열(Core 기각 라인)", "Tile App": "분실물 추적기 상표(Tile) 중의로 불분명",
 "Utility Advice": "선례 기각(App 기각) 계열",
 "Pump Workbook": "워크북 대상 불분명", "Wax Mode": "기능 토글로 읽혀 제품 불분명",
 "Drain Spec": "사양 참조로 제품 불분명", "Cruise Quantity": "수량 대상 불분명",
 "Violin Login": "제품 불분명", "Expense Coach": "코칭 대상 불분명",
 "Clause Habit": "결합 불성립", "Retainer Advice": "선례 기각(App 기각) 계열",
 "Title Mode": "선례 기각(App 기각) 계열", "Actuary Spec": "선례 기각(App 기각) 계열",
 "Jobsite Login": "제품 불분명", "Markdown Analysis": "분석 대상 불분명",
 "Itinerary Coach": "코칭 대상 불분명", "Scholarship Habit": "결합 불성립",
 "Lawyer Revision": "수정 지칭으로 제품 불분명(Notary Revision 기각 평행)", "Attorney Condition": "상태 명사로 제품명 부자연",
 "Shine Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가", "Nozzle Advice": "선례 기각(App 기각) 계열",
 "Campsite Workbook": "워크북 대상 불분명", "Viola Mode": "기능 토글로 읽혀 제품 불분명",
 "Symptom Spec": "사양 참조로 제품 불분명", "Debit Quantity": "수량 대상 불분명",
 "Court Login": "선례 기각(App 기각) 계열", "Shipper Analysis": "분석 대상 불분명",
 "Counteroffer Coach": "코칭 대상 불분명", "Peril Habit": "선례 기각(App 기각) 계열",
 "Judge Terminal": "단말·터미널 중의로 불분명", "Jury Booth": "부스 지칭으로 제품 불분명",
 "Lawsuit Summary": "요약 대상 불분명", "Divorce Plan": "계획 대상 불분명(Planner 기각 라인)",
 "Custody Balance": "잔액·균형 중의로 불분명", "Immigration Converter": "변환 기능 지칭으로 제품 불분명",
 "Testament Agreement": "합의 지칭으로 제품 불분명", "Notary Video": "terrain 대상 결합 불성립",
 "Mediation Capacity": "상태 명사로 제품명 부자연", "Guardianship Retreat": "terrain 대상 결합 불성립",
 "Detention Workbook": "선례 기각(App 기각) 계열", "Editor Spec": "사양 참조로 제품 불분명",
 "Contact Quantity": "수량 대상 불분명", "Portfolio Login": "제품 불분명",
 "Headlight Coach": "코칭 대상 불분명", "Brunch Habit": "결합 불성립",
 "Patent Rail": "레일 지칭으로 제품 불분명",
 "Copyright Counter": "계수기·조리대 중의로 불분명", "Migraine Newsletter": "결합 불성립",
 "Insomnia Size": "결합 불성립(속성 지칭)", "Skydiving Range": "결합 불성립",
 "Acne Limit": "결합 불성립", "Snowboarding Speed": "결합 불성립",
 "Eczema Depth": "결합 불성립", "Ziplining Temperature": "결합 불성립",
 "Psoriasis Pressure": "결합 불성립", "Sledding Wattage": "결합 불성립",
 "Vertigo Brightness": "결합 불성립", "Diving Capacity": "상태 명사로 제품명 부자연",
 "Arthritis Usage": "사용 지칭으로 제품 불분명", "Sailing Episode": "결합 불성립",
 "Menopause Cycle": "주기 지칭으로 제품 불분명", "Rafting Reception": "리셉션·수신 중의로 불분명",
 "Pregnancy Followup": "후속 지칭으로 제품 불분명", "Climbing Evaluation": "평가 대상 불분명",
 "Fertility Questionnaire": "설문 대상 불분명", "Biking Requirement": "요건 지칭으로 제품 불분명",
 "Thyroid Depreciation": "결합 불성립", "Golf Guarantor": "보증인 명사 결합 불성립",
 "Cholesterol Tuner": "튜너 기능 지칭으로 제품 불분명", "Fishing Timetable": "terrain 대상 결합 불성립",
 "Hypertension Opinion": "소견 대상 불분명", "Camping Tournament": "terrain 대상 결합 불성립",
 "Anemia Flyer": "terrain 대상 결합 불성립", "Damages App": "손해·손상 중의로 용도 불분명",
 "Heartburn Workbook": "선례 기각(App 기각) 계열", "Compensation Mode": "기능 토글로 읽혀 제품 불분명",
 "Locksmith Spec": "사양 참조로 제품 불분명", "Stargazing Quantity": "수량 대상 불분명",
 "Constipation Login": "선례 기각(App 기각) 계열", "Testimony Analysis": "분석 대상 불분명",
 "Birdwatching Habit": "결합 불성립",
}

lines = []
na = nr = 0
for t in titles:
    if t in A:
        conf, reason = A[t]
        lines.append(f"{t}\tA\tT\tT\tT\t{conf}\t{reason}")
        na += 1
    elif t in R_DUP:
        lines.append(f"{t}\tR\tT\tF\tT\t0.65\t{R_DUP[t]}")
        nr += 1
    elif t in R:
        lines.append(f"{t}\tR\tF\tT\tT\t0.6\t{R[t]}")
        nr += 1
    else:
        raise SystemExit(f"미판정: {t}")
out = base + r"\_dec_c42.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
