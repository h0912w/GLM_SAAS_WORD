# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk29_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Assessment App": (0.55, "역량·성과 평가 시행 관리 앱(실재)"),
 "Assessment Tips": (0.55, "Assessment App 승인 선례의 Tips 평행"),
 "Snack App": (0.55, "간식 주문·재고 관리 앱(실재)"),
 "Snack Tips": (0.55, "Snack App 승인 선례의 Tips 평행"),
 "Installment App": (0.55, "할부 결제 일정 관리 앱(실재)"),
 "Installment Tips": (0.55, "Installment App 승인 선례의 Tips 평행"),
 "Campaign App": (0.55, "마케팅 캠페인 운영 관리 앱(실재)"),
 "Knowledge App": (0.55, "지식 베이스 구축·관리 앱(실재)"),
 "Braces App": (0.55, "치아 교정 착용·관리 앱(실재)"),
 "Visit App": (0.55, "방문 일정·기록 관리 앱(실재)"),
 "Trademark Tips": (0.55, "Trademark App 승인 선례의 Tips 평행"),
 "Catering Tips": (0.55, "Catering App 승인 선례의 Tips 평행"),
 "Curtain Tips": (0.55, "Curtain App 승인 선례의 Tips 평행"),
 "Psoriasis Video": (0.55, "건선 관리 영상 가이드(Hypertension Video 평행)"),
 "Psoriasis Diary": (0.55, "건선 증상 기록 일지(Hypertension Diary 평행)"),
 "Ziplining Video": (0.55, "짚라인 강습 영상(Golf Video 평행)"),
}

R_DUP = {
 "Facial Advice": "직전 승인 Facial Tips와 동일 기능 의미 중복",
 "Attribution Advice": "직전 승인 Attribution Tips와 동일 기능 의미 중복",
 "Catering Advice": "이번 배치 승인 Catering Tips와 동일 기능 의미 중복",
 "Curtain Advice": "이번 배치 승인 Curtain Tips와 동일 기능 의미 중복",
 "Trademark Advice": "이번 배치 승인 Trademark Tips와 동일 기능 의미 중복",
 "Crossdock Advice": "직전 승인 Crossdock Tips와 동일 기능 의미 중복",
}

R = {
 "Bandwidth Mode": "선례 기각(App 기각) 계열", "Credential Spec": "사양 참조로 제품 불분명",
 "Backup Quantity": "수량 대상 불분명", "Satisfaction Login": "제품 불분명",
 "Offer Analysis": "분석 대상 불분명", "Sponsor Coach": "코칭 대상 불분명",
 "Sterilization Spec": "사양 참조로 제품 불분명", "Program Quantity": "선례 기각(App 기각) 계열",
 "Meal Login": "제품 불분명", "Lawyer Agreement": "계약서 문서 지칭으로 제품 불분명(Notary Agreement 기각 선례)",
 "Attorney Size": "결합 불성립(속성 지칭)", "Court Utilization": "활용 지칭으로 제품 불분명",
 "Curtain Tips2": "", "Tablet Workbook": "선례 기각(App 기각) 계열",
 "Freon Mode": "선례 기각(App 상표 기각) 계열", "Hinge Spec": "선례 기각(App 상표 기각) 계열",
 "Apostille Quantity": "수량 대상 불분명", "Invite Coach": "코칭 대상 불분명",
 "Judge Compass": "선례 기각(App 기각) 계열", "Jury Ring": "반지·링 중의로 불분명",
 "Lawsuit Ticker": "전광판·틱커 지칭으로 제품 불분명", "Divorce Table": "표·테이블 중의로 불분명",
 "Custody Sale": "판매 결합 불성립", "Immigration Markup": "마크업(가격·언어) 중의로 불분명",
 "Testament Helper": "도우미 지칭으로 제품 불분명", "Notary Model": "모델 지칭으로 제품 불분명",
 "Mediation Onboarding": "결합 불성립", "Guardianship Episode": "결합 불성립",
 "Crossdock Advice2": "", "Valuation Workbook": "워크북 대상 불분명",
 "Broker Mode": "기능 토글로 읽혀 제품 불분명", "Grievance Spec": "사양 참조로 제품 불분명",
 "Paving Quantity": "수량 대상 불분명", "Suspension Login": "제품 불분명",
 "Streetlight Analysis": "분석 대상 불분명", "Publisher Coach": "코칭 대상 불분명",
 "Salary Habit": "결합 불성립", "Patent Loop": "루프 기능 지칭으로 제품 불분명",
 "Copyright Chain": "사슬·체인점 중의로 불분명", "Migraine Barcode": "결합 불성립",
 "Insomnia Quote": "인용·견적 중의로 불분명", "Skydiving Nomination": "결합 불성립",
 "Acne Correction": "결합 불성립", "Snowboarding Simulator": "결합 불성립",
 "Eczema Predictor": "예측 대상 불분명", "Ziplining Recipe": "결합 불성립",
 "Sledding Expense": "결합 불성립", "Vertigo Newsletter": "결합 불성립",
 "Diving Onboarding": "결합 불성립", "Arthritis Checkin": "결합 불성립",
 "Sailing Weight": "결합 불성립(속성 지칭)", "Menopause Distance": "결합 불성립",
 "Rafting Type": "결합 불성립(분류 대상 부자연)", "Pregnancy Clock": "결합 불성립",
 "Climbing Depth": "결합 불성립", "Fertility Height": "결합 불성립",
 "Biking Pressure": "결합 불성립", "Thyroid Load": "결합 불성립",
 "Golf Brightness": "결합 불성립", "Cholesterol Frequency": "결합 불성립",
 "Fishing Usage": "사용 지칭으로 제품 불분명", "Hypertension Condition": "상태 명사로 제품명 부자연",
 "Camping Cycle": "주기 지칭으로 제품 불분명", "Anemia Breakdown": "내역·고장 중의로 불분명",
 "Glamping Followup": "후속 지칭으로 제품 불분명", "Heartburn Approval": "승인 지칭으로 제품 불분명",
 "Stargazing Questionnaire": "설문 대상 불분명", "Constipation Utilization": "활용 지칭으로 제품 불분명",
 "Birdwatching Depreciation": "결합 불성립", "Concussion Resignation": "결합 불성립",
 "Canyon Guarantor": "보증인 명사 결합 불성립", "Sprain Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Geyser Tutorial": "terrain 대상 결합 불성립", "Fracture Handbook": "terrain 대상 결합 불성립",
 "Fjord Timetable": "terrain 대상 결합 불성립", "Insulin Opinion": "terrain 대상 결합 불성립",
 "Savanna Gift": "결합 불성립", "Tundra Retreat": "terrain 대상 결합 불성립",
 "Prairie Tournament": "terrain 대상 결합 불성립", "Marsh Flyer": "terrain 대상 결합 불성립",
 "Cove App": "지명 지칭으로 제품 불분명", "Cliff Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Cavern Advice": "선례 기각(App 기각) 계열", "Oasis Workbook": "선례 기각(App 기각) 계열",
 "Dune Mode": "선례 기각(App 기각) 계열", "Whale Spec": "선례 기각(App 기각) 계열",
 "Dolphin Quantity": "선례 기각(App 기각) 계열", "Penguin Login": "선례 기각(App 기각) 계열",
 "Flamingo Analysis": "선례 기각(App 기각) 계열", "Turtle Coach": "선례 기각(App 기각) 계열",
 "Moose Habit": "선례 기각(App 기각) 계열", "Bison Tracker": "선례 기각(App 기각) 계열",
 "Reindeer Flow": "선례 기각(App 기각) 계열", "Syndication Workbook": "워크북 대상 불분명",
 "Bandwidth Spec": "선례 기각(App 기각) 계열", "Credential Quantity": "수량 대상 불분명",
 "Backup Login": "제품 불분명", "Satisfaction Analysis": "분석 대상 불분명",
 "Offer Coach": "코칭 대상 불분명", "Sponsor Habit": "결합 불성립",
 "Sterilization Quantity": "수량 대상 불분명",
 "Program Login": "선례 기각(App 기각) 계열",
 "Meal Analysis": "분석 대상 불분명",
 "Lawyer Reply": "결합 불성립", "Attorney Length": "결합 불성립(속성 지칭)",
 "Court Benefit": "혜택 지칭으로 제품 불분명", "Snack Tips2": "",
 "Facial Workbook": "워크북 대상 불분명", "Tablet Mode": "선례 기각(App 기각) 계열",
 "Freon Spec": "선례 기각(App 상표 기각) 계열", "Hinge Quantity": "선례 기각(App 상표 기각) 계열",
 "Apostille Login": "제품 불분명", "Invite Habit": "결합 불성립",
 "Judge Beacon": "선례 기각(App 기각) 계열", "Jury Gate": "게이트 지칭으로 제품 불분명",
 "Lawsuit Line": "전화선·라인 중의로 불분명", "Divorce Slip": "전표·미끄러짐 중의로 불분명",
 "Custody Charge": "요금·충전 중의로 불분명", "Immigration Redemption": "속죄·상환 중의로 불분명",
 "Testament Stage": "단계·무대 중의로 불분명", "Notary Availability": "상태 명사로 제품명 부자연",
 "Mediation Checkin": "결합 불성립", "Guardianship Cycle": "주기 지칭으로 제품 불분명",
 "Installment Tips2": "", "Crossdock Workbook": "워크북 대상 불분명",
 "Valuation Mode": "기능 토글로 읽혀 제품 불분명", "Broker Spec": "사양 참조로 제품 불분명",
 "Grievance Quantity": "수량 대상 불분명", "Paving Login": "제품 불분명",
 "Suspension Analysis": "분석 대상 불분명", "Streetlight Coach": "코칭 대상 불분명",
 "Publisher Habit": "결합 불성립", "Patent Grid": "그리드 지칭으로 제품 불분명",
 "Copyright Ring": "반지·링 중의로 불분명", "Migraine Appointment": "약속 대상 불분명",
 "Insomnia Warranty": "결합 불성립", "Skydiving Correction": "결합 불성립",
 "Acne Revision": "결합 불성립", "Snowboarding Predictor": "예측 대상 불분명",
 "Eczema Seal": "결합 불성립", "Sledding Newsletter": "결합 불성립",
 "Vertigo Inventory": "결합 불성립", "Diving Checkin": "결합 불성립",
 "Arthritis Size": "결합 불성립(속성 지칭)", "Sailing Distance": "결합 불성립",
 "Menopause Range": "결합 불성립", "Rafting Clock": "결합 불성립",
 "Pregnancy Time": "결합 불성립", "Climbing Height": "결합 불성립",
 "Fertility Width": "결합 불성립", "Biking Load": "결합 불성립",
 "Thyroid Voltage": "결합 불성립", "Golf Frequency": "결합 불성립",
 "Cholesterol Compatibility": "상태 명사로 제품명 부자연", "Fishing Condition": "상태 명사로 제품명 부자연",
 "Hypertension Humidity": "결합 불성립", "Camping Breakdown": "내역·고장 중의로 불분명",
 "Anemia Sensor": "결합 불성립", "Glamping Approval": "승인 지칭으로 제품 불분명",
 "Heartburn Matrix": "행렬·매트릭스 중의로 불분명", "Stargazing Utilization": "활용 지칭으로 제품 불분명",
 "Constipation Benefit": "혜택 지칭으로 제품 불분명", "Birdwatching Resignation": "결합 불성립",
 "Concussion Hazard": "결합 불성립", "Canyon Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Sprain Tutorial": "terrain 대상 결합 불성립", "Geyser Handbook": "terrain 대상 결합 불성립",
 "Fracture Timetable": "terrain 대상 결합 불성립", "Fjord Opinion": "terrain 대상 결합 불성립",
 "Insulin Gift": "결합 불성립", "Savanna Retreat": "terrain 대상 결합 불성립",
 "Tundra Tournament": "terrain 대상 결합 불성립", "Prairie Flyer": "terrain 대상 결합 불성립",
 "Marsh App": "지명 지칭으로 제품 불분명", "Cove Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Cliff Advice": "선례 기각(App 기각) 계열", "Cavern Workbook": "선례 기각(App 기각) 계열",
 "Oasis Mode": "선례 기각(App 기각) 계열", "Dune Spec": "선례 기각(App 기각) 계열",
 "Whale Quantity": "선례 기각(App 기각) 계열", "Dolphin Login": "선례 기각(App 기각) 계열",
 "Penguin Analysis": "선례 기각(App 기각) 계열",
}
del R["Curtain Tips2"]
del R["Crossdock Advice2"]
del R["Snack Tips2"]
del R["Installment Tips2"]
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
out = base + r"\_dec_c30.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
