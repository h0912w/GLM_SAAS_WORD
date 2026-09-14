# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk43_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Camping App": (0.55, "캠핑장 검색·예약 앱(Campsite App 평행)"),
 "Camping Tips": (0.55, "Camping App 승인 선례의 Tips 평행"),
 "Deadbolt App": (0.55, "스마트 데드볼트 잠금 관리 앱(실재)"),
 "Deadbolt Tips": (0.55, "Deadbolt App 승인 선례의 Tips 평행"),
 "Mailbox App": (0.55, "우편함·메일 관리 앱(실재)"),
 "Refrigerant App": (0.55, "냉매 사용 추적·규정 준수 앱(실재)"),
 "Dialect Tips": (0.55, "Dialect App 승인 선례의 Tips 평행"),
 "Landmark Tips": (0.55, "Landmark App 승인 선례의 Tips 평행"),
 "Honeymoon Tips": (0.55, "Honeymoon App 승인 선례의 Tips 평행"),
 "Intermodal Tips": (0.55, "Intermodal App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Truck Advice": "이번 배치 승인 Truck Tips와 동일 기능 의미 중복",
 "Saxophone Advice": "이번 배치 승인 Saxophone Tips와 동일 기능 의미 중복",
 "Equity Advice": "이번 배치 승인 Equity Tips와 동일 기능 의미 중복",
 "Dialect Advice": "이번 배치 승인 Dialect Tips와 동일 기능 의미 중복",
 "Landmark Advice": "이번 배치 승인 Landmark Tips와 동일 기능 의미 중복",
 "Honeymoon Advice": "이번 배치 승인 Honeymoon Tips와 동일 기능 의미 중복",
 "Intermodal Advice": "이번 배치 승인 Intermodal Tips와 동일 기능 의미 중복",
}

R = {
 "Rafting Approval": "승인 지칭으로 제품 불분명", "Pregnancy Matrix": "행렬·매트릭스 중의로 불분명",
 "Climbing Utilization": "활용 지칭으로 제품 불분명", "Fertility Benefit": "혜택 지칭으로 제품 불분명",
 "Biking Resignation": "결합 불성립", "Thyroid Hazard": "결합 불성립",
 "Golf Tutorial": "terrain 대상 결합 불성립", "Cholesterol Handbook": "terrain 대상 결합 불성립",
 "Fishing Gift": "결합 불성립", "Hypertension Retreat": "terrain 대상 결합 불성립",
 "Anemia Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Damages Advice": "선례 기각(App 기각) 계열",
 "Signage Workbook": "워크북 대상 불분명", "Glamping Mode": "기능 토글로 읽혀 제품 불분명",
 "Heartburn Spec": "선례 기각(App 기각) 계열", "Compensation Quantity": "수량 대상 불분명",
 "Locksmith Login": "제품 불분명", "Stargazing Analysis": "분석 대상 불분명",
 "Constipation Coach": "선례 기각(App 기각) 계열", "Testimony Habit": "결합 불성립",
 "Birdwatching Flow": "기능 흐름 지칭으로 제품 불분명", "Concussion Hub": "선례 기각(App 기각) 계열",
 "Canyon Radar": "선례 기각(App 기각) 계열", "Sprain Relay": "선례 기각(App 기각) 계열",
 "Geyser Vault": "선례 기각(App 기각) 계열", "Fracture Compass": "선례 기각(App 기각) 계열",
 "Fjord Beacon": "선례 기각(App 기각) 계열", "Insulin Forge": "선례 기각(App 기각) 계열",
 "Savanna Cascade": "선례 기각(App 기각) 계열", "Tundra Bridge": "선례 기각(App 기각) 계열",
 "Prairie Signal": "선례 기각(App 기각) 계열", "Marsh Watch": "선례 기각(App 기각) 계열",
 "Cove Scope": "선례 기각(App 기각) 계열", "Cliff Loop": "선례 기각(App 기각) 계열",
 "Cavern Grid": "선례 기각(App 기각) 계열", "Oasis Wave": "선례 기각(App 기각) 계열",
 "Dune Path": "선례 기각(App 기각) 계열", "Whale Point": "선례 기각(App 기각) 계열",
 "Dolphin Map": "선례 기각(App 기각) 계열", "Penguin Frame": "선례 기각(App 기각) 계열",
 "Flamingo Base": "선례 기각(App 기각) 계열", "Turtle Core": "선례 기각(App 기각) 계열",
 "Moose Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)", "Bison Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Reindeer Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Truck Workbook": "워크북 대상 불분명",
 "Retouching Workbook": "워크북 대상 불분명",
 "Timeline Mode": "기능 토글로 읽혀 제품 불분명", "Utility Spec": "선례 기각(App 기각) 계열",
 "Pump Quantity": "수량 대상 불분명", "Wax Login": "제품 불분명",
 "Drain Analysis": "분석 대상 불분명", "Cruise Coach": "코칭 대상 불분명",
 "Violin Habit": "결합 불성립", "Overflow App": "넘침·오버플로 중의로 용도 불분명",
 "Retainer Spec": "선례 기각(App 기각) 계열", "Title Login": "선례 기각(App 기각) 계열",
 "Actuary Analysis": "선례 기각(App 기각) 계열", "Jobsite Habit": "결합 불성립",
 "Lawyer Simulator": "시뮬레이터 결합 불성립(Notary Simulator 기각 평행)", "Attorney Cycle": "주기 지칭으로 제품 불분명",
 "Tile Workbook": "선례 기각(App 상표 기각) 계열", "Shine Mode": "선례 기각(App 상표 기각) 계열",
 "Nozzle Spec": "선례 기각(App 기각) 계열", "Campsite Quantity": "수량 대상 불분명",
 "Viola Login": "제품 불분명", "Symptom Analysis": "분석 대상 불분명",
 "Debit Coach": "코칭 대상 불분명", "Court Habit": "선례 기각(App 기각) 계열",
 "Judge Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)", "Jury Post": "게시물·부대 중의로 불분명",
 "Lawsuit Index": "색인·지수 중의로 불분명", "Divorce Fare": "요금 지칭으로 제품 불분명",
 "Custody Levy": "부과금 지칭으로 제품 불분명", "Immigration Estimator": "추정 기능 지칭으로 제품 불분명",
 "Testament Case": "사건·상자 중의로 불분명", "Notary Expense": "비용 결합 불성립",
 "Mediation Humidity": "결합 불성립", "Guardianship App": "후견 상태 지칭으로 용도 불분명",
 "Quote Workbook": "워크북 대상 불분명", "Termination Mode": "기능 토글로 읽혀 제품 불분명",
 "Excavation Spec": "사양 참조로 제품 불분명", "Detention Quantity": "선례 기각(App 기각) 계열",
 "Editor Analysis": "분석 대상 불분명", "Contact Coach": "코칭 대상 불분명",
 "Portfolio Habit": "결합 불성립", "Trademark Grid": "선례 기각(App 기각) 계열(Grid 기각 라인)",
 "Patent Ring": "반지·고리 중의로 불분명", "Copyright Bay": "베이 지칭으로 제품 불분명",
 "Migraine Onboarding": "결합 불성립", "Insomnia Distance": "결합 불성립",
 "Skydiving Clock": "결합 불성립", "Acne Time": "결합 불성립",
 "Snowboarding Width": "결합 불성립", "Eczema Temperature": "결합 불성립",
 "Ziplining Voltage": "결합 불성립", "Psoriasis Wattage": "결합 불성립",
 "Sledding Compatibility": "상태 명사로 제품명 부자연", "Vertigo Capacity": "상태 명사로 제품명 부자연",
 "Diving Humidity": "결합 불성립", "Arthritis Episode": "결합 불성립",
 "Sailing Sensor": "결합 불성립", "Menopause Reception": "리셉션·수신 중의로 불분명",
 "Rafting Matrix": "행렬·매트릭스 중의로 불분명", "Pregnancy Evaluation": "평가 대상 불분명",
 "Climbing Benefit": "혜택 지칭으로 제품 불분명", "Fertility Requirement": "요건 지칭으로 제품 불분명",
 "Biking Hazard": "결합 불성립", "Thyroid Guarantor": "보증인 명사 결합 불성립",
 "Golf Handbook": "terrain 대상 결합 불성립", "Cholesterol Timetable": "terrain 대상 결합 불성립",
 "Fishing Retreat": "terrain 대상 결합 불성립", "Hypertension Tournament": "terrain 대상 결합 불성립",
 "Anemia Advice": "선례 기각(App 기각) 계열", "Damages Workbook": "선례 기각(App 기각) 계열",
 "Signage Mode": "기능 토글로 읽혀 제품 불분명", "Glamping Spec": "사양 참조로 제품 불분명",
 "Heartburn Quantity": "선례 기각(App 기각) 계열", "Compensation Login": "제품 불분명",
 "Locksmith Analysis": "분석 대상 불분명", "Stargazing Coach": "코칭 대상 불분명",
 "Constipation Habit": "선례 기각(App 기각) 계열", "Birdwatching Hub": "선례 기각(App 기각) 계열",
 "Concussion Desk": "선례 기각(App 기각) 계열", "Canyon Relay": "선례 기각(App 기각) 계열",
 "Sprain Vault": "선례 기각(App 기각) 계열", "Geyser Compass": "선례 기각(App 기각) 계열",
 "Fracture Beacon": "선례 기각(App 기각) 계열", "Fjord Forge": "선례 기각(App 기각) 계열",
 "Insulin Cascade": "선례 기각(App 기각) 계열", "Savanna Bridge": "선례 기각(App 기각) 계열",
 "Tundra Signal": "선례 기각(App 기각) 계열", "Prairie Watch": "선례 기각(App 기각) 계열",
 "Marsh Scope": "선례 기각(App 기각) 계열", "Cove Loop": "선례 기각(App 기각) 계열",
 "Cliff Grid": "선례 기각(App 기각) 계열", "Cavern Wave": "선례 기각(App 기각) 계열",
 "Oasis Path": "선례 기각(App 기각) 계열", "Dune Point": "선례 기각(App 기각) 계열",
 "Whale Map": "선례 기각(App 기각) 계열", "Dolphin Frame": "선례 기각(App 기각) 계열",
 "Penguin Base": "선례 기각(App 기각) 계열", "Flamingo Core": "선례 기각(App 기각) 계열",
 "Turtle Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)", "Moose Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Bison Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Reindeer Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Retouching Mode": "기능 토글로 읽혀 제품 불분명", "Timeline Spec": "사양 참조로 제품 불분명",
 "Utility Quantity": "선례 기각(App 기각) 계열", "Pump Login": "제품 불분명",
 "Wax Analysis": "분석 대상 불분명", "Drain Coach": "코칭 대상 불분명",
 "Cruise Habit": "결합 불성립", "Dent App": "찌그러짐·치과 중의로 용도 불분명",
 "Overflow Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Booking App": "예약 플랫폼 상표(Booking.com) 중의로 불분명",
 "Saxophone Workbook": "워크북 대상 불분명", "Retainer Quantity": "선례 기각(App 기각) 계열",
 "Title Analysis": "선례 기각(App 기각) 계열", "Actuary Coach": "선례 기각(App 기각) 계열",
 "Lawyer Predictor": "예측 대상 불분명(Notary Predictor 기각 평행)", "Attorney Breakdown": "내역·고장 중의로 불분명",
 "Padding App": "충전재·여백 중의로 용도 불분명", "Booking Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가",
 "Tile Mode": "선례 기각(App 상표 기각) 계열", "Shine Spec": "선례 기각(App 상표 기각) 계열",
 "Nozzle Quantity": "선례 기각(App 기각) 계열", "Campsite Login": "제품 불분명",
 "Viola Analysis": "분석 대상 불분명", "Symptom Coach": "코칭 대상 불분명",
 "Debit Habit": "결합 불성립", "Court Tracker": "선례 기각(App 기각) 계열(Tracker 기각 라인)",
 "Judge Console": "선례 기각(App 기각) 계열(Console 기각 라인)", "Jury Harbor": "항구 지칭으로 제품 불분명",
 "Lawsuit Ticket": "티켓 지칭으로 제품 불분명", "Divorce Tax": "세금 결합 불성립",
 "Custody Due": "기한·당연 중의로 불분명", "Immigration Checker": "검사 기능 지칭으로 제품 불분명",
 "Testament Match": "매칭 대상 불분명", "Notary Newsletter": "결합 불성립",
 "Mediation Episode": "결합 불성립", "Guardianship Tips": "선례 기각(App 기각)의 Tips 평행 불가",
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
out = base + r"\_dec_c44.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
