# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk7_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Dividend Analysis": (0.55, "배당 분석(투자 분석 실재)"),
 "Lawyer Summary": (0.55, "사건 요약 관리(Summary 축)"),
 "Notary Receipt": (0.55, "공증 접수증 관리"),
 "Metronome App": (0.6, "메트로놈 앱(실재 카테고리)"),
 "Workout Tips": (0.55, "운동 팁(App→Tips 평행)"),
 "Idiom Coach": (0.55, "관용구 학습 코치(언어 코칭 실재)"),
 "Vertigo Cost": (0.55, "어지럼증 치료 비용(건강 비용 축)"),
 "Fjord Diagram": (0.55, "피오르 지형 다이어그램(지리 교육 축)"),
 "Dispensing App": (0.6, "약국 조제 관리 앱(실재)"),
 "Charter Tips": (0.55, "선박 전세 팁(App→Tips 평행)"),
 "Storage Login": (0.55, "보관 예약 포털 로그인"),
 "Editing App": (0.6, "사진 편집 앱(실재 카테고리)"),
 "Toast Tips": (0.55, "축사 준비 팁(App→Tips 평행)"),
 "Lawyer Timeline": (0.55, "사건 타임라인(Timeline 축)"),
 "Swag App": (0.6, "이벤트 기념품 관리 앱(실재 카테고리)"),
 "Idiom Habit": (0.55, "관용구 학습 습관(학습 습관 축)"),
 "Patent Record": (0.55, "특허 기록 관리"),
 "Snorkeling App": (0.6, "스노클링 투어 앱(실재)"),
 "Metronome Tips": (0.55, "연습 팁(App→Tips 평행)"),
 "Diner Tips": (0.55, "다이너 운영 팁(App→Tips 평행)"),
}
R_DUP = {
 "Payee Advice": "동일 배치 승인된 Payee Tips와 동일 기능 의미 중복",
 "Fuel Advice": "동일 배치 승인된 Fuel Tips와 동일 기능 의미 중복",
 "Deposit Advice": "동일 배치 승인된 Deposit Tips와 동일 기능 의미 중복",
 "Diner Advice": "동일 배치 승인된 Diner Tips와 동일 기능 의미 중복",
 "Workout Advice": "동일 배치 승인된 Workout Tips와 동일 기능 의미 중복",
}
R = {
 "Washer Mode": "기능 토글로 읽혀 제품 불분명", "Hostel Spec": "결합 불성립",
 "Bass Quantity": "수량 대상 불분명", "Triage Login": "결합 불성립",
 "Paralegal Coach": "코칭 대상 불분명", "Courier Habit": "결합 불성립",
 "Attorney Sum": "결합 불성립", "Court Advance": "결합 불성립",
 "Judge Helper": "판사 대상 서비스 불성립", "Jury Broadcast": "결합 불성립",
 "Lawsuit Limit": "결합 불성립", "Divorce Resignation": "결합 불성립",
 "Screening App": "스크리닝 대상 불분명", "Tick Advice": "대상 불분명(Tick 계열)",
 "Molar Workbook": "대상 불분명(Molar 계열)", "Toy Mode": "기능 토글로 읽혀 제품 불분명",
 "Product Spec": "일반 명사로 대상 불분명", "Injection Quantity": "수량 대상 불분명",
 "Igniter Login": "결합 불성립(Igniter 계열)", "Rim Analysis": "분석 대상 불분명(Rim 계열)",
 "Stairs Habit": "결합 불성립(Stairs 계열)",
 "Custody Cascade": "결합 불성립", "Immigration Nexus": "결합 불성립",
 "Tanker Workbook": "워크북 대상 불분명",
 "Testament Ticker": "결합 불성립", "Mediation Tax": "결합 불성립",
 "Guardianship Signature": "결합 불성립", "Trademark Kit": "키트 대상 불분명",
 "Patent Guarantee": "결합 불성립", "Copyright Eligibility": "자격 대상 불분명",
 "Toothpaste Analysis": "분석 대상 불분명", "Formula Coach": "코칭 대상 불분명",
 "Mailroom Habit": "결합 불성립", "Migraine Slip": "결합 불성립",
 "Insomnia Badge": "결합 불성립", "Skydiving Quota": "결합 불성립",
 "Acne Tab": "결합 불성립", "Snowboarding Advisory": "안내 대상 불분명",
 "Eczema Petition": "결합 불성립", "Ziplining Entry": "등록 대상 불분명",
 "Psoriasis Fee": "결합 불성립", "Sledding Plan": "계획 대상 불분명(Sailing Plan 기각 선례)",
 "Diving Tax": "결합 불성립", "Arthritis Loan": "결합 불성립",
 "Sailing Fund": "결합 불성립", "Menopause Cash": "결합 불성립",
 "Rafting Duty": "결합 불성립", "Pregnancy Allowance": "결합 불성립",
 "Climbing Stake": "결합 불성립", "Fertility Margin": "결합 불성립",
 "Biking Version": "결합 불성립", "Thyroid Link": "결합 불성립",
 "Golf Identifier": "결합 불성립", "Cholesterol Category": "결합 불성립",
 "Fishing Format": "결합 불성립", "Hypertension Serial": "결합 불성립",
 "Camping Marker": "결합 불성립", "Anemia Balance": "결합 불성립",
 "Glamping Levy": "결합 불성립", "Heartburn Due": "결합 불성립",
 "Stargazing Arrears": "결합 불성립", "Constipation Advance": "결합 불성립",
 "Birdwatching Redemption": "결합 불성립", "Concussion Extension": "결합 불성립",
 "Canyon Graph": "그래프 대상 불분명", "Sprain Label": "결합 불성립",
 "Geyser Manual": "설명 대상 불분명", "Fracture Worksheet": "학습지 근거 약함",
 "Insulin Schematic": "회로도 어휘 부자연", "Savanna Layout": "결합 불성립",
 "Tundra Sketch": "제품성 불분명", "Prairie Outline": "지형은 공예 오트라인 대상 아님",
 "Marsh Rendering": "렌더링 대상 불분명", "Cove Notification": "결합 불성립",
 "Cliff Kit": "키트 대상 불분명", "Cavern Count": "대상 불분명",
 "Oasis Message": "결합 불성립", "Dune Total": "결합 불성립",
 "Whale Widget": "위젯 대상 불분명", "Dolphin Repository": "결합 불성립",
 "Penguin Announcement": "결합 불성립", "Flamingo Calculator": "계산 대상 불분명",
 "Turtle Converter": "변환 대상 불분명", "Moose Generator": "생성 대상 불분명",
 "Bison Recorder": "기록 대상 불분명", "Reindeer Estimator": "산출 대상 불분명",
 "Shift Workbook": "워크북 대상 불분명", "Filtration Mode": "기능 토글로 읽혀 제품 불분명",
 "Masterkey Spec": "결합 불성립", "Terminology Quantity": "수량 대상 불분명",
 "Deed Mode": "기능 토글로 읽혀 제품 불분명", "Policyholder Spec": "결합 불성립",
 "Countertop Quantity": "수량 대상 불분명",
 "Cocktail Login": "결합 불성립",
 "Payee Workbook": "워크북 대상 불분명",
 "Gallery Analysis": "분석 대상 불분명", "Florist Coach": "코칭 대상 불분명",
 "Renewal Habit": "결합 불성립", "Turbidity Workbook": "워크북 대상 불분명",
 "Foam Mode": "기능 토글로 읽혀 제품 불분명", "Washer Spec": "결합 불성립",
 "Hostel Quantity": "수량 대상 불분명", "Bass Login": "결합 불성립",
 "Triage Analysis": "분석 대상 불분명", "Dividend Coach": "코칭 대상 불분명",
 "Paralegal Habit": "결합 불성립", "Attorney Debt": "결합 불성립",
 "Court Penalty": "결합 불성립", "Judge Stage": "결합 불성립",
 "Jury Barcode": "결합 불성립", "Lawsuit Type": "결합 불성립",
 "Divorce Hazard": "결합 불성립", "Screening Tips": "대상 불분명(Screening App 기각 선례)",
 "Tick Workbook": "대상 불분명(Tick 계열)", "Molar Mode": "기능 토글로 읽혀 제품 불분명",
 "Toy Spec": "결합 불성립", "Product Quantity": "수량 대상 불분명",
 "Injection Login": "결합 불성립", "Igniter Analysis": "분석 대상 불분명",
 "Rim Coach": "코칭 대상 불분명(Rim 계열)", "Custody Bridge": "결합 불성립",
 "Immigration Atlas": "결합 불성립", "Testament Line": "결합 불성립",
 "Notary Code": "결합 불성립", "Mediation Loan": "결합 불성립",
 "Guardianship Marker": "결합 불성립", "Trademark Count": "대상 불분명",
 "Copyright Broadcast": "결합 불성립", "Tanker Mode": "기능 토글로 읽혀 제품 불분명",
 "Deed Spec": "결합 불성립", "Policyholder Quantity": "수량 대상 불분명",
 "Countertop Login": "결합 불성립", "Cocktail Analysis": "분석 대상 불분명",
 "Toothpaste Coach": "코칭 대상 불분명", "Formula Habit": "결합 불성립",
 "Migraine Sample": "결합 불성립", "Insomnia Stub": "결합 불성립",
 "Skydiving Tab": "결합 불성립", "Acne Bulletin": "결합 불성립",
 "Snowboarding Petition": "결합 불성립", "Eczema Confirmation": "확인 대상 불분명",
 "Ziplining Fee": "요금 근거 약함", "Psoriasis Item": "항목 대상 불분명",
 "Sledding Cost": "활동 비용 근거 약함(Diving/Sailing Cost와 달리 산업성 없음)",
 "Vertigo Price": "가격 지칭 부자연(Vertigo Cost 승인과 구별)",
 "Diving Loan": "결합 불성립", "Arthritis Sum": "결합 불성립",
 "Sailing Cash": "결합 불성립", "Menopause Sale": "결합 불성립",
 "Rafting Allowance": "결합 불성립", "Pregnancy Tariff": "결합 불성립",
 "Climbing Margin": "결합 불성립", "Fertility Fine": "결합 불성립",
 "Biking Link": "결합 불성립", "Thyroid Rule": "결합 불성립",
 "Golf Category": "결합 불성립", "Cholesterol Attribute": "결합 불성립",
 "Fishing Serial": "결합 불성립", "Hypertension Token": "결합 불성립",
 "Camping Balance": "결합 불성립", "Anemia Interest": "결합 불성립",
 "Glamping Due": "결합 불성립", "Heartburn Subsidy": "결합 불성립",
 "Stargazing Advance": "결합 불성립", "Constipation Penalty": "결합 불성립",
 "Birdwatching Extension": "결합 불성립", "Concussion Trial": "결합 불성립",
 "Canyon Label": "결합 불성립", "Sprain Manual": "설명 대상 불분명",
 "Geyser Worksheet": "학습지 근거 약함", "Fracture Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Fjord Schematic": "회로도 어휘 부자연", "Insulin Layout": "결합 불성립",
 "Savanna Sketch": "제품성 불분명", "Tundra Outline": "지형은 공예 오트라인 대상 아님",
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
out = base + r"\_dec_c7.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
