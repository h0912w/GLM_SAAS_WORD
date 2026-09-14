# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk14_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Carrier App": (0.55, "운송·물류 배차 관리 앱(실재)"),
 "Carrier Tips": (0.55, "Carrier App 승인 선례의 Tips 평행"),
 "Lockout App": (0.55, "잠금·출입 통제 절차 관리 앱(실재)"),
 "Lockout Tips": (0.55, "Lockout App 승인 선례의 Tips 평행"),
 "Wrench App": (0.55, "자동차 정비 예약·작업 관리 앱(실재)"),
 "Cover App": (0.55, "보험 보장·가입 관리 앱(실재)"),
 "Realtor App": (0.55, "부동산 중개 매물·고객 관리 앱(실재)"),
 "Ductwork App": (0.55, "덕트 시공·점검 관리 앱(실재)"),
 "Union Tips": (0.55, "Union App 승인 선례의 Tips 평행"),
 "Turnaround Tips": (0.55, "Turnaround App 승인 선례의 Tips 평행"),
 "Attraction Tips": (0.55, "Attraction App 승인 선례의 Tips 평행"),
 "Recording Tips": (0.55, "Recording App 승인 선례의 Tips 평행"),
 "Eczema Guide": (0.55, "습진 관리 가이드 콘텐츠(Psoriasis Guide 평행)"),
 "Snowboarding Guide": (0.55, "스노보드 입문 가이드 콘텐츠(Ziplining Guide 평행)"),
 "Cholesterol Video": (0.55, "콜레스테롤 관리 영상 가이드(Hypertension Video 평행)"),
}

R_DUP = {
 "Insulation Advice": "직전 승인 Insulation Tips와 동일 기능 의미 중복",
 "Packing Advice": "직전 승인 Packing Tips와 동일 기능 의미 중복",
 "Trumpet Advice": "직전 승인 Trumpet Tips와 동일 기능 의미 중복",
 "Union Advice": "이번 배치 승인 Union Tips와 동일 기능 의미 중복",
 "Turnaround Advice": "이번 배치 승인 Turnaround Tips와 동일 기능 의미 중복",
}

R = {
 "Diaper Spec": "사양 참조로 제품 불분명", "Wardrobe Quantity": "수량 대상 불분명",
 "Waxing Login": "제품 불분명", "Syrup Analysis": "분석 대상 불분명",
 "Zoning Coach": "코칭 대상 불분명", "Bolt Habit": "결합 불성립",
 "Jury Signal": "신호 기능 지칭으로 제품 불분명", "Lawsuit Manager": "관리자 지칭으로 제품 불분명",
 "Divorce Log": "기록 대상 불분명", "Custody Pass": "통행증·패스 중의로 불분명",
 "Immigration Tariff": "결합 불성립", "Testament Trial": "재판·시험 중의로 불분명",
 "Notary Result": "결과 지칭으로 제품 불분명", "Mediation Availability": "상태 명사로 제품명 부자연",
 "Guardianship Inventory": "결합 불성립", "Trademark Condition": "상태 명사로 제품명 부자연",
 "Patent Retreat": "물러남·수련 중의로 불분명", "Tutoring Workbook": "워크북 대상 불분명",
 "Pothole Mode": "기능 토글로 읽혀 제품 불분명", "Newsletter Spec": "사양 참조로 제품 불분명",
 "Benefits Quantity": "수량 대상 불분명", "Complaint Login": "제품 불분명",
 "Bumper Analysis": "분석 대상 불분명", "Pastry Coach": "코칭 대상 불분명",
 "Copyright Bridge": "다리 중의로 불분명", "Migraine Comparison": "비교 대상 불분명",
 "Insomnia Reading": "독서·측정 중의로 불분명", "Skydiving Duration": "기간 속성 지칭으로 제품명 부자연",
 "Acne Volume": "결합 불성립", "Snowboarding Template": "결합 불성립",
 "Ziplining Reply": "결합 불성립", "Psoriasis Account": "결합 불성립",
 "Sledding Validation": "결합 불성립", "Vertigo Lookup": "탐색 대상 불분명",
 "Diving Availability": "상태 명사로 제품명 부자연", "Arthritis Eligibility": "결합 불성립",
 "Sailing Appointment": "약속 대상 불분명", "Menopause Feedback": "결합 불성립",
 "Rafting Quote": "인용·견적 중의로 불분명", "Pregnancy Warranty": "결합 불성립",
 "Climbing Nomination": "결합 불성립", "Fertility Correction": "결합 불성립",
 "Biking Verification": "결합 불성립", "Thyroid Simulator": "결합 불성립",
 "Golf Review": "리뷰 대상 불분명", "Cholesterol Recipe": "결합 불성립",
 "Fishing Refund": "결합 불성립", "Hypertension Expense": "결합 불성립",
 "Camping Claim": "결합 불성립", "Anemia Onboarding": "결합 불성립",
 "Glamping Length": "결합 불성립(속성 지칭)", "Heartburn Weight": "결합 불성립(속성 지칭)",
 "Stargazing Limit": "결합 불성립", "Constipation Type": "결합 불성립(분류 대상 부자연)",
 "Birdwatching Speed": "결합 불성립", "Concussion Depth": "결합 불성립",
 "Canyon Width": "결합 불성립", "Sprain Temperature": "결합 불성립",
 "Geyser Pressure": "결합 불성립", "Fracture Load": "결합 불성립",
 "Fjord Voltage": "결합 불성립", "Insulin Wattage": "결합 불성립",
 "Savanna Brightness": "결합 불성립", "Tundra Frequency": "결합 불성립",
 "Prairie Compatibility": "상태 명사로 제품명 부자연", "Marsh Capacity": "상태 명사로 제품명 부자연",
 "Cove Usage": "사용 지칭으로 제품 불분명", "Cliff Condition": "상태 명사로 제품명 부자연",
 "Cavern Humidity": "결합 불성립", "Oasis Episode": "결합 불성립",
 "Dune Cycle": "주기 지칭으로 제품 불분명", "Whale Breakdown": "내역·고장 중의로 불분명",
 "Dolphin Sensor": "결합 불성립", "Penguin Reception": "리셉션·수신 중의로 불분명",
 "Flamingo Followup": "후속 지칭으로 제품 불분명", "Turtle Approval": "승인 지칭으로 제품 불분명",
 "Moose Matrix": "행렬·매트릭스 중의로 불분명", "Bison Evaluation": "평가 대상 불분명",
 "Reindeer Questionnaire": "설문 대상 불분명", "Watermark Workbook": "워크북 대상 불분명",
 "Seating Mode": "기능 토글로 읽혀 제품 불분명", "Skimmer Quantity": "수량 대상 불분명",
 "Buff Login": "제품 불분명", "Leak Analysis": "분석 대상 불분명",
 "Tour Coach": "코칭 대상 불분명", "Drum Habit": "결합 불성립",
 "Chargeback Mode": "기능 토글로 읽혀 제품 불분명", "Discovery Spec": "사양 참조로 제품 불분명",
 "Rider Analysis": "분석 대상 불분명", "Candidate Coach": "코칭 대상 불분명",
 "Warranty Habit": "결합 불성립", "Lawyer Checker": "검사 대상 불분명",
 "Attorney Barcode": "결합 불성립", "Court Clock": "결합 불성립",
 "Judge Guarantor": "보증인 명사 결합 불성립", "Dine Workbook": "워크북 대상 불분명",
 "Neuter Mode": "기능 토글로 읽혀 제품 불분명", "Whitening Spec": "사양 참조로 제품 불분명",
 "Diaper Quantity": "수량 대상 불분명", "Wardrobe Login": "제품 불분명",
 "Waxing Analysis": "분석 대상 불분명", "Syrup Coach": "코칭 대상 불분명",
 "Zoning Habit": "결합 불성립", "Jury Watch": "시계·감시 중의로 불분명",
 "Lawsuit Engine": "엔진 지칭으로 제품 불분명", "Divorce Form": "서식 대상 불분명",
 "Custody Voucher": "바우처 결합 불성립", "Immigration Value": "가치 지칭으로 제품 불분명",
 "Testament Graph": "그래프 지칭으로 제품 불분명", "Notary Streak": "앱 기능 지칭으로 제품 불분명",
 "Mediation Eligibility": "결합 불성립", "Guardianship Claim": "결합 불성립",
 "Trademark Humidity": "결합 불성립", "Patent Tournament": "결합 불성립",
 "Insulation Workbook": "워크북 대상 불분명", "Tutoring Mode": "기능 토글로 읽혀 제품 불분명",
 "Pothole Spec": "사양 참조로 제품 불분명", "Newsletter Quantity": "수량 대상 불분명",
 "Benefits Login": "제품 불분명", "Complaint Analysis": "분석 대상 불분명",
 "Bumper Coach": "코칭 대상 불분명", "Pastry Habit": "결합 불성립",
 "Copyright Signal": "신호 기능 지칭으로 제품 불분명", "Migraine Proposal": "제안 대상 불분명",
 "Insomnia Reference": "참조 대상 불분명", "Skydiving Volume": "결합 불성립",
 "Eczema Rating": "평가 대상 불분명", "Acne Diagnostic": "진단 대상 불분명",
 "Ziplining Account": "결합 불성립",
 "Psoriasis Case": "결합 불성립(Case 계열 기각 선례)", "Sledding Lookup": "탐색 대상 불분명",
 "Vertigo Ping": "결합 불성립", "Diving Eligibility": "결합 불성립",
 "Arthritis Broadcast": "결합 불성립", "Sailing Feedback": "결합 불성립",
 "Menopause Invoice": "결합 불성립", "Rafting Warranty": "결합 불성립",
 "Pregnancy Deposit": "결합 불성립", "Climbing Correction": "결합 불성립",
 "Fertility Revision": "결합 불성립", "Biking Simulator": "결합 불성립",
 "Thyroid Predictor": "예측 대상 불분명", "Golf Recipe": "결합 불성립",
 "Fishing Expense": "결합 불성립", "Hypertension Newsletter": "결합 불성립",
 "Camping Onboarding": "결합 불성립", "Anemia Checkin": "결합 불성립",
 "Glamping Weight": "결합 불성립(속성 지칭)", "Heartburn Distance": "결합 불성립",
 "Stargazing Type": "결합 불성립(분류 대상 부자연)", "Constipation Clock": "결합 불성립",
 "Birdwatching Depth": "결합 불성립", "Concussion Height": "결합 불성립",
 "Canyon Temperature": "결합 불성립", "Sprain Pressure": "결합 불성립",
 "Geyser Load": "결합 불성립", "Fracture Voltage": "결합 불성립",
 "Fjord Wattage": "결합 불성립", "Insulin Brightness": "결합 불성립",
 "Savanna Frequency": "결합 불성립", "Tundra Compatibility": "상태 명사로 제품명 부자연",
 "Prairie Capacity": "상태 명사로 제품명 부자연", "Marsh Usage": "사용 지칭으로 제품 불분명",
 "Cove Condition": "상태 명사로 제품명 부자연", "Cliff Humidity": "결합 불성립",
 "Cavern Episode": "결합 불성립", "Oasis Cycle": "주기 지칭으로 제품 불분명",
 "Dune Breakdown": "내역·고장 중의로 불분명", "Whale Sensor": "결합 불성립",
 "Dolphin Reception": "리셉션·수신 중의로 불분명", "Penguin Followup": "후속 지칭으로 제품 불분명",
 "Flamingo Approval": "승인 지칭으로 제품 불분명", "Turtle Matrix": "행렬·매트릭스 중의로 불분명",
 "Moose Evaluation": "평가 대상 불분명", "Bison Questionnaire": "설문 대상 불분명",
 "Reindeer Utilization": "활용 지칭으로 제품 불분명", "Packing Workbook": "워크북 대상 불분명",
 "Watermark Mode": "기능 토글로 읽혀 제품 불분명", "Seating Spec": "사양 참조로 제품 불분명",
 "Skimmer Login": "제품 불분명",
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
out = base + r"\_dec_c15.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
