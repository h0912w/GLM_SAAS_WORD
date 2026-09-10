# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk48_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Nutrition Tips": (0.55, "영양 관리 팁(App→Tips 평행)"),
 "Jury Handbook": (0.55, "배심원 안내 핸드북(법원 배심원 안내서 실재)"),
 "Resident App": (0.6, "시민 주민 서비스 앱(시정 앱 실재)"),
 "Photo Tips": (0.55, "사진 촬영 팁(App→Tips 평행)"),
 "Divorce Scheduler": (0.55, "이혼 일정 스케줄러(Divorce Planner 평행)"),
 "Author App": (0.6, "저자 집필 도구 앱(실재 시장)"),
 "Threat Tips": (0.55, "위협 대응 팁(App→Tips 평행)"),
 "Elective App": (0.55, "학교 선택과목 신청 앱(코스 선택 시스템 실재)"),
 "Resident Tips": (0.55, "주민 서비스 팁(App→Tips 평행)"),
 "Copyright Handbook": (0.55, "저작권 핸드북(실재 서적 카테고리)"),
 "Curfew App": (0.55, "귀가 시간 관리 앱(부모 관리 앱 실재)"),
 "Author Tips": (0.55, "집필 팁(App→Tips 평행)"),
 "Vertigo Helper": (0.55, "어지럼증 관리 도우미(Menopause Helper 평행)"),
}
R_DUP = {
 "Naptime Advice": "동일 배치 승인된 Naptime App/Tips와 동일 기능 의미 중복",
 "Rating Advice": "동일 배치 승인된 Rating App/Tips와 동일 기능 의미 중복",
 "Notice Advice": "동일 배치 승인된 Notice App/Tips와 동일 기능 의미 중복",
 "Provisioning Advice": "동일 배치 승인된 Provisioning App/Tips와 동일 기능 의미 중복",
 "Nutrition Advice": "동일 배치 승인된 Nutrition App/Tips와 동일 기능 의미 중복",
 "Photo Advice": "동일 배치 승인된 Photo App/Tips와 동일 기능 의미 중복",
}
R = {
 "Billing Habit": "결합 불성립", "Staffing Workbook": "워크북 대상 불분명",
 "Termite Mode": "기능 토글로 읽혀 제품 불분명", "Mowing Spec": "사양 참조로 제품 불분명",
 "Turnover Quantity": "수량 대상 불분명", "Intake Login": "제품 불분명",
 "Preplanning Analysis": "분석 대상 불분명", "Schedule Coach": "코칭 대상 불분명",
 "Consultation Habit": "결합 불성립", "Lawyer Discount": "판촉 계열 기각 선례(Notary Discount)",
 "Attorney Rank": "결합 불성립", "Court Renewal": "갱신 대상 불분명",
 "Judge Depth": "결합 불성립", "Resident App SKIP": "",
 "Interviewer Workbook": "워크북 대상 불분명", "Wifi Mode": "기능 토글로 읽혀 제품 불분명",
 "Diagnosis Spec": "사양 참조로 제품 불분명", "Waiter Quantity": "수량 대상 불분명",
 "Deworming Login": "제품 불분명", "Flossing Analysis": "분석 대상 불분명",
 "Storytime Coach": "코칭 대상 불분명", "Sofa Habit": "결합 불성립",
 "Lawsuit Grid": "결합 불성립", "Custody Sheet": "결합 불성립(양식 단독으로 제품 불분명, Custody Form 기각 선례)",
 "Immigration Stub": "결합 불성립", "Testament Stake": "결합 불성립",
 "Notary Graph": "그래프 대상 불분명", "Mediation Result": "결합 불성립",
 "Guardianship Lookup": "탐색 대상 불분명", "Trademark Refund": "결합 불성립",
 "Patent Brightness": "결합 불성립", "Copyright Tutorial": "결합 불성립(Tutorial 계열 기각 선례)",
 "Author App SKIP": "", "Exhaust Workbook": "워크북 대상 불분명",
 "Bagel Mode": "기능 토글로 읽혀 제품 불분명", "Bloodwork Spec": "사양 참조로 제품 불분명",
 "Denture Quantity": "수량 대상 불분명", "Potty Login": "제품 불분명",
 "Trim Analysis": "분석 대상 불분명", "Counseling Coach": "코칭 대상 불분명",
 "Capacitor Habit": "결합 불성립", "Migraine Diagram": "도식 대상 불분명",
 "Insomnia Rendering": "결합 불성립", "Skydiving Message": "결합 불성립",
 "Acne Total": "결합 불성립", "Snowboarding Calculator": "계산 대상 불분명(Rafting Calculator 기각 선례)",
 "Eczema Converter": "변환 대상 불분명", "Ziplining Estimator": "산출 대상 불분명",
 "Psoriasis Checker": "검사 대상 불분명(Climbing Checker 기각 선례)", "Sledding Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Vertigo Guardian": "감시 대상 불분명", "Diving Result": "결합 불성립",
 "Arthritis Streak": "결합 불성립", "Sailing Comparison": "비교 대상 불분명",
 "Menopause Proposal": "제안 대상 불분명", "Rafting Copy": "결합 불성립",
 "Pregnancy Reading": "수치 대상 불분명(Anemia Reading 기각 선례)", "Climbing Deadline": "결합 불성립",
 "Fertility Duration": "결합 불성립", "Biking Progress": "진행 대상 불분명",
 "Thyroid Authorization": "결합 불성립", "Golf Rating": "평가 대상 불분명",
 "Cholesterol Agreement": "결합 불성립", "Fishing Case": "결합 불성립(Case 계열 기각 선례)",
 "Hypertension Match": "결합 불성립(Match 계열 기각 선례)", "Camping Ping": "결합 불성립",
 "Anemia Model": "결합 불성립", "Glamping Broadcast": "결합 불성립",
 "Heartburn Barcode": "결합 불성립", "Stargazing Invoice": "결합 불성립",
 "Constipation Renewal": "갱신 대상 불분명", "Birdwatching Deposit": "결합 불성립",
 "Concussion Certification": "결합 불성립", "Canyon Correction": "결합 불성립",
 "Sprain Revision": "결합 불성립", "Geyser Payment": "결합 불성립",
 "Fracture Verification": "결합 불성립", "Fjord Simulator": "결합 불성립",
 "Insulin Predictor": "예측 대상 불분명", "Savanna Seal": "결합 불성립",
 "Tundra Review": "결합 불성립", "Prairie Recipe": "결합 불성립",
 "Marsh Video": "결합 불성립", "Cove Diary": "결합 불성립",
 "Cliff Refund": "결합 불성립", "Cavern Expense": "결합 불성립",
 "Oasis Newsletter": "결합 불성립", "Dune Inventory": "결합 불성립",
 "Whale Claim": "결합 불성립", "Dolphin Onboarding": "결합 불성립",
 "Penguin Checkin": "결합 불성립", "Flamingo Size": "결합 불성립",
 "Turtle Length": "결합 불성립", "Moose Weight": "결합 불성립",
 "Bison Distance": "결합 불성립", "Reindeer Range": "결합 불성립",
 "Threat Tips SKIP": "", "Queue Workbook": "워크북 대상 불분명",
 "Sourcing Mode": "기능 토글로 읽혀 제품 불분명", "Badge Spec": "사양 참조로 제품 불분명",
 "Trade Quantity": "수량 대상 불분명", "Treatment Coach": "코칭 대상 불분명",
 "Naptime Workbook": "워크북 대상 불분명", "Staffing Mode": "기능 토글로 읽혀 제품 불분명",
 "Termite Spec": "사양 참조로 제품 불분명", "Mowing Quantity": "수량 대상 불분명",
 "Turnover Login": "제품 불분명", "Intake Analysis": "분석 대상 불분명",
 "Preplanning Coach": "코칭 대상 불분명", "Schedule Habit": "결합 불성립",
 "Lawyer Arrears": "결합 불성립", "Attorney Trend": "결합 불성립",
 "Court Quote": "인용·견적 중의로 대상 불분명", "Judge Height": "결합 불성립",
 "Jury Timetable": "결합 불성립", "Elective App SKIP": "",
 "Rating Workbook": "워크북 대상 불분명", "Interviewer Mode": "기능 토글로 읽혀 제품 불분명",
 "Wifi Spec": "사양 참조로 제품 불분명", "Diagnosis Quantity": "수량 대상 불분명",
 "Waiter Login": "제품 불분명", "Deworming Analysis": "분석 대상 불분명",
 "Flossing Coach": "코칭 대상 불분명", "Storytime Habit": "결합 불성립",
 "Lawsuit Wave": "결합 불성립", "Divorce Monitor": "결합 불성립(감시 대상 불분명)",
 "Custody Check": "검사 대상 불분명", "Immigration Statement": "결합 불성립",
 "Testament Margin": "결합 불성립", "Notary Label": "결합 불성립",
 "Mediation Streak": "결합 불성립", "Guardianship Ping": "결합 불성립",
 "Trademark Expense": "결합 불성립", "Patent Frequency": "결합 불성립",
 "Copyright Handbook SKIP": "", "Curfew App SKIP": "",
 "Notice Workbook": "워크북 대상 불분명", "Exhaust Mode": "기능 토글로 읽혀 제품 불분명",
 "Bagel Spec": "사양 참조로 제품 불분명", "Bloodwork Quantity": "수량 대상 불분명",
 "Denture Login": "제품 불분명", "Potty Analysis": "분석 대상 불분명",
 "Trim Coach": "코칭 대상 불분명", "Counseling Habit": "결합 불성립",
 "Migraine Schematic": "도식 대상 불분명", "Insomnia Notification": "알림 내용 불특정",
 "Skydiving Total": "결합 불성립", "Acne Widget": "결합 불성립",
 "Snowboarding Converter": "변환 대상 불분명", "Eczema Generator": "생성 대상 불분명",
 "Ziplining Checker": "검사 대상 불분명", "Psoriasis Detector": "탐지 대상 불분명",
 "Sledding Guardian": "감시 대상 불분명", "Diving Streak": "결합 불성립",
 "Arthritis Rank": "결합 불성립", "Sailing Proposal": "제안 대상 불분명",
 "Menopause Guarantee": "결합 불성립", "Rafting Reading": "결합 불성립(Reading 계열 기각 선례)",
 "Pregnancy Reference": "결합 불성립", "Climbing Duration": "결합 불성립",
 "Fertility Volume": "결합 불성립", "Biking Authorization": "결합 불성립",
 "Thyroid Template": "결합 불성립", "Golf Agreement": "결합 불성립",
 "Cholesterol Reply": "결합 불성립", "Fishing Match": "결합 불성립(Match 계열 기각 선례)",
 "Hypertension Validation": "결합 불성립", "Camping Model": "결합 불성립",
 "Anemia Availability": "상태 명사로 제품명 부자연", "Glamping Barcode": "결합 불성립",
 "Heartburn Appointment": "약속 대상 불분명", "Stargazing Renewal": "갱신 대상 불분명",
 "Constipation Quote": "인용·견적 중의로 대상 불분명", "Birdwatching Certification": "결합 불성립",
 "Concussion Nomination": "결합 불성립", "Canyon Revision": "결합 불성립",
 "Sprain Payment": "결합 불성립", "Geyser Verification": "결합 불성립",
 "Fracture Simulator": "결합 불성립", "Fjord Predictor": "예측 대상 불분명",
 "Insulin Seal": "결합 불성립", "Savanna Review": "결합 불성립",
 "Tundra Recipe": "결합 불성립", "Prairie Video": "결합 불성립",
 "Marsh Diary": "결합 불성립", "Cove Refund": "결합 불성립",
 "Cliff Expense": "결합 불성립",
}
for k in [k for k in R if k.endswith(" SKIP")]:
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
out = base + r"\_dec_c48.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
