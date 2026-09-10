# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk38_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Comparable App": (0.6, "부동산 실거가 comps 비교 앱(실재 시장)"),
 "Payout Tips": (0.55, "보험금 수령 팁(App→Tips 평행)"),
 "Attendance Analysis": (0.55, "행사 참석 데이터 분석(Attendance App 평행)"),
 "Pregnancy Recorder": (0.55, "임신 기록 저널(실재 앱)"),
 "Cholesterol Trend": (0.55, "혈지 추이 기록(Hypertension Trend 평행)"),
 "Hypertension Record": (0.6, "혈압 측정 기록(실검색 실재)"),
 "Constipation Guide": (0.55, "변비 관리 가이드(건강 가이드 실재)"),
 "Retail App": (0.55, "살롱 소매 판매 관리 앱(실재)"),
 "Adherence Tips": (0.55, "복약 순응 팁(App→Tips 평행)"),
 "Route App": (0.65, "경로 계획 앱(이사·물류 실재 시장)"),
 "Lighting Tips": (0.55, "사진 조명 팁(App→Tips 평행)"),
 "License App": (0.6, "사진 라이선스 관리 앱(실재)"),
 "Registrar Tips": (0.55, "혼인 등기 절차 팁(App→Tips 평행)"),
 "Divorce Portal": (0.55, "온라인 이혼 서류 포털(실재)"),
 "Immigration Timeline": (0.55, "비자 처리 기간 타임라인(실검색 실재)"),
 "Trademark Renewal": (0.6, "상표 갱신 서비스(USPTO 실재)"),
 "Comparable Tips": (0.55, "comps 비교 팁(App→Tips 평행)"),
 "Eczema Manual": (0.55, "아토피 자가관리 매뉴얼(Arthritis Manual 평행)"),
 "Menopause Calculator": (0.55, "폐경 시기 추정 계산기(실재)"),
 "Stargazing Guide": (0.55, "별 관측 가이드(Birdwatching Guide 평행)"),
 "Retail Tips": (0.55, "살롱 소매 판매 팁(App→Tips 평행)"),
}
R_DUP = {
 "Probation Advice": "동일 배치 승인된 Probation App/Tips와 동일 기능 의미 중복",
 "Berth Advice": "동일 배치 승인된 Berth App/Tips와 동일 기능 의미 중복",
 "Landscaping Advice": "동일 배치 승인된 Landscaping App/Tips와 동일 기능 의미 중복",
 "Payout Advice": "동일 배치 승인된 Payout App/Tips와 동일 기능 의미 중복",
 "Pregnancy Estimator": "동일 배치 승인된 Pregnancy Calculator와 기능 중복(Fertility Estimator 선례)",
 "Adherence Advice": "동일 배치 승인된 Adherence App/Tips와 동일 기능 의미 중복",
}
R = {
 "Remittance Analysis": "분석 대상 불분명", "Lawsuit Coach": "코칭 대상 불분명",
 "Trailer Habit": "결합 불성립", "Divorce Zone": "결합 불성립",
 "Custody Kiosk": "결합 불성립", "Immigration Summary": "요약 대상 불분명",
 "Testament Item": "결합 불성립", "Notary Serial": "결합 불성립",
 "Mediation Count": "카운트 대상 불분명", "Guardianship Reading": "결합 불성립",
 "Trademark Invoice": "결합 불성립", "Patent Size": "결합 불성립",
 "Copyright Episode": "결합 불성립", "Comparable App SKIP": "",
 "Deck Workbook": "워크북 대상 불분명", "Rubric Mode": "기능 토글로 읽혀 제품 불분명",
 "Referendum Spec": "사양 참조로 제품 불분명", "Story Quantity": "수량 대상 불분명",
 "Internship Login": "제품 불분명", "Transmission Coach": "코칭 대상 불분명",
 "Donut Habit": "결합 불성립", "Migraine Balance": "결합 불성립",
 "Insomnia Subsidy": "결합 불성립", "Skydiving Penalty": "결합 불성립",
 "Acne Markup": "마크업 대상 불분명", "Snowboarding Graph": "그래프 대상 불분명",
 "Eczema Label": "결합 불성립", "Ziplining Diagram": "도식 대상 불분명",
 "Psoriasis Schematic": "도식 대상 불분명", "Sledding Outline": "개요 대상 불분명",
 "Vertigo Rendering": "결합 불성립", "Diving Count": "카운트 대상 불분명",
 "Arthritis Message": "메시지 대상 불분명", "Sailing Repository": "결합 불성립",
 "Menopause Announcement": "이벤트 명칭으로 제품 불분명", "Rafting Generator": "생성 대상 불분명",
 "Climbing Detector": "탐지 대상 불분명", "Fertility Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Biking Helper": "도우미 대상 불분명", "Thyroid Stage": "단계 대상 불분명",
 "Golf Rank": "결합 불성립", "Fishing Guarantee": "결합 불성립",
 "Camping Reference": "결합 불성립", "Anemia Forecast": "결합 불성립",
 "Glamping Volume": "결합 불성립", "Heartburn Diagnostic": "진단 대상 불분명",
 "Stargazing Template": "결합 불성립", "Birdwatching Reply": "결합 불성립",
 "Concussion Account": "결합 불성립", "Canyon Match": "결합 불성립",
 "Sprain Validation": "결합 불성립", "Geyser Lookup": "탐색 대상 불분명",
 "Fracture Ping": "결합 불성립", "Fjord Model": "결합 불성립",
 "Insulin Availability": "상태 명사로 제품명 부자연", "Savanna Eligibility": "결합 불성립",
 "Tundra Broadcast": "결합 불성립", "Prairie Barcode": "결합 불성립",
 "Marsh Appointment": "약속 대상 불분명", "Cove Feedback": "결합 불성립",
 "Cliff Invoice": "결합 불성립", "Cavern Renewal": "갱신 대상 불분명",
 "Oasis Quote": "인용·견적 중의로 대상 불분명", "Dune Warranty": "결합 불성립",
 "Whale Deposit": "결합 불성립", "Dolphin Certification": "결합 불성립",
 "Penguin Nomination": "결합 불성립", "Flamingo Correction": "결합 불성립",
 "Turtle Revision": "결합 불성립", "Moose Payment": "결합 불성립",
 "Bison Verification": "결합 불성립", "Reindeer Simulator": "결합 불성립",
 "Retail App SKIP": "", "Berth Advice DUP": "",
 "Compressor Spec": "사양 참조로 제품 불분명", "Cylinder Quantity": "수량 대상 불분명",
 "Proofing Login": "제품 불분명", "Unpacking Analysis": "분석 대상 불분명",
 "Proof Coach": "코칭 대상 불분명", "Invitation Habit": "결합 불성립",
 "Route App SKIP": "", "Favor Advice": "팁 대상 불분명(Favor App 기각 선례)",
 "Occupant Workbook": "워크북 대상 불분명", "Technician Mode": "기능 토글로 읽혀 제품 불분명",
 "Rinse Spec": "사양 참조로 제품 불분명", "Plunger Quantity": "수량 대상 불분명",
 "Sightseeing Login": "제품 불분명", "Clarinet Analysis": "분석 대상 불분명",
 "Consent Coach": "코칭 대상 불분명", "Escrow Habit": "결합 불성립",
 "Lawyer Rule": "결합 불성립", "Attorney Widget": "결합 불성립",
 "Court Rating": "평가 대상 불분명", "Judge Refund": "결합 불성립",
 "Jury Breakdown": "결합 불성립", "License App SKIP": "",
 "Opening Workbook": "워크북 대상 불분명", "Bucket Mode": "기능 토글로 읽혀 제품 불분명",
 "Softener Spec": "사양 참조로 제품 불분명", "Traveler Quantity": "수량 대상 불분명",
 "Mandolin Login": "제품 불분명", "Vaccine Analysis": "분석 대상 불분명",
 "Remittance Coach": "코칭 대상 불분명", "Lawsuit Habit": "결합 불성립",
 "Custody Bay": "결합 불성립", "Testament Unit": "결합 불성립",
 "Notary Token": "결합 불성립", "Mediation Message": "메시지 대상 불분명",
 "Guardianship Reference": "결합 불성립", "Patent Length": "결합 불성립",
 "Copyright Cycle": "결합 불성립", "Bulk App": "제품 불분명",
 "Deck Mode": "기능 토글로 읽혀 제품 불분명", "Probation Workbook": "워크북 대상 불분명",
 "Rubric Spec": "사양 참조로 제품 불분명",
 "Referendum Quantity": "수량 대상 불분명", "Story Login": "제품 불분명",
 "Internship Analysis": "분석 대상 불분명", "Attendance Coach": "코칭 대상 불분명",
 "Transmission Habit": "결합 불성립", "Migraine Interest": "결합 불성립",
 "Insomnia Discount": "판촉 계열 기각 선례", "Skydiving Markup": "마크업 대상 불분명",
 "Acne Redemption": "결합 불성립", "Snowboarding Label": "결합 불성립",
 "Ziplining Schematic": "도식 대상 불분명", "Psoriasis Layout": "결합 불성립",
 "Sledding Rendering": "결합 불성립", "Vertigo Notification": "알림 내용 불특정",
 "Diving Message": "결합 불성립", "Arthritis Total": "결합 불성립",
 "Sailing Announcement": "결합 불성립", "Rafting Recorder": "기록 대상 불분명",
 "Climbing Timer": "결합 불성립(Timer 계열 기각 선례)", "Fertility Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Biking Stage": "단계 대상 불분명", "Thyroid Result": "결합 불성립",
 "Golf Trend": "결합 불성립", "Cholesterol Comparison": "비교 대상 불분명",
 "Fishing Record": "기록 대상 불분명(Camping Record 기각 선례)", "Hypertension Copy": "결합 불성립",
 "Camping Forecast": "결합 불성립", "Anemia Deadline": "결합 불성립",
 "Glamping Diagnostic": "진단 대상 불분명", "Heartburn Progress": "진행 대상 불분명",
 "Constipation Rating": "평가 대상 불분명", "Birdwatching Account": "결합 불성립",
 "Concussion Case": "결합 불성립", "Canyon Validation": "결합 불성립",
 "Sprain Lookup": "탐색 대상 불분명", "Geyser Ping": "결합 불성립",
 "Fracture Model": "결합 불성립", "Fjord Availability": "상태 명사로 제품명 부자연",
 "Insulin Eligibility": "결합 불성립", "Savanna Broadcast": "결합 불성립",
 "Tundra Barcode": "결합 불성립", "Prairie Appointment": "약속 대상 불분명",
 "Marsh Feedback": "결합 불성립", "Cove Invoice": "결합 불성립",
 "Cliff Renewal": "갱신 대상 불분명", "Cavern Quote": "인용·견적 중의로 대상 불분명",
 "Oasis Warranty": "결합 불성립", "Dune Deposit": "결합 불성립",
 "Whale Certification": "결합 불성립", "Dolphin Nomination": "결합 불성립",
 "Penguin Correction": "결합 불성립", "Flamingo Revision": "결합 불성립",
 "Turtle Payment": "결합 불성립", "Moose Verification": "결합 불성립",
 "Bison Simulator": "결합 불성립", "Reindeer Predictor": "예측 대상 불분명",
 "Service App": "제품 불분명(장례 서비스로 읽기 어려움)",
 "Berth Workbook": "워크북 대상 불분명", "Compressor Quantity": "수량 대상 불분명",
 "Cylinder Login": "제품 불분명", "Proofing Analysis": "분석 대상 불분명",
 "Unpacking Coach": "코칭 대상 불분명", "Proof Habit": "결합 불성립",
}
for k in [k for k in R if k.endswith(" SKIP") or k.endswith(" DUP")]:
    del R[k]
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
out = base + r"\_dec_c38.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
