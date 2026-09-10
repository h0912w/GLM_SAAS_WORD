# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk3_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Homework Habit": (0.55, "숙제·학습 습관 트래킹(study habit 실검색)"),
 "Lawyer History": (0.55, "사건 이력 조회(Lawyer Status 평행)"),
 "Notary Timeline": (0.55, "공증 진행 타임라인(Migraine Timeline 평행)"),
 "Mediation Fee": (0.55, "조정 절차 비용 안내(법률 비용 실검색)"),
 "Copyright Case": (0.55, "저작권 사건 검색·추적"),
 "Cocktail App": (0.6, "칵테일 레시피 앱(실재 카테고리)"),
 "Toothpaste Tips": (0.55, "치약 선택 팁(App→Tips 평행)"),
 "Copay Analysis": (0.55, "본인부담금 분석(Deductible Analysis 평행)"),
 "Skydiving Slot": (0.55, "점프 예약 슬롯(실제 관용구, Snowboarding Slot 평행)"),
 "Diving Fee": (0.55, "다이빙 참가 비용(Sailing Fee 평행)"),
 "Sailing Cost": (0.55, "요트 비용 정보(Rafting Cost 평행)"),
 "Cliff Diagram": (0.55, "절벽 지형 다이어그램(지리 교육, Dune/Cavern 평행)"),
 "Whale Outline": (0.55, "고래 공예 오트라인 인쇄물(대표 공예 검색어)"),
 "Storage App": (0.55, "창고 보관 예약 앱(실재 카테고리)"),
 "Gallery Tips": (0.55, "사진 전시·판매 팁(App→Tips 평행)"),
 "Vacation Login": (0.55, "여행 예약 포털 로그인(Safari Login 평행)"),
 "Prescription Coach": (0.55, "복약 코칭(Dosage Coach 평행)"),
 "Bass App": (0.55, "베이스 레슨 앱(music_lessons 업계 명확)"),
 "Triage Tips": (0.55, "응급 분류 요령 팁(App→Tips 평행)"),
 "Paralegal Workbook": (0.55, "법률보조 업무 워크북(Courier Workbook 평행)"),
 "Scaffold Analysis": (0.55, "공사 현장 데이터 분석(Welding Analysis 평행)"),
 "Lawyer File": (0.55, "사건 파일 관리(case file 실재)"),
 "Attorney Plan": (0.55, "변호 전략 계획"),
 "Immigration Route": (0.55, "이민 경로 안내(immigration route 실검색)"),
 "Notary Reminder": (0.55, "공증 기한 알림(Patent Timer 평행)"),
 "Patent Result": (0.55, "특허 심사 결과 조회"),
 "Copyright Match": (0.55, "저작권 유사성 매칭 검사"),
 "Countertop App": (0.55, "카운터톱 견적·시공 앱(실재 카테고리)"),
 "Cocktail Tips": (0.55, "칵테일 레시피 팁(App→Tips 평행)"),
 "Idiom Workbook": (0.55, "관용구 학습 워크북(ESL 교재 실재)"),
 "Insolvency Analysis": (0.55, "도산·부실 재무 분석(B2B 실재)"),
 "Skydiving Pass": (0.55, "점프 패스(Snowboarding Pass 평행)"),
 "Cove Diagram": (0.55, "만 지형 다이어그램(지리 교육 축)"),
}
R_DUP = {
 "Idiom Advice": "동일 배치 승인된 Idiom Tips와 동일 기능 의미 중복",
 "Formula Advice": "동일 배치 승인된 Formula Tips와 동일 기능 의미 중복",
 "Florist Advice": "동일 배치 승인된 Florist Tips와 동일 기능 의미 중복",
 "Dividend Advice": "동일 배치 승인된 Dividend Tips와 동일 기능 의미 중복",
 "Toothpaste Advice": "동일 배치 승인된 Toothpaste Tips와 동일 기능 의미 중복",
}
R = {
 "Valet Coach": "코칭 대상 불분명(Valet 계열 기각 선례)",
 "Attorney Unit": "결합 불성립", "Court Interest": "결합 불성립",
 "Judge Recorder": "판사 대상 서비스 불성립", "Jury Match": "결합 불성립",
 "Lawsuit Onboarding": "온보딩 대상 불분명", "Divorce Matrix": "결합 불성립",
 "Igniter App": "부품 단독으로 앱 대상 불분명", "Rim Tips": "대상 불분명(Rim App 기각 선례)",
 "Stairs Workbook": "워크북 대상 불분명(Stairs 계열 기각 선례)",
 "Location Mode": "기능 토글로 읽혀 제품 불분명", "Decor Spec": "결합 불성립",
 "Roof Quantity": "수량 대상 불분명", "Valve Login": "결합 불성립",
 "Microfiber Analysis": "분석 대상 불분명", "Backflow Coach": "코칭 대상 불분명",
 "Safari Habit": "결합 불성립", "Custody Desk": "데스크 대상 불분명",
 "Immigration Scale": "결합 불성립", "Testament Harbor": "결합 불성립",
 "Guardianship Identifier": "결합 불성립", "Trademark Diagram": "결합 불성립",
 "Patent Stage": "결합 불성립",
 "Mailroom Workbook": "워크북 대상 불분명", "Kayaking Mode": "기능 토글로 읽혀 제품 불분명",
 "Songbook Spec": "결합 불성립", "Stretch Quantity": "수량 대상 불분명",
 "Insolvency Login": "포털 서비스 대상 불분명",
 "Masonry Coach": "코칭 대상 불분명(Masonry 계열 약함)",
 "Barista Habit": "결합 불성립(Barista 계열 기각 선례)",
 "Migraine Estimate": "결합 불성립(Insomnia Estimate 기각 선례)",
 "Insomnia List": "결합 불성립(Acne List 기각 선례)",
 "Acne Pass": "결합 불성립(Eczema Pass 기각 선례)",
 "Snowboarding Statement": "결합 불성립", "Eczema Memo": "결합 불성립",
 "Ziplining Bulletin": "결합 불성립", "Psoriasis Brief": "결합 불성립",
 "Sledding Petition": "결합 불성립", "Vertigo Confirmation": "확인 대상 불분명",
 "Arthritis Item": "항목 대상 불분명",
 "Menopause Price": "가격 지칭 부자연(Pregnancy Price 기각 선례)",
 "Rafting Loan": "결합 불성립", "Pregnancy Sum": "결합 불성립",
 "Climbing Cash": "결합 불성립", "Fertility Sale": "결합 불성립",
 "Biking Allowance": "결합 불성립", "Thyroid Tariff": "결합 불성립",
 "Golf Margin": "결합 불성립", "Cholesterol Fine": "결합 불성립",
 "Fishing Link": "결합 불성립", "Hypertension Rule": "결합 불성립",
 "Camping Category": "결합 불성립", "Anemia Attribute": "결합 불성립",
 "Glamping Serial": "결합 불성립", "Heartburn Token": "결합 불성립",
 "Stargazing Balance": "결합 불성립", "Constipation Interest": "결합 불성립",
 "Birdwatching Due": "결합 불성립", "Concussion Subsidy": "결합 불성립",
 "Canyon Arrears": "결합 불성립", "Sprain Advance": "결합 불성립",
 "Geyser Penalty": "결합 불성립", "Fracture Markup": "결합 불성립",
 "Fjord Redemption": "결합 불성립", "Insulin Extension": "결합 불성립",
 "Savanna Trial": "결합 불성립", "Tundra Graph": "그래프 대상 불분명",
 "Prairie Label": "결합 불성립", "Marsh Manual": "설명 대상 불분명",
 "Cove Worksheet": "학습지 근거 약함", "Cavern Schematic": "회로도 어휘 부자연",
 "Oasis Layout": "결합 불성립", "Dune Sketch": "제품성 불분명",
 "Dolphin Rendering": "렌더링 대상 불분명", "Penguin Notification": "결합 불성립",
 "Flamingo Kit": "키트 대상 불분명", "Turtle Count": "대상 불분명",
 "Moose Message": "결합 불성립", "Bison Total": "결합 불성립",
 "Reindeer Widget": "위젯 대상 불분명", "Renewal Workbook": "워크북 대상 불분명",
 "Liner Mode": "기능 토글로 읽혀 제품 불분명", "Coating Spec": "결합 불성립",
 "Toilet Quantity": "수량 대상 불분명", "Ukulele Analysis": "분석 대상 불분명",
 "Reconciliation Habit": "결합 불성립", "Courier Mode": "기능 토글로 읽혀 제품 불분명",
 "Mortgage Spec": "결합 불성립", "Annuity Quantity": "수량 대상 불분명",
 "Overtime Login": "포털 서비스 대상 불분명", "Barcode Coach": "코칭 대상 불분명",
 "Valet Habit": "결합 불성립", "Court Asset": "결합 불성립",
 "Judge Estimator": "산출 대상 불분명", "Jury Validation": "검증 대상 불분명",
 "Lawsuit Checkin": "체크인 대상 불분명", "Divorce Evaluation": "평가 대상 불분명",
 "Injection App": "주사 단독으로 앱 대상 불분명", "Igniter Tips": "대상 불분명(Igniter 계열)",
 "Rim Advice": "대상 불분명(Rim 계열)",
 "Stairs Mode": "기능 토글로 읽혀 제품 불분명", "Location Spec": "결합 불성립",
 "Decor Quantity": "수량 대상 불분명", "Roof Login": "결합 불성립",
 "Valve Analysis": "분석 대상 불분명", "Microfiber Coach": "코칭 대상 불분명",
 "Backflow Habit": "결합 불성립", "Custody Radar": "레이더 대상 불분명",
 "Testament Roster": "명부 대상 불분명", "Mediation Item": "항목 대상 불분명",
 "Guardianship Category": "결합 불성립", "Trademark Schematic": "회로도 어휘 부자연",
 "Formula Workbook": "워크북 대상 불분명", "Mailroom Mode": "기능 토글로 읽혀 제품 불분명",
 "Kayaking Spec": "결합 불성립", "Songbook Quantity": "수량 대상 불분명",
 "Stretch Login": "결합 불성립", "Copay Coach": "코칭 대상 불분명",
 "Masonry Habit": "결합 불성립", "Migraine Order": "결합 불성립(Insomnia Order 기각 선례)",
 "Insomnia Table": "결합 불성립", "Acne Voucher": "결합 불성립",
 "Snowboarding Memo": "결합 불성립", "Eczema Quota": "결합 불성립",
 "Ziplining Brief": "결합 불성립", "Psoriasis Circular": "결합 불성립",
 "Sledding Confirmation": "확인 대상 불분명", "Vertigo Recap": "결합 불성립",
 "Diving Item": "항목 대상 불분명", "Arthritis Unit": "결합 불성립",
 "Sailing Price": "가격 지칭 부자연(Rafting Price 기각 선례)",
 "Menopause Fare": "결합 불성립", "Rafting Sum": "결합 불성립",
 "Pregnancy Debt": "결합 불성립", "Climbing Sale": "결합 불성립",
 "Fertility Charge": "결합 불성립", "Biking Tariff": "결합 불성립",
 "Thyroid Value": "결합 불성립", "Golf Fine": "결합 불성립",
 "Cholesterol Number": "수치 지칭이 조건명과 결합 시 부자연",
 "Fishing Rule": "결합 불성립", "Hypertension Detail": "결합 불성립",
 "Camping Attribute": "결합 불성립", "Anemia Field": "결합 불성립",
 "Glamping Token": "결합 불성립", "Heartburn Signature": "결합 불성립",
 "Stargazing Interest": "결합 불성립", "Constipation Asset": "결합 불성립",
 "Birdwatching Subsidy": "결합 불성립", "Concussion Discount": "결합 불성립",
 "Canyon Advance": "결합 불성립", "Sprain Penalty": "결합 불성립",
 "Geyser Markup": "결합 불성립", "Fracture Redemption": "결합 불성립",
 "Fjord Extension": "결합 불성립", "Insulin Trial": "결합 불성립",
 "Savanna Graph": "그래프 대상 불분명", "Tundra Label": "결합 불성립",
 "Prairie Manual": "설명 대상 불분명", "Marsh Worksheet": "학습지 근거 약함",
 "Cliff Schematic": "회로도 어휘 부자연", "Cavern Layout": "결합 불성립",
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
out = base + r"\_dec_c3.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
