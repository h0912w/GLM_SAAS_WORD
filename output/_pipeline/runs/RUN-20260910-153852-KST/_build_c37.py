# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk36_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Clause App": (0.55, "계약 조항 관리 앱(실재)"),
 "Clause Tips": (0.55, "Clause App 승인 선례의 Tips 평행"),
 "Scholarship App": (0.55, "장학금 검색·신청 관리 앱(실재)"),
 "Scholarship Tips": (0.55, "Scholarship App 승인 선례의 Tips 평행"),
 "Expense App": (0.55, "경비 지출 처리 관리 앱(실재)"),
 "Itinerary App": (0.55, "여행 일정 관리 앱(실재)"),
 "Counteroffer App": (0.55, "매매 협상 반제안 관리 앱(실재)"),
 "Headlight App": (0.55, "헤드라이트 교체·수리 관리 앱(Windshield App 평행)"),
 "Supplier Tips": (0.55, "Supplier App 승인 선례의 Tips 평행"),
 "Deduction Tips": (0.55, "Deduction App 승인 선례의 Tips 평행"),
 "Shelter Tips": (0.55, "Shelter App 승인 선례의 Tips 평행"),
 "Brunch App": (0.55, "브런치 예약·검색 앱(실재, Snack App 평행)"),
 "Brunch Tips": (0.55, "Brunch App 승인 선례의 Tips 평행"),
 "Insomnia Video": (0.55, "불면 관리 영상 가이드(Vertigo Video 평행)"),
 "Immigration Notification": (0.55, "이민 절차 알림 관리(Notification 절차 명사 선례 평행)"),
 "Testament Deadline": (0.55, "유언·상속 기한 관리(Deadline 절차 명사 선례 평행)"),
 "Birdwatching App": (0.55, "조류 관찰 기록·동정 앱(실재)"),
}

R_DUP = {
 "Listing Advice": "이번 배치 승인 Listing Tips와 동일 기능 의미 중복",
 "Fertilizer Advice": "이번 배치 승인 Fertilizer Tips와 동일 기능 의미 중복",
 "Cleaning Advice": "이번 배치 승인 Cleaning Tips와 동일 기능 의미 중복",
 "Supplier Advice": "이번 배치 승인 Supplier Tips와 동일 기능 의미 중복",
 "Deduction Advice": "이번 배치 승인 Deduction Tips와 동일 기능 의미 중복",
 "Shelter Advice": "이번 배치 승인 Shelter Tips와 동일 기능 의미 중복",
 "Plumbing Advice": "이번 배치 승인 Plumbing Tips와 동일 기능 의미 중복",
}

R = {
 "Cliff Hub": "선례 기각(App 기각) 계열", "Cavern Desk": "선례 기각(App 기각) 계열",
 "Oasis Radar": "선례 기각(App 기각) 계열", "Dune Relay": "선례 기각(App 기각) 계열",
 "Whale Vault": "선례 기각(App 기각) 계열", "Dolphin Compass": "선례 기각(App 기각) 계열",
 "Penguin Beacon": "선례 기각(App 기각) 계열", "Flamingo Forge": "선례 기각(App 기각) 계열",
 "Turtle Cascade": "선례 기각(App 기각) 계열", "Moose Bridge": "선례 기각(App 기각) 계열",
 "Bison Signal": "선례 기각(App 기각) 계열", "Reindeer Watch": "선례 기각(App 기각) 계열",
 "Claim Workbook": "워크북 대상 불분명", "Roster Mode": "기능 토글로 읽혀 제품 불분명",
 "Subcontractor Spec": "사양 참조로 제품 불분명", "Return Quantity": "수량 대상 불분명",
 "Checkin Login": "제품 불분명", "Transcript Analysis": "분석 대상 불분명",
 "Defect Coach": "코칭 대상 불분명", "Yield Habit": "선례 기각(App 기각) 계열",
 "Outreach Mode": "기능 토글로 읽혀 제품 불분명", "Segment Quantity": "선례 기각(App 상표 기각) 계열",
 "Rights Login": "선례 기각(App 기각) 계열", "Cargo Analysis": "분석 대상 불분명",
 "Churn Coach": "코칭 대상 불분명", "Firewall Habit": "결합 불성립",
 "Lawyer Appointment": "약속 대상 불분명", "Attorney Temperature": "결합 불성립",
 "Court Retreat": "결합 불성립", "Peril App": "위험 상태 지칭으로 용도 불분명",
 "Peril Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Major Workbook": "선례 기각(App 기각) 계열", "Podcast Spec": "사양 참조로 제품 불분명",
 "Channel Quantity": "수량 대상 불분명", "Skillset Login": "제품 불분명",
 "Livestream Analysis": "분석 대상 불분명", "Tuneup Coach": "코칭 대상 불분명",
 "Server Habit": "결합 불성립", "Judge Map": "선례 기각(App 기각) 계열(Map 기각 선례)",
 "Jury Ops": "운영 지칭으로 제품 불분명", "Lawsuit Profile": "프로필 대상 불분명",
 "Divorce Brief": "요약서·브리핑 중의로 불분명", "Custody Detail": "세부 지칭으로 제품 불분명",
 "Immigration Rendering": "렌더링 결합 불성립", "Testament Forecast": "예측 대상 불분명",
 "Notary Nomination": "결합 불성립", "Mediation Height": "결합 불성립",
 "Guardianship Depreciation": "결합 불성립", "Nap Workbook": "워크북 대상 불분명",
 "Shampoo Mode": "기능 토글로 읽혀 제품 불분명", "Refrigeration Spec": "사양 참조로 제품 불분명",
 "Chiller Quantity": "수량 대상 불분명", "Transponder Login": "제품 불분명",
 "Thumbnail Analysis": "분석 대상 불분명", "Hallway Coach": "선례 기각(App 기각) 계열",
 "Barbecue Habit": "결합 불성립", "Trademark Desk": "책상·데스크 중의로 불분명",
 "Patent Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)", "Copyright Register": "등록부·등록 중의로 불분명",
 "Migraine Verification": "결합 불성립", "Insomnia Recipe": "결합 불성립",
 "Skydiving Expense": "결합 불성립", "Acne Newsletter": "결합 불성립",
 "Snowboarding Checkin": "결합 불성립", "Eczema Size": "결합 불성립(속성 지칭)",
 "Ziplining Distance": "결합 불성립", "Psoriasis Range": "결합 불성립",
 "Sledding Clock": "결합 불성립", "Vertigo Time": "결합 불성립",
 "Diving Height": "결합 불성립", "Arthritis Width": "결합 불성립",
 "Sailing Load": "결합 불성립", "Menopause Voltage": "결합 불성립",
 "Rafting Frequency": "결합 불성립", "Pregnancy Compatibility": "상태 명사로 제품명 부자연",
 "Climbing Condition": "상태 명사로 제품명 부자연", "Fertility Humidity": "결합 불성립",
 "Biking Breakdown": "내역·고장 중의로 불분명", "Thyroid Sensor": "결합 불성립",
 "Golf Approval": "승인 지칭으로 제품 불분명", "Cholesterol Matrix": "행렬·매트릭스 중의로 불분명",
 "Fishing Utilization": "활용 지칭으로 제품 불분명", "Hypertension Benefit": "혜택 지칭으로 제품 불분명",
 "Camping Resignation": "결합 불성립", "Anemia Hazard": "결합 불성립",
 "Glamping Tutorial": "terrain 대상 결합 불성립", "Heartburn Handbook": "terrain 대상 결합 불성립",
 "Stargazing Gift": "결합 불성립", "Constipation Retreat": "terrain 대상 결합 불성립",
 "Concussion Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Canyon Workbook": "선례 기각(App 기각) 계열",
 "Sprain Mode": "선례 기각(App 기각) 계열", "Geyser Spec": "선례 기각(App 기각) 계열",
 "Fracture Quantity": "선례 기각(App 기각) 계열", "Fjord Login": "선례 기각(App 기각) 계열",
 "Insulin Analysis": "분석 대상 불분명", "Savanna Coach": "선례 기각(App 기각) 계열",
 "Tundra Habit": "선례 기각(App 기각) 계열", "Prairie Tracker": "선례 기각(App 기각) 계열",
 "Marsh Flow": "선례 기각(App 기각) 계열", "Cove Hub": "선례 기각(App 기각) 계열",
 "Cliff Desk": "선례 기각(App 기각) 계열", "Cavern Radar": "선례 기각(App 기각) 계열",
 "Oasis Relay": "선례 기각(App 기각) 계열", "Dune Vault": "선례 기각(App 기각) 계열",
 "Whale Compass": "선례 기각(App 기각) 계열", "Dolphin Beacon": "선례 기각(App 기각) 계열",
 "Penguin Forge": "선례 기각(App 기각) 계열", "Flamingo Cascade": "선례 기각(App 기각) 계열",
 "Turtle Bridge": "선례 기각(App 기각) 계열", "Moose Signal": "선례 기각(App 기각) 계열",
 "Bison Watch": "선례 기각(App 기각) 계열", "Reindeer Scope": "선례 기각(App 기각) 계열",
 "Listing Workbook": "워크북 대상 불분명", "Claim Mode": "기능 토글로 읽혀 제품 불분명",
 "Roster Spec": "사양 참조로 제품 불분명", "Subcontractor Quantity": "수량 대상 불분명",
 "Return Login": "제품 불분명", "Checkin Analysis": "분석 대상 불분명",
 "Transcript Coach": "코칭 대상 불분명", "Defect Habit": "결합 불성립",
 "Fertilizer Workbook": "워크북 대상 불분명", "Outreach Spec": "사양 참조로 제품 불분명",
 "Segment Login": "선례 기각(App 상표 기각) 계열", "Rights Analysis": "선례 기각(App 기각) 계열",
 "Cargo Coach": "코칭 대상 불분명", "Churn Habit": "결합 불성립",
 "Lawyer Feedback": "결합 불성립", "Attorney Pressure": "결합 불성립",
 "Court Tournament": "결합 불성립", "Peril Advice": "선례 기각(App 기각) 계열",
 "Plumbing Workbook": "워크북 대상 불분명", "Major Mode": "선례 기각(App 기각) 계열",
 "Podcast Quantity": "수량 대상 불분명", "Channel Login": "제품 불분명",
 "Skillset Analysis": "분석 대상 불분명", "Livestream Coach": "코칭 대상 불분명",
 "Tuneup Habit": "결합 불성립", "Judge Frame": "선례 기각(App 기각) 계열(프레임 중의)",
 "Jury Playbook": "플레이북 대상 불분명", "Lawsuit Status": "상태 지칭으로 제품 불분명",
 "Divorce Circular": "회람·안내문 결합 불성립", "Custody Identifier": "식별자 지칭으로 제품 불분명",
 "Notary Correction": "결합 불성립", "Mediation Width": "결합 불성립",
 "Guardianship Resignation": "결합 불성립", "Cleaning Workbook": "워크북 대상 불분명",
 "Nap Mode": "기능 토글로 읽혀 제품 불분명", "Shampoo Spec": "사양 참조로 제품 불분명",
 "Refrigeration Quantity": "수량 대상 불분명", "Chiller Login": "제품 불분명",
 "Transponder Analysis": "분석 대상 불분명", "Thumbnail Coach": "코칭 대상 불분명",
 "Hallway Habit": "선례 기각(App 기각) 계열", "Trademark Radar": "레이더 지칭으로 제품 불분명",
 "Patent Station": "선례 기각(App 기각) 계열(Station 기각 라인)", "Copyright Ops": "운영 지칭으로 제품 불분명",
 "Migraine Simulator": "결합 불성립", "Skydiving Newsletter": "결합 불성립",
 "Acne Inventory": "결합 불성립", "Snowboarding Size": "결합 불성립(속성 지칭)",
 "Eczema Length": "결합 불성립(속성 지칭)", "Ziplining Range": "결합 불성립",
 "Psoriasis Limit": "결합 불성립", "Sledding Time": "결합 불성립",
 "Vertigo Speed": "결합 불성립", "Diving Width": "결합 불성립",
 "Arthritis Temperature": "결합 불성립", "Sailing Voltage": "결합 불성립",
 "Menopause Wattage": "결합 불성립", "Rafting Compatibility": "상태 명사로 제품명 부자연",
 "Pregnancy Capacity": "상태 명사로 제품명 부자연", "Climbing Humidity": "결합 불성립",
 "Fertility Episode": "결합 불성립", "Biking Sensor": "결합 불성립",
 "Thyroid Reception": "리셉션·수신 중의로 불분명", "Golf Matrix": "행렬·매트릭스 중의로 불분명",
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
out = base + r"\_dec_c37.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
