# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk27_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Pallet App": (0.55, "팔레트 운영 관리 앱(실재)"),
 "Throughput App": (0.6, "생산 처리량 모니터링 앱(실재 카테고리)"),
 "Silo Tips": (0.55, "사일로 관리 팁(App→Tips 평행)"),
 "Recruiter App": (0.6, "리크루터 채용 관리 앱(실재 카테고리)"),
 "Lanyard Tips": (0.55, "명찰·래니야드 팁(App→Tips 평행)"),
 "Injury App": (0.55, "부상 기록·청구 관리 앱(실재)"),
 "Creditor Tips": (0.55, "채권 관리 팁(App→Tips 평행)"),
 "Redline App": (0.6, "계약서 수정(레드라인) 협업 앱(실재 카테고리)"),
 "Pallet Tips": (0.55, "팔레트 운영 팁(App→Tips 평행)"),
 "Alumni App": (0.6, "동문 관리 앱(실재 카테고리)"),
 "Throughput Tips": (0.55, "처리량 개선 팁(App→Tips 평행)"),
 "Sentiment App": (0.6, "고객 감성 분석 앱(실재 카테고리)"),
 "Recruiter Tips": (0.55, "채용 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Coverage Advice": "동일 배치 승인된 Coverage App/Tips와 동일 기능 의미 중복",
 "Checkup Advice": "동일 배치 승인된 Checkup App/Tips와 동일 기능 의미 중복",
 "Reefer Advice": "동일 배치 승인된 Reefer App/Tips와 동일 기능 의미 중복",
 "Silo Advice": "동일 배치 승인된 Silo App/Tips와 동일 기능 의미 중복",
 "Lanyard Advice": "동일 배치 승인된 Lanyard App/Tips와 동일 기능 의미 중복",
}
R = {
 "Acne Detail": "결합 불성립", "Snowboarding Field": "결합 불성립",
 "Eczema Format": "결합 불성립", "Ziplining Signature": "결합 불성립",
 "Psoriasis Marker": "결합 불성립", "Sledding Asset": "결합 불성립",
 "Vertigo Levy": "결합 불성립", "Diving Discount": "결합 불성립",
 "Arthritis Arrears": "결합 불성립", "Sailing Markup": "결합 불성립",
 "Menopause Redemption": "결합 불성립", "Rafting Graph": "그래프 대상 불분명",
 "Pregnancy Label": "결합 불성립", "Climbing Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Fertility Schematic": "회로도 어휘 부자연", "Biking Outline": "지형은 공예 오트라인 대상 아님",
 "Thyroid Rendering": "렌더링 대상 불분명", "Golf Count": "대상 불분명",
 "Cholesterol Message": "결합 불성립", "Fishing Repository": "결합 불성립",
 "Hypertension Announcement": "결합 불성립", "Camping Generator": "생성 대상 불분명",
 "Anemia Recorder": "기록 대상 불분명", "Glamping Detector": "탐지 대상 불분명",
 "Heartburn Timer": "결합 불성립", "Stargazing Helper": "결합 불성립",
 "Constipation Stage": "결합 불성립", "Birdwatching Rank": "결합 불성립",
 "Concussion Trend": "결합 불성립", "Canyon Proposal": "제안 대상 불분명",
 "Sprain Guarantee": "결합 불성립", "Geyser Record": "기록 대상 불분명",
 "Fracture Copy": "결합 불성립", "Fjord Reading": "결합 불성립",
 "Insulin Reference": "결합 불성립", "Savanna Forecast": "예측 대상 불분명",
 "Tundra Deadline": "결합 불성립", "Prairie Duration": "결합 불성립",
 "Marsh Volume": "결합 불성립", "Cove Diagnostic": "진단 대상 불분명",
 "Cliff Progress": "결합 불성립", "Cavern Authorization": "결합 불성립",
 "Oasis Template": "결합 불성립", "Dune Guide": "가이드 대상 불분명",
 "Whale Rating": "평가 대상 불분명", "Dolphin Agreement": "결합 불성립",
 "Penguin Reply": "결합 불성립", "Flamingo Account": "결합 불성립",
 "Turtle Case": "결합 불성립", "Moose Match": "결합 불성립",
 "Bison Validation": "결합 불성립", "Reindeer Lookup": "탐색 대상 불분명",
 "Leave Workbook": "워크북 대상 불분명", "Change Mode": "기능 토글로 읽혀 제품 불분명",
 "Vendor Spec": "결합 불성립", "Concierge Quantity": "수량 대상 불분명",
 "Grading Login": "결합 불성립", "Soil Coach": "코칭 대상 불분명",
 "Ledger Workbook": "워크북 대상 불분명", "Ballot Mode": "기능 토글로 읽혀 제품 불분명",
 "Placement Spec": "결합 불성립", "Feed Quantity": "수량 대상 불분명",
 "Permit Login": "결합 불성립", "Network Analysis": "분석 대상 불분명",
 "Perimeter Coach": "코칭 대상 불분명", "Runbook Habit": "결합 불성립",
 "Lawyer Price": "가격 지칭 부자연", "Attorney Penalty": "결합 불성립",
 "Court Result": "결합 불성립", "Judge Appointment": "판사 대상 임명 불성립",
 "Jury Clock": "결합 불성립", "Lawsuit Guarantor": "결합 불성립",
 "Cafe Workbook": "워크북 대상 불분명", "Flea Mode": "기능 토글로 읽혀 제품 불분명",
 "Gum Spec": "결합 불성립", "Craft Quantity": "수량 대상 불분명",
 "Dishwasher Login": "결합 불성립", "Blowout Analysis": "분석 대상 불분명",
 "Inhaler Coach": "코칭 대상 불분명", "Dehumidifier Habit": "결합 불성립",
 "Divorce Watch": "결합 불성립", "Custody Manager": "결합 불성립",
 "Immigration Report": "보고 대상 불분명", "Testament Sample": "Testament 계열 기각 선례",
 "Notary Sale": "결합 불성립", "Mediation Arrears": "결합 불성립",
 "Guardianship Generator": "생성 대상 불분명", "Trademark Authorization": "결합 불성립",
 "Patent Nomination": "결합 불성립", "Copyright Type": "결합 불성립",
 "Renovation Workbook": "워크북 대상 불분명", "Adjustment Mode": "기능 토글로 읽혀 제품 불분명",
 "Training Spec": "결합 불성립", "Patio Quantity": "수량 대상 불분명",
 "Transfer Login": "결합 불성립", "Ward Analysis": "분석 대상 불분명",
 "Feature Coach": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Aptitude Habit": "결합 불성립",
 "Migraine Tariff": "결합 불성립", "Insomnia Number": "수치 지칭 부자연",
 "Skydiving Detail": "결합 불성립", "Acne Identifier": "결합 불성립",
 "Snowboarding Format": "결합 불성립", "Eczema Serial": "결합 불성립",
 "Ziplining Marker": "결합 불성립", "Psoriasis Balance": "결합 불성립",
 "Sledding Levy": "결합 불성립", "Vertigo Due": "결합 불성립",
 "Diving Arrears": "결합 불성립", "Arthritis Advance": "결합 불성립",
 "Sailing Redemption": "결합 불성립", "Menopause Extension": "결합 불성립",
 "Rafting Label": "결합 불성립", "Pregnancy Manual": "설명 대상 불분명",
 "Climbing Schematic": "회로도 어휘 부자연", "Fertility Layout": "결합 불성립",
 "Biking Rendering": "렌더링 대상 불분명", "Thyroid Notification": "결합 불성립",
 "Golf Message": "결합 불성립", "Cholesterol Total": "결합 불성립",
 "Fishing Announcement": "결합 불성립", "Hypertension Calculator": "계산 대상 불분명",
 "Camping Recorder": "기록 대상 불분명", "Anemia Estimator": "산출 대상 불분명",
 "Glamping Timer": "결합 불성립", "Heartburn Workshop": "결합 불성립",
 "Stargazing Stage": "결합 불성립", "Constipation Result": "결합 불성립",
 "Birdwatching Trend": "결합 불성립", "Concussion Comparison": "비교 대상 불분명",
 "Canyon Guarantee": "결합 불성립", "Sprain Record": "기록 대상 불분명",
 "Geyser Copy": "결합 불성립", "Fracture Reading": "결합 불성립",
 "Fjord Reference": "결합 불성립", "Insulin Forecast": "예측 대상 불분명",
 "Savanna Deadline": "결합 불성립", "Tundra Duration": "결합 불성립",
 "Prairie Volume": "결합 불성립", "Marsh Diagnostic": "진단 대상 불분명",
 "Cove Progress": "결합 불성립", "Cliff Authorization": "결합 불성립",
 "Cavern Template": "결합 불성립", "Oasis Guide": "가이드 대상 불분명",
 "Dune Rating": "평가 대상 불분명", "Whale Agreement": "결합 불성립",
 "Dolphin Reply": "결합 불성립", "Penguin Account": "결합 불성립",
 "Flamingo Case": "결합 불성립", "Turtle Match": "결합 불성립",
 "Moose Validation": "결합 불성립", "Bison Lookup": "탐색 대상 불분명",
 "Reindeer Ping": "결합 불성립",
 "Coverage Workbook": "워크북 대상 불분명", "Leave Mode": "기능 토글로 읽혀 제품 불분명",
 "Change Spec": "결합 불성립", "Vendor Quantity": "수량 대상 불분명",
 "Concierge Login": "결합 불성립", "Grading Analysis": "분석 대상 불분명",
 "Soil Habit": "결합 불성립",
 "Ledger Mode": "기능 토글로 읽혀 제품 불분명", "Ballot Spec": "결합 불성립",
 "Placement Quantity": "수량 대상 불분명", "Feed Login": "결합 불성립",
 "Permit Analysis": "분석 대상 불분명", "Network Coach": "코칭 대상 불분명",
 "Perimeter Habit": "결합 불성립",
 "Lawyer Fare": "결합 불성립", "Attorney Markup": "결합 불성립",
 "Court Streak": "결합 불성립", "Judge Feedback": "판사 대상 피드백 불성립",
 "Jury Time": "결합 불성립", "Lawsuit Tuner": "결합 불성립",
 "Checkup Workbook": "워크북 대상 불분명", "Cafe Mode": "기능 토글로 읽혀 제품 불분명",
 "Flea Spec": "결합 불성립", "Gum Quantity": "수량 대상 불분명",
 "Craft Login": "결합 불성립", "Dishwasher Analysis": "분석 대상 불분명",
 "Blowout Coach": "코칭 대상 불분명", "Inhaler Habit": "결합 불성립",
 "Divorce Scope": "결합 불성립",
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
out = base + r"\_dec_c27.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
