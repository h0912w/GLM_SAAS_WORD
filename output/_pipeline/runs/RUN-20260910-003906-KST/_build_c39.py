# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk39_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Interpreter App": (0.6, "통역 예약·지원 앱(실재)"),
 "Route Tips": (0.55, "경로 계획 팁(App→Tips 평행)"),
 "Reimbursement App": (0.6, "비용 정산·환급 앱(실재 시장)"),
 "License Tips": (0.55, "사진 라이선스 팁(App→Tips 평행)"),
 "Lawsuit Tracker": (0.6, "소송 진행 상태 추적(Tracker 실재)"),
 "Immigration Reminder": (0.55, "비자·체류 기한 알림(실재)"),
 "Testament Plan": (0.55, "유언장·상속 계획(estate planning 실재)"),
 "Notary Signature": (0.55, "온라인 공증 서명(실재)"),
 "Inheritance App": (0.65, "상속 정산 관리 앱(실재 시장)"),
 "Vertigo Kit": (0.55, "어지럼증 자가 재활 키트(Epley 실재)"),
 "Pregnancy Checker": (0.55, "임신 검사 확인 도구(실재)"),
 "Delivery App": (0.65, "세탁 수거·배달 앱(실재 시장)"),
 "Padlock App": (0.6, "스마트 자물쇠 제어 앱(실재)"),
 "Interpreter Tips": (0.55, "통역 이용 팁(App→Tips 평행)"),
 "Vocabulary App": (0.65, "어휘 학습 앱(실재 시장)"),
 "Reimbursement Tips": (0.55, "정산 처리 팁(App→Tips 평행)"),
 "Hospital App": (0.6, "병원 환자 포털 앱(실재)"),
 "Inheritance Tips": (0.55, "상속 절차 팁(App→Tips 평행)"),
 "Sledding Kit": (0.55, "썰매 장비 키트(Climbing Kit 평행)"),
 "Fertility Helper": (0.55, "배략 주기 도우미(Calculator/Recorder 평행)"),
}
R_DUP = {
 "Lighting Advice": "동일 배치 승인된 Lighting App/Tips와 동일 기능 의미 중복",
 "Registrar Advice": "동일 배치 승인된 Registrar App/Tips와 동일 기능 의미 중복",
 "Comparable Advice": "동일 배치 승인된 Comparable App/Tips와 동일 기능 의미 중복",
 "Retail Advice": "동일 배치 승인된 Retail App/Tips와 동일 기능 의미 중복",
 "Route Advice": "동일 배치 승인된 Route App/Tips와 동일 기능 의미 중복",
 "License Advice": "동일 배치 승인된 License App/Tips와 동일 기능 의미 중복",
}
R = {
 "Favor Workbook": "워크북 대상 불분명", "Occupant Mode": "기능 토글로 읽혀 제품 불분명",
 "Technician Spec": "사양 참조로 제품 불분명", "Rinse Quantity": "수량 대상 불분명",
 "Plunger Login": "제품 불분명", "Sightseeing Analysis": "분석 대상 불분명",
 "Clarinet Coach": "코칭 대상 불분명", "Consent Habit": "결합 불성립",
 "Lawyer Detail": "결합 불성립", "Attorney Repository": "결합 불성립",
 "Court Agreement": "결합 불성립", "Judge Expense": "결합 불성립",
 "Jury Sensor": "결합 불성립", "Landscaping Workbook": "워크북 대상 불분명",
 "Opening Mode": "기능 토글로 읽혀 제품 불분명", "Bucket Spec": "사양 참조로 제품 불분명",
 "Softener Quantity": "수량 대상 불분명", "Traveler Login": "제품 불분명",
 "Mandolin Analysis": "분석 대상 불분명", "Vaccine Coach": "코칭 대상 불분명",
 "Remittance Habit": "결합 불성립", "Divorce Console": "결합 불성립",
 "Custody Post": "결합 불성립", "Mediation Total": "결합 불성립",
 "Guardianship Forecast": "결합 불성립", "Trademark Quote": "인용·견적 중의로 대상 불분명",
 "Patent Weight": "결합 불성립", "Copyright Breakdown": "결합 불성립",
 "Bulk Tips": "팁 대상 불분명(Bulk App 기각 선례)", "Payout Workbook": "워크북 대상 불분명",
 "Probation Mode": "기능 토글로 읽혀 제품 불분명", "Deck Spec": "사양 참조로 제품 불분명",
 "Rubric Quantity": "수량 대상 불분명", "Referendum Login": "제품 불분명",
 "Story Analysis": "분석 대상 불분명", "Internship Coach": "코칭 대상 불분명",
 "Attendance Habit": "결합 불성립", "Migraine Asset": "결합 불성립",
 "Insomnia Arrears": "결합 불성립", "Skydiving Redemption": "결합 불성립",
 "Acne Extension": "연장 대상 불분명", "Snowboarding Manual": "설명 대상 불분명(Ziplining Manual 기각 선례)",
 "Eczema Worksheet": "워크시트 근거 약함", "Ziplining Layout": "결합 불성립",
 "Psoriasis Sketch": "제품성 불분명", "Sledding Notification": "알림 내용 불특정",
 "Diving Total": "결합 불성립", "Arthritis Widget": "결합 불성립",
 "Sailing Calculator": "계산 대상 불분명(Rafting Calculator 기각 선례)",
 "Menopause Converter": "변환 대상 불분명", "Rafting Estimator": "산출 대상 불분명",
 "Climbing Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Fertility Guardian": "감시 대상 불분명",
 "Biking Result": "결합 불성립", "Thyroid Streak": "결합 불성립",
 "Golf Comparison": "비교 대상 불분명", "Cholesterol Proposal": "제안 대상 불분명",
 "Fishing Copy": "결합 불성립", "Hypertension Reading": "수치 대상 불분명(Anemia Reading 기각 선례)",
 "Camping Deadline": "결합 불성립", "Anemia Duration": "결합 불성립",
 "Glamping Progress": "진행 대상 불분명", "Heartburn Authorization": "결합 불성립",
 "Stargazing Rating": "평가 대상 불분명", "Constipation Agreement": "결합 불성립",
 "Birdwatching Case": "결합 불성립", "Concussion Match": "결합 불성립",
 "Canyon Lookup": "탐색 대상 불분명", "Sprain Ping": "결합 불성립",
 "Geyser Model": "결합 불성립", "Fracture Availability": "상태 명사로 제품명 부자연",
 "Fjord Eligibility": "결합 불성립", "Insulin Broadcast": "결합 불성립",
 "Savanna Barcode": "결합 불성립", "Tundra Appointment": "약속 대상 불분명",
 "Prairie Feedback": "결합 불성립", "Marsh Invoice": "결합 불성립",
 "Cove Renewal": "갱신 대상 불분명", "Cliff Quote": "인용·견적 중의로 대상 불분명",
 "Cavern Warranty": "결합 불성립", "Oasis Deposit": "결합 불성립",
 "Dune Certification": "결합 불성립", "Whale Nomination": "결합 불성립",
 "Dolphin Correction": "결합 불성립", "Penguin Revision": "결합 불성립",
 "Flamingo Payment": "결합 불성립", "Turtle Verification": "결합 불성립",
 "Moose Simulator": "결합 불성립", "Bison Predictor": "예측 대상 불분명",
 "Reindeer Seal": "결합 불성립", "Service Tips": "팁 대상 불분명(Service App 기각 선례)",
 "Adherence Workbook": "워크북 대상 불분명", "Berth Mode": "기능 토글로 읽혀 제품 불분명",
 "Compressor Login": "제품 불분명", "Cylinder Analysis": "분석 대상 불분명",
 "Proofing Coach": "코칭 대상 불분명", "Unpacking Habit": "결합 불성립",
 "Interpreter App SKIP": "", "Lighting Workbook": "워크북 대상 불분명",
 "Favor Mode": "기능 토글로 읽혀 제품 불분명", "Occupant Spec": "사양 참조로 제품 불분명",
 "Technician Quantity": "수량 대상 불분명", "Rinse Login": "제품 불분명",
 "Plunger Analysis": "분석 대상 불분명", "Sightseeing Coach": "코칭 대상 불분명",
 "Clarinet Habit": "결합 불성립", "Lawyer Identifier": "결합 불성립",
 "Attorney Announcement": "결합 불성립", "Court Reply": "결합 불성립",
 "Judge Newsletter": "결합 불성립", "Jury Reception": "결합 불성립",
 "Vocabulary App SKIP": "", "Registrar Workbook": "워크북 대상 불분명",
 "Landscaping Mode": "기능 토글로 읽혀 제품 불분명", "Opening Spec": "사양 참조로 제품 불분명",
 "Bucket Quantity": "수량 대상 불분명", "Softener Login": "제품 불분명",
 "Traveler Analysis": "분석 대상 불분명", "Mandolin Coach": "코칭 대상 불분명",
 "Vaccine Habit": "결합 불성립", "Lawsuit Flow": "결합 불성립",
 "Divorce Panel": "결합 불성립", "Custody Harbor": "결합 불성립",
 "Immigration Index": "결합 불성립", "Testament Cost": "결합 불성립",
 "Notary Marker": "표식 대상 불분명", "Mediation Widget": "결합 불성립",
 "Guardianship Deadline": "결합 불성립", "Trademark Warranty": "결합 불성립",
 "Patent Distance": "결합 불성립", "Copyright Sensor": "결합 불성립",
 "Hospital App SKIP": "", "Bulk Advice": "팁 대상 불분명",
 "Comparable Workbook": "워크북 대상 불분명", "Payout Mode": "기능 토글로 읽혀 제품 불분명",
 "Probation Spec": "사양 참조로 제품 불분명", "Deck Quantity": "수량 대상 불분명",
 "Rubric Login": "제품 불분명", "Referendum Analysis": "분석 대상 불분명",
 "Story Coach": "코칭 대상 불분명", "Internship Habit": "결합 불성립",
 "Migraine Levy": "결합 불성립", "Insomnia Advance": "결합 불성립",
 "Skydiving Extension": "연장 대상 불분명", "Acne Trial": "결합 불성립",
 "Snowboarding Worksheet": "워크시트 근거 약함", "Eczema Diagram": "도식 대상 불분명",
 "Ziplining Sketch": "제품성 불분명", "Psoriasis Outline": "개요 대상 불분명",
 "Vertigo Count": "카운트 대상 불분명", "Diving Widget": "결합 불성립",
 "Arthritis Repository": "결합 불성립", "Sailing Converter": "변환 대상 불분명",
 "Menopause Generator": "생성 대상 불분명", "Rafting Checker": "검사 대상 불분명",
 "Pregnancy Detector": "탐지 대상 불분명", "Climbing Guardian": "감시 대상 불분명",
 "Biking Streak": "결합 불성립", "Thyroid Rank": "결합 불성립",
 "Golf Proposal": "제안 대상 불분명", "Cholesterol Guarantee": "결합 불성립",
 "Fishing Reading": "결합 불성립", "Hypertension Reference": "결합 불성립",
 "Camping Duration": "결합 불성립", "Anemia Volume": "결합 불성립",
 "Glamping Authorization": "결합 불성립", "Heartburn Template": "결합 불성립",
 "Stargazing Agreement": "결합 불성립", "Constipation Reply": "결합 불성립",
 "Birdwatching Match": "결합 불성립", "Concussion Validation": "결합 불성립",
 "Canyon Ping": "결합 불성립", "Sprain Model": "결합 불성립",
 "Geyser Availability": "상태 명사로 제품명 부자연", "Fracture Eligibility": "결합 불성립",
 "Fjord Broadcast": "결합 불성립", "Insulin Barcode": "결합 불성립",
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
out = base + r"\_dec_c39.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
