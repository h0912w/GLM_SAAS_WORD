# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk35_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Fertilizer App": (0.55, "비료 시비·관리 앱(실재)"),
 "Fertilizer Tips": (0.55, "Fertilizer App 승인 선례의 Tips 평행"),
 "Plumbing App": (0.55, "배관 수리 접수·관리 앱(실재)"),
 "Plumbing Tips": (0.55, "Plumbing App 승인 선례의 Tips 평행"),
 "Cleaning App": (0.55, "청소 서비스 예약·관리 앱(실재)"),
 "Cleaning Tips": (0.55, "Cleaning App 승인 선례의 Tips 평행"),
 "Supplier App": (0.55, "공급업체 발주·관리 앱(실재)"),
 "Deduction App": (0.55, "세금 공제 계산·관리 앱(실재)"),
 "Shelter App": (0.55, "대피소·보호소 찾기 앱(실재)"),
 "Nap Tips": (0.55, "Nap App 승인 선례의 Tips 평행"),
 "Listing Tips": (0.55, "Listing App 승인 선례의 Tips 평행"),
 "Skydiving Diary": (0.55, "스카이다이빙 기록 일지(Ziplining Diary 평행)"),
}

R_DUP = {
 "Outreach Advice": "이번 배치 승인 Outreach Tips와 동일 기능 의미 중복",
 "Shampoo Advice": "이번 배치 승인 Shampoo Tips와 동일 기능 의미 중복",
 "Claim Advice": "이번 배치 승인 Claim Tips와 동일 기능 의미 중복",
 "Nap Advice": "이번 배치 승인 Nap Tips와 동일 기능 의미 중복",
}

R = {
 "Segment Mode": "선례 기각(App 상표 기각) 계열", "Rights Spec": "선례 기각(App 기각) 계열",
 "Cargo Quantity": "수량 대상 불분명", "Churn Login": "제품 불분명",
 "Firewall Analysis": "분석 대상 불분명", "Migration Coach": "선례 기각(App 기각) 계열",
 "Knowledge Habit": "결합 불성립", "Lawyer Broadcast": "결합 불성립",
 "Attorney Height": "결합 불성립", "Court Opinion": "소견 대상 불분명",
 "Major Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Podcast Workbook": "워크북 대상 불분명",
 "Channel Mode": "기능 토글로 읽혀 제품 불분명", "Skillset Spec": "사양 참조로 제품 불분명",
 "Livestream Quantity": "수량 대상 불분명", "Tuneup Login": "제품 불분명",
 "Server Analysis": "분석 대상 불분명", "Spay Coach": "코칭 대상 불분명",
 "Braces Habit": "결합 불성립", "Judge Path": "선례 기각(App 기각) 계열",
 "Jury Companion": "동반자 지칭으로 제품 불분명(Companion 기각 라인)", "Lawsuit Note": "메모·음표 중의로 불분명",
 "Divorce Tab": "탭 지칭으로 제품 불분명", "Custody Link": "링크 지칭으로 제품 불분명",
 "Immigration Sketch": "스케치 결합 불성립", "Testament Reading": "판독 대상 불분명(Reading 기각 평행)",
 "Notary Deposit": "예금·보증금 결합 불성립", "Mediation Speed": "결합 불성립",
 "Guardianship Benefit": "혜택 지칭으로 제품 불분명", "Refrigeration Workbook": "워크북 대상 불분명",
 "Chiller Mode": "기능 토글로 읽혀 제품 불분명", "Transponder Spec": "사양 참조로 제품 불분명",
 "Thumbnail Quantity": "수량 대상 불분명", "Hallway Login": "선례 기각(App 기각) 계열",
 "Barbecue Analysis": "분석 대상 불분명", "Theory Coach": "선례 기각(App 기각) 계열",
 "Visit Habit": "결합 불성립", "Trademark Flow": "흐름 지칭으로 제품 불분명",
 "Patent Deck": "데크(갑판·카드) 중의로 불분명(Deck 기각 라인)", "Copyright Monitor": "선례 기각(App 기각) 계열(Monitor 기각 라인)",
 "Migraine Revision": "결합 불성립", "Insomnia Seal": "결합 불성립",
 "Acne Refund": "결합 불성립", "Snowboarding Claim": "결합 불성립",
 "Eczema Onboarding": "결합 불성립", "Ziplining Length": "결합 불성립(속성 지칭)",
 "Psoriasis Weight": "결합 불성립(속성 지칭)", "Sledding Limit": "결합 불성립",
 "Vertigo Type": "결합 불성립(분류 대상 부자연)", "Diving Speed": "결합 불성립",
 "Arthritis Depth": "결합 불성립", "Sailing Temperature": "결합 불성립",
 "Menopause Pressure": "결합 불성립", "Rafting Wattage": "결합 불성립",
 "Pregnancy Brightness": "결합 불성립", "Climbing Capacity": "상태 명사로 제품명 부자연",
 "Fertility Usage": "사용 지칭으로 제품 불분명", "Biking Episode": "결합 불성립",
 "Thyroid Cycle": "주기 지칭으로 제품 불분명", "Golf Reception": "리셉션·수신 중의로 불분명",
 "Cholesterol Followup": "후속 지칭으로 제품 불분명", "Fishing Evaluation": "평가 대상 불분명",
 "Hypertension Questionnaire": "설문 대상 불분명", "Camping Requirement": "요건 지칭으로 제품 불분명",
 "Anemia Depreciation": "결합 불성립", "Glamping Guarantor": "보증인 명사 결합 불성립",
 "Heartburn Tuner": "튜너 기능 지칭으로 제품 불분명", "Stargazing Timetable": "terrain 대상 결합 불성립",
 "Constipation Opinion": "소견 대상 불분명", "Birdwatching Tournament": "terrain 대상 결합 불성립",
 "Concussion Flyer": "terrain 대상 결합 불성립", "Canyon Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Sprain Advice": "선례 기각(App 기각) 계열", "Geyser Workbook": "선례 기각(App 기각) 계열",
 "Fracture Mode": "선례 기각(App 기각) 계열", "Fjord Spec": "선례 기각(App 기각) 계열",
 "Insulin Quantity": "수량 대상 불분명", "Savanna Login": "선례 기각(App 기각) 계열",
 "Tundra Analysis": "선례 기각(App 기각) 계열", "Prairie Coach": "선례 기각(App 기각) 계열",
 "Marsh Habit": "선례 기각(App 기각) 계열", "Cove Tracker": "선례 기각(App 기각) 계열",
 "Cliff Flow": "선례 기각(App 기각) 계열", "Cavern Hub": "선례 기각(App 기각) 계열",
 "Oasis Desk": "선례 기각(App 기각) 계열", "Dune Radar": "선례 기각(App 기각) 계열",
 "Whale Relay": "선례 기각(App 기각) 계열", "Dolphin Vault": "선례 기각(App 기각) 계열",
 "Penguin Compass": "선례 기각(App 기각) 계열", "Flamingo Beacon": "선례 기각(App 기각) 계열",
 "Turtle Forge": "선례 기각(App 기각) 계열", "Moose Cascade": "선례 기각(App 기각) 계열",
 "Bison Bridge": "선례 기각(App 기각) 계열", "Reindeer Signal": "선례 기각(App 기각) 계열",
 "Roster Workbook": "워크북 대상 불분명", "Subcontractor Mode": "기능 토글로 읽혀 제품 불분명",
 "Return Spec": "사양 참조로 제품 불분명", "Checkin Quantity": "수량 대상 불분명",
 "Transcript Login": "제품 불분명", "Defect Analysis": "분석 대상 불분명",
 "Yield Coach": "선례 기각(App 기각) 계열", "Consumption Habit": "결합 불성립",
 "Outreach Workbook": "워크북 대상 불분명", "Segment Spec": "선례 기각(App 상표 기각) 계열",
 "Rights Quantity": "선례 기각(App 기각) 계열", "Cargo Login": "제품 불분명",
 "Churn Analysis": "분석 대상 불분명", "Firewall Coach": "코칭 대상 불분명",
 "Migration Habit": "선례 기각(App 기각) 계열", "Lawyer Barcode": "결합 불성립",
 "Attorney Width": "결합 불성립", "Court Gift": "결합 불성립",
 "Major Advice": "선례 기각(App 기각) 계열", "Podcast Mode": "기능 토글로 읽혀 제품 불분명",
 "Channel Spec": "사양 참조로 제품 불분명", "Skillset Quantity": "수량 대상 불분명",
 "Livestream Login": "제품 불분명", "Tuneup Analysis": "분석 대상 불분명",
 "Server Coach": "코칭 대상 불분명", "Spay Habit": "결합 불성립",
 "Judge Point": "선례 기각(App 기각) 계열", "Jury Register": "등록부·등록 중의로 불분명",
 "Lawsuit Tag": "태그 지칭으로 제품 불분명", "Divorce Bulletin": "게시판 결합 불성립",
 "Custody Rule": "규칙 지칭으로 제품 불분명", "Immigration Outline": "개요 지칭으로 제품 불분명",
 "Testament Reference": "참조 대상 불분명(Reference 기각 평행)", "Notary Certification": "인증 대상 불분명",
 "Mediation Depth": "결합 불성립", "Guardianship Requirement": "요건 지칭으로 제품 불분명",
 "Shampoo Workbook": "워크북 대상 불분명", "Refrigeration Mode": "기능 토글로 읽혀 제품 불분명",
 "Chiller Spec": "사양 참조로 제품 불분명", "Transponder Quantity": "수량 대상 불분명",
 "Thumbnail Login": "제품 불분명", "Hallway Analysis": "선례 기각(App 기각) 계열",
 "Barbecue Coach": "코칭 대상 불분명", "Theory Habit": "선례 기각(App 기각) 계열",
 "Trademark Hub": "허브 지칭으로 제품 불분명", "Patent Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)",
 "Copyright Companion": "동반자 지칭으로 제품 불분명(Companion 기각 라인)", "Migraine Payment": "결합 불성립",
 "Insomnia Review": "리뷰 대상 불분명", "Skydiving Refund": "결합 불성립",
 "Acne Expense": "결합 불성립", "Snowboarding Onboarding": "결합 불성립",
 "Eczema Checkin": "결합 불성립", "Ziplining Weight": "결합 불성립(속성 지칭)",
 "Psoriasis Distance": "결합 불성립", "Sledding Type": "결합 불성립(분류 대상 부자연)",
 "Vertigo Clock": "결합 불성립", "Diving Depth": "결합 불성립",
 "Arthritis Height": "결합 불성립", "Sailing Pressure": "결합 불성립",
 "Menopause Load": "결합 불성립", "Rafting Brightness": "결합 불성립",
 "Pregnancy Frequency": "결합 불성립", "Climbing Usage": "사용 지칭으로 제품 불분명",
 "Fertility Condition": "상태 명사로 제품명 부자연", "Biking Cycle": "주기 지칭으로 제품 불분명",
 "Thyroid Breakdown": "내역·고장 중의로 불분명", "Golf Followup": "후속 지칭으로 제품 불분명",
 "Cholesterol Approval": "승인 지칭으로 제품 불분명", "Fishing Questionnaire": "설문 대상 불분명",
 "Hypertension Utilization": "활용 지칭으로 제품 불분명", "Camping Depreciation": "결합 불성립",
 "Anemia Resignation": "결합 불성립", "Glamping Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Heartburn Tutorial": "terrain 대상 결합 불성립", "Stargazing Opinion": "소견 대상 불분명",
 "Constipation Gift": "결합 불성립", "Birdwatching Flyer": "terrain 대상 결합 불성립",
 "Concussion App": "뇌진탕 상태 지칭으로 용도 불분명", "Canyon Advice": "선례 기각(App 기각) 계열",
 "Sprain Workbook": "워크북 대상 불분명", "Geyser Mode": "선례 기각(App 기각) 계열",
 "Fracture Spec": "선례 기각(App 기각) 계열", "Fjord Quantity": "선례 기각(App 기각) 계열",
 "Insulin Login": "제품 불분명", "Savanna Analysis": "선례 기각(App 기각) 계열",
 "Tundra Coach": "선례 기각(App 기각) 계열", "Prairie Habit": "선례 기각(App 기각) 계열",
 "Marsh Tracker": "선례 기각(App 기각) 계열", "Cove Flow": "선례 기각(App 기각) 계열",
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
out = base + r"\_dec_c36.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
