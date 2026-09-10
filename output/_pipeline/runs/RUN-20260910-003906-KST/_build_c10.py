# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk10_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Behavior App": (0.6, "반려동물 행동 교정 앱(실재 카테고리)"),
 "Toothbrush Tips": (0.55, "칫솔 관리 팁(App→Tips 평행)"),
 "Maintenance App": (0.55, "조경 유지관리 앱(실재)"),
 "Inspection Tips": (0.55, "검수·점검 팁(App→Tips 평행)"),
 "Tailings App": (0.55, "광미 관리 앱(광산 시설 관리 실재)"),
 "Coil Tips": (0.55, "HVAC 코일 관리 팁(App→Tips 평행)"),
 "Thesis App": (0.6, "논문 관리 앱(실재 카테고리)"),
 "Meeting Tips": (0.55, "회의 운영 팁(App→Tips 평행)"),
 "Testament Form": (0.55, "유언장 양식 서비스(will form 실재)"),
 "Patent Deadline": (0.55, "특허 기한 관리(기한 추적 실재)"),
 "Copyright Renewal": (0.55, "저작권 갱신 관리(실재)"),
 "Latte App": (0.55, "카페 주문·리워드 앱(실재)"),
 "Behavior Tips": (0.55, "행동 교정 팁(App→Tips 평행)"),
 "Chemical App": (0.55, "살충 화학 처리 기록 앱(SDS 관리 실재)"),
 "Maintenance Tips": (0.55, "유지관리 팁(App→Tips 평행)"),
 "Logbook App": (0.6, "비행 로그북 앱(파일럿 실재 카테고리)"),
 "Tailings Tips": (0.55, "광미 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Nanny Advice": "동일 배치 승인된 Nanny App/Tips와 동일 기능 의미 중복",
 "Pricing Advice": "동일 배치 승인된 Pricing App/Tips와 동일 기능 의미 중복",
 "Keypad Advice": "동일 배치 승인된 Keypad App/Tips와 동일 기능 의미 중복",
 "Headline Advice": "동일 배치 승인된 Headline App/Tips와 동일 기능 의미 중복",
 "Toothbrush Advice": "동일 배치 승인된 Toothbrush App/Tips와 동일 기능 의미 중복",
 "Inspection Advice": "동일 배치 승인된 Inspection App/Tips와 동일 기능 의미 중복",
}
R = {
 "Notary Sample": "결합 불성립", "Mediation Cash": "결합 불성립",
 "Guardianship Levy": "결합 불성립", "Trademark Repository": "결합 불성립",
 "Patent Forecast": "예측 대상 불분명", "Copyright Invoice": "결합 불성립",
 "Sidewalk Workbook": "워크북 대상 불분명", "Snorkeling Mode": "기능 토글로 읽혀 제품 불분명",
 "Metronome Spec": "결합 불성립", "Workout Quantity": "수량 대상 불분명",
 "Payee Login": "결합 불성립", "Tanker Analysis": "분석 대상 불분명",
 "Deed Coach": "코칭 대상 불분명", "Policyholder Habit": "결합 불성립",
 "Migraine Badge": "결합 불성립", "Insomnia Tab": "결합 불성립",
 "Skydiving Advisory": "안내 대상 불분명", "Acne Petition": "결합 불성립",
 "Snowboarding Fee": "결합 불성립", "Eczema Item": "항목 대상 불분명",
 "Ziplining Cost": "활동 비용 근거 약함(Sledding Cost 기각 선례)",
 "Psoriasis Price": "가격 지칭 부자연", "Sledding Loan": "결합 불성립",
 "Vertigo Sum": "결합 불성립", "Diving Cash": "결합 불성립",
 "Arthritis Sale": "결합 불성립", "Sailing Allowance": "결합 불성립",
 "Menopause Tariff": "결합 불성립", "Rafting Margin": "결합 불성립",
 "Pregnancy Fine": "결합 불성립", "Climbing Link": "결합 불성립",
 "Fertility Rule": "결합 불성립", "Biking Category": "결합 불성립",
 "Thyroid Attribute": "결합 불성립", "Golf Serial": "결합 불성립",
 "Cholesterol Token": "결합 불성립", "Fishing Balance": "결합 불성립",
 "Hypertension Interest": "결합 불성립", "Camping Due": "결합 불성립",
 "Anemia Subsidy": "결합 불성립", "Glamping Advance": "결합 불성립",
 "Heartburn Penalty": "결합 불성립", "Stargazing Extension": "결합 불성립",
 "Constipation Trial": "결합 불성립", "Birdwatching Manual": "설명 대상 불분명",
 "Concussion Worksheet": "학습지 근거 약함", "Canyon Schematic": "회로도 어휘 부자연",
 "Sprain Layout": "결합 불성립", "Geyser Sketch": "제품성 불분명",
 "Fracture Outline": "제품성 불분명", "Fjord Rendering": "렌더링 대상 불분명",
 "Insulin Notification": "결합 불성립", "Savanna Kit": "키트 대상 불분명",
 "Tundra Count": "대상 불분명", "Prairie Message": "결합 불성립",
 "Marsh Total": "결합 불성립", "Cove Widget": "위젯 대상 불분명",
 "Cliff Repository": "결합 불성립", "Cavern Announcement": "결합 불성립",
 "Oasis Calculator": "계산 대상 불분명", "Dune Converter": "변환 대상 불분명",
 "Whale Generator": "생성 대상 불분명", "Dolphin Recorder": "기록 대상 불분명",
 "Penguin Estimator": "산출 대상 불분명", "Flamingo Checker": "검사 대상 불분명",
 "Turtle Detector": "탐지 대상 불분명", "Moose Timer": "결합 불성립",
 "Bison Workshop": "결합 불성립", "Reindeer Guardian": "감시 대상 불분명",
 "Cemetery Workbook": "워크북 대상 불분명", "Commission Mode": "기능 토글로 읽혀 제품 불분명",
 "Dispensing Spec": "결합 불성립", "Charter Quantity": "수량 대상 불분명",
 "Fuel Login": "결합 불성립", "Shift Analysis": "분석 대상 불분명",
 "Filtration Coach": "코칭 대상 불분명", "Masterkey Habit": "결합 불성립",
 "Bilingual Workbook": "워크북 대상 불분명", "Mileage Mode": "기능 토글로 읽혀 제품 불분명",
 "Editing Spec": "결합 불성립", "Toast Quantity": "수량 대상 불분명",
 "Deposit Login": "결합 불성립", "Turbidity Analysis": "분석 대상 불분명",
 "Foam Coach": "코칭 대상 불분명(Foam 계열 기각 선례)", "Washer Habit": "결합 불성립",
 "Lawyer Order": "결합 불성립", "Attorney Duty": "결합 불성립",
 "Court Graph": "그래프 대상 불분명", "Judge Comparison": "결합 불성립",
 "Jury Quote": "결합 불성립", "Lawsuit Height": "결합 불성립",
 "Divorce Timetable": "시간표 대상 불분명", "Priority Workbook": "워크북 대상 불분명",
 "Headhunter Mode": "기능 토글로 읽혀 제품 불분명", "Swag Spec": "결합 불성립",
 "Screening Quantity": "수량 대상 불분명(Screening 계열)", "Diner Login": "결합 불성립",
 "Tick Analysis": "분석 대상 불분명", "Molar Coach": "코칭 대상 불분명(Molar 계열)",
 "Toy Habit": "결합 불성립", "Custody Grid": "결합 불성립",
 "Immigration Planner": "계획 대상 불분명", "Notary Slot": "결합 불성립",
 "Mediation Sale": "결합 불성립", "Guardianship Due": "결합 불성립",
 "Trademark Announcement": "결합 불성립",
 "Nanny Workbook": "워크북 대상 불분명", "Sidewalk Mode": "기능 토글로 읽혀 제품 불분명",
 "Snorkeling Spec": "결합 불성립", "Metronome Quantity": "수량 대상 불분명",
 "Workout Login": "결합 불성립", "Payee Analysis": "분석 대상 불분명",
 "Tanker Coach": "코칭 대상 불분명", "Deed Habit": "결합 불성립",
 "Migraine Stub": "결합 불성립", "Insomnia Bulletin": "결합 불성립",
 "Skydiving Petition": "결합 불성립", "Acne Confirmation": "확인 대상 불분명",
 "Snowboarding Item": "항목 대상 불분명", "Eczema Unit": "결합 불성립",
 "Ziplining Price": "가격 지칭 부자연", "Psoriasis Fare": "결합 불성립",
 "Sledding Sum": "결합 불성립", "Vertigo Debt": "결합 불성립",
 "Diving Sale": "결합 불성립", "Arthritis Charge": "결합 불성립",
 "Sailing Tariff": "결합 불성립", "Menopause Value": "결합 불성립",
 "Rafting Fine": "결합 불성립", "Pregnancy Number": "수치 지칭 부자연",
 "Climbing Rule": "결합 불성립", "Fertility Detail": "결합 불성립",
 "Biking Attribute": "결합 불성립", "Thyroid Field": "결합 불성립",
 "Golf Token": "결합 불성립", "Cholesterol Signature": "결합 불성립",
 "Fishing Interest": "결합 불성립", "Hypertension Asset": "결합 불성립",
 "Camping Subsidy": "결합 불성립", "Anemia Discount": "결합 불성립",
 "Glamping Penalty": "결합 불성립", "Heartburn Markup": "결합 불성립",
 "Stargazing Trial": "결합 불성립", "Constipation Graph": "그래프 대상 불분명",
 "Birdwatching Worksheet": "학습지 근거 약함", "Concussion Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Canyon Layout": "결합 불성립", "Sprain Sketch": "제품성 불분명",
 "Geyser Outline": "지형은 공예 오트라인 대상 아님", "Fracture Rendering": "렌더링 대상 불분명",
 "Fjord Notification": "결합 불성립", "Insulin Kit": "키트 대상 불분명",
 "Savanna Count": "대상 불분명", "Tundra Message": "결합 불성립",
 "Prairie Total": "결합 불성립", "Marsh Widget": "위젯 대상 불분명",
 "Cove Repository": "결합 불성립", "Cliff Announcement": "결합 불성립",
 "Cavern Calculator": "계산 대상 불분명", "Oasis Converter": "변환 대상 불분명",
 "Dune Generator": "생성 대상 불분명", "Whale Recorder": "기록 대상 불분명",
 "Dolphin Estimator": "산출 대상 불분명", "Penguin Checker": "검사 대상 불분명",
 "Flamingo Detector": "탐지 대상 불분명", "Turtle Timer": "결합 불성립",
 "Moose Workshop": "결합 불성립", "Bison Guardian": "감시 대상 불분명",
 "Reindeer Helper": "결합 불성립",
 "Pricing Workbook": "워크북 대상 불분명", "Cemetery Mode": "기능 토글로 읽혀 제품 불분명",
 "Commission Spec": "결합 불성립", "Dispensing Quantity": "수량 대상 불분명",
 "Charter Login": "결합 불성립", "Fuel Analysis": "분석 대상 불분명",
 "Shift Coach": "코칭 대상 불분명", "Filtration Habit": "결합 불성립",
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
out = base + r"\_dec_c10.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
