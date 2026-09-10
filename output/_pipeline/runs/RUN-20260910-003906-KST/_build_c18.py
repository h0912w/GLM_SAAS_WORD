# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk18_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Roaming App": (0.6, "해외 로밍 관리 앱(실재 카테고리)"),
 "Audit Tips": (0.55, "보안 감사 팁(App→Tips 평행)"),
 "Discharge App": (0.55, "동물병원 퇴원 관리 앱(실재)"),
 "Xray Tips": (0.55, "방사선 관리 팁(App→Tips 평행)"),
 "Stroller App": (0.55, "유모차 공유·관리 앱(실재)"),
 "Spa Tips": (0.55, "스파 이용 팁(App→Tips 평행)"),
 "Driver App": (0.6, "운전기사 차량 관리 앱(실재 카테고리)"),
 "Roaming Tips": (0.55, "로밍 사용 팁(App→Tips 평행)"),
 "Franchise App": (0.6, "프랜차이즈 운영 관리 앱(실재)"),
 "Discharge Tips": (0.55, "퇴원 관리 팁(App→Tips 평행)"),
 "Cake App": (0.6, "케이크 주문 앱(실재 카테고리)"),
}
R_DUP = {
 "Pipeline Advice": "동일 배치 승인된 Pipeline App/Tips와 동일 기능 의미 중복",
 "Session Advice": "동일 배치 승인된 Session App/Tips와 동일 기능 의미 중복",
 "Audit Advice": "동일 배치 승인된 Audit App/Tips와 동일 기능 의미 중복",
 "Xray Advice": "동일 배치 승인된 Xray App/Tips와 동일 기능 의미 중복",
}
R = {
 "Neighborhood Analysis": "분석 대상 불분명", "Litigation Coach": "코칭 대상 불분명",
 "Dependent Habit": "결합 불성립", "Migraine Fee": "결합 불성립",
 "Insomnia Price": "가격 지칭 부자연", "Skydiving Sum": "결합 불성립",
 "Acne Debt": "결합 불성립", "Snowboarding Charge": "결합 불성립",
 "Eczema Duty": "결합 불성립", "Ziplining Value": "결합 불성립",
 "Psoriasis Stake": "결합 불성립", "Sledding Number": "수치 지칭 부자연",
 "Vertigo Version": "결합 불성립", "Diving Detail": "결합 불성립",
 "Arthritis Identifier": "결합 불성립", "Sailing Field": "결합 불성립",
 "Menopause Format": "결합 불성립", "Rafting Signature": "결합 불성립",
 "Pregnancy Marker": "결합 불성립", "Climbing Asset": "결합 불성립",
 "Fertility Levy": "결합 불성립", "Biking Discount": "결합 불성립",
 "Thyroid Arrears": "결합 불성립", "Golf Markup": "결합 불성립",
 "Cholesterol Redemption": "결합 불성립", "Fishing Graph": "그래프 대상 불분명",
 "Hypertension Label": "결합 불성립", "Camping Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Anemia Schematic": "회로도 어휘 부자연", "Glamping Outline": "지형은 공예 오트라인 대상 아님",
 "Heartburn Rendering": "렌더링 대상 불분명", "Stargazing Count": "대상 불분명",
 "Constipation Message": "결합 불성립", "Birdwatching Repository": "결합 불성립",
 "Concussion Announcement": "결합 불성립", "Canyon Converter": "변환 대상 불분명",
 "Sprain Generator": "생성 대상 불분명", "Geyser Recorder": "기록 대상 불분명",
 "Fracture Estimator": "산출 대상 불분명", "Fjord Checker": "검사 대상 불분명",
 "Insulin Detector": "탐지 대상 불분명", "Savanna Timer": "결합 불성립",
 "Tundra Workshop": "결합 불성립", "Prairie Guardian": "감시 대상 불분명",
 "Marsh Helper": "결합 불성립", "Cove Stage": "결합 불성립",
 "Cliff Result": "결합 불성립", "Cavern Streak": "결합 불성립",
 "Oasis Rank": "결합 불성립", "Dune Trend": "결합 불성립",
 "Whale Comparison": "비교 대상 불분명", "Dolphin Proposal": "제안 대상 불분명",
 "Penguin Guarantee": "결합 불성립", "Flamingo Record": "기록 대상 불분명",
 "Turtle Copy": "결합 불성립", "Moose Reading": "결합 불성립",
 "Bison Reference": "결합 불성립", "Reindeer Forecast": "예측 대상 불분명",
 "Refund Workbook": "워크북 대상 불분명", "Reference Mode": "기능 토글로 읽혀 제품 불분명",
 "Agenda Spec": "결합 불성립", "Financing Quantity": "수량 대상 불분명",
 "Compliance Login": "결합 불성립", "Appointment Analysis": "분석 대상 불분명",
 "Waiver Habit": "결합 불성립",
 "Milestone Workbook": "워크북 대상 불분명", "Wellness Mode": "기능 토글로 읽혀 제품 불분명",
 "Scheduling Spec": "결합 불성립", "Snow Quantity": "수량 대상 불분명",
 "Inventory Login": "결합 불성립", "Alteration Analysis": "분석 대상 불분명",
 "Memorial Coach": "코칭 대상 불분명", "Checkout Habit": "결합 불성립",
 "Lawyer Memo": "결합 불성립", "Attorney Attribute": "결합 불성립",
 "Court Total": "결합 불성립", "Judge Template": "판사 대상 서식 불성립",
 "Jury Video": "결합 불성립", "Lawsuit Episode": "결합 불성립",
 "Closing Tips": "다의어로 서비스 대상 불분명(Closing App 기각 선례)",
 "Sponge Advice": "도구 지칭으로 대상 불성립(Sponge App 기각 선례)",
 "Trap Workbook": "워크북 대상 불분명", "Roadtrip Mode": "기능 토글로 읽혀 제품 불분명",
 "Accordion Spec": "결합 불성립", "Allergy Quantity": "수량 대상 불분명",
 "Wire Login": "결합 불성립", "Divorce Analysis": "분석 대상 불분명",
 "Chassis Coach": "코칭 대상 불분명", "Amendment Habit": "결합 불성립",
 "Custody Terminal": "결합 불성립", "Immigration Counter": "결합 불성립",
 "Testament Update": "갱신 대상 불분명(Testament 계열 기각 선례)",
 "Notary Confirmation": "확인 대상 불분명", "Mediation Identifier": "결합 불성립",
 "Guardianship Diagram": "교육 다이어그램 축 대상 아님", "Trademark Streak": "결합 불성립",
 "Patent Validation": "검증 대상 불분명", "Copyright Recipe": "결합 불성립",
 "Curb Workbook": "워크북 대상 불분명", "Vineyard Mode": "기능 토글로 읽혀 제품 불분명",
 "Accompanist Spec": "결합 불성립", "Illness Quantity": "수량 대상 불분명",
 "Debtor Login": "결합 불성립", "Flatbed Analysis": "분석 대상 불분명",
 "Neighborhood Coach": "코칭 대상 불분명", "Litigation Habit": "결합 불성립",
 "Migraine Item": "항목 대상 불분명", "Insomnia Fare": "결합 불성립",
 "Skydiving Debt": "결합 불성립", "Acne Fund": "자금 근거 약함",
 "Snowboarding Duty": "결합 불성립", "Eczema Allowance": "결합 불성립",
 "Ziplining Stake": "결합 불성립", "Psoriasis Margin": "결합 불성립",
 "Sledding Version": "결합 불성립", "Vertigo Link": "결합 불성립",
 "Diving Identifier": "결합 불성립", "Arthritis Category": "결합 불성립",
 "Sailing Format": "결합 불성립", "Menopause Serial": "결합 불성립",
 "Rafting Marker": "결합 불성립", "Pregnancy Balance": "결합 불성립",
 "Climbing Levy": "결합 불성립", "Fertility Due": "결합 불성립",
 "Biking Arrears": "결합 불성립", "Thyroid Advance": "결합 불성립",
 "Golf Redemption": "결합 불성립", "Cholesterol Extension": "결합 불성립",
 "Fishing Label": "결합 불성립", "Hypertension Manual": "설명 대상 불분명",
 "Camping Schematic": "회로도 어휘 부자연", "Anemia Layout": "결합 불성립",
 "Glamping Rendering": "렌더링 대상 불분명", "Heartburn Notification": "결합 불성립",
 "Stargazing Message": "결합 불성립", "Constipation Total": "결합 불성립",
 "Birdwatching Announcement": "결합 불성립", "Concussion Calculator": "계산 대상 불분명",
 "Canyon Generator": "생성 대상 불분명", "Sprain Recorder": "기록 대상 불분명",
 "Geyser Estimator": "산출 대상 불분명", "Fracture Checker": "검사 대상 불분명",
 "Fjord Detector": "탐지 대상 불분명", "Insulin Timer": "결합 불성립",
 "Savanna Workshop": "결합 불성립", "Tundra Guardian": "감시 대상 불분명",
 "Prairie Helper": "결합 불성립", "Marsh Stage": "결합 불성립",
 "Cove Result": "결합 불성립", "Cliff Streak": "결합 불성립",
 "Cavern Rank": "결합 불성립", "Oasis Trend": "결합 불성립",
 "Dune Comparison": "비교 대상 불분명", "Whale Proposal": "제안 대상 불분명",
 "Dolphin Guarantee": "결합 불성립", "Penguin Record": "기록 대상 불분명",
 "Flamingo Copy": "결합 불성립", "Turtle Reading": "결합 불성립",
 "Moose Reference": "결합 불성립", "Bison Forecast": "예측 대상 불분명",
 "Reindeer Deadline": "결합 불성립",
 "Pipeline Workbook": "워크북 대상 불분명", "Refund Mode": "기능 토글로 읽혀 제품 불분명",
 "Reference Spec": "결합 불성립", "Agenda Quantity": "수량 대상 불분명",
 "Financing Login": "결합 불성립", "Compliance Analysis": "분석 대상 불분명",
 "Appointment Coach": "코칭 대상 불분명",
 "Session Workbook": "워크북 대상 불분명", "Milestone Mode": "기능 토글로 읽혀 제품 불분명",
 "Wellness Spec": "결합 불성립", "Scheduling Quantity": "수량 대상 불분명",
 "Snow Login": "결합 불성립", "Inventory Analysis": "분석 대상 불분명",
 "Alteration Coach": "코칭 대상 불분명", "Memorial Habit": "결합 불성립",
 "Lawyer Quota": "결합 불성립", "Attorney Field": "결합 불성립",
 "Court Widget": "위젯 대상 불분명", "Judge Guide": "판사 대상 안내 불성립",
 "Jury Diary": "결합 불성립", "Lawsuit Cycle": "결합 불성립",
 "Sponge Workbook": "도구 지칭으로 대상 불성립", "Trap Mode": "기능 토글로 읽혀 제품 불분명",
 "Closing Advice": "다의어로 서비스 대상 불분명(Closing App 기각 선례)",
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
out = base + r"\_dec_c18.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
