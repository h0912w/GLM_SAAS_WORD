# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk13_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Waiver Tips": (0.55, "면책 동의서 작성 팁(App→Tips 평행)"),
 "Memorial App": (0.6, "추모·기념 페이지 앱(실재 카테고리)"),
 "Checkout Tips": (0.55, "결제 운영 팁(App→Tips 평행)"),
 "Chassis App": (0.55, "섀시 트레일러 관리 앱(물류 실재)"),
 "Amendment Tips": (0.55, "계약 수정 팁(App→Tips 평행)"),
 "Neighborhood App": (0.6, "동네 정보 커뮤니티 앱(실재 카테고리)"),
 "Litigation Tips": (0.55, "소송 대응 팁(App→Tips 평행)"),
 "Appointment App": (0.6, "동물병원 예약 앱(실재 카테고리)"),
 "Alteration App": (0.55, "의류 수선 관리 앱(실재)"),
 "Memorial Tips": (0.55, "추모 서비스 팁(App→Tips 평행)"),
 "Divorce App": (0.55, "이혼 절차 관리 앱(실재)"),
 "Chassis Tips": (0.55, "섀시 운영 팁(App→Tips 평행)"),
}
R_DUP = {
 "Immunization Advice": "동일 배치 승인된 Immunization App/Tips와 동일 기능 의미 중복",
 "Recall Advice": "동일 배치 승인된 Recall App/Tips와 동일 기능 의미 중복",
 "Salvage Advice": "동일 배치 승인된 Salvage App/Tips와 동일 기능 의미 중복",
 "Dependent Advice": "동일 배치 승인된 Dependent App/Tips와 동일 기능 의미 중복",
 "Waiver Advice": "동일 배치 승인된 Waiver App/Tips와 동일 기능 의미 중복",
 "Checkout Advice": "동일 배치 승인된 Checkout App/Tips와 동일 기능 의미 중복",
 "Amendment Advice": "동일 배치 승인된 Amendment App/Tips와 동일 기능 의미 중복",
}
R = {
 "Sledding Sale": "결합 불성립", "Vertigo Charge": "결합 불성립",
 "Diving Tariff": "결합 불성립", "Arthritis Value": "결합 불성립",
 "Sailing Fine": "결합 불성립", "Menopause Number": "수치 지칭 부자연",
 "Rafting Rule": "결합 불성립", "Pregnancy Detail": "결합 불성립",
 "Climbing Attribute": "결합 불성립", "Fertility Field": "결합 불성립",
 "Biking Token": "결합 불성립", "Thyroid Signature": "결합 불성립",
 "Golf Interest": "결합 불성립", "Cholesterol Asset": "결합 불성립",
 "Fishing Subsidy": "결합 불성립", "Hypertension Discount": "결합 불성립",
 "Camping Penalty": "결합 불성립", "Anemia Markup": "결합 불성립",
 "Glamping Trial": "결합 불성립", "Heartburn Graph": "그래프 대상 불분명",
 "Stargazing Worksheet": "학습지 근거 약함", "Constipation Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Birdwatching Sketch": "제품성 불분명", "Concussion Outline": "제품성 불분명",
 "Canyon Notification": "결합 불성립", "Sprain Kit": "키트 대상 불분명",
 "Geyser Count": "대상 불분명", "Fracture Message": "결합 불성립",
 "Fjord Total": "결합 불성립", "Insulin Widget": "위젯 대상 불분명",
 "Savanna Repository": "결합 불성립", "Tundra Announcement": "결합 불성립",
 "Prairie Calculator": "계산 대상 불분명", "Marsh Converter": "변환 대상 불분명",
 "Cove Generator": "생성 대상 불분명", "Cliff Recorder": "기록 대상 불분명",
 "Cavern Estimator": "산출 대상 불분명", "Oasis Checker": "검사 대상 불분명",
 "Dune Detector": "탐지 대상 불분명", "Whale Timer": "결합 불성립",
 "Dolphin Workshop": "결합 불성립", "Penguin Guardian": "감시 대상 불분명",
 "Flamingo Helper": "결합 불성립", "Turtle Stage": "결합 불성립",
 "Moose Result": "결합 불성립", "Bison Streak": "결합 불성립",
 "Reindeer Rank": "결합 불성립",
 "Family Workbook": "워크북 대상 불분명", "Chemical Mode": "기능 토글로 읽혀 제품 불분명",
 "Maintenance Spec": "결합 불성립", "Inspection Quantity": "수량 대상 불분명",
 "Pricing Login": "결합 불성립", "Cemetery Analysis": "분석 대상 불분명",
 "Commission Coach": "코칭 대상 불분명", "Dispensing Habit": "결합 불성립",
 "Port Workbook": "워크북 대상 불분명", "Logbook Mode": "기능 토글로 읽혀 제품 불분명",
 "Tailings Spec": "결합 불성립", "Coil Quantity": "수량 대상 불분명",
 "Keypad Login": "결합 불성립", "Bilingual Analysis": "분석 대상 불분명",
 "Mileage Coach": "코칭 대상 불분명", "Editing Habit": "결합 불성립",
 "Lawyer Table": "결합 불성립(Table 축 기각)", "Attorney Margin": "결합 불성립",
 "Court Schematic": "회로도 어휘 부자연", "Judge Reading": "결합 불성립",
 "Jury Correction": "결합 불성립", "Lawsuit Voltage": "결합 불성립",
 "Divorce Flyer": "결합 불성립",
 "Amendment Workbook": "워크북 대상 불분명",
 "Pension Workbook": "워크북 대상 불분명", "Siding Mode": "기능 토글로 읽혀 제품 불분명",
 "Thesis Spec": "결합 불성립", "Meeting Quantity": "수량 대상 불분명",
 "Headline Login": "결합 불성립", "Priority Analysis": "분석 대상 불분명",
 "Headhunter Coach": "코칭 대상 불분명", "Swag Habit": "결합 불성립",
 "Custody Frame": "결합 불성립", "Immigration Ops": "운영 대상 불분명",
 "Testament Note": "결합 불성립", "Notary Statement": "결합 불성립",
 "Mediation Value": "결합 불성립", "Guardianship Penalty": "결합 불성립",
 "Trademark Estimator": "산출 대상 불분명", "Patent Authorization": "결합 불성립",
 "Copyright Nomination": "결합 불성립",
 "Cabinetry Workbook": "워크북 대상 불분명", "Withdrawal Mode": "기능 토글로 읽혀 제품 불분명",
 "Latte Spec": "결합 불성립", "Behavior Quantity": "수량 대상 불분명",
 "Toothbrush Login": "결합 불성립", "Nanny Analysis": "분석 대상 불분명",
 "Sidewalk Coach": "코칭 대상 불분명", "Snorkeling Habit": "결합 불성립",
 "Migraine Bulletin": "결합 불성립", "Insomnia Confirmation": "확인 대상 불분명",
 "Skydiving Item": "항목 대상 불분명", "Acne Unit": "결합 불성립",
 "Snowboarding Fare": "결합 불성립", "Eczema Tax": "결합 불성립",
 "Ziplining Debt": "결합 불성립", "Psoriasis Fund": "자금 근거 약함",
 "Sledding Charge": "결합 불성립", "Vertigo Duty": "결합 불성립",
 "Diving Value": "결합 불성립", "Arthritis Stake": "결합 불성립",
 "Sailing Number": "수치 지칭 부자연", "Menopause Version": "결합 불성립",
 "Rafting Detail": "결합 불성립", "Pregnancy Identifier": "결합 불성립",
 "Climbing Field": "결합 불성립", "Fertility Format": "결합 불성립",
 "Biking Signature": "결합 불성립", "Thyroid Marker": "결합 불성립",
 "Golf Asset": "결합 불성립", "Cholesterol Levy": "결합 불성립",
 "Fishing Discount": "결합 불성립", "Hypertension Arrears": "결합 불성립",
 "Camping Markup": "결합 불성립", "Anemia Redemption": "결합 불성립",
 "Glamping Graph": "그래프 대상 불분명", "Heartburn Label": "결합 불성립",
 "Stargazing Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Constipation Schematic": "회로도 어휘 부자연", "Birdwatching Outline": "지형은 공예 오트라인 대상 아님",
 "Concussion Rendering": "렌더링 대상 불분명", "Canyon Kit": "키트 대상 불분명",
 "Sprain Count": "대상 불분명", "Geyser Message": "결합 불성립",
 "Fracture Total": "결합 불성립", "Fjord Widget": "위젯 대상 불분명",
 "Insulin Repository": "결합 불성립",
 "Savanna Announcement": "결합 불성립", "Tundra Calculator": "계산 대상 불분명",
 "Prairie Converter": "변환 대상 불분명", "Marsh Generator": "생성 대상 불분명",
 "Cove Recorder": "기록 대상 불분명", "Cliff Estimator": "산출 대상 불분명",
 "Cavern Checker": "검사 대상 불분명", "Oasis Detector": "탐지 대상 불분명",
 "Dune Timer": "결합 불성립", "Whale Workshop": "결합 불성립",
 "Dolphin Guardian": "감시 대상 불분명", "Penguin Helper": "결합 불성립",
 "Flamingo Stage": "결합 불성립", "Turtle Result": "결합 불성립",
 "Moose Streak": "결합 불성립", "Bison Rank": "결합 불성립",
 "Reindeer Trend": "결합 불성립",
 "Immunization Workbook": "워크북 대상 불분명", "Family Mode": "기능 토글로 읽혀 제품 불분명",
 "Chemical Spec": "결합 불성립", "Maintenance Quantity": "수량 대상 불분명",
 "Inspection Login": "결합 불성립", "Pricing Analysis": "분석 대상 불분명",
 "Cemetery Coach": "코칭 대상 불분명", "Commission Habit": "결합 불성립",
 "Recall Workbook": "워크북 대상 불분명", "Port Mode": "기능 토글로 읽혀 제품 불분명",
 "Logbook Spec": "결합 불성립", "Tailings Quantity": "수량 대상 불분명",
 "Coil Login": "결합 불성립", "Keypad Analysis": "분석 대상 불분명",
 "Bilingual Coach": "코칭 대상 불분명", "Mileage Habit": "결합 불성립",
 "Lawyer Slip": "결합 불성립", "Attorney Fine": "결합 불성립",
 "Court Layout": "결합 불성립", "Judge Reference": "결합 불성립",
 "Jury Revision": "결합 불성립", "Lawsuit Wattage": "결합 불성립",
 "Salvage Workbook": "워크북 대상 불분명", "Pension Mode": "기능 토글로 읽혀 제품 불분명",
 "Siding Spec": "결합 불성립", "Thesis Quantity": "수량 대상 불분명",
 "Meeting Login": "결합 불성립", "Headline Analysis": "분석 대상 불분명",
 "Priority Coach": "코칭 대상 불분명", "Headhunter Habit": "결합 불성립",
 "Custody Base": "결합 불성립",
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
out = base + r"\_dec_c13.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
