# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk25_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Change App": (0.6, "공사 변경_ORDER 관리 앱(실재 카테고리)"),
 "Vendor Tips": (0.55, "벤더 관리 팁(App→Tips 평행)"),
 "Ballot App": (0.6, "투표·선거 안내 앱(실재 카테고리)"),
 "Placement Tips": (0.55, "광고 지면 팁(App→Tips 평행)"),
 "Flea App": (0.55, "반려동물 벼룩 치료 추적 앱(실재)"),
 "Gum Tips": (0.55, "잇몸 건강 팁(App→Tips 평행)"),
 "Adjustment App": (0.6, "보험 청구 조정 관리 앱(실재 카테고리)"),
 "Training Tips": (0.55, "직원 교육 팁(App→Tips 평행)"),
 "Leave App": (0.6, "휴가 신청·관리 앱(실재 카테고리)"),
 "Change Tips": (0.55, "변경_ORDER 팁(App→Tips 평행)"),
 "Ledger App": (0.6, "비영리 장부 관리 앱(실재 카테고리)"),
 "Ballot Tips": (0.55, "투표 안내 팁(App→Tips 평행)"),
 "Cafe App": (0.6, "카페 운영 관리 앱(실재 카테고리)"),
 "Flea Tips": (0.55, "벼룩 치료 팁(App→Tips 평행)"),
 "Renovation App": (0.6, "리노베이션 프로젝트 관리 앱(실재)"),
 "Adjustment Tips": (0.55, "청구 조정 팁(App→Tips 평행)"),
}
R_DUP = {
 "Concierge Advice": "동일 배치 승인된 Concierge App/Tips와 동일 기능 의미 중복",
 "Craft Advice": "동일 배치 승인된 Craft App/Tips와 동일 기능 의미 중복",
 "Patio Advice": "동일 배치 승인된 Patio App/Tips와 동일 기능 의미 중복",
 "Vendor Advice": "동일 배치 승인된 Vendor App/Tips와 동일 기능 의미 중복",
 "Gum Advice": "동일 배치 승인된 Gum App/Tips와 동일 기능 의미 중복",
 "Training Advice": "동일 배치 승인된 Training App/Tips와 동일 기능 의미 중복",
 "Placement Advice": "동일 배치 승인된 Placement App/Tips와 동일 기능 의미 중복",
}
R = {
 "Moose Agreement": "결합 불성립", "Bison Reply": "결합 불성립",
 "Reindeer Account": "결합 불성립",
 "Vendor Tips SKIP": "",
 "Grading Workbook": "워크북 대상 불분명", "Soil Spec": "결합 불성립",
 "Pledge Login": "결합 불성립", "Hearing Analysis": "분석 대상 불분명",
 "Creative Coach": "코칭 대상 불분명", "Archive Habit": "결합 불성립",
 "Feed Advice": "동일 배치 승인된 Feed App/Tips와 동일 기능 의미 중복",
 "Permit Workbook": "워크북 대상 불분명", "Network Mode": "기능 토글로 읽혀 제품 불분명",
 "Perimeter Spec": "결합 불성립", "Runbook Quantity": "수량 대상 불분명",
 "Callback Login": "결합 불성립", "Referral Analysis": "분석 대상 불분명",
 "Feedback Coach": "코칭 대상 불분명", "Appraisal Habit": "결합 불성립",
 "Lawyer Item": "항목 대상 불분명", "Attorney Subsidy": "결합 불성립",
 "Court Workshop": "결합 불성립", "Judge Availability": "판사 대상 상태 불성립",
 "Jury Distance": "결합 불성립", "Lawsuit Requirement": "결합 불성립",
 "Dishwasher Workbook": "워크북 대상 불분명", "Blowout Mode": "기능 토글로 읽혀 제품 불분명",
 "Inhaler Spec": "결합 불성립", "Dehumidifier Quantity": "수량 대상 불분명",
 "Mortise Login": "결합 불성립", "Syntax Analysis": "분석 대상 불분명",
 "Elevator Coach": "코칭 대상 불분명", "Client Habit": "결합 불성립",
 "Divorce Forge": "결합 불성립", "Custody Gate": "결합 불성립",
 "Immigration Ticker": "결합 불성립", "Testament Code": "Testament 계열 기각 선례",
 "Notary Sum": "결합 불성립", "Mediation Levy": "결합 불성립",
 "Guardianship Repository": "결합 불성립", "Trademark Duration": "결합 불성립",
 "Patent Quote": "견적 대상 불분명", "Copyright Weight": "결합 불성립",
 "Transfer Workbook": "워크북 대상 불분명", "Ward Mode": "기능 토글로 읽혀 제품 불분명",
 "Feature Spec": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Aptitude Quantity": "수량 대상 불분명", "Networking Login": "결합 불성립",
 "Radiator Analysis": "분석 대상 불분명", "Espresso Coach": "코칭 대상 불분명",
 "Diet Habit": "결합 불성립",
 "Migraine Sale": "결합 불성립", "Insomnia Value": "결합 불성립",
 "Skydiving Number": "수치 지칭 부자연", "Acne Version": "결합 불성립",
 "Snowboarding Identifier": "결합 불성립", "Eczema Category": "결합 불성립",
 "Ziplining Format": "결합 불성립", "Psoriasis Serial": "결합 불성립",
 "Sledding Marker": "결합 불성립", "Vertigo Balance": "결합 불성립",
 "Diving Levy": "결합 불성립", "Arthritis Due": "결합 불성립",
 "Sailing Arrears": "결합 불성립", "Menopause Advance": "결합 불성립",
 "Rafting Redemption": "결합 불성립", "Pregnancy Extension": "결합 불성립",
 "Climbing Label": "결합 불성립", "Fertility Manual": "설명 대상 불분명",
 "Biking Schematic": "회로도 어휘 부자연", "Thyroid Layout": "결합 불성립",
 "Golf Rendering": "렌더링 대상 불분명", "Cholesterol Notification": "결합 불성립",
 "Fishing Message": "결합 불성립", "Hypertension Total": "결합 불성립",
 "Camping Announcement": "결합 불성립", "Anemia Calculator": "계산 대상 불분명",
 "Glamping Recorder": "기록 대상 불분명", "Heartburn Estimator": "산출 대상 불분명",
 "Stargazing Timer": "결합 불성립", "Constipation Workshop": "결합 불성립",
 "Birdwatching Stage": "결합 불성립", "Concussion Result": "결합 불성립",
 "Canyon Rank": "결합 불성립", "Sprain Trend": "결합 불성립",
 "Geyser Comparison": "비교 대상 불분명", "Fracture Proposal": "제안 대상 불분명",
 "Fjord Guarantee": "결합 불성립", "Insulin Record": "기록 대상 불분명",
 "Savanna Copy": "결합 불성립", "Tundra Reading": "결합 불성립",
 "Prairie Reference": "결합 불성립", "Marsh Forecast": "예측 대상 불분명",
 "Cove Deadline": "결합 불성립", "Cliff Duration": "결합 불성립",
 "Cavern Volume": "결합 불성립", "Oasis Diagnostic": "진단 대상 불분명",
 "Dune Progress": "결합 불성립", "Whale Authorization": "결합 불성립",
 "Dolphin Template": "결합 불성립", "Penguin Guide": "가이드 대상 불분명",
 "Flamingo Rating": "평가 대상 불분명", "Turtle Agreement": "결합 불성립",
 "Moose Reply": "결합 불성립", "Bison Account": "결합 불성립",
 "Reindeer Case": "결합 불성립",
 "Concierge Workbook": "워크북 대상 불분명", "Grading Mode": "기능 토글로 읽혀 제품 불분명",
 "Soil Quantity": "수량 대상 불분명", "Pledge Analysis": "분석 대상 불분명",
 "Hearing Coach": "코칭 대상 불분명", "Creative Habit": "결합 불성립",
 "Placement Advice SKIP": "",
 "Feed Workbook": "워크북 대상 불분명", "Permit Mode": "기능 토글로 읽혀 제품 불분명",
 "Network Spec": "결합 불성립", "Perimeter Quantity": "수량 대상 불분명",
 "Runbook Login": "결합 불성립", "Callback Analysis": "분석 대상 불분명",
 "Referral Coach": "코칭 대상 불분명", "Feedback Habit": "결합 불성립",
 "Lawyer Unit": "결합 불성립", "Attorney Discount": "결합 불성립",
 "Court Guardian": "감시 대상 불분명", "Judge Eligibility": "판사 대상 상태 불성립",
 "Jury Range": "결합 불성립", "Lawsuit Depreciation": "결합 불성립",
 "Craft Workbook": "워크북 대상 불분명", "Dishwasher Mode": "기능 토글로 읽혀 제품 불분명",
 "Blowout Spec": "결합 불성립", "Inhaler Quantity": "수량 대상 불분명",
 "Dehumidifier Login": "결합 불성립", "Mortise Analysis": "분석 대상 불분명",
 "Syntax Coach": "코칭 대상 불분명", "Elevator Habit": "결합 불성립",
 "Divorce Cascade": "결합 불성립", "Custody Nexus": "결합 불성립",
 "Immigration Line": "결합 불성립", "Testament List": "Testament 계열 기각 선례",
 "Notary Debt": "결합 불성립", "Mediation Due": "결합 불성립",
 "Guardianship Announcement": "결합 불성립", "Trademark Volume": "결합 불성립",
 "Patent Warranty": "결합 불성립", "Copyright Distance": "결합 불성립",
 "Patio Workbook SKIP": "",
 "Transfer Mode": "기능 토글로 읽혀 제품 불분명", "Ward Spec": "결합 불성립",
 "Feature Quantity": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Aptitude Login": "결합 불성립", "Networking Analysis": "분석 대상 불분명",
 "Radiator Coach": "코칭 대상 불분명", "Espresso Habit": "결합 불성립",
 "Migraine Charge": "결합 불성립", "Insomnia Stake": "결합 불성립",
 "Skydiving Version": "결합 불성립", "Acne Link": "결합 불성립",
 "Snowboarding Category": "결합 불성립", "Eczema Attribute": "결합 불성립",
 "Ziplining Serial": "결합 불성립", "Psoriasis Token": "결합 불성립",
 "Sledding Balance": "결합 불성립", "Vertigo Interest": "결합 불성립",
 "Diving Due": "결합 불성립", "Arthritis Subsidy": "결합 불성립",
 "Sailing Advance": "결합 불성립", "Menopause Penalty": "결합 불성립",
 "Rafting Extension": "결합 불성립", "Pregnancy Trial": "결합 불성립",
 "Climbing Manual": "설명 대상 불분명", "Fertility Worksheet": "학습지 근거 약함",
 "Biking Layout": "결합 불성립", "Thyroid Sketch": "제품성 불분명",
 "Golf Notification": "결합 불성립", "Cholesterol Kit": "키트 대상 불분명",
 "Fishing Total": "결합 불성립", "Hypertension Widget": "위젯 대상 불분명",
 "Camping Calculator": "계산 대상 불분명", "Anemia Converter": "변환 대상 불분명",
 "Patio Workbook": "워크북 대상 불분명",
}
del R["Vendor Tips SKIP"]
del R["Placement Advice SKIP"]
del R["Patio Workbook SKIP"]
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
out = base + r"\_dec_c25.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
