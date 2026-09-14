# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk38_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Cruise App": (0.55, "크루즈 예약·일정 관리 앱(실재)"),
 "Cruise Tips": (0.55, "Cruise App 승인 선례의 Tips 평행"),
 "Debit App": (0.55, "체크카드 지출 관리 앱(실재)"),
 "Debit Tips": (0.55, "Debit App 승인 선례의 Tips 평행"),
 "Contact App": (0.55, "연락처 관리 앱(실재)"),
 "Drain App": (0.55, "배수 시설 점검·관리 앱(Plumbing App 평행)"),
 "Symptom App": (0.55, "증상 기록·확인 앱(실재)"),
 "Stargazing App": (0.55, "별 관측 보조 앱(실재, Birdwatching App 평행)"),
 "Violin Tips": (0.55, "Violin App 승인 선례의 Tips 평행"),
 "Portfolio Tips": (0.55, "Portfolio App 승인 선례의 Tips 평행"),
 "Jobsite Tips": (0.55, "Jobsite App 승인 선례의 Tips 평행"),
 "Testimony Tips": (0.55, "Testimony App 승인 선례의 Tips 평행"),
 "Insulin Tracker": (0.55, "인슐린 투여 추적 관리(Deadline Tracker 선례 평행)"),
 "Jury Calendar": (0.55, "배심 심리 일정 캘린더(Calendar 절차 명사 선례 평행)"),
 "Immigration Message": (0.55, "이민 관련 메시지 알림 관리(Message 절차 명사 선례 평행)"),
}

R_DUP = {
 "Markdown Advice": "이번 배치 승인 Markdown Tips와 동일 기능 의미 중복",
 "Shipper Advice": "이번 배치 승인 Shipper Tips와 동일 기능 의미 중복",
 "Violin Advice": "이번 배치 승인 Violin Tips와 동일 기능 의미 중복",
 "Jobsite Advice": "이번 배치 승인 Jobsite Tips와 동일 기능 의미 중복",
 "Testimony Advice": "이번 배치 승인 Testimony Tips와 동일 기능 의미 중복",
 "Debit Advice": "이번 배치 승인 Debit Tips와 동일 기능 의미 중복",
}

R = {
 "Acne Onboarding": "결합 불성립", "Snowboarding Weight": "결합 불성립(속성 지칭)",
 "Eczema Distance": "결합 불성립", "Ziplining Type": "결합 불성립(분류 대상 부자연)",
 "Psoriasis Clock": "결합 불성립", "Sledding Depth": "결합 불성립",
 "Vertigo Height": "결합 불성립", "Diving Pressure": "결합 불성립",
 "Arthritis Load": "결합 불성립", "Sailing Brightness": "결합 불성립",
 "Menopause Frequency": "결합 불성립", "Rafting Usage": "사용 지칭으로 제품 불분명",
 "Pregnancy Condition": "상태 명사로 제품명 부자연", "Climbing Cycle": "주기 지칭으로 제품 불분명",
 "Fertility Breakdown": "내역·고장 중의로 불분명", "Biking Followup": "후속 지칭으로 제품 불분명",
 "Thyroid Approval": "승인 지칭으로 제품 불분명", "Golf Questionnaire": "설문 대상 불분명",
 "Cholesterol Utilization": "활용 지칭으로 제품 불분명", "Fishing Depreciation": "결합 불성립",
 "Hypertension Resignation": "결합 불성립", "Camping Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Anemia Tutorial": "terrain 대상 결합 불성립", "Glamping Opinion": "소견 대상 불분명",
 "Heartburn Gift": "결합 불성립", "Stargazing Flyer": "terrain 대상 결합 불성립",
 "Constipation App": "변비 상태 지칭으로 용도 불분명", "Birdwatching Workbook": "워크북 대상 불분명",
 "Concussion Mode": "선례 기각(App 기각) 계열", "Canyon Quantity": "선례 기각(App 기각) 계열",
 "Sprain Login": "선례 기각(App 기각) 계열", "Geyser Analysis": "선례 기각(App 기각) 계열",
 "Fracture Coach": "선례 기각(App 기각) 계열", "Fjord Habit": "선례 기각(App 기각) 계열",
 "Savanna Flow": "선례 기각(App 기각) 계열", "Tundra Hub": "선례 기각(App 기각) 계열",
 "Prairie Desk": "선례 기각(App 기각) 계열", "Marsh Radar": "선례 기각(App 기각) 계열",
 "Cove Relay": "선례 기각(App 기각) 계열", "Cliff Vault": "선례 기각(App 기각) 계열",
 "Cavern Compass": "선례 기각(App 기각) 계열", "Oasis Beacon": "선례 기각(App 기각) 계열",
 "Dune Forge": "선례 기각(App 기각) 계열", "Whale Cascade": "선례 기각(App 기각) 계열",
 "Dolphin Bridge": "선례 기각(App 기각) 계열", "Penguin Signal": "선례 기각(App 기각) 계열",
 "Flamingo Watch": "선례 기각(App 기각) 계열", "Turtle Scope": "선례 기각(App 기각) 계열",
 "Moose Loop": "선례 기각(App 기각) 계열", "Bison Grid": "선례 기각(App 기각) 계열",
 "Reindeer Wave": "선례 기각(App 기각) 계열", "Expense Workbook": "워크북 대상 불분명",
 "Clause Mode": "기능 토글로 읽혀 제품 불분명", "Listing Quantity": "수량 대상 불분명",
 "Claim Login": "제품 불분명", "Roster Analysis": "분석 대상 불분명",
 "Subcontractor Coach": "코칭 대상 불분명", "Return Habit": "결합 불성립",
 "Itinerary Workbook": "워크북 대상 불분명", "Scholarship Mode": "기능 토글로 읽혀 제품 불분명",
 "Supplier Spec": "사양 참조로 제품 불분명", "Fertilizer Quantity": "수량 대상 불분명",
 "Outreach Analysis": "분석 대상 불분명", "Segment Habit": "선례 기각(App 상표 기각) 계열",
 "Lawyer Quote": "인용·견적 중의로 불분명(Notary Quote 기각 평행)", "Attorney Wattage": "결합 불성립",
 "Court Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Counteroffer Workbook": "워크북 대상 불분명",
 "Peril Mode": "선례 기각(App 기각) 계열", "Deduction Spec": "사양 참조로 제품 불분명",
 "Plumbing Quantity": "수량 대상 불분명", "Major Login": "선례 기각(App 기각) 계열",
 "Podcast Coach": "코칭 대상 불분명", "Channel Habit": "결합 불성립",
 "Judge Ledger": "원장 대상 불분명(Patent Ledger 기각 평행)", "Lawsuit File": "파일 대상 불분명",
 "Divorce Confirmation": "확인 지칭으로 제품 불분명", "Custody Field": "필드·분야 중의로 불분명",
 "Testament Diagnostic": "진단 대상 불분명", "Notary Verification": "결합 불성립",
 "Mediation Load": "결합 불성립", "Guardianship Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Headlight Workbook": "워크북 대상 불분명", "Brunch Mode": "기능 토글로 읽혀 제품 불분명",
 "Shelter Spec": "사양 참조로 제품 불분명", "Cleaning Quantity": "수량 대상 불분명",
 "Nap Login": "제품 불분명", "Shampoo Analysis": "분석 대상 불분명",
 "Refrigeration Coach": "코칭 대상 불분명", "Chiller Habit": "결합 불성립",
 "Trademark Compass": "나침반 지칭으로 제품 불분명", "Patent Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)",
 "Copyright Registry": "등록부 대상 불분명", "Migraine Review": "리뷰 대상 불분명",
 "Insomnia Expense": "결합 불성립", "Skydiving Onboarding": "결합 불성립",
 "Acne Checkin": "결합 불성립", "Snowboarding Distance": "결합 불성립",
 "Eczema Range": "결합 불성립", "Ziplining Clock": "결합 불성립",
 "Psoriasis Time": "결합 불성립", "Sledding Height": "결합 불성립",
 "Vertigo Width": "결합 불성립", "Diving Load": "결합 불성립",
 "Arthritis Voltage": "결합 불성립", "Sailing Frequency": "결합 불성립",
 "Menopause Compatibility": "상태 명사로 제품명 부자연", "Rafting Condition": "상태 명사로 제품명 부자연",
 "Pregnancy Humidity": "결합 불성립", "Climbing Breakdown": "내역·고장 중의로 불분명",
 "Fertility Sensor": "결합 불성립", "Biking Approval": "승인 지칭으로 제품 불분명",
 "Thyroid Matrix": "행렬·매트릭스 중의로 불분명", "Golf Utilization": "활용 지칭으로 제품 불분명",
 "Cholesterol Benefit": "혜택 지칭으로 제품 불분명", "Fishing Resignation": "결합 불성립",
 "Hypertension Hazard": "결합 불성립", "Camping Tutorial": "terrain 대상 결합 불성립",
 "Anemia Handbook": "terrain 대상 결합 불성립", "Glamping Gift": "결합 불성립",
 "Heartburn Retreat": "terrain 대상 결합 불성립", "Constipation Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Birdwatching Mode": "기능 토글로 읽혀 제품 불분명", "Concussion Spec": "선례 기각(App 기각) 계열",
 "Canyon Login": "선례 기각(App 기각) 계열", "Sprain Analysis": "선례 기각(App 기각) 계열",
 "Geyser Coach": "선례 기각(App 기각) 계열", "Fracture Habit": "선례 기각(App 기각) 계열",
 "Fjord Tracker": "선례 기각(App 기각) 계열", "Insulin Flow": "기능 토글로 읽혀 제품 불분명",
 "Savanna Hub": "선례 기각(App 기각) 계열", "Tundra Desk": "선례 기각(App 기각) 계열",
 "Prairie Radar": "선례 기각(App 기각) 계열", "Marsh Relay": "선례 기각(App 기각) 계열",
 "Cove Vault": "선례 기각(App 기각) 계열", "Cliff Compass": "선례 기각(App 기각) 계열",
 "Cavern Beacon": "선례 기각(App 기각) 계열", "Oasis Forge": "선례 기각(App 기각) 계열",
 "Dune Cascade": "선례 기각(App 기각) 계열", "Whale Bridge": "선례 기각(App 기각) 계열",
 "Dolphin Signal": "선례 기각(App 기각) 계열", "Penguin Watch": "선례 기각(App 기각) 계열",
 "Flamingo Scope": "선례 기각(App 기각) 계열", "Turtle Loop": "선례 기각(App 기각) 계열",
 "Moose Grid": "선례 기각(App 기각) 계열", "Bison Wave": "선례 기각(App 기각) 계열",
 "Reindeer Path": "선례 기각(App 기각) 계열", "Expense Mode": "기능 토글로 읽혀 제품 불분명",
 "Clause Spec": "사양 참조로 제품 불분명", "Listing Login": "제품 불분명",
 "Claim Analysis": "분석 대상 불분명", "Roster Coach": "코칭 대상 불분명",
 "Subcontractor Habit": "결합 불성립", "Markdown Workbook": "워크북 대상 불분명",
 "Itinerary Mode": "기능 토글로 읽혀 제품 불분명", "Scholarship Spec": "사양 참조로 제품 불분명",
 "Supplier Quantity": "수량 대상 불분명", "Fertilizer Login": "제품 불분명",
 "Outreach Coach": "코칭 대상 불분명", "Lawyer Warranty": "보증 결합 불성립", "Attorney Brightness": "결합 불성립",
 "Shipper Workbook": "워크북 대상 불분명", "Counteroffer Mode": "기능 토글로 읽혀 제품 불분명",
 "Peril Spec": "선례 기각(App 기각) 계열", "Deduction Quantity": "수량 대상 불분명",
 "Plumbing Login": "제품 불분명", "Major Analysis": "선례 기각(App 기각) 계열",
 "Podcast Habit": "결합 불성립", "Judge Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Jury Directory": "디렉터리 지칭으로 제품 불분명", "Lawsuit Level": "수준 지칭으로 제품 불분명",
 "Divorce Recap": "요약 대상 불분명", "Custody Format": "형식 지칭으로 제품 불분명",
 "Immigration Total": "합계 지칭으로 제품 불분명", "Testament Progress": "진행 지칭으로 제품 불분명(Progress 기각 라인)",
 "Notary Simulator": "시뮬레이터 결합 불성립", "Mediation Voltage": "결합 불성립",
 "Guardianship Tutorial": "terrain 대상 결합 불성립",
 "Actuary App": "계리사 직업 지칭으로 용도 불분명",
 "Court Advice": "선례 기각(App 기각) 계열",
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
out = base + r"\_dec_c39.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
