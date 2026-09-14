# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk40_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Excavation App": (0.55, "굴착 공사 관리 앱(실재)"),
 "Glamping App": (0.55, "글램핑장 검색·예약 앱(Campsite App 평행)"),
 "Viola Tips": (0.55, "Viola App 승인 선례의 Tips 평행"),
 "Campsite Tips": (0.55, "Campsite App 승인 선례의 Tips 평행"),
 "Compensation Tips": (0.55, "Compensation App 승인 선례의 Tips 평행"),
 "Pump Tips": (0.55, "Pump App 승인 선례의 Tips 평행"),
 "Migraine Diary": (0.55, "편두통 증상 기록 일지(Vertigo Diary 평행)"),
 "Testament Template": (0.55, "유언장 양식 템플릿(Template 절차 명사 선례 평행)"),
 "Testament Guide": (0.55, "유언·상속 절차 가이드(Guide 절차 명사 선례 평행)"),
}

R_DUP = {
 "Editor Advice": "이번 배치 승인 Editor Tips와 동일 기능 의미 중복",
 "Locksmith Advice": "이번 배치 승인 Locksmith Tips와 동일 기능 의미 중복",
 "Wax Advice": "이번 배치 승인 Wax Tips와 동일 기능 의미 중복",
 "Viola Advice": "이번 배치 승인 Viola Tips와 동일 기능 의미 중복",
 "Compensation Advice": "이번 배치 승인 Compensation Tips와 동일 기능 의미 중복",
 "Symptom Advice": "이번 배치 승인 Symptom Tips와 동일 기능 의미 중복",
}

R = {
 "Debit Workbook": "워크북 대상 불분명", "Court Mode": "선례 기각(App 기각) 계열",
 "Shipper Spec": "사양 참조로 제품 불분명", "Counteroffer Quantity": "수량 대상 불분명",
 "Peril Login": "선례 기각(App 기각) 계열", "Deduction Analysis": "분석 대상 불분명",
 "Plumbing Coach": "코칭 대상 불분명", "Major Habit": "선례 기각(App 기각) 계열",
 "Judge Studio": "선례 기각(App 기각) 계열(Studio 기각 라인)", "Jury Finder": "탐색 기능 지칭으로 제품 불분명(Finder 기각 라인)",
 "Lawsuit Update": "갱신 기능 지칭으로 제품 불분명", "Divorce Fee": "수수료 결합 불성립",
 "Custody Token": "토큰 지칭으로 제품 불분명", "Immigration Repository": "저장소 지칭으로 제품 불분명",
 "Notary Seal": "인장·밀봉 중의로 불분명", "Mediation Brightness": "결합 불성립",
 "Guardianship Timetable": "terrain 대상 결합 불성립", "Detention App": "구금·학교 지도 중의로 용도 불분명",
 "Contact Workbook": "워크북 대상 불분명", "Portfolio Mode": "기능 토글로 읽혀 제품 불분명",
 "Headlight Quantity": "수량 대상 불분명", "Brunch Login": "제품 불분명",
 "Shelter Analysis": "분석 대상 불분명", "Cleaning Coach": "코칭 대상 불분명",
 "Nap Habit": "결합 불성립", "Trademark Cascade": "선례 기각(App 기각) 계열(Cascade 중의)",
 "Patent Panel": "패널 지칭으로 제품 불분명", "Copyright Locator": "탐색 기능 지칭으로 제품 불분명(Locator 기각 라인)",
 "Insomnia Claim": "결합 불성립", "Skydiving Length": "결합 불성립(속성 지칭)",
 "Acne Weight": "결합 불성립(속성 지칭)", "Snowboarding Type": "결합 불성립(분류 대상 부자연)",
 "Eczema Clock": "결합 불성립", "Ziplining Depth": "결합 불성립",
 "Psoriasis Height": "결합 불성립", "Sledding Pressure": "결합 불성립",
 "Vertigo Load": "결합 불성립", "Diving Brightness": "결합 불성립",
 "Arthritis Frequency": "결합 불성립", "Sailing Usage": "사용 지칭으로 제품 불분명",
 "Menopause Condition": "상태 명사로 제품명 부자연", "Rafting Cycle": "주기 지칭으로 제품 불분명",
 "Pregnancy Breakdown": "내역·고장 중의로 불분명", "Climbing Followup": "후속 지칭으로 제품 불분명",
 "Fertility Approval": "승인 지칭으로 제품 불분명", "Biking Questionnaire": "설문 대상 불분명",
 "Thyroid Utilization": "활용 지칭으로 제품 불분명", "Golf Depreciation": "결합 불성립",
 "Cholesterol Resignation": "결합 불성립", "Fishing Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Hypertension Tutorial": "terrain 대상 결합 불성립", "Camping Opinion": "소견 대상 불분명",
 "Anemia Gift": "결합 불성립", "Glamping Flyer": "terrain 대상 결합 불성립",
 "Heartburn App": "속쓰림 상태 지칭으로 용도 불분명", "Stargazing Workbook": "워크북 대상 불분명",
 "Constipation Mode": "선례 기각(App 기각) 계열", "Testimony Spec": "사양 참조로 제품 불분명",
 "Birdwatching Login": "제품 불분명", "Concussion Analysis": "선례 기각(App 기각) 계열",
 "Canyon Habit": "선례 기각(App 기각) 계열", "Sprain Tracker": "선례 기각(App 기각) 계열",
 "Geyser Flow": "선례 기각(App 기각) 계열", "Fracture Hub": "선례 기각(App 기각) 계열",
 "Fjord Desk": "선례 기각(App 기각) 계열", "Insulin Radar": "제품 불분명",
 "Savanna Relay": "선례 기각(App 기각) 계열", "Tundra Vault": "선례 기각(App 기각) 계열",
 "Prairie Compass": "선례 기각(App 기각) 계열", "Marsh Beacon": "선례 기각(App 기각) 계열",
 "Cove Forge": "선례 기각(App 기각) 계열", "Cliff Cascade": "선례 기각(App 기각) 계열",
 "Cavern Bridge": "선례 기각(App 기각) 계열", "Oasis Signal": "선례 기각(App 기각) 계열",
 "Dune Watch": "선례 기각(App 기각) 계열", "Whale Scope": "선례 기각(App 기각) 계열",
 "Dolphin Loop": "선례 기각(App 기각) 계열", "Penguin Grid": "선례 기각(App 기각) 계열",
 "Flamingo Wave": "선례 기각(App 기각) 계열", "Turtle Path": "선례 기각(App 기각) 계열",
 "Moose Point": "선례 기각(App 기각) 계열", "Bison Map": "선례 기각(App 기각) 계열",
 "Reindeer Frame": "선례 기각(App 기각) 계열", "Utility App": "공공요금·소프트웨어 도구 중의로 대상 불분명",
 "Drain Workbook": "워크북 대상 불분명", "Cruise Mode": "기능 토글로 읽혀 제품 불분명",
 "Violin Spec": "사양 참조로 제품 불분명", "Expense Login": "제품 불분명",
 "Clause Analysis": "분석 대상 불분명", "Listing Habit": "결합 불성립",
 "Retainer App": "법률 계약금·교정기 중의로 대상 불분명", "Title Advice": "선례 기각(App 기각) 계열",
 "Actuary Workbook": "선례 기각(App 기각) 계열", "Jobsite Spec": "사양 참조로 제품 불분명",
 "Markdown Quantity": "수량 대상 불분명", "Itinerary Login": "제품 불분명",
 "Scholarship Analysis": "분석 대상 불분명", "Supplier Coach": "코칭 대상 불분명",
 "Fertilizer Habit": "결합 불성립", "Lawyer Nomination": "결합 불성립",
 "Attorney Capacity": "상태 명사로 제품명 부자연", "Nozzle App": "노즐 부품 지칭으로 용도 불분명",
 "Symptom Workbook": "워크북 대상 불분명", "Debit Mode": "기능 토글로 읽혀 제품 불분명",
 "Court Spec": "선례 기각(App 기각) 계열", "Shipper Quantity": "수량 대상 불분명",
 "Counteroffer Login": "제품 불분명", "Peril Analysis": "선례 기각(App 기각) 계열",
 "Deduction Coach": "코칭 대상 불분명", "Plumbing Habit": "결합 불성립",
 "Judge Lab": "선례 기각(App 기각) 계열(Lab 기각 라인)", "Jury Office": "사무실 지칭으로 제품 불분명",
 "Lawsuit Feed": "피드 지칭으로 제품 불분명", "Divorce Item": "항목 지칭으로 제품 불분명",
 "Custody Signature": "서명 대상 불분명", "Immigration Announcement": "공지 지칭으로 제품 불분명",
 "Notary Review": "리뷰 대상 불분명", "Mediation Frequency": "결합 불성립",
 "Guardianship Opinion": "소견 대상 불분명",
 "Editor Workbook": "워크북 대상 불분명", "Contact Mode": "기능 토글로 읽혀 제품 불분명",
 "Portfolio Spec": "사양 참조로 제품 불분명", "Headlight Login": "제품 불분명",
 "Brunch Analysis": "분석 대상 불분명", "Shelter Coach": "코칭 대상 불분명",
 "Cleaning Habit": "결합 불성립", "Trademark Bridge": "선례 기각(App 기각) 계열(Bridge 중의)",
 "Patent Scale": "저울·규모 중의로 불분명", "Copyright Finder": "탐색 기능 지칭으로 제품 불분명(Finder 기각 라인)",
 "Migraine Refund": "결합 불성립", "Insomnia Onboarding": "결합 불성립",
 "Skydiving Weight": "결합 불성립(속성 지칭)", "Acne Distance": "결합 불성립",
 "Snowboarding Clock": "결합 불성립", "Eczema Time": "결합 불성립",
 "Ziplining Height": "결합 불성립", "Psoriasis Width": "결합 불성립",
 "Sledding Load": "결합 불성립", "Vertigo Voltage": "결합 불성립",
 "Diving Frequency": "결합 불성립", "Arthritis Compatibility": "상태 명사로 제품명 부자연",
 "Sailing Condition": "상태 명사로 제품명 부자연", "Menopause Humidity": "결합 불성립",
 "Rafting Breakdown": "내역·고장 중의로 불분명", "Pregnancy Sensor": "결합 불성립",
 "Climbing Approval": "승인 지칭으로 제품 불분명", "Fertility Matrix": "행렬·매트릭스 중의로 불분명",
 "Biking Utilization": "활용 지칭으로 제품 불분명", "Thyroid Benefit": "혜택 지칭으로 제품 불분명",
 "Golf Resignation": "결합 불성립", "Cholesterol Hazard": "결합 불성립",
 "Fishing Tutorial": "terrain 대상 결합 불성립", "Hypertension Handbook": "terrain 대상 결합 불성립",
 "Camping Gift": "결합 불성립", "Anemia Retreat": "terrain 대상 결합 불성립",
 "Heartburn Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Locksmith Workbook": "워크북 대상 불분명",
 "Stargazing Mode": "기능 토글로 읽혀 제품 불분명", "Constipation Spec": "선례 기각(App 기각) 계열",
 "Testimony Quantity": "수량 대상 불분명", "Birdwatching Analysis": "분석 대상 불분명",
 "Concussion Coach": "선례 기각(App 기각) 계열", "Canyon Tracker": "선례 기각(App 기각) 계열",
 "Sprain Flow": "선례 기각(App 기각) 계열", "Geyser Hub": "선례 기각(App 기각) 계열",
 "Fracture Desk": "선례 기각(App 기각) 계열", "Fjord Radar": "선례 기각(App 기각) 계열",
 "Insulin Relay": "제품 불분명", "Savanna Vault": "선례 기각(App 기각) 계열",
 "Tundra Compass": "선례 기각(App 기각) 계열", "Prairie Beacon": "선례 기각(App 기각) 계열",
 "Marsh Forge": "선례 기각(App 기각) 계열", "Cove Cascade": "선례 기각(App 기각) 계열",
 "Cliff Bridge": "선례 기각(App 기각) 계열", "Cavern Signal": "선례 기각(App 기각) 계열",
 "Oasis Watch": "선례 기각(App 기각) 계열", "Dune Scope": "선례 기각(App 기각) 계열",
 "Whale Loop": "선례 기각(App 기각) 계열", "Dolphin Grid": "선례 기각(App 기각) 계열",
 "Penguin Wave": "선례 기각(App 기각) 계열", "Flamingo Path": "선례 기각(App 기각) 계열",
 "Turtle Point": "선례 기각(App 기각) 계열", "Moose Map": "선례 기각(App 기각) 계열",
 "Bison Frame": "선례 기각(App 기각) 계열", "Detention Tips": "선례 기각(App 기각)의 Tips 평행 불가",
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
out = base + r"\_dec_c41.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
