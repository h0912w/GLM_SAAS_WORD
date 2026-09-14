# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk47_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Obituary App": (0.55, "부고 작성·게시 앱(실재)"),
 "Obituary Tips": (0.55, "Obituary App 승인 선례의 Tips 평행"),
 "Golf App": (0.55, "골프 스코어·부킹 관리 앱(실재)"),
 "Mattress App": (0.55, "매트리스 쇼핑·추천 앱(실재)"),
 "Mattress Tips": (0.55, "Mattress App 승인 선례의 Tips 평행"),
 "Mobility App": (0.55, "마이크로모빌리티·이동 서비스 앱(실재)"),
 "Massage Tips": (0.55, "Massage App 승인 선례의 Tips 평행"),
 "Testimonial Tips": (0.55, "Testimonial App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Package Advice": "이번 배치 승인 Package Tips와 동일 기능 의미 중복",
 "Massage Advice": "이번 배치 승인 Massage Tips와 동일 기능 의미 중복",
 "Testimonial Advice": "이번 배치 승인 Testimonial Tips와 동일 기능 의미 중복",
}

R = {
 "Damages Coach": "선례 기각(App 기각) 계열", "Signage Habit": "결합 불성립",
 "Glamping Tracker": "추적 대상 불분명", "Heartburn Flow": "선례 기각(App 기각) 계열",
 "Stargazing Radar": "탐지 기능 지칭으로 제품 불분명", "Constipation Relay": "선례 기각(App 기각) 계열",
 "Birdwatching Beacon": "비컨 지칭으로 제품 불분명", "Concussion Forge": "선례 기각(App 기각) 계열",
 "Canyon Bridge": "선례 기각(App 기각) 계열", "Sprain Signal": "선례 기각(App 기각) 계열",
 "Geyser Watch": "선례 기각(App 기각) 계열", "Fracture Scope": "선례 기각(App 기각) 계열",
 "Fjord Loop": "선례 기각(App 기각) 계열", "Insulin Grid": "선례 기각(App 기각) 계열",
 "Savanna Wave": "선례 기각(App 기각) 계열", "Tundra Path": "선례 기각(App 기각) 계열",
 "Prairie Point": "선례 기각(App 기각) 계열", "Marsh Map": "선례 기각(App 기각) 계열",
 "Cove Frame": "선례 기각(App 기각) 계열", "Cliff Base": "선례 기각(App 기각) 계열",
 "Cavern Core": "선례 기각(App 기각) 계열", "Oasis Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Dune Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Whale Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Dolphin Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Penguin Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Flamingo Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Turtle Terminal": "선례 기각(App 기각) 계열(Terminal 중의)",
 "Moose Center": "선례 기각(App 기각) 계열(Center 기각 라인)", "Bison Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)",
 "Reindeer Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)", "Crew Mode": "기능 토글로 읽혀 제품 불분명",
 "Equipment Spec": "사양 참조로 제품 불분명", "Refrigerant Quantity": "수량 대상 불분명",
 "Deadbolt Login": "제품 불분명", "Dialect Analysis": "분석 대상 불분명",
 "Truck Coach": "코칭 대상 불분명", "Retouching Habit": "결합 불성립",
 "Rehearsal Workbook": "워크북 대상 불분명", "Vacuum Spec": "사양 참조로 제품 불분명",
 "Dent Quantity": "선례 기각(App 기각) 계열", "Overflow Login": "선례 기각(App 기각) 계열",
 "Landmark Analysis": "분석 대상 불분명", "Saxophone Coach": "코칭 대상 불분명",
 "Lawyer Refund": "환불 지칭으로 제품 불분명(Notary Refund 기각 평행)", "Attorney Evaluation": "평가 대상 불분명",
 "Impressioning App": "인상 채득 전문 용어로 용도 불분명", "Capsule Advice": "선례 기각(App 기각) 계열",
 "Gauge Workbook": "선례 기각(App 기각) 계열", "Strike Mode": "선례 기각(App 기각) 계열",
 "Notarization Spec": "사양 참조로 제품 불분명", "Padding Quantity": "선례 기각(App 기각) 계열",
 "Booking Login": "선례 기각(App 상표 기각) 계열", "Honeymoon Analysis": "분석 대상 불분명",
 "Tile Habit": "선례 기각(App 상표 기각) 계열", "Court Vault": "선례 기각(App 기각) 계열(Vault 기각 라인)",
 "Judge Chain": "선례 기각(App 기각) 계열(Chain 기각 라인)", "Jury Lobby": "로비·로비잉 중의로 불분명",
 "Lawsuit List": "목록 지칭으로 제품 불분명", "Divorce Sale": "판매 지칭으로 제품 불분명",
 "Custody Markup": "마크업(원가율·표준 언어) 중의로 불분명", "Immigration Stage": "단계 지칭으로 제품 불분명",
 "Testament Eligibility": "자격 지칭으로 제품 불분명", "Notary Length": "결합 불성립(속성 지칭)",
 "Mediation Approval": "승인 지칭으로 제품 불분명", "Balcony Advice": "선례 기각(App 기각) 계열",
 "Picnic Workbook": "선례 기각(App 상표 기각) 계열", "Tuning Mode": "기능 토글로 읽혀 제품 불분명",
 "Recovery Spec": "선례 기각(App 기각) 계열", "Guardianship Login": "선례 기각(App 기각) 계열",
 "Intermodal Analysis": "분석 대상 불분명", "Equity Coach": "코칭 대상 불분명",
 "Quote Habit": "결합 불성립", "Trademark Core": "선례 기각(App 기각) 계열(Core 기각 라인)",
 "Patent Assistant": "보조 기능 지칭으로 제품 불분명(Assistant 기각 라인)", "Copyright Passport": "여권 지칭으로 제품 불분명",
 "Migraine Limit": "결합 불성립", "Insomnia Depth": "결합 불성립",
 "Skydiving Pressure": "결합 불성립", "Acne Load": "결합 불성립",
 "Snowboarding Frequency": "결합 불성립", "Eczema Compatibility": "상태 명사로 제품명 부자연",
 "Ziplining Condition": "상태 명사로 제품명 부자연", "Psoriasis Humidity": "결합 불성립",
 "Sledding Breakdown": "내역·고장 중의로 불분명", "Vertigo Sensor": "결합 불성립",
 "Diving Approval": "승인 지칭으로 제품 불분명", "Arthritis Matrix": "행렬·매트릭스 중의로 불분명",
 "Sailing Utilization": "활용 지칭으로 제품 불분명", "Menopause Benefit": "혜택 지칭으로 제품 불분명",
 "Rafting Resignation": "결합 불성립", "Pregnancy Hazard": "결합 불성립",
 "Climbing Tutorial": "terrain 대상 결합 불성립", "Fertility Handbook": "terrain 대상 결합 불성립",
 "Biking Gift": "결합 불성립", "Thyroid Retreat": "terrain 대상 결합 불성립",
 "Cholesterol Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Bike Workbook": "워크북 대상 불분명",
 "Fishing Mode": "기능 토글로 읽혀 제품 불분명", "Hypertension Spec": "선례 기각(App 기각) 계열",
 "Negligence Quantity": "선례 기각(App 기각) 계열", "Mailbox Login": "제품 불분명",
 "Camping Analysis": "분석 대상 불분명", "Anemia Coach": "선례 기각(App 기각) 계열",
 "Damages Habit": "선례 기각(App 기각) 계열", "Glamping Flow": "기능 흐름 지칭으로 제품 불분명",
 "Heartburn Hub": "선례 기각(App 기각) 계열", "Stargazing Relay": "중계·교체 중의로 불분명",
 "Constipation Vault": "선례 기각(App 기각) 계열", "Birdwatching Forge": "선례 기각(App 기각) 계열",
 "Concussion Cascade": "선례 기각(App 기각) 계열", "Canyon Signal": "선례 기각(App 기각) 계열",
 "Sprain Watch": "선례 기각(App 기각) 계열", "Geyser Scope": "선례 기각(App 기각) 계열",
 "Fracture Loop": "선례 기각(App 기각) 계열", "Fjord Grid": "선례 기각(App 기각) 계열",
 "Insulin Wave": "선례 기각(App 기각) 계열", "Savanna Path": "선례 기각(App 기각) 계열",
 "Tundra Point": "선례 기각(App 기각) 계열", "Prairie Map": "선례 기각(App 기각) 계열",
 "Marsh Frame": "선례 기각(App 기각) 계열", "Cove Base": "선례 기각(App 기각) 계열",
 "Cliff Core": "선례 기각(App 기각) 계열", "Cavern Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Oasis Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Dune Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Whale Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Dolphin Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Penguin Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Flamingo Terminal": "선례 기각(App 기각) 계열(Terminal 중의)",
 "Turtle Center": "선례 기각(App 기각) 계열(Center 기각 라인)", "Moose Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)",
 "Bison Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)", "Reindeer Console": "선례 기각(App 기각) 계열(Console 기각 라인)",
 "Bypass App": "수술 우회로·네트워크 우회 중의로 용도 불분명", "Crew Spec": "사양 참조로 제품 불분명",
 "Equipment Quantity": "수량 대상 불분명", "Refrigerant Login": "제품 불분명",
 "Deadbolt Analysis": "분석 대상 불분명", "Dialect Coach": "코칭 대상 불분명",
 "Truck Habit": "결합 불성립", "Package Workbook": "워크북 대상 불분명",
 "Rehearsal Mode": "기능 토글로 읽혀 제품 불분명", "Vacuum Quantity": "수량 대상 불분명",
 "Dent Login": "선례 기각(App 기각) 계열", "Overflow Analysis": "선례 기각(App 기각) 계열",
 "Landmark Coach": "코칭 대상 불분명", "Saxophone Habit": "결합 불성립",
 "Lawyer Expense": "비용 결합 불성립", "Attorney Questionnaire": "설문 대상 불분명",
 "Capsule Workbook": "선례 기각(App 기각) 계열", "Gauge Mode": "선례 기각(App 기각) 계열",
 "Strike Spec": "선례 기각(App 기각) 계열", "Notarization Quantity": "수량 대상 불분명",
 "Padding Login": "선례 기각(App 기각) 계열", "Booking Analysis": "선례 기각(App 상표 기각) 계열",
 "Honeymoon Coach": "코칭 대상 불분명", "Court Compass": "선례 기각(App 기각) 계열(Compass 기각 라인)",
 "Judge Ring": "선례 기각(App 기각) 계열(Ring 중의)", "Jury Ticker": "전광판 지칭으로 제품 불분명",
 "Lawsuit Table": "표·테이블 중의로 불분명", "Divorce Charge": "요금·혐의 중의로 불분명",
 "Custody Redemption": "상환·구속 중의로 불분명", "Immigration Result": "결과 지칭으로 제품 불분명",
 "Testament Broadcast": "방송 지칭으로 제품 불분명", "Notary Weight": "결합 불성립(속성 지칭)",
 "Mediation Matrix": "행렬·매트릭스 중의로 불분명", "Impressioning Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Balcony Workbook": "선례 기각(App 기각) 계열", "Picnic Mode": "선례 기각(App 상표 기각) 계열",
 "Tuning Spec": "사양 참조로 제품 불분명", "Recovery Quantity": "선례 기각(App 기각) 계열",
 "Guardianship Analysis": "선례 기각(App 기각) 계열", "Intermodal Coach": "코칭 대상 불분명",
 "Equity Habit": "결합 불성립", "Trademark Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Patent Planner": "계획 대상 불분명(Planner 기각 라인)", "Copyright Lobby": "로비·로비잉 중의로 불분명",
 "Migraine Type": "결합 불성립(분류 대상 부자연)", "Insomnia Height": "결합 불성립",
 "Skydiving Load": "결합 불성립", "Acne Voltage": "결합 불성립",
 "Snowboarding Compatibility": "상태 명사로 제품명 부자연", "Eczema Capacity": "상태 명사로 제품명 부자연",
 "Ziplining Humidity": "결합 불성립", "Psoriasis Episode": "결합 불성립",
 "Sledding Sensor": "결합 불성립", "Vertigo Reception": "리셉션·수신 중의로 불분명",
 "Diving Matrix": "행렬·매트릭스 중의로 불분명",
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
out = base + r"\_dec_c48.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
