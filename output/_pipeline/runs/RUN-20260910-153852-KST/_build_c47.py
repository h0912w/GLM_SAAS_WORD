# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk46_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Package App": (0.55, "택배·물류 패키지 추적 앱(실재)"),
 "Package Tips": (0.55, "Package App 승인 선례의 Tips 평행"),
 "Massage App": (0.55, "마사지 예약·방문 서비스 앱(실재)"),
 "Testimonial App": (0.55, "고객 후기·추천사 수집 앱(실재)"),
 "Rehearsal Tips": (0.55, "Rehearsal App 승인 선례의 Tips 평행"),
 "Bike Tips": (0.55, "Bike App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Crew Advice": "이번 배치 승인 Crew Tips와 동일 기능 의미 중복",
 "Tuning Advice": "이번 배치 승인 Tuning Tips와 동일 기능 의미 중복",
 "Fishing Advice": "이번 배치 승인 Fishing Tips와 동일 기능 의미 중복",
 "Rehearsal Advice": "이번 배치 승인 Rehearsal Tips와 동일 기능 의미 중복",
 "Bike Advice": "이번 배치 승인 Bike Tips와 동일 기능 의미 중복",
}

R = {
 "Dune Core": "선례 기각(App 기각) 계열", "Whale Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Dolphin Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Penguin Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Flamingo Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Turtle Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Moose Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Bison Terminal": "선례 기각(App 기각) 계열(Terminal 중의)",
 "Reindeer Center": "선례 기각(App 기각) 계열(Center 기각 라인)", "Equipment Workbook": "워크북 대상 불분명",
 "Refrigerant Mode": "기능 토글로 읽혀 제품 불분명", "Deadbolt Spec": "사양 참조로 제품 불분명",
 "Dialect Quantity": "수량 대상 불분명", "Truck Login": "제품 불분명",
 "Retouching Analysis": "분석 대상 불분명", "Timeline Coach": "코칭 대상 불분명",
 "Utility Habit": "선례 기각(App 기각) 계열",
 "Vacuum Workbook": "워크북 대상 불분명", "Dent Mode": "선례 기각(App 기각) 계열",
 "Overflow Spec": "선례 기각(App 기각) 계열", "Landmark Quantity": "수량 대상 불분명",
 "Saxophone Login": "제품 불분명", "Retainer Habit": "선례 기각(App 기각) 계열",
 "Lawyer Video": "terrain 대상 결합 불성립", "Attorney Approval": "승인 지칭으로 제품 불분명",
 "Capsule App": "약·커피·호텔 캡슐 중의로 용도 불분명", "Gauge Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Strike Advice": "선례 기각(App 기각) 계열", "Notarization Workbook": "워크북 대상 불분명",
 "Padding Mode": "선례 기각(App 기각) 계열", "Booking Spec": "선례 기각(App 상표 기각) 계열",
 "Honeymoon Quantity": "수량 대상 불분명", "Tile Analysis": "선례 기각(App 상표 기각) 계열",
 "Shine Coach": "선례 기각(App 상표 기각) 계열", "Nozzle Habit": "선례 기각(App 기각) 계열",
 "Court Radar": "선례 기각(App 기각) 계열(Radar)", "Judge Rail": "선례 기각(App 기각) 계열(Rail 기각 라인)",
 "Jury Bin": "통·빈공간 중의로 불분명", "Lawsuit Receipt": "영수증 지칭으로 제품 불분명",
 "Divorce Fund": "펀드·기금 지칭으로 제품 불분명", "Custody Advance": "선금·전진 중의로 불분명",
 "Immigration Guardian": "보호자 지칭으로 제품 불분명", "Testament Model": "모범·모형 중의로 불분명",
 "Notary Checkin": "결합 불성립", "Mediation Reception": "리셉션·수신 중의로 불분명",
 "Balcony App": "발코니 지칭으로 용도 불분명", "Picnic Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가",
 "Recovery Workbook": "선례 기각(App 기각) 계열", "Guardianship Spec": "선례 기각(App 기각) 계열",
 "Intermodal Quantity": "수량 대상 불분명", "Equity Login": "제품 불분명",
 "Quote Analysis": "분석 대상 불분명", "Termination Coach": "코칭 대상 불분명",
 "Excavation Habit": "결합 불성립", "Trademark Frame": "선례 기각(App 기각) 계열(Frame 기각 라인)",
 "Patent Manager": "관리 기능 지칭으로 제품 불분명(Manager 기각 라인)", "Copyright Chart": "차트 지칭으로 제품 불분명",
 "Migraine Distance": "결합 불성립", "Insomnia Time": "결합 불성립",
 "Skydiving Width": "결합 불성립", "Acne Temperature": "결합 불성립",
 "Snowboarding Wattage": "결합 불성립", "Eczema Brightness": "결합 불성립",
 "Ziplining Capacity": "상태 명사로 제품명 부자연", "Psoriasis Usage": "사용 지칭으로 제품 불분명",
 "Sledding Episode": "결합 불성립", "Vertigo Cycle": "주기 지칭으로 제품 불분명",
 "Diving Reception": "리셉션·수신 중의로 불분명", "Arthritis Followup": "후속 지칭으로 제품 불분명",
 "Sailing Evaluation": "평가 대상 불분명", "Menopause Questionnaire": "설문 대상 불분명",
 "Rafting Requirement": "요건 지칭으로 제품 불분명", "Pregnancy Depreciation": "결합 불성립",
 "Climbing Guarantor": "보증인 명사 결합 불성립", "Fertility Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Biking Timetable": "terrain 대상 결합 불성립", "Thyroid Opinion": "소견 대상 불분명",
 "Golf Tournament": "terrain 대상 결합 불성립", "Cholesterol Flyer": "terrain 대상 결합 불성립",
 "Hypertension Workbook": "선례 기각(App 기각) 계열", "Negligence Mode": "선례 기각(App 기각) 계열",
 "Mailbox Spec": "사양 참조로 제품 불분명", "Camping Quantity": "수량 대상 불분명",
 "Anemia Login": "선례 기각(App 기각) 계열", "Damages Analysis": "선례 기각(App 기각) 계열",
 "Signage Coach": "코칭 대상 불분명", "Glamping Habit": "결합 불성립",
 "Heartburn Tracker": "선례 기각(App 기각) 계열", "Stargazing Desk": "책상·데스크 중의로 불분명",
 "Constipation Radar": "선례 기각(App 기각) 계열", "Birdwatching Compass": "나침반 지칭으로 제품 불분명",
 "Concussion Beacon": "선례 기각(App 기각) 계열", "Canyon Cascade": "선례 기각(App 기각) 계열",
 "Sprain Bridge": "선례 기각(App 기각) 계열", "Geyser Signal": "선례 기각(App 기각) 계열",
 "Fracture Watch": "선례 기각(App 기각) 계열", "Fjord Scope": "선례 기각(App 기각) 계열",
 "Insulin Loop": "선례 기각(App 기각) 계열", "Savanna Grid": "선례 기각(App 기각) 계열",
 "Tundra Wave": "선례 기각(App 기각) 계열", "Prairie Path": "선례 기각(App 기각) 계열",
 "Marsh Point": "선례 기각(App 기각) 계열", "Cove Map": "선례 기각(App 기각) 계열",
 "Cliff Frame": "선례 기각(App 기각) 계열", "Cavern Base": "선례 기각(App 기각) 계열",
 "Oasis Core": "선례 기각(App 기각) 계열", "Dune Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Whale Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Dolphin Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Penguin Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Flamingo Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Turtle Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Moose Terminal": "선례 기각(App 기각) 계열(Terminal 중의)",
 "Bison Center": "선례 기각(App 기각) 계열(Center 기각 라인)", "Reindeer Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)",
 "Crew Workbook": "워크북 대상 불분명", "Equipment Mode": "기능 토글로 읽혀 제품 불분명",
 "Refrigerant Spec": "사양 참조로 제품 불분명", "Deadbolt Quantity": "수량 대상 불분명",
 "Dialect Login": "제품 불분명", "Truck Analysis": "분석 대상 불분명",
 "Retouching Coach": "코칭 대상 불분명", "Timeline Habit": "결합 불성립",
 "Vacuum Mode": "기능 토글로 읽혀 제품 불분명", "Dent Spec": "선례 기각(App 기각) 계열",
 "Overflow Quantity": "선례 기각(App 기각) 계열", "Landmark Login": "제품 불분명",
 "Saxophone Analysis": "분석 대상 불분명", "Lawyer Diary": "일지·잡지 중의로 불분명(Journal 기각 라인)",
 "Attorney Matrix": "행렬·매트릭스 중의로 불분명", "Capsule Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Gauge Advice": "선례 기각(App 기각) 계열", "Tuning Workbook": "워크북 대상 불분명",
 "Strike Workbook": "선례 기각(App 기각) 계열", "Notarization Mode": "기능 토글로 읽혀 제품 불분명",
 "Padding Spec": "선례 기각(App 기각) 계열", "Booking Quantity": "선례 기각(App 상표 기각) 계열",
 "Honeymoon Login": "제품 불분명", "Tile Coach": "선례 기각(App 상표 기각) 계열",
 "Shine Habit": "선례 기각(App 상표 기각) 계열", "Court Relay": "선례 기각(App 기각) 계열(Relay 기각 라인)",
 "Judge Trail": "선례 기각(App 기각) 계열(Trail 기각 라인)", "Jury Passport": "여권 지칭으로 제품 불분명",
 "Lawsuit Code": "코드·법전 중의로 불분명", "Divorce Cash": "현금 지칭으로 제품 불분명",
 "Custody Penalty": "벌칙 지칭으로 제품 불분명", "Immigration Helper": "도우미 지칭으로 제품 불분명",
 "Testament Availability": "가용성 지칭으로 제품 불분명", "Notary Size": "결합 불성립(속성 지칭)",
 "Mediation Followup": "후속 지칭으로 제품 불분명",
 "Picnic Advice": "선례 기각(App 상표 기각) 계열",
 "Balcony Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Recovery Mode": "선례 기각(App 기각) 계열",
 "Guardianship Quantity": "선례 기각(App 기각) 계열", "Intermodal Login": "제품 불분명",
 "Equity Analysis": "분석 대상 불분명", "Quote Coach": "코칭 대상 불분명",
 "Termination Habit": "결합 불성립", "Trademark Base": "선례 기각(App 기각) 계열(Base 기각 라인)",
 "Patent Engine": "엔진 지칭으로 제품 불분명", "Copyright Bin": "통·빈공간 중의로 불분명",
 "Migraine Range": "결합 불성립", "Insomnia Speed": "결합 불성립",
 "Skydiving Temperature": "결합 불성립", "Acne Pressure": "결합 불성립",
 "Snowboarding Brightness": "결합 불성립", "Eczema Frequency": "결합 불성립",
 "Ziplining Usage": "사용 지칭으로 제품 불분명", "Psoriasis Condition": "상태 명사로 제품명 부자연",
 "Sledding Cycle": "주기 지칭으로 제품 불분명", "Vertigo Breakdown": "내역·고장 중의로 불분명",
 "Diving Followup": "후속 지칭으로 제품 불분명", "Arthritis Approval": "승인 지칭으로 제품 불분명",
 "Sailing Questionnaire": "설문 대상 불분명", "Menopause Utilization": "활용 지칭으로 제품 불분명",
 "Rafting Depreciation": "결합 불성립", "Pregnancy Resignation": "결합 불성립",
 "Climbing Tuner": "튜너 기능 지칭으로 제품 불분명", "Fertility Tutorial": "terrain 대상 결합 불성립",
 "Biking Opinion": "소견 대상 불분명", "Thyroid Gift": "결합 불성립",
 "Golf Flyer": "terrain 대상 결합 불성립", "Cholesterol App": "콜레스테롤 상태 지칭으로 용도 불분명",
 "Fishing Workbook": "워크북 대상 불분명", "Hypertension Mode": "선례 기각(App 기각) 계열",
 "Negligence Spec": "선례 기각(App 기각) 계열", "Mailbox Quantity": "수량 대상 불분명",
 "Camping Login": "제품 불분명", "Anemia Analysis": "선례 기각(App 기각) 계열",
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
out = base + r"\_dec_c47.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
