# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk23_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Ward App": (0.55, "행정구 서비스 안내 앱(실재)"),
 "Grading App": (0.6, "교사 채점 관리 앱(실재 카테고리)"),
 "Permit App": (0.6, "허가증 신청·관리 앱(실재 카테고리)"),
 "Network Tips": (0.55, "네트워크 관리 팁(App→Tips 평행)"),
 "Dishwasher App": (0.55, "식기세척기 제어 앱(스마트 가전 실재)"),
 "Blowout Tips": (0.55, "블로우 관리 팁(App→Tips 평행)"),
 "Transfer App": (0.55, "편입·전학 절차 관리 앱(실재)"),
 "Ward Tips": (0.55, "행정구 서비스 팁(App→Tips 평행)"),
 "Concierge App": (0.6, "컨시어지 서비스 앱(실재 카테고리)"),
 "Grading Tips": (0.55, "채점 팁(App→Tips 평행)"),
 "Feed App": (0.6, "피드 리더 앱(실재 카테고리)"),
 "Permit Tips": (0.55, "허가 신청 팁(App→Tips 평행)"),
}
R_DUP = {
 "Soil Advice": "동일 배치 승인된 Soil App/Tips와 동일 기능 의미 중복",
 "Perimeter Advice": "동일 배치 승인된 Perimeter App/Tips와 동일 기능 의미 중복",
 "Network Advice": "동일 배치 승인된 Network App/Tips와 동일 기능 의미 중복",
 "Inhaler Advice": "동일 배치 승인된 Inhaler App/Tips와 동일 기능 의미 중복",
}
R = {
 "Copyright Onboarding": "결합 불성립",
 "Feature Tips": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Aptitude Advice": "동일 배치 승인된 Aptitude App/Tips와 동일 기능 의미 중복",
 "Radiator Mode": "기능 토글로 읽혀 제품 불분명", "Espresso Spec": "결합 불성립",
 "Diet Quantity": "수량 대상 불분명", "Orthodontics Login": "결합 불성립",
 "Stroller Analysis": "분석 대상 불분명", "Spa Coach": "코칭 대상 불분명",
 "Migraine Sum": "결합 불성립", "Insomnia Charge": "결합 불성립",
 "Skydiving Value": "결합 불성립", "Acne Stake": "결합 불성립",
 "Snowboarding Version": "결합 불성립", "Eczema Link": "결합 불성립",
 "Ziplining Identifier": "결합 불성립", "Psoriasis Category": "결합 불성립",
 "Sledding Format": "결합 불성립", "Vertigo Serial": "결합 불성립",
 "Diving Marker": "결합 불성립", "Arthritis Balance": "결합 불성립",
 "Sailing Levy": "결합 불성립", "Menopause Due": "결합 불성립",
 "Rafting Arrears": "결합 불성립", "Pregnancy Advance": "결합 불성립",
 "Climbing Redemption": "결합 불성립", "Fertility Extension": "결합 불성립",
 "Biking Label": "결합 불성립", "Thyroid Manual": "설명 대상 불분명",
 "Golf Schematic": "회로도 어휘 부자연", "Cholesterol Layout": "결합 불성립",
 "Fishing Rendering": "렌더링 대상 불분명", "Hypertension Notification": "결합 불성립",
 "Camping Message": "결합 불성립", "Anemia Total": "결합 불성립",
 "Glamping Announcement": "결합 불성립", "Heartburn Calculator": "계산 대상 불분명",
 "Stargazing Recorder": "기록 대상 불분명", "Constipation Estimator": "산출 대상 불분명",
 "Birdwatching Timer": "결합 불성립", "Concussion Workshop": "결합 불성립",
 "Canyon Helper": "결합 불성립", "Sprain Stage": "결합 불성립",
 "Geyser Result": "결합 불성립", "Fracture Streak": "결합 불성립",
 "Fjord Rank": "결합 불성립", "Insulin Trend": "결합 불성립",
 "Savanna Comparison": "비교 대상 불분명", "Tundra Proposal": "제안 대상 불분명",
 "Prairie Guarantee": "결합 불성립", "Marsh Record": "기록 대상 불분명",
 "Cove Copy": "결합 불성립", "Cliff Reading": "결합 불성립",
 "Cavern Reference": "결합 불성립", "Oasis Forecast": "예측 대상 불분명",
 "Dune Deadline": "결합 불성립", "Whale Duration": "결합 불성립",
 "Dolphin Volume": "결합 불성립", "Penguin Diagnostic": "진단 대상 불분명",
 "Flamingo Progress": "결합 불성립", "Turtle Authorization": "결합 불성립",
 "Moose Template": "결합 불성립", "Bison Guide": "가이드 대상 불분명",
 "Reindeer Rating": "평가 대상 불분명",
 "Networking Workbook": "워크북 대상 불분명", "Pledge Mode": "기능 토글로 읽혀 제품 불분명",
 "Hearing Spec": "결합 불성립", "Creative Quantity": "수량 대상 불분명",
 "Archive Login": "결합 불성립", "Driver Analysis": "분석 대상 불분명",
 "Roaming Coach": "코칭 대상 불분명", "Audit Habit": "결합 불성립",
 "Runbook Workbook": "워크북 대상 불분명", "Callback Mode": "기능 토글로 읽혀 제품 불분명",
 "Referral Spec": "결합 불성립", "Feedback Quantity": "수량 대상 불분명",
 "Appraisal Login": "결합 불성립", "Franchise Analysis": "분석 대상 불분명",
 "Discharge Coach": "코칭 대상 불분명", "Xray Habit": "결합 불성립",
 "Lawyer Recap": "요약 대상 불분명", "Attorney Asset": "결합 불성립",
 "Court Checker": "검사 대상 불분명", "Judge Lookup": "판사 대상 검색 불성립",
 "Jury Size": "수치 지칭 부자연", "Lawsuit Questionnaire": "결합 불성립",
 "Dehumidifier Workbook": "워크북 대상 불분명", "Mortise Mode": "기능 토글로 읽혀 제품 불분명",
 "Syntax Spec": "결합 불성립", "Elevator Quantity": "수량 대상 불분명",
 "Client Login": "결합 불성립", "Cake Analysis": "분석 대상 불분명",
 "Closing Habit": "결합 불성립",
 "Divorce Vault": "결합 불성립", "Custody Trail": "결합 불성립",
 "Immigration Bin": "결합 불성립", "Testament Order": "Testament 계열 기각 선례",
 "Notary Fare": "결합 불성립", "Mediation Balance": "결합 불성립",
 "Guardianship Message": "결합 불성립", "Trademark Reference": "결합 불성립",
 "Patent Feedback": "결합 불성립", "Copyright Checkin": "결합 불성립",
 "Aptitude Workbook": "워크북 대상 불분명", "Networking Mode": "기능 토글로 읽혀 제품 불분명",
 "Radiator Spec": "결합 불성립", "Espresso Quantity": "수량 대상 불분명",
 "Diet Login": "결합 불성립", "Orthodontics Analysis": "분석 대상 불분명",
 "Stroller Coach": "코칭 대상 불분명", "Spa Habit": "결합 불성립",
 "Migraine Debt": "결합 불성립", "Insomnia Duty": "결합 불성립",
 "Skydiving Stake": "결합 불성립", "Acne Margin": "결합 불성립",
 "Snowboarding Link": "결합 불성립", "Eczema Rule": "결합 불성립",
 "Ziplining Category": "결합 불성립", "Psoriasis Attribute": "결합 불성립",
 "Sledding Serial": "결합 불성립", "Vertigo Token": "결합 불성립",
 "Diving Balance": "결합 불성립", "Arthritis Interest": "결합 불성립",
 "Sailing Due": "결합 불성립", "Menopause Subsidy": "결합 불성립",
 "Rafting Advance": "결합 불성립", "Pregnancy Penalty": "결합 불성립",
 "Climbing Extension": "결합 불성립", "Fertility Trial": "결합 불성립",
 "Biking Manual": "설명 대상 불분명", "Thyroid Worksheet": "학습지 근거 약함",
 "Golf Layout": "결합 불성립", "Cholesterol Sketch": "제품성 불분명",
 "Fishing Notification": "결합 불성립", "Hypertension Kit": "키트 대상 불분명",
 "Camping Total": "결합 불성립", "Anemia Widget": "위젯 대상 불분명",
 "Glamping Calculator": "계산 대상 불분명", "Heartburn Converter": "변환 대상 불분명",
 "Stargazing Estimator": "산출 대상 불분명", "Constipation Checker": "검사 대상 불분명",
 "Birdwatching Workshop": "결합 불성립", "Concussion Guardian": "감시 대상 불분명",
 "Canyon Stage": "결합 불성립", "Sprain Result": "결합 불성립",
 "Geyser Streak": "결합 불성립", "Fracture Rank": "결합 불성립",
 "Fjord Trend": "결합 불성립", "Insulin Comparison": "비교 대상 불분명",
 "Savanna Proposal": "제안 대상 불분명", "Tundra Guarantee": "결합 불성립",
 "Prairie Record": "기록 대상 불분명", "Marsh Copy": "결합 불성립",
 "Cove Reading": "결합 불성립", "Cliff Reference": "결합 불성립",
 "Cavern Forecast": "예측 대상 불분명", "Oasis Deadline": "결합 불성립",
 "Dune Duration": "결합 불성립", "Whale Volume": "결합 불성립",
 "Dolphin Diagnostic": "진단 대상 불분명", "Penguin Progress": "결합 불성립",
 "Flamingo Authorization": "결합 불성립", "Turtle Template": "결합 불성립",
 "Moose Guide": "가이드 대상 불분명", "Bison Rating": "평가 대상 불분명",
 "Reindeer Agreement": "결합 불성립",
 "Feature Advice": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Soil Workbook": "워크북 대상 불분명", "Pledge Spec": "결합 불성립",
 "Hearing Quantity": "수량 대상 불분명", "Creative Login": "결합 불성립",
 "Archive Analysis": "분석 대상 불분명", "Driver Coach": "코칭 대상 불분명",
 "Roaming Habit": "결합 불성립",
 "Permit R_DUP_SKIP": "",
 "Runbook Mode": "기능 토글로 읽혀 제품 불분명", "Callback Spec": "결합 불성립",
 "Perimeter Workbook": "워크북 대상 불분명",
 "Referral Quantity": "수량 대상 불분명", "Feedback Login": "결합 불성립",
 "Appraisal Analysis": "분석 대상 불분명", "Franchise Coach": "코칭 대상 불분명",
 "Discharge Habit": "결합 불성립",
 "Lawyer Entry": "등록 대상 불분명", "Attorney Levy": "결합 불성립",
}
del R["Permit R_DUP_SKIP"]
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
out = base + r"\_dec_c23.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
