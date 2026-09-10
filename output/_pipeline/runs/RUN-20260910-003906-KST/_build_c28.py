# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk28_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Ensemble App": (0.55, "합주단·합창단 운영 앱(실재)"),
 "Injury Tips": (0.55, "부상 관리 팁(App→Tips 평행)"),
 "Payment App": (0.6, "결제 관리 앱(실재 카테고리)"),
 "Redline Tips": (0.55, "계약 수정 팁(App→Tips 평행)"),
 "Alumni Tips": (0.55, "동문 관리 팁(App→Tips 평행)"),
 "Caption App": (0.6, "자막 생성 관리 앱(실재 카테고리)"),
 "Sentiment Tips": (0.55, "감성 분석 팁(App→Tips 평행)"),
 "Casino App": (0.6, "카지노 리조트 안내 앱(실재 카테고리)"),
 "Ensemble Tips": (0.55, "합주 운영 팁(App→Tips 평행)"),
 "Trademark Template": (0.55, "상표 출원 서식(Patent Template 평행)"),
 "Trademark Guide": (0.55, "상표 등록 가이드(Patent Guide 평행)"),
 "Payment Tips": (0.55, "결제 관리 팁(App→Tips 평행)"),
 "Bundle App": (0.55, "상품 번들 구성 앱(실재)"),
 "Patent Correction": (0.55, "특허 정정 절차(certificate of correction 실재)"),
 "Lawsuit Tutorial": (0.55, "소송 절차 안내(Divorce Tutorial 평행)"),
 "Immigration Form": (0.55, "이민 서류 작성 서비스(실재)"),
}
R_DUP = {
 "Creditor Advice": "동일 배치 승인된 Creditor App/Tips와 동일 기능 의미 중복",
 "Pallet Advice": "동일 배치 승인된 Pallet App/Tips와 동일 기능 의미 중복",
 "Throughput Advice": "동일 배치 승인된 Throughput App/Tips와 동일 기능 의미 중복",
 "Recruiter Advice": "동일 배치 승인된 Recruiter App/Tips와 동일 기능 의미 중복",
 "Injury Advice": "동일 배치 승인된 Injury App/Tips와 동일 기능 의미 중복",
 "Redline Advice": "동일 배치 승인된 Redline App/Tips와 동일 기능 의미 중복",
 "Alumni Advice": "동일 배치 승인된 Alumni App/Tips와 동일 기능 의미 중복",
}
R = {
 "Custody Engine": "결합 불성립", "Immigration Log": "기록 대상 불분명",
 "Testament Slot": "Testament 계열 기각 선례", "Notary Charge": "결합 불성립",
 "Mediation Advance": "결합 불성립", "Guardianship Recorder": "기록 대상 불분명",
 "Patent Revision": "표준 절차 용어 아님", "Copyright Clock": "결합 불성립",
 "Reefer Workbook": "워크북 대상 불분명", "Renovation Mode": "기능 토글로 읽혀 제품 불분명",
 "Adjustment Spec": "결합 불성립", "Training Quantity": "수량 대상 불분명",
 "Patio Login": "결합 불성립", "Transfer Analysis": "분석 대상 불분명",
 "Ward Coach": "코칭 대상 불분명", "Feature Habit": "다의어로 대상 불분명(Feature App 기각 선례)",
 "Migraine Value": "결합 불성립", "Insomnia Version": "결합 불성립",
 "Skydiving Identifier": "결합 불성립", "Acne Category": "결합 불성립",
 "Snowboarding Serial": "결합 불성립", "Eczema Token": "결합 불성립",
 "Ziplining Balance": "결합 불성립", "Psoriasis Interest": "결합 불성립",
 "Sledding Due": "결합 불성립", "Vertigo Subsidy": "결합 불성립",
 "Diving Advance": "결합 불성립", "Arthritis Penalty": "결합 불성립",
 "Sailing Extension": "결합 불성립", "Menopause Trial": "결합 불성립",
 "Rafting Manual": "설명 대상 불분명", "Pregnancy Worksheet": "학습지 근거 약함",
 "Climbing Layout": "결합 불성립", "Fertility Sketch": "제품성 불분명",
 "Biking Notification": "결합 불성립", "Thyroid Kit": "키트 대상 불분명",
 "Golf Total": "결합 불성립", "Cholesterol Widget": "위젯 대상 불분명",
 "Fishing Calculator": "계산 대상 불분명", "Hypertension Converter": "변환 대상 불분명",
 "Camping Estimator": "산출 대상 불분명", "Anemia Checker": "검사 대상 불분명",
 "Glamping Workshop": "결합 불성립", "Heartburn Guardian": "감시 대상 불분명",
 "Stargazing Result": "결합 불성립", "Constipation Streak": "결합 불성립",
 "Birdwatching Comparison": "비교 대상 불분명", "Concussion Proposal": "제안 대상 불분명",
 "Canyon Record": "기록 대상 불분명", "Sprain Copy": "결합 불성립",
 "Geyser Reading": "결합 불성립", "Fracture Reference": "결합 불성립",
 "Fjord Forecast": "예측 대상 불분명", "Insulin Deadline": "결합 불성립",
 "Savanna Duration": "결합 불성립", "Tundra Volume": "결합 불성립",
 "Prairie Diagnostic": "진단 대상 불분명", "Marsh Progress": "결합 불성립",
 "Cove Authorization": "결합 불성립", "Cliff Template": "결합 불성립",
 "Cavern Guide": "가이드 대상 불분명", "Oasis Rating": "평가 대상 불분명",
 "Dune Agreement": "결합 불성립", "Whale Reply": "결합 불성립",
 "Dolphin Account": "결합 불성립", "Penguin Case": "결합 불성립",
 "Flamingo Match": "결합 불성립", "Turtle Validation": "결합 불성립",
 "Moose Lookup": "탐색 대상 불분명", "Bison Ping": "결합 불성립",
 "Reindeer Model": "결합 불성립",
 "Coverage Mode": "기능 토글로 읽혀 제품 불분명", "Leave Spec": "결합 불성립",
 "Change Quantity": "수량 대상 불분명", "Vendor Login": "결합 불성립",
 "Concierge Analysis": "분석 대상 불분명", "Grading Coach": "코칭 대상 불분명",
 "Silo Workbook": "워크북 대상 불분명", "Ledger Spec": "결합 불성립",
 "Ballot Quantity": "수량 대상 불분명", "Placement Login": "결합 불성립",
 "Feed Analysis": "분석 대상 불분명", "Permit Coach": "코칭 대상 불분명",
 "Network Habit": "결합 불성립",
 "Lawyer Tax": "결합 불성립", "Attorney Redemption": "결합 불성립",
 "Court Rank": "결합 불성립", "Judge Invoice": "결합 불성립",
 "Jury Speed": "결합 불성립",
 "Sentiment Advice SKIP": "",
 "Lanyard Workbook": "워크북 대상 불분명", "Checkup Mode": "기능 토글로 읽혀 제품 불분명",
 "Cafe Spec": "결합 불성립", "Flea Quantity": "수량 대상 불분명",
 "Gum Login": "결합 불성립", "Craft Analysis": "분석 대상 불분명",
 "Dishwasher Coach": "코칭 대상 불분명", "Blowout Habit": "결합 불성립",
 "Divorce Loop": "결합 불성립", "Custody Assistant": "지원 대상 불분명",
 "Testament Pass": "Testament 계열 기각 선례", "Notary Duty": "결합 불성립",
 "Mediation Penalty": "결합 불성립", "Guardianship Estimator": "산출 대상 불분명",
 "Copyright Time": "결합 불성립",
 "Creditor Workbook SKIP": "",
 "Reefer Mode": "기능 토글로 읽혀 제품 불분명", "Renovation Spec": "결합 불성립",
 "Adjustment Quantity": "수량 대상 불분명", "Training Login": "결합 불성립",
 "Patio Analysis": "분석 대상 불분명", "Transfer Coach": "코칭 대상 불분명",
 "Ward Habit": "결합 불성립",
 "Migraine Stake": "결합 불성립", "Insomnia Link": "결합 불성립",
 "Skydiving Category": "결합 불성립", "Acne Attribute": "결합 불성립",
 "Snowboarding Token": "결합 불성립", "Eczema Signature": "결합 불성립",
 "Ziplining Interest": "결합 불성립", "Psoriasis Asset": "결합 불성립",
 "Sledding Subsidy": "결합 불성립", "Vertigo Discount": "결합 불성립",
 "Diving Penalty": "결합 불성립", "Arthritis Markup": "결합 불성립",
 "Sailing Trial": "결합 불성립", "Menopause Graph": "그래프 대상 불분명",
 "Rafting Worksheet": "학습지 근거 약함", "Pregnancy Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Climbing Sketch": "제품성 불분명", "Fertility Outline": "지형은 공예 오트라인 대상 아님",
 "Biking Kit": "키트 대상 불분명", "Thyroid Count": "대상 불분명",
 "Golf Widget": "위젯 대상 불분명", "Cholesterol Repository": "결합 불성립",
 "Fishing Converter": "변환 대상 불분명", "Hypertension Generator": "생성 대상 불분명",
 "Camping Checker": "검사 대상 불분명", "Anemia Detector": "탐지 대상 불분명",
 "Glamping Guardian": "감시 대상 불분명", "Heartburn Helper": "결합 불성립",
 "Stargazing Streak": "결합 불성립", "Constipation Rank": "결합 불성립",
 "Birdwatching Proposal": "제안 대상 불분명", "Concussion Guarantee": "결합 불성립",
 "Canyon Copy": "결합 불성립", "Sprain Reading": "결합 불성립",
 "Geyser Reference": "결합 불성립", "Fracture Forecast": "예측 대상 불분명",
 "Fjord Deadline": "결합 불성립", "Insulin Duration": "결합 불성립",
 "Savanna Volume": "결합 불성립", "Tundra Diagnostic": "진단 대상 불분명",
 "Prairie Progress": "결합 불성립", "Marsh Authorization": "결합 불성립",
 "Cove Template": "결합 불성립", "Cliff Guide": "가이드 대상 불분명",
 "Cavern Rating": "평가 대상 불분명", "Oasis Agreement": "결합 불성립",
 "Dune Reply": "결합 불성립", "Whale Account": "결합 불성립",
 "Dolphin Case": "결합 불성립", "Penguin Match": "결합 불성립",
 "Flamingo Validation": "결합 불성립", "Turtle Lookup": "탐색 대상 불분명",
 "Moose Ping": "결합 불성립", "Bison Model": "결합 불성립",
 "Reindeer Availability": "상태 명사로 제품명 부자연",
 "Pallet Workbook": "워크북 대상 불분명", "Coverage Spec": "결합 불성립",
 "Leave Quantity": "수량 대상 불분명", "Change Login": "결합 불성립",
 "Vendor Analysis": "분석 대상 불분명", "Concierge Coach": "코칭 대상 불분명",
 "Grading Habit": "결합 불성립",
 "Silo Mode": "기능 토글로 읽혀 제품 불분명", "Ledger Quantity": "수량 대상 불분명",
}
del R["Sentiment Advice SKIP"]
R["Creditor Workbook"] = "워크북 대상 불분명"
R["Throughput Workbook"] = "워크북 대상 불분명"
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
out = base + r"\_dec_c28.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
