# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk24_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Craft App": (0.55, "아이 만들기 활동 앱(실재)"),
 "Dishwasher Tips": (0.55, "식기세척기 팁(App→Tips 평행)"),
 "Patio App": (0.55, "파티오 설계·시공 앱(실재)"),
 "Transfer Tips": (0.55, "편입 절차 팁(App→Tips 평행)"),
 "Vendor App": (0.6, "벤더 관리 앱(실재 카테고리)"),
 "Concierge Tips": (0.55, "컨시어지 팁(App→Tips 평행)"),
 "Placement App": (0.6, "광고 지면 운영 앱(실재 카테고리)"),
 "Feed Tips": (0.55, "피드 운영 팁(App→Tips 평행)"),
 "Gum App": (0.55, "잇몸 건강 관리 앱(실재)"),
 "Craft Tips": (0.55, "만들기 활동 팁(App→Tips 평행)"),
 "Training App": (0.6, "직원 교육 훈련 앱(실재 카테고리)"),
 "Patio Tips": (0.55, "파티오 관리 팁(App→Tips 평행)"),
 "Patent Renewal": (0.55, "특허 연차료 갱신 서비스(실재)"),
}
R_DUP = {
 "Blowout Advice": "동일 배치 승인된 Blowout App/Tips와 동일 기능 의미 중복",
 "Ward Advice": "동일 배치 승인된 Ward App/Tips와 동일 기능 의미 중복",
 "Grading Advice": "동일 배치 승인된 Grading App/Tips와 동일 기능 의미 중복",
 "Permit Advice": "동일 배치 승인된 Permit App/Tips와 동일 기능 의미 중복",
 "Dishwasher Advice": "동일 배치 승인된 Dishwasher App/Tips와 동일 기능 의미 중복",
 "Transfer Advice": "동일 배치 승인된 Transfer App/Tips와 동일 기능 의미 중복",
}
R = {
 "Court Detector": "탐지 대상 불분명", "Judge Ping": "결합 불성립",
 "Jury Length": "결합 불성립", "Lawsuit Utilization": "결합 불성립",
 "Inhaler Workbook": "워크북 대상 불분명", "Dehumidifier Mode": "기능 토글로 읽혀 제품 불분명",
 "Mortise Spec": "결합 불성립", "Syntax Quantity": "수량 대상 불분명",
 "Elevator Login": "결합 불성립", "Client Analysis": "분석 대상 불분명",
 "Cake Coach": "코칭 대상 불분명",
 "Divorce Compass": "결합 불성립", "Custody Chain": "결합 불성립",
 "Immigration Passport": "서류 지칭으로 서비스 대상 불분명", "Testament Bill": "Testament 계열 기각 선례",
 "Notary Tax": "결합 불성립", "Mediation Interest": "결합 불성립",
 "Guardianship Total": "결합 불성립", "Trademark Forecast": "예측 대상 불분명",
 "Patent Invoice": "결합 불성립", "Copyright Size": "수치 지칭 부자연",
 "Feature Workbook": "워크북 대상 불분명", "Aptitude Mode": "기능 토글로 읽혀 제품 불분명",
 "Networking Spec": "결합 불성립", "Radiator Quantity": "수량 대상 불분명",
 "Espresso Login": "결합 불성립", "Diet Analysis": "분석 대상 불분명",
 "Orthodontics Coach": "코칭 대상 불분명", "Stroller Habit": "결합 불성립",
 "Migraine Fund": "결합 불성립", "Insomnia Allowance": "결합 불성립",
 "Skydiving Margin": "결합 불성립", "Acne Fine": "결합 불성립",
 "Snowboarding Rule": "결합 불성립", "Eczema Detail": "결합 불성립",
 "Ziplining Attribute": "결합 불성립", "Psoriasis Field": "결합 불성립",
 "Sledding Token": "결합 불성립", "Vertigo Signature": "결합 불성립",
 "Diving Interest": "결합 불성립", "Arthritis Asset": "결합 불성립",
 "Sailing Subsidy": "결합 불성립", "Menopause Discount": "결합 불성립",
 "Rafting Penalty": "결합 불성립", "Pregnancy Markup": "결합 불성립",
 "Climbing Trial": "결합 불성립", "Fertility Graph": "그래프 대상 불분명",
 "Biking Worksheet": "학습지 근거 약함", "Thyroid Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Golf Sketch": "제품성 불분명", "Cholesterol Outline": "지형은 공예 오트라인 대상 아님",
 "Fishing Kit": "키트 대상 불분명", "Hypertension Count": "대상 불분명",
 "Camping Widget": "위젯 대상 불분명", "Anemia Repository": "결합 불성립",
 "Glamping Converter": "변환 대상 불분명", "Heartburn Generator": "생성 대상 불분명",
 "Stargazing Checker": "검사 대상 불분명", "Constipation Detector": "탐지 대상 불분명",
 "Birdwatching Guardian": "감시 대상 불분명", "Concussion Helper": "결합 불성립",
 "Canyon Result": "결합 불성립", "Sprain Streak": "결합 불성립",
 "Geyser Rank": "결합 불성립", "Fracture Trend": "결합 불성립",
 "Fjord Comparison": "비교 대상 불분명", "Insulin Proposal": "제안 대상 불분명",
 "Savanna Guarantee": "결합 불성립", "Tundra Record": "기록 대상 불분명",
 "Prairie Copy": "결합 불성립", "Marsh Reading": "결합 불성립",
 "Cove Reference": "결합 불성립", "Cliff Forecast": "예측 대상 불분명",
 "Cavern Deadline": "결합 불성립", "Oasis Duration": "결합 불성립",
 "Dune Volume": "결합 불성립", "Whale Diagnostic": "진단 대상 불분명",
 "Dolphin Progress": "결합 불성립", "Penguin Authorization": "결합 불성립",
 "Flamingo Template": "결합 불성립", "Turtle Guide": "가이드 대상 불분명",
 "Moose Rating": "평가 대상 불분명", "Bison Agreement": "결합 불성립",
 "Reindeer Reply": "결합 불성립",
 "Soil Mode": "기능 토글로 읽혀 제품 불분명", "Pledge Quantity": "수량 대상 불분명",
 "Hearing Login": "결합 불성립", "Creative Analysis": "분석 대상 불분명",
 "Archive Coach": "코칭 대상 불분명", "Driver Habit": "결합 불성립",
 "Network Workbook": "워크북 대상 불분명", "Perimeter Mode": "기능 토글로 읽혀 제품 불분명",
 "Runbook Spec": "결합 불성립", "Callback Quantity": "수량 대상 불분명",
 "Referral Login": "결합 불성립", "Feedback Analysis": "분석 대상 불분명",
 "Appraisal Coach": "코칭 대상 불분명", "Franchise Habit": "결합 불성립",
 "Lawyer Fee": "결합 불성립", "Attorney Due": "결합 불성립",
 "Court Timer": "결합 불성립", "Judge Model": "판사 대상 모델 불성립",
 "Jury Weight": "결합 불성립", "Lawsuit Benefit": "결합 불성립",
 "Blowout Workbook": "워크북 대상 불분명",
 "Inhaler Mode": "기능 토글로 읽혀 제품 불분명", "Dehumidifier Spec": "결합 불성립",
 "Mortise Quantity": "수량 대상 불분명", "Syntax Login": "결합 불성립",
 "Elevator Analysis": "분석 대상 불분명", "Client Coach": "코칭 대상 불분명",
 "Cake Habit": "결합 불성립",
 "Divorce Beacon": "결합 불성립", "Custody Ring": "결합 불성립",
 "Immigration Lobby": "시설 지칭으로 불성립", "Testament Receipt": "Testament 계열 기각 선례",
 "Notary Loan": "결합 불성립", "Mediation Asset": "결합 불성립",
 "Guardianship Widget": "위젯 대상 불분명", "Trademark Deadline": "결합 불성립",
 "Copyright Length": "결합 불성립",
 "Ward Workbook": "워크북 대상 불분명",
 "Feature Mode": "기능 토글로 읽혀 제품 불분명", "Aptitude Spec": "결합 불성립",
 "Networking Quantity": "수량 대상 불분명", "Radiator Login": "결합 불성립",
 "Espresso Analysis": "분석 대상 불분명", "Diet Coach": "코칭 대상 불분명",
 "Orthodontics Habit": "결합 불성립",
 "Migraine Cash": "결합 불성립", "Insomnia Tariff": "결합 불성립",
 "Skydiving Fine": "결합 불성립", "Acne Number": "수치 지칭 부자연",
 "Snowboarding Detail": "결합 불성립", "Eczema Identifier": "결합 불성립",
 "Ziplining Field": "결합 불성립", "Psoriasis Format": "결합 불성립",
 "Sledding Signature": "결합 불성립", "Vertigo Marker": "결합 불성립",
 "Diving Asset": "결합 불성립", "Arthritis Levy": "결합 불성립",
 "Sailing Discount": "결합 불성립", "Menopause Arrears": "결합 불성립",
 "Rafting Markup": "결합 불성립", "Pregnancy Redemption": "결합 불성립",
 "Climbing Graph": "그래프 대상 불분명", "Fertility Label": "결합 불성립",
 "Biking Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Thyroid Schematic": "회로도 어휘 부자연", "Golf Outline": "지형은 공예 오트라인 대상 아님",
 "Cholesterol Rendering": "렌더링 대상 불분명", "Fishing Count": "대상 불분명",
 "Hypertension Message": "결합 불성립", "Camping Repository": "결합 불성립",
 "Anemia Announcement": "결합 불성립", "Glamping Generator": "생성 대상 불분명",
 "Heartburn Recorder": "기록 대상 불분명", "Stargazing Detector": "탐지 대상 불분명",
 "Constipation Timer": "결합 불성립", "Birdwatching Helper": "결합 불성립",
 "Concussion Stage": "결합 불성립", "Canyon Streak": "결합 불성립",
 "Sprain Rank": "결합 불성립", "Geyser Trend": "결합 불성립",
 "Fracture Comparison": "비교 대상 불분명", "Fjord Proposal": "제안 대상 불분명",
 "Insulin Guarantee": "결합 불성립", "Savanna Record": "기록 대상 불분명",
 "Tundra Copy": "결합 불성립", "Prairie Reading": "결합 불성립",
 "Marsh Reference": "결합 불성립", "Cove Forecast": "예측 대상 불분명",
 "Cliff Deadline": "결합 불성립", "Cavern Duration": "결합 불성립",
 "Oasis Volume": "결합 불성립", "Dune Diagnostic": "진단 대상 불분명",
 "Whale Progress": "결합 불성립", "Dolphin Authorization": "결합 불성립",
 "Penguin Template": "결합 불성립", "Flamingo Guide": "가이드 대상 불분명",
 "Turtle Rating": "평가 대상 불분명",
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
out = base + r"\_dec_c24.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
