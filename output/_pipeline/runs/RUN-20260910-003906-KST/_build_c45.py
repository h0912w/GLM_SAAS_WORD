# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk45_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Hypertension Guide": (0.55, "고혈압 관리 가이드(실재 콘텐츠)"),
 "Trade App": (0.55, "차량 트레이드인 앱(실재)"),
 "Mowing App": (0.65, "잔디 깎기 예약 앱(실재 시장)"),
 "Turnover Tips": (0.55, "턴오버 청소 팁(App→Tips 평행)"),
 "Diagnosis App": (0.65, "차량 진단 앱(OBD 실재 시장)"),
 "Waiter Tips": (0.55, "웨이터 업무 팁(App→Tips 평행)"),
 "Bloodwork App": (0.6, "반려동물 혈액검사 결과 앱(수의 랩 포털 실재)"),
 "Psoriasis Calculator": (0.55, "건선 PASI 점수 계산기(임상 도구 실재)"),
 "Fishing Guide": (0.55, "낚시 스팟 가이드(실재 콘텐츠)"),
 "Badge App": (0.6, "행사 명찰·QR 체크인 앱(실재)"),
 "Trade Tips": (0.55, "트레이드인 팁(App→Tips 평행)"),
 "Termite App": (0.55, "흰개미 점검 앱(실재)"),
 "Mowing Tips": (0.55, "잔디 관리 팁(App→Tips 평행)"),
 "Wifi App": (0.55, "행사장 와이파이 포털 앱(실재)"),
 "Diagnosis Tips": (0.55, "차량 진단 팁(App→Tips 평행)"),
 "Divorce Manager": (0.55, "이혼 절차 문서 관리(케이스 오거나이저 실재)"),
 "Custody Report": (0.55, "양육 일수 보고서(공동양육 앱 실재)"),
 "Trademark Review": (0.55, "상표 클리어런스 검토(실무 실재)"),
 "Bagel App": (0.6, "베이글 주문 앱(실재)"),
 "Bloodwork Tips": (0.55, "혈액검사 준비 팁(App→Tips 평행)"),
}
R_DUP = {
 "Fertility Record": "동일 배치 승인된 Fertility Recorder와 동일 기능 의미 중복",
 "Prescription Advice": "동일 배치 승인된 Prescription App/Tips와 동일 기능 의미 중복",
 "Intake Advice": "동일 배치 승인된 Intake App/Tips와 동일 기능 의미 중복",
 "Deworming Advice": "동일 배치 승인된 Deworming App/Tips와 동일 기능 의미 중복",
 "Potty Advice": "동일 배치 승인된 Potty App/Tips와 동일 기능 의미 중복",
 "Climbing Record": "동일 배치 승인된 Climbing Recorder와 동일 기능 의미 중복",
 "Turnover Advice": "동일 배치 승인된 Turnover App/Tips와 동일 기능 의미 중복",
 "Waiter Advice": "동일 배치 승인된 Waiter App/Tips와 동일 기능 의미 중복",
}
R = {
 "Biking Reference": "결합 불성립", "Thyroid Forecast": "결합 불성립",
 "Golf Volume": "결합 불성립", "Cholesterol Diagnostic": "진단 대상 불분명",
 "Fishing Template": "결합 불성립", "Camping Reply": "결합 불성립",
 "Anemia Account": "결합 불성립", "Glamping Validation": "결합 불성립",
 "Heartburn Lookup": "탐색 대상 불분명", "Stargazing Availability": "상태 명사로 제품명 부자연",
 "Constipation Eligibility": "결합 불성립", "Birdwatching Appointment": "약속 대상 불분명",
 "Concussion Feedback": "결합 불성립", "Canyon Renewal": "갱신 대상 불분명",
 "Sprain Quote": "인용·견적 중의로 대상 불분명", "Geyser Warranty": "결합 불성립",
 "Fracture Deposit": "결합 불성립", "Fjord Certification": "결합 불성립",
 "Insulin Nomination": "결합 불성립", "Savanna Correction": "결합 불성립",
 "Tundra Revision": "결합 불성립", "Prairie Payment": "결합 불성립",
 "Marsh Verification": "결합 불성립", "Cove Simulator": "결합 불성립",
 "Cliff Predictor": "예측 대상 불분명", "Cavern Seal": "결합 불성립",
 "Oasis Review": "결합 불성립", "Dune Recipe": "결합 불성립",
 "Whale Video": "결합 불성립", "Dolphin Diary": "결합 불성립",
 "Penguin Refund": "결합 불성립", "Flamingo Expense": "결합 불성립",
 "Turtle Newsletter": "결합 불성립", "Moose Inventory": "결합 불성립",
 "Bison Claim": "결합 불성립", "Reindeer Onboarding": "결합 불성립",
 "Treatment Workbook": "워크북 대상 불분명", "Billing Spec": "사양 참조로 제품 불분명",
 "Care Quantity": "수량 대상 불분명", "Contract Login": "제품 불분명",
 "Irrigation Analysis": "분석 대상 불분명", "Supply Coach": "코칭 대상 불분명",
 "Delivery Habit": "결합 불성립", "Mowing App SKIP": "",
 "Preplanning Workbook": "워크북 대상 불분명", "Schedule Mode": "기능 토글로 읽혀 제품 불분명",
 "Consultation Spec": "사양 참조로 제품 불분명", "Certification Login": "제품 불분명",
 "Reserve Analysis": "분석 대상 불분명", "Blower Coach": "코칭 대상 불분명",
 "Padlock Habit": "결합 불성립", "Lawyer Interest": "결합 불성립",
 "Attorney Guardian": "감시 대상 불분명", "Court Broadcast": "결합 불성립",
 "Judge Limit": "결합 불성립", "Jury Resignation": "결합 불성립",
 "Diagnosis App SKIP": "", "Flossing Workbook": "워크북 대상 불분명",
 "Storytime Mode": "기능 토글로 읽혀 제품 불분명", "Sofa Spec": "사양 참조로 제품 불분명",
 "Coloring Quantity": "수량 대상 불분명", "Ointment Login": "제품 불분명",
 "Humidifier Analysis": "분석 대상 불분명", "Combination Coach": "코칭 대상 불분명",
 "Vocabulary Habit": "결합 불성립", "Lawsuit Bridge": "결합 불성립",
 "Divorce Keeper": "결합 불성립", "Custody Roll": "결합 불성립",
 "Immigration Sample": "결합 불성립", "Testament Charge": "결합 불성립",
 "Notary Penalty": "결합 불성립", "Mediation Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Guardianship Reply": "결합 불성립", "Trademark Seal": "결합 불성립",
 "Patent Temperature": "결합 불성립", "Copyright Depreciation": "결합 불성립",
 "Bloodwork App SKIP": "", "Denture Tips": "팁 대상 불분명(Denture App 기각 선례)",
 "Trim Workbook": "워크북 대상 불분명", "Counseling Mode": "기능 토글로 읽혀 제품 불분명",
 "Capacitor Spec": "사양 참조로 제품 불분명", "Keyless Quantity": "수량 대상 불분명",
 "Clubhouse Login": "제품 불분명", "Skiing Analysis": "분석 대상 불분명",
 "Repertoire Coach": "코칭 대상 불분명", "Hospital Habit": "결합 불성립",
 "Migraine Trial": "결합 불성립", "Insomnia Diagram": "도식 대상 불분명",
 "Skydiving Outline": "개요 대상 불분명", "Acne Rendering": "결합 불성립",
 "Snowboarding Message": "결합 불성립", "Eczema Total": "결합 불성립",
 "Ziplining Announcement": "결합 불성립", "Sledding Recorder": "기록 대상 불분명",
 "Vertigo Estimator": "산출 대상 불분명", "Diving Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Arthritis Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Sailing Stage": "단계 대상 불분명",
 "Menopause Result": "결합 불성립", "Rafting Trend": "결합 불성립",
 "Pregnancy Comparison": "비교 대상 불분명", "Fertility Copy": "결합 불성립",
 "Biking Forecast": "결합 불성립", "Thyroid Deadline": "결합 불성립",
 "Golf Diagnostic": "진단 대상 불분명", "Cholesterol Progress": "진행 대상 불분명",
 "Hypertension Rating": "평가 대상 불분명", "Camping Account": "결합 불성립",
 "Anemia Case": "결합 불성립(Case 계열 기각 선례)", "Glamping Lookup": "탐색 대상 불분명",
 "Heartburn Ping": "결합 불성립", "Stargazing Eligibility": "결합 불성립",
 "Constipation Broadcast": "결합 불성립", "Birdwatching Feedback": "결합 불성립",
 "Concussion Invoice": "결합 불성립", "Canyon Quote": "인용·견적 중의로 대상 불분명",
 "Sprain Warranty": "결합 불성립", "Geyser Deposit": "결합 불성립",
 "Fracture Certification": "결합 불성립", "Fjord Nomination": "결합 불성립",
 "Insulin Correction": "결합 불성립", "Savanna Revision": "결합 불성립",
 "Tundra Payment": "결합 불성립", "Prairie Verification": "결합 불성립",
 "Marsh Simulator": "결합 불성립", "Cove Predictor": "예측 대상 불분명",
 "Cliff Seal": "결합 불성립", "Cavern Review": "결합 불성립",
 "Oasis Recipe": "결합 불성립", "Dune Video": "결합 불성립",
 "Whale Diary": "결합 불성립", "Dolphin Refund": "결합 불성립",
 "Penguin Expense": "결합 불성립", "Flamingo Newsletter": "결합 불성립",
 "Turtle Inventory": "결합 불성립", "Moose Claim": "결합 불성립",
 "Bison Onboarding": "결합 불성립", "Reindeer Checkin": "결합 불성립",
 "Badge App SKIP": "", "Treatment Mode": "기능 토글로 읽혀 제품 불분명",
 "Billing Quantity": "수량 대상 불분명", "Care Login": "제품 불분명",
 "Contract Analysis": "분석 대상 불분명", "Irrigation Coach": "코칭 대상 불분명",
 "Supply Habit": "결합 불성립", "Termite App SKIP": "",
 "Intake Workbook": "워크북 대상 불분명", "Preplanning Mode": "기능 토글로 읽혀 제품 불분명",
 "Schedule Spec": "사양 참조로 제품 불분명", "Consultation Quantity": "수량 대상 불분명",
 "Certification Analysis": "분석 대상 불분명", "Reserve Coach": "코칭 대상 불분명",
 "Blower Habit": "결합 불성립", "Lawyer Asset": "결합 불성립",
 "Attorney Helper": "도우미 대상 불분명(Biking Helper 기각 선례)", "Court Barcode": "결합 불성립",
 "Judge Type": "결합 불성립", "Jury Hazard": "결합 불성립",
 "Wifi App SKIP": "", "Deworming Workbook": "워크북 대상 불분명",
 "Flossing Mode": "기능 토글로 읽혀 제품 불분명", "Storytime Spec": "사양 참조로 제품 불분명",
 "Sofa Quantity": "수량 대상 불분명", "Coloring Login": "제품 불분명",
 "Ointment Analysis": "분석 대상 불분명", "Humidifier Coach": "코칭 대상 불분명",
 "Combination Habit": "결합 불성립", "Lawsuit Signal": "결합 불성립",
 "Immigration Slot": "결합 불성립", "Testament Duty": "결합 불성립",
 "Notary Markup": "마크업 대상 불분명", "Mediation Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Guardianship Account": "결합 불성립", "Patent Pressure": "결합 불성립",
 "Copyright Resignation": "결합 불성립", "Bagel App SKIP": "",
 "Denture Advice": "팁 대상 불분명(Denture App 기각 선례)",
 "Potty Workbook": "워크북 대상 불분명", "Trim Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c45.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
