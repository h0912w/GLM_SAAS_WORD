# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk46_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Sourcing App": (0.65, "후보 소싱 앱(리크루팅 실재 시장)"),
 "Badge Tips": (0.55, "행사 명찰 운영 팁(App→Tips 평행)"),
 "Staffing App": (0.6, "인력 배치 스케줄 앱(실재)"),
 "Termite Tips": (0.55, "흰개미 점검 팁(App→Tips 평행)"),
 "Court Appointment": (0.55, "법원 출석 일정 알림(코트데이 리마인더 실재)"),
 "Interviewer App": (0.6, "면접관 일정·기록 앱(실재)"),
 "Wifi Tips": (0.55, "행사 와이파이 팁(App→Tips 평행)"),
 "Lawsuit Watch": (0.55, "소송 모니터링(리갈 워치 실재)"),
 "Custody Log": (0.55, "양육 일수 기록(공동양육 로그 실재)"),
 "Exhaust App": (0.55, "배기량 시뮬레이터 앱(자동차 애호가 실재)"),
 "Bagel Tips": (0.55, "베이글 운영 팁(App→Tips 평행)"),
 "Acne Kit": (0.55, "여드름 관리 키트(Eczema Kit 평행, 실재)"),
 "Arthritis Helper": (0.55, "관절염 통증 도우미(Menopause Helper 평행)"),
 "Queue App": (0.6, "고객 대기열 관리 앱(실재)"),
 "Sourcing Tips": (0.55, "소싱 팁(App→Tips 평행)"),
 "Naptime App": (0.65, "아기 낮잠 트래커 앱(실재 시장)"),
 "Staffing Tips": (0.55, "인력 운영 팁(App→Tips 평행)"),
 "Rating App": (0.6, "고객 평점 수집 앱(실재)"),
 "Interviewer Tips": (0.55, "면접 진행 팁(App→Tips 평행)"),
}
R_DUP = {
 "Trade Advice": "동일 배치 승인된 Trade App/Tips와 동일 기능 의미 중복",
 "Mowing Advice": "동일 배치 승인된 Mowing App/Tips와 동일 기능 의미 중복",
 "Diagnosis Advice": "동일 배치 승인된 Diagnosis App/Tips와 동일 기능 의미 중복",
 "Bloodwork Advice": "동일 배치 승인된 Bloodwork App/Tips와 동일 기능 의미 중복",
 "Badge Advice": "동일 배치 승인된 Badge App/Tips와 동일 기능 의미 중복",
 "Termite Advice": "동일 배치 승인된 Termite App/Tips와 동일 기능 의미 중복",
 "Wifi Advice": "동일 배치 승인된 Wifi App/Tips와 동일 기능 의미 중복",
}
R = {
 "Counseling Spec": "사양 참조로 제품 불분명", "Capacitor Quantity": "수량 대상 불분명",
 "Keyless Login": "제품 불분명", "Clubhouse Analysis": "분석 대상 불분명",
 "Skiing Coach": "코칭 대상 불분명", "Repertoire Habit": "결합 불성립",
 "Migraine Graph": "그래프 대상 불분명", "Insomnia Schematic": "도식 대상 불분명",
 "Skydiving Rendering": "결합 불성립", "Acne Notification": "알림 내용 불특정",
 "Snowboarding Total": "결합 불성립", "Eczema Widget": "결합 불성립",
 "Ziplining Calculator": "계산 대상 불분명(Rafting Calculator 기각 선례)",
 "Psoriasis Converter": "변환 대상 불분명", "Sledding Estimator": "산출 대상 불분명",
 "Vertigo Checker": "검사 대상 불분명(Climbing Checker 기각 선례)",
 "Diving Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Arthritis Guardian": "감시 대상 불분명",
 "Sailing Result": "결합 불성립", "Menopause Streak": "결합 불성립",
 "Rafting Comparison": "비교 대상 불분명", "Pregnancy Proposal": "제안 대상 불분명",
 "Climbing Copy": "결합 불성립", "Fertility Reading": "수치 대상 불분명(Anemia Reading 기각 선례)",
 "Biking Deadline": "결합 불성립", "Thyroid Duration": "결합 불성립",
 "Golf Progress": "진행 대상 불분명", "Cholesterol Authorization": "결합 불성립",
 "Fishing Rating": "평가 대상 불분명", "Hypertension Agreement": "결합 불성립",
 "Camping Case": "결합 불성립(Case 계열 기각 선례)", "Anemia Match": "결합 불성립(Match 계열 기각 선례)",
 "Glamping Ping": "결합 불성립", "Heartburn Model": "결합 불성립",
 "Stargazing Broadcast": "결합 불성립", "Constipation Barcode": "결합 불성립",
 "Birdwatching Invoice": "결합 불성립", "Concussion Renewal": "갱신 대상 불분명",
 "Canyon Warranty": "결합 불성립", "Sprain Deposit": "결합 불성립",
 "Geyser Certification": "결합 불성립", "Fracture Nomination": "결합 불성립",
 "Fjord Correction": "결합 불성립", "Insulin Revision": "결합 불성립",
 "Savanna Payment": "결합 불성립", "Tundra Verification": "결합 불성립",
 "Prairie Simulator": "결합 불성립", "Marsh Predictor": "예측 대상 불분명",
 "Cove Seal": "결합 불성립", "Cliff Review": "결합 불성립",
 "Cavern Recipe": "결합 불성립", "Oasis Video": "결합 불성립",
 "Dune Diary": "결합 불성립", "Whale Refund": "결합 불성립",
 "Dolphin Expense": "결합 불성립", "Penguin Newsletter": "결합 불성립",
 "Flamingo Inventory": "결합 불성립", "Turtle Claim": "결합 불성립",
 "Moose Onboarding": "결합 불성립", "Bison Checkin": "결합 불성립",
 "Reindeer Size": "결합 불성립", "Sourcing App SKIP": "",
 "Treatment Spec": "사양 참조로 제품 불분명", "Billing Login": "제품 불분명",
 "Care Analysis": "분석 대상 불분명", "Contract Coach": "코칭 대상 불분명",
 "Irrigation Habit": "결합 불성립", "Staffing App SKIP": "",
 "Turnover Workbook": "워크북 대상 불분명", "Intake Mode": "기능 토글로 읽혀 제품 불분명",
 "Preplanning Spec": "사양 참조로 제품 불분명", "Schedule Quantity": "수량 대상 불분명",
 "Consultation Login": "제품 불분명", "Certification Coach": "코칭 대상 불분명",
 "Reserve Habit": "결합 불성립", "Lawyer Levy": "결합 불성립",
 "Attorney Stage": "단계 대상 불분명(Sailing Stage 기각 선례)",
 "Judge Clock": "결합 불성립", "Jury Guarantor": "결합 불성립",
 "Interviewer App SKIP": "", "Waiter Workbook": "워크북 대상 불분명",
 "Deworming Mode": "기능 토글로 읽혀 제품 불분명", "Flossing Spec": "사양 참조로 제품 불분명",
 "Storytime Quantity": "수량 대상 불분명", "Sofa Login": "제품 불분명",
 "Coloring Analysis": "분석 대상 불분명", "Ointment Coach": "코칭 대상 불분명",
 "Humidifier Habit": "결합 불성립", "Divorce Engine": "결합 불성립",
 "Immigration Pass": "결합 불성립(통행증 중의)", "Testament Allowance": "결합 불성립",
 "Notary Redemption": "결합 불성립", "Mediation Guardian": "감시 대상 불분명",
 "Guardianship Case": "결합 불성립(Case 계열 기각 선례)", "Trademark Recipe": "결합 불성립",
 "Patent Load": "결합 불성립", "Copyright Hazard": "결합 불성립",
 "Exhaust App SKIP": "", "Denture Workbook": "워크북 대상 불분명",
 "Potty Mode": "기능 토글로 읽혀 제품 불분명", "Trim Spec": "사양 참조로 제품 불분명",
 "Counseling Quantity": "수량 대상 불분명", "Capacitor Login": "제품 불분명",
 "Keyless Analysis": "분석 대상 불분명", "Clubhouse Coach": "코칭 대상 불분명",
 "Skiing Habit": "결합 불성립", "Migraine Label": "결합 불성립",
 "Insomnia Layout": "결합 불성립", "Skydiving Notification": "알림 내용 불특정",
 "Acne Kit SKIP": "", "Snowboarding Widget": "결합 불성립",
 "Eczema Repository": "결합 불성립", "Ziplining Converter": "변환 대상 불분명",
 "Psoriasis Generator": "생성 대상 불분명", "Sledding Checker": "검사 대상 불분명",
 "Vertigo Detector": "탐지 대상 불분명", "Diving Guardian": "감시 대상 불분명",
 "Sailing Streak": "결합 불성립", "Menopause Rank": "결합 불성립",
 "Rafting Proposal": "제안 대상 불분명", "Pregnancy Guarantee": "결합 불성립",
 "Climbing Reading": "결합 불성립(Reading 계열 기각 선례)", "Fertility Reference": "결합 불성립",
 "Biking Duration": "결합 불성립", "Thyroid Volume": "결합 불성립",
 "Golf Authorization": "결합 불성립", "Cholesterol Template": "결합 불성립",
 "Fishing Agreement": "결합 불성립", "Hypertension Reply": "결합 불성립",
 "Camping Match": "결합 불성립(Match 계열 기각 선례)", "Anemia Validation": "결합 불성립",
 "Glamping Model": "결합 불성립", "Heartburn Availability": "상태 명사로 제품명 부자연",
 "Stargazing Barcode": "결합 불성립", "Constipation Appointment": "약속 대상 불분명",
 "Birdwatching Renewal": "갱신 대상 불분명", "Concussion Quote": "인용·견적 중의로 대상 불분명",
 "Canyon Deposit": "결합 불성립", "Sprain Certification": "결합 불성립",
 "Geyser Nomination": "결합 불성립", "Fracture Correction": "결합 불성립",
 "Fjord Revision": "결합 불성립", "Insulin Payment": "결합 불성립",
 "Savanna Verification": "결합 불성립", "Tundra Simulator": "결합 불성립",
 "Prairie Predictor": "예측 대상 불분명", "Marsh Seal": "결합 불성립",
 "Cove Review": "결합 불성립", "Cliff Recipe": "결합 불성립",
 "Cavern Video": "결합 불성립", "Oasis Diary": "결합 불성립",
 "Dune Refund": "결합 불성립", "Whale Expense": "결합 불성립",
 "Dolphin Newsletter": "결합 불성립", "Penguin Inventory": "결합 불성립",
 "Flamingo Claim": "결합 불성립", "Turtle Onboarding": "결합 불성립",
 "Moose Checkin": "결합 불성립", "Bison Size": "결합 불성립",
 "Reindeer Length": "결합 불성립", "Queue App SKIP": "",
 "Trade Workbook": "워크북 대상 불분명", "Treatment Quantity": "수량 대상 불분명",
 "Billing Analysis": "분석 대상 불분명", "Care Coach": "코칭 대상 불분명",
 "Contract Habit": "결합 불성립", "Naptime App SKIP": "",
 "Mowing Workbook": "워크북 대상 불분명", "Turnover Mode": "기능 토글로 읽혀 제품 불분명",
 "Intake Spec": "사양 참조로 제품 불분명", "Preplanning Quantity": "수량 대상 불분명",
 "Schedule Login": "제품 불분명", "Consultation Analysis": "분석 대상 불분명",
 "Certification Habit": "결합 불성립", "Lawyer Due": "결합 불성립",
 "Attorney Result": "결합 불성립", "Court Feedback": "결합 불성립",
 "Judge Time": "결합 불성립", "Jury Tuner": "결합 불성립",
 "Rating App SKIP": "", "Diagnosis Workbook": "워크북 대상 불분명",
 "Waiter Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c46.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
