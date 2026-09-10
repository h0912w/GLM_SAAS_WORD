# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk26_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Coverage App": (0.6, "보험 커버리지 관리 앱(실재 카테고리)"),
 "Leave Tips": (0.55, "휴가 관리 팁(App→Tips 평행)"),
 "Ledger Tips": (0.55, "장부 관리 팁(App→Tips 평행)"),
 "Checkup App": (0.6, "차량 점검 관리 앱(실재 카테고리)"),
 "Cafe Tips": (0.55, "카페 운영 팁(App→Tips 평행)"),
 "Reefer App": (0.6, "냉장 컨테이너 모니터링 앱(실재)"),
 "Renovation Tips": (0.55, "리노베이션 팁(App→Tips 평행)"),
 "Coverage Tips": (0.55, "커버리지 관리 팁(App→Tips 평행)"),
 "Silo App": (0.55, "사일로 저장·모니터링 앱(실재)"),
 "Checkup Tips": (0.55, "차량 점검 팁(App→Tips 평행)"),
 "Lanyard App": (0.55, "이벤트 명찰·래니야드 관리 앱(실재)"),
 "Creditor App": (0.55, "채권자 관리 앱(실재)"),
 "Reefer Tips": (0.55, "냉장 컨테이너 운영 팁(App→Tips 평행)"),
}
R_DUP = {
 "Change Advice": "동일 배치 승인된 Change App/Tips와 동일 기능 의미 중복",
 "Ballot Advice": "동일 배치 승인된 Ballot App/Tips와 동일 기능 의미 중복",
 "Adjustment Advice": "동일 배치 승인된 Adjustment App/Tips와 동일 기능 의미 중복",
 "Leave Advice": "동일 배치 승인된 Leave App/Tips와 동일 기능 의미 중복",
 "Ledger Advice": "동일 배치 승인된 Ledger App/Tips와 동일 기능 의미 중복",
 "Cafe Advice": "동일 배치 승인된 Cafe App/Tips와 동일 기능 의미 중복",
 "Renovation Advice": "동일 배치 승인된 Renovation App/Tips와 동일 기능 의미 중복",
}
R = {
 "Glamping Estimator": "산출 대상 불분명", "Heartburn Checker": "검사 대상 불분명",
 "Stargazing Workshop": "결합 불성립", "Constipation Guardian": "감시 대상 불분명",
 "Birdwatching Result": "결합 불성립", "Concussion Streak": "결합 불성립",
 "Canyon Trend": "결합 불성립", "Sprain Comparison": "비교 대상 불분명",
 "Geyser Proposal": "제안 대상 불분명", "Fracture Guarantee": "결합 불성립",
 "Fjord Record": "기록 대상 불분명", "Insulin Copy": "결합 불성립",
 "Savanna Reading": "결합 불성립", "Tundra Reference": "결합 불성립",
 "Prairie Forecast": "예측 대상 불분명", "Marsh Deadline": "결합 불성립",
 "Cove Duration": "결합 불성립", "Cliff Volume": "결합 불성립",
 "Cavern Diagnostic": "진단 대상 불분명", "Oasis Progress": "결합 불성립",
 "Dune Authorization": "결합 불성립", "Whale Template": "결합 불성립",
 "Dolphin Guide": "가이드 대상 불분명", "Penguin Rating": "평가 대상 불분명",
 "Flamingo Agreement": "결합 불성립", "Turtle Reply": "결합 불성립",
 "Moose Account": "결합 불성립", "Bison Case": "결합 불성립",
 "Reindeer Match": "결합 불성립",
 "Concierge Mode": "기능 토글로 읽혀 제품 불분명", "Vendor Workbook": "워크북 대상 불분명",
 "Grading Spec": "결합 불성립",
 "Soil Login": "결합 불성립", "Pledge Coach": "코칭 대상 불분명",
 "Hearing Habit": "결합 불성립",
 "Placement Workbook": "워크북 대상 불분명", "Feed Mode": "기능 토글로 읽혀 제품 불분명",
 "Permit Spec": "결합 불성립", "Network Quantity": "수량 대상 불분명",
 "Perimeter Login": "결합 불성립", "Runbook Analysis": "분석 대상 불분명",
 "Callback Coach": "코칭 대상 불분명", "Referral Habit": "결합 불성립",
 "Lawyer Plan": "계획 대상 불분명", "Attorney Arrears": "결합 불성립",
 "Court Helper": "결합 불성립", "Judge Broadcast": "결합 불성립",
 "Jury Limit": "결합 불성립", "Lawsuit Resignation": "결합 불성립",
 "Flea Advice": "동일 배치 승인된 Flea App/Tips와 동일 기능 의미 중복",
 "Gum Workbook": "워크북 대상 불분명", "Craft Mode": "기능 토글로 읽혀 제품 불분명",
 "Dishwasher Spec": "결합 불성립", "Blowout Quantity": "수량 대상 불분명",
 "Inhaler Login": "결합 불성립", "Dehumidifier Analysis": "분석 대상 불분명",
 "Mortise Coach": "코칭 대상 불분명", "Syntax Habit": "결합 불성립",
 "Divorce Bridge": "결합 불성립", "Custody Atlas": "결합 불성립",
 "Immigration Window": "결합 불성립", "Testament Table": "Testament 계열 기각 선례",
 "Notary Fund": "결합 불성립", "Mediation Subsidy": "결합 불성립",
 "Guardianship Calculator": "계산 대상 불분명", "Trademark Diagnostic": "진단 대상 불분명",
 "Patent Deposit": "결합 불성립", "Copyright Range": "결합 불성립",
 "Training Workbook": "워크북 대상 불분명", "Patio Mode": "기능 토글로 읽혀 제품 불분명",
 "Transfer Spec": "결합 불성립", "Ward Quantity": "수량 대상 불분명",
 "Feature Login": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Aptitude Analysis": "분석 대상 불분명", "Networking Coach": "코칭 대상 불분명",
 "Radiator Habit": "결합 불성립",
 "Migraine Duty": "결합 불성립", "Insomnia Margin": "결합 불성립",
 "Skydiving Link": "결합 불성립", "Acne Rule": "결합 불성립",
 "Snowboarding Attribute": "결합 불성립", "Eczema Field": "결합 불성립",
 "Ziplining Token": "결합 불성립", "Psoriasis Signature": "결합 불성립",
 "Sledding Interest": "결합 불성립", "Vertigo Asset": "결합 불성립",
 "Diving Subsidy": "결합 불성립", "Arthritis Discount": "결합 불성립",
 "Sailing Penalty": "결합 불성립", "Menopause Markup": "결합 불성립",
 "Rafting Trial": "결합 불성립", "Pregnancy Graph": "그래프 대상 불분명",
 "Climbing Worksheet": "학습지 근거 약함", "Fertility Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Biking Sketch": "제품성 불분명", "Thyroid Outline": "지형은 공예 오트라인 대상 아님",
 "Golf Kit": "키트 대상 불분명", "Cholesterol Count": "대상 불분명",
 "Fishing Widget": "위젯 대상 불분명", "Hypertension Repository": "결합 불성립",
 "Camping Converter": "변환 대상 불분명", "Anemia Generator": "생성 대상 불분명",
 "Glamping Checker": "검사 대상 불분명", "Heartburn Detector": "탐지 대상 불분명",
 "Stargazing Guardian": "감시 대상 불분명", "Constipation Helper": "결합 불성립",
 "Birdwatching Streak": "결합 불성립", "Concussion Rank": "결합 불성립",
 "Canyon Comparison": "비교 대상 불분명", "Sprain Proposal": "제안 대상 불분명",
 "Geyser Guarantee": "결합 불성립", "Fracture Record": "기록 대상 불분명",
 "Fjord Copy": "결합 불성립", "Insulin Reading": "결합 불성립",
 "Savanna Reference": "결합 불성립", "Tundra Forecast": "예측 대상 불분명",
 "Prairie Deadline": "결합 불성립", "Marsh Duration": "결합 불성립",
 "Cove Volume": "결합 불성립", "Cliff Diagnostic": "진단 대상 불분명",
 "Cavern Progress": "결합 불성립", "Oasis Authorization": "결합 불성립",
 "Dune Template": "결합 불성립", "Whale Guide": "가이드 대상 불분명",
 "Dolphin Rating": "평가 대상 불분명", "Penguin Agreement": "결합 불성립",
 "Flamingo Reply": "결합 불성립", "Turtle Account": "결합 불성립",
 "Moose Case": "결합 불성립", "Bison Match": "결합 불성립",
 "Reindeer Validation": "결합 불성립",
 "Vendor Mode SKIP": "",
 "Concierge Spec": "결합 불성립", "Grading Quantity": "수량 대상 불분명",
 "Soil Analysis": "분석 대상 불분명", "Pledge Habit": "결합 불성립",
 "Ballot Workbook": "워크북 대상 불분명", "Change Workbook": "워크북 대상 불분명",
 "Placement Mode": "기능 토글로 읽혀 제품 불분명",
 "Feed Spec": "결합 불성립", "Permit Quantity": "수량 대상 불분명",
 "Network Login": "결합 불성립", "Perimeter Analysis": "분석 대상 불분명",
 "Runbook Coach": "코칭 대상 불분명", "Callback Habit": "결합 불성립",
 "Lawyer Cost": "결합 불성립", "Attorney Advance": "결합 불성립",
 "Court Stage": "결합 불성립", "Judge Barcode": "결합 불성립",
 "Jury Type": "결합 불성립", "Lawsuit Hazard": "결합 불성립",
 "Flea Workbook": "워크북 대상 불분명", "Gum Mode": "기능 토글로 읽혀 제품 불분명",
 "Craft Spec": "결합 불성립", "Dishwasher Quantity": "수량 대상 불분명",
 "Blowout Login": "결합 불성립", "Inhaler Analysis": "분석 대상 불분명",
 "Dehumidifier Coach": "코칭 대상 불분명", "Mortise Habit": "결합 불성립",
 "Divorce Signal": "결합 불성립", "Custody Keeper": "결합 불성립",
 "Immigration Roll": "결합 불성립", "Testament Slip": "Testament 계열 기각 선례",
 "Notary Cash": "결합 불성립", "Mediation Discount": "결합 불성립",
 "Guardianship Converter": "변환 대상 불분명", "Trademark Progress": "결합 불성립",
 "Patent Certification": "결합 불성립", "Copyright Limit": "결합 불성립",
 "Adjustment Workbook": "워크북 대상 불분명", "Vendor Mode": "기능 토글로 읽혀 제품 불분명",
 "Training Mode": "기능 토글로 읽혀 제품 불분명",
 "Patio Spec": "결합 불성립", "Transfer Quantity": "수량 대상 불분명",
 "Ward Login": "결합 불성립", "Feature Analysis": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Aptitude Coach": "코칭 대상 불분명", "Networking Habit": "결합 불성립",
 "Migraine Allowance": "결합 불성립", "Insomnia Fine": "결합 불성립",
 "Skydiving Rule": "결합 불성립",
}
del R["Vendor Mode SKIP"]
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
out = base + r"\_dec_c26.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
