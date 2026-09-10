# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk21_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Pledge App": (0.6, "기부 서약 관리 앱(실재 카테고리)"),
 "Hearing Tips": (0.55, "심리·공청회 팁(App→Tips 평행)"),
 "Callback App": (0.6, "콜백 예약 관리 앱(실재 카테고리)"),
 "Referral Tips": (0.55, "추천 채용 팁(App→Tips 평행)"),
 "Mortise App": (0.55, "스마트 모티스 잠금 관리 앱(실재)"),
 "Syntax Tips": (0.55, "구문 학습 팁(App→Tips 평행)"),
 "Networking App": (0.6, "네트워킹 이벤트 앱(실재 카테고리)"),
 "Radiator Tips": (0.55, "라디에이터 관리 팁(App→Tips 평행)"),
 "Runbook App": (0.6, "운영 런북 관리 앱(실재 카테고리)"),
 "Callback Tips": (0.55, "콜백 운영 팁(App→Tips 평행)"),
 "Dehumidifier App": (0.55, "제습기 제어·관리 앱(실재)"),
 "Mortise Tips": (0.55, "모티스 잠금 팁(App→Tips 평행)"),
 "Aptitude App": (0.6, "적성 검사 앱(실재 카테고리)"),
 "Networking Tips": (0.55, "네트워킹 팁(App→Tips 평행)"),
 "Pledge Tips": (0.55, "기부 서약 팁(App→Tips 평행)"),
}
R_DUP = {
 "Creative Advice": "동일 배치 승인된 Creative App/Tips와 동일 기능 의미 중복",
 "Elevator Advice": "동일 배치 승인된 Elevator App/Tips와 동일 기능 의미 중복",
 "Espresso Advice": "동일 배치 승인된 Espresso App/Tips와 동일 기능 의미 중복",
 "Hearing Advice": "동일 배치 승인된 Hearing App/Tips와 동일 기능 의미 중복",
 "Referral Advice": "동일 배치 승인된 Referral App/Tips와 동일 기능 의미 중복",
 "Syntax Advice": "동일 배치 승인된 Syntax App/Tips와 동일 기능 의미 중복",
 "Radiator Advice": "동일 배치 승인된 Radiator App/Tips와 동일 기능 의미 중복",
}
R = {
 "Insulin Stage": "결합 불성립", "Savanna Result": "결합 불성립",
 "Tundra Streak": "결합 불성립", "Prairie Rank": "결합 불성립",
 "Marsh Trend": "결합 불성립", "Cove Comparison": "비교 대상 불분명",
 "Cliff Proposal": "제안 대상 불분명", "Cavern Guarantee": "결합 불성립",
 "Oasis Record": "기록 대상 불분명", "Dune Copy": "결합 불성립",
 "Whale Reading": "결합 불성립", "Dolphin Reference": "결합 불성립",
 "Penguin Forecast": "예측 대상 불분명", "Flamingo Deadline": "결합 불성립",
 "Turtle Duration": "결합 불성립", "Moose Volume": "결합 불성립",
 "Bison Diagnostic": "진단 대상 불분명", "Reindeer Progress": "결합 불성립",
 "Creative Workbook": "워크북 대상 불분명", "Archive Workbook": "워크북 대상 불분명",
 "Driver Mode": "기능 토글로 읽혀 제품 불분명", "Roaming Spec": "결합 불성립",
 "Audit Quantity": "수량 대상 불분명", "Pipeline Login": "결합 불성립",
 "Refund Analysis": "분석 대상 불분명", "Reference Coach": "코칭 대상 불분명",
 "Agenda Habit": "결합 불성립",
 "Feedback Advice": "동일 배치 승인된 Feedback App/Tips와 동일 기능 의미 중복",
 "Appraisal Workbook": "워크북 대상 불분명", "Franchise Mode": "기능 토글로 읽혀 제품 불분명",
 "Discharge Spec": "결합 불성립", "Xray Quantity": "수량 대상 불분명",
 "Session Login": "결합 불성립", "Milestone Analysis": "분석 대상 불분명",
 "Wellness Coach": "코칭 대상 불분명", "Scheduling Habit": "결합 불성립",
 "Lawyer Circular": "결합 불성립", "Attorney Signature": "결합 불성립",
 "Court Converter": "변환 대상 불분명", "Judge Account": "판사 대상 계정 불성립",
 "Jury Inventory": "결합 불성립", "Lawsuit Followup": "결합 불성립",
 "Client Workbook": "워크북 대상 불분명", "Cake Mode": "기능 토글로 읽혀 제품 불분명",
 "Closing Quantity": "수량 대상 불분명", "Sponge Login": "결합 불성립",
 "Trap Analysis": "분석 대상 불분명", "Roadtrip Coach": "코칭 대상 불분명",
 "Accordion Habit": "결합 불성립",
 "Divorce Hub": "허브 대상 불분명", "Custody Panel": "결합 불성립",
 "Immigration Harbor": "시설 지칭으로 불성립", "Testament Reminder": "Testament 계열 기각 선례",
 "Notary Unit": "결합 불성립", "Mediation Serial": "결합 불성립",
 "Guardianship Rendering": "렌더링 대상 불분명", "Trademark Guarantee": "결합 불성립",
 "Patent Eligibility": "상태 명사로 제품명 부자연", "Copyright Newsletter": "결합 불성립",
 "Diet Workbook": "워크북 대상 불분명", "Orthodontics Mode": "기능 토글로 읽혀 제품 불분명",
 "Stroller Spec": "결합 불성립", "Spa Quantity": "수량 대상 불분명",
 "Curb Analysis": "분석 대상 불분명", "Vineyard Coach": "코칭 대상 불분명",
 "Accompanist Habit": "결합 불성립",
 "Migraine Fare": "결합 불성립", "Insomnia Fund": "결합 불성립",
 "Skydiving Duty": "결합 불성립", "Acne Allowance": "결합 불성립",
 "Snowboarding Margin": "결합 불성립", "Eczema Fine": "결합 불성립",
 "Ziplining Link": "결합 불성립", "Psoriasis Rule": "결합 불성립",
 "Sledding Category": "결합 불성립", "Vertigo Attribute": "결합 불성립",
 "Diving Serial": "결합 불성립", "Arthritis Token": "결합 불성립",
 "Sailing Balance": "결합 불성립", "Menopause Interest": "결합 불성립",
 "Rafting Due": "결합 불성립", "Pregnancy Subsidy": "결합 불성립",
 "Climbing Advance": "결합 불성립", "Fertility Penalty": "결합 불성립",
 "Biking Extension": "결합 불성립", "Thyroid Trial": "결합 불성립",
 "Golf Manual": "설명 대상 불분명", "Cholesterol Worksheet": "학습지 근거 약함",
 "Fishing Layout": "결합 불성립", "Hypertension Sketch": "제품성 불분명",
 "Camping Notification": "결합 불성립", "Anemia Kit": "키트 대상 불분명",
 "Glamping Total": "결합 불성립", "Heartburn Widget": "위젯 대상 불분명",
 "Stargazing Calculator": "계산 대상 불분명", "Constipation Converter": "변환 대상 불분명",
 "Birdwatching Estimator": "산출 대상 불분명", "Concussion Checker": "검사 대상 불분명",
 "Canyon Timer": "결합 불성립", "Sprain Workshop": "결합 불성립",
 "Geyser Guardian": "감시 대상 불분명", "Fracture Helper": "결합 불성립",
 "Fjord Stage": "결합 불성립", "Insulin Result": "결합 불성립",
 "Savanna Streak": "결합 불성립", "Tundra Rank": "결합 불성립",
 "Prairie Trend": "결합 불성립", "Marsh Comparison": "비교 대상 불분명",
 "Cove Proposal": "제안 대상 불분명", "Cliff Guarantee": "결합 불성립",
 "Cavern Record": "기록 대상 불분명", "Oasis Copy": "결합 불성립",
 "Dune Reading": "결합 불성립", "Whale Reference": "결합 불성립",
 "Dolphin Forecast": "예측 대상 불분명", "Penguin Deadline": "결합 불성립",
 "Flamingo Duration": "결합 불성립", "Turtle Volume": "결합 불성립",
 "Moose Diagnostic": "진단 대상 불분명", "Bison Progress": "결합 불성립",
 "Reindeer Authorization": "결합 불성립",
 "Creative Mode R_DUP_PLACEHOLDER2": "",
 "Archive Mode": "기능 토글로 읽혀 제품 불분명", "Driver Spec": "결합 불성립",
 "Roaming Quantity": "수량 대상 불분명", "Audit Login": "결합 불성립",
 "Pipeline Analysis": "분석 대상 불분명", "Refund Coach": "코칭 대상 불분명",
 "Reference Habit": "결합 불성립",
 "Feedback Workbook": "워크북 대상 불분명", "Appraisal Mode": "기능 토글로 읽혀 제품 불분명",
 "Franchise Spec": "결합 불성립", "Discharge Quantity": "수량 대상 불분명",
 "Xray Login": "결합 불성립", "Session Analysis": "분석 대상 불분명",
 "Milestone Coach": "코칭 대상 불분명", "Wellness Habit": "결합 불성립",
 "Lawyer Advisory": "안내 대상 불분명", "Attorney Marker": "결합 불성립",
 "Court Generator": "생성 대상 불분명", "Judge Case": "판사 대상 사건 불성립",
 "Jury Claim": "결합 불성립", "Lawsuit Approval": "결합 불성립",
 "Client Mode": "기능 토글로 읽혀 제품 불분명", "Cake Spec": "결합 불성립",
 "Closing Login": "결합 불성립", "Sponge Analysis": "분석 대상 불분명",
 "Trap Coach": "코칭 대상 불분명", "Roadtrip Habit": "결합 불성립",
 "Divorce Desk": "결합 불성립", "Custody Scale": "결합 불성립",
 "Immigration Roster": "결합 불성립", "Testament Index": "Testament 계열 기각 선례",
 "Notary Plan": "계획 대상 불분명", "Mediation Token": "결합 불성립",
 "Guardianship Notification": "결합 불성립", "Trademark Record": "기록 대상 불분명",
 "Patent Broadcast": "결합 불성립", "Copyright Inventory": "결합 불성립",
 "Espresso Workbook": "워크북 대상 불분명", "Elevator Workbook": "워크북 대상 불분명",
 "Diet Mode": "기능 토글로 읽혀 제품 불분명",
 "Orthodontics Spec": "결합 불성립", "Stroller Quantity": "수량 대상 불분명",
 "Spa Login": "결합 불성립", "Curb Coach": "코칭 대상 불분명",
 "Vineyard Habit": "결합 불성립",
 "Migraine Tax": "결합 불성립", "Insomnia Cash": "결합 불성립",
 "Skydiving Allowance": "결합 불성립", "Acne Tariff": "결합 불성립",
 "Snowboarding Fine": "결합 불성립", "Eczema Number": "수치 지칭 부자연",
 "Ziplining Rule": "결합 불성립", "Psoriasis Detail": "결합 불성립",
 "Sledding Attribute": "결합 불성립", "Vertigo Field": "결합 불성립",
 "Diving Token": "결합 불성립", "Arthritis Signature": "결합 불성립",
}
del R["Creative Mode R_DUP_PLACEHOLDER2"]
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
out = base + r"\_dec_c21.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
