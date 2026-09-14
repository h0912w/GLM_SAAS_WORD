# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk49_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Estimate Tips": (0.55, "Estimate App 승인 선례의 Tips 평행"),
 "Haulage Tips": (0.55, "Haulage App 승인 선례의 Tips 평행"),
 "Kitten App": (0.55, "새끼 고양이 케어·성장 기록 앱(실재)"),
 "Kitten Tips": (0.55, "Kitten App 승인 선례의 Tips 평행"),
 "Patent Monitor": (0.55, "특허 출원·등록 감시 서비스(실재, Trademark Watch 평행)"),
}

R_DUP = {
 "Compost Advice": "이번 배치 승인 Compost Tips와 동일 기능 의미 중복",
 "Checklist Advice": "이번 배치 승인 Checklist Tips와 동일 기능 의미 중복",
 "Expiration Advice": "이번 배치 승인 Expiration Tips와 동일 기능 의미 중복",
 "Estimate Advice": "이번 배치 승인 Estimate Tips와 동일 기능 의미 중복",
 "Haulage Advice": "이번 배치 승인 Haulage Tips와 동일 기능 의미 중복",
 "Biking App": "이번 배치 승인 Bike App와 동일 기능 의미 중복",
}

R = {
 "Trademark Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Patent Companion": "도우미 기능 지칭으로 제품 불분명(Assistant 기각 라인)",
 "Copyright Line": "줄·라인 중의로 불분명", "Migraine Time": "결합 불성립",
 "Insomnia Temperature": "결합 불성립", "Skydiving Wattage": "결합 불성립",
 "Acne Brightness": "결합 불성립", "Snowboarding Usage": "사용 지칭으로 제품 불분명",
 "Eczema Condition": "상태 명사로 제품명 부자연", "Ziplining Cycle": "주기 지칭으로 제품 불분명",
 "Psoriasis Breakdown": "내역·고장 중의로 불분명", "Sledding Followup": "후속 지칭으로 제품 불분명",
 "Vertigo Approval": "승인 지칭으로 제품 불분명", "Diving Questionnaire": "설문 대상 불분명",
 "Arthritis Utilization": "활용 지칭으로 제품 불분명", "Sailing Depreciation": "결합 불성립",
 "Menopause Resignation": "결합 불성립", "Rafting Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Pregnancy Tutorial": "terrain 대상 결합 불성립", "Climbing Opinion": "소견 대상 불분명",
 "Fertility Gift": "결합 불성립", "Biking Flyer": "terrain 대상 결합 불성립",
 "Thyroid App": "갑상선 상태 지칭으로 용도 불분명(Cholesterol App 평행)",
 "Compost Workbook": "워크북 대상 불분명", "Golf Workbook": "워크북 대상 불분명",
 "Cholesterol Mode": "선례 기각(App 기각) 계열", "Bike Quantity": "수량 대상 불분명",
 "Fishing Login": "제품 불분명", "Hypertension Analysis": "선례 기각(App 기각) 계열",
 "Negligence Coach": "선례 기각(App 기각) 계열", "Mailbox Habit": "결합 불성립",
 "Camping Tracker": "추적 대상 불분명(Glamping Tracker 평행)", "Anemia Flow": "선례 기각(App 기각) 계열",
 "Glamping Radar": "선례 기각(App 기각) 계열", "Heartburn Relay": "선례 기각(App 기각) 계열",
 "Stargazing Beacon": "선례 기각(App 기각) 계열", "Constipation Forge": "선례 기각(App 기각) 계열",
 "Birdwatching Signal": "선례 기각(App 기각) 계열", "Concussion Watch": "선례 기각(App 기각) 계열",
 "Canyon Loop": "선례 기각(App 기각) 계열", "Sprain Grid": "선례 기각(App 기각) 계열",
 "Geyser Wave": "선례 기각(App 기각) 계열", "Fracture Path": "선례 기각(App 기각) 계열",
 "Fjord Point": "선례 기각(App 기각) 계열", "Insulin Map": "선례 기각(App 기각) 계열",
 "Savanna Frame": "선례 기각(App 기각) 계열", "Tundra Base": "선례 기각(App 기각) 계열",
 "Prairie Core": "선례 기각(App 기각) 계열", "Marsh Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Cove Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Cliff Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)",
 "Cavern Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Oasis Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)",
 "Dune Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Whale Terminal": "선례 기각(App 기각) 계열(Terminal 중의)",
 "Dolphin Center": "선례 기각(App 기각) 계열(Center 기각 라인)", "Penguin Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)",
 "Flamingo Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)", "Turtle Console": "선례 기각(App 기각) 계열(Console 기각 라인)",
 "Moose Panel": "패널 지칭으로 제품 불분명", "Bison Scale": "저울·규모 중의로 불분명",
 "Reindeer Route": "선례 기각(App 기각) 계열(Route 기각 라인)",
 "Obituary Mode": "기능 토글로 읽혀 제품 불분명", "Crew Analysis": "분석 대상 불분명",
 "Equipment Coach": "코칭 대상 불분명", "Refrigerant Habit": "결합 불성립",
 "Bypass Workbook": "선례 기각(App 기각) 계열", "Package Quantity": "수량 대상 불분명",
 "Rehearsal Login": "제품 불분명", "Vacuum Coach": "코칭 대상 불분명",
 "Dent Habit": "선례 기각(App 기각) 계열",
 "Crown Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Mobility Workbook": "워크북 대상 불분명",
 "Mattress Mode": "기능 토글로 읽혀 제품 불분명", "Massage Spec": "사양 참조로 제품 불분명",
 "Capsule Quantity": "선례 기각(App 기각) 계열", "Gauge Login": "선례 기각(App 기각) 계열",
 "Strike Analysis": "선례 기각(App 기각) 계열", "Notarization Coach": "코칭 대상 불분명",
 "Padding Habit": "선례 기각(App 기각) 계열", "Court Cascade": "선례 기각(App 기각) 계열(Cascade 기각 라인)",
 "Judge Atlas": "지도책 지칭으로 제품 불분명", "Jury Roll": "명부·굴리기 중의로 불분명",
 "Lawsuit Slot": "슬롯 지칭으로 제품 불분명", "Divorce Tariff": "관세·요율 중의로 불분명",
 "Custody Graph": "그래프 지칭으로 제품 불분명", "Immigration Trend": "추세 지칭으로 제품 불분명",
 "Testament Feedback": "피드백 지칭으로 제품 불분명", "Notary Limit": "결합 불성립(속성 지칭)",
 "Mediation Utilization": "활용 지칭으로 제품 불분명", "Mirror Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Impressioning Mode": "선례 기각(App 기각) 계열", "Testimonial Spec": "사양 참조로 제품 불분명",
 "Balcony Quantity": "선례 기각(App 기각) 계열", "Picnic Login": "선례 기각(App 상표 기각) 계열",
 "Tuning Analysis": "분석 대상 불분명", "Recovery Coach": "선례 기각(App 기각) 계열",
 "Guardianship Tracker": "선례 기각(App 기각) 계열", "Trademark Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Copyright Window": "창문·체감 기간 중의로 불분명", "Migraine Speed": "결합 불성립",
 "Insomnia Pressure": "결합 불성립", "Skydiving Brightness": "결합 불성립",
 "Acne Frequency": "결합 불성립", "Snowboarding Condition": "상태 명사로 제품명 부자연",
 "Eczema Humidity": "결합 불성립", "Ziplining Breakdown": "내역·고장 중의로 불분명",
 "Psoriasis Sensor": "결합 불성립", "Sledding Approval": "승인 지칭으로 제품 불분명",
 "Vertigo Matrix": "행렬·매트릭스 중의로 불분명", "Diving Utilization": "활용 지칭으로 제품 불분명",
 "Arthritis Benefit": "혜택 지칭으로 제품 불분명", "Sailing Resignation": "결합 불성립",
 "Menopause Hazard": "결합 불성립", "Rafting Tutorial": "terrain 대상 결합 불성립",
 "Pregnancy Handbook": "terrain 대상 결합 불성립", "Climbing Gift": "결합 불성립",
 "Fertility Retreat": "terrain 대상 결합 불성립", "Thyroid Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Golf Mode": "기능 토글로 읽혀 제품 불분명", "Cholesterol Spec": "선례 기각(App 기각) 계열",
 "Bike Login": "제품 불분명", "Fishing Analysis": "분석 대상 불분명",
 "Hypertension Coach": "선례 기각(App 기각) 계열", "Negligence Habit": "선례 기각(App 기각) 계열",
 "Camping Flow": "기능 흐름 지칭으로 제품 불분명", "Anemia Hub": "선례 기각(App 기각) 계열",
 "Glamping Relay": "선례 기각(App 기각) 계열", "Heartburn Vault": "선례 기각(App 기각) 계열",
 "Stargazing Forge": "선례 기각(App 기각) 계열", "Constipation Cascade": "선례 기각(App 기각) 계열",
 "Birdwatching Watch": "선례 기각(App 기각) 계열", "Concussion Scope": "선례 기각(App 기각) 계열",
 "Canyon Grid": "선례 기각(App 기각) 계열", "Sprain Wave": "선례 기각(App 기각) 계열",
 "Geyser Path": "선례 기각(App 기각) 계열", "Fracture Point": "선례 기각(App 기각) 계열",
 "Fjord Map": "선례 기각(App 기각) 계열", "Insulin Frame": "선례 기각(App 기각) 계열",
 "Savanna Base": "선례 기각(App 기각) 계열", "Tundra Core": "선례 기각(App 기각) 계열",
 "Prairie Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)", "Marsh Board": "선례 기각(App 기각) 계열(Board 기각 라인)",
 "Cove Deck": "선례 기각(App 기각) 계열(Deck 기각 라인)", "Cliff Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Cavern Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)", "Oasis Station": "선례 기각(App 기각) 계열(Station 기각 라인)",
 "Dune Terminal": "선례 기각(App 기각) 계열(Terminal 중의)", "Whale Center": "선례 기각(App 기각) 계열(Center 기각 라인)",
 "Dolphin Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)", "Penguin Portal": "선례 기각(App 기각) 계열(Portal 기각 라인)",
 "Flamingo Console": "선례 기각(App 기각) 계열(Console 기각 라인)", "Turtle Panel": "패널 지칭으로 제품 불분명",
 "Moose Scale": "저울·규모 중의로 불분명", "Bison Route": "선례 기각(App 기각) 계열(Route 기각 라인)",
 "Reindeer Rail": "선례 기각(App 기각) 계열(Rail 기각 라인)", "Checklist Workbook": "워크북 대상 불분명",
 "Obituary Spec": "사양 참조로 제품 불분명", "Crew Coach": "코칭 대상 불분명",
 "Equipment Habit": "결합 불성립", "Bunker App": "대피소·골프 벙커 중의로 용도 불분명",
 "Bypass Mode": "선례 기각(App 기각) 계열",
 "Package Login": "제품 불분명", "Rehearsal Analysis": "분석 대상 불분명",
 "Vacuum Habit": "결합 불성립", "Lawyer Claim": "클레임 지칭으로 제품 불분명",
 "Attorney Requirement": "요건 지칭으로 제품 불분명", "Lawyer Onboarding": "온보딩 지칭으로 제품 불분명",
 "Attorney Depreciation": "결합 불성립", "Cooler App": "보냉통·냉각기 중의로 용도 불분명",
 "Crown Advice": "선례 기각(App 기각) 계열", "Mobility Mode": "기능 토글로 읽혀 제품 불분명",
 "Mattress Spec": "사양 참조로 제품 불분명", "Massage Quantity": "수량 대상 불분명",
 "Capsule Login": "선례 기각(App 기각) 계열", "Gauge Analysis": "선례 기각(App 기각) 계열",
 "Strike Coach": "선례 기각(App 기각) 계열", "Notarization Habit": "결합 불성립",
 "Court Bridge": "선례 기각(App 기각) 계열(Bridge 기각 라인)", "Judge Keeper": "보관인 기능 지칭으로 제품 불분명(Keeper 기각 라인)",
 "Jury Report": "보고서 지칭으로 제품 불분명", "Lawsuit Pass": "통행증·패스 중의로 불분명",
 "Divorce Value": "가치 지칭으로 제품 불분명", "Custody Label": "라벨 지칭으로 제품 불분명",
 "Immigration Comparison": "비교 지칭으로 제품 불분명", "Testament Invoice": "청구서 지칭으로 제품 불분명",
 "Notary Type": "결합 불성립(분류 대상 부자연)", "Mediation Benefit": "혜택 지칭으로 제품 불분명",
 "Plaque App": "명판·치아 플라크·기념패 중의로 용도 불분명",
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
out = base + r"\_dec_c50.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
