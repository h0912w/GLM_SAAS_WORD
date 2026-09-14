# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk20_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Fleet App": (0.55, "차량 관제(플릿) 관리 앱(실재)"),
 "Fleet Tips": (0.55, "Fleet App 승인 선례의 Tips 평행"),
 "Savings App": (0.55, "저축 목표·예산 관리 앱(실재)"),
 "Savings Tips": (0.55, "Savings App 승인 선례의 Tips 평행"),
 "Conditioner App": (0.55, "에어컨 설치·점검 관리 앱(실재)"),
 "Conditioner Tips": (0.55, "Conditioner App 승인 선례의 Tips 평행"),
 "Incident App": (0.55, "사고·장애 보고 관리 앱(실재)"),
 "Playtime App": (0.55, "아이·반려동물 놀이 일정 기록 앱(실재)"),
 "Climbing Diary": (0.55, "클라이밍 등반 기록 일지(Camping Diary 평행)"),
 "Notary Deadline": (0.55, "공증 기한 관리(Deadline 절차 명사 선례 평행)"),
 "Custody Petition": (0.55, "양육권 신청 절차 관리(Patent Timetable 평행)"),
 "Lawsuit Calendar": (0.55, "소송 일정 캘린더(Judge Timetable 평행)"),
 "Testament Kit": (0.55, "유언장 작성 키트(실재)"),
 "Pickup Tips": (0.55, "Pickup App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Vent Advice": "직전 승인 Vent Tips와 동일 기능 의미 중복",
 "Forwarder Advice": "직전 승인 Forwarder Tips와 동일 기능 의미 중복",
 "Ductless Advice": "직전 승인 Ductless Tips와 동일 기능 의미 중복",
 "Pickup Advice": "이번 배치 승인 Pickup Tips와 동일 기능 의미 중복",
}

R = {
 "Drayage Coach": "코칭 대상 불분명", "Realtor Habit": "결합 불성립",
 "Copyright Base": "기반 지칭으로 제품 불분명", "Migraine Diagnostic": "진단 대상 불분명",
 "Insomnia Rating": "평가 대상 불분명", "Skydiving Case": "결합 불성립(Case 계열 기각 선례)",
 "Acne Match": "매칭·경기 중의로 불분명", "Snowboarding Model": "모델 지칭으로 제품 불분명",
 "Eczema Availability": "상태 명사로 제품명 부자연", "Ziplining Barcode": "결합 불성립",
 "Psoriasis Appointment": "약속 대상 불분명", "Sledding Renewal": "결합 불성립",
 "Vertigo Quote": "인용·견적 중의로 불분명", "Diving Certification": "결합 불성립",
 "Arthritis Nomination": "결합 불성립", "Sailing Payment": "결합 불성립",
 "Menopause Verification": "결합 불성립", "Rafting Seal": "결합 불성립",
 "Pregnancy Review": "리뷰 대상 불분명", "Fertility Refund": "결합 불성립",
 "Biking Inventory": "결합 불성립", "Thyroid Claim": "결합 불성립",
 "Golf Size": "결합 불성립(속성 지칭)", "Cholesterol Length": "결합 불성립(속성 지칭)",
 "Fishing Range": "결합 불성립", "Hypertension Limit": "결합 불성립",
 "Camping Time": "결합 불성립", "Anemia Speed": "결합 불성립",
 "Glamping Width": "결합 불성립", "Heartburn Temperature": "결합 불성립",
 "Stargazing Voltage": "결합 불성립", "Constipation Wattage": "결합 불성립",
 "Birdwatching Compatibility": "상태 명사로 제품명 부자연", "Concussion Capacity": "상태 명사로 제품명 부자연",
 "Canyon Condition": "상태 명사로 제품명 부자연", "Sprain Humidity": "결합 불성립",
 "Geyser Episode": "결합 불성립", "Fracture Cycle": "주기 지칭으로 제품 불분명",
 "Fjord Breakdown": "내역·고장 중의로 불분명", "Insulin Sensor": "결합 불성립",
 "Savanna Reception": "리셉션·수신 중의로 불분명", "Tundra Followup": "후속 지칭으로 제품 불분명",
 "Prairie Approval": "승인 지칭으로 제품 불분명", "Marsh Matrix": "행렬·매트릭스 중의로 불분명",
 "Cove Evaluation": "평가 대상 불분명", "Cliff Questionnaire": "설문 대상 불분명",
 "Cavern Utilization": "활용 지칭으로 제품 불분명", "Oasis Benefit": "혜택 지칭으로 제품 불분명",
 "Dune Requirement": "요건 지칭으로 제품 불분명", "Whale Depreciation": "결합 불성립",
 "Dolphin Resignation": "결합 불성립", "Penguin Hazard": "결합 불성립",
 "Flamingo Guarantor": "보증인 명사 결합 불성립", "Turtle Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Moose Tutorial": "동물 대상 결합 불성립", "Bison Handbook": "동물 대상 결합 불성립",
 "Reindeer Timetable": "동물 대상 결합 불성립", "Season Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Garment Workbook": "워크북 대상 불분명", "Membership Spec": "사양 참조로 제품 불분명",
 "Insurance Quantity": "수량 대상 불분명", "Customs Login": "제품 불분명",
 "Safety Coach": "코칭 대상 불분명", "Ductwork Habit": "결합 불성립",
 "Blast Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Rekeying Workbook": "워크북 대상 불분명",
 "Rental Quantity": "수량 대상 불분명", "Officiant Login": "제품 불분명",
 "Scratch Habit": "선례 기각(App 기각) 계열", "Lawyer Comparison": "비교 대상 불분명",
 "Attorney Revision": "결합 불성립", "Court Brightness": "결합 불성립",
 "Judge Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Showing Workbook": "워크북 대상 불분명", "Exclusion Mode": "선례 기각(App 기각) 계열",
 "Withholding Spec": "사양 참조로 제품 불분명", "Roofing Quantity": "수량 대상 불분명",
 "Minor Login": "선례 기각(App 기각) 계열", "Video Coach": "코칭 대상 불분명",
 "Survey Habit": "결합 불성립", "Jury Ledger": "장부 지칭으로 제품 불분명",
 "Divorce File": "파일·제출 중의로 불분명", "Immigration Attribute": "속성 지칭으로 제품 불분명",
 "Mediation Nomination": "결합 불성립", "Guardianship Time": "결합 불성립",
 "Trademark Utilization": "활용 지칭으로 제품 불분명", "Fob Workbook": "워크북 대상 불분명",
 "Fence Mode": "기능 토글로 읽혀 제품 불분명", "Hiking Spec": "사양 참조로 제품 불분명",
 "Chord Quantity": "수량 대상 불분명", "Test Login": "선례 기각(App 기각) 계열",
 "Foreclosure Analysis": "분석 대상 불분명", "Patent Coach": "코칭 대상 불분명",
 "Drayage Habit": "결합 불성립", "Copyright Core": "핵심 지칭으로 제품 불분명",
 "Migraine Progress": "진행 대상 불분명", "Insomnia Agreement": "결합 불성립",
 "Skydiving Match": "매칭·경기 중의로 불분명", "Acne Validation": "결합 불성립",
 "Snowboarding Availability": "상태 명사로 제품명 부자연", "Eczema Eligibility": "결합 불성립",
 "Ziplining Appointment": "약속 대상 불분명", "Psoriasis Feedback": "결합 불성립",
 "Sledding Quote": "인용·견적 중의로 불분명", "Vertigo Warranty": "결합 불성립",
 "Diving Nomination": "결합 불성립", "Arthritis Correction": "결합 불성립",
 "Sailing Verification": "결합 불성립", "Menopause Simulator": "결합 불성립",
 "Rafting Review": "리뷰 대상 불분명", "Pregnancy Recipe": "결합 불성립",
 "Climbing Refund": "결합 불성립", "Fertility Expense": "결합 불성립",
 "Biking Claim": "결합 불성립", "Thyroid Onboarding": "결합 불성립",
 "Golf Length": "결합 불성립(속성 지칭)", "Cholesterol Weight": "결합 불성립(속성 지칭)",
 "Fishing Limit": "결합 불성립", "Hypertension Type": "결합 불성립(분류 대상 부자연)",
 "Camping Speed": "결합 불성립", "Anemia Depth": "결합 불성립",
 "Glamping Temperature": "결합 불성립", "Heartburn Pressure": "결합 불성립",
 "Stargazing Wattage": "결합 불성립", "Constipation Brightness": "결합 불성립",
 "Birdwatching Capacity": "상태 명사로 제품명 부자연", "Concussion Usage": "사용 지칭으로 제품 불분명",
 "Canyon Humidity": "결합 불성립", "Sprain Episode": "결합 불성립",
 "Geyser Cycle": "주기 지칭으로 제품 불분명", "Fracture Breakdown": "내역·고장 중의로 불분명",
 "Fjord Sensor": "결합 불성립", "Insulin Reception": "리셉션·수신 중의로 불분명",
 "Savanna Followup": "후속 지칭으로 제품 불분명", "Tundra Approval": "승인 지칭으로 제품 불분명",
 "Prairie Matrix": "행렬·매트릭스 중의로 불분명", "Marsh Evaluation": "평가 대상 불분명",
 "Cove Questionnaire": "설문 대상 불분명", "Cliff Utilization": "활용 지칭으로 제품 불분명",
 "Cavern Benefit": "혜택 지칭으로 제품 불분명", "Oasis Requirement": "요건 지칭으로 제품 불분명",
 "Dune Depreciation": "결합 불성립", "Whale Resignation": "결합 불성립",
 "Dolphin Hazard": "결합 불성립", "Penguin Guarantor": "보증인 명사 결합 불성립",
 "Flamingo Tuner": "튜너 기능 지칭으로 제품 불분명", "Turtle Tutorial": "동물 대상 결합 불성립",
 "Moose Handbook": "동물 대상 결합 불성립", "Bison Timetable": "동물 대상 결합 불성립",
 "Reindeer Opinion": "동물 대상 결합 불성립", "Season Advice": "선례 기각(App 기각)의 Advice 불가",
 "Garment Mode": "기능 토글로 읽혀 제품 불분명", "Membership Quantity": "수량 대상 불분명",
 "Insurance Login": "제품 불분명", "Customs Analysis": "분석 대상 불분명",
 "Safety Habit": "결합 불성립", "Blast Advice": "선례 기각(App 기각)의 Advice 불가",
 "Vent Workbook": "워크북 대상 불분명", "Rekeying Mode": "기능 토글로 읽혀 제품 불분명",
 "Rental Login": "제품 불분명", "Officiant Analysis": "분석 대상 불분명",
 "Lawyer Proposal": "제안 대상 불분명", "Attorney Payment": "결합 불성립",
 "Court Frequency": "결합 불성립", "Judge Advice": "선례 기각(App 기각)의 Advice 불가",
 "Forwarder Workbook": "워크북 대상 불분명", "Showing Mode": "기능 토글로 읽혀 제품 불분명",
 "Exclusion Spec": "선례 기각(App 기각) 계열", "Withholding Quantity": "수량 대상 불분명",
 "Roofing Login": "제품 불분명", "Minor Analysis": "선례 기각(App 기각) 계열",
 "Video Habit": "결합 불성립", "Jury Board": "이사회·게시판 중의로 불분명",
 "Lawsuit Directory": "디렉터리 지칭으로 제품 불분명", "Divorce Level": "수준 지칭으로 제품 불분명",
 "Custody Confirmation": "확인 지칭으로 제품 불분명", "Immigration Field": "분야·필드 중의로 불분명",
 "Testament Count": "세다·개수 중의로 불분명", "Notary Duration": "기간 속성 지칭으로 제품명 부자연",
 "Mediation Correction": "결합 불성립", "Guardianship Speed": "결합 불성립",
 "Trademark Benefit": "혜택 지칭으로 제품 불분명", "Conditioner Workbook": "워크북 대상 불분명",
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
out = base + r"\_dec_c21.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
