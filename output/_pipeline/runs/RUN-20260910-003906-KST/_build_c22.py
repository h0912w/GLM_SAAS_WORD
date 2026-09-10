# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk22_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Soil App": (0.6, "토양 건강·시비 관리 앱(실재 카테고리)"),
 "Perimeter App": (0.6, "경계 보안 감시 앱(실재 카테고리)"),
 "Runbook Tips": (0.55, "런북 작성 팁(App→Tips 평행)"),
 "Inhaler App": (0.55, "흡입기 사용 추적 앱(실재)"),
 "Dehumidifier Tips": (0.55, "제습기 관리 팁(App→Tips 평행)"),
 "Aptitude Tips": (0.55, "적성 검사 팁(App→Tips 평행)"),
 "Soil Tips": (0.55, "토양 관리 팁(App→Tips 평행)"),
 "Network App": (0.6, "네트워크 관리 앱(실재 카테고리)"),
 "Perimeter Tips": (0.55, "경계 보안 팁(App→Tips 평행)"),
 "Blowout App": (0.6, "블로우 드라이 예약 앱(실재 카테고리)"),
 "Inhaler Tips": (0.55, "흡입기 사용 팁(App→Tips 평행)"),
}
R_DUP = {
 "Pledge Advice": "동일 배치 승인된 Pledge App/Tips와 동일 기능 의미 중복",
 "Callback Advice": "동일 배치 승인된 Callback App/Tips와 동일 기능 의미 중복",
 "Mortise Advice": "동일 배치 승인된 Mortise App/Tips와 동일 기능 의미 중복",
 "Networking Advice": "동일 배치 승인된 Networking App/Tips와 동일 기능 의미 중복",
 "Runbook Advice": "동일 배치 승인된 Runbook App/Tips와 동일 기능 의미 중복",
 "Dehumidifier Advice": "동일 배치 승인된 Dehumidifier App/Tips와 동일 기능 의미 중복",
}
R = {
 "Sailing Interest": "결합 불성립", "Menopause Asset": "결합 불성립",
 "Rafting Subsidy": "결합 불성립", "Pregnancy Discount": "결합 불성립",
 "Climbing Penalty": "결합 불성립", "Fertility Markup": "결합 불성립",
 "Biking Trial": "결합 불성립", "Thyroid Graph": "그래프 대상 불분명",
 "Golf Worksheet": "학습지 근거 약함", "Cholesterol Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Fishing Sketch": "제품성 불분명", "Hypertension Outline": "지형은 공예 오트라인 대상 아님",
 "Camping Kit": "키트 대상 불분명", "Anemia Count": "대상 불분명",
 "Glamping Widget": "위젯 대상 불분명", "Heartburn Repository": "결합 불성립",
 "Stargazing Converter": "변환 대상 불분명", "Constipation Generator": "생성 대상 불분명",
 "Birdwatching Checker": "검사 대상 불분명", "Concussion Detector": "탐지 대상 불분명",
 "Canyon Workshop": "결합 불성립", "Sprain Guardian": "감시 대상 불분명",
 "Geyser Helper": "결합 불성립", "Fracture Stage": "결합 불성립",
 "Fjord Result": "결합 불성립", "Insulin Streak": "결합 불성립",
 "Savanna Rank": "결합 불성립", "Tundra Trend": "결합 불성립",
 "Prairie Comparison": "비교 대상 불분명", "Marsh Proposal": "제안 대상 불분명",
 "Cove Guarantee": "결합 불성립", "Cliff Record": "기록 대상 불분명",
 "Cavern Copy": "결합 불성립", "Oasis Reading": "결합 불성립",
 "Dune Reference": "결합 불성립", "Whale Forecast": "예측 대상 불분명",
 "Dolphin Deadline": "결합 불성립", "Penguin Duration": "결합 불성립",
 "Flamingo Volume": "결합 불성립", "Turtle Diagnostic": "진단 대상 불분명",
 "Moose Progress": "결합 불성립", "Bison Authorization": "결합 불성립",
 "Reindeer Template": "결합 불성립",
 "Hearing Workbook": "워크북 대상 불분명", "Creative Mode": "기능 토글로 읽혀 제품 불분명",
 "Archive Spec": "결합 불성립", "Driver Quantity": "수량 대상 불분명",
 "Roaming Login": "결합 불성립", "Audit Analysis": "분석 대상 불분명",
 "Pipeline Coach": "코칭 대상 불분명", "Refund Habit": "결합 불성립",
 "Referral Workbook": "워크북 대상 불분명", "Feedback Mode": "기능 토글로 읽혀 제품 불분명",
 "Appraisal Spec": "결합 불성립", "Franchise Quantity": "수량 대상 불분명",
 "Discharge Login": "결합 불성립", "Xray Analysis": "분석 대상 불분명",
 "Session Coach": "코칭 대상 불분명", "Milestone Habit": "결합 불성립",
 "Lawyer Petition": "결합 불성립", "Attorney Balance": "결합 불성립",
 "Court Recorder": "기록 대상 불분명", "Judge Match": "판사 대상 매칭 불성립",
 "Jury Onboarding": "결합 불성립", "Lawsuit Matrix": "결합 불성립",
 "Syntax Workbook": "워크북 대상 불분명", "Elevator Mode": "기능 토글로 읽혀 제품 불분명",
 "Client Spec": "결합 불성립", "Cake Quantity": "수량 대상 불분명",
 "Closing Analysis": "분석 대상 불분명", "Sponge Coach": "코칭 대상 불분명",
 "Trap Habit": "결합 불성립",
 "Divorce Radar": "탐지 대상 불분명", "Custody Route": "경로 대상 불분명",
 "Immigration Alert": "알림 대상 불분명", "Testament Ticket": "Testament 계열 기각 선례",
 "Notary Cost": "결합 불성립", "Mediation Signature": "결합 불성립",
 "Guardianship Kit": "키트 대상 불분명", "Trademark Copy": "결합 불성립",
 "Patent Barcode": "결합 불성립", "Copyright Claim": "결합 불성립",
 "Feature App": "다의어(기능/특집)로 서비스 대상 불분명",
 "Radiator Workbook": "워크북 대상 불분명", "Espresso Mode": "기능 토글로 읽혀 제품 불분명",
 "Diet Spec": "결합 불성립", "Orthodontics Quantity": "수량 대상 불분명",
 "Stroller Login": "결합 불성립", "Spa Analysis": "분석 대상 불분명",
 "Curb Habit": "결합 불성립",
 "Migraine Loan": "결합 불성립", "Insomnia Sale": "결합 불성립",
 "Skydiving Tariff": "결합 불성립", "Acne Value": "결합 불성립",
 "Snowboarding Number": "수치 지칭 부자연", "Eczema Version": "결합 불성립",
 "Ziplining Detail": "결합 불성립", "Psoriasis Identifier": "결합 불성립",
 "Sledding Field": "결합 불성립", "Vertigo Format": "결합 불성립",
 "Diving Signature": "결합 불성립", "Arthritis Marker": "결합 불성립",
 "Sailing Asset": "결합 불성립", "Menopause Levy": "결합 불성립",
 "Rafting Discount": "결합 불성립", "Pregnancy Arrears": "결합 불성립",
 "Climbing Markup": "결합 불성립", "Fertility Redemption": "결합 불성립",
 "Biking Graph": "그래프 대상 불분명", "Thyroid Label": "결합 불성립",
 "Golf Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Cholesterol Schematic": "회로도 어휘 부자연", "Fishing Outline": "지형은 공예 오트라인 대상 아님",
 "Hypertension Rendering": "렌더링 대상 불분명", "Camping Count": "대상 불분명",
 "Anemia Message": "결합 불성립", "Glamping Repository": "결합 불성립",
 "Heartburn Announcement": "결합 불성립", "Stargazing Generator": "생성 대상 불분명",
 "Constipation Recorder": "기록 대상 불분명", "Birdwatching Detector": "탐지 대상 불분명",
 "Concussion Timer": "결합 불성립", "Canyon Guardian": "감시 대상 불분명",
 "Sprain Helper": "결합 불성립", "Geyser Stage": "결합 불성립",
 "Fracture Result": "결합 불성립", "Fjord Streak": "결합 불성립",
 "Insulin Rank": "결합 불성립", "Savanna Trend": "결합 불성립",
 "Tundra Comparison": "비교 대상 불분명", "Prairie Proposal": "제안 대상 불분명",
 "Marsh Guarantee": "결합 불성립", "Cove Record": "기록 대상 불분명",
 "Cliff Copy": "결합 불성립", "Cavern Reading": "결합 불성립",
 "Oasis Reference": "결합 불성립", "Dune Forecast": "예측 대상 불분명",
 "Whale Deadline": "결합 불성립", "Dolphin Duration": "결합 불성립",
 "Penguin Volume": "결합 불성립", "Flamingo Diagnostic": "진단 대상 불분명",
 "Turtle Progress": "결합 불성립", "Moose Authorization": "결합 불성립",
 "Bison Template": "결합 불성립", "Reindeer Guide": "가이드 대상 불분명",
 "Pledge Workbook": "워크북 대상 불분명", "Hearing Mode": "기능 토글로 읽혀 제품 불분명",
 "Creative Spec": "결합 불성립", "Archive Quantity": "수량 대상 불분명",
 "Driver Login": "결합 불성립", "Roaming Analysis": "분석 대상 불분명",
 "Audit Coach": "코칭 대상 불분명", "Pipeline Habit": "결합 불성립",
 "Callback Workbook": "워크북 대상 불분명", "Referral Mode": "기능 토글로 읽혀 제품 불분명",
 "Feedback Spec": "결합 불성립", "Appraisal Quantity": "수량 대상 불분명",
 "Franchise Login": "결합 불성립", "Discharge Analysis": "분석 대상 불분명",
 "Xray Coach": "코칭 대상 불분명", "Session Habit": "결합 불성립",
 "Lawyer Confirmation": "확인 대상 불분명", "Attorney Interest": "결합 불성립",
 "Court Estimator": "산출 대상 불분명", "Judge Validation": "판사 대상 검증 불성립",
 "Jury Checkin": "결합 불성립", "Lawsuit Evaluation": "평가 대상 불분명",
 "Mortise Workbook": "워크북 대상 불분명", "Syntax Mode": "기능 토글로 읽혀 제품 불분명",
 "Elevator Spec": "결합 불성립", "Client Quantity": "수량 대상 불분명",
 "Cake Login": "결합 불성립", "Closing Coach": "코칭 대상 불분명",
 "Sponge Habit": "결합 불성립",
 "Divorce Relay": "결합 불성립", "Custody Rail": "결합 불성립",
 "Immigration Chart": "차트 대상 불분명", "Testament Estimate": "Testament 계열 기각 선례",
 "Notary Price": "가격 지칭 부자연", "Mediation Marker": "결합 불성립",
 "Guardianship Count": "대상 불분명", "Trademark Reading": "결합 불성립",
 "Patent Appointment": "결합 불성립",
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
out = base + r"\_dec_c22.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
