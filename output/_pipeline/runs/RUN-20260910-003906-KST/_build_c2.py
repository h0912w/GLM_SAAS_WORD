# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk2_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Mailroom Tips": (0.55, "우편물 운영 팁"),
 "Masonry Login": (0.55, "석공 업체 포털 로그인(Welding/Tractor Login 평행)"),
 "Chore Habit": (0.55, "집안일 습관 트래킹(행위 도메인 결합)"),
 "Menopause Plan": (0.55, "폐경기 관리 계획(건강 관리 플랜 실검색)"),
 "Fertility Fund": (0.55, "불임 치료 자금(Fertility Loan 승인 선례 평행)"),
 "Oasis Diagram": (0.55, "오아시스 생태 다이어그램(지리 교육)"),
 "Penguin Outline": (0.55, "펭귄 공예 오트라인 인쇄물"),
 "Florist App": (0.55, "꽃집 운영 앱"),
 "Renewal Tips": (0.55, "임대 갱신 안내 팁"),
 "Reconciliation Analysis": (0.55, "계정 조정 분석(B2B 회계 분석)"),
 "Paralegal Tips": (0.55, "법률보조 업무 팁"),
 "Mortgage Workbook": (0.55, "모기지 계획 워크북"),
 "Homework Coach": (0.55, "과제 코칭 서비스(실검색)"),
 "Lawsuit Claim": (0.55, "소송 청구 관리"),
 "Idiom Tips": (0.55, "관용구 학습 팁"),
 "Location Workbook": (0.55, "촬영지 스카우팅 워크북"),
 "Safari Coach": (0.55, "사파리 투어 가이드 코칭"),
 "Harmonica Habit": (0.55, "하모니카 연습 습관 트래킹(Reader Habit 평행)"),
 "Notary Summary": (0.55, "공증 건 요약 관리"),
 "Mediation Entry": (0.55, "조정 신청 접수(Sailing Entry 평행)"),
 "Trademark Worksheet": (0.55, "상표 출원 준비 워크시트"),
 "Patent Helper": (0.55, "특허 절차 도우미"),
 "Toothpaste App": (0.55, "치약 정기배송 앱"),
 "Formula Tips": (0.55, "분유 수유 팁"),
 "Kayaking Workbook": (0.55, "카약 여행 계획 워크북"),
 "Menopause Cost": (0.55, "폐경 치료 비용 정보(Pregnancy/Rafting Cost 평행)"),
 "Cavern Diagram": (0.55, "동굴 형성 다이어그램(지리 교육)"),
 "Dolphin Outline": (0.55, "돌고래 공예 오트라인 인쇄물"),
 "Gallery App": (0.55, "사진 포트폴리오 갤러리 앱"),
 "Florist Tips": (0.55, "꽃 관리·판매 팁"),
 "Prescription Analysis": (0.55, "복약·처방 데이터 분석(Dosage Analysis 평행)"),
 "Dividend App": (0.55, "배당 포트폴리오 추적 앱(실재 카테고리)"),
 "Dividend Tips": (0.55, "배당 투자 팁(실검색 콘텐츠)"),
 "Triage App": (0.6, "환자 분류 앱(triage 소프트웨어 실재)"),
 "Courier Workbook": (0.55, "택배 운영 워크북"),
 "Coating Workbook": (0.55, "코팅 관리 기록 워크북(디테일링 실재)"),
 "Scaffold Login": (0.55, "공사 현장 포털 로그인"),
}
R_DUP = {
 "Kayaking Advice": "동일 배치 승인된 Kayaking Tips와 동일 기능 의미 중복",
 "Courier Advice": "동일 배치 승인된 Courier Tips와 동일 기능 의미 중복",
 "Mailroom Advice": "동일 배치 승인된 Mailroom Tips와 동일 기능 의미 중복",
 "Renewal Advice": "동일 배치 승인된 Renewal Tips와 동일 기능 의미 중복",
 "Paralegal Advice": "동일 배치 승인된 Paralegal Tips와 동일 기능 의미 중복",
 "Liner Advice": "동일 배치 승인된 Liner Tips와 동일 기능 의미 중복",
}
R = {
 "Songbook Workbook": "워크북 대상 불분명(Songbook 계열 기각 선례)",
 "Stretch Mode": "기능 토글로 읽혀 제품 불분명", "Insolvency Spec": "결합 불성립",
 "Copay Quantity": "수량 대상 불분명", "Barista Analysis": "분석 대상 불분명(Barista 계열 기각 선례)",
 "Mouthwash Coach": "코칭 대상 불분명(Mouthwash 계열 기각 선례)",
 "Barista Coach": "코칭 대상 불분명(Barista 계열 기각 선례)",
 "Migraine Index": "색인 대상 불분명", "Insomnia Receipt": "결합 불성립",
 "Skydiving Slip": "결합 불성립", "Acne Sample": "결합 불성립",
 "Snowboarding Badge": "배지 대상 불분명", "Eczema Stub": "결합 불성립",
 "Ziplining Quota": "결합 불성립", "Psoriasis Tab": "결합 불성립",
 "Sledding Circular": "결합 불성립", "Vertigo Advisory": "안내 대상 불분명",
 "Diving Recap": "요약 대상 불분명", "Arthritis Entry": "등록 대상 불분명",
 "Diving Entry": "입수 기법 어휘로 읽혀 혼동(Sailing Entry와 달리 대상 불분명)",
 "Sailing Unit": "결합 불성립", "Rafting Fare": "결합 불성립",
 "Pregnancy Tax": "결합 불성립", "Climbing Debt": "결합 불성립",
 "Pregnancy Loan": "대출 산업 근거 없음(Fertility Loan과 달리 대상 불분명)",
 "Climbing Fund": "결합 불성립", "Fertility Cash": "현금 지칭 부자연",
 "Biking Charge": "결합 불성립", "Thyroid Duty": "결합 불성립",
 "Golf Value": "결합 불성립", "Cholesterol Stake": "결합 불성립",
 "Fishing Number": "결합 불성립", "Hypertension Version": "결합 불성립",
 "Camping Detail": "결합 불성립", "Anemia Identifier": "결합 불성립",
 "Glamping Field": "결합 불성립", "Heartburn Format": "결합 불성립",
 "Stargazing Signature": "결합 불성립", "Constipation Marker": "결합 불성립",
 "Birdwatching Asset": "결합 불성립", "Concussion Levy": "결합 불성립",
 "Canyon Subsidy": "결합 불성립", "Sprain Discount": "결합 불성립",
 "Geyser Arrears": "결합 불성립", "Fracture Advance": "결합 불성립",
 "Fjord Penalty": "결합 불성립", "Insulin Markup": "결합 불성립",
 "Savanna Redemption": "결합 불성립", "Tundra Extension": "결합 불성립",
 "Prairie Trial": "결합 불성립", "Marsh Graph": "그래프 대상 불분명",
 "Cove Label": "결합 불성립", "Cliff Manual": "설명 대상 불분명",
 "Cavern Worksheet": "학습지 근거 약함(Whale/Dune만 교육 축 승인)",
 "Dune Schematic": "회로도 어휘 부자연", "Whale Layout": "결합 불성립",
 "Dolphin Sketch": "제품성 불분명", "Flamingo Rendering": "렌더링 대상 불분명",
 "Turtle Notification": "결합 불성립", "Moose Kit": "키트 대상 불분명",
 "Bison Count": "대상 불분명", "Reindeer Message": "결합 불성립",
 "Toilet Mode": "기능 토글로 읽혀 제품 불분명", "Vacation Spec": "결합 불성립",
 "Ukulele Quantity": "수량 대상 불분명", "Prescription Login": "포털 서비스 대상 불분명(Dosage Login 기각 선례)",
 "Matter Coach": "코칭 대상 불분명", "Container Habit": "결합 불성립",
 "Overtime Spec": "결합 불성립", "Scaffold Quantity": "수량 산출 근거 약함",
 "Barcode Login": "결합 불성립", "Valet Analysis": "분석 대상 불분명(Valet 계열 기각 선례)",
 "Welding Habit": "결합 불성립", "Lawyer View": "조회 대상 불분명",
 "Attorney Item": "항목 대상 불분명", "Court Balance": "결합 불성립",
 "Judge Generator": "생성 대상 불분명", "Jury Case": "서비스 대상 불분명",
 "Divorce Approval": "결합 불성립", "Rim App": "앱 대상 불분명",
 "Stairs Advice": "계단 단독으로 조언 대상 불분명", "Decor Mode": "기능 토글로 읽혀 제품 불분명",
 "Roof Spec": "결합 불성립", "Valve Quantity": "수량 대상 불분명",
 "Microfiber Login": "결합 불성립", "Backflow Analysis": "분석 대상 불분명",
 "Custody Hub": "허브 대상 불분명", "Immigration Panel": "패널 대상 불분명",
 "Testament Post": "결합 불성립", "Guardianship Detail": "결합 불성립",
 "Copyright Account": "계정 대상 불분명", "Songbook Mode": "기능 토글로 읽혀 제품 불분명",
 "Stretch Spec": "결합 불성립", "Insolvency Quantity": "수량 대상 불분명",
 "Copay Login": "포털 서비스 대상 불분명", "Masonry Analysis": "분석 대상 불분명",
 "Mouthwash Habit": "결합 불성립", "Migraine Ticket": "결합 불성립",
 "Insomnia Code": "결합 불성립", "Skydiving Sample": "결합 불성립",
 "Acne Slot": "결합 불성립", "Snowboarding Stub": "결합 불성립",
 "Eczema Statement": "결합 불성립", "Ziplining Tab": "결합 불성립",
 "Psoriasis Bulletin": "결합 불성립", "Sledding Advisory": "안내 대상 불분명(Diving Advisory와 달리 특보 근거 없음)",
 "Vertigo Petition": "결합 불성립", "Arthritis Fee": "결합 불성립",
 "Sailing Plan": "계획 대상 불분명(1라운드 기각 선례)", "Rafting Tax": "결합 불성립",
 "Biking Duty": "결합 불성립", "Thyroid Allowance": "결합 불성립",
 "Golf Stake": "결합 불성립", "Cholesterol Margin": "결합 불성립",
 "Fishing Version": "결합 불성립", "Hypertension Link": "결합 불성립",
 "Camping Identifier": "결합 불성립", "Anemia Category": "결합 불성립",
 "Glamping Format": "결합 불성립", "Heartburn Serial": "결합 불성립",
 "Stargazing Marker": "결합 불성립", "Constipation Balance": "결합 불성립",
 "Birdwatching Levy": "결합 불성립", "Concussion Due": "결합 불성립",
 "Canyon Discount": "결합 불성립", "Sprain Arrears": "결합 불성립",
 "Geyser Advance": "결합 불성립", "Fracture Penalty": "결합 불성립",
 "Fjord Markup": "결합 불성립", "Insulin Redemption": "결합 불성립",
 "Savanna Extension": "결합 불성립", "Tundra Trial": "결합 불성립",
 "Prairie Graph": "그래프 대상 불분명", "Marsh Label": "결합 불성립",
 "Cove Manual": "설명 대상 불분명", "Cliff Worksheet": "학습지 근거 약함",
 "Oasis Schematic": "회로도 어휘 부자연", "Dune Layout": "결합 불성립",
 "Whale Sketch": "제품성 불분명", "Penguin Rendering": "렌더링 대상 불분명",
 "Flamingo Notification": "결합 불성립", "Turtle Kit": "키트 대상 불분명",
 "Moose Count": "대상 불분명", "Bison Message": "결합 불성립",
 "Reindeer Total": "결합 불성립", "Liner Workbook": "워크북 대상 불분명",
 "Coating Mode": "기능 토글로 읽혀 제품 불분명", "Toilet Spec": "결합 불성립",
 "Vacation Quantity": "수량 대상 불분명", "Ukulele Login": "포털 서비스 대상 불분명(Harmonica Login 기각 선례)",
 "Reconciliation Coach": "코칭 대상 불분명", "Matter Habit": "결합 불성립",
 "Mortgage Mode": "기능 토글로 읽혀 제품 불분명",
 "Annuity Mode": "기능 토글로 읽혀 제품 불분명", "Annuity Spec": "결합 불성립",
 "Overtime Quantity": "수량 대상 불분명", "Barcode Analysis": "분석 대상 불분명",
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
out = base + r"\_dec_c2.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
