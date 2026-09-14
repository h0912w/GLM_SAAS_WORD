# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk37_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Markdown App": (0.55, "마크다운 문서 편집 앱(실재)"),
 "Markdown Tips": (0.55, "Markdown App 승인 선례의 Tips 평행"),
 "Shipper App": (0.55, "배송 발주·화주 관리 앱(실재)"),
 "Shipper Tips": (0.55, "Shipper App 승인 선례의 Tips 평행"),
 "Testimony App": (0.55, "증언 기록·정리 앱(Transcript App 평행)"),
 "Violin App": (0.55, "바이올린 학습·연주 보조 앱(실재)"),
 "Jobsite App": (0.55, "건설 현장 관리 앱(실재)"),
 "Portfolio App": (0.55, "포트폴리오 관리 앱(실재)"),
 "Expense Tips": (0.55, "Expense App 승인 선례의 Tips 평행"),
 "Itinerary Tips": (0.55, "Itinerary App 승인 선례의 Tips 평행"),
 "Counteroffer Tips": (0.55, "Counteroffer App 승인 선례의 Tips 평행"),
 "Headlight Tips": (0.55, "Headlight App 승인 선례의 Tips 평행"),
 "Birdwatching Tips": (0.55, "Birdwatching App 승인 선례의 Tips 평행"),
 "Insomnia Diary": (0.55, "불면 증상 기록 일지(Vertigo Diary 평행)"),
 "Immigration Kit": (0.55, "이민 서류 준비 키트(Kit 절차 명사 선례 평행)"),
 "Divorce Petition": (0.55, "이혼 소송 신청서 절차 관리(Petition 절차 명사 선례 평행)"),
}

R_DUP = {
 "Clause Advice": "이번 배치 승인 Clause Tips와 동일 기능 의미 중복",
 "Scholarship Advice": "이번 배치 승인 Scholarship Tips와 동일 기능 의미 중복",
 "Birdwatching Advice": "이번 배치 승인 Birdwatching Tips와 동일 기능 의미 중복",
 "Expense Advice": "이번 배치 승인 Expense Tips와 동일 기능 의미 중복",
 "Itinerary Advice": "이번 배치 승인 Itinerary Tips와 동일 기능 의미 중복",
 "Counteroffer Advice": "이번 배치 승인 Counteroffer Tips와 동일 기능 의미 중복",
 "Headlight Advice": "이번 배치 승인 Headlight Tips와 동일 기능 의미 중복",
 "Brunch Advice": "이번 배치 승인 Brunch Tips와 동일 기능 의미 중복",
}

R = {
 "Cholesterol Evaluation": "평가 대상 불분명", "Fishing Benefit": "혜택 지칭으로 제품 불분명",
 "Hypertension Requirement": "요건 지칭으로 제품 불분명", "Camping Hazard": "결합 불성립",
 "Anemia Guarantor": "보증인 명사 결합 불성립", "Glamping Handbook": "terrain 대상 결합 불성립",
 "Heartburn Timetable": "terrain 대상 결합 불성립", "Stargazing Retreat": "terrain 대상 결합 불성립",
 "Constipation Tournament": "terrain 대상 결합 불성립", "Concussion Advice": "선례 기각(App 기각) 계열",
 "Canyon Mode": "선례 기각(App 기각) 계열", "Sprain Spec": "선례 기각(App 기각) 계열",
 "Geyser Quantity": "선례 기각(App 기각) 계열", "Fracture Login": "선례 기각(App 기각) 계열",
 "Fjord Analysis": "선례 기각(App 기각) 계열", "Insulin Coach": "코칭 대상 불분명",
 "Savanna Habit": "선례 기각(App 기각) 계열", "Tundra Tracker": "선례 기각(App 기각) 계열",
 "Prairie Flow": "선례 기각(App 기각) 계열", "Marsh Hub": "선례 기각(App 기각) 계열",
 "Cove Desk": "선례 기각(App 기각) 계열", "Cliff Radar": "선례 기각(App 기각) 계열",
 "Cavern Relay": "선례 기각(App 기각) 계열", "Oasis Vault": "선례 기각(App 기각) 계열",
 "Dune Compass": "선례 기각(App 기각) 계열", "Whale Beacon": "선례 기각(App 기각) 계열",
 "Dolphin Forge": "선례 기각(App 기각) 계열", "Penguin Cascade": "선례 기각(App 기각) 계열",
 "Flamingo Bridge": "선례 기각(App 기각) 계열", "Turtle Signal": "선례 기각(App 기각) 계열",
 "Moose Watch": "선례 기각(App 기각) 계열", "Bison Scope": "선례 기각(App 기각) 계열",
 "Reindeer Loop": "선례 기각(App 기각) 계열", "Listing Mode": "기능 토글로 읽혀 제품 불분명",
 "Claim Spec": "사양 참조로 제품 불분명", "Roster Quantity": "수량 대상 불분명",
 "Subcontractor Login": "제품 불분명", "Return Analysis": "분석 대상 불분명",
 "Checkin Coach": "코칭 대상 불분명", "Transcript Habit": "결합 불성립",
 "Supplier Workbook": "워크북 대상 불분명", "Fertilizer Mode": "기능 토글로 읽혀 제품 불분명",
 "Outreach Quantity": "수량 대상 불분명", "Segment Analysis": "선례 기각(App 상표 기각) 계열",
 "Rights Coach": "선례 기각(App 기각) 계열", "Cargo Habit": "결합 불성립",
 "Lawyer Invoice": "청구서 결합 불성립(Notary Invoice 기각 평행)", "Attorney Load": "결합 불성립",
 "Court Flyer": "terrain 대상 결합 불성립", "Peril Advice": "선례 기각(App 기각) 계열",
 "Deduction Workbook": "워크북 대상 불분명", "Plumbing Mode": "기능 토글로 읽혀 제품 불분명",
 "Major Spec": "선례 기각(App 기각) 계열", "Podcast Login": "제품 불분명",
 "Channel Analysis": "분석 대상 불분명", "Skillset Coach": "코칭 대상 불분명",
 "Livestream Habit": "결합 불성립", "Judge Base": "선례 기각(App 기각) 계열(Base 기각 라인)",
 "Jury Journal": "일지·잡지 중의로 불분명", "Lawsuit View": "조회 기능 지칭으로 제품 불분명",
 "Divorce Advisory": "자문 대상 불분명", "Custody Category": "결합 불성립(분류 대상 부자연)",
 "Testament Duration": "결합 불성립", "Notary Revision": "결합 불성립",
 "Mediation Temperature": "결합 불성립", "Guardianship Hazard": "결합 불성립",
 "Brunch Workbook": "워크북 대상 불분명", "Shelter Mode": "기능 토글로 읽혀 제품 불분명",
 "Cleaning Mode": "기능 토글로 읽혀 제품 불분명", "Nap Spec": "사양 참조로 제품 불분명",
 "Shampoo Quantity": "수량 대상 불분명", "Refrigeration Login": "제품 불분명",
 "Chiller Analysis": "분석 대상 불분명", "Transponder Coach": "코칭 대상 불분명",
 "Cleaning Spec": "사양 참조로 제품 불분명", "Nap Quantity": "수량 대상 불분명",
 "Shampoo Login": "제품 불분명", "Refrigeration Analysis": "분석 대상 불분명",
 "Chiller Coach": "코칭 대상 불분명", "Transponder Habit": "결합 불성립",
 "Thumbnail Habit": "결합 불성립", "Trademark Relay": "릴레이 지칭으로 제품 불분명",
 "Patent Terminal": "터미널 지칭으로 제품 불분명(Terminal 기각 라인)", "Copyright Playbook": "플레이북 대상 불분명",
 "Migraine Predictor": "예측 대상 불분명", "Skydiving Inventory": "결합 불성립",
 "Acne Claim": "결합 불성립", "Snowboarding Length": "결합 불성립(속성 지칭)",
 "Eczema Weight": "결합 불성립(속성 지칭)", "Ziplining Limit": "결합 불성립",
 "Psoriasis Type": "결합 불성립(분류 대상 부자연)", "Sledding Speed": "결합 불성립",
 "Vertigo Depth": "결합 불성립", "Diving Temperature": "결합 불성립",
 "Arthritis Pressure": "결합 불성립", "Sailing Wattage": "결합 불성립",
 "Menopause Brightness": "결합 불성립", "Rafting Capacity": "상태 명사로 제품명 부자연",
 "Pregnancy Usage": "사용 지칭으로 제품 불분명", "Climbing Episode": "결합 불성립",
 "Fertility Cycle": "주기 지칭으로 제품 불분명", "Biking Reception": "리셉션·수신 중의로 불분명",
 "Thyroid Followup": "후속 지칭으로 제품 불분명", "Golf Evaluation": "평가 대상 불분명",
 "Cholesterol Questionnaire": "설문 대상 불분명", "Fishing Requirement": "요건 지칭으로 제품 불분명",
 "Hypertension Depreciation": "결합 불성립", "Camping Guarantor": "보증인 명사 결합 불성립",
 "Anemia Tuner": "튜너 기능 지칭으로 제품 불분명", "Glamping Timetable": "terrain 대상 결합 불성립",
 "Heartburn Opinion": "소견 대상 불분명", "Stargazing Tournament": "terrain 대상 결합 불성립",
 "Constipation Flyer": "terrain 대상 결합 불성립", "Concussion Workbook": "워크북 대상 불분명",
 "Shelter Workbook": "워크북 대상 불분명",
 "Canyon Spec": "선례 기각(App 기각) 계열", "Sprain Quantity": "선례 기각(App 기각) 계열",
 "Geyser Login": "선례 기각(App 기각) 계열", "Fracture Analysis": "선례 기각(App 기각) 계열",
 "Fjord Coach": "선례 기각(App 기각) 계열", "Insulin Habit": "결합 불성립",
 "Savanna Tracker": "선례 기각(App 기각) 계열", "Tundra Flow": "선례 기각(App 기각) 계열",
 "Prairie Hub": "선례 기각(App 기각) 계열", "Marsh Desk": "선례 기각(App 기각) 계열",
 "Cove Radar": "선례 기각(App 기각) 계열", "Cliff Relay": "선례 기각(App 기각) 계열",
 "Cavern Vault": "선례 기각(App 기각) 계열", "Oasis Compass": "선례 기각(App 기각) 계열",
 "Dune Beacon": "선례 기각(App 기각) 계열", "Whale Forge": "선례 기각(App 기각) 계열",
 "Dolphin Cascade": "선례 기각(App 기각) 계열", "Penguin Bridge": "선례 기각(App 기각) 계열",
 "Flamingo Signal": "선례 기각(App 기각) 계열", "Turtle Watch": "선례 기각(App 기각) 계열",
 "Moose Scope": "선례 기각(App 기각) 계열", "Bison Loop": "선례 기각(App 기각) 계열",
 "Reindeer Grid": "선례 기각(App 기각) 계열", "Clause Workbook": "워크북 대상 불분명",
 "Listing Spec": "사양 참조로 제품 불분명", "Claim Quantity": "수량 대상 불분명",
 "Roster Login": "제품 불분명", "Subcontractor Analysis": "분석 대상 불분명",
 "Return Coach": "코칭 대상 불분명", "Checkin Habit": "결합 불성립",
 "Scholarship Workbook": "워크북 대상 불분명", "Supplier Mode": "기능 토글로 읽혀 제품 불분명",
 "Fertilizer Spec": "사양 참조로 제품 불분명", "Outreach Login": "제품 불분명",
 "Segment Coach": "선례 기각(App 상표 기각) 계열", "Rights Habit": "선례 기각(App 기각) 계열",
 "Lawyer Renewal": "갱신 대상 불분명(Notary Renewal 기각 평행)", "Attorney Voltage": "결합 불성립",
 "Court App": "법원·운동 코트 중의로 대상 불분명", "Peril Workbook": "선례 기각(App 기각) 계열",
 "Deduction Mode": "기능 토글로 읽혀 제품 불분명", "Plumbing Spec": "사양 참조로 제품 불분명",
 "Major Quantity": "선례 기각(App 기각) 계열", "Podcast Analysis": "분석 대상 불분명",
 "Channel Coach": "코칭 대상 불분명", "Skillset Habit": "결합 불성립",
 "Judge Core": "선례 기각(App 기각) 계열(Core 기각 라인)", "Jury Registry": "등록부 대상 불분명",
 "Lawsuit History": "이력 대상 불분명", "Custody Attribute": "속성 지칭으로 제품 불분명",
 "Immigration Count": "수량 지칭으로 제품 불분명", "Testament Volume": "볼륨(부피·권) 중의로 불분명",
 "Notary Payment": "결합 불성립", "Mediation Pressure": "결합 불성립",
 "Guardianship Guarantor": "보증인 명사 결합 불성립", "Brunch Workbook2": "",
 "Cleaning Spec2": "", "Nap Quantity2": "",
 "Shampoo Login2": "", "Refrigeration Analysis2": "",
 "Chiller Coach2": "", "Transponder Habit2": "",
 "Trademark Vault": "금고 지칭으로 제품 불분명", "Patent Center": "센터 지칭으로 제품 불분명(Center 기각 라인)",
 "Copyright Journal": "일지·잡지 중의로 불분명", "Migraine Seal": "결합 불성립",
 "Insomnia Refund": "결합 불성립", "Skydiving Claim": "결합 불성립",
}
for k in [k for k in R if k.endswith("2")]:
    del R[k]

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
out = base + r"\_dec_c38.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
