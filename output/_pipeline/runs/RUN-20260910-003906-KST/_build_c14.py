# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk14_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Immigration Playbook": (0.55, "이민 실무 매뉴얼(실무 지침서 실재)"),
 "Patent Template": (0.55, "특허 출원 서식(실재)"),
 "Flatbed App": (0.55, "평판 트레일러 운송 앱(flatbed trucking 실재)"),
 "Neighborhood Tips": (0.55, "동네 정보 팁(App→Tips 평행)"),
 "Acne Plan": (0.55, "여드름 관리 계획(건강 관리 플랜 축)"),
 "Compliance App": (0.6, "위생 규정 준수 관리 앱(식음 실재)"),
 "Appointment Tips": (0.55, "예약 관리 팁(App→Tips 평행)"),
 "Inventory App": (0.6, "재고 관리 앱(실재 카테고리)"),
 "Alteration Tips": (0.55, "의류 수선 팁(App→Tips 평행)"),
 "Wire App": (0.6, "와이어 송금 앱(실재 카테고리)"),
 "Divorce Tips": (0.55, "이혼 절차 팁(App→Tips 평행)"),
 "Patent Guide": (0.55, "특허 출원 가이드(실재)"),
 "Debtor App": (0.55, "채무자 관리 앱(회수 업무 실재)"),
 "Flatbed Tips": (0.55, "평판 운송 팁(App→Tips 평행)"),
 "Acne Cost": (0.55, "여드름 치료 비용(건강 비용 축)"),
 "Financing App": (0.6, "차량 금융 앱(auto financing 실재)"),
 "Compliance Tips": (0.55, "규정 준수 팁(App→Tips 평행)"),
 "Snow App": (0.6, "제설 요청·관리 앱(snow removal 실재)"),
 "Inventory Tips": (0.55, "재고 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Litigation Advice": "동일 배치 승인된 Litigation App/Tips와 동일 기능 의미 중복",
 "Memorial Advice": "동일 배치 승인된 Memorial App/Tips와 동일 기능 의미 중복",
 "Chassis Advice": "동일 배치 승인된 Chassis App/Tips와 동일 기능 의미 중복",
 "Neighborhood Advice": "동일 배치 승인된 Neighborhood App/Tips와 동일 기능 의미 중복",
 "Appointment Advice": "동일 배치 승인된 Appointment App/Tips와 동일 기능 의미 중복",
 "Alteration Advice": "동일 배치 승인된 Alteration App/Tips와 동일 기능 의미 중복",
}
R = {
 "Testament Tag": "결합 불성립", "Notary Memo": "결합 불성립",
 "Mediation Stake": "결합 불성립", "Guardianship Markup": "결합 불성립",
 "Trademark Checker": "검사 대상 불분명", "Copyright Correction": "결합 불성립",
 "Dependent Workbook": "워크북 대상 불분명", "Cabinetry Mode": "기능 토글로 읽혀 제품 불분명",
 "Withdrawal Spec": "결합 불성립", "Latte Quantity": "수량 대상 불분명",
 "Behavior Login": "결합 불성립", "Toothbrush Analysis": "분석 대상 불분명",
 "Nanny Coach": "코칭 대상 불분명", "Sidewalk Habit": "결합 불성립",
 "Migraine Brief": "결합 불성립", "Insomnia Recap": "결합 불성립",
 "Skydiving Unit": "결합 불성립",
 "Snowboarding Tax": "결합 불성립", "Eczema Loan": "결합 불성립",
 "Ziplining Fund": "결합 불성립", "Psoriasis Cash": "결합 불성립",
 "Sledding Duty": "결합 불성립", "Vertigo Allowance": "결합 불성립",
 "Diving Stake": "결합 불성립", "Arthritis Margin": "결합 불성립",
 "Sailing Version": "결합 불성립", "Menopause Link": "결합 불성립",
 "Rafting Identifier": "결합 불성립", "Pregnancy Category": "결합 불성립",
 "Climbing Format": "결합 불성립", "Fertility Serial": "결합 불성립",
 "Biking Marker": "결합 불성립", "Thyroid Balance": "결합 불성립",
 "Golf Levy": "결합 불성립", "Cholesterol Due": "결합 불성립",
 "Fishing Arrears": "결합 불성립", "Hypertension Advance": "결합 불성립",
 "Camping Redemption": "결합 불성립", "Anemia Extension": "결합 불성립",
 "Glamping Label": "결합 불성립", "Heartburn Manual": "설명 대상 불분명",
 "Stargazing Schematic": "회로도 어휘 부자연", "Constipation Layout": "결합 불성립",
 "Birdwatching Rendering": "렌더링 대상 불분명", "Concussion Notification": "결합 불성립",
 "Canyon Count": "대상 불분명", "Sprain Message": "결합 불성립",
 "Geyser Total": "결합 불성립", "Fracture Widget": "위젯 대상 불분명",
 "Fjord Repository": "결합 불성립", "Insulin Announcement": "결합 불성립",
 "Savanna Calculator": "계산 대상 불분명", "Tundra Converter": "변환 대상 불분명",
 "Prairie Generator": "생성 대상 불분명", "Marsh Recorder": "기록 대상 불분명",
 "Cove Estimator": "산출 대상 불분명", "Cliff Checker": "검사 대상 불분명",
 "Cavern Detector": "탐지 대상 불분명", "Oasis Timer": "결합 불성립",
 "Dune Workshop": "결합 불성립", "Whale Guardian": "감시 대상 불분명",
 "Dolphin Helper": "결합 불성립", "Penguin Stage": "결합 불성립",
 "Flamingo Result": "결합 불성립", "Turtle Streak": "결합 불성립",
 "Moose Rank": "결합 불성립", "Bison Trend": "결합 불성립",
 "Reindeer Comparison": "비교 대상 불분명",
 "Waiver Workbook": "워크북 대상 불분명", "Immunization Mode": "기능 토글로 읽혀 제품 불분명",
 "Family Spec": "결합 불성립", "Chemical Quantity": "수량 대상 불분명",
 "Inspection Analysis": "분석 대상 불분명", "Pricing Coach": "코칭 대상 불분명",
 "Cemetery Habit": "결합 불성립",
 "Checkout Workbook": "워크북 대상 불분명", "Recall Mode": "기능 토글로 읽혀 제품 불분명",
 "Port Spec": "결합 불성립", "Logbook Quantity": "수량 대상 불분명",
 "Tailings Login": "결합 불성립", "Coil Analysis": "분석 대상 불분명",
 "Keypad Coach": "코칭 대상 불분명", "Bilingual Habit": "결합 불성립",
 "Lawyer Sample": "결합 불성립", "Attorney Number": "수치 지칭 부자연",
 "Court Sketch": "제품성 불분명", "Judge Forecast": "예측 대상 불분명",
 "Jury Payment": "결합 불성립", "Lawsuit Brightness": "결합 불성립",
 "Amendment Workbook": "워크북 대상 불분명", "Salvage Mode": "기능 토글로 읽혀 제품 불분명",
 "Pension Spec": "결합 불성립", "Siding Quantity": "수량 대상 불분명",
 "Thesis Login": "결합 불성립", "Meeting Analysis": "분석 대상 불분명",
 "Headline Coach": "코칭 대상 불분명", "Priority Habit": "결합 불성립",
 "Custody Core": "결합 불성립", "Immigration Journal": "저널 대상 불분명",
 "Testament Profile": "결합 불성립", "Notary Quota": "결합 불성립",
 "Mediation Margin": "결합 불성립", "Guardianship Redemption": "결합 불성립",
 "Trademark Detector": "탐지 대상 불분명", "Copyright Revision": "결합 불성립",
 "Litigation Workbook": "워크북 대상 불분명", "Dependent Mode": "기능 토글로 읽혀 제품 불분명",
 "Cabinetry Spec": "결합 불성립", "Withdrawal Quantity": "수량 대상 불분명",
 "Latte Login": "결합 불성립", "Behavior Analysis": "분석 대상 불분명",
 "Toothbrush Coach": "코칭 대상 불분명", "Nanny Habit": "결합 불성립",
 "Migraine Circular": "결합 불성립", "Insomnia Entry": "등록 대상 불분명",
 "Skydiving Plan": "계획 대상 불분명(Sailing Plan 기각 선례)",
 "Snowboarding Loan": "결합 불성립", "Eczema Sum": "결합 불성립",
 "Ziplining Cash": "결합 불성립", "Psoriasis Sale": "결합 불성립",
 "Sledding Allowance": "결합 불성립", "Vertigo Tariff": "결합 불성립",
 "Diving Margin": "결합 불성립", "Arthritis Fine": "결합 불성립",
 "Sailing Link": "결합 불성립", "Menopause Rule": "결합 불성립",
 "Rafting Category": "결합 불성립", "Pregnancy Attribute": "결합 불성립",
 "Climbing Serial": "결합 불성립", "Fertility Token": "결합 불성립",
 "Biking Balance": "결합 불성립", "Thyroid Interest": "결합 불성립",
 "Golf Due": "결합 불성립", "Cholesterol Subsidy": "결합 불성립",
 "Fishing Advance": "결합 불성립", "Hypertension Penalty": "결합 불성립",
 "Camping Extension": "결합 불성립", "Anemia Trial": "결합 불성립",
 "Glamping Manual": "설명 대상 불분명", "Heartburn Worksheet": "학습지 근거 약함",
 "Stargazing Layout": "결합 불성립", "Constipation Sketch": "제품성 불분명",
 "Birdwatching Notification": "결합 불성립", "Concussion Kit": "키트 대상 불분명",
 "Canyon Message": "결합 불성립", "Sprain Total": "결합 불성립",
 "Geyser Widget": "위젯 대상 불분명", "Fracture Repository": "결합 불성립",
 "Fjord Announcement": "결합 불성립", "Insulin Calculator": "계산 대상 불분명",
 "Savanna Converter": "변환 대상 불분명", "Tundra Generator": "생성 대상 불분명",
 "Prairie Recorder": "기록 대상 불분명", "Marsh Estimator": "산출 대상 불분명",
 "Cove Checker": "검사 대상 불분명", "Cliff Detector": "탐지 대상 불분명",
 "Cavern Timer": "결합 불성립", "Oasis Workshop": "결합 불성립",
 "Dune Guardian": "감시 대상 불분명", "Whale Helper": "결합 불성립",
 "Dolphin Stage": "결합 불성립", "Penguin Result": "결합 불성립",
 "Flamingo Streak": "결합 불성립", "Turtle Rank": "결합 불성립",
 "Moose Trend": "결합 불성립", "Bison Comparison": "비교 대상 불분명",
 "Reindeer Proposal": "제안 대상 불분명",
 "Waiver Mode": "기능 토글로 읽혀 제품 불분명", "Immunization Spec": "결합 불성립",
 "Family Quantity": "수량 대상 불분명", "Chemical Login": "결합 불성립",
 "Inspection Coach": "코칭 대상 불분명", "Pricing Habit": "결합 불성립",
 "Memorial Workbook": "워크북 대상 불분명", "Checkout Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c14.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
