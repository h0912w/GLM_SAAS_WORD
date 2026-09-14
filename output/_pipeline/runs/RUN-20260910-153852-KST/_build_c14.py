# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk13_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Insulation App": (0.55, "단열 시공·점검 관리 앱(실재)"),
 "Insulation Tips": (0.55, "Insulation App 승인 선례의 Tips 평행"),
 "Tutoring Tips": (0.55, "Tutoring App 승인 선례의 Tips 평행"),
 "Packing App": (0.55, "여행 짐 싸기 체크리스트 앱(실재)"),
 "Packing Tips": (0.55, "Packing App 승인 선례의 Tips 평행"),
 "Watermark Tips": (0.55, "Watermark App 승인 선례의 Tips 평행"),
 "Trumpet App": (0.55, "트럼펫 레슨·연습 앱(실재)"),
 "Trumpet Tips": (0.55, "Trumpet App 승인 선례의 Tips 평행"),
 "Dine Tips": (0.55, "Dine App 승인 선례의 Tips 평행"),
 "Union App": (0.6, "노조 회원·협상 관리 앱(실재)"),
 "Turnaround App": (0.55, "경영 회생 프로젝트 관리 앱(실재)"),
 "Attraction App": (0.55, "관광 명소 티켓·안내 앱(실재)"),
 "Recording App": (0.55, "회의·음성 녹음 관리 앱(실재)"),
 "Fishing Video": (0.55, "낚시 기법 영상 가이드(Camping Video 평행)"),
 "Fishing Diary": (0.55, "조황 기록 일지(catch log 실재)"),
 "Hypertension Diary": (0.55, "혈압 기록 일지(실재)"),
 "Insomnia Record": (0.55, "수면 기록(Vertigo Record 평행)"),
}

R_DUP = {
 "Tutoring Advice": "직전 승인 Tutoring Tips와 동일 기능 의미 중복",
 "Pothole Advice": "직전 승인 Pothole Tips와 동일 기능 의미 중복",
 "Watermark Advice": "이번 배치 승인 Watermark Tips와 동일 기능 의미 중복",
 "Seating Advice": "직전 승인 Seating Tips와 동일 기능 의미 중복",
 "Chargeback Advice": "직전 승인 Chargeback Tips와 동일 기능 의미 중복",
 "Neuter Advice": "직전 승인 Neuter Tips와 동일 기능 의미 중복",
 "Dine Advice": "이번 배치 승인 Dine Tips와 동일 기능 의미 중복",
}

R = {
 "Newsletter Workbook": "워크북 대상 불분명", "Benefits Mode": "기능 토글로 읽혀 제품 불분명",
 "Complaint Spec": "사양 참조로 제품 불분명", "Bumper Quantity": "수량 대상 불분명",
 "Pastry Login": "제품 불분명", "Anesthesia Coach": "코칭 대상 불분명",
 "Fieldtrip Habit": "결합 불성립", "Copyright Forge": "용광로 중의로 불분명",
 "Migraine Rank": "순위 대상 불분명", "Skydiving Forecast": "예측 대상 불분명",
 "Acne Deadline": "결합 불성립", "Snowboarding Progress": "진행 대상 불분명",
 "Eczema Authorization": "결합 불성립", "Ziplining Rating": "평가 대상 불분명",
 "Psoriasis Agreement": "결합 불성립", "Sledding Case": "결합 불성립(Case 계열 기각 선례)",
 "Vertigo Match": "매칭 대상 불분명", "Diving Ping": "결합 불성립",
 "Arthritis Model": "모델 지칭으로 제품 불분명", "Sailing Broadcast": "결합 불성립",
 "Menopause Barcode": "결합 불성립", "Rafting Invoice": "결합 불성립",
 "Pregnancy Renewal": "결합 불성립", "Climbing Deposit": "결합 불성립",
 "Fertility Certification": "결합 불성립", "Biking Revision": "결합 불성립",
 "Thyroid Payment": "결합 불성립", "Golf Predictor": "예측 대상 불분명",
 "Cholesterol Seal": "결합 불성립", "Camping Newsletter": "결합 불성립",
 "Anemia Inventory": "결합 불성립", "Glamping Checkin": "결합 불성립",
 "Heartburn Size": "결합 불성립(속성 지칭)", "Stargazing Distance": "결합 불성립",
 "Constipation Range": "결합 불성립", "Birdwatching Clock": "결합 불성립",
 "Concussion Time": "결합 불성립", "Canyon Depth": "결합 불성립",
 "Sprain Height": "결합 불성립", "Geyser Width": "결합 불성립",
 "Fracture Temperature": "결합 불성립", "Fjord Pressure": "결합 불성립",
 "Insulin Load": "결합 불성립", "Savanna Voltage": "결합 불성립",
 "Tundra Wattage": "결합 불성립", "Prairie Brightness": "결합 불성립",
 "Marsh Frequency": "결합 불성립", "Cove Compatibility": "상태 명사로 제품명 부자연",
 "Cliff Capacity": "상태 명사로 제품명 부자연", "Cavern Usage": "사용 지칭으로 제품 불분명",
 "Oasis Condition": "상태 명사로 제품명 부자연", "Dune Humidity": "결합 불성립",
 "Whale Episode": "결합 불성립", "Dolphin Cycle": "주기 지칭으로 제품 불분명",
 "Penguin Breakdown": "내역·고장 중의로 불분명", "Flamingo Sensor": "결합 불성립",
 "Turtle Reception": "리셉션·수신 중의로 불분명", "Moose Followup": "후속 지칭으로 제품 불분명",
 "Bison Approval": "승인 지칭으로 제품 불분명", "Reindeer Matrix": "행렬·매트릭스 중의로 불분명",
 "Skimmer Mode": "기능 토글로 읽혀 제품 불분명", "Buff Spec": "사양 참조로 제품 불분명",
 "Leak Quantity": "수량 대상 불분명", "Tour Login": "제품 불분명",
 "Drum Analysis": "분석 대상 불분명", "Provider Coach": "코칭 대상 불분명",
 "Discovery Workbook": "워크북 대상 불분명", "Rider Quantity": "수량 대상 불분명",
 "Candidate Login": "제품 불분명", "Warranty Analysis": "분석 대상 불분명",
 "Restock Coach": "코칭 대상 불분명", "Shuttle Habit": "결합 불성립",
 "Lawyer Recorder": "기록 대상 불분명", "Attorney Eligibility": "결합 불성립",
 "Court Limit": "결합 불성립", "Judge Resignation": "결합 불성립",
 "Whitening Workbook": "워크북 대상 불분명", "Diaper Mode": "기능 토글로 읽혀 제품 불분명",
 "Wardrobe Spec": "사양 참조로 제품 불분명", "Waxing Quantity": "수량 대상 불분명",
 "Syrup Login": "제품 불분명", "Zoning Analysis": "분석 대상 불분명",
 "Bolt Coach": "코칭 대상 불분명", "Linguist Habit": "결합 불성립",
 "Jury Bridge": "다리 중의로 불분명", "Lawsuit Keeper": "관리인 중의로 불분명",
 "Divorce Report": "보고서 대상 불분명", "Custody Slot": "슬롯 지칭으로 제품 불분명",
 "Immigration Allowance": "결합 불성립", "Testament Extension": "연장 지칭으로 제품 불분명",
 "Notary Stage": "단계 대상 불분명", "Mediation Model": "모델 지칭으로 제품 불분명",
 "Guardianship Newsletter": "결합 불성립", "Trademark Usage": "사용 지칭으로 제품 불분명",
 "Patent Gift": "결합 불성립", "Pothole Workbook": "워크북 대상 불분명",
 "Newsletter Mode": "기능 토글로 읽혀 제품 불분명", "Benefits Spec": "사양 참조로 제품 불분명",
 "Complaint Quantity": "수량 대상 불분명", "Bumper Login": "제품 불분명",
 "Pastry Analysis": "분석 대상 불분명", "Anesthesia Habit": "결합 불성립",
 "Copyright Cascade": "폭포·연쇄 중의로 불분명", "Migraine Trend": "결합 불성립",
 "Insomnia Copy": "복사·원고 중의로 불분명", "Skydiving Deadline": "결합 불성립",
 "Acne Duration": "기간 속성 지칭으로 제품명 부자연", "Snowboarding Authorization": "결합 불성립",
 "Eczema Template": "결합 불성립", "Ziplining Agreement": "결합 불성립",
 "Psoriasis Reply": "결합 불성립", "Sledding Match": "매칭·경기 중의로 불분명",
 "Vertigo Validation": "결합 불성립", "Diving Model": "모델 지칭으로 제품 불분명",
 "Arthritis Availability": "상태 명사로 제품명 부자연", "Sailing Barcode": "결합 불성립",
 "Menopause Appointment": "약속 대상 불분명", "Rafting Renewal": "결합 불성립",
 "Pregnancy Quote": "인용·견적 중의로 불분명", "Climbing Certification": "결합 불성립",
 "Fertility Nomination": "결합 불성립", "Biking Payment": "결합 불성립",
 "Thyroid Verification": "결합 불성립", "Golf Seal": "결합 불성립",
 "Cholesterol Review": "리뷰 대상 불분명", "Hypertension Refund": "결합 불성립",
 "Camping Inventory": "결합 불성립", "Anemia Claim": "결합 불성립",
 "Glamping Size": "결합 불성립(속성 지칭)", "Heartburn Length": "결합 불성립(속성 지칭)",
 "Stargazing Range": "결합 불성립", "Constipation Limit": "결합 불성립",
 "Birdwatching Time": "결합 불성립", "Concussion Speed": "결합 불성립",
 "Canyon Height": "결합 불성립", "Sprain Width": "결합 불성립",
 "Geyser Temperature": "결합 불성립", "Fracture Pressure": "결합 불성립",
 "Fjord Load": "결합 불성립", "Insulin Voltage": "결합 불성립",
 "Savanna Wattage": "결합 불성립", "Tundra Brightness": "결합 불성립",
 "Prairie Frequency": "결합 불성립", "Marsh Compatibility": "상태 명사로 제품명 부자연",
 "Cove Capacity": "상태 명사로 제품명 부자연", "Cliff Usage": "사용 지칭으로 제품 불분명",
 "Cavern Condition": "상태 명사로 제품명 부자연", "Oasis Humidity": "결합 불성립",
 "Dune Episode": "결합 불성립", "Whale Cycle": "주기 지칭으로 제품 불분명",
 "Dolphin Breakdown": "내역·고장 중의로 불분명", "Penguin Sensor": "결합 불성립",
 "Flamingo Reception": "리셉션·수신 중의로 불분명", "Turtle Followup": "후속 지칭으로 제품 불분명",
 "Moose Approval": "승인 지칭으로 제품 불분명", "Bison Matrix": "행렬·매트릭스 중의로 불분명",
 "Reindeer Evaluation": "평가 대상 불분명", "Seating Workbook": "워크북 대상 불분명",
 "Skimmer Spec": "사양 참조로 제품 불분명", "Buff Quantity": "수량 대상 불분명",
 "Leak Login": "제품 불분명", "Tour Analysis": "분석 대상 불분명",
 "Drum Coach": "코칭 대상 불분명", "Provider Habit": "결합 불성립",
 "Chargeback Workbook": "워크북 대상 불분명", "Discovery Mode": "기능 토글로 읽혀 제품 불분명",
 "Rider Login": "제품 불분명", "Candidate Analysis": "분석 대상 불분명",
 "Warranty Coach": "코칭 대상 불분명", "Restock Habit": "결합 불성립",
 "Lawyer Estimator": "산출 대상 불분명", "Attorney Broadcast": "결합 불성립",
 "Court Type": "결합 불성립(분류 대상 부자연)", "Judge Hazard": "결합 불성립",
 "Neuter Workbook": "워크북 대상 불분명", "Whitening Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c14.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
