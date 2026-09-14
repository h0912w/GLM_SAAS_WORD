# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk27_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Broker App": (0.55, "중개 거래·고객 관리 앱(실재)"),
 "Broker Tips": (0.55, "Broker App 승인 선례의 Tips 평행"),
 "Grievance Tips": (0.55, "Grievance App 승인 선례의 Tips 평행"),
 "Valuation App": (0.55, "자산 가치 평가 관리 앱(실재)"),
 "Syndication App": (0.55, "콘텐츠 신디케이션 배포 관리 앱(실재)"),
 "Lawyer Template": (0.55, "법률 문서 템플릿 관리(Notary Template 평행)"),
 "Vertigo Video": (0.55, "어지럼증 관리 영상 가이드(Hypertension Video 평행)"),
 "Vertigo Diary": (0.55, "어지럼증 증상 기록 일지(Hypertension Diary 평행)"),
 "Sledding Video": (0.55, "썰매 강습 영상 가이드(Golf Video 평행)"),
}

R_DUP = {
 "Apostille Advice": "직전 승인 Apostille Tips와 동일 기능 의미 중복",
 "Paving Advice": "직전 승인 Paving Tips와 동일 기능 의미 중복",
 "Credential Advice": "직전 승인 Credential Tips와 동일 기능 의미 중복",
 "Sterilization Advice": "직전 승인 Sterilization Tips와 동일 기능 의미 중복",
 "Grievance Advice": "이번 배치 승인 Grievance Tips와 동일 기능 의미 중복",
}

R = {
 "Lawyer Authorization": "결합 불성립", "Attorney Inventory": "결합 불성립",
 "Court Approval": "승인 지칭으로 제품 불분명", "Freon App": "냉매 제품 상표(Freon)로 불분명",
 "Hinge Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가", "Apostille Advice2": "",
 "Invite Spec": "사양 참조로 제품 불분명", "Coping Login": "제품 불분명",
 "Wheel Analysis": "분석 대상 불분명", "Cistern Coach": "코칭 대상 불분명",
 "Souvenir Habit": "결합 불성립", "Judge Desk": "선례 기각(App 기각) 계열",
 "Jury Route": "경로 지칭으로 제품 불분명", "Lawsuit Chart": "도표 지칭으로 제품 불분명(Graph 기각 선례)",
 "Divorce Bill": "법안·고지서 중의로 불분명", "Custody Sum": "합계·요약 중의로 불분명",
 "Immigration Discount": "할인 결합 불성립", "Testament Detector": "탐지 도구 지칭으로 제품 불분명",
 "Notary Match": "매칭·경기 중의로 불분명", "Mediation Expense": "결합 불성립",
 "Guardianship Capacity": "상태 명사로 제품명 부자연", "Trademark Retreat": "결합 불성립",
 "Grievance Tips2": "", "Suspension Workbook": "워크북 대상 불분명",
 "Streetlight Mode": "기능 토글로 읽혀 제품 불분명", "Publisher Spec": "사양 참조로 제품 불분명",
 "Salary Quantity": "수량 대상 불분명", "Background Login": "선례 기각(App 기각) 계열",
 "Windshield Analysis": "분석 대상 불분명", "Bakery Coach": "코칭 대상 불분명",
 "Exam Habit": "결합 불성립", "Patent Bridge": "다리·연결 중의로 불분명",
 "Copyright Scale": "저울·규모 중의로 불분명", "Migraine Model": "모델 지칭으로 제품 불분명",
 "Insomnia Appointment": "약속 대상 불분명", "Skydiving Quote": "인용·견적 중의로 불분명",
 "Acne Warranty": "결합 불성립", "Snowboarding Correction": "결합 불성립",
 "Eczema Revision": "결합 불성립", "Ziplining Simulator": "결합 불성립",
 "Psoriasis Predictor": "예측 대상 불분명", "Sledding Recipe": "결합 불성립",
 "Diving Expense": "결합 불성립", "Arthritis Newsletter": "결합 불성립",
 "Sailing Onboarding": "결합 불성립", "Menopause Checkin": "결합 불성립",
 "Rafting Weight": "결합 불성립(속성 지칭)", "Pregnancy Distance": "결합 불성립",
 "Climbing Type": "결합 불성립(분류 대상 부자연)", "Fertility Clock": "결합 불성립",
 "Biking Depth": "결합 불성립", "Thyroid Height": "결합 불성립",
 "Golf Pressure": "결합 불성립", "Cholesterol Load": "결합 불성립",
 "Fishing Brightness": "결합 불성립", "Hypertension Frequency": "결합 불성립",
 "Camping Usage": "사용 지칭으로 제품 불분명", "Anemia Condition": "상태 명사로 제품명 부자연",
 "Glamping Cycle": "주기 지칭으로 제품 불분명", "Heartburn Breakdown": "내역·고장 중의로 불분명",
 "Stargazing Followup": "후속 지칭으로 제품 불분명", "Constipation Approval": "승인 지칭으로 제품 불분명",
 "Birdwatching Questionnaire": "설문 대상 불분명", "Concussion Utilization": "활용 지칭으로 제품 불분명",
 "Canyon Requirement": "요건 지칭으로 제품 불분명", "Sprain Depreciation": "결합 불성립",
 "Geyser Resignation": "결합 불성립", "Fracture Hazard": "결합 불성립",
 "Fjord Guarantor": "보증인 명사 결합 불성립", "Insulin Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Savanna Tutorial": "terrain 대상 결합 불성립", "Tundra Handbook": "terrain 대상 결합 불성립",
 "Prairie Timetable": "terrain 대상 결합 불성립", "Marsh Opinion": "terrain 대상 결합 불성립",
 "Cove Gift": "결합 불성립", "Cliff Retreat": "terrain 대상 결합 불성립",
 "Cavern Tournament": "terrain 대상 결합 불성립", "Oasis Flyer": "terrain 대상 결합 불성립",
 "Dune App": "지명 지칭·분석 플랫폼 상표(Dune)로 불분명", "Whale Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Dolphin Advice": "선례 기각(App 기각) 계열", "Penguin Workbook": "선례 기각(App 기각) 계열",
 "Flamingo Mode": "선례 기각(App 기각) 계열", "Turtle Spec": "선례 기각(App 기각) 계열",
 "Moose Quantity": "선례 기각(App 기각) 계열", "Bison Login": "선례 기각(App 기각) 계열",
 "Reindeer Analysis": "선례 기각(App 기각) 계열", "Bandwidth Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Backup Workbook": "워크북 대상 불분명", "Satisfaction Mode": "기능 토글로 읽혀 제품 불분명",
 "Offer Spec": "사양 참조로 제품 불분명", "Sponsor Quantity": "수량 대상 불분명",
 "Reservation Analysis": "분석 대상 불분명", "Grooming Coach": "코칭 대상 불분명",
 "Hygiene Habit": "결합 불성립", "Program Workbook": "선례 기각(App 기각) 계열",
 "Meal Mode": "기능 토글로 읽혀 제품 불분명", "Loyalty Coach": "코칭 대상 불분명",
 "Attorney Claim": "결합 불성립", "Court Matrix": "행렬·매트릭스 중의로 불분명",
 "Tablet App": "기기·정제 중의로 불분명", "Freon Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가",
 "Hinge Advice": "선례 기각(App 상표 기각) 계열", "Apostille Workbook": "워크북 대상 불분명",
 "Invite Quantity": "수량 대상 불분명", "Coping Analysis": "분석 대상 불분명",
 "Wheel Coach": "코칭 대상 불분명", "Cistern Habit": "결합 불성립",
 "Judge Radar": "선례 기각(App 기각) 계열", "Jury Rail": "레일 지칭으로 제품 불분명",
 "Lawsuit Bin": "쓰레기통·저장함 중의로 불분명", "Divorce Receipt": "영수증 결합 불성립",
 "Custody Debt": "부채 결합 불성립", "Immigration Arrears": "연체금 결합 불성립",
 "Testament Timer": "타이머 기능 지칭으로 제품 불분명", "Notary Validation": "결합 불성립",
 "Mediation Newsletter": "결합 불성립", "Guardianship Usage": "사용 지칭으로 제품 불분명",
 "Trademark Tournament": "결합 불성립", "Valuation App2": "",
 "Grievance Advice2": "", "Paving Workbook": "워크북 대상 불분명",
 "Suspension Mode": "기능 토글로 읽혀 제품 불분명", "Streetlight Spec": "사양 참조로 제품 불분명",
 "Publisher Quantity": "수량 대상 불분명", "Salary Login": "제품 불분명",
 "Background Analysis": "선례 기각(App 기각) 계열", "Windshield Coach": "코칭 대상 불분명",
 "Bakery Habit": "결합 불성립", "Patent Signal": "신호 지칭으로 제품 불분명(Signal 기각 선례)",
 "Copyright Route": "경로 지칭으로 제품 불분명", "Migraine Availability": "상태 명사로 제품명 부자연",
 "Insomnia Feedback": "결합 불성립", "Skydiving Warranty": "결합 불성립",
 "Acne Deposit": "결합 불성립", "Snowboarding Revision": "결합 불성립",
 "Eczema Payment": "결합 불성립", "Ziplining Predictor": "예측 대상 불분명",
 "Psoriasis Seal": "결합 불성립", "Diving Newsletter": "결합 불성립",
 "Arthritis Inventory": "결합 불성립", "Sailing Checkin": "결합 불성립",
 "Menopause Size": "결합 불성립(속성 지칭)", "Rafting Distance": "결합 불성립",
 "Pregnancy Range": "결합 불성립", "Climbing Clock": "결합 불성립",
 "Fertility Time": "결합 불성립", "Biking Height": "결합 불성립",
 "Thyroid Width": "결합 불성립", "Golf Load": "결합 불성립",
 "Cholesterol Voltage": "결합 불성립", "Fishing Frequency": "결합 불성립",
 "Hypertension Compatibility": "상태 명사로 제품명 부자연", "Camping Condition": "상태 명사로 제품명 부자연",
 "Anemia Humidity": "결합 불성립", "Glamping Breakdown": "내역·고장 중의로 불분명",
 "Heartburn Sensor": "결합 불성립", "Stargazing Approval": "승인 지칭으로 제품 불분명",
 "Constipation Matrix": "행렬·매트릭스 중의로 불분명", "Birdwatching Utilization": "활용 지칭으로 제품 불분명",
 "Concussion Benefit": "혜택 지칭으로 제품 불분명", "Canyon Depreciation": "결합 불성립",
 "Sprain Resignation": "결합 불성립", "Geyser Hazard": "결합 불성립",
 "Fracture Guarantor": "보증인 명사 결합 불성립", "Fjord Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Insulin Tutorial": "terrain 대상 결합 불성립", "Savanna Handbook": "terrain 대상 결합 불성립",
 "Tundra Timetable": "terrain 대상 결합 불성립", "Prairie Opinion": "terrain 대상 결합 불성립",
 "Marsh Gift": "결합 불성립", "Cove Retreat": "terrain 대상 결합 불성립",
 "Cliff Tournament": "terrain 대상 결합 불성립", "Cavern Flyer": "terrain 대상 결합 불성립",
 "Oasis App": "지명 지칭으로 제품 불분명", "Dune Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Whale Advice": "선례 기각(App 기각) 계열", "Dolphin Workbook": "선례 기각(App 기각) 계열",
 "Penguin Mode": "선례 기각(App 기각) 계열", "Flamingo Spec": "선례 기각(App 기각) 계열",
 "Turtle Quantity": "선례 기각(App 기각) 계열", "Moose Login": "선례 기각(App 기각) 계열",
 "Bison Analysis": "선례 기각(App 기각) 계열", "Reindeer Coach": "선례 기각(App 기각) 계열",
 "Bandwidth Advice": "선례 기각(App 기각) 계열", "Credential Workbook": "워크북 대상 불분명",
 "Backup Mode": "기능 토글로 읽혀 제품 불분명", "Satisfaction Spec": "사양 참조로 제품 불분명",
 "Offer Quantity": "수량 대상 불분명", "Sponsor Login": "제품 불분명",
}
del R["Apostille Advice2"]
del R["Grievance Tips2"]
del R["Valuation App2"]
del R["Grievance Advice2"]
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
out = base + r"\_dec_c28.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
