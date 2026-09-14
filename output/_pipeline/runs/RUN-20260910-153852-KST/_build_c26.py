# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk25_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Streetlight App": (0.55, "가로등 점검·관리 앱(실재)"),
 "Streetlight Tips": (0.55, "Streetlight App 승인 선례의 Tips 평행"),
 "Satisfaction App": (0.55, "고객 만족도 조사·관리 앱(실재)"),
 "Satisfaction Tips": (0.55, "Satisfaction App 승인 선례의 Tips 평행"),
 "Meal App": (0.55, "식단 기록·계획 관리 앱(실재)"),
 "Meal Tips": (0.55, "Meal App 승인 선례의 Tips 평행"),
 "Suspension App": (0.55, "차량 서스펜션 정비 관리 앱(Wheel App 평행)"),
 "Backup App": (0.55, "데이터 백업·복원 관리 앱(실재)"),
 "Apostille App": (0.55, "아포스티유 인증 절차 관리 앱(실재)"),
 "Publisher Tips": (0.55, "Publisher App 승인 선례의 Tips 평행"),
 "Offer Tips": (0.55, "Offer App 승인 선례의 Tips 평행"),
 "Trademark Handbook": (0.55, "상표 등록 절차 핸드북(Patent Handbook 평행)"),
 "Trademark Timetable": (0.55, "상표 등록 절차 일정 관리(Judge Timetable 평행)"),
 "Arthritis Video": (0.55, "관절염 관리 영상 가이드(Hypertension Video 평행)"),
 "Arthritis Diary": (0.55, "관절염 증상 기록 일지(Hypertension Diary 평행)"),
 "Diving Video": (0.55, "다이빙 강습 영상 가이드(Golf Video 평행)"),
}

R_DUP = {
 "Salary Advice": "이번 배치 승인 Salary Tips와 동일 기능 의미 중복",
 "Publisher Advice": "이번 배치 승인 Publisher Tips와 동일 기능 의미 중복",
 "Offer Advice": "이번 배치 승인 Offer Tips와 동일 기능 의미 중복",
 "Sponsor Advice": "이번 배치 승인 Sponsor Tips와 동일 기능 의미 중복",
 "Invite Advice": "이번 배치 승인 Invite Tips와 동일 기능 의미 중복",
}

R = {
 "Cistern Spec": "사양 참조로 제품 불분명", "Souvenir Quantity": "수량 대상 불분명",
 "Trombone Login": "제품 불분명", "Savings Coach": "코칭 대상 불분명",
 "Judge Habit": "선례 기각(App 기각) 계열", "Jury Portal": "포털 지칭으로 제품 불분명",
 "Lawsuit Post": "게시물·우편 중의로 불분명", "Divorce Index": "색인·지수 중의로 불분명",
 "Custody Price": "가격 결합 불성립", "Immigration Asset": "자산 결합 불성립",
 "Testament Generator": "생성 도구 지칭으로 제품 불분명", "Notary Agreement": "계약서 문서 지칭으로 제품 불분명",
 "Mediation Recipe": "결합 불성립", "Guardianship Wattage": "결합 불성립",
 "Background Workbook": "선례 기각(App 기각) 계열", "Windshield Mode": "기능 토글로 읽혀 제품 불분명",
 "Bakery Spec": "사양 참조로 제품 불분명", "Exam Quantity": "수량 대상 불분명",
 "Sedation Login": "제품 불분명", "Playtime Analysis": "분석 대상 불분명",
 "Conditioner Coach": "코칭 대상 불분명", "Pickup Habit": "결합 불성립",
 "Patent Compass": "나침반 기능 지칭으로 제품 불분명", "Copyright Zone": "구역 지칭으로 제품 불분명",
 "Migraine Match": "매칭·경기 중의로 불분명", "Insomnia Availability": "상태 명사로 제품명 부자연",
 "Skydiving Appointment": "약속 대상 불분명", "Acne Feedback": "결합 불성립",
 "Snowboarding Warranty": "결합 불성립", "Eczema Deposit": "결합 불성립",
 "Ziplining Correction": "결합 불성립", "Psoriasis Revision": "결합 불성립",
 "Sledding Simulator": "결합 불성립", "Vertigo Predictor": "예측 대상 불분명",
 "Diving Recipe": "결합 불성립", "Sailing Expense": "결합 불성립",
 "Menopause Newsletter": "결합 불성립", "Rafting Onboarding": "결합 불성립",
 "Pregnancy Checkin": "결합 불성립", "Climbing Weight": "결합 불성립(속성 지칭)",
 "Fertility Distance": "결합 불성립", "Biking Type": "결합 불성립(분류 대상 부자연)",
 "Thyroid Clock": "결합 불성립", "Golf Depth": "결합 불성립",
 "Cholesterol Height": "결합 불성립", "Fishing Pressure": "결합 불성립",
 "Hypertension Load": "결합 불성립", "Camping Brightness": "결합 불성립",
 "Anemia Frequency": "결합 불성립", "Glamping Usage": "사용 지칭으로 제품 불분명",
 "Heartburn Condition": "상태 명사로 제품명 부자연", "Stargazing Cycle": "주기 지칭으로 제품 불분명",
 "Constipation Breakdown": "내역·고장 중의로 불분명", "Birdwatching Followup": "후속 지칭으로 제품 불분명",
 "Concussion Approval": "승인 지칭으로 제품 불분명", "Canyon Evaluation": "평가 대상 불분명",
 "Sprain Questionnaire": "설문 대상 불분명", "Geyser Utilization": "활용 지칭으로 제품 불분명",
 "Fracture Benefit": "혜택 지칭으로 제품 불분명", "Fjord Requirement": "요건 지칭으로 제품 불분명",
 "Insulin Depreciation": "결합 불성립", "Savanna Resignation": "결합 불성립",
 "Tundra Hazard": "결합 불성립", "Prairie Guarantor": "보증인 명사 결합 불성립",
 "Marsh Tuner": "튜너 기능 지칭으로 제품 불분명", "Cove Tutorial": "terrain 대상 결합 불성립",
 "Cliff Handbook": "terrain 대상 결합 불성립", "Cavern Timetable": "terrain 대상 결합 불성립",
 "Oasis Opinion": "terrain 대상 결합 불성립", "Dune Gift": "결합 불성립",
 "Whale Retreat": "동물 대상 결합 불성립", "Dolphin Tournament": "동물 대상 결합 불성립",
 "Penguin Flyer": "동물 대상 결합 불성립", "Flamingo App": "동물 지칭으로 제품 불분명",
 "Turtle Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Moose Advice": "선례 기각(App 기각) 계열",
 "Bison Workbook": "선례 기각(App 기각) 계열", "Reindeer Mode": "선례 기각(App 기각) 계열",
 "Reservation Mode": "기능 토글로 읽혀 제품 불분명", "Grooming Spec": "사양 참조로 제품 불분명",
 "Hygiene Quantity": "수량 대상 불분명", "Curriculum Analysis": "분석 대상 불분명",
 "Incident Coach": "코칭 대상 불분명", "Program App": "프로그램 대상 불분명(적립·방송·소프트웨어 중의)",
 "Loyalty Spec": "사양 참조로 제품 불분명", "Fleet Habit": "결합 불성립",
 "Lawyer Volume": "결합 불성립", "Attorney Refund": "결합 불성립",
 "Court Sensor": "결합 불성립", "Coping Mode": "기능 토글로 읽혀 제품 불분명",
 "Wheel Spec": "사양 참조로 제품 불분명", "Cistern Quantity": "수량 대상 불분명",
 "Souvenir Login": "제품 불분명", "Trombone Analysis": "분석 대상 불분명",
 "Savings Habit": "결합 불성립", "Judge Tracker": "선례 기각(App 기각) 계열",
 "Jury Console": "콘솔 중의로 불분명", "Lawsuit Harbor": "항구 지칭으로 제품 불분명",
 "Divorce Ticket": "티켓 중의로 불분명", "Custody Fare": "요금 결합 불성립",
 "Immigration Levy": "부과금 결합 불성립", "Testament Recorder": "녹음 도구 지칭으로 제품 불분명",
 "Notary Reply": "결합 불성립", "Mediation Video": "영상 대상 불분명(Attorney Video 기각 선례)",
 "Guardianship Brightness": "결합 불성립", "Patent Beacon": "신호 기능 지칭으로 제품 불분명",
 "Copyright Portal": "포털 지칭으로 제품 불분명", "Migraine Validation": "결합 불성립",
 "Insomnia Eligibility": "결합 불성립", "Skydiving Feedback": "결합 불성립",
 "Acne Invoice": "결합 불성립", "Snowboarding Deposit": "결합 불성립",
 "Eczema Certification": "결합 불성립", "Ziplining Revision": "결합 불성립",
 "Psoriasis Payment": "결합 불성립", "Sledding Predictor": "예측 대상 불분명",
 "Vertigo Seal": "결합 불성립", "Sailing Newsletter": "결합 불성립",
 "Menopause Inventory": "결합 불성립", "Rafting Checkin": "결합 불성립",
 "Pregnancy Size": "결합 불성립(속성 지칭)", "Climbing Distance": "결합 불성립",
 "Fertility Range": "결합 불성립", "Biking Clock": "결합 불성립",
 "Thyroid Time": "결합 불성립", "Golf Height": "결합 불성립",
 "Cholesterol Width": "결합 불성립", "Fishing Load": "결합 불성립",
 "Hypertension Voltage": "결합 불성립", "Camping Frequency": "결합 불성립",
 "Anemia Compatibility": "상태 명사로 제품명 부자연", "Glamping Condition": "상태 명사로 제품명 부자연",
 "Heartburn Humidity": "결합 불성립", "Stargazing Breakdown": "내역·고장 중의로 불분명",
 "Constipation Sensor": "결합 불성립", "Birdwatching Approval": "승인 지칭으로 제품 불분명",
 "Concussion Matrix": "행렬·매트릭스 중의로 불분명", "Canyon Questionnaire": "설문 대상 불분명",
 "Sprain Utilization": "활용 지칭으로 제품 불분명", "Geyser Benefit": "혜택 지칭으로 제품 불분명",
 "Fracture Requirement": "요건 지칭으로 제품 불분명", "Fjord Depreciation": "결합 불성립",
 "Insulin Resignation": "결합 불성립", "Savanna Hazard": "결합 불성립",
 "Tundra Guarantor": "보증인 명사 결합 불성립", "Prairie Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Marsh Tutorial": "terrain 대상 결합 불성립", "Cove Handbook": "terrain 대상 결합 불성립",
 "Cliff Timetable": "terrain 대상 결합 불성립", "Cavern Opinion": "terrain 대상 결합 불성립",
 "Oasis Gift": "결합 불성립", "Dune Retreat": "terrain 대상 결합 불성립",
 "Whale Tournament": "동물 대상 결합 불성립", "Dolphin Flyer": "동물 대상 결합 불성립",
 "Penguin App": "동물 지칭으로 제품 불분명", "Flamingo Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Turtle Advice": "선례 기각(App 기각) 계열", "Moose Workbook": "선례 기각(App 기각) 계열",
 "Bison Mode": "선례 기각(App 기각) 계열", "Reindeer Spec": "선례 기각(App 기각) 계열",
 "Sponsor Workbook": "워크북 대상 불분명", "Reservation Spec": "사양 참조로 제품 불분명",
 "Salary Workbook": "워크북 대상 불분명",
 "Grooming Quantity": "수량 대상 불분명", "Hygiene Login": "제품 불분명",
 "Curriculum Coach": "코칭 대상 불분명", "Incident Habit": "결합 불성립",
 "Meal Tips2": "", "Loyalty Quantity": "수량 대상 불분명",
 "Lawyer Diagnostic": "진단 대상 불분명", "Attorney Expense": "결합 불성립",
 "Court Reception": "리셉션·수신 중의로 불분명", "Invite Workbook": "워크북 대상 불분명",
 "Background Mode": "선례 기각(App 기각) 계열", "Windshield Spec": "사양 참조로 제품 불분명",
 "Bakery Quantity": "수량 대상 불분명", "Exam Login": "제품 불분명",
 "Sedation Analysis": "분석 대상 불분명", "Playtime Coach": "코칭 대상 불분명",
 "Conditioner Habit": "결합 불성립", "Backup Tips": (0.55, "Backup App 승인 선례의 Tips 평행"),
}
del R["Meal Tips2"]
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
out = base + r"\_dec_c26.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
