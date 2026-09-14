# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk10_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Leak App": (0.55, "누수 감지·신고 관리 앱(실재)"),
 "Leak Tips": (0.55, "Leak App 승인 선례의 Tips 평행"),
 "Tour Tips": (0.55, "Tour App 승인 선례의 Tips 평행"),
 "Rider App": (0.55, "배달·이동 라이더용 앱(실재)"),
 "Rider Tips": (0.55, "Rider App 승인 선례의 Tips 평행"),
 "Candidate Tips": (0.55, "Candidate App 승인 선례의 Tips 평행"),
 "Waxing App": (0.55, "왁싱 시술 예약·관리 앱(실재)"),
 "Waxing Tips": (0.55, "Waxing App 승인 선례의 Tips 평행"),
 "Wardrobe App": (0.55, "옷장 정리·코디 기록 앱(실재)"),
 "Benefits App": (0.6, "직원 복리후생 관리 앱(실재)"),
 "Complaint App": (0.6, "민원 접수·처리 관리 앱(실재)"),
 "Complaint Tips": (0.55, "Complaint App 승인 선례의 Tips 평행"),
 "Attorney Match": (0.55, "변호사-의뢰인 매칭 앱(실재)"),
 "Syrup Tips": (0.55, "Syrup App 승인 선례의 Tips 평행"),
 "Bumper Tips": (0.55, "Bumper App 승인 선례의 Tips 평행"),
 "Sledding Guide": (0.55, "슬레딩 명소 가이드(Climbing Guide 평행)"),
 "Anemia Video": (0.55, "빈혈 관리 영상 가이드(Heartburn Video 평행)"),
 "Migraine Helper": (0.55, "편두통 관리 도우미(Insomnia Helper 평행)"),
 "Acne Record": (0.55, "여드름 발작 기록(Eczema Record 평행)"),
}

R_DUP = {
 "Tour Advice": "직전 승인 Tour Tips와 동일 기능 의미 중복",
 "Candidate Advice": "직전 승인 Candidate Tips와 동일 기능 의미 중복",
 "Drum Advice": "직전 승인 Drum Tips와 동일 기능 의미 중복",
 "Warranty Advice": "직전 승인 Warranty Tips와 동일 기능 의미 중복",
 "Zoning Advice": "직전 승인 Zoning Tips와 동일 기능 의미 중복",
 "Pastry Advice": "직전 승인 Pastry Tips와 동일 기능 의미 중복",
 "Syrup Advice": "이번 배치 승인 Syrup Tips와 동일 기능 의미 중복",
 "Bumper Advice": "이번 배치 승인 Bumper Tips와 동일 기능 의미 중복",
}

R = {
 "Glamping Refund": "결합 불성립", "Heartburn Expense": "결합 불성립",
 "Stargazing Claim": "결합 불성립", "Constipation Onboarding": "결합 불성립",
 "Birdwatching Length": "결합 불성립(속성 지칭)", "Concussion Weight": "결합 불성립(속성 지칭)",
 "Canyon Range": "결합 불성립", "Sprain Limit": "결합 불성립",
 "Geyser Type": "결합 불성립(분류 대상 부자연)", "Fracture Clock": "결합 불성립",
 "Fjord Time": "결합 불성립", "Insulin Speed": "결합 불성립",
 "Savanna Depth": "결합 불성립", "Tundra Height": "결합 불성립",
 "Prairie Width": "결합 불성립", "Marsh Temperature": "결합 불성립",
 "Cove Pressure": "결합 불성립", "Cliff Load": "결합 불성립",
 "Cavern Voltage": "결합 불성립", "Oasis Wattage": "결합 불성립",
 "Dune Brightness": "결합 불성립", "Whale Frequency": "결합 불성립",
 "Dolphin Compatibility": "상태 명사로 제품명 부자연", "Penguin Capacity": "상태 명사로 제품명 부자연",
 "Flamingo Usage": "사용 지칭으로 제품 불분명", "Turtle Condition": "상태 명사로 제품명 부자연",
 "Moose Humidity": "결합 불성립", "Bison Episode": "결합 불성립",
 "Reindeer Cycle": "주기 지칭으로 제품 불분명", "Provider Workbook": "워크북 대상 불분명",
 "Warehouse Quantity": "수량 대상 불분명", "Adjuster Analysis": "분석 대상 불분명",
 "Bid Habit": "결합 불성립", "Restock Workbook": "워크북 대상 불분명",
 "Shuttle Mode": "기능 토글로 읽혀 제품 불분명", "Classroom Spec": "사양 참조로 제품 불분명",
 "Calibration Quantity": "수량 대상 불분명", "Rotation Login": "제품 불분명",
 "Stewardship Coach": "코칭 대상 불분명", "Lawyer Widget": "위젯 기능 지칭으로 제품 불분명",
 "Court Checkin": "결합 불성립", "Judge Evaluation": "평가 대상 불분명",
 "Bolt Workbook": "워크북 대상 불분명", "Linguist Mode": "기능 토글로 읽혀 제품 불분명",
 "Damage Spec": "사양 참조로 제품 불분명", "Vow Login": "제품 불분명",
 "Winterization Coach": "코칭 대상 불분명", "Undercarriage Habit": "결합 불성립",
 "Jury Relay": "릴레이 지칭으로 제품 불분명", "Lawsuit Trail": "트레일·경로 중의로 불분명",
 "Divorce Passport": "결합 불성립", "Custody Receipt": "결합 불성립",
 "Immigration Debt": "결합 불성립", "Testament Discount": "결합 불성립",
 "Notary Checker": "체크 대상 불분명", "Mediation Account": "결합 불성립",
 "Guardianship Review": "리뷰 대상 불분명", "Trademark Voltage": "결합 불성립",
 "Patent Guarantor": "결합 불성립", "Anesthesia Mode": "기능 토글로 읽혀 제품 불분명",
 "Fieldtrip Spec": "사양 참조로 제품 불분명", "Polish Quantity": "수량 대상 불분명",
 "Thermocouple Analysis": "분석 대상 불분명", "Panic Coach": "코칭 대상 불분명",
 "Pool Habit": "결합 불성립", "Copyright Radar": "레이더 기능 지칭으로 제품 불분명",
 "Migraine Guardian": "감시자 명사 결합 불성립", "Insomnia Rank": "순위 대상 불분명",
 "Skydiving Guarantee": "결합 불성립", "Snowboarding Forecast": "예측 대상 불분명",
 "Eczema Deadline": "결합 불성립", "Ziplining Diagnostic": "진단 대상 불분명",
 "Psoriasis Progress": "진행 대상 불분명", "Vertigo Rating": "평가 대상 불분명",
 "Diving Account": "결합 불성립", "Arthritis Case": "결합 불성립(Case 계열 기각 선례)",
 "Sailing Lookup": "탐색 대상 불분명", "Menopause Ping": "결합 불성립",
 "Rafting Eligibility": "결합 불성립", "Pregnancy Broadcast": "결합 불성립",
 "Climbing Feedback": "결합 불성립", "Fertility Invoice": "결합 불성립",
 "Biking Warranty": "결합 불성립", "Thyroid Deposit": "결합 불성립",
 "Golf Correction": "결합 불성립", "Cholesterol Revision": "결합 불성립",
 "Fishing Simulator": "결합 불성립", "Hypertension Predictor": "예측 대상 불분명",
 "Camping Recipe": "결합 불성립", "Glamping Expense": "결합 불성립",
 "Heartburn Newsletter": "결합 불성립", "Stargazing Onboarding": "결합 불성립",
 "Constipation Checkin": "결합 불성립", "Birdwatching Weight": "결합 불성립(속성 지칭)",
 "Concussion Distance": "결합 불성립", "Canyon Limit": "결합 불성립",
 "Sprain Type": "결합 불성립(분류 대상 부자연)", "Geyser Clock": "결합 불성립",
 "Fracture Time": "결합 불성립", "Fjord Speed": "결합 불성립",
 "Insulin Depth": "결합 불성립", "Savanna Height": "결합 불성립",
 "Tundra Width": "결합 불성립", "Prairie Temperature": "결합 불성립",
 "Marsh Pressure": "결합 불성립", "Cove Load": "결합 불성립",
 "Cliff Voltage": "결합 불성립", "Cavern Wattage": "결합 불성립",
 "Oasis Brightness": "결합 불성립", "Dune Frequency": "결합 불성립",
 "Whale Compatibility": "상태 명사로 제품명 부자연", "Dolphin Capacity": "상태 명사로 제품명 부자연",
 "Penguin Usage": "사용 지칭으로 제품 불분명", "Flamingo Condition": "상태 명사로 제품명 부자연",
 "Turtle Humidity": "결합 불성립", "Moose Episode": "결합 불성립",
 "Bison Cycle": "주기 지칭으로 제품 불분명", "Reindeer Breakdown": "내역·고장 중의로 불분명",
 "Buff App": "버핑 대상 불분명으로 용도 불분명", "Drum Workbook": "워크북 대상 불분명",
 "Provider Mode": "기능 토글로 읽혀 제품 불분명", "Warehouse Login": "제품 불분명",
 "Adjuster Coach": "코칭 대상 불분명", "Warranty Workbook": "워크북 대상 불분명",
 "Restock Mode": "기능 토글로 읽혀 제품 불분명", "Shuttle Spec": "사양 참조로 제품 불분명",
 "Classroom Quantity": "수량 대상 불분명", "Calibration Login": "제품 불분명",
 "Rotation Analysis": "분석 대상 불분명", "Stewardship Habit": "결합 불성립",
 "Lawyer Repository": "결합 불성립", "Attorney Validation": "결합 불성립",
 "Court Size": "규모 지칭으로 제품 불분명", "Judge Questionnaire": "문진 대상 불분명",
 "Zoning Workbook": "워크북 대상 불분명", "Bolt Mode": "기능 토글로 읽혀 제품 불분명",
 "Linguist Spec": "사양 참조로 제품 불분명", "Damage Quantity": "수량 대상 불분명",
 "Vow Analysis": "분석 대상 불분명", "Winterization Habit": "결합 불성립",
 "Jury Vault": "금고 지칭으로 제품 불분명", "Lawsuit Chain": "체인 지칭으로 제품 불분명",
 "Divorce Lobby": "로비 지칭으로 제품 불분명", "Custody Code": "코드 지칭으로 제품 불분명",
 "Immigration Fund": "결합 불성립", "Testament Arrears": "결합 불성립",
 "Notary Detector": "탐지 대상 불분명", "Mediation Case": "결합 불성립(Case 계열 기각 선례)",
 "Guardianship Recipe": "결합 불성립", "Trademark Wattage": "결합 불성립",
 "Patent Tuner": "튜너 결합 불성립", "Pastry Workbook": "워크북 대상 불분명",
 "Anesthesia Spec": "사양 참조로 제품 불분명", "Fieldtrip Quantity": "수량 대상 불분명",
 "Polish Login": "제품 불분명", "Thermocouple Coach": "코칭 대상 불분명",
 "Panic Habit": "결합 불성립", "Copyright Relay": "릴레이 지칭으로 제품 불분명",
 "Insomnia Trend": "결합 불성립", "Skydiving Record": "기록 대상 불분명",
 "Acne Copy": "복사·원고 중의로 불분명", "Snowboarding Deadline": "결합 불성립",
 "Eczema Duration": "기간 속성 지칭으로 제품명 부자연", "Ziplining Progress": "진행 대상 불분명",
 "Psoriasis Authorization": "결합 불성립", "Sledding Rating": "평가 대상 불분명",
 "Vertigo Agreement": "결합 불성립", "Diving Case": "결합 불성립(Case 계열 기각 선례)",
 "Arthritis Match": "매칭 대상 불분명", "Sailing Ping": "결합 불성립",
 "Menopause Model": "모델 지칭으로 제품 불분명", "Rafting Broadcast": "결합 불성립",
 "Pregnancy Barcode": "결합 불성립",
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
out = base + r"\_dec_c11.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
