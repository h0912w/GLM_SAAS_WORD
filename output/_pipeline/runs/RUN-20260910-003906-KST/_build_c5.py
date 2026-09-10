# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk5_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Prairie Diagram": (0.55, "초원 생태 다이어그램(지리 교육 축)"),
 "Tundra Diagram": (0.55, "툰드라 생태 다이어그램(지리 교육 축)"),
 "Filtration App": (0.6, "필터 관리 앱(HVAC 실재)"),
 "Masterkey Tips": (0.55, "마스터키 운영 팁(App→Tips 평행)"),
 "Washer Tips": (0.55, "세탁기 관리 팁(App→Tips 평행)"),
 "Bass Workbook": (0.55, "베이스 연습 워크북(음악 교재 실재)"),
 "Courier Login": (0.55, "배송 접수 포털 로그인"),
 "Mortgage Analysis": (0.55, "모기지 분석(금융 분석 축)"),
 "Lawyer Update": (0.55, "사건 업데이트(Notary Update 평행)"),
 "Toy Tips": (0.55, "장난감 선택 팁(App→Tips 평행)"),
 "Mediation Cost": (0.55, "조정 비용 안내(Mediation Fee 평행)"),
 "Tanker App": (0.55, "유조차 운송 관리 앱(실재)"),
 "Deed Tips": (0.55, "등기 절차 팁(App→Tips 평행)"),
 "Mailroom Login": (0.55, "메일룸 시스템 로그인(실무 포털 축)"),
 "Stretch Habit": (0.55, "스트레칭 습관(stretching habit 실검색)"),
 "Diving Cost": (0.55, "다이빙 비용 정보(Sailing Cost 평행)"),
 "Shift App": (0.6, "교대 근무 관리 앱(실재 카테고리)"),
 "Turbidity App": (0.6, "수영장 수질(탁도) 측정 앱(pool testing 실재)"),
 "Filtration Tips": (0.55, "필터 관리 팁(App→Tips 평행)"),
 "Terminology Workbook": (0.55, "번역 용어 정리 워크북(Idiom Workbook 평행)"),
 "Paralegal Login": (0.55, "로펌 업무 포털 로그인(실무 포털 축)"),
 "Courier Analysis": (0.55, "배송 데이터 분석(Container Analysis 평행)"),
 "Lawyer Feed": (0.55, "법률 소식 피드(Notary Feed 평행)"),
 "Divorce Requirement": (0.55, "이혼 요건 안내(divorce requirements 실검색)"),
}
R_DUP = {
 "Terminology Advice": "동일 배치 승인된 Terminology Tips와 동일 기능 의미 중복",
 "Hostel Advice": "동일 배치 승인된 Hostel Tips와 동일 기능 의미 중복",
 "Policyholder Advice": "동일 배치 승인된 Policyholder Tips와 동일 기능 의미 중복",
 "Masterkey Advice": "동일 배치 승인된 Masterkey Tips와 동일 기능 의미 중복",
 "Washer Advice": "동일 배치 승인된 Washer Tips와 동일 기능 의미 중복",
 "Toy Advice": "동일 배치 승인된 Toy Tips와 동일 기능 의미 중복",
}
R = {
 "Pregnancy Cash": "결합 불성립", "Climbing Duty": "결합 불성립",
 "Fertility Allowance": "결합 불성립", "Biking Stake": "결합 불성립",
 "Thyroid Margin": "결합 불성립", "Golf Version": "결합 불성립",
 "Cholesterol Link": "결합 불성립", "Fishing Identifier": "결합 불성립",
 "Hypertension Category": "결합 불성립", "Camping Format": "결합 불성립",
 "Anemia Serial": "결합 불성립", "Glamping Marker": "결합 불성립",
 "Heartburn Balance": "결합 불성립", "Stargazing Levy": "결합 불성립",
 "Constipation Due": "결합 불성립", "Birdwatching Arrears": "결합 불성립",
 "Concussion Advance": "결합 불성립", "Canyon Markup": "결합 불성립",
 "Sprain Redemption": "결합 불성립", "Geyser Extension": "결합 불성립",
 "Fracture Trial": "결합 불성립", "Fjord Graph": "그래프 대상 불분명",
 "Insulin Label": "결합 불성립", "Savanna Manual": "설명 대상 불분명",
 "Tundra Worksheet": "학습지 근거 약함", "Marsh Schematic": "회로도 어휘 부자연",
 "Cove Layout": "결합 불성립", "Cliff Sketch": "제품성 불분명",
 "Cavern Outline": "지형은 공예 오트라인 대상 아님", "Oasis Rendering": "렌더링 대상 불분명",
 "Dune Notification": "결합 불성립", "Whale Kit": "키트 대상 불분명",
 "Dolphin Count": "대상 불분명", "Penguin Message": "결합 불성립",
 "Flamingo Total": "결합 불성립", "Turtle Widget": "위젯 대상 불분명",
 "Moose Repository": "결합 불성립", "Bison Announcement": "결합 불성립",
 "Reindeer Calculator": "계산 대상 불분명", "Storage Workbook": "워크북 대상 불분명",
 "Gallery Mode": "기능 토글로 읽혀 제품 불분명", "Florist Spec": "결합 불성립",
 "Renewal Quantity": "수량 대상 불분명", "Liner Login": "결합 불성립",
 "Coating Analysis": "분석 대상 불분명", "Toilet Coach": "코칭 대상 불분명",
 "Vacation Habit": "결합 불성립", "Foam App": "앱 대상 불분명",
 "Triage Mode": "기능 토글로 읽혀 제품 불분명", "Dividend Spec": "결합 불성립",
 "Paralegal Quantity": "수량 대상 불분명", "Annuity Coach": "코칭 대상 불분명",
 "Overtime Habit": "결합 불성립", "Attorney Fare": "결합 불성립",
 "Court Subsidy": "결합 불성립", "Judge Timer": "측정 대상 불분명",
 "Jury Model": "결합 불성립", "Lawsuit Weight": "결합 불성립",
 "Divorce Benefit": "혜택 대상 불분명", "Molar App": "치아 단위로 앱 대상 불분명",
 "Product Advice": "일반 명사로 대상 불분명(Product 계열 기각 선례)",
 "Injection Workbook": "대상 불분명(Injection 계열)", "Igniter Mode": "기능 토글로 읽혀 제품 불분명",
 "Rim Spec": "결합 불성립", "Idiom Quantity": "수량 대상 불분명",
 "Stairs Login": "결합 불성립(Stairs 계열 기각 선례)",
 "Location Analysis": "분석 대상 불분명", "Decor Coach": "코칭 대상 불분명",
 "Roof Habit": "결합 불성립", "Custody Compass": "결합 불성립",
 "Immigration Chain": "결합 불성립", "Testament Bin": "결합 불성립",
 "Notary Estimate": "견적 대상 불분명", "Guardianship Format": "결합 불성립",
 "Trademark Outline": "결합 불성립", "Patent Trend": "추이 대상 불분명",
 "Copyright Ping": "결합 불성립", "Countertop Workbook": "워크북 대상 불분명",
 "Cocktail Mode": "기능 토글로 읽혀 제품 불분명", "Toothpaste Spec": "결합 불성립",
 "Formula Quantity": "수량 대상 불분명", "Kayaking Analysis": "분석 대상 불분명",
 "Songbook Coach": "코칭 대상 불분명(Songbook 계열 기각 선례)",
 "Migraine Code": "결합 불성립", "Insomnia Slot": "결합 불성립",
 "Skydiving Stub": "결합 불성립", "Acne Statement": "결합 불성립",
 "Snowboarding Bulletin": "결합 불성립", "Eczema Brief": "결합 불성립",
 "Ziplining Petition": "결합 불성립", "Psoriasis Confirmation": "확인 대상 불분명",
 "Sledding Fee": "요금 근거 약함(Diving Fee와 달리 실검색 축약)", "Vertigo Item": "항목 대상 불분명",
 "Arthritis Price": "가격 지칭 부자연(Arthritis Cost 승인과 구별)",
 "Sailing Loan": "결합 불성립", "Menopause Sum": "결합 불성립",
 "Rafting Cash": "결합 불성립", "Pregnancy Sale": "결합 불성립",
 "Climbing Allowance": "결합 불성립", "Fertility Tariff": "결합 불성립",
 "Biking Margin": "결합 불성립", "Thyroid Fine": "결합 불성립",
 "Golf Link": "결합 불성립", "Cholesterol Rule": "결합 불성립",
 "Fishing Category": "결합 불성립", "Hypertension Attribute": "결합 불성립",
 "Camping Serial": "결합 불성립", "Anemia Token": "결합 불성립",
 "Glamping Balance": "결합 불성립", "Heartburn Interest": "결합 불성립",
 "Stargazing Due": "결합 불성립", "Constipation Subsidy": "결합 불성립",
 "Birdwatching Advance": "결합 불성립", "Concussion Penalty": "결합 불성립",
 "Canyon Redemption": "결합 불성립", "Sprain Extension": "결합 불성립",
 "Geyser Trial": "결합 불성립", "Fracture Graph": "그래프 대상 불분명",
 "Fjord Label": "결합 불성립", "Insulin Manual": "설명 대상 불분명",
 "Savanna Worksheet": "학습지 근거 약함", "Prairie Schematic": "회로도 어휘 부자연",
 "Marsh Layout": "결합 불성립", "Cove Sketch": "제품성 불분명",
 "Cliff Outline": "지형은 공예 오트라인 대상 아님", "Cavern Rendering": "렌더링 대상 불분명",
 "Oasis Notification": "결합 불성립", "Dune Kit": "키트 대상 불분명",
 "Whale Count": "대상 불분명", "Dolphin Message": "결합 불성립",
 "Penguin Total": "결합 불성립", "Flamingo Widget": "위젯 대상 불분명",
 "Turtle Repository": "결합 불성립", "Moose Announcement": "결합 불성립",
 "Bison Calculator": "계산 대상 불분명", "Reindeer Converter": "변환 대상 불분명",
 "Storage Mode": "기능 토글로 읽혀 제품 불분명", "Gallery Spec": "결합 불성립",
 "Florist Quantity": "수량 대상 불분명", "Renewal Login": "무엇의 갱신인지 불분명해 결합 불성립",
 "Liner Analysis": "분석 대상 불분명", "Coating Coach": "코칭 대상 불분명",
 "Toilet Habit": "결합 불성립", "Turbidity Workbook": "워크북 대상 불분명",
 "Foam Tips": "대상 불분명(Foam App 기각 선례)", "Hostel Workbook": "워크북 대상 불분명",
 "Bass Mode": "기능 토글로 읽혀 제품 불분명", "Triage Spec": "결합 불성립",
 "Dividend Quantity": "수량 대상 불분명", "Mortgage Coach": "코칭 대상 불분명",
 "Annuity Habit": "결합 불성립", "Attorney Tax": "결합 불성립",
 "Court Discount": "결합 불성립", "Judge Workshop": "워크숍 주체 불분명(Patent Workshop 기각 선례)",
 "Jury Availability": "결합 불성립", "Lawsuit Distance": "결합 불성립",
 "Tick App": "앱 대상 불분명", "Molar Tips": "대상 불분명(Molar App 기각 선례)",
 "Product Workbook": "대상 불분명(Product 계열)", "Injection Mode": "기능 토글로 읽혀 제품 불분명",
 "Igniter Spec": "결합 불성립", "Rim Quantity": "수량 대상 불분명",
 "Idiom Login": "결합 불성립", "Stairs Analysis": "분석 대상 불분명",
 "Location Coach": "코칭 대상 불분명", "Decor Habit": "결합 불성립",
 "Custody Beacon": "결합 불성립", "Immigration Ring": "결합 불성립",
 "Testament Passport": "결합 불성립", "Notary Order": "주문 대상 불분명",
 "Mediation Price": "가격 지칭 부자연(Mediation Cost 승인과 구별)",
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
out = base + r"\_dec_c5.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
