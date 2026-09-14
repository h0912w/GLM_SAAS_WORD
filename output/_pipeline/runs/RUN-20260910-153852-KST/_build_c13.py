# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk12_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Psoriasis Guide": (0.55, "건선 관리 가이드 콘텐츠(Arthritis Guide 평행)"),
 "Seating App": (0.55, "좌석 배치 관리 앱(실재)"),
 "Seating Tips": (0.55, "Seating App 승인 선례의 Tips 평행"),
 "Chargeback App": (0.6, "차지백 대응 관리 앱(실재)"),
 "Chargeback Tips": (0.55, "Chargeback App 승인 선례의 Tips 평행"),
 "Neuter App": (0.55, "반려동물 중절 수술 예약·사후관리 앱(실재)"),
 "Neuter Tips": (0.55, "Neuter App 승인 선례의 Tips 평행"),
 "Tutoring App": (0.6, "과외·튜터링 매칭 앱(실재)"),
 "Pothole Tips": (0.55, "Pothole App 승인 선례의 Tips 평행"),
 "Whitening Tips": (0.55, "Whitening App 승인 선례의 Tips 평행"),
 "Discovery Tips": (0.55, "Discovery App 승인 선례의 Tips 평행"),
 "Dine App": (0.55, "레스토랑 예약·외식 관리 앱(실재)"),
 "Watermark App": (0.55, "사진·문서 워터마크 앱(실재)"),
 "Ziplining Guide": (0.55, "짚라인 투어 가이드(Climbing Guide 평행)"),
 "Hypertension Video": (0.55, "고혈압 관리 영상 가이드(Anemia Video 평행)"),
 "Patent Timetable": (0.55, "특허 절차 일정 관리(Patent Followup 평행)"),
 "Patent Opinion": (0.55, "특허 의견서 관리(실재 업무)"),
}

R_DUP = {
 "Skimmer Advice": "직전 승인 Skimmer Tips와 동일 기능 의미 중복",
 "Discovery Advice": "직전 승인 Discovery Tips와 동일 기능 의미 중복",
 "Whitening Advice": "직전 승인 Whitening Tips와 동일 기능 의미 중복",
 "Diaper Advice": "직전 승인 Diaper Tips와 동일 기능 의미 중복",
 "Newsletter Advice": "직전 승인 Newsletter Tips와 동일 기능 의미 중복",
}

R = {
 "Eczema Diagnostic": "진단 대상 불분명", "Ziplining Template": "결합 불성립",
 "Sledding Reply": "결합 불성립", "Vertigo Account": "결합 불성립",
 "Diving Validation": "결합 불성립", "Arthritis Lookup": "탐색 대상 불분명",
 "Sailing Availability": "상태 명사로 제품명 부자연", "Menopause Eligibility": "결합 불성립",
 "Rafting Appointment": "약속 대상 불분명", "Pregnancy Feedback": "결합 불성립",
 "Climbing Quote": "인용·견적 중의로 불분명", "Fertility Warranty": "결합 불성립",
 "Biking Nomination": "결합 불성립", "Thyroid Correction": "결합 불성립",
 "Golf Verification": "결합 불성립", "Cholesterol Simulator": "결합 불성립",
 "Fishing Review": "리뷰 대상 불분명", "Hypertension Recipe": "결합 불성립",
 "Camping Refund": "결합 불성립", "Anemia Expense": "결합 불성립",
 "Glamping Claim": "결합 불성립", "Heartburn Onboarding": "결합 불성립",
 "Stargazing Length": "결합 불성립(속성 지칭)", "Constipation Weight": "결합 불성립(속성 지칭)",
 "Birdwatching Limit": "결합 불성립", "Concussion Type": "결합 불성립(분류 대상 부자연)",
 "Canyon Time": "결합 불성립", "Sprain Speed": "결합 불성립",
 "Geyser Depth": "결합 불성립", "Fracture Height": "결합 불성립",
 "Fjord Width": "결합 불성립", "Insulin Temperature": "결합 불성립",
 "Savanna Pressure": "결합 불성립", "Tundra Load": "결합 불성립",
 "Prairie Voltage": "결합 불성립", "Marsh Wattage": "결합 불성립",
 "Cove Brightness": "결합 불성립", "Cliff Frequency": "결합 불성립",
 "Cavern Compatibility": "상태 명사로 제품명 부자연", "Oasis Capacity": "상태 명사로 제품명 부자연",
 "Dune Usage": "사용 지칭으로 제품 불분명", "Whale Condition": "상태 명사로 제품명 부자연",
 "Dolphin Humidity": "결합 불성립", "Penguin Episode": "결합 불성립",
 "Flamingo Cycle": "주기 지칭으로 제품 불분명", "Turtle Breakdown": "내역·고장 중의로 불분명",
 "Moose Sensor": "결합 불성립", "Bison Reception": "리셉션·수신 중의로 불분명",
 "Reindeer Followup": "후속 지칭으로 제품 불분명", "Buff Workbook": "워크북 대상 불분명",
 "Leak Mode": "기능 토글로 읽혀 제품 불분명", "Tour Spec": "사양 참조로 제품 불분명",
 "Drum Quantity": "수량 대상 불분명", "Provider Login": "제품 불분명",
 "Warehouse Habit": "결합 불성립", "Rider Mode": "기능 토글로 읽혀 제품 불분명",
 "Candidate Spec": "사양 참조로 제품 불분명", "Warranty Quantity": "수량 대상 불분명",
 "Restock Login": "제품 불분명", "Shuttle Analysis": "분석 대상 불분명",
 "Classroom Coach": "코칭 대상 불분명", "Calibration Habit": "결합 불성립",
 "Lawyer Converter": "변환 대상 불분명", "Attorney Model": "모델 지칭으로 제품 불분명",
 "Court Distance": "결합 불성립", "Judge Requirement": "요건 지칭으로 제품 불분명",
 "Wardrobe Workbook": "워크북 대상 불분명", "Waxing Mode": "기능 토글로 읽혀 제품 불분명",
 "Syrup Spec": "사양 참조로 제품 불분명", "Zoning Quantity": "수량 대상 불분명",
 "Bolt Login": "제품 불분명", "Linguist Analysis": "분석 대상 불분명",
 "Damage Coach": "코칭 대상 불분명", "Jury Forge": "용광로 중의로 불분명",
 "Lawsuit Nexus": "연결점 중의로 불분명", "Divorce Window": "창문·기간 중의로 불분명",
 "Custody Slip": "전표·미끄러짐 중의로 불분명", "Immigration Charge": "요금·혐의 중의로 불분명",
 "Testament Markup": "가산금·마크업 중의로 불분명", "Notary Guardian": "감시자 명사 결합 불성립",
 "Mediation Lookup": "탐색 대상 불분명", "Guardianship Refund": "결합 불성립",
 "Trademark Compatibility": "상태 명사로 제품명 부자연", "Benefits Workbook": "워크북 대상 불분명",
 "Complaint Mode": "기능 토글로 읽혀 제품 불분명", "Bumper Spec": "사양 참조로 제품 불분명",
 "Pastry Quantity": "수량 대상 불분명", "Anesthesia Analysis": "분석 대상 불분명",
 "Fieldtrip Coach": "코칭 대상 불분명", "Polish Habit": "결합 불성립",
 "Copyright Beacon": "비컨 기능 지칭으로 제품 불분명", "Migraine Streak": "앱 기능 지칭으로 제품 불분명",
 "Insomnia Guarantee": "결합 불성립", "Skydiving Reference": "참조 대상 불분명",
 "Acne Forecast": "예측 대상 불분명", "Snowboarding Diagnostic": "진단 대상 불분명",
 "Eczema Progress": "진행 대상 불분명", "Psoriasis Rating": "평가 대상 불분명",
 "Sledding Account": "결합 불성립", "Vertigo Case": "결합 불성립(Case 계열 기각 선례)",
 "Diving Lookup": "탐색 대상 불분명", "Arthritis Ping": "결합 불성립",
 "Sailing Eligibility": "결합 불성립", "Menopause Broadcast": "결합 불성립",
 "Rafting Feedback": "결합 불성립", "Pregnancy Invoice": "결합 불성립",
 "Climbing Warranty": "결합 불성립", "Fertility Deposit": "결합 불성립",
 "Biking Correction": "결합 불성립", "Thyroid Revision": "결합 불성립",
 "Golf Simulator": "결합 불성립", "Cholesterol Predictor": "예측 대상 불분명",
 "Fishing Recipe": "결합 불성립", "Camping Expense": "결합 불성립",
 "Anemia Newsletter": "결합 불성립", "Glamping Onboarding": "결합 불성립",
 "Heartburn Checkin": "결합 불성립", "Stargazing Weight": "결합 불성립(속성 지칭)",
 "Constipation Distance": "결합 불성립", "Birdwatching Type": "결합 불성립(분류 대상 부자연)",
 "Concussion Clock": "결합 불성립", "Canyon Speed": "결합 불성립",
 "Sprain Depth": "결합 불성립", "Geyser Height": "결합 불성립",
 "Fracture Width": "결합 불성립", "Fjord Temperature": "결합 불성립",
 "Insulin Pressure": "결합 불성립", "Savanna Load": "결합 불성립",
 "Tundra Voltage": "결합 불성립", "Prairie Wattage": "결합 불성립",
 "Marsh Brightness": "결합 불성립", "Cove Frequency": "결합 불성립",
 "Cliff Compatibility": "상태 명사로 제품명 부자연", "Cavern Capacity": "상태 명사로 제품명 부자연",
 "Oasis Usage": "사용 지칭으로 제품 불분명", "Dune Condition": "상태 명사로 제품명 부자연",
 "Whale Humidity": "결합 불성립", "Dolphin Episode": "결합 불성립",
 "Penguin Cycle": "주기 지칭으로 제품 불분명", "Flamingo Breakdown": "내역·고장 중의로 불분명",
 "Turtle Sensor": "결합 불성립", "Moose Reception": "리셉션·수신 중의로 불분명",
 "Bison Followup": "후속 지칭으로 제품 불분명", "Reindeer Approval": "승인 지칭으로 제품 불분명",
 "Skimmer Workbook": "워크북 대상 불분명", "Buff Mode": "기능 토글로 읽혀 제품 불분명",
 "Leak Spec": "사양 참조로 제품 불분명", "Tour Quantity": "수량 대상 불분명",
 "Drum Login": "제품 불분명", "Provider Analysis": "분석 대상 불분명",
 "Rider Spec": "사양 참조로 제품 불분명", "Candidate Quantity": "수량 대상 불분명",
 "Warranty Login": "제품 불분명", "Restock Analysis": "분석 대상 불분명",
 "Shuttle Coach": "코칭 대상 불분명", "Classroom Habit": "결합 불성립",
 "Lawyer Generator": "생성 대상 불분명", "Attorney Availability": "상태 명사로 제품명 부자연",
 "Court Range": "결합 불성립", "Judge Depreciation": "결합 불성립",
 "Diaper Workbook": "워크북 대상 불분명", "Wardrobe Mode": "기능 토글로 읽혀 제품 불분명",
 "Waxing Spec": "사양 참조로 제품 불분명", "Syrup Quantity": "수량 대상 불분명",
 "Zoning Login": "제품 불분명", "Bolt Analysis": "분석 대상 불분명",
 "Linguist Coach": "코칭 대상 불분명", "Damage Habit": "결합 불성립",
 "Jury Cascade": "폭포·연쇄 중의로 불분명", "Lawsuit Atlas": "지도집 중의로 불분명",
 "Divorce Roll": "말다·명단 중의로 불분명", "Custody Sample": "표본 지칭으로 제품 불분명",
 "Immigration Duty": "의무·관세 중의로 불분명", "Testament Redemption": "결합 불성립",
 "Notary Helper": "도우미 대상 불분명", "Mediation Ping": "결합 불성립",
 "Guardianship Expense": "결합 불성립", "Trademark Capacity": "상태 명사로 제품명 부자연",
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
out = base + r"\_dec_c13.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
