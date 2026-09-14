# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk34_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Shampoo App": (0.55, "샴푸 구매·추천 관리 앱(실재)"),
 "Shampoo Tips": (0.55, "Shampoo App 승인 선례의 Tips 평행"),
 "Claim App": (0.55, "보험 청구·클레임 접수 앱(실재)"),
 "Claim Tips": (0.55, "Claim App 승인 선례의 Tips 평행"),
 "Listing App": (0.55, "매물·상품 리스팅 관리 앱(실재)"),
 "Nap App": (0.55, "낮잠 기록·관리 앱(실재)"),
 "Court Timetable": (0.55, "법원 일정 관리 시간표(Deadline 절차 명사 선례 평행)"),
 "Refrigeration Tips": (0.55, "Refrigeration App 승인 선례의 Tips 평행"),
 "Roster Tips": (0.55, "Roster App 승인 선례의 Tips 평행"),
 "Outreach Tips": (0.55, "Outreach App 승인 선례의 Tips 평행"),
 "Trademark Tracker": (0.55, "상표 출원 상태 추적 관리(Deadline Tracker 선례 평행)"),
 "Skydiving Video": (0.55, "스카이다이빙 강습·체험 영상(Sledding Video 평행)"),
 "Acne Video": (0.55, "여드름 관리 영상 가이드(Eczema Video 평행)"),
 "Acne Diary": (0.55, "여드름 증상 기록 일지(Eczema Diary 평행)"),
}

R_DUP = {
 "Chiller Advice": "이번 배치 승인 Chiller Tips와 동일 기능 의미 중복",
 "Subcontractor Advice": "이번 배치 승인 Subcontractor Tips와 동일 기능 의미 중복",
 "Podcast Advice": "이번 배치 승인 Podcast Tips와 동일 기능 의미 중복",
 "Refrigeration Advice": "이번 배치 승인 Refrigeration Tips와 동일 기능 의미 중복",
 "Roster Advice": "이번 배치 승인 Roster Tips와 동일 기능 의미 중복",
}

R = {
 "Judge Grid": "선례 기각(App 기각) 계열", "Jury Scheduler": "스케줄러 도구 지칭으로 대상 불분명",
 "Lawsuit Check": "확인 기능 지칭으로 제품 불분명", "Divorce Memo": "메모 결합 불성립",
 "Custody Number": "번호 지칭으로 제품 불분명", "Immigration Schematic": "도식 지칭으로 제품 불분명",
 "Testament Record": "기록 대상 불분명(Record 기각 평행)", "Notary Quote": "인용·견적 중의로 불분명",
 "Mediation Clock": "결합 불성립", "Guardianship Questionnaire": "설문 대상 불분명",
 "Transponder Workbook": "워크북 대상 불분명", "Thumbnail Mode": "기능 토글로 읽혀 제품 불분명",
 "Hallway Spec": "선례 기각(App 기각) 계열", "Barbecue Quantity": "수량 대상 불분명",
 "Theory Login": "선례 기각(App 기각) 계열", "Visit Analysis": "분석 대상 불분명",
 "Installment Coach": "코칭 대상 불분명", "Trademark Habit": "결합 불성립",
 "Patent Ledger": "원장 대상 불분명", "Copyright Planner": "계획 대상 불분명",
 "Migraine Nomination": "결합 불성립", "Insomnia Simulator": "결합 불성립",
 "Skydiving Recipe": "결합 불성립", "Snowboarding Newsletter": "결합 불성립",
 "Eczema Inventory": "결합 불성립", "Ziplining Checkin": "결합 불성립",
 "Psoriasis Size": "결합 불성립(속성 지칭)", "Sledding Distance": "결합 불성립(속성 지칭)",
 "Vertigo Range": "결합 불성립", "Diving Clock": "결합 불성립",
 "Arthritis Time": "결합 불성립", "Sailing Height": "결합 불성립",
 "Menopause Width": "결합 불성립", "Rafting Load": "결합 불성립",
 "Pregnancy Voltage": "결합 불성립", "Climbing Frequency": "결합 불성립",
 "Fertility Compatibility": "상태 명사로 제품명 부자연", "Biking Condition": "상태 명사로 제품명 부자연",
 "Thyroid Humidity": "결합 불성립", "Golf Breakdown": "내역·고장 중의로 불분명",
 "Cholesterol Sensor": "결합 불성립", "Fishing Approval": "승인 지칭으로 제품 불분명",
 "Hypertension Matrix": "행렬·매트릭스 중의로 불분명", "Camping Utilization": "활용 지칭으로 제품 불분명",
 "Anemia Benefit": "혜택 지칭으로 제품 불분명", "Glamping Resignation": "결합 불성립",
 "Heartburn Hazard": "결합 불성립", "Stargazing Tutorial": "terrain 대상 결합 불성립",
 "Constipation Handbook": "terrain 대상 결합 불성립", "Birdwatching Gift": "결합 불성립",
 "Concussion Retreat": "terrain 대상 결합 불성립", "Canyon Flyer": "terrain 대상 결합 불성립",
 "Sprain App": "염좌 상태 지칭으로 용도 불분명", "Geyser Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Fracture Advice": "선례 기각(App 기각) 계열", "Fjord Workbook": "선례 기각(App 기각) 계열",
 "Insulin Mode": "기능 토글로 읽혀 제품 불분명", "Savanna Spec": "선례 기각(App 기각) 계열",
 "Tundra Quantity": "선례 기각(App 기각) 계열", "Prairie Login": "선례 기각(App 기각) 계열",
 "Marsh Analysis": "선례 기각(App 기각) 계열", "Cove Coach": "선례 기각(App 기각) 계열",
 "Cliff Habit": "선례 기각(App 기각) 계열", "Cavern Tracker": "선례 기각(App 기각) 계열",
 "Oasis Flow": "선례 기각(App 기각) 계열", "Dune Hub": "선례 기각(App 기각) 계열",
 "Whale Desk": "선례 기각(App 기각) 계열", "Dolphin Radar": "선례 기각(App 기각) 계열",
 "Penguin Relay": "선례 기각(App 기각) 계열", "Flamingo Vault": "선례 기각(App 기각) 계열",
 "Turtle Compass": "선례 기각(App 기각) 계열", "Moose Beacon": "선례 기각(App 기각) 계열",
 "Bison Forge": "선례 기각(App 기각) 계열", "Reindeer Cascade": "선례 기각(App 기각) 계열",
 "Return Workbook": "워크북 대상 불분명", "Checkin Mode": "기능 토글로 읽혀 제품 불분명",
 "Transcript Spec": "사양 참조로 제품 불분명", "Defect Quantity": "수량 대상 불분명",
 "Yield Login": "선례 기각(App 기각) 계열", "Consumption Analysis": "분석 대상 불분명",
 "Campaign Coach": "코칭 대상 불분명", "Segment Workbook": "선례 기각(App 상표 기각) 계열",
 "Rights Mode": "선례 기각(App 기각) 계열", "Cargo Spec": "사양 참조로 제품 불분명",
 "Churn Quantity": "수량 대상 불분명", "Firewall Login": "제품 불분명",
 "Migration Analysis": "선례 기각(App 기각) 계열", "Knowledge Coach": "코칭 대상 불분명",
 "Assessment Habit": "결합 불성립", "Lawyer Eligibility": "결합 불성립",
 "Attorney Depth": "결합 불성립", "Major App": "전공·주요 중의로 대상 불분명",
 "Channel Workbook": "워크북 대상 불분명", "Skillset Mode": "기능 토글로 읽혀 제품 불분명",
 "Livestream Spec": "사양 참조로 제품 불분명", "Tuneup Quantity": "수량 대상 불분명",
 "Server Login": "제품 불분명", "Spay Analysis": "분석 대상 불분명",
 "Braces Coach": "코칭 대상 불분명", "Snack Habit": "결합 불성립",
 "Judge Wave": "선례 기각(App 기각) 계열", "Jury Monitor": "선례 기각(App 기각) 계열(Monitor 기각 라인)",
 "Lawsuit Score": "점수 지칭으로 제품 불분명", "Divorce Quota": "쿼터 결합 불성립",
 "Custody Version": "버전 지칭으로 제품 불분명", "Immigration Layout": "레이아웃 지칭으로 제품 불분명",
 "Testament Copy": "사본·복사 중의로 불분명(Copy 기각 평행)", "Notary Warranty": "보증 결합 불성립",
 "Mediation Time": "결합 불성립", "Guardianship Utilization": "활용 지칭으로 제품 불분명",
 "Chiller Workbook": "워크북 대상 불분명", "Transponder Mode": "기능 토글로 읽혀 제품 불분명",
 "Thumbnail Spec": "사양 참조로 제품 불분명", "Hallway Quantity": "선례 기각(App 기각) 계열",
 "Barbecue Login": "제품 불분명", "Theory Analysis": "선례 기각(App 기각) 계열",
 "Visit Coach": "코칭 대상 불분명", "Installment Habit": "결합 불성립",
 "Patent Board": "게시판·판 지칭으로 제품 불분명(Board 기각 라인)", "Copyright Scheduler": "스케줄러 도구 지칭으로 대상 불분명",
 "Migraine Correction": "결합 불성립", "Insomnia Predictor": "예측 대상 불분명",
 "Snowboarding Inventory": "결합 불성립", "Eczema Claim": "결합 불성립",
 "Ziplining Size": "결합 불성립(속성 지칭)", "Psoriasis Length": "결합 불성립(속성 지칭)",
 "Sledding Range": "결합 불성립", "Vertigo Limit": "결합 불성립",
 "Diving Time": "결합 불성립", "Arthritis Speed": "결합 불성립",
 "Sailing Width": "결합 불성립", "Menopause Temperature": "결합 불성립",
 "Rafting Voltage": "결합 불성립", "Pregnancy Wattage": "결합 불성립",
 "Climbing Compatibility": "상태 명사로 제품명 부자연", "Fertility Capacity": "상태 명사로 제품명 부자연",
 "Biking Humidity": "결합 불성립", "Thyroid Episode": "결합 불성립",
 "Golf Sensor": "결합 불성립", "Cholesterol Reception": "리셉션·수신 중의로 불분명",
 "Fishing Matrix": "행렬·매트릭스 중의로 불분명", "Hypertension Evaluation": "평가 대상 불분명",
 "Camping Benefit": "혜택 지칭으로 제품 불분명", "Anemia Requirement": "요건 지칭으로 제품 불분명",
 "Glamping Hazard": "결합 불성립", "Heartburn Guarantor": "보증인 명사 결합 불성립",
 "Stargazing Handbook": "terrain 대상 결합 불성립", "Constipation Timetable": "terrain 대상 결합 불성립",
 "Birdwatching Retreat": "terrain 대상 결합 불성립", "Concussion Tournament": "terrain 대상 결합 불성립",
 "Canyon App": "지명 지칭으로 제품 불분명", "Sprain Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Geyser Advice": "선례 기각(App 기각) 계열", "Fracture Workbook": "워크북 대상 불분명",
 "Fjord Mode": "선례 기각(App 기각) 계열", "Insulin Spec": "사양 참조로 제품 불분명",
 "Savanna Quantity": "선례 기각(App 기각) 계열", "Tundra Login": "선례 기각(App 기각) 계열",
 "Prairie Analysis": "선례 기각(App 기각) 계열", "Marsh Coach": "선례 기각(App 기각) 계열",
 "Cove Habit": "선례 기각(App 기각) 계열", "Cliff Tracker": "선례 기각(App 기각) 계열",
 "Cavern Flow": "선례 기각(App 기각) 계열", "Oasis Hub": "선례 기각(App 기각) 계열",
 "Dune Desk": "선례 기각(App 기각) 계열", "Whale Radar": "선례 기각(App 기각) 계열",
 "Dolphin Relay": "선례 기각(App 기각) 계열", "Penguin Vault": "선례 기각(App 기각) 계열",
 "Flamingo Compass": "선례 기각(App 기각) 계열", "Turtle Beacon": "선례 기각(App 기각) 계열",
 "Moose Forge": "선례 기각(App 기각) 계열", "Bison Cascade": "선례 기각(App 기각) 계열",
 "Reindeer Bridge": "선례 기각(App 기각) 계열(Bridge 중의)", "Subcontractor Workbook": "워크북 대상 불분명",
 "Return Mode": "기능 토글로 읽혀 제품 불분명", "Checkin Spec": "사양 참조로 제품 불분명",
 "Transcript Quantity": "수량 대상 불분명", "Defect Login": "제품 불분명",
 "Yield Analysis": "선례 기각(App 기각) 계열", "Consumption Coach": "코칭 대상 불분명",
 "Campaign Habit": "결합 불성립",
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
out = base + r"\_dec_c35.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
