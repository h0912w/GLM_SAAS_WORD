# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk17_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Pipeline App": (0.6, "CI/CD 파이프라인 관리 앱(실재 카테고리)"),
 "Refund Tips": (0.55, "환불 처리 팁(App→Tips 평행)"),
 "Session App": (0.55, "PT 세션 예약 관리 앱(실재)"),
 "Milestone Tips": (0.55, "발달 이정표 기록 팁(App→Tips 평행)"),
 "Trap Tips": (0.55, "배수 트랩 관리 팁(App→Tips 평행)"),
 "Patent Case": (0.55, "특허 사건 관리(Copyright Case 평행)"),
 "Curb Tips": (0.55, "연석 정비 팁(App→Tips 평행)"),
 "Insomnia Cost": (0.55, "불면증 치료 비용(건강 비용 축)"),
 "Audit App": (0.6, "보안 감사 관리 앱(실재 카테고리)"),
 "Pipeline Tips": (0.55, "파이프라인 운영 팁(App→Tips 평행)"),
 "Xray App": (0.6, "치과 방사선 뷰어 앱(실재)"),
 "Session Tips": (0.55, "세션 운영 팁(App→Tips 평행)"),
 "Patent Match": (0.55, "특허 매칭·검색(Copyright Match 평행)"),
 "Spa App": (0.6, "스파 예약 관리 앱(실재 카테고리)"),
}
R_DUP = {
 "Reference Advice": "동일 배치 승인된 Reference App/Tips와 동일 기능 의미 중복",
 "Wellness Advice": "동일 배치 승인된 Wellness App/Tips와 동일 기능 의미 중복",
 "Roadtrip Advice": "동일 배치 승인된 Roadtrip App/Tips와 동일 기능 의미 중복",
 "Vineyard Advice": "동일 배치 승인된 Vineyard App/Tips와 동일 기능 의미 중복",
 "Refund Advice": "동일 배치 승인된 Refund App/Tips와 동일 기능 의미 중복",
 "Milestone Advice": "동일 배치 승인된 Milestone App/Tips와 동일 기능 의미 중복",
 "Trap Advice": "동일 배치 승인된 Trap App/Tips와 동일 기능 의미 중복",
 "Curb Advice": "동일 배치 승인된 Curb App/Tips와 동일 기능 의미 중복",
}
R = {
 "Cholesterol Penalty": "결합 불성립", "Fishing Extension": "결합 불성립",
 "Hypertension Trial": "결합 불성립", "Camping Manual": "설명 대상 불분명",
 "Anemia Worksheet": "학습지 근거 약함", "Glamping Layout": "결합 불성립",
 "Heartburn Sketch": "제품성 불분명", "Stargazing Notification": "결합 불성립",
 "Constipation Kit": "키트 대상 불분명", "Birdwatching Total": "결합 불성립",
 "Concussion Widget": "위젯 대상 불분명", "Canyon Announcement": "결합 불성립",
 "Sprain Calculator": "계산 대상 불분명", "Geyser Converter": "변환 대상 불분명",
 "Fracture Generator": "생성 대상 불분명", "Fjord Recorder": "기록 대상 불분명",
 "Insulin Estimator": "산출 대상 불분명", "Savanna Checker": "검사 대상 불분명",
 "Tundra Detector": "탐지 대상 불분명", "Prairie Timer": "결합 불성립",
 "Marsh Workshop": "결합 불성립", "Cove Guardian": "감시 대상 불분명",
 "Cliff Helper": "결합 불성립", "Cavern Stage": "결합 불성립",
 "Oasis Result": "결합 불성립", "Dune Streak": "결합 불성립",
 "Whale Rank": "결합 불성립", "Dolphin Trend": "결합 불성립",
 "Penguin Comparison": "비교 대상 불분명", "Flamingo Proposal": "제안 대상 불분명",
 "Turtle Guarantee": "결합 불성립", "Moose Record": "기록 대상 불분명",
 "Bison Copy": "결합 불성립", "Reindeer Reading": "결합 불성립",
 "Agenda Workbook": "워크북 대상 불분명", "Financing Mode": "기능 토글로 읽혀 제품 불분명",
 "Compliance Spec": "결합 불성립", "Appointment Quantity": "수량 대상 불분명",
 "Waiver Analysis": "분석 대상 불분명", "Immunization Coach": "코칭 대상 불분명",
 "Family Habit": "결합 불성립",
 "Scheduling Workbook": "워크북 대상 불분명", "Snow Mode": "기능 토글로 읽혀 제품 불분명",
 "Inventory Spec": "결합 불성립", "Alteration Quantity": "수량 대상 불분명",
 "Memorial Login": "결합 불성립", "Checkout Analysis": "분석 대상 불분명",
 "Recall Coach": "코칭 대상 불분명", "Port Habit": "결합 불성립",
 "Lawyer Stub": "결합 불성립", "Attorney Identifier": "결합 불성립",
 "Court Count": "대상 불분명", "Judge Progress": "결합 불성립",
 "Jury Review": "검토 대상 불분명", "Lawsuit Condition": "결합 불성립",
 "Sponge App": "도구 지칭으로 앱 대상 불성립", "Roadtrip Advice R_DUP_PLACEHOLDER": "",
 "Accordion Workbook": "워크북 대상 불분명", "Allergy Mode": "기능 토글로 읽혀 제품 불분명",
 "Wire Spec": "결합 불성립", "Divorce Quantity": "수량 대상 불분명",
 "Chassis Login": "결합 불성립", "Amendment Analysis": "분석 대상 불분명",
 "Salvage Coach": "코칭 대상 불분명", "Pension Habit": "결합 불성립",
 "Custody Lab": "결합 불성립", "Immigration Finder": "탐색 대상 불분명",
 "Testament Level": "결합 불성립", "Notary Advisory": "안내 대상 불분명",
 "Mediation Rule": "결합 불성립", "Guardianship Manual": "설명 대상 불분명",
 "Trademark Stage": "결합 불성립", "Copyright Seal": "결합 불성립",
 "Accompanist Workbook": "워크북 대상 불분명", "Illness Mode": "기능 토글로 읽혀 제품 불분명",
 "Debtor Spec": "결합 불성립", "Flatbed Quantity": "수량 대상 불분명",
 "Neighborhood Login": "결합 불성립", "Litigation Analysis": "분석 대상 불분명",
 "Dependent Coach": "코칭 대상 불분명", "Cabinetry Habit": "결합 불성립",
 "Migraine Entry": "등록 대상 불분명",
 "Skydiving Loan": "결합 불성립", "Acne Sum": "결합 불성립",
 "Snowboarding Sale": "결합 불성립", "Eczema Charge": "결합 불성립",
 "Ziplining Tariff": "결합 불성립", "Psoriasis Value": "결합 불성립",
 "Sledding Fine": "결합 불성립", "Vertigo Number": "수치 지칭 부자연",
 "Diving Rule": "결합 불성립", "Arthritis Detail": "결합 불성립",
 "Sailing Attribute": "결합 불성립", "Menopause Field": "결합 불성립",
 "Rafting Token": "결합 불성립", "Pregnancy Signature": "결합 불성립",
 "Climbing Interest": "결합 불성립", "Fertility Asset": "결합 불성립",
 "Biking Subsidy": "결합 불성립", "Thyroid Discount": "결합 불성립",
 "Golf Penalty": "결합 불성립", "Cholesterol Markup": "결합 불성립",
 "Fishing Trial": "결합 불성립", "Hypertension Graph": "그래프 대상 불분명",
 "Camping Worksheet": "학습지 근거 약함", "Anemia Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Glamping Sketch": "제품성 불분명", "Heartburn Outline": "지형은 공예 오트라인 대상 아님",
 "Stargazing Kit": "키트 대상 불분명", "Constipation Count": "대상 불분명",
 "Birdwatching Widget": "위젯 대상 불분명", "Concussion Repository": "결합 불성립",
 "Canyon Calculator": "계산 대상 불분명", "Sprain Converter": "변환 대상 불분명",
 "Geyser Generator": "생성 대상 불분명", "Fracture Recorder": "기록 대상 불분명",
 "Fjord Estimator": "산출 대상 불분명", "Insulin Checker": "검사 대상 불분명",
 "Savanna Detector": "탐지 대상 불분명", "Tundra Timer": "결합 불성립",
 "Prairie Workshop": "결합 불성립", "Marsh Guardian": "감시 대상 불분명",
 "Cove Helper": "결합 불성립", "Cliff Stage": "결합 불성립",
 "Cavern Result": "결합 불성립", "Oasis Streak": "결합 불성립",
 "Dune Rank": "결합 불성립", "Whale Trend": "결합 불성립",
 "Dolphin Comparison": "비교 대상 불분명", "Penguin Proposal": "제안 대상 불분명",
 "Flamingo Guarantee": "결합 불성립", "Turtle Record": "기록 대상 불분명",
 "Moose Copy": "결합 불성립", "Bison Reading": "결합 불성립",
 "Reindeer Reference": "결합 불성립",
 "Reference Workbook": "워크북 대상 불분명", "Agenda Mode": "기능 토글로 읽혀 제품 불분명",
 "Financing Spec": "결합 불성립", "Compliance Quantity": "수량 대상 불분명",
 "Appointment Login": "결합 불성립", "Waiver Coach": "코칭 대상 불분명",
 "Immunization Habit": "결합 불성립",
 "Session Advice R_DUP_PLACEHOLDER": "",
 "Wellness Workbook": "워크북 대상 불분명", "Scheduling Mode": "기능 토글로 읽혀 제품 불분명",
 "Snow Spec": "결합 불성립", "Inventory Quantity": "수량 대상 불분명",
 "Alteration Login": "결합 불성립", "Memorial Analysis": "분석 대상 불분명",
 "Checkout Coach": "코칭 대상 불분명", "Recall Habit": "결합 불성립",
 "Lawyer Statement": "결합 불성립", "Attorney Category": "결합 불성립",
 "Court Message": "결합 불성립", "Judge Authorization": "결합 불성립",
 "Jury Recipe": "결합 불성립", "Lawsuit Humidity": "결합 불성립",
 "Closing App": "다의어로 서비스 대상 불분명(pool closing 애매)",
 "Sponge Tips": "도구 지칭으로 대상 불성립",
 "Roadtrip Workbook": "워크북 대상 불분명", "Accordion Mode": "기능 토글로 읽혀 제품 불분명",
 "Allergy Spec": "결합 불성립", "Wire Quantity": "수량 대상 불분명",
 "Divorce Login": "결합 불성립", "Chassis Analysis": "분석 대상 불분명",
 "Amendment Coach": "코칭 대상 불분명", "Salvage Habit": "결합 불성립",
 "Custody Station": "결합 불성립", "Immigration Office": "정부 기관 지칭으로 서비스 대상 불분명",
 "Testament Rate": "결합 불성립", "Notary Petition": "결합 불성립",
 "Mediation Detail": "결합 불성립", "Guardianship Worksheet": "학습지 근거 약함",
 "Trademark Result": "결합 불성립", "Copyright Review": "검토 대상 불분명",
 "Vineyard Workbook": "워크북 대상 불분명", "Accompanist Mode": "기능 토글로 읽혀 제품 불분명",
 "Illness Spec": "결합 불성립", "Debtor Quantity": "수량 대상 불분명",
 "Flatbed Login": "결합 불성립",
}
del R["Roadtrip Advice R_DUP_PLACEHOLDER"]
del R["Session Advice R_DUP_PLACEHOLDER"]
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
out = base + r"\_dec_c17.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
