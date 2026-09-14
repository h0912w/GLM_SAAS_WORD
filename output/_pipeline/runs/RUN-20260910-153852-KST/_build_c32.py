# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk31_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Defect App": (0.55, "제품 결함 추적 관리 앱(실재)"),
 "Defect Tips": (0.55, "Defect App 승인 선례의 Tips 평행"),
 "Churn App": (0.55, "고객 이탈 방지 관리 앱(실재)"),
 "Churn Tips": (0.55, "Churn App 승인 선례의 Tips 평행"),
 "Tuneup App": (0.55, "차량·기기 정비 관리 앱(실재)"),
 "Tuneup Tips": (0.55, "Tuneup App 승인 선례의 Tips 평행"),
 "Transcript App": (0.55, "음성 녹취록 생성·관리 앱(실재)"),
 "Cargo App": (0.55, "화물 운송·추적 관리 앱(실재)"),
 "Livestream App": (0.55, "실시간 방송 송출 앱(실재)"),
 "Thumbnail App": (0.55, "썸네일 이미지 제작 앱(실재)"),
 "Firewall Tips": (0.55, "Firewall App 승인 선례의 Tips 평행"),
 "Server Tips": (0.55, "Server App 승인 선례의 Tips 평행"),
 "Barbecue Tips": (0.55, "Barbecue App 승인 선례의 Tips 평행"),
 "Eczema Video": (0.55, "습진 관리 영상 가이드(Hypertension Video 평행)"),
 "Eczema Diary": (0.55, "습진 증상 기록 일지(Hypertension Diary 평행)"),
 "Snowboarding Video": (0.55, "스노보드 강습 영상(Golf Video 평행)"),
}

R_DUP = {
 "Firewall Advice": "이번 배치 승인 Firewall Tips와 동일 기능 의미 중복",
 "Server Advice": "이번 배치 승인 Server Tips와 동일 기능 의미 중복",
 "Spay Advice": "직전 승인 Spay Tips와 동일 기능 의미 중복",
 "Barbecue Advice": "이번 배치 승인 Barbecue Tips와 동일 기능 의미 중복",
 "Consumption Advice": "직전 승인 Consumption Tips와 동일 기능 의미 중복",
}

R = {
 "Fjord Retreat": "terrain 대상 결합 불성립", "Insulin Tournament": "terrain 대상 결합 불성립",
 "Savanna Flyer": "terrain 대상 결합 불성립", "Tundra App": "지명 지칭으로 제품 불분명",
 "Prairie Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Marsh Advice": "선례 기각(App 기각) 계열",
 "Cove Workbook": "선례 기각(App 기각) 계열", "Cliff Mode": "선례 기각(App 기각) 계열",
 "Cavern Spec": "선례 기각(App 기각) 계열", "Oasis Quantity": "선례 기각(App 기각) 계열",
 "Dune Login": "선례 기각(App 기각) 계열", "Whale Analysis": "선례 기각(App 기각) 계열",
 "Dolphin Coach": "선례 기각(App 기각) 계열", "Penguin Habit": "선례 기각(App 기각) 계열",
 "Flamingo Tracker": "선례 기각(App 기각) 계열", "Turtle Flow": "선례 기각(App 기각) 계열",
 "Moose Hub": "선례 기각(App 기각) 계열", "Bison Desk": "선례 기각(App 기각) 계열",
 "Reindeer Radar": "선례 기각(App 기각) 계열", "Yield Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Campaign Workbook": "워크북 대상 불분명", "Attribution Spec": "사양 참조로 제품 불분명",
 "Syndication Quantity": "수량 대상 불분명", "Bandwidth Analysis": "선례 기각(App 기각) 계열",
 "Credential Coach": "코칭 대상 불분명", "Backup Habit": "결합 불성립",
 "Migration Advice": "선례 기각(App 기각) 계열", "Knowledge Workbook": "워크북 대상 불분명",
 "Assessment Mode": "기능 토글로 읽혀 제품 불분명", "Catering Spec": "사양 참조로 제품 불분명",
 "Sterilization Coach": "코칭 대상 불분명", "Program Habit": "선례 기각(App 기각) 계열",
 "Lawyer Match": "매칭·경기 중의로 불분명", "Attorney Range": "결합 불성립",
 "Court Resignation": "결합 불성립", "Server Tips2": "",
 "Spay Advice2": "", "Braces Workbook": "워크북 대상 불분명",
 "Snack Mode": "기능 토글로 읽혀 제품 불분명", "Curtain Spec": "사양 참조로 제품 불분명",
 "Facial Quantity": "수량 대상 불분명", "Tablet Login": "선례 기각(App 기각) 계열",
 "Freon Analysis": "선례 기각(App 상표 기각) 계열", "Hinge Coach": "선례 기각(App 상표 기각) 계열",
 "Apostille Habit": "결합 불성립", "Judge Bridge": "선례 기각(App 기각) 계열(Bridge 중의)",
 "Jury Keeper": "관리인 지칭으로 제품 불분명(Keeper 기각 라인)", "Lawsuit Report": "보고서 대상 불분명(Summary 기각 평행)",
 "Divorce Pass": "통행증·패스 중의로 불분명", "Custody Tariff": "관세·요율 결합 불성립",
 "Immigration Graph": "그래프 지칭으로 제품 불분명(Graph 기각 선례)", "Testament Rank": "순위 지칭으로 제품 불분명",
 "Notary Barcode": "결합 불성립", "Mediation Weight": "결합 불성립(속성 지칭)",
 "Guardianship Reception": "리셉션·수신 중의로 불분명",
 "Hallway App": "복도 지칭으로 제품 불분명", "Barbecue Tips2": "",
 "Theory Advice": "선례 기각(App 기각) 계열", "Visit Workbook": "워크북 대상 불분명",
 "Installment Mode": "기능 토글로 읽혀 제품 불분명", "Trademark Spec": "사양 참조로 제품 불분명",
 "Crossdock Quantity": "수량 대상 불분명", "Valuation Login": "제품 불분명",
 "Broker Analysis": "분석 대상 불분명", "Grievance Coach": "코칭 대상 불분명",
 "Paving Habit": "결합 불성립", "Patent Point": "지점 지칭으로 제품 불분명(Point 기각 선례)",
 "Copyright Atlas": "지도책 지칭으로 제품 불분명", "Migraine Renewal": "결합 불성립",
 "Insomnia Nomination": "결합 불성립", "Skydiving Verification": "결합 불성립",
 "Acne Simulator": "결합 불성립", "Snowboarding Recipe": "결합 불성립",
 "Ziplining Expense": "결합 불성립", "Psoriasis Newsletter": "결합 불성립",
 "Sledding Onboarding": "결합 불성립", "Vertigo Checkin": "결합 불성립",
 "Diving Weight": "결합 불성립(속성 지칭)", "Arthritis Distance": "결합 불성립",
 "Sailing Type": "결합 불성립(분류 대상 부자연)", "Menopause Clock": "결합 불성립",
 "Rafting Depth": "결합 불성립", "Pregnancy Height": "결합 불성립",
 "Climbing Pressure": "결합 불성립", "Fertility Load": "결합 불성립",
 "Biking Brightness": "결합 불성립", "Thyroid Frequency": "결합 불성립",
 "Golf Usage": "사용 지칭으로 제품 불분명", "Cholesterol Condition": "상태 명사로 제품명 부자연",
 "Fishing Cycle": "주기 지칭으로 제품 불분명", "Hypertension Breakdown": "내역·고장 중의로 불분명",
 "Camping Followup": "후속 지칭으로 제품 불분명", "Anemia Approval": "승인 지칭으로 제품 불분명",
 "Glamping Questionnaire": "설문 대상 불분명", "Heartburn Utilization": "활용 지칭으로 제품 불분명",
 "Stargazing Depreciation": "결합 불성립", "Constipation Resignation": "결합 불성립",
 "Birdwatching Tuner": "튜너 기능 지칭으로 제품 불분명", "Concussion Tutorial": "terrain 대상 결합 불성립",
 "Canyon Timetable": "terrain 대상 결합 불성립", "Sprain Opinion": "terrain 대상 결합 불성립",
 "Geyser Gift": "결합 불성립", "Fracture Retreat": "terrain 대상 결합 불성립",
 "Fjord Tournament": "terrain 대상 결합 불성립", "Insulin Flyer": "terrain 대상 결합 불성립",
 "Savanna App": "지명 지칭으로 제품 불분명", "Tundra Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Prairie Advice": "선례 기각(App 기각) 계열", "Marsh Workbook": "선례 기각(App 기각) 계열",
 "Cove Mode": "선례 기각(App 기각) 계열", "Cliff Spec": "선례 기각(App 기각) 계열",
 "Cavern Quantity": "선례 기각(App 기각) 계열", "Oasis Login": "선례 기각(App 기각) 계열",
 "Dune Analysis": "선례 기각(App 기각) 계열", "Whale Coach": "선례 기각(App 기각) 계열",
 "Dolphin Habit": "선례 기각(App 기각) 계열", "Penguin Tracker": "선례 기각(App 기각) 계열",
 "Flamingo Flow": "선례 기각(App 기각) 계열", "Turtle Hub": "선례 기각(App 기각) 계열",
 "Moose Desk": "선례 기각(App 기각) 계열", "Bison Radar": "선례 기각(App 기각) 계열",
 "Reindeer Relay": "선례 기각(App 기각) 계열", "Yield Advice": "선례 기각(App 기각) 계열",
 "Consumption Workbook": "워크북 대상 불분명", "Campaign Mode": "기능 토글로 읽혀 제품 불분명",
 "Attribution Quantity": "수량 대상 불분명", "Syndication Login": "제품 불분명",
 "Bandwidth Coach": "선례 기각(App 기각) 계열", "Credential Habit": "결합 불성립",
 "Churn Tips2": "", "Firewall Advice2": "",
 "Migration Workbook": "선례 기각(App 기각) 계열", "Knowledge Mode": "기능 토글로 읽혀 제품 불분명",
 "Assessment Spec": "사양 참조로 제품 불분명", "Catering Quantity": "수량 대상 불분명",
 "Sterilization Habit": "결합 불성립", "Lawyer Validation": "결합 불성립",
 "Attorney Limit": "결합 불성립", "Court Hazard": "결합 불성립",
 "Tuneup Tips2": "", "Server Advice2": "",
 "Spay Workbook": "워크북 대상 불분명", "Braces Mode": "기능 토글로 읽혀 제품 불분명",
 "Snack Spec": "사양 참조로 제품 불분명", "Curtain Quantity": "수량 대상 불분명",
 "Facial Login": "제품 불분명", "Tablet Analysis": "선례 기각(App 기각) 계열",
 "Freon Coach": "선례 기각(App 상표 기각) 계열", "Hinge Habit": "선례 기각(App 상표 기각) 계열",
 "Judge Signal": "선례 기각(App 기각) 계열(Signal 기각 선례)", "Jury Manager": "관리자 지칭으로 제품 불분명(Manager 기각 라인)",
 "Lawsuit Log": "로그 대상 불분명(Record 기각 평행)", "Divorce Voucher": "바우처 결합 불성립",
 "Custody Value": "가치 속성 지칭으로 제품 불분명", "Immigration Label": "라벨 지칭으로 제품 불분명",
 "Testament Trend": "추세 지칭으로 제품 불분명", "Notary Appointment": "약속 대상 불분명",
 "Mediation Distance": "결합 불성립", "Guardianship Followup": "후속 지칭으로 제품 불분명",
 "Thumbnail App2": "", "Hallway Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Theory Workbook": "선례 기각(App 기각) 계열", "Visit Mode": "기능 토글로 읽혀 제품 불분명",
 "Installment Spec": "사양 참조로 제품 불분명", "Trademark Quantity": "수량 대상 불분명",
 "Crossdock Login": "제품 불분명", "Valuation Analysis": "분석 대상 불분명",
 "Broker Coach": "코칭 대상 불분명", "Grievance Habit": "결합 불성립",
 "Patent Map": "지도 지칭으로 제품 불분명(Map 기각 선례)", "Copyright Keeper": "관리인 지칭으로 제품 불분명(Keeper 기각 라인)",
 "Migraine Quote": "인용·견적 중의로 불분명", "Insomnia Correction": "결합 불성립",
 "Skydiving Simulator": "결합 불성립", "Acne Predictor": "예측 대상 불분명",
 "Eczema Diary2": "", "Ziplining Newsletter": "결합 불성립",
 "Psoriasis Inventory": "결합 불성립", "Sledding Checkin": "결합 불성립",
 "Vertigo Size": "결합 불성립(속성 지칭)", "Diving Distance": "결합 불성립",
 "Arthritis Range": "결합 불성립", "Sailing Clock": "결합 불성립",
 "Menopause Time": "결합 불성립", "Rafting Height": "결합 불성립",
 "Pregnancy Width": "결합 불성립", "Climbing Load": "결합 불성립",
 "Fertility Voltage": "결합 불성립",
}
del R["Server Tips2"]
del R["Spay Advice2"]
del R["Barbecue Tips2"]
del R["Churn Tips2"]
del R["Firewall Advice2"]
del R["Tuneup Tips2"]
del R["Server Advice2"]
del R["Thumbnail App2"]
del R["Eczema Diary2"]
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
out = base + r"\_dec_c32.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
