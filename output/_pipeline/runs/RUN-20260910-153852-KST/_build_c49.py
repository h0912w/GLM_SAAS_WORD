# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk48_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Compost App": (0.55, "퇴비화·음식물 쓰레기 관리 앱(실재)"),
 "Compost Tips": (0.55, "Compost App 승인 선례의 Tips 평행"),
 "Checklist App": (0.55, "체크리스트 작성·관리 앱(실재)"),
 "Checklist Tips": (0.55, "Checklist App 승인 선례의 Tips 평행"),
 "Expiration App": (0.55, "유통기한·만료일 관리 앱(실재)"),
 "Expiration Tips": (0.55, "Expiration App 승인 선례의 Tips 평행"),
 "Estimate App": (0.55, "공사·서비스 견적 산정 앱(실재, Quote App 평행)"),
 "Haulage App": (0.55, "화물 운송 관리 앱(실재)"),
 "Golf Tips": (0.55, "Golf App 승인 선례의 Tips 평행"),
 "Mobility Tips": (0.55, "Mobility App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Obituary Advice": "이번 배치 승인 Obituary Tips와 동일 기능 의미 중복",
 "Mattress Advice": "이번 배치 승인 Mattress Tips와 동일 기능 의미 중복",
 "Golf Advice": "이번 배치 승인 Golf Tips와 동일 기능 의미 중복",
 "Mobility Advice": "이번 배치 승인 Mobility Tips와 동일 기능 의미 중복",
}

R = {
 "Arthritis Evaluation": "평가 대상 불분명", "Sailing Benefit": "혜택 지칭으로 제품 불분명",
 "Menopause Requirement": "요건 지칭으로 제품 불분명", "Rafting Hazard": "결합 불성립",
 "Pregnancy Guarantor": "보증인 명사 결합 불성립", "Climbing Handbook": "terrain 대상 결합 불성립",
 "Fertility Timetable": "terrain 대상 결합 불성립", "Biking Retreat": "terrain 대상 결합 불성립",
 "Thyroid Tournament": "terrain 대상 결합 불성립", "Cholesterol Advice": "선례 기각(App 기각) 계열",
 "Bike Mode": "기능 토글로 읽혀 제품 불분명", "Fishing Spec": "사양 참조로 제품 불분명",
 "Hypertension Quantity": "선례 기각(App 기각) 계열", "Negligence Login": "선례 기각(App 기각) 계열",
 "Mailbox Analysis": "분석 대상 불분명", "Camping Coach": "코칭 대상 불분명",
 "Anemia Habit": "선례 기각(App 기각) 계열", "Glamping Hub": "선례 기각(App 기각) 계열",
 "Heartburn Desk": "선례 기각(App 기각) 계열", "Stargazing Vault": "선례 기각(App 기각) 계열",
 "Constipation Compass": "선례 기각(App 기각) 계열", "Birdwatching Cascade": "선례 기각(App 기각) 계열",
 "Concussion Bridge": "선례 기각(App 기각) 계열", "Canyon Watch": "선례 기각(App 기각) 계열",
 "Sprain Scope": "선례 기각(App 기각) 계열", "Geyser Loop": "선례 기각(App 기각) 계열",
 "Fracture Grid": "선례 기각(App 기각) 계열", "Fjord Wave": "선례 기각(App 기각) 계열",
 "Insulin Path": "선례 기각(App 기각) 계열", "Savanna Point": "선례 기각(App 기각) 계열",
 "Tundra Map": "선례 기각(App 기각) 계열", "Prairie Frame": "선례 기각(App 기각) 계열",
 "Marsh Base": "선례 기각(App 기각) 계열", "Cove Core": "선례 기각(App 기각) 계열",
 "Cliff Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)", "Cavern Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Oasis Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Dune Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Whale Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)", "Dolphin Station": "선례 기각(App 기각) 계열(Station 기각 라인)",
 "Penguin Terminal": "선례 기각(App 기각) 계열(Terminal 중의)", "Flamingo Center": "선례 기각(App 기각) 계열(Center 기각 라인)",
 "Turtle Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)", "Moose Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)",
 "Bison Console": "선례 기각(App 기각) 계열(Console 기각 라인)", "Bison Panel": "패널 지칭으로 제품 불분명",
 "Reindeer Panel": "패널 지칭으로 제품 불분명", "Crew Quantity": "수량 대상 불분명",
 "Equipment Login": "제품 불분명", "Refrigerant Analysis": "분석 대상 불분명",
 "Deadbolt Coach": "코칭 대상 불분명", "Dialect Habit": "결합 불성립",
 "Bypass Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Package Mode": "기능 토글로 읽혀 제품 불분명",
 "Rehearsal Spec": "사양 참조로 제품 불분명", "Vacuum Login": "제품 불분명",
 "Dent Analysis": "선례 기각(App 기각) 계열", "Overflow Coach": "선례 기각(App 기각) 계열",
 "Landmark Habit": "결합 불성립", "Lawyer Newsletter": "결합 불성립",
 "Attorney Utilization": "활용 지칭으로 제품 불분명", "Massage Workbook": "워크북 대상 불분명",
 "Capsule Mode": "선례 기각(App 기각) 계열", "Gauge Spec": "선례 기각(App 기각) 계열",
 "Strike Quantity": "선례 기각(App 기각) 계열", "Notarization Login": "제품 불분명",
 "Padding Analysis": "선례 기각(App 기각) 계열", "Booking Coach": "선례 기각(App 상표 기각) 계열",
 "Honeymoon Habit": "결합 불성립", "Court Beacon": "선례 기각(App 기각) 계열(Beacon 기각 라인)",
 "Judge Gate": "게이트 지칭으로 제품 불분명", "Jury Line": "줄·전화선 중의로 불분명",
 "Lawsuit Slip": "전표·미끄러짐 중의로 불분명", "Divorce Duty": "의무·관세 중의로 불분명",
 "Custody Extension": "연장 지칭으로 제품 불분명", "Immigration Streak": "연속 지칭으로 제품 불분명",
 "Testament Barcode": "바코드 지칭으로 제품 불분명", "Notary Distance": "결합 불성립(속성 지칭)",
 "Mediation Evaluation": "평가 대상 불분명", "Impressioning Advice": "선례 기각(App 기각) 계열",
 "Testimonial Workbook": "워크북 대상 불분명", "Balcony Mode": "선례 기각(App 기각) 계열",
 "Picnic Spec": "선례 기각(App 상표 기각) 계열", "Tuning Quantity": "수량 대상 불분명",
 "Recovery Login": "선례 기각(App 기각) 계열", "Guardianship Coach": "선례 기각(App 기각) 계열",
 "Intermodal Habit": "결합 불성립", "Trademark Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Patent Scheduler": "스케줄러 도구 지칭으로 제품 불분명(Scheduler 기각 라인)", "Copyright Ticker": "전광판 지칭으로 제품 불분명",
 "Migraine Clock": "결합 불성립", "Insomnia Width": "결합 불성립",
 "Skydiving Voltage": "결합 불성립", "Acne Wattage": "결합 불성립",
 "Snowboarding Capacity": "상태 명사로 제품명 부자연", "Eczema Usage": "사용 지칭으로 제품 불분명",
 "Ziplining Episode": "결합 불성립", "Psoriasis Cycle": "주기 지칭으로 제품 불분명",
 "Sledding Reception": "리셉션·수신 중의로 불분명", "Vertigo Followup": "후속 지칭으로 제품 불분명",
 "Diving Evaluation": "평가 대상 불분명", "Arthritis Questionnaire": "설문 대상 불분명",
 "Sailing Requirement": "요건 지칭으로 제품 불분명", "Menopause Depreciation": "결합 불성립",
 "Rafting Guarantor": "보증인 명사 결합 불성립", "Pregnancy Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Climbing Timetable": "terrain 대상 결합 불성립", "Fertility Opinion": "소견 대상 불분명",
 "Biking Tournament": "terrain 대상 결합 불성립", "Thyroid Flyer": "terrain 대상 결합 불성립",
 "Cholesterol Workbook": "선례 기각(App 기각) 계열", "Bike Spec": "사양 참조로 제품 불분명",
 "Fishing Quantity": "수량 대상 불분명", "Hypertension Login": "선례 기각(App 기각) 계열",
 "Negligence Analysis": "선례 기각(App 기각) 계열", "Mailbox Coach": "코칭 대상 불분명",
 "Camping Habit": "결합 불성립", "Anemia Tracker": "선례 기각(App 기각) 계열",
 "Glamping Desk": "책상·데스크 중의로 불분명", "Heartburn Radar": "선례 기각(App 기각) 계열",
 "Stargazing Compass": "나침반 지칭으로 제품 불분명", "Constipation Beacon": "선례 기각(App 기각) 계열",
 "Birdwatching Bridge": "선례 기각(App 기각) 계열", "Concussion Signal": "선례 기각(App 기각) 계열",
 "Canyon Scope": "선례 기각(App 기각) 계열", "Sprain Loop": "선례 기각(App 기각) 계열",
 "Geyser Grid": "선례 기각(App 기각) 계열", "Fracture Wave": "선례 기각(App 기각) 계열",
 "Fjord Path": "선례 기각(App 기각) 계열", "Insulin Point": "선례 기각(App 기각) 계열",
 "Savanna Map": "선례 기각(App 기각) 계열", "Tundra Frame": "선례 기각(App 기각) 계열",
 "Prairie Base": "선례 기각(App 기각) 계열", "Marsh Core": "선례 기각(App 기각) 계열",
 "Cove Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)", "Cliff Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Cavern Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Oasis Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Dune Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)", "Whale Station": "선례 기각(App 기각) 계열(Station 기각 라인)",
 "Dolphin Terminal": "선례 기각(App 기각) 계열(Terminal 중의)", "Penguin Center": "선례 기각(App 기각) 계열(Center 기각 라인)",
 "Flamingo Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)", "Turtle Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)",
 "Moose Console": "선례 기각(App 기각) 계열(Console 기각 라인)", "Reindeer Scale": "저울·규모 중의로 불분명",
 "Obituary Workbook": "워크북 대상 불분명", "Crew Login": "제품 불분명",
 "Equipment Analysis": "분석 대상 불분명", "Refrigerant Coach": "코칭 대상 불분명",
 "Deadbolt Habit": "결합 불성립",
 "Bypass Advice": "선례 기각(App 기각) 계열", "Package Spec": "사양 참조로 제품 불분명",
 "Rehearsal Quantity": "수량 대상 불분명", "Vacuum Analysis": "분석 대상 불분명",
 "Dent Coach": "선례 기각(App 기각) 계열", "Overflow Habit": "선례 기각(App 기각) 계열",
 "Lawyer Inventory": "재고 결합 불성립", "Attorney Benefit": "혜택 지칭으로 제품 불분명",
 "Crown App": "왕관·치아 크라운 중의로 용도 불분명", "Mattress Workbook": "워크북 대상 불분명",
 "Massage Mode": "기능 토글로 읽혀 제품 불분명", "Capsule Spec": "선례 기각(App 기각) 계열",
 "Gauge Quantity": "선례 기각(App 기각) 계열", "Strike Login": "선례 기각(App 기각) 계열",
 "Notarization Analysis": "분석 대상 불분명", "Padding Coach": "선례 기각(App 기각) 계열",
 "Booking Habit": "선례 기각(App 상표 기각) 계열", "Court Forge": "선례 기각(App 기각) 계열(Forge 기각 라인)",
 "Judge Nexus": "연결점 지칭으로 제품 불분명", "Jury Window": "창문·체감 기간 중의로 불분명",
 "Lawsuit Sample": "샘플 지칭으로 제품 불분명", "Divorce Allowance": "수당·용돈 중의로 불분명",
 "Custody Trial": "재판·시용 중의로 불분명", "Immigration Rank": "계급 지칭으로 제품 불분명",
 "Testament Appointment": "임명·약속 중의로 불분명", "Notary Range": "결합 불성립(속성 지칭)",
 "Mediation Questionnaire": "설문 대상 불분명", "Mirror App": "거울·화면 미러링 중의로 용도 불분명",
 "Impressioning Workbook": "선례 기각(App 기각) 계열", "Testimonial Mode": "기능 토글로 읽혀 제품 불분명",
 "Balcony Spec": "선례 기각(App 기각) 계열", "Picnic Quantity": "선례 기각(App 상표 기각) 계열",
 "Tuning Login": "제품 불분명", "Recovery Analysis": "선례 기각(App 기각) 계열",
 "Guardianship Habit": "선례 기각(App 기각) 계열",
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
out = base + r"\_dec_c49.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
