# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk18_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Fence App": (0.55, "울타리 시공·견적 관리 앱(실재)"),
 "Fence Tips": (0.55, "Fence App 승인 선례의 Tips 평행"),
 "Garment App": (0.55, "의류 관리·수선 기록 앱(실재)"),
 "Rekeying App": (0.55, "자물쇠 재교체(리키잉) 관리 앱(실재)"),
 "Showing App": (0.55, "부동산 임장(쇼잉) 예약 관리 앱(실재)"),
 "Fob App": (0.55, "출입 키 포브 발급·관리 앱(실재)"),
 "Membership Tips": (0.55, "Membership App 승인 선례의 Tips 평행"),
 "Hiking Tips": (0.55, "Hiking App 승인 선례의 Tips 평행"),
 "Withholding Tips": (0.55, "Withholding App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Insurance Advice": "직전 승인 Insurance Tips와 동일 기능 의미 중복",
 "Rental Advice": "직전 승인 Rental Tips와 동일 기능 의미 중복",
 "Roofing Advice": "직전 승인 Roofing Tips와 동일 기능 의미 중복",
 "Chord Advice": "직전 승인 Chord Tips와 동일 기능 의미 중복",
 "Membership Advice": "이번 배치 승인 Membership Tips와 동일 기능 의미 중복",
 "Withholding Advice": "이번 배치 승인 Withholding Tips와 동일 기능 의미 중복",
 "Hiking Advice": "이번 배치 승인 Hiking Tips와 동일 기능 의미 중복",
}

R = {
 "Thyroid Refund": "결합 불성립", "Golf Inventory": "결합 불성립",
 "Cholesterol Claim": "결합 불성립", "Fishing Size": "결합 불성립(속성 지칭)",
 "Hypertension Length": "결합 불성립(속성 지칭)", "Camping Range": "결합 불성립",
 "Anemia Limit": "결합 불성립", "Glamping Time": "결합 불성립",
 "Heartburn Speed": "결합 불성립", "Stargazing Width": "결합 불성립",
 "Constipation Temperature": "결합 불성립", "Birdwatching Voltage": "결합 불성립",
 "Concussion Wattage": "결합 불성립", "Canyon Frequency": "결합 불성립",
 "Sprain Compatibility": "상태 명사로 제품명 부자연", "Geyser Capacity": "상태 명사로 제품명 부자연",
 "Fracture Usage": "사용 지칭으로 제품 불분명", "Fjord Condition": "상태 명사로 제품명 부자연",
 "Insulin Humidity": "결합 불성립", "Savanna Episode": "결합 불성립",
 "Tundra Cycle": "주기 지칭으로 제품 불분명", "Prairie Breakdown": "내역·고장 중의로 불분명",
 "Marsh Sensor": "결합 불성립", "Cove Reception": "리셉션·수신 중의로 불분명",
 "Cliff Followup": "후속 지칭으로 제품 불분명", "Cavern Approval": "승인 지칭으로 제품 불분명",
 "Oasis Matrix": "행렬·매트릭스 중의로 불분명", "Dune Evaluation": "평가 대상 불분명",
 "Whale Questionnaire": "설문 대상 불분명", "Dolphin Utilization": "활용 지칭으로 제품 불분명",
 "Penguin Benefit": "혜택 지칭으로 제품 불분명", "Flamingo Requirement": "요건 지칭으로 제품 불분명",
 "Turtle Depreciation": "결합 불성립", "Moose Resignation": "결합 불성립",
 "Bison Hazard": "결합 불성립", "Reindeer Guarantor": "보증인 명사 결합 불성립",
 "Customs Workbook": "워크북 대상 불분명", "Safety Spec": "사양 참조로 제품 불분명",
 "Ductwork Quantity": "수량 대상 불분명", "Lockout Login": "제품 불분명",
 "Turnaround Analysis": "분석 대상 불분명", "Packing Coach": "코칭 대상 불분명",
 "Watermark Habit": "결합 불성립", "Officiant Workbook": "워크북 대상 불분명",
 "Scratch Quantity": "선례 기각(App 기각) 계열", "Wrench Login": "제품 불분명",
 "Attraction Analysis": "분석 대상 불분명", "Trumpet Coach": "코칭 대상 불분명",
 "Lawyer Result": "결과 지칭으로 제품 불분명", "Attorney Deposit": "결합 불성립",
 "Court Pressure": "결합 불성립", "Judge Retreat": "물러남·수련 중의로 불분명",
 "Exclusion App": "배제 대상 불명으로 제품 불분명", "Minor Workbook": "선례 기각(App 기각) 계열",
 "Video Spec": "사양 참조로 제품 불분명", "Survey Quantity": "수량 대상 불분명",
 "Cover Login": "제품 불분명", "Recording Analysis": "분석 대상 불분명",
 "Dine Habit": "결합 불성립", "Jury Map": "지도 중의로 불분명",
 "Lawsuit Ops": "운영 약어로 제품 불분명", "Divorce Profile": "프로필 대상 불분명",
 "Custody Bulletin": "게시물 대상 불분명", "Immigration Rule": "규칙 지칭으로 제품 불분명",
 "Testament Sketch": "스케치 중의로 불분명", "Notary Copy": "복사·원고 중의로 불분명",
 "Mediation Quote": "인용·견적 중의로 불분명", "Guardianship Range": "결합 불성립",
 "Trademark Approval": "승인 지칭으로 제품 불분명", "Test Workbook": "선례 기각(App 기각) 계열",
 "Foreclosure Mode": "기능 토글로 읽혀 제품 불분명", "Patent Spec": "사양 참조로 제품 불분명",
 "Drayage Quantity": "수량 대상 불분명", "Realtor Login": "제품 불분명",
 "Carrier Analysis": "분석 대상 불분명", "Union Coach": "코칭 대상 불분명",
 "Insulation Habit": "결합 불성립", "Copyright Point": "점수 지칭으로 제품 불분명",
 "Migraine Deadline": "결합 불성립", "Insomnia Authorization": "결합 불성립",
 "Skydiving Agreement": "결합 불성립", "Acne Reply": "결합 불성립",
 "Snowboarding Validation": "결합 불성립", "Eczema Lookup": "탐색 대상 불분명",
 "Ziplining Availability": "상태 명사로 제품명 부자연", "Psoriasis Eligibility": "결합 불성립",
 "Sledding Appointment": "약속 대상 불분명", "Vertigo Feedback": "결합 불성립",
 "Diving Quote": "인용·견적 중의로 불분명", "Arthritis Warranty": "결합 불성립",
 "Sailing Nomination": "결합 불성립", "Menopause Correction": "결합 불성립",
 "Rafting Verification": "결합 불성립", "Pregnancy Simulator": "결합 불성립",
 "Climbing Review": "리뷰 대상 불분명", "Fertility Recipe": "결합 불성립",
 "Biking Refund": "결합 불성립", "Thyroid Expense": "결합 불성립",
 "Golf Claim": "결합 불성립", "Cholesterol Onboarding": "결합 불성립",
 "Fishing Length": "결합 불성립(속성 지칭)", "Hypertension Weight": "결합 불성립(속성 지칭)",
 "Camping Limit": "결합 불성립", "Anemia Type": "결합 불성립(분류 대상 부자연)",
 "Glamping Speed": "결합 불성립", "Heartburn Depth": "결합 불성립",
 "Stargazing Temperature": "결합 불성립", "Constipation Pressure": "결합 불성립",
 "Birdwatching Wattage": "결합 불성립", "Concussion Brightness": "결합 불성립",
 "Canyon Compatibility": "상태 명사로 제품명 부자연", "Sprain Capacity": "상태 명사로 제품명 부자연",
 "Geyser Usage": "사용 지칭으로 제품 불분명", "Fracture Condition": "상태 명사로 제품명 부자연",
 "Fjord Humidity": "결합 불성립", "Insulin Episode": "결합 불성립",
 "Savanna Cycle": "주기 지칭으로 제품 불분명", "Tundra Breakdown": "내역·고장 중의로 불분명",
 "Prairie Sensor": "결합 불성립", "Marsh Reception": "리셉션·수신 중의로 불분명",
 "Cove Followup": "후속 지칭으로 제품 불분명", "Cliff Approval": "승인 지칭으로 제품 불분명",
 "Cavern Matrix": "행렬·매트릭스 중의로 불분명", "Oasis Evaluation": "평가 대상 불분명",
 "Dune Questionnaire": "설문 대상 불분명", "Whale Utilization": "활용 지칭으로 제품 불분명",
 "Dolphin Benefit": "혜택 지칭으로 제품 불분명", "Penguin Requirement": "요건 지칭으로 제품 불분명",
 "Flamingo Depreciation": "결합 불성립", "Turtle Resignation": "결합 불성립",
 "Moose Hazard": "결합 불성립", "Bison Guarantor": "보증인 명사 결합 불성립",
 "Reindeer Tuner": "튜너 기능 지칭으로 제품 불분명", "Insurance Workbook": "워크북 대상 불분명",
 "Customs Mode": "기능 토글로 읽혀 제품 불분명", "Safety Quantity": "수량 대상 불분명",
 "Ductwork Login": "제품 불분명", "Lockout Analysis": "분석 대상 불분명",
 "Turnaround Coach": "코칭 대상 불분명", "Packing Habit": "결합 불성립",
 "Rental Workbook": "워크북 대상 불분명", "Officiant Mode": "기능 토글로 읽혀 제품 불분명",
 "Scratch Login": "선례 기각(App 기각) 계열", "Wrench Analysis": "분석 대상 불분명",
 "Attraction Coach": "코칭 대상 불분명", "Trumpet Habit": "결합 불성립",
 "Lawyer Streak": "앱 기능 지칭으로 제품 불분명", "Attorney Certification": "결합 불성립",
 "Court Load": "결합 불성립", "Judge Tournament": "결합 불성립",
 "Exclusion Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Roofing Workbook": "워크북 대상 불분명",
 "Minor Mode": "선례 기각(App 기각) 계열", "Video Quantity": "수량 대상 불분명",
 "Survey Login": "제품 불분명", "Cover Analysis": "분석 대상 불분명",
 "Recording Coach": "코칭 대상 불분명", "Jury Frame": "액자·틀 중의로 불분명",
 "Lawsuit Playbook": "플레이북 중의로 불분명", "Divorce Status": "상태 명사로 제품명 부자연",
 "Custody Brief": "요약서·소송 준비 중의로 불분명", "Immigration Detail": "세부 지칭으로 제품 불분명",
 "Testament Outline": "개요 지칭으로 제품 불분명", "Notary Reading": "독서·측정 중의로 불분명",
 "Mediation Warranty": "결합 불성립", "Guardianship Limit": "결합 불성립",
 "Trademark Matrix": "행렬·매트릭스 중의로 불분명", "Chord Workbook": "워크북 대상 불분명",
 "Test Mode": "선례 기각(App 기각) 계열", "Foreclosure Spec": "사양 참조로 제품 불분명",
 "Patent Quantity": "수량 대상 불분명", "Drayage Login": "제품 불분명",
 "Realtor Analysis": "분석 대상 불분명", "Carrier Coach": "코칭 대상 불분명",
 "Union Habit": "결합 불성립", "Copyright Map": "지도 중의로 불분명",
 "Migraine Duration": "기간 속성 지칭으로 제품명 부자연", "Insomnia Template": "결합 불성립",
 "Skydiving Reply": "결합 불성립", "Acne Account": "결합 불성립",
 "Snowboarding Lookup": "탐색 대상 불분명", "Eczema Ping": "결합 불성립",
 "Ziplining Eligibility": "결합 불성립", "Psoriasis Broadcast": "결합 불성립",
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
out = base + r"\_dec_c19.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
