# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk40_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Delivery Tips": (0.55, "세탁 배달 이용 팁(App→Tips 평행)"),
 "Padlock Tips": (0.55, "스마트 자물쇠 사용 팁(App→Tips 평행)"),
 "Vocabulary Tips": (0.55, "어휘 학습 팁(App→Tips 평행)"),
 "Repertoire App": (0.6, "연주 레퍼토리 관리 앱(실재)"),
 "Hospital Tips": (0.55, "병원 이용 팁(App→Tips 평행)"),
 "Menopause Recorder": (0.55, "폐경 증상 기록(실재 트래커)"),
 "Thyroid Trend": (0.55, "갑상선 수치 추이(Hypertension Trend 평행)"),
 "Cholesterol Record": (0.55, "혈지 검사 기록(Hypertension Record 평행)"),
 "Heartburn Guide": (0.55, "속쓰림 관리 가이드(Constipation Guide 평행)"),
 "Irrigation App": (0.7, "관개 제어 앱(스마트 관수 실재 시장)"),
 "Humidifier App": (0.65, "가습기 제어 앱(스마트 가습기 실재)"),
 "Skiing App": (0.65, "스키 트래킹 앱(실재 시장)"),
 "Repertoire Tips": (0.55, "레퍼토리 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Interpreter Advice": "동일 배치 승인된 Interpreter App/Tips와 동일 기능 의미 중복",
 "Reimbursement Advice": "동일 배치 승인된 Reimbursement App/Tips와 동일 기능 의미 중복",
 "Inheritance Advice": "동일 배치 승인된 Inheritance App/Tips와 동일 기능 의미 중복",
 "Delivery Advice": "동일 배치 승인된 Delivery App/Tips와 동일 기능 의미 중복",
 "Padlock Advice": "동일 배치 승인된 Padlock App/Tips와 동일 기능 의미 중복",
 "Vocabulary Advice": "동일 배치 승인된 Vocabulary App/Tips와 동일 기능 의미 중복",
 "Hospital Advice": "동일 배치 승인된 Hospital App/Tips와 동일 기능 의미 중복",
}
R = {
 "Savanna Appointment": "약속 대상 불분명", "Tundra Feedback": "결합 불성립",
 "Prairie Invoice": "결합 불성립", "Marsh Renewal": "갱신 대상 불분명",
 "Cove Quote": "인용·견적 중의로 대상 불분명", "Cliff Warranty": "결합 불성립",
 "Cavern Deposit": "결합 불성립", "Oasis Certification": "결합 불성립",
 "Dune Nomination": "결합 불성립", "Whale Correction": "결합 불성립",
 "Dolphin Revision": "결합 불성립", "Penguin Payment": "결합 불성립",
 "Flamingo Verification": "결합 불성립", "Turtle Simulator": "결합 불성립",
 "Moose Predictor": "예측 대상 불분명", "Bison Seal": "결합 불성립",
 "Reindeer Review": "결합 불성립", "Supply App": "제품 불분명",
 "Service Advice": "팁 대상 불분명(Service App 기각 선례)", "Retail Workbook": "워크북 대상 불분명",
 "Adherence Mode": "기능 토글로 읽혀 제품 불분명", "Berth Spec": "사양 참조로 제품 불분명",
 "Compressor Analysis": "분석 대상 불분명", "Cylinder Coach": "코칭 대상 불분명",
 "Proofing Habit": "결합 불성립", "Blower App": "제품 불분명(블로어 단독 카테고리 약함)",
 "Route Workbook": "워크북 대상 불분명", "Lighting Mode": "기능 토글로 읽혀 제품 불분명",
 "Favor Spec": "사양 참조로 제품 불분명", "Occupant Quantity": "수량 대상 불분명",
 "Technician Login": "제품 불분명", "Rinse Analysis": "분석 대상 불분명",
 "Plunger Coach": "코칭 대상 불분명", "Sightseeing Habit": "결합 불성립",
 "Lawyer Category": "결합 불성립", "Attorney Calculator": "계산 대상 불분명",
 "Court Account": "결합 불성립", "Judge Inventory": "결합 불성립",
 "Jury Followup": "결합 불성립", "Combination App": "제품 불분명(결합형 잠금 장치로 읽기 어려움)",
 "License Workbook": "워크북 대상 불분명", "Registrar Mode": "기능 토글로 읽혀 제품 불분명",
 "Landscaping Spec": "사양 참조로 제품 불분명", "Opening Quantity": "수량 대상 불분명",
 "Bucket Login": "제품 불분명", "Softener Analysis": "분석 대상 불분명",
 "Traveler Coach": "코칭 대상 불분명", "Mandolin Habit": "결합 불성립",
 "Lawsuit Hub": "결합 불성립", "Divorce Scale": "결합 불성립",
 "Custody Roster": "결합 불성립", "Immigration Ticket": "결합 불성립",
 "Testament Price": "결합 불성립", "Notary Balance": "결합 불성립",
 "Mediation Repository": "결합 불성립", "Guardianship Duration": "결합 불성립",
 "Trademark Deposit": "결합 불성립", "Patent Range": "결합 불성립",
 "Copyright Reception": "결합 불성립", "Hospital App SKIP": "",
 "Bulk Workbook": "워크북 대상 불분명", "Comparable Mode": "기능 토글로 읽혀 제품 불분명",
 "Payout Spec": "사양 참조로 제품 불분명", "Probation Quantity": "수량 대상 불분명",
 "Deck Login": "제품 불분명", "Rubric Analysis": "분석 대상 불분명",
 "Referendum Coach": "코칭 대상 불분명", "Story Habit": "결합 불성립",
 "Migraine Due": "결합 불성립", "Insomnia Penalty": "결합 불성립",
 "Skydiving Trial": "결합 불성립", "Acne Graph": "그래프 대상 불분명",
 "Snowboarding Diagram": "도식 대상 불분명", "Eczema Schematic": "도식 대상 불분명",
 "Ziplining Outline": "개요 대상 불분명", "Psoriasis Rendering": "결합 불성립",
 "Sledding Count": "카운트 대상 불분명", "Vertigo Message": "메시지 대상 불분명",
 "Diving Repository": "결합 불성립", "Arthritis Announcement": "결합 불성립",
 "Sailing Generator": "생성 대상 불분명", "Rafting Detector": "탐지 대상 불분명",
 "Pregnancy Timer": "결합 불성립(Timer 계열 기각 선례)", "Climbing Helper": "도우미 대상 불분명(Biking Helper 기각 선례)",
 "Fertility Stage": "단계 대상 불분명", "Biking Rank": "결합 불성립",
 "Golf Guarantee": "결합 불성립", "Fishing Reference": "결합 불성립",
 "Hypertension Forecast": "결합 불성립", "Camping Volume": "결합 불성립",
 "Anemia Diagnostic": "진단 대상 불분명", "Glamping Template": "결합 불성립",
 "Stargazing Reply": "결합 불성립", "Constipation Account": "결합 불성립",
 "Birdwatching Validation": "결합 불성립", "Concussion Lookup": "탐색 대상 불분명",
 "Canyon Model": "결합 불성립", "Sprain Availability": "상태 명사로 제품명 부자연",
 "Geyser Eligibility": "결합 불성립", "Fracture Broadcast": "결합 불성립",
 "Fjord Barcode": "결합 불성립", "Insulin Appointment": "결합 불성립",
 "Savanna Feedback": "결합 불성립", "Tundra Invoice": "결합 불성립",
 "Prairie Renewal": "갱신 대상 불분명", "Marsh Quote": "인용·견적 중의로 대상 불분명",
 "Cove Warranty": "결합 불성립", "Cliff Deposit": "결합 불성립",
 "Cavern Certification": "결합 불성립", "Oasis Nomination": "결합 불성립",
 "Dune Correction": "결합 불성립", "Whale Revision": "결합 불성립",
 "Dolphin Payment": "결합 불성립", "Penguin Verification": "결합 불성립",
 "Flamingo Simulator": "결합 불성립", "Turtle Predictor": "예측 대상 불분명",
 "Moose Seal": "결합 불성립", "Bison Review": "결합 불성립",
 "Reindeer Recipe": "결합 불성립", "Irrigation App SKIP": "",
 "Supply Tips": "팁 대상 불분명(Supply App 기각 선례)", "Service Workbook": "워크북 대상 불분명",
 "Retail Mode": "기능 토글로 읽혀 제품 불분명", "Adherence Spec": "사양 참조로 제품 불분명",
 "Berth Quantity": "수량 대상 불분명", "Compressor Coach": "코칭 대상 불분명",
 "Cylinder Habit": "결합 불성립", "Reserve App": "제품 불분명(광물 매장량·예약 중의)",
 "Blower Tips": "팁 대상 불분명(Blower App 기각 선례)", "Interpreter Workbook": "워크북 대상 불분명",
 "Route Mode": "기능 토글로 읽혀 제품 불분명", "Lighting Spec": "사양 참조로 제품 불분명",
 "Favor Quantity": "수량 대상 불분명", "Occupant Login": "제품 불분명",
 "Technician Analysis": "분석 대상 불분명", "Rinse Coach": "코칭 대상 불분명",
 "Plunger Habit": "결합 불성립", "Lawyer Attribute": "결합 불성립",
 "Attorney Converter": "변환 대상 불분명", "Court Case": "결합 불성립(Case 계열 기각 선례)",
 "Judge Claim": "결합 불성립", "Jury Approval": "결합 불성립",
 "Humidifier App SKIP": "", "Combination Tips": "팁 대상 불분명(Combination App 기각 선례)",
 "Reimbursement Workbook": "워크북 대상 불분명", "License Mode": "기능 토글로 읽혀 제품 불분명",
 "Registrar Spec": "사양 참조로 제품 불분명", "Landscaping Quantity": "수량 대상 불분명",
 "Opening Login": "제품 불분명", "Bucket Analysis": "분석 대상 불분명",
 "Softener Coach": "코칭 대상 불분명", "Traveler Habit": "결합 불성립",
 "Lawsuit Desk": "결합 불성립", "Divorce Route": "결합 불성립",
 "Custody Alert": "결합 불성립", "Immigration Estimate": "산출 대상 불분명",
 "Testament Fare": "결합 불성립", "Notary Interest": "결합 불성립",
 "Mediation Announcement": "결합 불성립", "Guardianship Volume": "결합 불성립",
 "Trademark Certification": "결합 불성립", "Patent Limit": "결합 불성립",
 "Copyright Followup": "결합 불성립", "Skiing App SKIP": "",
 "Inheritance Workbook": "워크북 대상 불분명", "Bulk Mode": "기능 토글로 읽혀 제품 불분명",
 "Comparable Spec": "사양 참조로 제품 불분명", "Payout Quantity": "수량 대상 불분명",
 "Probation Login": "제품 불분명", "Deck Analysis": "분석 대상 불분명",
 "Rubric Coach": "코칭 대상 불분명", "Referendum Habit": "결합 불성립",
 "Migraine Subsidy": "결합 불성립", "Insomnia Markup": "마크업 대상 불분명",
 "Skydiving Graph": "그래프 대상 불분명", "Acne Label": "결합 불성립",
 "Snowboarding Schematic": "도식 대상 불분명", "Eczema Layout": "결합 불성립",
 "Ziplining Rendering": "결합 불성립", "Psoriasis Notification": "알림 내용 불특정",
 "Sledding Message": "결합 불성립", "Vertigo Total": "결합 불성립",
 "Diving Announcement": "결합 불성립", "Arthritis Calculator": "계산 대상 불분명",
}
for k in [k for k in R if k.endswith(" SKIP")]:
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
out = base + r"\_dec_c40.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
