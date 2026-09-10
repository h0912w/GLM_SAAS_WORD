# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk9_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Pricing App": (0.55, "세탁 요금 책정 관리 앱(pricing software 실재)"),
 "Cemetery Tips": (0.55, "묘지·추모 관리 팁(App→Tips 평행)"),
 "Keypad App": (0.6, "스마트 락 키패드 관리 앱(실재)"),
 "Bilingual Tips": (0.55, "이중언어 학습 팁(App→Tips 평행)"),
 "Divorce Tutorial": (0.55, "이혼 절차 튜토리얼(교육 콘텐츠 실재)"),
 "Headline App": (0.6, "헤드라인 생성·분석 앱(실재 카테고리)"),
 "Priority Tips": (0.55, "문의 우선순위 운영 팁(App→Tips 평행)"),
 "Toothbrush App": (0.6, "칫솔 관리·타이머 앱(실재)"),
 "Nanny Tips": (0.55, "보모 매칭·육아 팁(App→Tips 평행)"),
 "Psoriasis Cost": (0.55, "건선 치료 비용(건강 비용 축)"),
 "Canyon Diagram": (0.55, "협곡 지형 다이어그램(지리 교육 축)"),
 "Inspection App": (0.6, "청소 검수·점검 관리 앱(실재)"),
 "Pricing Tips": (0.55, "요금 책정 팁(App→Tips 평행)"),
 "Coil App": (0.55, "HVAC 코일 관리 앱(코일 세척 실재)"),
 "Keypad Tips": (0.55, "키패드 잠금 설정 팁(App→Tips 평행)"),
 "Divorce Handbook": (0.55, "이혼 절차 핸드북(실재)"),
 "Meeting App": (0.6, "공공 회의 관리 앱(실재 카테고리)"),
 "Headline Tips": (0.55, "헤드라인 작성 팁(App→Tips 평행)"),
}
R_DUP = {
 "Commission Advice": "동일 배치 승인된 Commission App/Tips와 동일 기능 의미 중복",
 "Mileage Advice": "동일 배치 승인된 Mileage App/Tips와 동일 기능 의미 중복",
 "Headhunter Advice": "동일 배치 승인된 Headhunter App/Tips와 동일 기능 의미 중복",
 "Sidewalk Advice": "동일 배치 승인된 Sidewalk App/Tips와 동일 기능 의미 중복",
 "Cemetery Advice": "동일 배치 승인된 Cemetery App/Tips와 동일 기능 의미 중복",
 "Bilingual Advice": "동일 배치 승인된 Bilingual App/Tips와 동일 기능 의미 중복",
 "Priority Advice": "동일 배치 승인된 Priority App/Tips와 동일 기능 의미 중복",
}
R = {
 "Sailing Charge": "결합 불성립", "Menopause Duty": "결합 불성립",
 "Rafting Value": "결합 불성립", "Pregnancy Stake": "결합 불성립",
 "Climbing Number": "수치 지칭 부자연", "Fertility Version": "결합 불성립",
 "Biking Detail": "결합 불성립", "Thyroid Identifier": "결합 불성립",
 "Golf Field": "결합 불성립", "Cholesterol Format": "결합 불성립",
 "Fishing Signature": "결합 불성립", "Hypertension Marker": "결합 불성립",
 "Camping Asset": "결합 불성립", "Anemia Levy": "결합 불성립",
 "Glamping Discount": "결합 불성립", "Heartburn Arrears": "결합 불성립",
 "Stargazing Markup": "결합 불성립", "Constipation Redemption": "결합 불성립",
 "Birdwatching Graph": "그래프 대상 불분명", "Concussion Label": "결합 불성립",
 "Canyon Worksheet": "학습지 근거 약함", "Sprain Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Geyser Schematic": "회로도 어휘 부자연", "Fracture Layout": "결합 불성립",
 "Fjord Sketch": "제품성 불분명", "Insulin Outline": "제품성 불분명",
 "Savanna Rendering": "렌더링 대상 불분명", "Tundra Notification": "결합 불성립",
 "Prairie Kit": "키트 대상 불분명", "Marsh Count": "대상 불분명",
 "Cove Message": "결합 불성립", "Cliff Total": "결합 불성립",
 "Cavern Widget": "위젯 대상 불분명", "Oasis Repository": "결합 불성립",
 "Dune Announcement": "결합 불성립", "Whale Calculator": "계산 대상 불분명",
 "Dolphin Converter": "변환 대상 불분명", "Penguin Generator": "생성 대상 불분명",
 "Flamingo Recorder": "기록 대상 불분명", "Turtle Estimator": "산출 대상 불분명",
 "Moose Checker": "검사 대상 불분명", "Bison Detector": "탐지 대상 불분명",
 "Reindeer Timer": "결합 불성립", "Dispensing Workbook": "워크북 대상 불분명",
 "Charter Mode": "기능 토글로 읽혀 제품 불분명", "Fuel Spec": "결합 불성립",
 "Shift Quantity": "수량 대상 불분명", "Filtration Login": "결합 불성립",
 "Masterkey Analysis": "분석 대상 불분명", "Terminology Coach": "코칭 대상 불분명",
 "Lawyer Ticket": "결합 불성립", "Attorney Sale": "결합 불성립",
 "Court Extension": "결합 불성립", "Judge Rank": "결합 불성립",
 "Jury Invoice": "결합 불성립", "Lawsuit Speed": "결합 불성립",
 "Headline Workbook": "워크북 대상 불분명",
 "Swag Workbook": "워크북 대상 불분명", "Screening Mode": "기능 토글로 읽혀 제품 불분명",
 "Diner Spec": "결합 불성립", "Tick Quantity": "수량 대상 불분명",
 "Molar Login": "결합 불성립(Molar 계열)", "Toy Analysis": "분석 대상 불분명",
 "Product Coach": "코칭 대상 불분명", "Injection Habit": "결합 불성립",
 "Custody Scope": "범위 대상 불분명", "Immigration Engine": "결합 불성립",
 "Testament Report": "보고서 대상 불분명(Testament 계열 기각 선례)",
 "Notary Slip": "결합 불성립", "Mediation Fund": "자금 근거 약함",
 "Guardianship Asset": "결합 불성립", "Trademark Widget": "위젯 대상 불분명",
 "Patent Reference": "결합 불성립", "Copyright Feedback": "결합 불성립",
 "Snorkeling Workbook": "워크북 대상 불분명", "Metronome Mode": "기능 토글로 읽혀 제품 불분명",
 "Editing Workbook": "워크북 대상 불분명",
 "Toast Mode": "기능 토글로 읽혀 제품 불분명",
 "Deposit Spec": "결합 불성립", "Turbidity Quantity": "수량 대상 불분명",
 "Foam Login": "결합 불성립(Foam 계열 기각 선례)", "Washer Analysis": "분석 대상 불분명",
 "Hostel Coach": "코칭 대상 불분명", "Bass Habit": "결합 불성립",
 "Workout Spec": "결합 불성립", "Payee Quantity": "수량 대상 불분명",
 "Tanker Login": "결합 불성립", "Deed Analysis": "분석 대상 불분명",
 "Policyholder Coach": "코칭 대상 불분명", "Countertop Habit": "결합 불성립",
 "Migraine Voucher": "결합 불성립", "Insomnia Quota": "결합 불성립",
 "Skydiving Circular": "결합 불성립", "Acne Advisory": "안내 대상 불분명",
 "Snowboarding Entry": "등록 대상 불분명", "Eczema Fee": "결합 불성립",
 "Ziplining Plan": "계획 대상 불분명(Sailing Plan 기각 선례)",
 "Sledding Tax": "결합 불성립", "Vertigo Loan": "결합 불성립",
 "Diving Fund": "결합 불성립", "Arthritis Cash": "결합 불성립",
 "Sailing Duty": "결합 불성립", "Menopause Allowance": "결합 불성립",
 "Rafting Stake": "결합 불성립", "Pregnancy Margin": "결합 불성립",
 "Climbing Version": "결합 불성립", "Fertility Link": "결합 불성립",
 "Biking Identifier": "결합 불성립", "Thyroid Category": "결합 불성립",
 "Golf Format": "결합 불성립", "Cholesterol Serial": "결합 불성립",
 "Fishing Marker": "결합 불성립", "Hypertension Balance": "결합 불성립",
 "Camping Levy": "결합 불성립", "Anemia Due": "결합 불성립",
 "Glamping Arrears": "결합 불성립", "Heartburn Advance": "결합 불성립",
 "Stargazing Redemption": "결합 불성립", "Constipation Extension": "결합 불성립",
 "Birdwatching Label": "결합 불성립", "Concussion Manual": "설명 대상 불분명",
 "Sprain Schematic": "회로도 어휘 부자연", "Geyser Layout": "결합 불성립",
 "Fracture Sketch": "제품성 불분명", "Fjord Outline": "지형은 공예 오트라인 대상 아님",
 "Insulin Rendering": "렌더링 대상 불분명", "Savanna Notification": "결합 불성립",
 "Tundra Kit": "키트 대상 불분명", "Prairie Count": "대상 불분명",
 "Marsh Message": "결합 불성립", "Cove Total": "결합 불성립",
 "Cliff Widget": "위젯 대상 불분명", "Cavern Repository": "결합 불성립",
 "Oasis Announcement": "결합 불성립", "Dune Calculator": "계산 대상 불분명",
 "Whale Converter": "변환 대상 불분명", "Dolphin Generator": "생성 대상 불분명",
 "Penguin Recorder": "기록 대상 불분명", "Flamingo Estimator": "산출 대상 불분명",
 "Turtle Checker": "검사 대상 불분명", "Moose Detector": "탐지 대상 불분명",
 "Bison Timer": "결합 불성립", "Reindeer Workshop": "결합 불성립",
 "Commission Workbook": "워크북 대상 불분명", "Dispensing Mode": "기능 토글로 읽혀 제품 불분명",
 "Charter Spec": "결합 불성립", "Fuel Quantity": "수량 대상 불분명",
 "Shift Login": "결합 불성립", "Filtration Analysis": "분석 대상 불분명",
 "Masterkey Coach": "코칭 대상 불분명", "Terminology Habit": "결합 불성립",
 "Bilingual Workbook": "워크북 대상 불분명",
 "Mileage Workbook": "워크북 대상 불분명", "Editing Mode": "기능 토글로 읽혀 제품 불분명",
 "Toast Spec": "결합 불성립", "Deposit Quantity": "수량 대상 불분명",
 "Turbidity Login": "결합 불성립", "Foam Analysis": "분석 대상 불분명(Foam 계열 기각 선례)",
 "Washer Coach": "코칭 대상 불분명", "Hostel Habit": "결합 불성립",
 "Lawyer Estimate": "견적 대상 불분명(Notary Estimate 기각 선례)",
 "Attorney Charge": "결합 불성립", "Court Trial": "결합 불성립",
 "Judge Trend": "결합 불성립", "Jury Renewal": "결합 불성립",
 "Lawsuit Depth": "결합 불성립", "Screening Spec": "결합 불성립(Screening 계열)",
 "Diner Quantity": "수량 대상 불분명", "Tick Login": "결합 불성립",
 "Molar Analysis": "분석 대상 불분명(Molar 계열)", "Toy Coach": "코칭 대상 불분명",
 "Product Habit": "결합 불성립", "Custody Loop": "결합 불성립",
 "Immigration Assistant": "어시스턴트 대상 불분명", "Testament Log": "결합 불성립(Testament 계열 기각 선례)",
 "Headhunter Workbook": "워크북 대상 불분명",
 "Swag Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c9.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
