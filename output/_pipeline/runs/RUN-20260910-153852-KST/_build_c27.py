# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk26_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Paving App": (0.55, "도로 포장 시공 관리 앱(실재)"),
 "Paving Tips": (0.55, "Paving App 승인 선례의 Tips 평행"),
 "Suspension Tips": (0.55, "Suspension App 승인 선례의 Tips 평행"),
 "Credential App": (0.55, "자격 증명·인증서 관리 앱(실재)"),
 "Credential Tips": (0.55, "Credential App 승인 선례의 Tips 평행"),
 "Sterilization App": (0.55, "기구 멸균 기록·관리 앱(실재)"),
 "Sterilization Tips": (0.55, "Sterilization App 승인 선례의 Tips 평행"),
 "Grievance App": (0.55, "민원·불만 접수 처리 관리 앱(실재)"),
 "Backup Tips": (0.55, "Backup App 승인 선례의 Tips 평행"),
 "Apostille Tips": (0.55, "Apostille App 승인 선례의 Tips 평행"),
 "Lawsuit Alert": (0.55, "소송 일정 알림 관리(Reminder/Notification 절차 명사 선례 평행)"),
 "Divorce Order": (0.55, "법원 명령 이행 관리(Notification 절차 명사 선례 평행)"),
 "Diving Diary": (0.55, "다이빙 로그 기록 일지(Rafting Diary 평행)"),
}

R_DUP = {
 "Streetlight Advice": "직전 승인 Streetlight Tips와 동일 기능 의미 중복",
 "Suspension Advice": "이번 배치 승인 Suspension Tips와 동일 기능 의미 중복",
 "Backup Advice": "이번 배치 승인 Backup Tips와 동일 기능 의미 중복",
 "Satisfaction Advice": "직전 승인 Satisfaction Tips와 동일 기능 의미 중복",
 "Meal Advice": "직전 승인 Meal Tips와 동일 기능 의미 중복",
}

R = {
 "Coping Spec": "사양 참조로 제품 불분명", "Wheel Quantity": "수량 대상 불분명",
 "Cistern Login": "제품 불분명", "Souvenir Analysis": "분석 대상 불분명",
 "Trombone Coach": "코칭 대상 불분명", "Judge Flow": "선례 기각(App 기각) 계열",
 "Jury Panel": "배심원단·패널 중의로 불분명", "Lawsuit Roster": "명단 지칭으로 제품 불분명",
 "Divorce Estimate": "견적·추정 중의로 불분명", "Custody Tax": "세금 결합 불성립",
 "Immigration Due": "기한·요금 중의로 불분명", "Testament Estimator": "추정 도구 지칭으로 제품 불분명",
 "Notary Account": "계정 결합 불성립", "Mediation Diary": "일지 대상 불분명(Attorney Diary 기각 선례)",
 "Guardianship Frequency": "결합 불성립", "Trademark Opinion": "의견 대상 불분명(Judge Opinion 기각 선례)",
 "Publisher Workbook": "워크북 대상 불분명", "Streetlight Workbook": "워크북 대상 불분명",
 "Salary Mode": "기능 토글로 읽혀 제품 불분명",
 "Background Spec": "선례 기각(App 기각) 계열", "Windshield Quantity": "수량 대상 불분명",
 "Bakery Login": "제품 불분명", "Exam Analysis": "분석 대상 불분명",
 "Sedation Coach": "코칭 대상 불분명", "Playtime Habit": "결합 불성립",
 "Patent Forge": "용광로·조립 중의로 불분명", "Copyright Console": "콘솔 중의로 불분명",
 "Migraine Lookup": "탐색 대상 불분명", "Insomnia Broadcast": "결합 불성립",
 "Skydiving Invoice": "결합 불성립", "Acne Renewal": "결합 불성립",
 "Snowboarding Certification": "결합 불성립", "Eczema Nomination": "결합 불성립",
 "Ziplining Payment": "결합 불성립", "Psoriasis Verification": "결합 불성립",
 "Sledding Seal": "결합 불성립", "Vertigo Review": "리뷰 대상 불분명",
 "Diving Diary2": "", "Arthritis Refund": "결합 불성립",
 "Sailing Inventory": "결합 불성립", "Menopause Claim": "결합 불성립",
 "Rafting Size": "결합 불성립(속성 지칭)", "Pregnancy Length": "결합 불성립(속성 지칭)",
 "Climbing Range": "결합 불성립", "Fertility Limit": "결합 불성립",
 "Biking Time": "결합 불성립", "Thyroid Speed": "결합 불성립",
 "Golf Width": "결합 불성립", "Cholesterol Temperature": "결합 불성립",
 "Fishing Voltage": "결합 불성립", "Hypertension Wattage": "결합 불성립",
 "Camping Compatibility": "상태 명사로 제품명 부자연", "Anemia Capacity": "상태 명사로 제품명 부자연",
 "Glamping Humidity": "결합 불성립", "Heartburn Episode": "결합 불성립",
 "Stargazing Sensor": "결합 불성립", "Constipation Reception": "리셉션·수신 중의로 불분명",
 "Birdwatching Matrix": "행렬·매트릭스 중의로 불분명", "Concussion Evaluation": "평가 대상 불분명",
 "Canyon Utilization": "활용 지칭으로 제품 불분명", "Sprain Benefit": "혜택 지칭으로 제품 불분명",
 "Geyser Requirement": "요건 지칭으로 제품 불분명", "Fracture Depreciation": "결합 불성립",
 "Fjord Resignation": "결합 불성립", "Insulin Hazard": "결합 불성립",
 "Savanna Guarantor": "보증인 명사 결합 불성립", "Tundra Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Prairie Tutorial": "terrain 대상 결합 불성립", "Marsh Handbook": "terrain 대상 결합 불성립",
 "Cove Timetable": "terrain 대상 결합 불성립", "Cliff Opinion": "terrain 대상 결합 불성립",
 "Cavern Gift": "결합 불성립", "Oasis Retreat": "terrain 대상 결합 불성립",
 "Dune Tournament": "terrain 대상 결합 불성립", "Whale Flyer": "동물 대상 결합 불성립",
 "Dolphin App": "동물 지칭으로 제품 불분명", "Penguin Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Flamingo Advice": "선례 기각(App 기각) 계열", "Turtle Workbook": "선례 기각(App 기각) 계열",
 "Moose Mode": "선례 기각(App 기각) 계열", "Bison Spec": "선례 기각(App 기각) 계열",
 "Reindeer Quantity": "선례 기각(App 기각) 계열", "Hinge App": "유명 데이팅 앱 상표(Hinge)",
 "Offer Workbook": "워크북 대상 불분명", "Sponsor Mode": "기능 토글로 읽혀 제품 불분명",
 "Reservation Quantity": "수량 대상 불분명", "Grooming Login": "제품 불분명",
 "Hygiene Analysis": "분석 대상 불분명", "Curriculum Habit": "결합 불성립",
 "Bandwidth App": "대역폭 속성 지칭으로 제품 불분명", "Program Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Loyalty Login": "제품 불분명", "Lawyer Progress": "진행 대상 불분명",
 "Attorney Newsletter": "결합 불성립", "Court Followup": "후속 지칭으로 제품 불분명",
 "Invite Mode": "기능 토글로 읽혀 제품 불분명", "Coping Quantity": "수량 대상 불분명",
 "Wheel Login": "제품 불분명", "Cistern Analysis": "분석 대상 불분명",
 "Souvenir Coach": "코칭 대상 불분명", "Trombone Habit": "결합 불성립",
 "Judge Hub": "선례 기각(App 기각) 계열", "Jury Scale": "저울·규모 중의로 불분명",
 "Lawsuit Alert2": "", "Divorce Order2": "", "Custody Loan": "대출 결합 불성립",
 "Immigration Subsidy": "보조금 결합 불성립", "Testament Checker": "검사 도구 지칭으로 제품 불분명",
 "Notary Case": "결합 불성립(Case 계열 기각 선례)", "Mediation Refund": "결합 불성립",
 "Guardianship Compatibility": "상태 명사로 제품명 부자연", "Trademark Gift": "결합 불성립",
 "Publisher Mode": "기능 토글로 읽혀 제품 불분명", "Salary Spec": "사양 참조로 제품 불분명",
 "Background Quantity": "선례 기각(App 기각) 계열", "Windshield Login": "제품 불분명",
 "Bakery Analysis": "분석 대상 불분명", "Exam Coach": "코칭 대상 불분명",
 "Sedation Habit": "결합 불성립", "Patent Cascade": "폭포·연쇄 중의로 불분명",
 "Copyright Panel": "패널 중의로 불분명", "Migraine Ping": "결합 불성립",
 "Insomnia Barcode": "결합 불성립", "Skydiving Renewal": "결합 불성립",
 "Acne Quote": "인용·견적 중의로 불분명", "Snowboarding Nomination": "결합 불성립",
 "Eczema Correction": "결합 불성립", "Ziplining Verification": "결합 불성립",
 "Psoriasis Simulator": "결합 불성립", "Sledding Review": "리뷰 대상 불분명",
 "Vertigo Recipe": "결합 불성립", "Diving Refund": "결합 불성립",
 "Arthritis Expense": "결합 불성립", "Sailing Claim": "결합 불성립",
 "Menopause Onboarding": "결합 불성립", "Rafting Length": "결합 불성립(속성 지칭)",
 "Pregnancy Weight": "결합 불성립(속성 지칭)", "Climbing Limit": "결합 불성립",
 "Fertility Type": "결합 불성립(분류 대상 부자연)", "Biking Speed": "결합 불성립",
 "Thyroid Depth": "결합 불성립", "Golf Temperature": "결합 불성립",
 "Cholesterol Pressure": "결합 불성립", "Fishing Wattage": "결합 불성립",
 "Hypertension Brightness": "결합 불성립", "Camping Capacity": "상태 명사로 제품명 부자연",
 "Anemia Usage": "사용 지칭으로 제품 불분명", "Glamping Episode": "결합 불성립",
 "Heartburn Cycle": "주기 지칭으로 제품 불분명", "Stargazing Reception": "리셉션·수신 중의로 불분명",
 "Constipation Followup": "후속 지칭으로 제품 불분명", "Birdwatching Evaluation": "평가 대상 불분명",
 "Concussion Questionnaire": "설문 대상 불분명", "Canyon Benefit": "혜택 지칭으로 제품 불분명",
 "Sprain Requirement": "요건 지칭으로 제품 불분명", "Geyser Depreciation": "결합 불성립",
 "Fracture Resignation": "결합 불성립", "Fjord Hazard": "결합 불성립",
 "Insulin Guarantor": "보증인 명사 결합 불성립", "Savanna Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Tundra Tutorial": "terrain 대상 결합 불성립", "Prairie Handbook": "terrain 대상 결합 불성립",
 "Marsh Timetable": "terrain 대상 결합 불성립", "Cove Opinion": "terrain 대상 결합 불성립",
 "Cliff Gift": "결합 불성립", "Cavern Retreat": "terrain 대상 결합 불성립",
 "Oasis Tournament": "terrain 대상 결합 불성립", "Dune Flyer": "terrain 대상 결합 불성립",
 "Whale App": "동물 지칭으로 제품 불분명", "Dolphin Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Penguin Advice": "선례 기각(App 기각) 계열", "Flamingo Workbook": "선례 기각(App 기각) 계열",
 "Turtle Mode": "선례 기각(App 기각) 계열", "Moose Spec": "선례 기각(App 기각) 계열",
 "Bison Quantity": "선례 기각(App 기각) 계열", "Reindeer Login": "선례 기각(App 기각) 계열",
 "Satisfaction Workbook": "워크북 대상 불분명", "Offer Mode": "기능 토글로 읽혀 제품 불분명",
 "Sponsor Spec": "사양 참조로 제품 불분명", "Reservation Login": "제품 불분명",
 "Grooming Analysis": "분석 대상 불분명", "Hygiene Coach": "코칭 대상 불분명",
 "Program Advice": "선례 기각(App 기각) 계열", "Meal Workbook": "워크북 대상 불분명",
 "Loyalty Analysis": "분석 대상 불분명",
}
del R["Diving Diary2"]
del R["Lawsuit Alert2"]
del R["Divorce Order2"]
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
out = base + r"\_dec_c27.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
