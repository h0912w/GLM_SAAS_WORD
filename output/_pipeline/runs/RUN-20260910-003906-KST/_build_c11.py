# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk11_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Siding App": (0.55, "사이딩 시공 관리 앱(실재)"),
 "Thesis Tips": (0.55, "논문 작성 팁(App→Tips 평행)"),
 "Latte Tips": (0.55, "라떼 제조·주문 팁(App→Tips 평행)"),
 "Eczema Plan": (0.55, "습진 관리 계획(건강 관리 플랜 축)"),
 "Family App": (0.55, "가족 돌봄 조율 앱(family organizer 실재)"),
 "Chemical Tips": (0.55, "살충 화학 처리 팁(App→Tips 평행)"),
 "Port App": (0.6, "항만 물류 추적 앱(실재 카테고리)"),
 "Logbook Tips": (0.55, "비행 기록 팁(App→Tips 평행)"),
 "Pension App": (0.6, "연금 관리 앱(실재 카테고리)"),
 "Siding Tips": (0.55, "사이딩 시공 팁(App→Tips 평행)"),
 "Cabinetry App": (0.55, "캐비닛 제작·설치 관리 앱(실재)"),
 "Eczema Cost": (0.55, "습진 치료 비용(건강 비용 축)"),
}
R_DUP = {
 "Coil Advice": "동일 배치 승인된 Coil App/Tips와 동일 기능 의미 중복",
 "Meeting Advice": "동일 배치 승인된 Meeting App/Tips와 동일 기능 의미 중복",
 "Behavior Advice": "동일 배치 승인된 Behavior App/Tips와 동일 기능 의미 중복",
 "Maintenance Advice": "동일 배치 승인된 Maintenance App/Tips와 동일 기능 의미 중복",
 "Tailings Advice": "동일 배치 승인된 Tailings App/Tips와 동일 기능 의미 중복",
 "Thesis Advice": "동일 배치 승인된 Thesis App/Tips와 동일 기능 의미 중복",
 "Latte Advice": "동일 배치 승인된 Latte App/Tips와 동일 기능 의미 중복",
}
R = {
 "Keypad Workbook": "워크북 대상 불분명", "Bilingual Mode": "기능 토글로 읽혀 제품 불분명",
 "Mileage Spec": "결합 불성립", "Editing Quantity": "수량 대상 불분명",
 "Toast Login": "결합 불성립", "Deposit Analysis": "분석 대상 불분명",
 "Turbidity Coach": "코칭 대상 불분명", "Foam Habit": "결합 불성립(Foam 계열 기각 선례)",
 "Lawyer Bill": "결합 불성립(Notary Bill 기각 선례)", "Attorney Allowance": "결합 불성립",
 "Court Label": "결합 불성립", "Judge Proposal": "제안 대상 불분명",
 "Jury Warranty": "결합 불성립", "Lawsuit Width": "결합 불성립",
 "Divorce Opinion": "소견 대상 불분명",
 "Headline Workbook": "워크북 대상 불분명", "Priority Mode": "기능 토글로 읽혀 제품 불분명",
 "Headhunter Spec": "결합 불성립", "Swag Quantity": "수량 대상 불분명",
 "Screening Login": "결합 불성립(Screening 계열)", "Diner Analysis": "분석 대상 불분명",
 "Tick Coach": "코칭 대상 불분명", "Molar Habit": "결합 불성립(Molar 계열)",
 "Custody Wave": "결합 불성립", "Immigration Scheduler": "스케줄 대상 불분명",
 "Testament Card": "결합 불성립", "Notary Pass": "결합 불성립",
 "Mediation Charge": "결합 불성립", "Guardianship Subsidy": "결합 불성립",
 "Trademark Calculator": "계산 대상 불분명", "Patent Duration": "결합 불성립",
 "Copyright Quote": "견적 대상 불분명", "Withdrawal App": "철회 대상 불분명",
 "Toothbrush Workbook": "워크북 대상 불분명", "Nanny Mode": "기능 토글로 읽혀 제품 불분명",
 "Sidewalk Spec": "결합 불성립", "Snorkeling Quantity": "수량 대상 불분명",
 "Metronome Login": "결합 불성립", "Workout Analysis": "분석 대상 불분명",
 "Payee Coach": "코칭 대상 불분명", "Tanker Habit": "결합 불성립",
 "Migraine Statement": "결합 불성립", "Insomnia Brief": "결합 불성립",
 "Skydiving Confirmation": "확인 대상 불분명", "Acne Recap": "결합 불성립",
 "Snowboarding Unit": "결합 불성립",
 "Ziplining Fare": "결합 불성립", "Psoriasis Tax": "결합 불성립",
 "Sledding Debt": "결합 불성립", "Vertigo Fund": "자금 근거 약함",
 "Diving Charge": "결합 불성립", "Arthritis Duty": "결합 불성립",
 "Sailing Value": "결합 불성립", "Menopause Stake": "결합 불성립",
 "Rafting Number": "수치 지칭 부자연", "Pregnancy Version": "결합 불성립",
 "Climbing Detail": "결합 불성립", "Fertility Identifier": "결합 불성립",
 "Biking Field": "결합 불성립", "Thyroid Format": "결합 불성립",
 "Golf Signature": "결합 불성립", "Cholesterol Marker": "결합 불성립",
 "Fishing Asset": "결합 불성립", "Hypertension Levy": "결합 불성립",
 "Camping Discount": "결합 불성립", "Anemia Arrears": "결합 불성립",
 "Glamping Markup": "결합 불성립", "Heartburn Redemption": "결합 불성립",
 "Stargazing Graph": "그래프 대상 불분명", "Constipation Label": "결합 불성립",
 "Birdwatching Diagram": "교육 다이어그램 축은 동물·지형 대상에서만 확인(관찰 활동 제외)",
 "Concussion Schematic": "회로도 어휘 부자연", "Canyon Sketch": "제품성 불분명",
 "Sprain Outline": "제품성 불분명", "Geyser Rendering": "렌더링 대상 불분명",
 "Fracture Notification": "결합 불성립", "Fjord Kit": "키트 대상 불분명",
 "Insulin Count": "대상 불분명", "Savanna Message": "결합 불성립",
 "Tundra Total": "결합 불성립", "Prairie Widget": "위젯 대상 불분명",
 "Marsh Repository": "결합 불성립", "Cove Announcement": "결합 불성립",
 "Cliff Calculator": "계산 대상 불분명", "Cavern Converter": "변환 대상 불분명",
 "Oasis Generator": "생성 대상 불분명", "Dune Recorder": "기록 대상 불분명",
 "Whale Estimator": "산출 대상 불분명", "Dolphin Checker": "검사 대상 불분명",
 "Penguin Detector": "탐지 대상 불분명", "Flamingo Timer": "결합 불성립",
 "Turtle Workshop": "결합 불성립", "Moose Guardian": "감시 대상 불분명",
 "Bison Helper": "결합 불성립", "Reindeer Stage": "결합 불성립",
 "Inspection Workbook": "워크북 대상 불분명", "Pricing Mode": "기능 토글로 읽혀 제품 불분명",
 "Cemetery Spec": "결합 불성립", "Commission Quantity": "수량 대상 불분명",
 "Dispensing Login": "결합 불성립", "Charter Analysis": "분석 대상 불분명",
 "Fuel Coach": "코칭 대상 불분명", "Shift Habit": "결합 불성립",
 "Coil Workbook": "워크북 대상 불분명", "Keypad Mode": "기능 토글로 읽혀 제품 불분명",
 "Bilingual Spec": "결합 불성립", "Mileage Quantity": "수량 대상 불분명",
 "Editing Login": "결합 불성립", "Toast Analysis": "분석 대상 불분명",
 "Deposit Coach": "코칭 대상 불분명", "Turbidity Habit": "결합 불성립",
 "Lawyer Receipt": "영수증 대상 불분명(Notary Receipt와 달리 근거 약함)",
 "Attorney Tariff": "결합 불성립", "Court Manual": "설명 대상 불분명",
 "Judge Guarantee": "결합 불성립", "Jury Deposit": "결합 불성립",
 "Lawsuit Temperature": "결합 불성립", "Divorce Gift": "결합 불성립",
 "Meeting Workbook": "워크북 대상 불분명", "Headline Mode": "기능 토글로 읽혀 제품 불분명",
 "Priority Spec": "결합 불성립", "Headhunter Quantity": "수량 대상 불분명",
 "Swag Login": "결합 불성립", "Screening Analysis": "분석 대상 불분명(Screening 계열)",
 "Diner Coach": "코칭 대상 불분명", "Tick Habit": "결합 불성립",
 "Custody Path": "결합 불성립", "Immigration Monitor": "감시 대상 불분명",
 "Testament Sheet": "결합 불성립", "Notary Voucher": "결합 불성립",
 "Mediation Duty": "결합 불성립", "Guardianship Discount": "결합 불성립",
 "Trademark Converter": "변환 대상 불분명", "Patent Volume": "결합 불성립",
 "Copyright Warranty": "결합 불성립",
 "Withdrawal Tips": "철회 대상 불분명", "Behavior Workbook": "워크북 대상 불분명",
 "Toothbrush Mode": "기능 토글로 읽혀 제품 불분명", "Nanny Spec": "결합 불성립",
 "Sidewalk Quantity": "수량 대상 불분명", "Snorkeling Login": "결합 불성립",
 "Metronome Analysis": "분석 대상 불분명", "Workout Coach": "코칭 대상 불분명",
 "Payee Habit": "결합 불성립", "Migraine Memo": "결합 불성립",
 "Insomnia Circular": "결합 불성립", "Skydiving Recap": "결합 불성립",
 "Acne Entry": "등록 대상 불분명", "Snowboarding Plan": "계획 대상 불분명(Sailing Plan 기각 선례)",
 "Ziplining Tax": "결합 불성립", "Psoriasis Loan": "결합 불성립",
 "Sledding Fund": "결합 불성립", "Vertigo Cash": "결합 불성립",
 "Diving Duty": "결합 불성립", "Arthritis Allowance": "결합 불성립",
 "Sailing Stake": "결합 불성립", "Menopause Margin": "결합 불성립",
 "Rafting Version": "결합 불성립", "Pregnancy Link": "결합 불성립",
 "Climbing Identifier": "결합 불성립", "Fertility Category": "결합 불성립",
 "Biking Format": "결합 불성립", "Thyroid Serial": "결합 불성립",
 "Golf Marker": "결합 불성립", "Cholesterol Balance": "결합 불성립",
 "Fishing Levy": "결합 불성립", "Hypertension Due": "결합 불성립",
 "Camping Arrears": "결합 불성립", "Anemia Advance": "결합 불성립",
 "Glamping Redemption": "결합 불성립", "Heartburn Extension": "결합 불성립",
 "Stargazing Label": "결합 불성립", "Constipation Manual": "설명 대상 불분명",
 "Birdwatching Schematic": "회로도 어휘 부자연", "Concussion Layout": "결합 불성립",
 "Canyon Outline": "지형은 공예 오트라인 대상 아님", "Sprain Rendering": "렌더링 대상 불분명",
 "Geyser Notification": "결합 불성립", "Fracture Kit": "키트 대상 불분명",
 "Fjord Count": "대상 불분명", "Insulin Message": "결합 불성립",
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
out = base + r"\_dec_c11.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
