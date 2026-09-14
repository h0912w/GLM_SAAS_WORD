# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk9_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Drum App": (0.55, "드럼 레슨·연습 앱(실재)"),
 "Drum Tips": (0.55, "Drum App 승인 선례의 Tips 평행"),
 "Provider Tips": (0.55, "Provider App 승인 선례의 Tips 평행"),
 "Warranty App": (0.6, "보증·AS 이력 관리 앱(실재)"),
 "Warranty Tips": (0.55, "Warranty App 승인 선례의 Tips 평행"),
 "Restock Tips": (0.55, "Restock App 승인 선례의 Tips 평행"),
 "Zoning App": (0.55, "토지 용도지역 조회·알림 앱(실재)"),
 "Zoning Tips": (0.55, "Zoning App 승인 선례의 Tips 평행"),
 "Tour App": (0.55, "투어 예약·오디오 안내 앱(실재)"),
 "Bolt Tips": (0.55, "Bolt App 승인 선례의 Tips 평행"),
 "Pastry App": (0.55, "제과 레시피·주문 관리 앱(실재)"),
 "Pastry Tips": (0.55, "Pastry App 승인 선례의 Tips 평행"),
 "Candidate App": (0.6, "채용 후보자 관리 앱(실재)"),
 "Syrup App": (0.55, "단풍시럽 채집·제조 기록 앱(실재 니치)"),
 "Bumper App": (0.55, "범퍼 수리 견적 앱(실재)"),
 "Lawyer Message": (0.55, "사건 진행 안내 메시지(Notary Message 평행)"),
 "Custody Order": (0.55, "양육 명령 서류 관리(Immigration Petition 평행)"),
 "Camping Review": (0.55, "캠핑장 리뷰(Glamping Review 평행)"),
 "Vertigo Guide": (0.55, "어지럼 관리 가이드 콘텐츠(Arthritis Guide 평행)"),
}

R_DUP = {
 "Provider Advice": "직전 승인 Provider Tips와 동일 기능 의미 중복",
 "Restock Advice": "직전 승인 Restock Tips와 동일 기능 의미 중복",
 "Shuttle Advice": "직전 승인 Shuttle Tips와 동일 기능 의미 중복",
 "Bolt Advice": "이번 배치 승인 Bolt Tips와 동일 기능 의미 중복",
 "Linguist Advice": "직전 승인 Linguist Tips와 동일 기능 의미 중복",
 "Anesthesia Advice": "직전 승인 Anesthesia Tips와 동일 기능 의미 중복",
}

R = {
 "Fjord Type": "결합 불성립(분류 대상 부자연)", "Insulin Clock": "결합 불성립",
 "Savanna Time": "결합 불성립", "Tundra Speed": "결합 불성립",
 "Prairie Depth": "결합 불성립", "Marsh Height": "결합 불성립",
 "Cove Width": "결합 불성립", "Cliff Temperature": "결합 불성립",
 "Cavern Pressure": "결합 불성립", "Oasis Load": "결합 불성립",
 "Dune Voltage": "결합 불성립", "Whale Wattage": "결합 불성립",
 "Dolphin Brightness": "결합 불성립", "Penguin Frequency": "결합 불성립",
 "Flamingo Compatibility": "상태 명사로 제품명 부자연", "Turtle Capacity": "상태 명사로 제품명 부자연",
 "Moose Usage": "사용 지칭으로 제품 불분명", "Bison Condition": "상태 명사로 제품명 부자연",
 "Reindeer Humidity": "결합 불성립", "Warehouse Mode": "기능 토글로 읽혀 제품 불분명",
 "Adjuster Quantity": "수량 대상 불분명", "Bid Analysis": "분석 대상 불분명",
 "Fulfillment Coach": "코칭 대상 불분명", "Amenity Habit": "결합 불성립",
 "Classroom Workbook": "워크북 대상 불분명", "Calibration Mode": "기능 토글로 읽혀 제품 불분명",
 "Rotation Spec": "사양 참조로 제품 불분명", "Stewardship Login": "제품 불분명",
 "Content Coach": "코칭 대상 불분명", "Circulation Habit": "결합 불성립",
 "Attorney Account": "결합 불성립", "Court Claim": "결합 불성립",
 "Judge Approval": "승인 지칭으로 제품 불분명", "Damage Workbook": "워크북 대상 불분명",
 "Vow Spec": "사양 참조로 제품 불분명", "Winterization Login": "제품 불분명",
 "Undercarriage Analysis": "분석 대상 불분명", "Drainpipe Coach": "코칭 대상 불분명",
 "Tourist Habit": "결합 불성립", "Jury Desk": "데스크 지칭으로 제품 불분명",
 "Lawsuit Route": "경로 지칭으로 제품 불분명", "Divorce Chart": "차트 대상 불분명",
 "Immigration Loan": "결합 불성립", "Testament Due": "기한 지칭으로 제품 불분명",
 "Notary Recorder": "기록 대상 불분명", "Mediation Agreement": "결합 불성립",
 "Guardianship Predictor": "예측 대상 불분명", "Trademark Pressure": "결합 불성립",
 "Patent Resignation": "결합 불성립", "Fieldtrip Workbook": "워크북 대상 불분명",
 "Polish Mode": "기능 토글로 읽혀 제품 불분명", "Thermocouple Quantity": "수량 대상 불분명",
 "Panic Login": "제품 불분명", "Pool Analysis": "분석 대상 불분명",
 "Surfing Coach": "코칭 대상 불분명", "Tempo Habit": "결합 불성립",
 "Copyright Hub": "허브 지칭으로 제품 불분명", "Migraine Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Insomnia Result": "결과 지칭으로 제품 불분명", "Skydiving Comparison": "비교 대상 불분명",
 "Acne Proposal": "제안 대상 불분명", "Snowboarding Reading": "독서·측정 중의로 불분명",
 "Eczema Reference": "참조 대상 불분명", "Ziplining Duration": "기간 속성 지칭으로 제품명 부자연",
 "Psoriasis Volume": "결합 불성립", "Sledding Authorization": "결합 불성립",
 "Vertigo Template": "결합 불성립", "Diving Agreement": "결합 불성립",
 "Arthritis Reply": "결합 불성립", "Sailing Match": "매칭·경기 중의로 불분명",
 "Menopause Validation": "결합 불성립", "Rafting Model": "모델 지칭으로 제품 불분명",
 "Pregnancy Availability": "상태 명사로 제품명 부자연", "Climbing Barcode": "결합 불성립",
 "Fertility Appointment": "약속 대상 불분명", "Biking Renewal": "결합 불성립",
 "Thyroid Quote": "인용·견적 중의로 불분명", "Golf Certification": "결합 불성립",
 "Cholesterol Nomination": "결합 불성립", "Fishing Payment": "결합 불성립",
 "Hypertension Verification": "결합 불성립", "Camping Seal": "결합 불성립",
 "Anemia Review": "리뷰 대상 불분명", "Glamping Diary": "결합 불성립(개인 일지 형식 부재)",
 "Heartburn Refund": "결합 불성립", "Stargazing Inventory": "결합 불성립",
 "Constipation Claim": "결합 불성립", "Birdwatching Size": "결합 불성립(속성 지칭)",
 "Concussion Length": "결합 불성립(속성 지칭)", "Canyon Distance": "결합 불성립",
 "Sprain Range": "결합 불성립", "Geyser Limit": "결합 불성립",
 "Fracture Type": "결합 불성립(분류 대상 부자연)", "Fjord Clock": "결합 불성립",
 "Insulin Time": "결합 불성립", "Savanna Speed": "결합 불성립",
 "Tundra Depth": "결합 불성립", "Prairie Height": "결합 불성립",
 "Marsh Width": "결합 불성립", "Cove Temperature": "결합 불성립",
 "Cliff Pressure": "결합 불성립", "Cavern Load": "결합 불성립",
 "Oasis Voltage": "결합 불성립", "Dune Wattage": "결합 불성립",
 "Whale Brightness": "결합 불성립", "Dolphin Frequency": "결합 불성립",
 "Penguin Compatibility": "상태 명사로 제품명 부자연", "Flamingo Capacity": "상태 명사로 제품명 부자연",
 "Turtle Usage": "사용 지칭으로 제품 불분명", "Moose Condition": "상태 명사로 제품명 부자연",
 "Bison Humidity": "결합 불성립", "Reindeer Episode": "결합 불성립",
 "Warehouse Spec": "사양 참조로 제품 불분명", "Adjuster Login": "제품 불분명",
 "Bid Coach": "코칭 대상 불분명", "Fulfillment Habit": "결합 불성립",
 "Shuttle Workbook": "워크북 대상 불분명", "Classroom Mode": "기능 토글로 읽혀 제품 불분명",
 "Calibration Spec": "사양 참조로 제품 불분명", "Rotation Quantity": "수량 대상 불분명",
 "Stewardship Analysis": "분석 대상 불분명", "Content Habit": "결합 불성립",
 "Lawyer Total": "합계 지칭으로 제품 불분명", "Attorney Case": "결합 불성립(Case 계열 기각 선례)",
 "Court Onboarding": "결합 불성립", "Judge Matrix": "행렬·매트릭스 중의로 불분명",
 "Linguist Workbook": "워크북 대상 불분명", "Damage Mode": "기능 토글로 읽혀 제품 불분명",
 "Vow Quantity": "수량 대상 불분명", "Winterization Analysis": "분석 대상 불분명",
 "Undercarriage Coach": "코칭 대상 불분명", "Drainpipe Habit": "결합 불성립",
 "Jury Radar": "레이더 기능 지칭으로 제품 불분명", "Lawsuit Rail": "레일 지칭으로 제품 불분명",
 "Divorce Bin": "빈 지칭으로 제품 불분명", "Custody Bill": "청구서·법안 중의로 불분명",
 "Immigration Sum": "합계 지칭으로 제품 불분명", "Testament Subsidy": "결합 불성립",
 "Notary Estimator": "산출 대상 불분명", "Mediation Reply": "결합 불성립",
 "Guardianship Seal": "결합 불성립", "Trademark Load": "결합 불성립",
 "Patent Hazard": "결합 불성립", "Anesthesia Workbook": "워크북 대상 불분명",
 "Fieldtrip Mode": "기능 토글로 읽혀 제품 불분명", "Polish Spec": "사양 참조로 제품 불분명",
 "Thermocouple Login": "제품 불분명", "Panic Analysis": "분석 대상 불분명",
 "Pool Coach": "코칭 대상 불분명", "Surfing Habit": "결합 불성립",
 "Copyright Desk": "데스크 지칭으로 제품 불분명", "Migraine Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Insomnia Streak": "앱 기능 지칭으로 제품 불분명", "Skydiving Proposal": "제안 대상 불분명",
 "Acne Guarantee": "결합 불성립", "Snowboarding Reference": "참조 대상 불분명",
 "Eczema Forecast": "예측 대상 불분명", "Ziplining Volume": "결합 불성립",
 "Psoriasis Diagnostic": "진단 대상 불분명", "Sledding Template": "결합 불성립",
 "Diving Reply": "결합 불성립", "Arthritis Account": "결합 불성립",
 "Sailing Validation": "결합 불성립", "Menopause Lookup": "탐색 대상 불분명",
 "Rafting Availability": "상태 명사로 제품명 부자연", "Pregnancy Eligibility": "결합 불성립",
 "Climbing Appointment": "약속 대상 불분명", "Fertility Feedback": "결합 불성립",
 "Biking Quote": "인용·견적 중의로 불분명", "Thyroid Warranty": "결합 불성립",
 "Golf Nomination": "결합 불성립", "Cholesterol Correction": "결합 불성립",
 "Fishing Verification": "결합 불성립", "Hypertension Simulator": "결합 불성립",
 "Anemia Recipe": "결합 불성립",
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
out = base + r"\_dec_c10.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
