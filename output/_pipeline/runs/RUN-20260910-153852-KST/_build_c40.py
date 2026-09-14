# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk39_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Editor App": (0.55, "문서·이미지 편집 앱(실재)"),
 "Editor Tips": (0.55, "Editor App 승인 선례의 Tips 평행"),
 "Locksmith App": (0.55, "자물쇠·도어 수리 서비스 앱(실재)"),
 "Locksmith Tips": (0.55, "Locksmith App 승인 선례의 Tips 평행"),
 "Wax App": (0.55, "왁싱 예약·왁스 제품 관리 앱(실재)"),
 "Wax Tips": (0.55, "Wax App 승인 선례의 Tips 평행"),
 "Viola App": (0.55, "비올라 학습·연주 보조 앱(Violin App 평행)"),
 "Pump App": (0.55, "펌프·유축 관리 앱(실재)"),
 "Campsite App": (0.55, "캠핑장 검색·예약 앱(실재)"),
 "Compensation App": (0.55, "보상·급여 관리 앱(실재)"),
 "Contact Tips": (0.55, "Contact App 승인 선례의 Tips 평행"),
 "Drain Tips": (0.55, "Drain App 승인 선례의 Tips 평행"),
 "Symptom Tips": (0.55, "Symptom App 승인 선례의 Tips 평행"),
 "Stargazing Tips": (0.55, "Stargazing App 승인 선례의 Tips 평행"),
 "Migraine Video": (0.55, "편두통 관리 영상 가이드(Hypertension Video 평행)"),
 "Copyright Calendar": (0.55, "저작권 기한 캘린더(Calendar 절차 명사 선례 평행)"),
}

R_DUP = {
 "Portfolio Advice": "이번 배치 승인 Portfolio Tips와 동일 기능 의미 중복",
 "Cruise Advice": "이번 배치 승인 Cruise Tips와 동일 기능 의미 중복",
 "Debit Advice": "이번 배치 승인 Debit Tips와 동일 기능 의미 중복",
 "Drain Advice": "이번 배치 승인 Drain Tips와 동일 기능 의미 중복",
 "Stargazing Advice": "이번 배치 승인 Stargazing Tips와 동일 기능 의미 중복",
 "Contact Advice": "이번 배치 승인 Contact Tips와 동일 기능 의미 중복",
}

R = {
 "Headlight Mode": "기능 토글로 읽혀 제품 불분명", "Brunch Spec": "사양 참조로 제품 불분명",
 "Shelter Quantity": "수량 대상 불분명", "Cleaning Login": "제품 불분명",
 "Nap Analysis": "분석 대상 불분명", "Shampoo Coach": "코칭 대상 불분명",
 "Refrigeration Habit": "결합 불성립", "Trademark Beacon": "비컨 지칭으로 제품 불분명",
 "Patent Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)", "Migraine Recipe": "결합 불성립",
 "Insomnia Newsletter": "결합 불성립", "Skydiving Checkin": "결합 불성립",
 "Acne Size": "결합 불성립(속성 지칭)", "Snowboarding Range": "결합 불성립",
 "Eczema Limit": "결합 불성립", "Ziplining Time": "결합 불성립",
 "Psoriasis Speed": "결합 불성립", "Sledding Width": "결합 불성립",
 "Vertigo Temperature": "결합 불성립", "Diving Voltage": "결합 불성립",
 "Arthritis Wattage": "결합 불성립", "Sailing Compatibility": "상태 명사로 제품명 부자연",
 "Menopause Capacity": "상태 명사로 제품명 부자연", "Rafting Humidity": "결합 불성립",
 "Pregnancy Episode": "결합 불성립", "Climbing Sensor": "결합 불성립",
 "Fertility Reception": "리셉션·수신 중의로 불분명", "Biking Matrix": "행렬·매트릭스 중의로 불분명",
 "Thyroid Evaluation": "평가 대상 불분명", "Golf Benefit": "혜택 지칭으로 제품 불분명",
 "Cholesterol Requirement": "요건 지칭으로 제품 불분명", "Fishing Hazard": "결합 불성립",
 "Hypertension Guarantor": "보증인 명사 결합 불성립", "Camping Handbook": "terrain 대상 결합 불성립",
 "Anemia Timetable": "terrain 대상 결합 불성립", "Glamping Retreat": "terrain 대상 결합 불성립",
 "Heartburn Tournament": "terrain 대상 결합 불성립", "Constipation Advice": "선례 기각(App 기각) 계열",
 "Testimony Workbook": "워크북 대상 불분명", "Birdwatching Spec": "사양 참조로 제품 불분명",
 "Concussion Quantity": "선례 기각(App 기각) 계열", "Canyon Analysis": "선례 기각(App 기각) 계열",
 "Sprain Coach": "선례 기각(App 기각) 계열", "Geyser Habit": "선례 기각(App 기각) 계열",
 "Fracture Tracker": "선례 기각(App 기각) 계열", "Fjord Flow": "선례 기각(App 기각) 계열",
 "Insulin Hub": "기능 토글로 읽혀 제품 불분명", "Savanna Desk": "선례 기각(App 기각) 계열",
 "Tundra Radar": "선례 기각(App 기각) 계열", "Prairie Relay": "선례 기각(App 기각) 계열",
 "Marsh Vault": "선례 기각(App 기각) 계열", "Cove Compass": "선례 기각(App 기각) 계열",
 "Cliff Beacon": "선례 기각(App 기각) 계열", "Cavern Forge": "선례 기각(App 기각) 계열",
 "Oasis Cascade": "선례 기각(App 기각) 계열", "Dune Bridge": "선례 기각(App 기각) 계열",
 "Whale Signal": "선례 기각(App 기각) 계열", "Dolphin Watch": "선례 기각(App 기각) 계열",
 "Penguin Scope": "선례 기각(App 기각) 계열", "Flamingo Loop": "선례 기각(App 기각) 계열",
 "Turtle Grid": "선례 기각(App 기각) 계열", "Moose Wave": "선례 기각(App 기각) 계열",
 "Bison Path": "선례 기각(App 기각) 계열", "Reindeer Point": "선례 기각(App 기각) 계열",
 "Violin Workbook": "워크북 대상 불분명",
 "Expense Spec": "사양 참조로 제품 불분명", "Clause Quantity": "수량 대상 불분명",
 "Listing Analysis": "분석 대상 불분명", "Claim Coach": "코칭 대상 불분명",
 "Roster Habit": "결합 불성립", "Title App": "제목·소유권·직함 중의로 대상 불분명",
 "Actuary Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Jobsite Workbook": "워크북 대상 불분명",
 "Markdown Mode": "기능 토글로 읽혀 제품 불분명", "Itinerary Spec": "사양 참조로 제품 불분명",
 "Scholarship Quantity": "수량 대상 불분명", "Supplier Login": "제품 불분명",
 "Fertilizer Analysis": "분석 대상 불분명", "Outreach Habit": "결합 불성립",
 "Lawyer Deposit": "예금·보증금 결합 불성립", "Attorney Frequency": "결합 불성립",
 "Court Workbook": "선례 기각(App 기각) 계열",
 "Shipper Mode": "기능 토글로 읽혀 제품 불분명", "Counteroffer Spec": "사양 참조로 제품 불분명",
 "Peril Quantity": "선례 기각(App 기각) 계열", "Deduction Login": "제품 불분명",
 "Plumbing Analysis": "분석 대상 불분명", "Major Coach": "선례 기각(App 기각) 계열",
 "Judge Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Jury Locator": "탐색 기능 지칭으로 제품 불분명(Locator 기각 라인)",
 "Lawsuit Rate": "요율·비율 지칭으로 제품 불분명", "Divorce Entry": "입장·기입 중의로 불분명",
 "Custody Serial": "연재물·일련번호 중의로 불분명", "Immigration Widget": "위젯 지칭으로 제품 불분명",
 "Testament Authorization": "권한부여 지칭으로 제품 불분명", "Notary Predictor": "예측 대상 불분명",
 "Mediation Wattage": "결합 불성립", "Guardianship Handbook": "terrain 대상 결합 불성립",
 "Portfolio Workbook": "워크북 대상 불분명", "Headlight Spec": "사양 참조로 제품 불분명",
 "Brunch Quantity": "수량 대상 불분명", "Shelter Login": "제품 불분명",
 "Cleaning Analysis": "분석 대상 불분명", "Nap Coach": "코칭 대상 불분명",
 "Shampoo Habit": "결합 불성립", "Trademark Forge": "단조·조작 중의로 불분명",
 "Patent Console": "콘솔 지칭으로 제품 불분명", "Copyright Directory": "디렉터리 지칭으로 제품 불분명",
 "Insomnia Inventory": "결합 불성립", "Skydiving Size": "결합 불성립(속성 지칭)",
 "Acne Length": "결합 불성립(속성 지칭)", "Snowboarding Limit": "결합 불성립",
 "Eczema Type": "결합 불성립(분류 대상 부자연)", "Ziplining Speed": "결합 불성립",
 "Psoriasis Depth": "결합 불성립", "Sledding Temperature": "결합 불성립",
 "Vertigo Pressure": "결합 불성립", "Diving Wattage": "결합 불성립",
 "Arthritis Brightness": "결합 불성립", "Sailing Capacity": "상태 명사로 제품명 부자연",
 "Menopause Usage": "사용 지칭으로 제품 불분명", "Rafting Episode": "결합 불성립",
 "Pregnancy Cycle": "주기 지칭으로 제품 불분명", "Climbing Reception": "리셉션·수신 중의로 불분명",
 "Fertility Followup": "후속 지칭으로 제품 불분명", "Biking Evaluation": "평가 대상 불분명",
 "Thyroid Questionnaire": "설문 대상 불분명", "Golf Requirement": "요건 지칭으로 제품 불분명",
 "Cholesterol Depreciation": "결합 불성립", "Fishing Guarantor": "보증인 명사 결합 불성립",
 "Hypertension Tuner": "튜너 기능 지칭으로 제품 불분명", "Camping Timetable": "terrain 대상 결합 불성립",
 "Anemia Opinion": "소견 대상 불분명", "Glamping Tournament": "terrain 대상 결합 불성립",
 "Heartburn Flyer": "terrain 대상 결합 불성립", "Constipation Workbook": "선례 기각(App 기각) 계열",
 "Testimony Mode": "기능 토글로 읽혀 제품 불분명", "Birdwatching Quantity": "수량 대상 불분명",
 "Concussion Login": "선례 기각(App 기각) 계열", "Canyon Coach": "선례 기각(App 기각) 계열",
 "Sprain Habit": "선례 기각(App 기각) 계열", "Geyser Tracker": "선례 기각(App 기각) 계열",
 "Fracture Flow": "선례 기각(App 기각) 계열", "Fjord Hub": "선례 기각(App 기각) 계열",
 "Insulin Desk": "제품 불분명", "Savanna Radar": "선례 기각(App 기각) 계열",
 "Tundra Relay": "선례 기각(App 기각) 계열", "Prairie Vault": "선례 기각(App 기각) 계열",
 "Marsh Compass": "선례 기각(App 기각) 계열", "Cove Beacon": "선례 기각(App 기각) 계열",
 "Cliff Forge": "선례 기각(App 기각) 계열", "Cavern Cascade": "선례 기각(App 기각) 계열",
 "Oasis Bridge": "선례 기각(App 기각) 계열", "Dune Signal": "선례 기각(App 기각) 계열",
 "Whale Watch": "선례 기각(App 기각) 계열", "Dolphin Scope": "선례 기각(App 기각) 계열",
 "Penguin Loop": "선례 기각(App 기각) 계열", "Flamingo Grid": "선례 기각(App 기각) 계열",
 "Turtle Wave": "선례 기각(App 기각) 계열", "Moose Path": "선례 기각(App 기각) 계열",
 "Bison Point": "선례 기각(App 기각) 계열", "Reindeer Map": "선례 기각(App 기각) 계열",
 "Cruise Workbook": "워크북 대상 불분명",
 "Violin Mode": "기능 토글로 읽혀 제품 불분명", "Expense Quantity": "수량 대상 불분명",
 "Clause Login": "제품 불분명", "Listing Coach": "코칭 대상 불분명",
 "Claim Habit": "결합 불성립", "Title Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Actuary Advice": "선례 기각(App 기각) 계열", "Jobsite Mode": "기능 토글로 읽혀 제품 불분명",
 "Markdown Spec": "사양 참조로 제품 불분명", "Itinerary Quantity": "수량 대상 불분명",
 "Scholarship Login": "제품 불분명", "Supplier Analysis": "분석 대상 불분명",
 "Fertilizer Coach": "코칭 대상 불분명", "Lawyer Certification": "인증 대상 불분명",
 "Attorney Compatibility": "상태 명사로 제품명 부자연",
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
out = base + r"\_dec_c40.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
