# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk42_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Keyless App": (0.65, "키리스 스마트 잠금 앱(실재 시장)"),
 "Clubhouse Tips": (0.55, "클럽하우스 예약 팁(App→Tips 평행)"),
 "Ziplining Kit": (0.55, "지프라인 장비 키트(가정용 실재)"),
 "Pregnancy Helper": (0.55, "임신 주차 도우미(실재 앱)"),
 "Billing App": (0.7, "어린이집 청구 관리 앱(실재 시장)"),
 "Care Tips": (0.55, "케어 관리 팁(App→Tips 평행)"),
 "Consultation App": (0.6, "약사 상담 예약 앱(텔레팜러시 실재)"),
 "Container Tips": (0.55, "컨테이너 운송 팁(App→Tips 평행)"),
 "Coloring Tips": (0.55, "컬러 작업 팁(App→Tips 평행)"),
 "Keyless Tips": (0.55, "키리스 잠금 팁(App→Tips 평행)"),
 "Arthritis Recorder": (0.55, "관절 통증 기록(증상 트래커 실재)"),
 "Fertility Trend": (0.55, "배략 주기 추이(BBT 차트 실재)"),
 "Thyroid Record": (0.55, "갑상선 검사 기록(Hypertension Record 평행)"),
 "Anemia Guide": (0.55, "빈혈 관리 가이드(Constipation Guide 평행)"),
 "Billing Tips": (0.55, "청구 관리 팁(App→Tips 평행)"),
 "Schedule App": (0.65, "살롱 예약 스케줄 앱(실재 시장)"),
 "Consultation Tips": (0.55, "상담 준비 팁(App→Tips 평행)"),
}
R_DUP = {
 "Skiing Advice": "동일 배치 승인된 Skiing App/Tips와 동일 기능 의미 중복",
 "Contract Advice": "동일 배치 승인된 Contract App/Tips와 동일 기능 의미 중복",
 "Certification Advice": "동일 배치 승인된 Certification App/Tips와 동일 기능 의미 중복",
 "Clubhouse Advice": "동일 배치 승인된 Clubhouse App/Tips와 동일 기능 의미 중복",
 "Care Advice": "동일 배치 승인된 Care App/Tips와 동일 기능 의미 중복",
 "Container Advice": "동일 배치 승인된 Container App/Tips와 동일 기능 의미 중복",
}
R = {
 "Trademark Correction": "결합 불성립", "Patent Clock": "결합 불성립",
 "Copyright Matrix": "결합 불성립", "Hospital Mode": "기능 토글로 읽혀 제품 불분명",
 "Inheritance Spec": "사양 참조로 제품 불분명", "Bulk Quantity": "수량 대상 불분명",
 "Comparable Login": "제품 불분명", "Payout Analysis": "분석 대상 불분명",
 "Probation Coach": "코칭 대상 불분명", "Deck Habit": "결합 불성립",
 "Migraine Arrears": "결합 불성립", "Insomnia Extension": "연장 대상 불분명",
 "Skydiving Manual": "설명 대상 불분명(Ziplining Manual 기각 선례)", "Acne Worksheet": "워크시트 근거 약함",
 "Snowboarding Sketch": "제품성 불분명", "Eczema Outline": "개요 대상 불분명",
 "Psoriasis Count": "카운트 대상 불분명", "Sledding Widget": "결합 불성립",
 "Vertigo Repository": "결합 불성립", "Diving Converter": "변환 대상 불분명",
 "Arthritis Generator": "생성 대상 불분명", "Sailing Checker": "검사 대상 불분명",
 "Menopause Detector": "탐지 대상 불분명", "Rafting Guardian": "감시 대상 불분명",
 "Climbing Streak": "결합 불성립", "Fertility Rank": "결합 불성립",
 "Biking Proposal": "제안 대상 불분명", "Thyroid Guarantee": "결합 불성립",
 "Golf Reading": "결합 불성립", "Cholesterol Reference": "결합 불성립",
 "Fishing Duration": "결합 불성립", "Hypertension Volume": "결합 불성립",
 "Camping Authorization": "결합 불성립", "Anemia Template": "결합 불성립",
 "Glamping Agreement": "결합 불성립", "Heartburn Reply": "결합 불성립",
 "Stargazing Match": "결합 불성립(Match 계열 기각 선례)", "Constipation Validation": "결합 불성립",
 "Birdwatching Model": "결합 불성립", "Concussion Availability": "상태 명사로 제품명 부자연",
 "Canyon Broadcast": "결합 불성립", "Sprain Barcode": "결합 불성립",
 "Geyser Appointment": "약속 대상 불분명", "Fracture Feedback": "결합 불성립",
 "Fjord Invoice": "결합 불성립", "Insulin Renewal": "갱신 대상 불분명",
 "Savanna Quote": "인용·견적 중의로 대상 불분명", "Tundra Warranty": "결합 불성립",
 "Prairie Deposit": "결합 불성립", "Marsh Certification": "결합 불성립",
 "Cove Nomination": "결합 불성립", "Cliff Correction": "결합 불성립",
 "Cavern Revision": "결합 불성립", "Oasis Payment": "결합 불성립",
 "Dune Verification": "결합 불성립", "Whale Simulator": "결합 불성립",
 "Dolphin Predictor": "예측 대상 불분명", "Penguin Seal": "결합 불성립",
 "Flamingo Review": "결합 불성립", "Turtle Recipe": "결합 불성립",
 "Moose Video": "결합 불성립", "Bison Diary": "결합 불성립",
 "Reindeer Refund": "결합 불성립", "Billing App SKIP": "",
 "Irrigation Workbook": "워크북 대상 불분명", "Supply Mode": "기능 토글로 읽혀 제품 불분명",
 "Delivery Spec": "사양 참조로 제품 불분명", "Service Quantity": "수량 대상 불분명",
 "Retail Login": "제품 불분명", "Adherence Analysis": "분석 대상 불분명",
 "Berth Coach": "코칭 대상 불분명", "Consultation App SKIP": "",
 "Reserve Workbook": "워크북 대상 불분명", "Blower Mode": "기능 토글로 읽혀 제품 불분명",
 "Padlock Spec": "사양 참조로 제품 불분명", "Interpreter Quantity": "수량 대상 불분명",
 "Route Login": "제품 불분명", "Lighting Analysis": "분석 대상 불분명",
 "Favor Coach": "코칭 대상 불분명", "Occupant Habit": "결합 불성립",
 "Lawyer Serial": "결합 불성립", "Attorney Estimator": "산출 대상 불분명",
 "Court Lookup": "탐색 대상 불분명", "Judge Size": "결합 불성립",
 "Jury Questionnaire": "결합 불성립(문서명으로 제품 불분명)", "Sofa App": "",
 "Coloring Tips SKIP": "", "Ointment Advice": "팁 대상 불분명(Ointment App 기각 선례)",
 "Humidifier Workbook": "워크북 대상 불분명", "Combination Mode": "기능 토글로 읽혀 제품 불분명",
 "Vocabulary Spec": "사양 참조로 제품 불분명", "Reimbursement Quantity": "수량 대상 불분명",
 "License Login": "제품 불분명", "Registrar Analysis": "분석 대상 불분명",
 "Landscaping Coach": "코칭 대상 불분명", "Opening Habit": "결합 불성립",
 "Lawsuit Vault": "결합 불성립", "Divorce Chain": "결합 불성립",
 "Custody Passport": "결합 불성립", "Immigration Receipt": "결합 불성립",
 "Testament Sum": "결합 불성립", "Notary Due": "결합 불성립",
 "Mediation Generator": "생성 대상 불분명", "Guardianship Authorization": "결합 불성립",
 "Trademark Revision": "결합 불성립", "Patent Time": "결합 불성립",
 "Copyright Evaluation": "결합 불성립", "Capacitor App": "제품 불분명(부품명으로 제품 불분명)",
 "Keyless Tips SKIP": "", "Repertoire Workbook": "워크북 대상 불분명",
 "Skiing Workbook": "워크북 대상 불분명",
 "Repertoire Mode": "기능 토글로 읽혀 제품 불분명", "Hospital Spec": "사양 참조로 제품 불분명",
 "Inheritance Quantity": "수량 대상 불분명", "Bulk Login": "제품 불분명",
 "Comparable Analysis": "분석 대상 불분명", "Payout Coach": "코칭 대상 불분명",
 "Probation Habit": "결합 불성립", "Migraine Advance": "결합 불성립",
 "Insomnia Trial": "결합 불성립", "Skydiving Worksheet": "워크시트 근거 약함",
 "Acne Diagram": "도식 대상 불분명", "Snowboarding Outline": "개요 대상 불분명",
 "Eczema Rendering": "결합 불성립", "Ziplining Count": "카운트 대상 불분명",
 "Psoriasis Message": "메시지 대상 불분명", "Sledding Repository": "결합 불성립",
 "Vertigo Announcement": "결합 불성립", "Diving Generator": "생성 대상 불분명",
 "Sailing Detector": "탐지 대상 불분명", "Menopause Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Rafting Helper": "도우미 대상 불분명", "Pregnancy Stage": "단계 대상 불분명",
 "Climbing Rank": "결합 불성립", "Biking Guarantee": "결합 불성립",
 "Golf Reference": "결합 불성립", "Cholesterol Forecast": "결합 불성립",
 "Fishing Volume": "결합 불성립", "Hypertension Diagnostic": "진단 대상 불분명",
 "Camping Template": "결합 불성립", "Glamping Reply": "결합 불성립",
 "Heartburn Account": "결합 불성립", "Stargazing Validation": "결합 불성립",
 "Constipation Lookup": "탐색 대상 불분명", "Birdwatching Availability": "상태 명사로 제품명 부자연",
 "Concussion Eligibility": "결합 불성립", "Canyon Barcode": "결합 불성립",
 "Sprain Appointment": "약속 대상 불분명", "Geyser Feedback": "결합 불성립",
 "Fracture Invoice": "결합 불성립", "Fjord Renewal": "갱신 대상 불분명",
 "Insulin Quote": "인용·견적 중의로 대상 불분명", "Savanna Warranty": "결합 불성립",
 "Tundra Deposit": "결합 불성립", "Prairie Certification": "결합 불성립",
 "Marsh Nomination": "결합 불성립", "Cove Correction": "결합 불성립",
 "Cliff Revision": "결합 불성립", "Cavern Payment": "결합 불성립",
 "Oasis Verification": "결합 불성립", "Dune Simulator": "결합 불성립",
 "Whale Predictor": "예측 대상 불분명", "Dolphin Seal": "결합 불성립",
 "Penguin Review": "결합 불성립", "Flamingo Recipe": "결합 불성립",
 "Turtle Video": "결합 불성립", "Moose Diary": "결합 불성립",
 "Bison Refund": "결합 불성립", "Reindeer Expense": "결합 불성립",
 "Contract Workbook": "워크북 대상 불분명", "Irrigation Mode": "기능 토글로 읽혀 제품 불분명",
 "Supply Spec": "사양 참조로 제품 불분명", "Delivery Quantity": "수량 대상 불분명",
 "Service Login": "제품 불분명", "Retail Analysis": "분석 대상 불분명",
 "Adherence Coach": "코칭 대상 불분명", "Berth Habit": "결합 불성립",
 "Schedule App SKIP": "", "Certification Workbook": "워크북 대상 불분명",
 "Reserve Mode": "기능 토글로 읽혀 제품 불분명", "Blower Spec": "사양 참조로 제품 불분명",
 "Padlock Quantity": "수량 대상 불분명",
}
R["Sofa App"] = (0.55, "소파 클리닝 예약 앱(실재 서비스)")
A["Sofa App"] = R.pop("Sofa App")
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
out = base + r"\_dec_c42.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
