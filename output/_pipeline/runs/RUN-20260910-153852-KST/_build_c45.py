# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk44_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Equipment App": (0.55, "장비 대여·유지보수 관리 앱(실재)"),
 "Equipment Tips": (0.55, "Equipment App 승인 선례의 Tips 평행"),
 "Vacuum App": (0.55, "청소기·진공 관리 앱(실재)"),
 "Vacuum Tips": (0.55, "Vacuum App 승인 선례의 Tips 평행"),
 "Notarization App": (0.55, "온라인 공증 절차 앱(실재)"),
 "Crew App": (0.55, "크루 스케줄·인력 관리 앱(실재)"),
 "Mailbox Tips": (0.55, "Mailbox App 승인 선례의 Tips 평행"),
 "Refrigerant Tips": (0.55, "Refrigerant App 승인 선례의 Tips 평행"),
 "Stargazing Tracker": (0.55, "별 관측 추적 보조(Stargazing App 승인, SkyView 류)"),
}

R_DUP = {
 "Camping Advice": "이번 배치 승인 Camping Tips와 동일 기능 의미 중복",
 "Deadbolt Advice": "이번 배치 승인 Deadbolt Tips와 동일 기능 의미 중복",
 "Mailbox Advice": "이번 배치 승인 Mailbox Tips와 동일 기능 의미 중복",
 "Refrigerant Advice": "이번 배치 승인 Refrigerant Tips와 동일 기능 의미 중복",
}

R = {
 "Equity Workbook": "워크북 대상 불분명", "Quote Mode": "기능 토글로 읽혀 제품 불분명",
 "Termination Spec": "사양 참조로 제품 불분명", "Excavation Quantity": "수량 대상 불분명",
 "Detention Login": "선례 기각(App 기각) 계열", "Editor Coach": "코칭 대상 불분명",
 "Contact Habit": "결합 불성립", "Trademark Wave": "선례 기각(App 기각) 계열(Wave 기각 라인)",
 "Patent Gate": "게이트 지칭으로 제품 불분명", "Copyright Post": "게시물·부대 중의로 불분명",
 "Migraine Checkin": "결합 불성립", "Insomnia Range": "결합 불성립",
 "Skydiving Time": "결합 불성립", "Acne Speed": "결합 불성립",
 "Snowboarding Temperature": "결합 불성립", "Eczema Pressure": "결합 불성립",
 "Ziplining Wattage": "결합 불성립", "Psoriasis Brightness": "결합 불성립",
 "Sledding Capacity": "상태 명사로 제품명 부자연", "Vertigo Usage": "사용 지칭으로 제품 불분명",
 "Diving Episode": "결합 불성립", "Arthritis Cycle": "주기 지칭으로 제품 불분명",
 "Sailing Reception": "리셉션·수신 중의로 불분명", "Menopause Followup": "후속 지칭으로 제품 불분명",
 "Rafting Evaluation": "평가 대상 불분명", "Pregnancy Questionnaire": "설문 대상 불분명",
 "Climbing Requirement": "요건 지칭으로 제품 불분명", "Fertility Depreciation": "결합 불성립",
 "Biking Guarantor": "보증인 명사 결합 불성립", "Thyroid Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Golf Timetable": "terrain 대상 결합 불성립", "Cholesterol Opinion": "소견 대상 불분명",
 "Fishing Tournament": "terrain 대상 결합 불성립", "Hypertension Flyer": "terrain 대상 결합 불성립",
 "Negligence App": "법적 과실 상태 지칭으로 용도 불분명", "Anemia Workbook": "선례 기각(App 기각) 계열",
 "Damages Mode": "선례 기각(App 기각) 계열", "Signage Spec": "사양 참조로 제품 불분명",
 "Glamping Quantity": "수량 대상 불분명", "Heartburn Login": "선례 기각(App 기각) 계열",
 "Compensation Analysis": "분석 대상 불분명", "Locksmith Coach": "코칭 대상 불분명",
 "Stargazing Habit": "결합 불성립", "Constipation Tracker": "선례 기각(App 기각) 계열",
 "Birdwatching Desk": "책상·데스크 중의로 불분명", "Concussion Radar": "선례 기각(App 기각) 계열",
 "Canyon Vault": "선례 기각(App 기각) 계열", "Sprain Compass": "선례 기각(App 기각) 계열",
 "Geyser Beacon": "선례 기각(App 기각) 계열", "Fracture Forge": "선례 기각(App 기각) 계열",
 "Fjord Cascade": "선례 기각(App 기각) 계열", "Insulin Bridge": "선례 기각(App 기각) 계열",
 "Savanna Signal": "선례 기각(App 기각) 계열", "Tundra Watch": "선례 기각(App 기각) 계열",
 "Prairie Scope": "선례 기각(App 기각) 계열", "Marsh Loop": "선례 기각(App 기각) 계열",
 "Cove Grid": "선례 기각(App 기각) 계열", "Cliff Wave": "선례 기각(App 기각) 계열",
 "Cavern Path": "선례 기각(App 기각) 계열", "Oasis Point": "선례 기각(App 기각) 계열",
 "Dune Map": "선례 기각(App 기각) 계열", "Whale Frame": "선례 기각(App 기각) 계열",
 "Dolphin Base": "선례 기각(App 기각) 계열", "Penguin Core": "선례 기각(App 기각) 계열",
 "Flamingo Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)", "Turtle Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Moose Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Bison Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Reindeer Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Dialect Workbook": "워크북 대상 불분명", "Truck Mode": "기능 토글로 읽혀 제품 불분명",
 "Retouching Spec": "사양 참조로 제품 불분명", "Timeline Quantity": "수량 대상 불분명",
 "Utility Login": "선례 기각(App 기각) 계열", "Pump Analysis": "분석 대상 불분명",
 "Wax Coach": "코칭 대상 불분명", "Drain Habit": "결합 불성립",
 "Dent Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Overflow Advice": "선례 기각(App 기각) 계열",
 "Landmark Workbook": "워크북 대상 불분명", "Saxophone Mode": "기능 토글로 읽혀 제품 불분명",
 "Retainer Login": "선례 기각(App 기각) 계열", "Title Coach": "선례 기각(App 기각) 계열",
 "Actuary Habit": "선례 기각(App 기각) 계열", "Lawyer Seal": "인장·밀봉 중의로 불분명(Notary Seal 기각 평행)",
 "Attorney Sensor": "결합 불성립", "Padding Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Booking Advice": "선례 기각(App 상표 기각) 계열", "Honeymoon Workbook": "워크북 대상 불분명",
 "Tile Spec": "선례 기각(App 상표 기각) 계열", "Shine Quantity": "선례 기각(App 상표 기각) 계열",
 "Nozzle Login": "선례 기각(App 기각) 계열", "Campsite Analysis": "분석 대상 불분명",
 "Viola Coach": "코칭 대상 불분명", "Symptom Habit": "결합 불성립",
 "Court Flow": "선례 기각(App 기각) 계열(Flow 기각 라인)", "Judge Panel": "패널 지칭으로 제품 불분명",
 "Jury Roster": "명단 지칭으로 제품 불분명", "Lawsuit Estimate": "추정 지칭으로 제품 불분명",
 "Divorce Loan": "대출 결합 불성립", "Custody Subsidy": "보조금 지칭으로 제품 불분명",
 "Immigration Detector": "탐지 기능 지칭으로 제품 불분명", "Testament Validation": "검증 지칭으로 제품 불분명",
 "Notary Inventory": "재고 결합 불성립", "Mediation Cycle": "주기 지칭으로 제품 불분명",
 "Recovery App": "재활·데이터 복구 중의로 용도 불분명", "Guardianship Advice": "선례 기각(App 기각) 계열",
 "Intermodal Workbook": "워크북 대상 불분명", "Equity Mode": "기능 토글로 읽혀 제품 불분명",
 "Quote Spec": "사양 참조로 제품 불분명", "Termination Quantity": "수량 대상 불분명",
 "Excavation Login": "제품 불분명", "Detention Analysis": "선례 기각(App 기각) 계열",
 "Editor Habit": "결합 불성립", "Trademark Path": "선례 기각(App 기각) 계열(Path 기각 라인)",
 "Patent Nexus": "연결점 지칭으로 제품 불분명", "Copyright Harbor": "항구 지칭으로 제품 불분명",
 "Migraine Size": "결합 불성립(속성 지칭)", "Insomnia Limit": "결합 불성립",
 "Skydiving Speed": "결합 불성립", "Acne Depth": "결합 불성립",
 "Snowboarding Pressure": "결합 불성립", "Eczema Load": "결합 불성립",
 "Ziplining Brightness": "결합 불성립", "Psoriasis Frequency": "결합 불성립",
 "Sledding Usage": "사용 지칭으로 제품 불분명", "Vertigo Condition": "상태 명사로 제품명 부자연",
 "Diving Cycle": "주기 지칭으로 제품 불분명", "Arthritis Breakdown": "내역·고장 중의로 불분명",
 "Sailing Followup": "후속 지칭으로 제품 불분명", "Menopause Approval": "승인 지칭으로 제품 불분명",
 "Rafting Questionnaire": "설문 대상 불분명", "Pregnancy Utilization": "활용 지칭으로 제품 불분명",
 "Climbing Depreciation": "결합 불성립", "Fertility Resignation": "결합 불성립",
 "Biking Tuner": "튜너 기능 지칭으로 제품 불분명", "Thyroid Tutorial": "terrain 대상 결합 불성립",
 "Golf Opinion": "소견 대상 불분명", "Cholesterol Gift": "결합 불성립",
 "Fishing Flyer": "terrain 대상 결합 불성립", "Hypertension App": "고혈압 상태 지칭으로 용도 불분명",
 "Negligence Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Camping Workbook": "워크북 대상 불분명",
 "Anemia Mode": "선례 기각(App 기각) 계열", "Damages Spec": "선례 기각(App 기각) 계열",
 "Signage Quantity": "수량 대상 불분명", "Glamping Login": "제품 불분명",
 "Heartburn Analysis": "선례 기각(App 기각) 계열", "Compensation Coach": "코칭 대상 불분명",
 "Locksmith Habit": "결합 불성립", "Constipation Flow": "선례 기각(App 기각) 계열",
 "Birdwatching Radar": "탐지 기능 지칭으로 제품 불분명", "Concussion Relay": "선례 기각(App 기각) 계열",
 "Canyon Compass": "선례 기각(App 기각) 계열", "Sprain Beacon": "선례 기각(App 기각) 계열",
 "Geyser Forge": "선례 기각(App 기각) 계열", "Fracture Cascade": "선례 기각(App 기각) 계열",
 "Fjord Bridge": "선례 기각(App 기각) 계열", "Insulin Signal": "선례 기각(App 기각) 계열",
 "Savanna Watch": "선례 기각(App 기각) 계열", "Tundra Scope": "선례 기각(App 기각) 계열",
 "Prairie Loop": "선례 기각(App 기각) 계열", "Marsh Grid": "선례 기각(App 기각) 계열",
 "Cove Wave": "선례 기각(App 기각) 계열", "Cliff Path": "선례 기각(App 기각) 계열",
 "Cavern Point": "선례 기각(App 기각) 계열", "Oasis Map": "선례 기각(App 기각) 계열",
 "Dune Frame": "선례 기각(App 기각) 계열", "Whale Base": "선례 기각(App 기각) 계열",
 "Dolphin Core": "선례 기각(App 기각) 계열", "Penguin Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Flamingo Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Turtle Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Moose Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Bison Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Reindeer Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Deadbolt Workbook": "워크북 대상 불분명",
 "Dialect Mode": "기능 토글로 읽혀 제품 불분명", "Truck Spec": "사양 참조로 제품 불분명",
 "Retouching Quantity": "수량 대상 불분명", "Timeline Login": "제품 불분명",
 "Utility Analysis": "선례 기각(App 기각) 계열", "Pump Coach": "코칭 대상 불분명",
 "Wax Habit": "결합 불성립", "Dent Advice": "선례 기각(App 기각) 계열",
 "Overflow Workbook": "선례 기각(App 기각) 계열", "Landmark Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c45.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
