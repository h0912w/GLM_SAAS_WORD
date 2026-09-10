# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk47_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Divorce Assistant": (0.55, "이혼 절차 진행 보조(Divorce Manager 평행)"),
 "Notice App": (0.55, "행사 공지 앱(공지 보드 실재)"),
 "Exhaust Tips": (0.55, "배기 시스템 팁(App→Tips 평행)"),
 "Migraine Manual": (0.55, "편두통 관리 매뉴얼(Insomnia Manual 평행)"),
 "Skydiving Kit": (0.55, "스카이다이빙 장비 키트(Diving Kit 평행)"),
 "Psoriasis Recorder": (0.55, "건선 발작 기록(Vertigo Recorder 평행, PASI 추적 실재)"),
 "Cholesterol Guide": (0.55, "콜레스테롤 관리 가이드(Hypertension Guide 평행)"),
 "Provisioning App": (0.6, "사용자 프로비저닝 앱(IT 실재)"),
 "Queue Tips": (0.55, "대기열 운영 팁(App→Tips 평행)"),
 "Nutrition App": (0.7, "영양 관리 앱(대형 실재 시장)"),
 "Naptime Tips": (0.55, "낮잠 수립 팁(App→Tips 평행)"),
 "Photo App": (0.7, "사진 편집·관리 앱(대형 실재 시장)"),
 "Rating Tips": (0.55, "평점 수집 팁(App→Tips 평행)"),
 "Divorce Planner": (0.6, "이혼 절차 플래너(체크리스트 실재)"),
 "Notice Tips": (0.55, "공지 운영 팁(App→Tips 평행)"),
 "Eczema Calculator": (0.55, "아토피 EASI 점수 계산기(Psoriasis Calculator 평행, 임상 실재)"),
 "Climbing Forecast": (0.55, "산악 기상 예보(mountain-forecast 실재)"),
 "Golf Guide": (0.55, "골프 코스 가이드(실재 콘텐츠)"),
 "Threat App": (0.6, "위협 모니터링 앱(보안 실재)"),
 "Provisioning Tips": (0.55, "프로비저닝 팁(App→Tips 평행)"),
}
R_DUP = {
 "Bagel Advice": "동일 배치 승인된 Bagel App/Tips와 동일 기능 의미 중복",
 "Sourcing Advice": "동일 배치 승인된 Sourcing App/Tips와 동일 기능 의미 중복",
 "Interviewer Advice": "동일 배치 승인된 Interviewer App/Tips와 동일 기능 의미 중복",
 "Exhaust Advice": "동일 배치 승인된 Exhaust App/Tips와 동일 기능 의미 중복",
 "Pregnancy Record": "동일 배치 승인된 Pregnancy Recorder와 동일 기능 의미 중복",
 "Fertility Forecast": "동일 배치 승인된 Fertility Calculator와 기능 중복 우려(Fertility Estimator 기각 선례)",
 "Queue Advice": "동일 배치 승인된 Queue App/Tips와 동일 기능 의미 중복",
 "Staffing Advice": "동일 배치 승인된 Staffing App/Tips와 동일 기능 의미 중복",
}
R = {
 "Deworming Spec": "사양 참조로 제품 불분명", "Flossing Quantity": "수량 대상 불분명",
 "Storytime Login": "제품 불분명", "Sofa Analysis": "분석 대상 불분명",
 "Coloring Coach": "코칭 대상 불분명", "Ointment Habit": "결합 불성립",
 "Lawsuit Scope": "결합 불성립", "Custody Form": "결합 불성립(양식 단독으로 제품 불분명)",
 "Immigration Voucher": "결합 불성립", "Testament Tariff": "결합 불성립",
 "Notary Extension": "연장 대상 불분명", "Mediation Helper": "도우미 대상 불분명(Attorney Helper 기각 선례)",
 "Guardianship Match": "결합 불성립(Match 계열 기각 선례)", "Trademark Video": "결합 불성립",
 "Patent Voltage": "결합 불성립", "Copyright Guarantor": "결합 불성립",
 "Notice App SKIP": "", "Bloodwork Workbook": "워크북 대상 불분명",
 "Denture Mode": "기능 토글로 읽혀 제품 불분명", "Potty Spec": "사양 참조로 제품 불분명",
 "Trim Quantity": "수량 대상 불분명", "Counseling Login": "제품 불분명",
 "Capacitor Analysis": "분석 대상 불분명", "Keyless Coach": "코칭 대상 불분명",
 "Clubhouse Habit": "결합 불성립", "Insomnia Sketch": "제품성 불분명",
 "Acne Count": "카운트 대상 불분명", "Snowboarding Repository": "결합 불성립",
 "Eczema Announcement": "결합 불성립", "Ziplining Generator": "생성 대상 불분명",
 "Sledding Detector": "탐지 대상 불분명", "Vertigo Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Diving Helper": "도우미 대상 불분명(Sailing Helper 기각 선례)", "Arthritis Stage": "단계 대상 불분명",
 "Sailing Rank": "결합 불성립", "Menopause Trend": "결합 불성립(추이 대상 불분명, Pregnancy Trend 기각 선례)",
 "Rafting Guarantee": "결합 불성립", "Climbing Reference": "결합 불성립",
 "Biking Volume": "결합 불성립", "Thyroid Diagnostic": "진단 대상 불분명",
 "Golf Template": "결합 불성립", "Fishing Reply": "결합 불성립",
 "Hypertension Account": "결합 불성립", "Camping Validation": "결합 불성립",
 "Anemia Lookup": "탐색 대상 불분명", "Glamping Availability": "상태 명사로 제품명 부자연",
 "Heartburn Eligibility": "결합 불성립", "Stargazing Appointment": "약속 대상 불분명",
 "Constipation Feedback": "결합 불성립", "Birdwatching Quote": "인용·견적 중의로 대상 불분명",
 "Concussion Warranty": "결합 불성립", "Canyon Certification": "결합 불성립",
 "Sprain Nomination": "결합 불성립", "Geyser Correction": "결합 불성립",
 "Fracture Revision": "결합 불성립", "Fjord Payment": "결합 불성립",
 "Insulin Verification": "결합 불성립", "Savanna Simulator": "결합 불성립",
 "Tundra Predictor": "예측 대상 불분명", "Prairie Seal": "결합 불성립",
 "Marsh Review": "결합 불성립", "Cove Recipe": "결합 불성립",
 "Cliff Video": "결합 불성립", "Cavern Diary": "결합 불성립",
 "Oasis Refund": "결합 불성립", "Dune Expense": "결합 불성립",
 "Whale Newsletter": "결합 불성립", "Dolphin Inventory": "결합 불성립",
 "Penguin Claim": "결합 불성립", "Flamingo Onboarding": "결합 불성립",
 "Turtle Checkin": "결합 불성립", "Moose Size": "결합 불성립",
 "Bison Length": "결합 불성립", "Reindeer Weight": "결합 불성립",
 "Provisioning App SKIP": "", "Badge Workbook": "워크북 대상 불분명",
 "Trade Mode": "기능 토글로 읽혀 제품 불분명", "Treatment Login": "제품 불분명",
 "Billing Coach": "코칭 대상 불분명", "Care Habit": "결합 불성립",
 "Nutrition App SKIP": "", "Termite Workbook": "워크북 대상 불분명",
 "Mowing Mode": "기능 토글로 읽혀 제품 불분명", "Turnover Spec": "사양 참조로 제품 불분명",
 "Intake Quantity": "수량 대상 불분명", "Preplanning Login": "제품 불분명",
 "Schedule Analysis": "분석 대상 불분명", "Consultation Coach": "코칭 대상 불분명",
 "Lawyer Subsidy": "결합 불성립", "Attorney Streak": "결합 불성립",
 "Court Invoice": "결합 불성립", "Judge Speed": "결합 불성립",
 "Jury Tutorial": "결합 불성립", "Photo App SKIP": "",
 "Wifi Workbook": "워크북 대상 불분명", "Diagnosis Mode": "기능 토글로 읽혀 제품 불분명",
 "Waiter Spec": "사양 참조로 제품 불분명", "Deworming Quantity": "수량 대상 불분명",
 "Flossing Login": "제품 불분명", "Storytime Analysis": "분석 대상 불분명",
 "Sofa Coach": "코칭 대상 불분명", "Coloring Habit": "결합 불성립",
 "Lawsuit Loop": "결합 불성립", "Custody Card": "결합 불성립",
 "Immigration Badge": "결합 불성립", "Testament Value": "결합 불성립",
 "Notary Trial": "결합 불성립", "Mediation Stage": "단계 대상 불분명",
 "Guardianship Validation": "결합 불성립", "Trademark Diary": "결합 불성립",
 "Patent Wattage": "결합 불성립", "Copyright Tuner": "결합 불성립",
 "Notice Tips SKIP": "", "Bagel Workbook": "워크북 대상 불분명",
 "Bloodwork Mode": "기능 토글로 읽혀 제품 불분명", "Denture Spec": "사양 참조로 제품 불분명",
 "Potty Quantity": "수량 대상 불분명", "Trim Login": "제품 불분명",
 "Counseling Analysis": "분석 대상 불분명", "Capacitor Coach": "코칭 대상 불분명",
 "Keyless Habit": "결합 불성립", "Migraine Worksheet": "학습지 근거 약함(Insomnia Worksheet 기각 선례)",
 "Insomnia Outline": "개요 대상 불분명", "Skydiving Count": "카운트 대상 불분명",
 "Acne Message": "메시지 대상 불분명", "Snowboarding Announcement": "결합 불성립",
 "Eczema Calculator SKIP": "", "Ziplining Recorder": "기록 대상 불분명",
 "Psoriasis Estimator": "산출 대상 불분명", "Sledding Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Vertigo Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Diving Stage": "단계 대상 불분명",
 "Arthritis Result": "결합 불성립", "Sailing Trend": "결합 불성립",
 "Menopause Comparison": "비교 대상 불분명", "Rafting Record": "기록 대상 불분명",
 "Pregnancy Copy": "결합 불성립", "Fertility Deadline": "결합 불성립",
 "Biking Diagnostic": "진단 대상 불분명", "Thyroid Progress": "진행 대상 불분명",
 "Cholesterol Rating": "평가 대상 불분명", "Fishing Account": "결합 불성립",
 "Hypertension Case": "결합 불성립(Case 계열 기각 선례)", "Camping Lookup": "탐색 대상 불분명",
 "Anemia Ping": "결합 불성립", "Glamping Eligibility": "결합 불성립",
 "Heartburn Broadcast": "결합 불성립", "Stargazing Feedback": "결합 불성립",
 "Constipation Invoice": "결합 불성립", "Birdwatching Warranty": "결합 불성립",
 "Concussion Deposit": "결합 불성립", "Canyon Nomination": "결합 불성립",
 "Sprain Correction": "결합 불성립", "Geyser Revision": "결합 불성립",
 "Fracture Payment": "결합 불성립", "Fjord Verification": "결합 불성립",
 "Insulin Simulator": "결합 불성립", "Savanna Predictor": "예측 대상 불분명",
 "Tundra Seal": "결합 불성립", "Prairie Review": "결합 불성립",
 "Marsh Recipe": "결합 불성립", "Cove Video": "결합 불성립",
 "Cliff Diary": "결합 불성립", "Cavern Refund": "결합 불성립",
 "Oasis Expense": "결합 불성립", "Dune Newsletter": "결합 불성립",
 "Whale Inventory": "결합 불성립", "Dolphin Claim": "결합 불성립",
 "Penguin Onboarding": "결합 불성립", "Flamingo Checkin": "결합 불성립",
 "Turtle Size": "결합 불성립", "Moose Length": "결합 불성립",
 "Bison Weight": "결합 불성립", "Reindeer Distance": "결합 불성립",
 "Threat App SKIP": "", "Sourcing Workbook": "워크북 대상 불분명",
 "Badge Mode": "기능 토글로 읽혀 제품 불분명", "Trade Spec": "사양 참조로 제품 불분명",
 "Treatment Analysis": "분석 대상 불분명",
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
out = base + r"\_dec_c47.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
