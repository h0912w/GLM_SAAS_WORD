# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk6_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Payee App": (0.55, "수취인·송금 관리 앱(실재)"),
 "Tanker Tips": (0.55, "유조차 운송 팁(App→Tips 평행)"),
 "Savanna Diagram": (0.55, "사바나 생태 다이어그램(지리 교육 축)"),
 "Fuel App": (0.6, "연료 관리 앱(항공 실재)"),
 "Shift Tips": (0.55, "교대 근무 운영 팁(App→Tips 평행)"),
 "Deposit App": (0.6, "보증금 관리 앱(부동산 실재)"),
 "Turbidity Tips": (0.55, "수질 관리 팁(App→Tips 평행)"),
 "Paralegal Analysis": (0.55, "로펌 업무 데이터 분석(legal analytics 실재)"),
 "Lawyer Draft": (0.55, "법률 서류 초안 작성(Notary Draft 평행)"),
 "Diner App": (0.55, "다이너 주문·예약 앱(실재)"),
 "Workout App": (0.6, "운동 기록 앱(실재 카테고리)"),
 "Payee Tips": (0.55, "송금·수취 팁(App→Tips 평행)"),
 "Vertigo Plan": (0.55, "어지럼증 관리 계획(건강 관리 플랜 축)"),
 "Charter App": (0.6, "선박 전세 예약 앱(실재 카테고리)"),
 "Fuel Tips": (0.55, "연료 관리 팁(App→Tips 평행)"),
 "Toast App": (0.55, "결혼식 축사 준비 앱(wedding toast 실재)"),
 "Deposit Tips": (0.55, "보증금 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Tanker Advice": "동일 배치 승인된 Tanker Tips와 동일 기능 의미 중복",
 "Deed Advice": "동일 배치 승인된 Deed Tips와 동일 기능 의미 중복",
 "Shift Advice": "동일 배치 승인된 Shift Tips와 동일 기능 의미 중복",
 "Turbidity Advice": "동일 배치 승인된 Turbidity Tips와 동일 기능 의미 중복",
 "Filtration Advice": "동일 배치 승인된 Filtration Tips와 동일 기능 의미 중복",
}
R = {
 "Guardianship Serial": "결합 불성립", "Trademark Rendering": "렌더링 대상 불분명",
 "Patent Comparison": "비교 대상 불분명", "Copyright Model": "결합 불성립",
 "Toothpaste Quantity": "수량 대상 불분명", "Formula Login": "결합 불성립",
 "Countertop Mode": "기능 토글로 읽혀 제품 불분명", "Cocktail Spec": "결합 불성립",
 "Policyholder Mode": "기능 토글로 읽혀 제품 불분명",
 "Mailroom Analysis": "분석 대상 불분명", "Kayaking Coach": "코칭 대상 불분명",
 "Policyholder Workbook": "워크북 대상 불분명",
 "Deed Workbook": "워크북 대상 불분명",
 "Songbook Habit": "결합 불성립(Songbook 계열 기각 선례)",
 "Migraine List": "결합 불성립(Acne List 기각 선례)", "Insomnia Pass": "결합 불성립",
 "Skydiving Statement": "결합 불성립", "Acne Memo": "결합 불성립",
 "Snowboarding Brief": "결합 불성립", "Eczema Circular": "결합 불성립",
 "Ziplining Confirmation": "확인 대상 불분명", "Psoriasis Recap": "결합 불성립",
 "Sledding Item": "항목 대상 불분명", "Vertigo Unit": "결합 불성립",
 "Diving Price": "가격 지칭 부자연(Diving Cost 승인과 구별)",
 "Arthritis Fare": "결합 불성립", "Sailing Sum": "결합 불성립",
 "Menopause Debt": "결합 불성립", "Rafting Sale": "결합 불성립",
 "Pregnancy Charge": "결합 불성립", "Climbing Tariff": "결합 불성립",
 "Fertility Value": "결합 불성립", "Biking Fine": "결합 불성립",
 "Thyroid Number": "수치 지칭 부자연", "Golf Rule": "결합 불성립",
 "Cholesterol Detail": "결합 불성립", "Fishing Attribute": "결합 불성립",
 "Hypertension Field": "결합 불성립", "Camping Token": "결합 불성립",
 "Anemia Signature": "결합 불성립", "Glamping Interest": "결합 불성립",
 "Heartburn Asset": "결합 불성립", "Stargazing Subsidy": "결합 불성립",
 "Constipation Discount": "결합 불성립", "Birdwatching Penalty": "결합 불성립",
 "Concussion Markup": "결합 불성립", "Canyon Extension": "결합 불성립",
 "Sprain Trial": "결합 불성립", "Geyser Graph": "그래프 대상 불분명",
 "Fracture Label": "결합 불성립", "Fjord Manual": "설명 대상 불분명",
 "Insulin Worksheet": "학습지 근거 약함", "Tundra Schematic": "회로도 어휘 부자연",
 "Prairie Layout": "결합 불성립", "Marsh Sketch": "제품성 불분명",
 "Cove Outline": "지형은 공예 오트라인 대상 아님", "Cliff Rendering": "렌더링 대상 불분명",
 "Cavern Notification": "결합 불성립", "Oasis Kit": "키트 대상 불분명",
 "Dune Count": "대상 불분명", "Whale Message": "결합 불성립",
 "Dolphin Total": "결합 불성립", "Penguin Widget": "위젯 대상 불분명",
 "Flamingo Repository": "결합 불성립", "Turtle Announcement": "결합 불성립",
 "Moose Calculator": "계산 대상 불분명", "Bison Converter": "변환 대상 불분명",
 "Reindeer Generator": "생성 대상 불분명", "Masterkey Workbook": "워크북 대상 불분명",
 "Terminology Mode": "기능 토글로 읽혀 제품 불분명", "Storage Spec": "결합 불성립",
 "Gallery Quantity": "수량 대상 불분명", "Florist Login": "결합 불성립",
 "Renewal Analysis": "분석 대상 불분명", "Liner Coach": "코칭 대상 불분명",
 "Coating Habit": "결합 불성립", "Foam Advice": "대상 불분명(Foam 계열 기각 선례)",
 "Washer Workbook": "워크북 대상 불분명", "Hostel Mode": "기능 토글로 읽혀 제품 불분명",
 "Bass Spec": "결합 불성립", "Triage Quantity": "수량 대상 불분명",
 "Dividend Login": "결합 불성립", "Courier Coach": "코칭 대상 불분명",
 "Mortgage Habit": "결합 불성립", "Attorney Loan": "결합 불성립",
 "Court Arrears": "결합 불성립", "Judge Guardian": "감시 대상 불분명",
 "Jury Eligibility": "서비스 대상 불분명", "Lawsuit Range": "결합 불성립",
 "Divorce Depreciation": "결합 불성립", "Tick Tips": "대상 불분명(Tick App 기각 선례)",
 "Molar Advice": "대상 불분명(Molar 계열)", "Toy Workbook": "워크북 대상 불분명",
 "Product Mode": "기능 토글로 읽혀 제품 불분명", "Injection Spec": "결합 불성립",
 "Igniter Quantity": "수량 대상 불분명", "Rim Login": "결합 불성립(Rim 계열)",
 "Idiom Analysis": "분석 대상 불분명", "Stairs Coach": "코칭 대상 불분명(Stairs 계열)",
 "Location Habit": "결합 불성립", "Custody Forge": "결합 불성립",
 "Immigration Gate": "결합 불성립", "Testament Lobby": "결합 불성립",
 "Notary Bill": "결합 불성립(Notary Estimate 기각 선례)", "Mediation Fare": "결합 불성립",
 "Guardianship Token": "결합 불성립", "Trademark Notification": "결합 불성립",
 "Patent Proposal": "제안 대상 불분명", "Copyright Availability": "결합 불성립",
 "Countertop Spec": "결합 불성립", "Cocktail Quantity": "수량 대상 불분명",
 "Toothpaste Login": "결합 불성립", "Formula Analysis": "분석 대상 불분명",
 "Mailroom Coach": "코칭 대상 불분명", "Kayaking Habit": "결합 불성립",
 "Migraine Table": "결합 불성립(Insomnia Table 기각 선례)",
 "Insomnia Voucher": "결합 불성립", "Skydiving Memo": "결합 불성립",
 "Acne Quota": "결합 불성립", "Snowboarding Circular": "결합 불성립",
 "Eczema Advisory": "안내 대상 불분명", "Ziplining Recap": "결합 불성립",
 "Psoriasis Entry": "등록 대상 불분명", "Sledding Unit": "결합 불성립",
 "Diving Fare": "결합 불성립", "Arthritis Tax": "결합 불성립",
 "Sailing Debt": "결합 불성립", "Menopause Fund": "자금 근거 약함",
 "Rafting Charge": "결합 불성립", "Pregnancy Duty": "결합 불성립",
 "Climbing Value": "결합 불성립", "Fertility Stake": "결합 불성립",
 "Biking Number": "결합 불성립", "Thyroid Version": "결합 불성립",
 "Golf Detail": "결합 불성립", "Cholesterol Identifier": "결합 불성립",
 "Fishing Field": "결합 불성립", "Hypertension Format": "결합 불성립",
 "Camping Signature": "결합 불성립", "Anemia Marker": "결합 불성립",
 "Glamping Asset": "결합 불성립", "Heartburn Levy": "결합 불성립",
 "Stargazing Discount": "결합 불성립", "Constipation Arrears": "결합 불성립",
 "Birdwatching Markup": "결합 불성립", "Concussion Redemption": "결합 불성립",
 "Canyon Trial": "결합 불성립", "Sprain Graph": "그래프 대상 불분명",
 "Geyser Label": "결합 불성립", "Fracture Manual": "설명 대상 불분명",
 "Fjord Worksheet": "학습지 근거 약함", "Insulin Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Savanna Schematic": "회로도 어휘 부자연", "Tundra Layout": "결합 불성립",
 "Prairie Sketch": "제품성 불분명", "Marsh Outline": "지형은 공예 오트라인 대상 아님",
 "Cove Rendering": "렌더링 대상 불분명", "Cliff Notification": "결합 불성립",
 "Cavern Kit": "키트 대상 불분명", "Oasis Count": "대상 불분명",
 "Dune Message": "결합 불성립", "Whale Total": "결합 불성립",
 "Dolphin Widget": "위젯 대상 불분명", "Penguin Repository": "결합 불성립",
 "Flamingo Announcement": "결합 불성립", "Turtle Calculator": "계산 대상 불분명",
 "Moose Converter": "변환 대상 불분명", "Bison Generator": "생성 대상 불분명",
 "Reindeer Recorder": "기록 대상 불분명", "Filtration Workbook": "워크북 대상 불분명",
 "Masterkey Mode": "기능 토글로 읽혀 제품 불분명", "Terminology Spec": "결합 불성립",
 "Storage Quantity": "수량 대상 불분명", "Gallery Login": "결합 불성립",
 "Florist Analysis": "분석 대상 불분명", "Renewal Coach": "코칭 대상 불분명",
 "Liner Habit": "결합 불성립", "Foam Workbook": "대상 불분명(Foam 계열)",
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
out = base + r"\_dec_c6.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
