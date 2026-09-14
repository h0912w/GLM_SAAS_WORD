# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk45_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Tuning App": (0.55, "악기 조율 보조 앱(실재)"),
 "Tuning Tips": (0.55, "Tuning App 승인 선례의 Tips 평행"),
 "Fishing App": (0.55, "낚시 기록·포인트 관리 앱(실재, Fishbrain 류)"),
 "Fishing Tips": (0.55, "Fishing App 승인 선례의 Tips 평행"),
 "Rehearsal App": (0.55, "연습·리허설 일정 관리 앱(실재)"),
 "Bike App": (0.55, "자전거 라이드·정비 관리 앱(실재)"),
 "Notarization Tips": (0.55, "Notarization App 승인 선례의 Tips 평행"),
 "Crew Tips": (0.55, "Crew App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Equipment Advice": "이번 배치 승인 Equipment Tips와 동일 기능 의미 중복",
 "Vacuum Advice": "이번 배치 승인 Vacuum Tips와 동일 기능 의미 중복",
 "Notarization Advice": "이번 배치 승인 Notarization Tips와 동일 기능 의미 중복",
}

R = {
 "Saxophone Spec": "사양 참조로 제품 불분명", "Retainer Analysis": "선례 기각(App 기각) 계열",
 "Title Habit": "선례 기각(App 기각) 계열", "Lawyer Review": "리뷰 대상 불분명(Notary Review 기각 평행)",
 "Attorney Reception": "리셉션·수신 중의로 불분명", "Strike App": "파업·타격 중의로 용도 불분명",
 "Padding Advice": "선례 기각(App 기각) 계열", "Booking Workbook": "선례 기각(App 상표 기각) 계열",
 "Honeymoon Mode": "기능 토글로 읽혀 제품 불분명", "Tile Quantity": "선례 기각(App 상표 기각) 계열",
 "Shine Login": "선례 기각(App 상표 기각) 계열", "Nozzle Analysis": "선례 기각(App 기각) 계열",
 "Campsite Coach": "코칭 대상 불분명", "Viola Habit": "결합 불성립",
 "Court Hub": "선례 기각(App 기각) 계열(Hub 기각 라인)", "Judge Scale": "저울·규모 중의로 불분명(Patent Scale 기각 평행)",
 "Jury Alert": "알림 기능 지칭으로 제품 불분명", "Lawsuit Order": "명령·주문 중의로 불분명",
 "Divorce Sum": "합계·요약 중의로 불분명", "Custody Discount": "할인 지칭으로 제품 불분명",
 "Immigration Timer": "타이머 지칭으로 제품 불분명", "Testament Lookup": "조회 기능 지칭으로 제품 불분명",
 "Notary Claim": "결합 불성립", "Mediation Breakdown": "내역·고장 중의로 불분명",
 "Recovery Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Guardianship Workbook": "선례 기각(App 기각) 계열",
 "Intermodal Mode": "기능 토글로 읽혀 제품 불분명", "Equity Spec": "사양 참조로 제품 불분명",
 "Quote Quantity": "수량 대상 불분명", "Termination Login": "제품 불분명",
 "Excavation Analysis": "분석 대상 불분명", "Detention Coach": "선례 기각(App 기각) 계열",
 "Trademark Point": "선례 기각(App 기각) 계열(Point 기각 라인)", "Patent Atlas": "지도집 지칭으로 제품 불분명",
 "Copyright Roster": "명단 지칭으로 제품 불분명", "Migraine Length": "결합 불성립(속성 지칭)",
 "Insomnia Type": "결합 불성립(분류 대상 부자연)", "Skydiving Depth": "결합 불성립",
 "Acne Height": "결합 불성립", "Snowboarding Load": "결합 불성립",
 "Eczema Voltage": "결합 불성립", "Ziplining Frequency": "결합 불성립",
 "Psoriasis Compatibility": "상태 명사로 제품명 부자연", "Sledding Condition": "상태 명사로 제품명 부자연",
 "Vertigo Humidity": "결합 불성립", "Diving Breakdown": "내역·고장 중의로 불분명",
 "Arthritis Sensor": "결합 불성립", "Sailing Approval": "승인 지칭으로 제품 불분명",
 "Menopause Matrix": "행렬·매트릭스 중의로 불분명", "Rafting Utilization": "활용 지칭으로 제품 불분명",
 "Pregnancy Benefit": "혜택 지칭으로 제품 불분명", "Climbing Resignation": "결합 불성립",
 "Fertility Hazard": "결합 불성립", "Biking Tutorial": "terrain 대상 결합 불성립",
 "Thyroid Handbook": "terrain 대상 결합 불성립", "Golf Gift": "결합 불성립",
 "Cholesterol Retreat": "terrain 대상 결합 불성립", "Hypertension Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Negligence Advice": "선례 기각(App 기각) 계열", "Mailbox Workbook": "워크북 대상 불분명",
 "Camping Mode": "기능 토글로 읽혀 제품 불분명", "Anemia Spec": "선례 기각(App 기각) 계열",
 "Damages Quantity": "선례 기각(App 기각) 계열", "Signage Login": "제품 불분명",
 "Glamping Analysis": "분석 대상 불분명", "Heartburn Coach": "선례 기각(App 기각) 계열",
 "Compensation Habit": "결합 불성립", "Stargazing Flow": "기능 흐름 지칭으로 제품 불분명",
 "Constipation Hub": "선례 기각(App 기각) 계열", "Birdwatching Relay": "중계·교체 중의로 불분명",
 "Concussion Vault": "선례 기각(App 기각) 계열", "Canyon Beacon": "선례 기각(App 기각) 계열",
 "Sprain Forge": "선례 기각(App 기각) 계열", "Geyser Cascade": "선례 기각(App 기각) 계열",
 "Fracture Bridge": "선례 기각(App 기각) 계열", "Fjord Signal": "선례 기각(App 기각) 계열",
 "Insulin Watch": "선례 기각(App 기각) 계열", "Savanna Scope": "선례 기각(App 기각) 계열",
 "Tundra Loop": "선례 기각(App 기각) 계열", "Prairie Grid": "선례 기각(App 기각) 계열",
 "Marsh Wave": "선례 기각(App 기각) 계열", "Cove Path": "선례 기각(App 기각) 계열",
 "Cliff Point": "선례 기각(App 기각) 계열", "Cavern Map": "선례 기각(App 기각) 계열",
 "Oasis Frame": "선례 기각(App 기각) 계열", "Dune Base": "선례 기각(App 기각) 계열",
 "Whale Core": "선례 기각(App 기각) 계열", "Dolphin Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Penguin Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Flamingo Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Turtle Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Moose Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Bison Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Reindeer Terminal": "선례 기각(App 기각) 계열(Terminal 중의)",
 "Refrigerant Workbook": "워크북 대상 불분명", "Deadbolt Mode": "기능 토글로 읽혀 제품 불분명",
 "Dialect Spec": "사양 참조로 제품 불분명", "Truck Quantity": "수량 대상 불분명",
 "Retouching Login": "제품 불분명", "Timeline Analysis": "분석 대상 불분명",
 "Utility Coach": "선례 기각(App 기각) 계열", "Pump Habit": "결합 불성립",
 "Vacuum Advice": "이번 배치 승인 Vacuum Tips와 동일 기능 의미 중복",
 "Dent Workbook": "선례 기각(App 기각) 계열", "Overflow Mode": "선례 기각(App 기각) 계열",
 "Landmark Spec": "사양 참조로 제품 불분명", "Saxophone Quantity": "수량 대상 불분명",
 "Retainer Coach": "선례 기각(App 기각) 계열", "Lawyer Recipe": "결합 불성립(Notary Recipe 기각 평행)",
 "Attorney Followup": "후속 지칭으로 제품 불분명", "Gauge App": "계기 지칭으로 용도 불분명",
 "Strike Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Padding Workbook": "선례 기각(App 기각) 계열", "Booking Mode": "선례 기각(App 상표 기각) 계열",
 "Honeymoon Spec": "사양 참조로 제품 불분명", "Tile Login": "선례 기각(App 상표 기각) 계열",
 "Shine Analysis": "선례 기각(App 상표 기각) 계열", "Nozzle Coach": "선례 기각(App 기각) 계열",
 "Campsite Habit": "결합 불성립", "Court Desk": "선례 기각(App 기각) 계열(Desk 기각 라인)",
 "Judge Route": "선례 기각(App 기각) 계열(Route 기각 라인)", "Jury Chart": "차트 지칭으로 제품 불분명",
 "Lawsuit Bill": "청구서·법안 중의로 불분명", "Divorce Debt": "부채 결합 불성립",
 "Custody Arrears": "체납 지칭으로 제품 불분명", "Immigration Workshop": "워크숍 대상 불분명",
 "Testament Ping": "핑 지칭으로 제품 불분명", "Notary Onboarding": "결합 불성립",
 "Mediation Sensor": "결합 불성립", "Picnic App": "식료품 배송 상표(Picnic) 중의로 불분명",
 "Guardianship Mode": "선례 기각(App 기각) 계열", "Intermodal Spec": "사양 참조로 제품 불분명",
 "Equity Quantity": "수량 대상 불분명", "Quote Login": "제품 불분명",
 "Termination Analysis": "분석 대상 불분명", "Excavation Coach": "코칭 대상 불분명",
 "Detention Habit": "선례 기각(App 기각) 계열", "Trademark Map": "선례 기각(App 기각) 계열(Map 기각 라인)",
 "Patent Keeper": "관리 기능 지칭으로 제품 불분명(Keeper 기각 라인)", "Copyright Alert": "알림 기능 지칭으로 제품 불분명",
 "Migraine Weight": "결합 불성립(속성 지칭)", "Insomnia Clock": "결합 불성립",
 "Skydiving Height": "결합 불성립", "Acne Width": "결합 불성립",
 "Snowboarding Voltage": "결합 불성립", "Eczema Wattage": "결합 불성립",
 "Ziplining Compatibility": "상태 명사로 제품명 부자연", "Psoriasis Capacity": "상태 명사로 제품명 부자연",
 "Sledding Humidity": "결합 불성립", "Vertigo Episode": "결합 불성립",
 "Diving Sensor": "결합 불성립", "Arthritis Reception": "리셉션·수신 중의로 불분명",
 "Sailing Matrix": "행렬·매트릭스 중의로 불분명", "Menopause Evaluation": "평가 대상 불분명",
 "Rafting Benefit": "혜택 지칭으로 제품 불분명", "Pregnancy Requirement": "요건 지칭으로 제품 불분명",
 "Climbing Hazard": "결합 불성립", "Fertility Guarantor": "보증인 명사 결합 불성립",
 "Biking Handbook": "terrain 대상 결합 불성립", "Thyroid Timetable": "terrain 대상 결합 불성립",
 "Golf Retreat": "terrain 대상 결합 불성립", "Cholesterol Tournament": "terrain 대상 결합 불성립",
 "Hypertension Advice": "선례 기각(App 기각) 계열",
 "Recovery Advice": "선례 기각(App 기각) 계열", "Negligence Workbook": "선례 기각(App 기각) 계열",
 "Mailbox Mode": "기능 토글로 읽혀 제품 불분명", "Camping Spec": "사양 참조로 제품 불분명",
 "Anemia Quantity": "선례 기각(App 기각) 계열", "Damages Login": "선례 기각(App 기각) 계열",
 "Signage Analysis": "분석 대상 불분명", "Glamping Coach": "코칭 대상 불분명",
 "Heartburn Habit": "선례 기각(App 기각) 계열", "Stargazing Hub": "선례 기각(App 기각) 계열",
 "Constipation Desk": "선례 기각(App 기각) 계열", "Birdwatching Vault": "선례 기각(App 기각) 계열",
 "Concussion Compass": "선례 기각(App 기각) 계열", "Canyon Forge": "선례 기각(App 기각) 계열",
 "Sprain Cascade": "선례 기각(App 기각) 계열", "Geyser Bridge": "선례 기각(App 기각) 계열",
 "Fracture Signal": "선례 기각(App 기각) 계열", "Fjord Watch": "선례 기각(App 기각) 계열",
 "Insulin Scope": "선례 기각(App 기각) 계열", "Savanna Loop": "선례 기각(App 기각) 계열",
 "Tundra Grid": "선례 기각(App 기각) 계열", "Prairie Wave": "선례 기각(App 기각) 계열",
 "Marsh Path": "선례 기각(App 기각) 계열", "Cove Point": "선례 기각(App 기각) 계열",
 "Cliff Map": "선례 기각(App 기각) 계열", "Cavern Frame": "선례 기각(App 기각) 계열",
 "Oasis Base": "선례 기각(App 기각) 계열",
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
out = base + r"\_dec_c46.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
