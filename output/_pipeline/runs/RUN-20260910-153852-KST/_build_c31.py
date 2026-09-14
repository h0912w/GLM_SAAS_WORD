# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk30_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Consumption App": (0.55, "에너지·자원 소비 추적 앱(실재)"),
 "Consumption Tips": (0.55, "Consumption App 승인 선례의 Tips 평행"),
 "Firewall App": (0.55, "네트워크 방화벽 관리 앱(실재)"),
 "Server App": (0.55, "서버 운영·모니터링 앱(실재)"),
 "Spay App": (0.55, "반려동물 중성화 수술 관리 앱(실재)"),
 "Spay Tips": (0.55, "Spay App 승인 선례의 Tips 평행"),
 "Barbecue App": (0.55, "바비큐 주문·대여 관리 앱(실재)"),
 "Braces Tips": (0.55, "Braces App 승인 선례의 Tips 평행"),
 "Knowledge Tips": (0.55, "Knowledge App 승인 선례의 Tips 평행"),
 "Visit Tips": (0.55, "Visit App 승인 선례의 Tips 평행"),
 "Campaign Tips": (0.55, "Campaign App 승인 선례의 Tips 평행"),
 "Immigration Extension": (0.55, "비자·체류 연장 절차 관리(Deadline 절차 명사 선례 평행)"),
 "Ziplining Diary": (0.55, "짚라인 기록 일지(Rafting Diary 평행)"),
}

R_DUP = {
 "Braces Advice": "이번 배치 승인 Braces Tips와 동일 기능 의미 중복",
 "Knowledge Advice": "이번 배치 승인 Knowledge Tips와 동일 기능 의미 중복",
 "Visit Advice": "이번 배치 승인 Visit Tips와 동일 기능 의미 중복",
 "Campaign Advice": "이번 배치 승인 Campaign Tips와 동일 기능 의미 중복",
 "Assessment Advice": "직전 승인 Assessment Tips와 동일 기능 의미 중복",
 "Installment Advice": "직전 승인 Installment Tips와 동일 기능 의미 중복",
}

R = {
 "Flamingo Coach": "선례 기각(App 기각) 계열", "Turtle Habit": "선례 기각(App 기각) 계열",
 "Moose Tracker": "선례 기각(App 기각) 계열", "Bison Flow": "선례 기각(App 기각) 계열",
 "Reindeer Hub": "선례 기각(App 기각) 계열", "Migration App": "이주·데이터 이전 중의로 불분명",
 "Attribution Workbook": "워크북 대상 불분명", "Syndication Mode": "기능 토글로 읽혀 제품 불분명",
 "Bandwidth Quantity": "선례 기각(App 기각) 계열", "Credential Login": "제품 불분명",
 "Backup Analysis": "분석 대상 불분명", "Satisfaction Coach": "코칭 대상 불분명",
 "Offer Habit": "결합 불성립", "Catering Workbook": "워크북 대상 불분명",
 "Sterilization Login": "제품 불분명", "Program Analysis": "선례 기각(App 기각) 계열",
 "Meal Coach": "코칭 대상 불분명", "Lawyer Account": "계정 결합 불성립",
 "Attorney Weight": "결합 불성립(속성 지칭)", "Court Requirement": "요건 지칭으로 제품 불분명",
 "Snack Advice": "직전 승인 Snack Tips와 동일 기능 의미 중복", "Curtain Workbook": "워크북 대상 불분명",
 "Facial Mode": "기능 토글로 읽혀 제품 불분명", "Tablet Spec": "선례 기각(App 기각) 계열",
 "Freon Quantity": "선례 기각(App 상표 기각) 계열", "Hinge Login": "선례 기각(App 상표 기각) 계열",
 "Apostille Analysis": "분석 대상 불분명", "Judge Forge": "선례 기각(App 기각) 계열",
 "Jury Nexus": "연결점 명사 결합 불성립", "Lawsuit Window": "창문·기간 중의로 불분명",
 "Divorce Sample": "견본 지칭으로 제품 불분명", "Custody Duty": "의무 결합 불성립",
 "Testament Result": "결과 지칭으로 제품 불분명", "Notary Eligibility": "결합 불성립",
 "Mediation Size": "결합 불성립(속성 지칭)", "Guardianship Breakdown": "내역·고장 중의로 불분명",
 "Theory App": "이론 대상 불분명", "Trademark Workbook": "워크북 대상 불분명",
 "Crossdock Mode": "기능 토글로 읽혀 제품 불분명", "Valuation Spec": "사양 참조로 제품 불분명",
 "Broker Quantity": "수량 대상 불분명", "Grievance Login": "제품 불분명",
 "Paving Analysis": "분석 대상 불분명", "Suspension Coach": "코칭 대상 불분명",
 "Streetlight Habit": "결합 불성립", "Patent Wave": "파도·물결 중의로 불분명(Wave 기각 선례)",
 "Copyright Gate": "게이트 지칭으로 제품 불분명", "Migraine Feedback": "결합 불성립",
 "Insomnia Deposit": "결합 불성립", "Skydiving Revision": "결합 불성립",
 "Acne Payment": "결합 불성립", "Snowboarding Seal": "결합 불성립",
 "Eczema Review": "리뷰 대상 불분명", "Psoriasis Refund": "결합 불성립",
 "Sledding Inventory": "결합 불성립", "Vertigo Claim": "결합 불성립",
 "Diving Size": "결합 불성립(속성 지칭)", "Arthritis Length": "결합 불성립(속성 지칭)",
 "Sailing Range": "결합 불성립", "Menopause Limit": "결합 불성립",
 "Rafting Time": "결합 불성립", "Pregnancy Speed": "결합 불성립",
 "Climbing Width": "결합 불성립", "Fertility Temperature": "결합 불성립",
 "Biking Voltage": "결합 불성립", "Thyroid Wattage": "결합 불성립",
 "Golf Compatibility": "상태 명사로 제품명 부자연", "Cholesterol Capacity": "상태 명사로 제품명 부자연",
 "Fishing Humidity": "결합 불성립", "Hypertension Episode": "결합 불성립",
 "Camping Sensor": "결합 불성립", "Anemia Reception": "리셉션·수신 중의로 불분명",
 "Glamping Matrix": "행렬·매트릭스 중의로 불분명", "Heartburn Evaluation": "평가 대상 불분명",
 "Stargazing Benefit": "혜택 지칭으로 제품 불분명", "Constipation Requirement": "요건 지칭으로 제품 불분명",
 "Birdwatching Hazard": "결합 불성립", "Concussion Guarantor": "보증인 명사 결합 불성립",
 "Canyon Tutorial": "terrain 대상 결합 불성립", "Sprain Handbook": "terrain 대상 결합 불성립",
 "Geyser Timetable": "terrain 대상 결합 불성립", "Fracture Opinion": "terrain 대상 결합 불성립",
 "Fjord Gift": "결합 불성립", "Insulin Retreat": "terrain 대상 결합 불성립",
 "Savanna Tournament": "terrain 대상 결합 불성립", "Tundra Flyer": "terrain 대상 결합 불성립",
 "Prairie App": "지명 지칭으로 제품 불분명", "Marsh Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Cove Advice": "선례 기각(App 기각) 계열", "Cliff Workbook": "선례 기각(App 기각) 계열",
 "Cavern Mode": "선례 기각(App 기각) 계열", "Oasis Spec": "선례 기각(App 기각) 계열",
 "Dune Quantity": "선례 기각(App 기각) 계열", "Whale Login": "선례 기각(App 기각) 계열",
 "Dolphin Analysis": "선례 기각(App 기각) 계열", "Penguin Coach": "선례 기각(App 기각) 계열",
 "Flamingo Habit": "선례 기각(App 기각) 계열", "Turtle Tracker": "선례 기각(App 기각) 계열",
 "Moose Flow": "선례 기각(App 기각) 계열", "Bison Hub": "선례 기각(App 기각) 계열",
 "Reindeer Desk": "선례 기각(App 기각) 계열", "Yield App": "수익률·수확량·양보 중의로 불분명",
 "Attribution Mode": "기능 토글로 읽혀 제품 불분명", "Syndication Spec": "사양 참조로 제품 불분명",
 "Bandwidth Login": "선례 기각(App 기각) 계열", "Credential Analysis": "분석 대상 불분명",
 "Backup Coach": "코칭 대상 불분명", "Satisfaction Habit": "결합 불성립",
 "Migration Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Assessment Workbook": "워크북 대상 불분명",
 "Catering Mode": "기능 토글로 읽혀 제품 불분명", "Sterilization Analysis": "분석 대상 불분명",
 "Program Coach": "선례 기각(App 기각) 계열", "Meal Habit": "결합 불성립",
 "Lawyer Case": "결합 불성립(Case 계열 기각 선례)", "Attorney Distance": "결합 불성립",
 "Court Depreciation": "결합 불성립", "Braces Advice2": "",
 "Snack Workbook": "워크북 대상 불분명", "Curtain Mode": "기능 토글로 읽혀 제품 불분명",
 "Facial Spec": "사양 참조로 제품 불분명", "Tablet Quantity": "선례 기각(App 기각) 계열",
 "Freon Login": "선례 기각(App 상표 기각) 계열", "Hinge Analysis": "선례 기각(App 상표 기각) 계열",
 "Apostille Coach": "코칭 대상 불분명", "Judge Cascade": "선례 기각(App 기각) 계열",
 "Jury Atlas": "지도책 지칭으로 제품 불분명", "Lawsuit Roll": "명단·롤 중의로 불분명",
 "Divorce Slot": "시간대 슬롯 지칭으로 제품 불분명", "Custody Allowance": "수당·용돈 결합 불성립",
 "Immigration Trial": "재판·시험 중의로 불분명(Trial 기각 선례)", "Testament Streak": "연속 기록 지칭으로 제품 불분명",
 "Notary Broadcast": "결합 불성립", "Mediation Length": "결합 불성립(속성 지칭)",
 "Guardianship Sensor": "결합 불성립", "Barbecue App2": "",
 "Theory Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Installment Workbook": "워크북 대상 불분명",
 "Trademark Mode": "기능 토글로 읽혀 제품 불분명", "Crossdock Spec": "사양 참조로 제품 불분명",
 "Valuation Quantity": "수량 대상 불분명", "Broker Login": "제품 불분명",
 "Grievance Analysis": "분석 대상 불분명", "Paving Coach": "코칭 대상 불분명",
 "Suspension Habit": "결합 불성립", "Patent Path": "경로 지칭으로 제품 불분명(Path 기각 선례)",
 "Copyright Nexus": "연결점 명사 결합 불성립", "Migraine Invoice": "결합 불성립",
 "Insomnia Certification": "결합 불성립", "Skydiving Payment": "결합 불성립",
 "Acne Verification": "결합 불성립", "Snowboarding Review": "리뷰 대상 불분명",
 "Eczema Recipe": "결합 불성립", "Ziplining Refund": "결합 불성립",
 "Psoriasis Expense": "결합 불성립", "Sledding Claim": "결합 불성립",
 "Vertigo Onboarding": "결합 불성립", "Diving Length": "결합 불성립(속성 지칭)",
 "Arthritis Weight": "결합 불성립(속성 지칭)", "Sailing Limit": "결합 불성립",
 "Menopause Type": "결합 불성립(분류 대상 부자연)", "Rafting Speed": "결합 불성립",
 "Pregnancy Depth": "결합 불성립", "Climbing Temperature": "결합 불성립",
 "Fertility Pressure": "결합 불성립", "Biking Wattage": "결합 불성립",
 "Thyroid Brightness": "결합 불성립", "Golf Capacity": "상태 명사로 제품명 부자연",
 "Cholesterol Usage": "사용 지칭으로 제품 불분명", "Fishing Episode": "결합 불성립",
 "Hypertension Cycle": "주기 지칭으로 제품 불분명", "Camping Reception": "리셉션·수신 중의로 불분명",
 "Anemia Followup": "후속 지칭으로 제품 불분명", "Glamping Evaluation": "평가 대상 불분명",
 "Heartburn Questionnaire": "설문 대상 불분명", "Stargazing Requirement": "요건 지칭으로 제품 불분명",
 "Constipation Depreciation": "결합 불성립", "Birdwatching Guarantor": "보증인 명사 결합 불성립",
 "Concussion Tuner": "튜너 기능 지칭으로 제품 불분명", "Canyon Handbook": "terrain 대상 결합 불성립",
 "Sprain Timetable": "terrain 대상 결합 불성립", "Geyser Opinion": "terrain 대상 결합 불성립",
 "Fracture Gift": "결합 불성립",
}
del R["Braces Advice2"]
del R["Barbecue App2"]
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
out = base + r"\_dec_c31.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
