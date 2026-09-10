# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk8_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Commission App": (0.55, "직원 커미션 관리 앱(살롱 실재)"),
 "Dispensing Tips": (0.55, "조제 운영 팁(App→Tips 평행)"),
 "Mileage App": (0.6, "마일리지 기록 앱(실재 카테고리)"),
 "Editing Tips": (0.55, "사진 편집 팁(App→Tips 평행)"),
 "Hostel Login": (0.55, "호스텔 예약 포털 로그인"),
 "Lawyer Reminder": (0.55, "기한 알림(Reminder 축)"),
 "Headhunter App": (0.6, "헤드헌팅 앱(실재 카테고리)"),
 "Swag Tips": (0.55, "이벤트 기념품 팁(App→Tips 평행)"),
 "Sidewalk App": (0.55, "보도 정비 관리 앱(시설 관리 실재)"),
 "Snorkeling Tips": (0.55, "스노클링 팁(App→Tips 평행)"),
 "Workout Workbook": (0.55, "운동 프로그램 워크북(fitness workbook 실재)"),
 "Geyser Diagram": (0.55, "간헐천 지형 다이어그램(지리 교육 축)"),
 "Cemetery App": (0.6, "묘지·추모 관리 앱(실재)"),
 "Commission Tips": (0.55, "커미션 정산 팁(App→Tips 평행)"),
 "Bilingual App": (0.6, "이중언어 학습 앱(실재 카테고리)"),
 "Mileage Tips": (0.55, "마일리지 활용 팁(App→Tips 평행)"),
 "Priority App": (0.6, "문의 우선순위 관리 앱(실재)"),
 "Headhunter Tips": (0.55, "헤드헌팅 팁(App→Tips 평행)"),
 "Nanny App": (0.6, "보모 매칭 앱(실재 카테고리)"),
 "Sidewalk Tips": (0.55, "보도 관리 팁(App→Tips 평행)"),
 "Psoriasis Plan": (0.55, "건선 관리 계획(건강 관리 플랜 축)"),
}
R_DUP = {
 "Charter Advice": "동일 배치 승인된 Charter Tips와 동일 기능 의미 중복",
 "Toast Advice": "동일 배치 승인된 Toast Tips와 동일 기능 의미 중복",
 "Metronome Advice": "동일 배치 승인된 Metronome Tips와 동일 기능 의미 중복",
 "Dispensing Advice": "동일 배치 승인된 Dispensing Tips와 동일 기능 의미 중복",
 "Editing Advice": "동일 배치 승인된 Editing Tips와 동일 기능 의미 중복",
 "Swag Advice": "동일 배치 승인된 Swag Tips와 동일 기능 의미 중복",
 "Snorkeling Advice": "동일 배치 승인된 Snorkeling Tips와 동일 기능 의미 중복",
}
R = {
 "Prairie Rendering": "렌더링 대상 불분명", "Marsh Notification": "결합 불성립",
 "Cove Kit": "키트 대상 불분명", "Cliff Count": "대상 불분명",
 "Cavern Message": "결합 불성립", "Oasis Total": "결합 불성립",
 "Dune Widget": "위젯 대상 불분명", "Whale Repository": "결합 불성립",
 "Dolphin Announcement": "결합 불성립", "Penguin Calculator": "계산 대상 불분명",
 "Flamingo Converter": "변환 대상 불분명", "Turtle Generator": "생성 대상 불분명",
 "Moose Recorder": "기록 대상 불분명", "Bison Estimator": "산출 대상 불분명",
 "Reindeer Checker": "검사 대상 불분명", "Fuel Workbook": "워크북 대상 불분명",
 "Shift Mode": "기능 토글로 읽혀 제품 불분명", "Filtration Spec": "결합 불성립",
 "Masterkey Quantity": "수량 대상 불분명", "Terminology Login": "결합 불성립",
 "Gallery Coach": "코칭 대상 불분명", "Florist Habit": "결합 불성립",
 "Deposit Workbook": "워크북 대상 불분명", "Turbidity Mode": "기능 토글로 읽혀 제품 불분명",
 "Foam Spec": "결합 불성립", "Washer Quantity": "수량 대상 불분명",
 "Bass Analysis": "분석 대상 불분명", "Triage Coach": "코칭 대상 불분명",
 "Dividend Habit": "결합 불성립", "Attorney Fund": "결합 불성립",
 "Court Markup": "결합 불성립", "Judge Result": "판사 대상 서비스 불성립",
 "Jury Appointment": "서비스 대상 불분명", "Lawsuit Clock": "결합 불성립",
 "Divorce Guarantor": "결합 불성립", "Screening Advice": "대상 불분명(Screening 계열)",
 "Diner Workbook": "워크북 대상 불분명", "Tick Mode": "기능 토글로 읽혀 제품 불분명",
 "Molar Spec": "결합 불성립(Molar 계열)", "Toy Quantity": "수량 대상 불분명",
 "Product Login": "일반 명사로 대상 불분명", "Injection Analysis": "분석 대상 불분명",
 "Igniter Coach": "코칭 대상 불분명", "Rim Habit": "결합 불성립(Rim 계열)",
 "Custody Signal": "신호 대상 불분명", "Immigration Keeper": "관리 대상 불분명",
 "Testament Window": "결합 불성립", "Notary List": "목록 대상 불분명(List 축 기각)",
 "Mediation Sum": "결합 불성립", "Guardianship Balance": "결합 불성립",
 "Trademark Message": "결합 불성립", "Patent Copy": "결합 불성립",
 "Copyright Barcode": "결합 불성립", "Payee Mode": "기능 토글로 읽혀 제품 불분명",
 "Tanker Spec": "결합 불성립", "Deed Quantity": "수량 대상 불분명",
 "Policyholder Login": "결합 불성립", "Countertop Analysis": "분석 대상 불분명",
 "Cocktail Coach": "코칭 대상 불분명", "Toothpaste Habit": "결합 불성립",
 "Migraine Slot": "결합 불성립", "Insomnia Statement": "결합 불성립",
 "Skydiving Bulletin": "결합 불성립", "Acne Brief": "결합 불성립",
 "Snowboarding Confirmation": "확인 대상 불분명", "Eczema Recap": "결합 불성립",
 "Ziplining Item": "항목 대상 불분명", "Psoriasis Unit": "결합 불성립",
 "Sledding Price": "가격 지칭 부자연", "Vertigo Fare": "결합 불성립",
 "Diving Sum": "결합 불성립", "Arthritis Debt": "결합 불성립",
 "Sailing Sale": "결합 불성립", "Menopause Charge": "결합 불성립",
 "Rafting Tariff": "결합 불성립", "Pregnancy Value": "결합 불성립",
 "Climbing Fine": "결합 불성립", "Fertility Number": "수치 지칭 부자연",
 "Biking Rule": "결합 불성립", "Thyroid Detail": "결합 불성립",
 "Golf Attribute": "결합 불성립", "Cholesterol Field": "결합 불성립",
 "Fishing Token": "결합 불성립", "Hypertension Signature": "결합 불성립",
 "Camping Interest": "결합 불성립", "Anemia Asset": "결합 불성립",
 "Glamping Subsidy": "결합 불성립", "Heartburn Discount": "결합 불성립",
 "Stargazing Penalty": "결합 불성립", "Constipation Markup": "결합 불성립",
 "Birdwatching Trial": "결합 불성립", "Concussion Graph": "그래프 대상 불분명",
 "Canyon Manual": "설명 대상 불분명", "Sprain Worksheet": "학습지 근거 약함",
 "Fracture Schematic": "회로도 어휘 부자연", "Fjord Layout": "결합 불성립",
 "Insulin Sketch": "제품성 불분명", "Savanna Outline": "지형은 공예 오트라인 대상 아님",
 "Tundra Rendering": "렌더링 대상 불분명", "Prairie Notification": "결합 불성립",
 "Marsh Kit": "키트 대상 불분명", "Cove Count": "대상 불분명",
 "Cliff Message": "결합 불성립", "Cavern Total": "결합 불성립",
 "Oasis Widget": "위젯 대상 불분명", "Dune Repository": "결합 불성립",
 "Whale Announcement": "결합 불성립", "Dolphin Calculator": "계산 대상 불분명",
 "Penguin Converter": "변환 대상 불분명", "Flamingo Generator": "생성 대상 불분명",
 "Turtle Recorder": "기록 대상 불분명", "Moose Estimator": "산출 대상 불분명",
 "Bison Checker": "검사 대상 불분명", "Reindeer Detector": "탐지 대상 불분명",
 "Charter Workbook": "워크북 대상 불분명", "Fuel Mode": "기능 토글로 읽혀 제품 불분명",
 "Shift Spec": "결합 불성립", "Filtration Quantity": "수량 대상 불분명",
 "Masterkey Login": "결합 불성립", "Terminology Analysis": "분석 대상 불분명",
 "Gallery Habit": "결합 불성립", "Toast Workbook": "워크북 대상 불분명",
 "Deposit Mode": "기능 토글로 읽혀 제품 불분명", "Turbidity Spec": "결합 불성립",
 "Foam Quantity": "수량 대상 불분명", "Washer Login": "결합 불성립",
 "Hostel Analysis": "분석 대상 불분명", "Bass Coach": "코칭 대상 불분명",
 "Triage Habit": "결합 불성립", "Lawyer Index": "색인 대상 불분명",
 "Attorney Cash": "결합 불성립", "Court Redemption": "결합 불성립",
 "Judge Streak": "결합 불성립", "Jury Feedback": "서비스 대상 불분명",
 "Lawsuit Time": "결합 불성립", "Divorce Tuner": "결합 불성립",
 "Screening Workbook": "대상 불분명(Screening 계열)", "Diner Mode": "기능 토글로 읽혀 제품 불분명",
 "Tick Spec": "결합 불성립", "Molar Quantity": "수량 대상 불분명",
 "Toy Login": "결합 불성립", "Product Analysis": "분석 대상 불분명",
 "Injection Coach": "코칭 대상 불분명", "Igniter Habit": "결합 불성립",
 "Custody Watch": "감시 대상 불분명", "Immigration Manager": "관리 대상 불분명",
 "Testament Roll": "결합 불성립", "Notary Table": "결합 불성립(Table 축 기각)",
 "Mediation Debt": "결합 불성립", "Guardianship Interest": "결합 불성립",
 "Trademark Total": "결합 불성립", "Patent Reading": "결합 불성립",
 "Copyright Appointment": "결합 불성립", "Metronome Workbook": "워크북 대상 불분명",
 "Workout Mode": "기능 토글로 읽혀 제품 불분명", "Payee Spec": "결합 불성립",
 "Tanker Quantity": "수량 대상 불분명", "Deed Login": "결합 불성립",
 "Policyholder Analysis": "분석 대상 불분명", "Countertop Coach": "코칭 대상 불분명",
 "Cocktail Habit": "결합 불성립", "Migraine Pass": "결합 불성립",
 "Insomnia Memo": "결합 불성립", "Skydiving Brief": "결합 불성립",
 "Acne Circular": "결합 불성립", "Snowboarding Recap": "결합 불성립",
 "Eczema Entry": "등록 대상 불분명", "Ziplining Unit": "결합 불성립",
 "Sledding Fare": "결합 불성립", "Vertigo Tax": "결합 불성립",
 "Diving Debt": "결합 불성립", "Arthritis Fund": "결합 불성립",
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
out = base + r"\_dec_c8.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
