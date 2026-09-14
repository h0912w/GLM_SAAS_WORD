# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk28_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Facial App": (0.55, "페이셜 시술 예약 관리 앱(실재)"),
 "Facial Tips": (0.55, "Facial App 승인 선례의 Tips 평행"),
 "Crossdock App": (0.55, "크로스도킹 물류 처리 관리 앱(실재)"),
 "Crossdock Tips": (0.55, "Crossdock App 승인 선례의 Tips 평행"),
 "Attribution App": (0.55, "마케팅 기여도 추적 앱(실재)"),
 "Attribution Tips": (0.55, "Attribution App 승인 선례의 Tips 평행"),
 "Catering App": (0.55, "케이터링 주문·배식 관리 앱(실재)"),
 "Curtain App": (0.55, "커튼 제작·설치 관리 앱(실재)"),
 "Trademark App": (0.55, "상표 출원·관리 앱(실재)"),
 "Lawyer Guide": (0.55, "법률 절차 안내 가이드(Notary Guide 평행)"),
 "Valuation Tips": (0.55, "Valuation App 승인 선례의 Tips 평행"),
 "Syndication Tips": (0.55, "Syndication App 승인 선례의 Tips 평행"),
 "Sledding Diary": (0.55, "썰매 기록 일지(Rafting Diary 평행)"),
}

R_DUP = {
 "Broker Advice": "직전 승인 Broker Tips와 동일 기능 의미 중복",
 "Valuation Advice": "이번 배치 승인 Valuation Tips와 동일 기능 의미 중복",
 "Syndication Advice": "이번 배치 승인 Syndication Tips와 동일 기능 의미 중복",
}

R = {
 "Reservation Coach": "코칭 대상 불분명", "Grooming Habit": "결합 불성립",
 "Sterilization Workbook": "워크북 대상 불분명", "Program Mode": "선례 기각(App 기각) 계열",
 "Meal Spec": "사양 참조로 제품 불분명", "Loyalty Habit": "결합 불성립",
 "Attorney Onboarding": "결합 불성립", "Court Evaluation": "평가 대상 불분명",
 "Tablet Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Freon Advice": "선례 기각(App 상표 기각) 계열",
 "Hinge Workbook": "선례 기각(App 상표 기각) 계열", "Apostille Mode": "기능 토글로 읽혀 제품 불분명",
 "Invite Login": "제품 불분명", "Coping Coach": "코칭 대상 불분명",
 "Wheel Habit": "결합 불성립", "Judge Relay": "선례 기각(App 기각) 계열",
 "Jury Trail": "오솔길·추적 중의로 불분명", "Lawsuit Passport": "여권 결합 불성립",
 "Divorce Code": "코드·법전 중의로 불분명", "Custody Fund": "기금 결합 불성립",
 "Immigration Advance": "선급금·사전 승인 중의로 불분명", "Testament Workshop": "워크숍·작업장 중의로 불분명",
 "Notary Lookup": "탐색 대상 불분명", "Mediation Inventory": "결합 불성립",
 "Guardianship Condition": "상태 명사로 제품명 부자연", "Trademark Flyer": "결합 불성립",
 "Grievance Workbook": "워크북 대상 불분명", "Paving Mode": "기능 토글로 읽혀 제품 불분명",
 "Suspension Spec": "사양 참조로 제품 불분명", "Streetlight Quantity": "수량 대상 불분명",
 "Publisher Login": "제품 불분명", "Salary Analysis": "분석 대상 불분명",
 "Background Coach": "선례 기각(App 기각) 계열", "Windshield Habit": "결합 불성립",
 "Patent Watch": "시계·감시 중의로 불분명(Watch 기각 선례)", "Copyright Rail": "레일 지칭으로 제품 불분명",
 "Migraine Eligibility": "결합 불성립", "Insomnia Invoice": "결합 불성립",
 "Skydiving Deposit": "결합 불성립", "Acne Certification": "결합 불성립",
 "Snowboarding Payment": "결합 불성립", "Eczema Verification": "결합 불성립",
 "Ziplining Seal": "결합 불성립", "Psoriasis Review": "리뷰 대상 불분명",
 "Vertigo Refund": "결합 불성립", "Diving Inventory": "결합 불성립",
 "Arthritis Claim": "결합 불성립", "Sailing Size": "결합 불성립(속성 지칭)",
 "Menopause Length": "결합 불성립(속성 지칭)", "Rafting Range": "결합 불성립",
 "Pregnancy Limit": "결합 불성립", "Climbing Time": "결합 불성립",
 "Fertility Speed": "결합 불성립", "Biking Width": "결합 불성립",
 "Thyroid Temperature": "결합 불성립", "Golf Voltage": "결합 불성립",
 "Cholesterol Wattage": "결합 불성립", "Fishing Compatibility": "상태 명사로 제품명 부자연",
 "Hypertension Capacity": "상태 명사로 제품명 부자연", "Camping Humidity": "결합 불성립",
 "Anemia Episode": "결합 불성립", "Glamping Sensor": "결합 불성립",
 "Heartburn Reception": "리셉션·수신 중의로 불분명", "Stargazing Matrix": "행렬·매트릭스 중의로 불분명",
 "Constipation Evaluation": "평가 대상 불분명", "Birdwatching Benefit": "혜택 지칭으로 제품 불분명",
 "Concussion Requirement": "요건 지칭으로 제품 불분명", "Canyon Resignation": "결합 불성립",
 "Sprain Hazard": "결합 불성립", "Geyser Guarantor": "보증인 명사 결합 불성립",
 "Fracture Tuner": "튜너 기능 지칭으로 제품 불분명", "Fjord Tutorial": "terrain 대상 결합 불성립",
 "Insulin Handbook": "terrain 대상 결합 불성립", "Savanna Timetable": "terrain 대상 결합 불성립",
 "Tundra Opinion": "terrain 대상 결합 불성립", "Prairie Gift": "결합 불성립",
 "Marsh Retreat": "terrain 대상 결합 불성립", "Cove Tournament": "terrain 대상 결합 불성립",
 "Cliff Flyer": "terrain 대상 결합 불성립", "Cavern App": "지명 지칭으로 제품 불분명",
 "Oasis Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Dune Advice": "선례 기각(App 기각) 계열",
 "Whale Workbook": "선례 기각(App 기각) 계열", "Dolphin Mode": "선례 기각(App 기각) 계열",
 "Penguin Spec": "선례 기각(App 기각) 계열", "Flamingo Quantity": "선례 기각(App 기각) 계열",
 "Turtle Login": "선례 기각(App 기각) 계열", "Moose Analysis": "선례 기각(App 기각) 계열",
 "Bison Coach": "선례 기각(App 기각) 계열", "Reindeer Habit": "선례 기각(App 기각) 계열",
 "Bandwidth Workbook": "선례 기각(App 기각) 계열", "Credential Mode": "기능 토글로 읽혀 제품 불분명",
 "Backup Spec": "사양 참조로 제품 불분명", "Satisfaction Quantity": "수량 대상 불분명",
 "Offer Login": "제품 불분명", "Sponsor Analysis": "분석 대상 불분명",
 "Reservation Habit": "결합 불성립", "Sterilization Mode": "기능 토글로 읽혀 제품 불분명",
 "Program Spec": "선례 기각(App 기각) 계열", "Meal Quantity": "수량 대상 불분명",
 "Lawyer Rating": "평가 대상 불분명", "Attorney Checkin": "결합 불성립",
 "Court Questionnaire": "설문 대상 불분명", "Tablet Advice": "선례 기각(App 기각) 계열",
 "Freon Workbook": "선례 기각(App 상표 기각) 계열", "Hinge Mode": "선례 기각(App 상표 기각) 계열",
 "Apostille Spec": "사양 참조로 제품 불분명", "Invite Analysis": "분석 대상 불분명",
 "Coping Habit": "결합 불성립", "Judge Vault": "선례 기각(App 기각) 계열",
 "Jury Chain": "체인(사슬·체인점) 중의로 불분명", "Lawsuit Lobby": "로비(현관·로비잉) 중의로 불분명",
 "Divorce List": "목록 지칭으로 제품 불분명", "Custody Cash": "현금 결합 불성립",
 "Immigration Penalty": "벌칙 결합 불성립", "Testament Guardian": "후견인 명사 결합 불성립",
 "Notary Ping": "결합 불성립", "Mediation Claim": "결합 불성립",
 "Guardianship Humidity": "결합 불성립", "Trademark App2": "",
 "Crossdock Tips2": "", "Broker Workbook": "워크북 대상 불분명",
 "Grievance Mode": "기능 토글로 읽혀 제품 불분명", "Paving Spec": "사양 참조로 제품 불분명",
 "Suspension Quantity": "수량 대상 불분명", "Streetlight Login": "제품 불분명",
 "Publisher Analysis": "분석 대상 불분명", "Salary Coach": "코칭 대상 불분명",
 "Background Habit": "선례 기각(App 기각) 계열", "Patent Scope": "범위 기능 지칭으로 제품 불분명",
 "Copyright Trail": "오솔길·추적 중의로 불분명", "Migraine Broadcast": "결합 불성립",
 "Insomnia Renewal": "결합 불성립", "Skydiving Certification": "결합 불성립",
 "Acne Nomination": "결합 불성립", "Snowboarding Verification": "결합 불성립",
 "Eczema Simulator": "결합 불성립", "Ziplining Review": "리뷰 대상 불분명",
 "Psoriasis Recipe": "결합 불성립", "Sledding Refund": "결합 불성립",
 "Vertigo Expense": "결합 불성립", "Diving Claim": "결합 불성립",
 "Arthritis Onboarding": "결합 불성립", "Sailing Length": "결합 불성립(속성 지칭)",
 "Menopause Weight": "결합 불성립(속성 지칭)", "Rafting Limit": "결합 불성립",
 "Pregnancy Type": "결합 불성립(분류 대상 부자연)", "Climbing Speed": "결합 불성립",
 "Fertility Depth": "결합 불성립", "Biking Temperature": "결합 불성립",
 "Thyroid Pressure": "결합 불성립", "Golf Wattage": "결합 불성립",
 "Cholesterol Brightness": "결합 불성립", "Fishing Capacity": "상태 명사로 제품명 부자연",
 "Hypertension Usage": "사용 지칭으로 제품 불분명", "Camping Episode": "결합 불성립",
 "Anemia Cycle": "주기 지칭으로 제품 불분명", "Glamping Reception": "리셉션·수신 중의로 불분명",
 "Heartburn Followup": "후속 지칭으로 제품 불분명", "Stargazing Evaluation": "평가 대상 불분명",
 "Constipation Questionnaire": "설문 대상 불분명", "Birdwatching Requirement": "요건 지칭으로 제품 불분명",
 "Concussion Depreciation": "결합 불성립", "Canyon Hazard": "결합 불성립",
 "Sprain Guarantor": "보증인 명사 결합 불성립", "Geyser Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Fracture Tutorial": "terrain 대상 결합 불성립", "Fjord Handbook": "terrain 대상 결합 불성립",
 "Insulin Timetable": "terrain 대상 결합 불성립", "Savanna Opinion": "terrain 대상 결합 불성립",
 "Tundra Gift": "결합 불성립", "Prairie Retreat": "terrain 대상 결합 불성립",
 "Marsh Tournament": "terrain 대상 결합 불성립", "Cove Flyer": "terrain 대상 결합 불성립",
 "Cliff App": "지명 지칭으로 제품 불분명", "Cavern Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Oasis Advice": "선례 기각(App 기각) 계열", "Dune Workbook": "선례 기각(App 기각) 계열",
 "Whale Mode": "선례 기각(App 기각) 계열", "Dolphin Spec": "선례 기각(App 기각) 계열",
 "Penguin Quantity": "선례 기각(App 기각) 계열", "Flamingo Login": "선례 기각(App 기각) 계열",
 "Turtle Analysis": "선례 기각(App 기각) 계열", "Moose Coach": "선례 기각(App 기각) 계열",
 "Bison Habit": "선례 기각(App 기각) 계열", "Reindeer Tracker": "선례 기각(App 기각) 계열",
}
del R["Trademark App2"]
del R["Crossdock Tips2"]
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
out = base + r"\_dec_c29.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
