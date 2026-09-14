# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk8_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Shuttle App": (0.55, "셔틀 배차·예약 앱(실재)"),
 "Shuttle Tips": (0.55, "Shuttle App 승인 선례의 Tips 평행"),
 "Classroom Tips": (0.55, "Classroom App 승인 선례의 Tips 평행"),
 "Damage Tips": (0.55, "Damage App 승인 선례의 Tips 평행"),
 "Linguist App": (0.55, "통번역 인력 매칭 앱(실재)"),
 "Linguist Tips": (0.55, "Linguist App 승인 선례의 Tips 평행"),
 "Provider App": (0.55, "서비스 제공자 포털 앱(실재)"),
 "Restock App": (0.55, "재입고 알림·재고 보충 앱(실재)"),
 "Bolt App": (0.55, "볼트 체결·토크 관리 앱(산업 현장 실재)"),
 "Anesthesia App": (0.55, "마취 기록·투여 계산 앱(실재)"),
 "Anesthesia Tips": (0.55, "Anesthesia App 승인 선례의 Tips 평행"),
 "Fieldtrip Tips": (0.55, "Fieldtrip App 승인 선례의 Tips 평행"),
 "Lawyer Kit": (0.55, "법률 문서 준비 키트(Notary Kit 승인 선례 평행)"),
 "Mediation Guide": (0.55, "조정 절차 가이드 콘텐츠(Attorney Guide 평행)"),
 "Copyright Tracker": (0.55, "저작물 사용·라이선스 추적(Jury Tracker 평행)"),
 "Migraine Checker": (0.55, "편두통 증상 체크(Acne/Eczema Checker 평행)"),
 "Insomnia Helper": (0.55, "수면 관리 도우미(Eczema/Psoriasis Helper 평행)"),
 "Diving Guide": (0.55, "다이빙 스팟 가이드 콘텐츠(Guide 관용구)"),
 "Heartburn Video": (0.55, "속쓰림 완화 생활 영상 가이드(Constipation Video 평행)"),
 "Glamping Video": (0.55, "글램핑 숙소 소개 영상(Geyser/Fjord Video 평행)"),
 "Heartburn Diary": (0.55, "속쓰림·식이 기록 일지(Fracture Diary 평행)"),
 "Divorce Alert": (0.55, "절차 기한 알림(Custody Reminder 승인 선례 평행)"),
}

R_DUP = {
 "Warehouse Advice": "직전 승인 Warehouse Tips와 동일 기능 의미 중복",
 "Calibration Advice": "직전 승인 Calibration Tips와 동일 기능 의미 중복",
 "Polish Advice": "직전 승인 Polish Tips와 동일 기능 의미 중복",
 "Damage Advice": "이번 배치 승인 Damage Tips와 동일 기능 의미 중복",
 "Fieldtrip Advice": "이번 배치 승인 Fieldtrip Tips와 동일 기능 의미 중복",
 "Classroom Advice": "이번 배치 승인 Classroom Tips와 동일 기능 의미 중복",
}

R = {
 "Cavern Width": "결합 불성립", "Oasis Temperature": "결합 불성립",
 "Dune Pressure": "결합 불성립", "Whale Load": "결합 불성립",
 "Dolphin Voltage": "결합 불성립", "Penguin Wattage": "결합 불성립",
 "Flamingo Brightness": "결합 불성립", "Turtle Frequency": "결합 불성립",
 "Moose Compatibility": "상태 명사로 제품명 부자연", "Bison Capacity": "상태 명사로 제품명 부자연",
 "Reindeer Usage": "사용 지칭으로 제품 불분명", "Adjuster Mode": "기능 토글로 읽혀 제품 불분명",
 "Bid Quantity": "수량 대상 불분명", "Fulfillment Login": "제품 불분명",
 "Amenity Analysis": "분석 대상 불분명", "Tuition Coach": "코칭 대상 불분명",
 "Downtime Habit": "결합 불성립", "Rotation Workbook": "워크북 대상 불분명",
 "Stewardship Spec": "사양 참조로 제품 불분명", "Content Login": "제품 불분명",
 "Circulation Analysis": "분석 대상 불분명", "Activation Habit": "결합 불성립",
 "Attorney Agreement": "결합 불성립", "Court Newsletter": "결합 불성립",
 "Judge Reception": "리셉션·수신 중의로 불분명", "Vow Workbook": "워크북 대상 불분명",
 "Winterization Spec": "사양 참조로 제품 불분명", "Undercarriage Quantity": "수량 대상 불분명",
 "Drainpipe Login": "제품 불분명", "Tourist Analysis": "분석 대상 불분명",
 "Percussion Coach": "코칭 대상 불분명", "Jury Flow": "플로우 지칭으로 제품 불분명",
 "Lawsuit Panel": "패널·배심 중의로 불분명", "Divorce Roster": "명단 지칭으로 제품 불분명",
 "Custody Ticket": "티켓·접수 중의로 불분명", "Immigration Fare": "요금 지칭으로 제품 불분명",
 "Testament Asset": "자산 지칭으로 제품 불분명", "Notary Converter": "변환 대상 불분명",
 "Guardianship Verification": "결합 불성립", "Trademark Width": "결합 불성립",
 "Patent Requirement": "요건 지칭으로 제품 불분명", "Thermocouple Mode": "기능 토글로 읽혀 제품 불분명",
 "Panic Spec": "사양 참조로 제품 불분명", "Pool Quantity": "수량 대상 불분명",
 "Surfing Login": "제품 불분명", "Tempo Analysis": "분석 대상 불분명",
 "Bandage Coach": "코칭 대상 불분명", "Bankruptcy Habit": "결합 불성립",
 "Skydiving Rank": "순위 대상 불분명", "Acne Trend": "결합 불성립",
 "Snowboarding Record": "기록 대상 불분명", "Eczema Copy": "복사·원고 중의로 불분명",
 "Ziplining Forecast": "예측 대상 불분명", "Psoriasis Deadline": "결합 불성립",
 "Sledding Diagnostic": "진단 대상 불분명", "Vertigo Progress": "진행 대상 불분명",
 "Arthritis Rating": "평가 대상 불분명", "Sailing Account": "결합 불성립",
 "Menopause Case": "결합 불성립(Case 계열 기각 선례)", "Rafting Lookup": "탐색 대상 불분명",
 "Pregnancy Ping": "결합 불성립", "Climbing Eligibility": "결합 불성립",
 "Fertility Broadcast": "결합 불성립", "Biking Feedback": "결합 불성립",
 "Thyroid Invoice": "결합 불성립", "Golf Warranty": "결합 불성립",
 "Cholesterol Deposit": "결합 불성립", "Fishing Correction": "결합 불성립",
 "Hypertension Revision": "결합 불성립", "Camping Simulator": "결합 불성립",
 "Anemia Predictor": "예측 대상 불분명", "Glamping Recipe": "결합 불성립",
 "Stargazing Expense": "결합 불성립", "Constipation Newsletter": "결합 불성립",
 "Birdwatching Onboarding": "결합 불성립", "Concussion Checkin": "결합 불성립",
 "Canyon Length": "결합 불성립(속성 지칭)", "Sprain Weight": "결합 불성립(속성 지칭)",
 "Geyser Distance": "결합 불성립", "Fracture Range": "결합 불성립",
 "Fjord Limit": "결합 불성립", "Insulin Type": "결합 불성립(분류 대상 부자연)",
 "Savanna Clock": "결합 불성립", "Tundra Time": "결합 불성립",
 "Prairie Speed": "결합 불성립", "Marsh Depth": "결합 불성립",
 "Cove Height": "결합 불성립", "Cliff Width": "결합 불성립",
 "Cavern Temperature": "결합 불성립", "Oasis Pressure": "결합 불성립",
 "Dune Load": "결합 불성립", "Whale Voltage": "결합 불성립",
 "Dolphin Wattage": "결합 불성립", "Penguin Brightness": "결합 불성립",
 "Flamingo Frequency": "결합 불성립", "Turtle Compatibility": "상태 명사로 제품명 부자연",
 "Moose Capacity": "상태 명사로 제품명 부자연", "Bison Usage": "사용 지칭으로 제품 불분명",
 "Reindeer Condition": "상태 명사로 제품명 부자연", "Warehouse Workbook": "워크북 대상 불분명",
 "Adjuster Spec": "사양 참조로 제품 불분명", "Bid Login": "제품 불분명",
 "Fulfillment Analysis": "분석 대상 불분명", "Amenity Coach": "코칭 대상 불분명",
 "Tuition Habit": "결합 불성립", "Calibration Workbook": "워크북 대상 불분명",
 "Rotation Mode": "기능 토글로 읽혀 제품 불분명", "Stewardship Quantity": "수량 대상 불분명",
 "Content Analysis": "분석 대상 불분명", "Circulation Coach": "코칭 대상 불분명",
 "Lawyer Count": "카운트 대상 불분명", "Attorney Reply": "결합 불성립",
 "Court Inventory": "결합 불성립", "Judge Followup": "후속 대상 불분명",
 "Vow Mode": "기능 토글로 읽혀 제품 불분명", "Winterization Quantity": "수량 대상 불분명",
 "Undercarriage Login": "제품 불분명", "Drainpipe Analysis": "분석 대상 불분명",
 "Tourist Coach": "코칭 대상 불분명", "Percussion Habit": "결합 불성립",
 "Jury Hub": "허브 지칭으로 제품 불분명", "Lawsuit Scale": "규모·저울 중의로 불분명",
 "Custody Estimate": "산출 대상 불분명", "Immigration Tax": "결합 불성립",
 "Testament Levy": "결합 불성립", "Notary Generator": "생성 대상 불분명",
 "Mediation Rating": "평가 대상 불분명", "Guardianship Simulator": "결합 불성립",
 "Trademark Temperature": "결합 불성립", "Patent Depreciation": "결합 불성립",
 "Polish Workbook": "워크북 대상 불분명", "Thermocouple Spec": "사양 참조로 제품 불분명",
 "Panic Quantity": "수량 대상 불분명", "Pool Login": "제품 불분명",
 "Surfing Analysis": "분석 대상 불분명", "Tempo Coach": "코칭 대상 불분명",
 "Bandage Habit": "결합 불성립", "Copyright Flow": "플로우 지칭으로 제품 불분명",
 "Migraine Detector": "탐지 대상 불분명", "Insomnia Stage": "단계 대상 불분명",
 "Skydiving Trend": "결합 불성립", "Acne Comparison": "비교 대상 불분명",
 "Snowboarding Copy": "복사·원고 중의로 불분명", "Eczema Reading": "독서·측정 중의로 불분명",
 "Ziplining Deadline": "결합 불성립", "Psoriasis Duration": "기간 속성 지칭으로 제품명 부자연",
 "Sledding Progress": "진행 대상 불분명", "Vertigo Authorization": "결합 불성립",
 "Diving Rating": "평가 대상 불분명", "Arthritis Agreement": "결합 불성립",
 "Sailing Case": "결합 불성립(Case 계열 기각 선례)", "Menopause Match": "매칭 대상 불분명",
 "Rafting Ping": "결합 불성립", "Pregnancy Model": "모델 지칭으로 제품 불분명",
 "Climbing Broadcast": "결합 불성립", "Fertility Barcode": "결합 불성립",
 "Biking Invoice": "결합 불성립", "Thyroid Renewal": "결합 불성립",
 "Golf Deposit": "결합 불성립", "Cholesterol Certification": "결합 불성립",
 "Fishing Revision": "결합 불성립", "Hypertension Payment": "결합 불성립",
 "Camping Predictor": "예측 대상 불분명", "Anemia Seal": "결합 불성립",
 "Stargazing Newsletter": "결합 불성립", "Constipation Inventory": "결합 불성립",
 "Birdwatching Checkin": "결합 불성립", "Concussion Size": "결합 불성립(속성 지칭)",
 "Canyon Weight": "결합 불성립(속성 지칭)", "Sprain Distance": "결합 불성립",
 "Geyser Range": "결합 불성립", "Fracture Limit": "결합 불성립",
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
out = base + r"\_dec_c9.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
