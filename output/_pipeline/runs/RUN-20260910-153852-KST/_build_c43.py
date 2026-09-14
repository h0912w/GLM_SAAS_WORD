# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk42_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Truck App": (0.55, "트럭 운송·차량 관리 앱(실재)"),
 "Truck Tips": (0.55, "Truck App 승인 선례의 Tips 평행"),
 "Saxophone App": (0.55, "색소폰 학습·연주 보조 앱(Violin App 평행)"),
 "Saxophone Tips": (0.55, "Saxophone App 승인 선례의 Tips 평행"),
 "Equity App": (0.55, "주식 보상·지분 관리 앱(실재)"),
 "Equity Tips": (0.55, "Equity App 승인 선례의 Tips 평행"),
 "Dialect App": (0.55, "방언 학습·사전 앱(실재)"),
 "Landmark App": (0.55, "랜드마크 정보·탐색 앱(실재)"),
 "Honeymoon App": (0.55, "허니문 계획·예약 앱(Itinerary App 평행)"),
 "Intermodal App": (0.55, "복합운송 화물 관리 앱(실재)"),
 "Retouching Tips": (0.55, "Retouching App 승인 선례의 Tips 평행"),
 "Quote Tips": (0.55, "Quote App 승인 선례의 Tips 평행"),
 "Lawsuit Timeline": (0.55, "소송 절차 타임라인 관리(Court Timetable 절차 명사 평행)"),
 "Lawsuit Reminder": (0.55, "소송 기한 알림 도구(Notification·Deadline 절차 명사 평행)"),
 "Birdwatching Tracker": (0.55, "조류 관찰 기록 추적(Birdwatching App 승인, eBird 류)"),
}

R_DUP = {
 "Timeline Advice": "이번 배치 승인 Timeline Tips와 동일 기능 의미 중복",
 "Termination Advice": "이번 배치 승인 Termination Tips와 동일 기능 의미 중복",
 "Signage Advice": "이번 배치 승인 Signage Tips와 동일 기능 의미 중복",
 "Retouching Advice": "이번 배치 승인 Retouching Tips와 동일 기능 의미 중복",
 "Quote Advice": "이번 배치 승인 Quote Tips와 동일 기능 의미 중복",
}

R = {
 "Concussion Tracker": "선례 기각(App 기각) 계열", "Canyon Hub": "선례 기각(App 기각) 계열",

 "Sprain Desk": "선례 기각(App 기각) 계열", "Geyser Radar": "선례 기각(App 기각) 계열",
 "Fracture Relay": "선례 기각(App 기각) 계열", "Fjord Vault": "선례 기각(App 기각) 계열",
 "Insulin Compass": "선례 기각(App 기각) 계열", "Savanna Beacon": "선례 기각(App 기각) 계열",
 "Tundra Forge": "선례 기각(App 기각) 계열", "Prairie Cascade": "선례 기각(App 기각) 계열",
 "Marsh Bridge": "선례 기각(App 기각) 계열", "Cove Signal": "선례 기각(App 기각) 계열",
 "Cliff Watch": "선례 기각(App 기각) 계열", "Cavern Scope": "선례 기각(App 기각) 계열",
 "Oasis Loop": "선례 기각(App 기각) 계열", "Dune Grid": "선례 기각(App 기각) 계열",
 "Whale Wave": "선례 기각(App 기각) 계열", "Dolphin Path": "선례 기각(App 기각) 계열",
 "Penguin Point": "선례 기각(App 기각) 계열", "Flamingo Map": "선례 기각(App 기각) 계열",
 "Turtle Frame": "선례 기각(App 기각) 계열", "Moose Base": "선례 기각(App 기각) 계열",
 "Bison Core": "선례 기각(App 기각) 계열", "Reindeer Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Utility Workbook": "선례 기각(App 기각) 계열", "Pump Mode": "기능 토글로 읽혀 제품 불분명",
 "Wax Spec": "사양 참조로 제품 불분명", "Drain Quantity": "수량 대상 불분명",
 "Cruise Login": "제품 불분명", "Violin Analysis": "분석 대상 불분명",
 "Expense Habit": "결합 불성립", "Retainer Workbook": "선례 기각(App 기각) 계열",
 "Title Spec": "선례 기각(App 기각) 계열", "Actuary Quantity": "선례 기각(App 기각) 계열",
 "Jobsite Analysis": "분석 대상 불분명", "Markdown Coach": "코칭 대상 불분명",
 "Itinerary Habit": "결합 불성립", "Lawyer Payment": "결제 지칭으로 제품 불분명(Notary Payment 기각 평행)",
 "Attorney Humidity": "결합 불성립", "Tile Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가",
 "Shine Advice": "선례 기각(App 상표 기각) 계열", "Nozzle Workbook": "선례 기각(App 기각) 계열",
 "Campsite Mode": "기능 토글로 읽혀 제품 불분명", "Viola Spec": "사양 참조로 제품 불분명",
 "Symptom Quantity": "수량 대상 불분명", "Debit Login": "제품 불분명",
 "Court Analysis": "선례 기각(App 기각) 계열", "Shipper Coach": "코칭 대상 불분명",
 "Counteroffer Habit": "결합 불성립", "Judge Center": "선례 기각(App 기각) 계열(Center 기각 라인)",
 "Jury Kiosk": "키오스크 지칭으로 제품 불분명", "Divorce Cost": "비용 결합 불성립",
 "Custody Interest": "이자·관심 중의로 불분명", "Immigration Generator": "생성 기능 지칭으로 제품 불분명",
 "Testament Reply": "회신 지칭으로 제품 불분명", "Notary Diary": "일지·잡지 중의로 불분명(Journal 기각 라인)",
 "Mediation Usage": "사용 지칭으로 제품 불분명", "Guardianship Tournament": "terrain 대상 결합 불성립",
 "Anemia App": "빈혈 상태 지칭으로 용도 불분명", "Damages Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Excavation Workbook": "워크북 대상 불분명", "Detention Mode": "선례 기각(App 기각) 계열",
 "Editor Quantity": "수량 대상 불분명", "Contact Login": "제품 불분명",
 "Portfolio Analysis": "분석 대상 불분명", "Headlight Habit": "결합 불성립",
 "Trademark Scope": "범위 지칭으로 제품 불분명", "Patent Trail": "선례 기각(App 기각) 계열(Trail 기각 라인)",
 "Copyright Booth": "부스 지칭으로 제품 불분명", "Migraine Inventory": "결합 불성립",
 "Insomnia Length": "결합 불성립(속성 지칭)", "Skydiving Limit": "결합 불성립",
 "Acne Type": "결합 불성립(분류 대상 부자연)", "Snowboarding Depth": "결합 불성립",
 "Eczema Height": "결합 불성립", "Ziplining Pressure": "결합 불성립",
 "Psoriasis Load": "결합 불성립", "Sledding Brightness": "결합 불성립",
 "Vertigo Frequency": "결합 불성립", "Diving Usage": "사용 지칭으로 제품 불분명",
 "Arthritis Condition": "상태 명사로 제품명 부자연", "Sailing Cycle": "주기 지칭으로 제품 불분명",
 "Menopause Breakdown": "내역·고장 중의로 불분명", "Rafting Followup": "후속 지칭으로 제품 불분명",
 "Pregnancy Approval": "승인 지칭으로 제품 불분명", "Climbing Questionnaire": "설문 대상 불분명",
 "Fertility Utilization": "활용 지칭으로 제품 불분명", "Biking Depreciation": "결합 불성립",
 "Thyroid Resignation": "결합 불성립", "Golf Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Cholesterol Tutorial": "terrain 대상 결합 불성립", "Fishing Opinion": "소견 대상 불분명",
 "Hypertension Gift": "결합 불성립", "Camping Flyer": "terrain 대상 결합 불성립",
 "Glamping Workbook": "워크북 대상 불분명", "Heartburn Mode": "선례 기각(App 기각) 계열",
 "Compensation Spec": "사양 참조로 제품 불분명", "Locksmith Quantity": "수량 대상 불분명",
 "Stargazing Login": "제품 불분명", "Constipation Analysis": "선례 기각(App 기각) 계열",
 "Testimony Coach": "코칭 대상 불분명", "Concussion Flow": "선례 기각(App 기각) 계열",
 "Canyon Desk": "선례 기각(App 기각) 계열", "Sprain Radar": "선례 기각(App 기각) 계열",
 "Geyser Relay": "선례 기각(App 기각) 계열", "Fracture Vault": "선례 기각(App 기각) 계열",
 "Fjord Compass": "선례 기각(App 기각) 계열", "Insulin Beacon": "선례 기각(App 기각) 계열",
 "Savanna Forge": "선례 기각(App 기각) 계열", "Tundra Cascade": "선례 기각(App 기각) 계열",
 "Prairie Bridge": "선례 기각(App 기각) 계열", "Marsh Signal": "선례 기각(App 기각) 계열",
 "Cove Watch": "선례 기각(App 기각) 계열", "Cliff Scope": "선례 기각(App 기각) 계열",
 "Cavern Loop": "선례 기각(App 기각) 계열", "Oasis Grid": "선례 기각(App 기각) 계열",
 "Dune Wave": "선례 기각(App 기각) 계열", "Whale Path": "선례 기각(App 기각) 계열",
 "Dolphin Point": "선례 기각(App 기각) 계열", "Penguin Map": "선례 기각(App 기각) 계열",
 "Flamingo Frame": "선례 기각(App 기각) 계열", "Turtle Base": "선례 기각(App 기각) 계열",
 "Moose Core": "선례 기각(App 기각) 계열", "Bison Ledger": "선례 기각(App 기각) 계열(Ledger 기각 라인)",
 "Reindeer Board": "선례 기각(App 기각) 계열(Board 기각 라인)", "Timeline Workbook": "워크북 대상 불분명",
 "Utility Mode": "선례 기각(App 기각) 계열", "Pump Spec": "사양 참조로 제품 불분명",
 "Wax Quantity": "수량 대상 불분명", "Drain Login": "제품 불분명",
 "Cruise Analysis": "분석 대상 불분명", "Violin Coach": "코칭 대상 불분명",
 "Retainer Mode": "선례 기각(App 기각) 계열", "Title Quantity": "선례 기각(App 기각) 계열",
 "Actuary Login": "선례 기각(App 기각) 계열", "Jobsite Coach": "코칭 대상 불분명",
 "Markdown Habit": "결합 불성립", "Lawyer Verification": "결합 불성립(Notary Verification 기각 평행)",
 "Attorney Episode": "결합 불성립",
 "Tile Advice": "선례 기각(App 상표 기각) 계열", "Shine Workbook": "선례 기각(App 상표 기각) 계열",
 "Nozzle Mode": "선례 기각(App 기각) 계열", "Campsite Spec": "사양 참조로 제품 불분명",
 "Viola Quantity": "수량 대상 불분명", "Symptom Login": "제품 불분명",
 "Debit Analysis": "분석 대상 불분명", "Court Coach": "선례 기각(App 기각) 계열",
 "Shipper Habit": "결합 불성립", "Judge Zone": "선례 기각(App 기각) 계열(Zone 기각 라인)",
 "Jury Bay": "베이 지칭으로 제품 불분명", "Divorce Price": "가격 지칭으로 제품 불분명",
 "Custody Asset": "자산 지칭으로 제품 불분명", "Immigration Recorder": "기록 기능 지칭으로 제품 불분명",
 "Testament Account": "계정·기술 중의로 불분명", "Notary Refund": "환불 지칭으로 제품 불분명",
 "Mediation Condition": "상태 명사로 제품명 부자연", "Guardianship Flyer": "terrain 대상 결합 불성립",
 "Termination Workbook": "워크북 대상 불분명", "Excavation Mode": "기능 토글로 읽혀 제품 불분명",
 "Detention Spec": "선례 기각(App 기각) 계열", "Editor Login": "제품 불분명",
 "Contact Analysis": "분석 대상 불분명", "Portfolio Coach": "코칭 대상 불분명",
 "Trademark Loop": "선례 기각(App 기각) 계열(Loop 기각 라인)", "Patent Chain": "선례 기각(App 기각) 계열(Chain 기각 라인)",
 "Copyright Kiosk": "키오스크 지칭으로 제품 불분명", "Migraine Claim": "결합 불성립",
 "Insomnia Weight": "결합 불성립(속성 지칭)", "Skydiving Type": "결합 불성립(분류 대상 부자연)",
 "Acne Clock": "결합 불성립", "Snowboarding Height": "결합 불성립",
 "Eczema Width": "결합 불성립", "Ziplining Load": "결합 불성립",
 "Psoriasis Voltage": "결합 불성립", "Sledding Frequency": "결합 불성립",
 "Vertigo Compatibility": "상태 명사로 제품명 부자연", "Diving Condition": "상태 명사로 제품명 부자연",
 "Arthritis Humidity": "결합 불성립", "Sailing Breakdown": "내역·고장 중의로 불분명",
 "Menopause Sensor": "결합 불성립",
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
out = base + r"\_dec_c43.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
