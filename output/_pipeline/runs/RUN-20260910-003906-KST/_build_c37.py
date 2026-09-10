# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk37_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Arthritis Kit": (0.55, "관절염 관리 키트(실재)"),
 "Fertility Checker": (0.55, "배략 확인 도구(배란검사 실재)"),
 "Berth App": (0.6, "선석·마리나 예약 앱(실재)"),
 "Escrow Analysis": (0.6, "에스크로 계정 분석(실무 실재)"),
 "Court Template": (0.55, "법원 제출 서식 템플릿(실재)"),
 "Landscaping App": (0.65, "조경 시공 관리 앱(실재 시장)"),
 "Lawsuit Analysis": (0.6, "소송 사건 분석(Analysis 평행)"),
 "Divorce Center": (0.55, "이혼 종합 안내 센터(셀프헬프 실재)"),
 "Mediation Kit": (0.55, "조정 준비 키트(ADR 툴킷 실재)"),
 "Payout App": (0.6, "보험금 지급 관리 앱(실재)"),
 "Probation Tips": (0.55, "수습 기간 관리 팁(App→Tips 평행)"),
 "Rubric Workbook": (0.55, "루브릭 설계 워크북(교사 서식 실재)"),
 "Transmission Analysis": (0.55, "변속기 진단 데이터 분석(OBD 실재)"),
 "Diving Kit": (0.55, "다이빙 장비 키트(Climbing Kit 평행)"),
 "Thyroid Helper": (0.55, "갑상선 약 복용 관리 도우미(복약 알림 실재)"),
 "Adherence App": (0.7, "복약 순응도 관리 앱(실재 시장)"),
 "Berth Tips": (0.55, "선석 예약 팁(App→Tips 평행)"),
 "Lighting App": (0.65, "사진 조명 설계 앱(실재 카테고리)"),
 "Court Guide": (0.55, "법원 이용 가이드(셀프헬프 실재)"),
 "Registrar App": (0.55, "혼인 신고·등기 예약 앱(실재)"),
 "Landscaping Tips": (0.55, "조경 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Technician Advice": "동일 배치 승인된 Technician App/Tips와 동일 기능 의미 중복",
 "Deck Advice": "동일 배치 승인된 Deck App/Tips와 동일 기능 의미 중복",
}
R = {
 "Migraine Signature": "결합 불성립", "Insomnia Levy": "결합 불성립",
 "Skydiving Arrears": "결합 불성립", "Acne Advance": "결합 불성립",
 "Snowboarding Extension": "연장 대상 불분명", "Eczema Trial": "결합 불성립",
 "Ziplining Manual": "설명 대상 불분명(훈련 전통 약함)", "Psoriasis Worksheet": "워크시트 근거 약함",
 "Sledding Layout": "결합 불성립", "Vertigo Sketch": "제품성 불분명",
 "Diving Notification": "알림 내용 불특정", "Arthritis Kit SKIP": "",
 "Sailing Total": "결합 불성립", "Menopause Widget": "결합 불성립",
 "Rafting Calculator": "계산 대상 불분명", "Pregnancy Converter": "변환 대상 불분명",
 "Climbing Estimator": "산출 대상 불분명", "Fertility Checker SKIP": "",
 "Biking Workshop": "결합 불성립(Camping Workshop 기각 선례)",
 "Thyroid Guardian": "감시 대상 불분명", "Golf Result": "결합 불성립",
 "Cholesterol Streak": "결합 불성립", "Fishing Comparison": "비교 대상 불분명",
 "Hypertension Proposal": "제안 대상 불분명", "Camping Copy": "결합 불성립",
 "Anemia Reading": "수치 대상 불분명", "Glamping Deadline": "결합 불성립",
 "Heartburn Duration": "결합 불성립", "Stargazing Progress": "결합 불성립",
 "Constipation Authorization": "결합 불성립", "Birdwatching Rating": "평가 대상 불분명",
 "Concussion Agreement": "결합 불성립", "Canyon Account": "결합 불성립",
 "Sprain Case": "결합 불성립", "Geyser Match": "결합 불성립",
 "Fracture Validation": "결합 불성립", "Fjord Lookup": "탐색 대상 불분명",
 "Insulin Ping": "결합 불성립", "Savanna Model": "결합 불성립",
 "Tundra Availability": "상태 명사로 제품명 부자연", "Prairie Eligibility": "결합 불성립",
 "Marsh Broadcast": "결합 불성립", "Cove Barcode": "결합 불성립",
 "Cliff Appointment": "약속 대상 불분명", "Cavern Feedback": "결합 불성립",
 "Oasis Invoice": "결합 불성립", "Dune Renewal": "갱신 대상 불분명",
 "Whale Quote": "인용·견적 중의로 대상 불분명", "Dolphin Warranty": "결합 불성립",
 "Penguin Deposit": "결합 불성립", "Flamingo Certification": "결합 불성립",
 "Turtle Nomination": "결합 불성립", "Moose Correction": "결합 불성립",
 "Bison Revision": "결합 불성립", "Reindeer Payment": "결합 불성립",
 "Berth App SKIP": "", "Compressor Workbook": "워크북 대상 불분명",
 "Cylinder Mode": "기능 토글로 읽혀 제품 불분명", "Proofing Spec": "사양 참조로 제품 불분명",
 "Unpacking Quantity": "수량 대상 불분명", "Proof Login": "제품 불분명",
 "Invitation Analysis": "분석 대상 불분명", "Eviction Coach": "코칭 대상 불분명",
 "Algae Habit": "결합 불성립", "Favor App": "제품 불분명(favor 다의성)",
 "Occupant Tips": "팁 대상 불분명", "Rinse Workbook": "워크북 대상 불분명",
 "Plunger Mode": "기능 토글로 읽혀 제품 불분명", "Sightseeing Spec": "사양 참조로 제품 불분명",
 "Clarinet Quantity": "수량 대상 불분명", "Consent Login": "제품 불분명",
 "Escrow Analysis SKIP": "", "Statute Coach": "코칭 대상 불분명",
 "Backorder Habit": "결합 불성립", "Lawyer Version": "결합 불성립",
 "Attorney Message": "결합 불성립", "Court Template SKIP": "",
 "Judge Video": "결합 불성립", "Jury Episode": "결합 불성립",
 "Landscaping App SKIP": "", "Opening Tips": "팁 대상 불분명(Opening App 기각 선례)",
 "Bucket Advice": "팁 대상 불분명", "Softener Workbook": "워크북 대상 불분명",
 "Traveler Mode": "기능 토글로 읽혀 제품 불분명", "Mandolin Spec": "사양 참조로 제품 불분명",
 "Vaccine Quantity": "수량 대상 불분명", "Remittance Login": "제품 불분명",
 "Lawsuit Analysis SKIP": "", "Trailer Coach": "코칭 대상 불분명",
 "Contingency Habit": "결합 불성립", "Divorce Center SKIP": "",
 "Custody Booth": "결합 불성립", "Immigration Draft": "결합 불성립",
 "Testament Fee": "결합 불성립", "Notary Format": "결합 불성립",
 "Mediation Kit SKIP": "", "Guardianship Copy": "결합 불성립",
 "Trademark Feedback": "결합 불성립", "Patent Checkin": "결합 불성립",
 "Copyright Humidity": "결합 불성립", "Payout App SKIP": "",
 "Probation Tips SKIP": "", "Rubric Workbook SKIP": "",
 "Referendum Mode": "기능 토글로 읽혀 제품 불분명", "Story Spec": "사양 참조로 제품 불분명",
 "Internship Quantity": "수량 대상 불분명", "Attendance Login": "제품 불분명",
 "Transmission Analysis SKIP": "", "Donut Coach": "코칭 대상 불분명",
 "Euthanasia Habit": "결합 불성립", "Migraine Marker": "표식 대상 불분명",
 "Insomnia Due": "결합 불성립", "Skydiving Advance": "결합 불성립",
 "Acne Penalty": "결합 불성립", "Snowboarding Trial": "결합 불성립",
 "Eczema Graph": "그래프 대상 불분명", "Ziplining Worksheet": "워크시트 근거 약함",
 "Psoriasis Diagram": "도식 대상 불분명", "Sledding Sketch": "제품성 불분명",
 "Vertigo Outline": "개요 대상 불분명", "Diving Kit SKIP": "",
 "Arthritis Count": "카운트 대상 불분명", "Sailing Widget": "결합 불성립",
 "Menopause Repository": "결합 불성립", "Rafting Converter": "변환 대상 불분명",
 "Pregnancy Generator": "생성 대상 불분명", "Climbing Checker": "검사 대상 불분명",
 "Fertility Detector": "탐지 대상 불분명", "Biking Guardian": "감시 대상 불분명",
 "Thyroid Helper SKIP": "", "Golf Streak": "결합 불성립",
 "Cholesterol Rank": "결합 불성립", "Fishing Proposal": "제안 대상 불분명",
 "Hypertension Guarantee": "결합 불성립", "Camping Reading": "결합 불성립",
 "Anemia Reference": "결합 불성립", "Glamping Duration": "결합 불성립",
 "Heartburn Volume": "결합 불성립", "Stargazing Authorization": "결합 불성립",
 "Constipation Template": "결합 불성립", "Birdwatching Agreement": "결합 불성립",
 "Concussion Reply": "결합 불성립", "Canyon Case": "결합 불성립",
 "Sprain Match": "결합 불성립", "Geyser Validation": "결합 불성립",
 "Fracture Lookup": "탐색 대상 불분명", "Fjord Ping": "결합 불성립",
 "Insulin Model": "결합 불성립", "Savanna Availability": "상태 명사로 제품명 부자연",
 "Tundra Eligibility": "결합 불성립", "Prairie Broadcast": "결합 불성립",
 "Marsh Barcode": "결합 불성립", "Cove Appointment": "약속 대상 불분명",
 "Cliff Feedback": "결합 불성립", "Cavern Invoice": "결합 불성립",
 "Oasis Renewal": "갱신 대상 불분명", "Dune Quote": "인용·견적 중의로 대상 불분명",
 "Whale Warranty": "결합 불성립", "Dolphin Deposit": "결합 불성립",
 "Penguin Certification": "결합 불성립", "Flamingo Nomination": "결합 불성립",
 "Turtle Correction": "결합 불성립", "Moose Revision": "결합 불성립",
 "Bison Payment": "결합 불성립", "Reindeer Verification": "결합 불성립",
 "Adherence App SKIP": "", "Berth Tips SKIP": "",
 "Compressor Mode": "기능 토글로 읽혀 제품 불분명", "Cylinder Spec": "사양 참조로 제품 불분명",
 "Proofing Quantity": "수량 대상 불분명", "Unpacking Login": "제품 불분명",
 "Proof Analysis": "분석 대상 불분명", "Invitation Coach": "코칭 대상 불분명",
 "Eviction Habit": "결합 불성립", "Lighting App SKIP": "",
 "Favor Tips": "대상 불분명(Favor App 기각 선례)", "Occupant Advice": "팁 대상 불분명",
 "Technician Workbook": "워크북 대상 불분명", "Rinse Mode": "기능 토글로 읽혀 제품 불분명",
 "Plunger Spec": "사양 참조로 제품 불분명", "Sightseeing Quantity": "수량 대상 불분명",
 "Clarinet Login": "제품 불분명", "Consent Analysis": "분석 대상 불분명",
 "Escrow Coach": "코칭 대상 불분명", "Statute Habit": "결합 불성립",
 "Lawyer Link": "결합 불성립", "Attorney Total": "결합 불성립",
 "Court Guide SKIP": "", "Judge Diary": "결합 불성립",
 "Jury Cycle": "결합 불성립", "Registrar App SKIP": "",
 "Landscaping Tips SKIP": "", "Opening Advice": "팁 대상 불분명",
 "Bucket Workbook": "워크북 대상 불분명", "Softener Mode": "기능 토글로 읽혀 제품 불분명",
 "Traveler Spec": "사양 참조로 제품 불분명", "Mandolin Quantity": "수량 대상 불분명",
 "Vaccine Login": "제품 불분명",
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
out = base + r"\_dec_c37.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
