# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk19_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Archive App": (0.6, "미디어 아카이브 관리 앱(DAM 실재 카테고리)"),
 "Orthodontics App": (0.6, "교정 치료 관리 앱(실재 카테고리)"),
 "Stroller Tips": (0.55, "유모차 관리 팁(App→Tips 평행)"),
 "Spa Advice R_DUP_PLACEHOLDER": "",
 "Driver Tips": (0.55, "운전기사 관리 팁(App→Tips 평행)"),
 "Roaming Advice R_DUP_PLACEHOLDER": "",
 "Appraisal App": (0.6, "차량 감정 평가 앱(실재 카테고리)"),
 "Franchise Tips": (0.55, "프랜차이즈 운영 팁(App→Tips 평행)"),
 "Discharge Advice R_DUP_PLACEHOLDER": "",
 "Client App": (0.6, "사진작가 고객 관리 앱(실재 카테고리)"),
 "Cake Tips": (0.55, "케이크 주문 팁(App→Tips 평행)"),
 "Patent Lookup": (0.55, "특허 검색 도구(실재 기능)"),
 "Diet App": (0.55, "반려동물 식단 관리 앱(실재)"),
 "Orthodontics Tips": (0.55, "교정 관리 팁(App→Tips 평행)"),
 "Stroller Advice R_DUP_PLACEHOLDER": "",
 "Migraine Plan": (0.55, "편두통 관리 계획(건강 관리 플랜 축)"),
 "Creative App": (0.55, "마케팅 크리에이티브 자산 관리 앱(실재)"),
 "Archive Tips": (0.55, "아카이브 관리 팁(App→Tips 평행)"),
 "Driver Advice R_DUP_PLACEHOLDER": "",
}
del A["Spa Advice R_DUP_PLACEHOLDER"]
del A["Roaming Advice R_DUP_PLACEHOLDER"]
del A["Discharge Advice R_DUP_PLACEHOLDER"]
del A["Stroller Advice R_DUP_PLACEHOLDER"]
del A["Driver Advice R_DUP_PLACEHOLDER"]
R_DUP = {
 "Spa Advice": "동일 배치 승인된 Spa App/Tips와 동일 기능 의미 중복",
 "Roaming Advice": "동일 배치 승인된 Roaming App/Tips와 동일 기능 의미 중복",
 "Discharge Advice": "동일 배치 승인된 Discharge App/Tips와 동일 기능 의미 중복",
 "Stroller Advice": "동일 배치 승인된 Stroller App/Tips와 동일 기능 의미 중복",
 "Driver Advice": "동일 배치 승인된 Driver App/Tips와 동일 기능 의미 중복",
}
R = {
 "Roadtrip Spec": "결합 불성립", "Accordion Quantity": "수량 대상 불분명",
 "Allergy Login": "결합 불성립", "Wire Analysis": "분석 대상 불분명",
 "Divorce Coach": "코칭 대상 불분명", "Chassis Habit": "결합 불성립",
 "Custody Center": "기관 지칭으로 서비스 대상 불분명", "Immigration Booth": "시설 지칭으로 불성립",
 "Testament Feed": "Testament 계열 기각 선례", "Notary Recap": "요약 대상 불분명",
 "Mediation Category": "결합 불성립", "Guardianship Schematic": "회로도 어휘 부자연",
 "Trademark Rank": "결합 불성립", "Copyright Video": "결합 불성립",
 "Curb Mode": "기능 토글로 읽혀 제품 불분명", "Vineyard Spec": "결합 불성립",
 "Accompanist Quantity": "수량 대상 불분명", "Illness Login": "결합 불성립",
 "Debtor Analysis": "분석 대상 불분명", "Flatbed Coach": "코칭 대상 불분명",
 "Neighborhood Habit": "결합 불성립",
 "Migraine Unit": "결합 불성립", "Insomnia Tax": "결합 불성립",
 "Skydiving Fund": "결합 불성립", "Acne Cash": "결합 불성립",
 "Snowboarding Allowance": "결합 불성립", "Eczema Tariff": "결합 불성립",
 "Ziplining Margin": "결합 불성립", "Psoriasis Fine": "결합 불성립",
 "Sledding Link": "결합 불성립", "Vertigo Rule": "결합 불성립",
 "Diving Category": "결합 불성립", "Arthritis Attribute": "결합 불성립",
 "Sailing Serial": "결합 불성립", "Menopause Token": "결합 불성립",
 "Rafting Balance": "결합 불성립", "Pregnancy Interest": "결합 불성립",
 "Climbing Due": "결합 불성립", "Fertility Subsidy": "결합 불성립",
 "Biking Advance": "결합 불성립", "Thyroid Penalty": "결합 불성립",
 "Golf Extension": "결합 불성립", "Cholesterol Trial": "결합 불성립",
 "Fishing Manual": "설명 대상 불분명", "Hypertension Worksheet": "학습지 근거 약함",
 "Camping Layout": "결합 불성립", "Anemia Sketch": "제품성 불분명",
 "Glamping Notification": "결합 불성립", "Heartburn Kit": "키트 대상 불분명",
 "Stargazing Total": "결합 불성립", "Constipation Widget": "위젯 대상 불분명",
 "Birdwatching Calculator": "계산 대상 불분명", "Concussion Converter": "변환 대상 불분명",
 "Canyon Recorder": "기록 대상 불분명", "Sprain Estimator": "산출 대상 불분명",
 "Geyser Checker": "검사 대상 불분명", "Fracture Detector": "탐지 대상 불분명",
 "Fjord Timer": "결합 불성립", "Insulin Workshop": "결합 불성립",
 "Savanna Guardian": "감시 대상 불분명", "Tundra Helper": "결합 불성립",
 "Prairie Stage": "결합 불성립", "Marsh Result": "결합 불성립",
 "Cove Streak": "결합 불성립", "Cliff Rank": "결합 불성립",
 "Cavern Trend": "결합 불성립", "Oasis Comparison": "비교 대상 불분명",
 "Dune Proposal": "제안 대상 불분명", "Whale Guarantee": "결합 불성립",
 "Dolphin Record": "기록 대상 불분명", "Penguin Copy": "결합 불성립",
 "Flamingo Reading": "결합 불성립", "Turtle Reference": "결합 불성립",
 "Moose Forecast": "예측 대상 불분명", "Bison Deadline": "결합 불성립",
 "Reindeer Duration": "결합 불성립",
 "Audit Workbook": "워크북 대상 불분명", "Pipeline Mode": "기능 토글로 읽혀 제품 불분명",
 "Refund Spec": "결합 불성립", "Reference Quantity": "수량 대상 불분명",
 "Agenda Login": "결합 불성립", "Financing Analysis": "분석 대상 불분명",
 "Compliance Coach": "코칭 대상 불분명", "Appointment Habit": "결합 불성립",
 "Session Mode": "기능 토글로 읽혀 제품 불분명", "Milestone Spec": "결합 불성립",
 "Wellness Quantity": "수량 대상 불분명", "Scheduling Login": "결합 불성립",
 "Snow Analysis": "분석 대상 불분명", "Inventory Coach": "코칭 대상 불분명",
 "Alteration Habit": "결합 불성립",
 "Lawyer Tab": "결합 불성립", "Attorney Format": "결합 불성립",
 "Court Repository": "결합 불성립", "Judge Rating": "평가 대상 불분명",
 "Jury Refund": "결합 불성립", "Lawsuit Breakdown": "결합 불성립",
 "Closing Workbook": "워크북 대상 불분명", "Sponge Mode": "기능 토글로 읽혀 제품 불분명",
 "Trap Spec": "결합 불성립",
 "Roadtrip Quantity": "수량 대상 불분명", "Accordion Login": "결합 불성립",
 "Allergy Analysis": "분석 대상 불분명", "Wire Coach": "코칭 대상 불분명",
 "Divorce Habit": "결합 불성립", "Custody Zone": "결합 불성립",
 "Immigration Kiosk": "시설 지칭으로 불성립", "Testament Draft": "Testament 계열 기각 선례",
 "Notary Entry": "등록 대상 불분명", "Mediation Attribute": "결합 불성립",
 "Guardianship Layout": "결합 불성립", "Trademark Trend": "결합 불성립",
 "Patent Ping": "결합 불성립", "Copyright Diary": "결합 불성립",
 "Xray Workbook": "워크북 대상 불분명", "Spa Workbook": "워크북 대상 불분명",
 "Curb Spec": "결합 불성립", "Vineyard Quantity": "수량 대상 불분명",
 "Accompanist Login": "결합 불성립", "Illness Analysis": "분석 대상 불분명",
 "Debtor Coach": "코칭 대상 불분명", "Flatbed Habit": "결합 불성립",
 "Insomnia Loan": "결합 불성립", "Skydiving Cash": "결합 불성립",
 "Acne Sale": "결합 불성립", "Snowboarding Tariff": "결합 불성립",
 "Eczema Value": "결합 불성립", "Ziplining Fine": "결합 불성립",
 "Psoriasis Number": "수치 지칭 부자연", "Sledding Rule": "결합 불성립",
 "Vertigo Detail": "결합 불성립", "Diving Attribute": "결합 불성립",
 "Arthritis Field": "결합 불성립", "Sailing Token": "결합 불성립",
 "Menopause Signature": "결합 불성립", "Rafting Interest": "결합 불성립",
 "Pregnancy Asset": "결합 불성립", "Climbing Subsidy": "결합 불성립",
 "Fertility Discount": "결합 불성립", "Biking Penalty": "결합 불성립",
 "Thyroid Markup": "결합 불성립", "Golf Trial": "결합 불성립",
 "Cholesterol Graph": "그래프 대상 불분명", "Fishing Worksheet": "학습지 근거 약함",
 "Hypertension Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Camping Sketch": "제품성 불분명", "Anemia Outline": "지형은 공예 오트라인 대상 아님",
 "Glamping Kit": "키트 대상 불분명", "Heartburn Count": "대상 불분명",
 "Stargazing Widget": "위젯 대상 불분명", "Constipation Repository": "결합 불성립",
 "Birdwatching Converter": "변환 대상 불분명", "Concussion Generator": "생성 대상 불분명",
 "Canyon Estimator": "산출 대상 불분명", "Sprain Checker": "검사 대상 불분명",
 "Geyser Detector": "탐지 대상 불분명", "Fracture Timer": "결합 불성립",
 "Fjord Workshop": "결합 불성립", "Insulin Guardian": "감시 대상 불분명",
 "Savanna Helper": "결합 불성립", "Tundra Stage": "결합 불성립",
 "Prairie Result": "결합 불성립", "Marsh Streak": "결합 불성립",
 "Cove Rank": "결합 불성립", "Cliff Trend": "결합 불성립",
 "Cavern Comparison": "비교 대상 불분명", "Oasis Proposal": "제안 대상 불분명",
 "Dune Guarantee": "결합 불성립", "Whale Record": "기록 대상 불분명",
 "Dolphin Copy": "결합 불성립", "Penguin Reading": "결합 불성립",
 "Flamingo Reference": "결합 불성립", "Turtle Forecast": "예측 대상 불분명",
 "Moose Deadline": "결합 불성립", "Bison Duration": "결합 불성립",
 "Reindeer Volume": "결합 불성립",
 "Audit Mode": "기능 토글로 읽혀 제품 불분명", "Pipeline Spec": "결합 불성립",
 "Refund Quantity": "수량 대상 불분명", "Reference Login": "결합 불성립",
 "Roaming Workbook": "워크북 대상 불분명",
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
out = base + r"\_dec_c19.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
