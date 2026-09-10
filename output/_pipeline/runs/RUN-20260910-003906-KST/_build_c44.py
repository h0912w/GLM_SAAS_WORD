# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk44_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Prescription App": (0.6, "수의 처방 관리 앱(실재)"),
 "Treatment Tips": (0.55, "치료 관리 팁(App→Tips 평행)"),
 "Intake App": (0.6, "고객 접수 인테이크 앱(실재)"),
 "Preplanning Tips": (0.55, "장례 사전 계획 팁(App→Tips 평행)"),
 "Deworming App": (0.55, "구충 스케줄 알림 앱(반려동물 관리 실재)"),
 "Flossing Tips": (0.55, "치실 사용 팁(App→Tips 평행)"),
 "Potty App": (0.65, "배변 훈련 앱(실재 시장)"),
 "Trim Tips": (0.55, "트리밍 예약 팁(App→Tips 평행)"),
 "Insomnia Manual": (0.55, "수면 개선 매뉴얼(CBT-I 자료 실재)"),
 "Snowboarding Kit": (0.55, "스노보드 장비 키트(Climbing Kit 평행)"),
 "Menopause Helper": (0.55, "폐경 증상 도우미(Calculator/Recorder 평행)"),
 "Prescription Tips": (0.55, "처방 관리 팁(App→Tips 평행)"),
 "Turnover App": (0.6, "숙소 턴오버 청소 스케줄 앱(실재)"),
 "Intake Tips": (0.55, "인테이크 운영 팁(App→Tips 평행)"),
 "Waiter App": (0.6, "웨이터 주문 보조 앱(실재)"),
 "Deworming Tips": (0.55, "구충 관리 팁(App→Tips 평행)"),
 "Potty Tips": (0.55, "배변 훈련 팁(App→Tips 평행)"),
 "Vertigo Recorder": (0.55, "어지럼증 발작 기록(임상 일지 실재)"),
}
R_DUP = {
 "Schedule Advice": "동일 배치 승인된 Schedule App/Tips와 동일 기능 의미 중복",
 "Storytime Advice": "동일 배치 승인된 Storytime App/Tips와 동일 기능 의미 중복",
 "Counseling Advice": "동일 배치 승인된 Counseling App/Tips와 동일 기능 의미 중복",
 "Treatment Advice": "동일 배치 승인된 Treatment App/Tips와 동일 기능 의미 중복",
 "Preplanning Advice": "동일 배치 승인된 Preplanning App/Tips와 동일 기능 의미 중복",
 "Flossing Advice": "동일 배치 승인된 Flossing App/Tips와 동일 기능 의미 중복",
 "Trim Advice": "동일 배치 승인된 Trim App/Tips와 동일 기능 의미 중복",
}
R = {
 "Cavern Simulator": "결합 불성립", "Oasis Predictor": "예측 대상 불분명",
 "Dune Seal": "결합 불성립", "Whale Review": "결합 불성립",
 "Dolphin Recipe": "결합 불성립", "Penguin Video": "결합 불성립",
 "Flamingo Diary": "결합 불성립", "Turtle Refund": "결합 불성립",
 "Moose Expense": "결합 불성립", "Bison Newsletter": "결합 불성립",
 "Reindeer Inventory": "결합 불성립", "Billing Workbook": "워크북 대상 불분명",
 "Care Mode": "기능 토글로 읽혀 제품 불분명", "Contract Spec": "사양 참조로 제품 불분명",
 "Irrigation Quantity": "수량 대상 불분명", "Supply Login": "제품 불분명",
 "Delivery Analysis": "분석 대상 불분명", "Service Coach": "코칭 대상 불분명",
 "Retail Habit": "결합 불성립", "Consultation Workbook": "워크북 대상 불분명",
 "Container Mode": "기능 토글로 읽혀 제품 불분명", "Certification Spec": "사양 참조로 제품 불분명",
 "Reserve Quantity": "수량 대상 불분명", "Blower Login": "제품 불분명",
 "Padlock Analysis": "분석 대상 불분명", "Interpreter Coach": "코칭 대상 불분명",
 "Route Habit": "결합 불성립", "Lawyer Marker": "표식 대상 불분명",
 "Attorney Timer": "결합 불성립(Timer 계열 기각 선례)", "Court Availability": "상태 명사로 제품명 부자연",
 "Judge Distance": "결합 불성립", "Jury Requirement": "결합 불성립",
 "Sofa Workbook": "워크북 대상 불분명", "Coloring Mode": "기능 토글로 읽혀 제품 불분명",
 "Ointment Spec": "사양 참조로 제품 불분명", "Humidifier Quantity": "수량 대상 불분명",
 "Combination Login": "제품 불분명", "Vocabulary Analysis": "분석 대상 불분명",
 "Reimbursement Coach": "코칭 대상 불분명", "License Habit": "결합 불성립",
 "Lawsuit Forge": "결합 불성립", "Divorce Nexus": "결합 불성립",
 "Custody Line": "결합 불성립", "Immigration Table": "결합 불성립",
 "Testament Cash": "결합 불성립", "Notary Arrears": "결합 불성립",
 "Mediation Checker": "검사 대상 불분명", "Guardianship Rating": "평가 대상 불분명",
 "Trademark Simulator": "결합 불성립", "Patent Height": "결합 불성립",
 "Copyright Benefit": "결합 불성립", "Potty App SKIP": "",
 "Capacitor Workbook": "워크북 대상 불분명", "Keyless Mode": "기능 토글로 읽혀 제품 불분명",
 "Clubhouse Spec": "사양 참조로 제품 불분명", "Skiing Quantity": "수량 대상 불분명",
 "Repertoire Login": "제품 불분명", "Hospital Analysis": "분석 대상 불분명",
 "Inheritance Coach": "코칭 대상 불분명", "Bulk Habit": "결합 불성립",
 "Migraine Redemption": "결합 불성립", "Skydiving Layout": "결합 불성립",
 "Acne Sketch": "제품성 불분명", "Eczema Count": "카운트 대상 불분명",
 "Ziplining Widget": "결합 불성립", "Psoriasis Repository": "결합 불성립",
 "Sledding Converter": "변환 대상 불분명", "Vertigo Generator": "생성 대상 불분명",
 "Diving Checker": "검사 대상 불분명(Climbing Checker 기각 선례)", "Arthritis Detector": "탐지 대상 불분명",
 "Sailing Guardian": "감시 대상 불분명", "Rafting Streak": "결합 불성립",
 "Pregnancy Rank": "결합 불성립", "Climbing Proposal": "제안 대상 불분명",
 "Fertility Guarantee": "결합 불성립", "Biking Reading": "결합 불성립",
 "Thyroid Reference": "결합 불성립", "Golf Duration": "결합 불성립",
 "Cholesterol Volume": "결합 불성립", "Fishing Authorization": "결합 불성립",
 "Hypertension Template": "결합 불성립", "Camping Agreement": "결합 불성립",
 "Anemia Reply": "결합 불성립", "Glamping Match": "결합 불성립(Match 계열 기각 선례)",
 "Heartburn Validation": "결합 불성립", "Stargazing Model": "결합 불성립",
 "Constipation Availability": "상태 명사로 제품명 부자연", "Birdwatching Barcode": "결합 불성립",
 "Concussion Appointment": "약속 대상 불분명", "Canyon Invoice": "결합 불성립",
 "Sprain Renewal": "갱신 대상 불분명", "Geyser Quote": "인용·견적 중의로 대상 불분명",
 "Fracture Warranty": "결합 불성립", "Fjord Deposit": "결합 불성립",
 "Insulin Certification": "결합 불성립", "Savanna Nomination": "결합 불성립",
 "Tundra Correction": "결합 불성립", "Prairie Revision": "결합 불성립",
 "Marsh Payment": "결합 불성립", "Cove Verification": "결합 불성립",
 "Cliff Simulator": "결합 불성립", "Cavern Predictor": "예측 대상 불분명",
 "Oasis Seal": "결합 불성립", "Dune Review": "결합 불성립",
 "Whale Recipe": "결합 불성립", "Dolphin Video": "결합 불성립",
 "Penguin Diary": "결합 불성립", "Flamingo Refund": "결합 불성립",
 "Turtle Expense": "결합 불성립", "Moose Newsletter": "결합 불성립",
 "Bison Inventory": "결합 불성립", "Reindeer Claim": "결합 불성립",
 "Billing Mode": "기능 토글로 읽혀 제품 불분명", "Care Spec": "사양 참조로 제품 불분명",
 "Contract Quantity": "수량 대상 불분명", "Irrigation Login": "제품 불분명",
 "Supply Analysis": "분석 대상 불분명", "Delivery Coach": "코칭 대상 불분명",
 "Service Habit": "결합 불성립", "Schedule Workbook": "워크북 대상 불분명",
 "Consultation Mode": "기능 토글로 읽혀 제품 불분명", "Container Spec": "사양 참조로 제품 불분명",
 "Certification Quantity": "수량 대상 불분명", "Reserve Login": "제품 불분명",
 "Blower Analysis": "분석 대상 불분명", "Padlock Coach": "코칭 대상 불분명",
 "Interpreter Habit": "결합 불성립", "Lawyer Balance": "결합 불성립",
 "Attorney Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Court Eligibility": "결합 불성립",
 "Judge Range": "결합 불성립", "Jury Depreciation": "결합 불성립",
 "Waiter App SKIP": "", "Storytime Workbook": "워크북 대상 불분명",
 "Sofa Mode": "기능 토글로 읽혀 제품 불분명", "Coloring Spec": "사양 참조로 제품 불분명",
 "Ointment Quantity": "수량 대상 불분명", "Humidifier Login": "제품 불분명",
 "Combination Analysis": "분석 대상 불분명", "Vocabulary Coach": "코칭 대상 불분명",
 "Reimbursement Habit": "결합 불성립", "Lawsuit Cascade": "결합 불성립",
 "Divorce Atlas": "결합 불성립", "Custody Window": "결합 불성립",
 "Immigration Slip": "결합 불성립", "Testament Sale": "결합 불성립",
 "Notary Advance": "결합 불성립", "Mediation Detector": "탐지 대상 불분명",
 "Guardianship Agreement": "결합 불성립", "Trademark Predictor": "예측 대상 불분명",
 "Patent Width": "결합 불성립", "Copyright Requirement": "결합 불성립",
 "Denture App": "제품 불분명(틀니 단독 앱 카테고리 약함)", "Counseling Workbook": "워크북 대상 불분명",
 "Capacitor Mode": "기능 토글로 읽혀 제품 불분명", "Keyless Spec": "사양 참조로 제품 불분명",
 "Clubhouse Quantity": "수량 대상 불분명", "Skiing Login": "제품 불분명",
 "Repertoire Analysis": "분석 대상 불분명", "Hospital Coach": "코칭 대상 불분명",
 "Inheritance Habit": "결합 불성립", "Migraine Extension": "연장 대상 불분명",
 "Insomnia Worksheet": "워크시트 근거 약함", "Skydiving Sketch": "제품성 불분명",
 "Acne Outline": "개요 대상 불분명", "Snowboarding Count": "카운트 대상 불분명",
 "Eczema Message": "메시지 대상 불분명", "Ziplining Repository": "결합 불성립",
 "Psoriasis Announcement": "결합 불성립", "Sledding Generator": "생성 대상 불분명",
 "Diving Detector": "탐지 대상 불분명", "Arthritis Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Sailing Helper": "도우미 대상 불분명(Biking Helper 기각 선례)", "Menopause Stage": "단계 대상 불분명",
 "Rafting Rank": "결합 불성립", "Pregnancy Trend": "결합 불성립(추이 대상 불분명)",
 "Climbing Guarantee": "결합 불성립",
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
out = base + r"\_dec_c44.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
