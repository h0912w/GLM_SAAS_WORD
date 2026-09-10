# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk4_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Terminology App": (0.6, "번역 용어집 관리 앱(실재 카테고리)"),
 "Storage Tips": (0.55, "보관 이용 팁(App→Tips 평행)"),
 "Ukulele Coach": (0.55, "우쿨렐레 레슨 코치(Harmonica Coach 평행)"),
 "Prescription Habit": (0.55, "복약 습관 관리(Dosage Habit 평행)"),
 "Hostel App": (0.6, "호스텔 예약 앱(실재 카테고리)"),
 "Bass Tips": (0.55, "베이스 연주 팁(App→Tips 평행)"),
 "Dividend Workbook": (0.55, "배당 투자 계획 워크북(금융 소비자 워크북 축)"),
 "Overtime Analysis": (0.55, "초과근무 데이터 분석(HR 분석 실재)"),
 "Attorney Cost": (0.55, "변호사 비용 정보(Attorney Fee 평행)"),
 "Divorce Questionnaire": (0.6, "이혼 절차 설문(intake 실재, Questionnaire 검증 축)"),
 "Policyholder App": (0.6, "보험 가입자 포털 앱(실재)"),
 "Countertop Tips": (0.55, "카운터톱 관리 팁(App→Tips 평행)"),
 "Arthritis Plan": (0.55, "관절염 관리 계획(arthritis care plan 실검색)"),
 "Marsh Diagram": (0.55, "습지 생태 다이어그램(지리 교육 축)"),
 "Masterkey App": (0.6, "마스터키 시스템 관리 앱(실재)"),
 "Terminology Tips": (0.55, "용어 관리 팁(App→Tips 평행)"),
 "Vacation Coach": (0.55, "여행 계획 코치(travel coach 관용구)"),
 "Ukulele Habit": (0.55, "연습 습관 트래킹(Harmonica Habit 평행)"),
 "Washer App": (0.55, "세탁기 설치·수리 앱(가전 수리 실재)"),
 "Hostel Tips": (0.55, "호스텔 예약 팁(App→Tips 평행)"),
 "Triage Workbook": (0.55, "분류 프로토콜 교육 워크북(의료 교육 실재)"),
 "Mortgage Login": (0.55, "모기지 신청 포털 로그인"),
 "Annuity Analysis": (0.55, "연금 수익 분석(금융 분석 축)"),
 "Lawyer Rate": (0.55, "변호사 요율 조회(lawyer rates 실검색)"),
 "Toy App": (0.55, "장난감 대여·추천 앱(실재 카테고리)"),
 "Location Login": (0.55, "촬영지 예약 포털 로그인(Location App 연계)"),
 "Mediation Plan": (0.55, "조정 절차 계획(mediation plan 실재)"),
 "Copyright Lookup": (0.55, "저작권 조회 도구(copyright search 실재)"),
 "Deed App": (0.6, "증서·등기 관리 앱(실재)"),
 "Policyholder Tips": (0.55, "보험 활용 팁(App→Tips 평행)"),
 "Stretch Coach": (0.55, "스트레칭 코치(실재 카테고리)"),
 "Diving Plan": (0.55, "다이빙 계획(dive plan 안전 절차 용어)"),
 "Arthritis Cost": (0.55, "관절염 치료 비용(Menopause Cost 평행)"),
}
R_DUP = {
 "Gallery Advice": "동일 배치 승인된 Gallery Tips와 동일 기능 의미 중복",
 "Triage Advice": "동일 배치 승인된 Triage Tips와 동일 기능 의미 중복",
 "Cocktail Advice": "동일 배치 승인된 Cocktail Tips와 동일 기능 의미 중복",
 "Storage Advice": "동일 배치 승인된 Storage Tips와 동일 기능 의미 중복",
 "Bass Advice": "동일 배치 승인된 Bass Tips와 동일 기능 의미 중복",
 "Countertop Advice": "동일 배치 승인된 Countertop Tips와 동일 기능 의미 중복",
}
R = {
 "Oasis Sketch": "제품성 불분명", "Dune Outline": "지형은 공예 오트라인 대상 아님(동물 축만 승인)",
 "Whale Rendering": "렌더링 대상 불분명", "Dolphin Notification": "결합 불성립",
 "Penguin Kit": "키트 대상 불분명", "Flamingo Count": "대상 불분명",
 "Turtle Message": "결합 불성립", "Moose Total": "결합 불성립",
 "Bison Widget": "위젯 대상 불분명", "Reindeer Repository": "결합 불성립",
 "Renewal Mode": "기능 토글로 읽혀 제품 불분명", "Liner Spec": "결합 불성립",
 "Gallery Workbook": "워크북 대상 불분명",
 "Coating Quantity": "수량 대상 불분명", "Toilet Login": "결합 불성립",
 "Vacation Analysis": "분석 대상 불분명",
 "Florist Workbook": "워크북 대상 불분명", "Paralegal Mode": "기능 토글로 읽혀 제품 불분명",
 "Courier Spec": "결합 불성립", "Mortgage Quantity": "수량 대상 불분명",
 "Annuity Login": "포털 서비스 대상 불분명",
 "Scaffold Coach": "코칭 대상 불분명", "Barcode Habit": "결합 불성립",
 "Lawyer Level": "결합 불성립", "Court Levy": "결합 불성립",
 "Judge Checker": "검사 대상 불분명", "Jury Lookup": "조회 서비스 대상 불분명",
 "Lawsuit Size": "결합 불성립",
 "Product App": "일반 명사로 앱 대상 불분명", "Injection Tips": "대상 불분명(Injection 계열)",
 "Igniter Advice": "대상 불분명(Igniter 계열)", "Rim Workbook": "대상 불분명(Rim 계열)",
 "Idiom Mode": "기능 토글로 읽혀 제품 불분명", "Stairs Spec": "결합 불성립",
 "Location Quantity": "수량 대상 불분명", "Decor Login": "결합 불성립",
 "Roof Analysis": "분석 대상 불분명", "Valve Coach": "코칭 대상 불분명",
 "Microfiber Habit": "결합 불성립", "Custody Relay": "결합 불성립",
 "Immigration Rail": "결합 불성립", "Testament Alert": "알림 대상 불분명",
 "Notary Index": "색인 대상 불분명", "Mediation Unit": "결합 불성립",
 "Guardianship Attribute": "결합 불성립", "Trademark Layout": "결합 불성립",
 "Patent Streak": "결합 불성립", "Copyright Validation": "검증 대상 불분명",
 "Toothpaste Workbook": "워크북 대상 불분명", "Formula Mode": "기능 토글로 읽혀 제품 불분명",
 "Mailroom Spec": "결합 불성립", "Kayaking Quantity": "수량 대상 불분명",
 "Songbook Login": "결합 불성립(Songbook 계열 기각 선례)",
 "Stretch Analysis": "분석 대상 불분명", "Insolvency Coach": "코칭 대상 불분명",
 "Copay Habit": "결합 불성립", "Migraine Bill": "결합 불성립",
 "Insomnia Slip": "결합 불성립", "Skydiving Voucher": "바우처 대상 불분명(Snowboarding Voucher 기각 선례)",
 "Acne Badge": "결합 불성립", "Snowboarding Quota": "결합 불성립",
 "Eczema Tab": "결합 불성립", "Ziplining Circular": "결합 불성립",
 "Psoriasis Advisory": "안내 대상 불분명", "Sledding Recap": "결합 불성립",
 "Vertigo Entry": "결합 불성립", "Diving Unit": "결합 불성립",
 "Sailing Fare": "결합 불성립", "Menopause Tax": "결합 불성립",
 "Rafting Debt": "결합 불성립", "Pregnancy Fund": "자금 산업 근거 약함(Fertility Fund와 구별)",
 "Climbing Charge": "결합 불성립", "Fertility Duty": "결합 불성립",
 "Biking Value": "결합 불성립", "Thyroid Stake": "결합 불성립",
 "Golf Number": "결합 불성립", "Cholesterol Version": "결합 불성립",
 "Fishing Detail": "결합 불성립", "Hypertension Identifier": "결합 불성립",
 "Camping Field": "결합 불성립", "Anemia Format": "결합 불성립",
 "Glamping Signature": "결합 불성립", "Heartburn Marker": "결합 불성립",
 "Stargazing Asset": "결합 불성립", "Constipation Levy": "결합 불성립",
 "Birdwatching Discount": "결합 불성립", "Concussion Arrears": "결합 불성립",
 "Canyon Penalty": "결합 불성립", "Sprain Markup": "결합 불성립",
 "Geyser Redemption": "결합 불성립", "Fracture Extension": "결합 불성립",
 "Fjord Trial": "결합 불성립", "Insulin Graph": "그래프 대상 불분명",
 "Savanna Label": "결합 불성립", "Tundra Manual": "설명 대상 불분명",
 "Prairie Worksheet": "학습지 근거 약함", "Cove Schematic": "회로도 어휘 부자연",
 "Cliff Layout": "결합 불성립", "Cavern Sketch": "제품성 불분명",
 "Oasis Outline": "지형은 공예 오트라인 대상 아님", "Dune Rendering": "렌더링 대상 불분명",
 "Whale Notification": "결합 불성립", "Dolphin Kit": "키트 대상 불분명",
 "Penguin Count": "대상 불분명", "Flamingo Message": "결합 불성립",
 "Turtle Total": "결합 불성립", "Moose Widget": "위젯 대상 불분명",
 "Bison Repository": "결합 불성립", "Reindeer Announcement": "결합 불성립",
 "Terminology Workbook": "워크북 대상 불분명", "Florist Mode": "기능 토글로 읽혀 제품 불분명",
 "Renewal Spec": "결합 불성립", "Liner Quantity": "수량 대상 불분명",
 "Coating Login": "결합 불성립", "Toilet Analysis": "분석 대상 불분명",
 "Dividend Mode": "기능 토글로 읽혀 제품 불분명", "Paralegal Spec": "결합 불성립",
 "Courier Quantity": "수량 대상 불분명", "Overtime Coach": "코칭 대상 불분명",
 "Scaffold Habit": "결합 불성립", "Attorney Price": "가격 지칭 부자연(Fee/Rate 승인과 구별)",
 "Court Due": "결합 불성립", "Judge Detector": "탐지 대상 불분명",
 "Jury Ping": "결합 불성립", "Lawsuit Length": "결합 불성립",
 "Divorce Utilization": "결합 불성립",
 "Product Tips": "일반 명사로 대상 불분명(Product App 기각 선례)",
 "Injection Advice": "대상 불분명(Injection 계열)",
 "Igniter Workbook": "대상 불분명(Igniter 계열)", "Rim Mode": "기능 토글로 읽혀 제품 불분명",
 "Idiom Spec": "결합 불성립", "Stairs Quantity": "수량 대상 불분명",
 "Decor Analysis": "분석 대상 불분명", "Roof Coach": "코칭 대상 불분명",
 "Valve Habit": "결합 불성립", "Custody Vault": "결합 불성립",
 "Immigration Trail": "결합 불성립", "Testament Chart": "차트 대상 불분명",
 "Notary Ticket": "결합 불성립", "Guardianship Field": "결합 불성립",
 "Trademark Sketch": "제품성 불분명", "Patent Rank": "결합 불성립",
 "Cocktail Workbook": "워크북 대상 불분명", "Toothpaste Mode": "기능 토글로 읽혀 제품 불분명",
 "Formula Spec": "결합 불성립", "Mailroom Quantity": "수량 대상 불분명",
 "Kayaking Login": "활동 단독으로 포털 서비스 불분명", "Songbook Analysis": "분석 대상 불분명",
 "Insolvency Habit": "결합 불성립", "Migraine Receipt": "결합 불성립",
 "Insomnia Sample": "결합 불성립", "Skydiving Badge": "배지 대상 불분명",
 "Acne Stub": "결합 불성립", "Snowboarding Tab": "결합 불성립",
 "Eczema Bulletin": "결합 불성립", "Ziplining Advisory": "안내 대상 불분명",
 "Psoriasis Petition": "결합 불성립", "Sledding Entry": "등록 대상 불분명(Diving Entry 기각 선례)",
 "Vertigo Fee": "결합 불성립", "Sailing Tax": "결합 불성립",
 "Menopause Loan": "대출 산업 근거 없음", "Rafting Fund": "결합 불성립",
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
out = base + r"\_dec_c4.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
