# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk4_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Notary Kit": (0.55, "공증 서류 준비 키트(법률 문서 킷 실재)"),
 "Mediation Deadline": (0.55, "조정 절차 기한 관리(Attorney Deadline 승인 선례 평행)"),
 "Patent Followup": (0.55, "특허 후속 기한 관리(docketing 실재)"),
 "Tempo App": (0.55, "메트로놈·템포 트레이닝 앱(실재)"),
 "Tempo Tips": (0.55, "Tempo App 승인 선례의 Tips 평행"),
 "Bandage Tips": (0.55, "Bandage App 승인 선례의 Tips 평행"),
 "Concussion Video": (0.55, "뇌진탕 처치·회복 영상 가이드(Fracture Video 평행)"),
 "Concussion Diary": (0.55, "뇌진탕 회복 기록 일지(Fracture Diary 평행)"),
 "Diving Forecast": (0.55, "다이빙 해양 컨디션 예보(Sailing Forecast 평행)"),
 "Insomnia Recorder": (0.55, "수면·코골이 기록 앱(실재)"),
 "Rafting Guide": (0.55, "래프팅 강 등급·투어 가이드(Climbing Guide 평행)"),
 "Birdwatching Video": (0.55, "조류 관찰 영상 콘텐츠(관찰 기록 영상 실재)"),
 "Fulfillment App": (0.6, "주문 풀필먼트 관리 앱(실재)"),
 "Fulfillment Tips": (0.55, "Fulfillment App 승인 선례의 Tips 평행"),
 "Amenity Tips": (0.55, "Amenity App 승인 선례의 Tips 평행"),
 "Bid App": (0.6, "입찰 관리 앱(실재)"),
 "Content App": (0.6, "콘텐츠 기획·발행 관리 앱(실재)"),
 "Content Tips": (0.55, "Content App 승인 선례의 Tips 평행"),
 "Circulation Tips": (0.55, "Circulation App 승인 선례의 Tips 평행"),
 "Surfing App": (0.55, "서핑 스팟·파도 정보 앱(실재)"),
 "Tourist Tips": (0.55, "Tourist App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Bankruptcy Advice": "이번 배치 승인 Bankruptcy Tips와 동일 기능 의미 중복",
 "Tuition Advice": "직전 승인 Tuition Tips와 동일 기능 의미 중복",
 "Percussion Advice": "직전 승인 Percussion Tips와 동일 기능 의미 중복",
 "Bandage Advice": "이번 배치 승인 Bandage Tips와 동일 기능 의미 중복",
 "Amenity Advice": "이번 배치 승인 Amenity Tips와 동일 기능 의미 중복",
 "Circulation Advice": "이번 배치 승인 Circulation Tips와 동일 기능 의미 중복",
}

R = {
 "Liability Login": "제품 불분명", "Garnishment Analysis": "분석 대상 불분명",
 "Flooring Coach": "코칭 대상 불분명", "Elective Habit": "결합 불성립",
 "Lawsuit Studio": "스튜디오 지칭으로 제품 불분명", "Divorce Finder": "탐색 대상 불분명",
 "Custody Rate": "비율·요율 중의로 불분명", "Immigration Recap": "요약 대상 불분명",
 "Testament Field": "필드 대상 불분명", "Mediation Forecast": "예측 대상 불분명",
 "Guardianship Quote": "인용·견적 중의로 불분명", "Trademark Range": "결합 불성립",
 "Patent Reception": "리셉션·수신 중의로 불분명", "Copyright Workbook": "워크북 대상 불분명",
 "Consolidation Mode": "기능 토글로 읽혀 제품 불분명", "Staging Spec": "사양 참조로 제품 불분명",
 "Beneficiary Quantity": "수량 대상 불분명", "Seniority Login": "제품 불분명",
 "Waterproofing Analysis": "분석 대상 불분명", "Mentorship Coach": "코칭 대상 불분명",
 "Curfew Habit": "결합 불성립", "Migraine Widget": "위젯 기능 지칭으로 제품 불분명",
 "Insomnia Generator": "생성 대상 불분명", "Skydiving Detector": "탐지 대상 불분명",
 "Acne Timer": "결합 불성립(Timer 계열 기각 선례)", "Snowboarding Stage": "단계 대상 불분명",
 "Eczema Result": "결과 지칭으로 제품 불분명", "Ziplining Trend": "결합 불성립",
 "Psoriasis Comparison": "비교 대상 불분명", "Sledding Record": "기록 대상 불분명",
 "Vertigo Copy": "복사·원고 중의로 불분명", "Arthritis Deadline": "결합 불성립",
 "Sailing Diagnostic": "진단 대상 불분명", "Menopause Progress": "진행 대상 불분명",
 "Pregnancy Rating": "평가 대상 불분명", "Climbing Account": "결합 불성립",
 "Fertility Case": "결합 불성립(Case 계열 기각 선례)", "Biking Lookup": "탐색 대상 불분명",
 "Thyroid Ping": "결합 불성립", "Golf Eligibility": "결합 불성립",
 "Cholesterol Broadcast": "결합 불성립", "Fishing Feedback": "결합 불성립",
 "Hypertension Invoice": "결합 불성립", "Camping Warranty": "결합 불성립",
 "Anemia Deposit": "결합 불성립", "Glamping Correction": "결합 불성립",
 "Heartburn Revision": "결합 불성립", "Stargazing Simulator": "결합 불성립",
 "Constipation Predictor": "예측 대상 불분명", "Birdwatching Recipe": "결합 불성립",
 "Canyon Refund": "결합 불성립", "Sprain Expense": "결합 불성립",
 "Geyser Newsletter": "결합 불성립", "Fracture Inventory": "결합 불성립",
 "Fjord Claim": "결합 불성립", "Insulin Onboarding": "결합 불성립",
 "Savanna Checkin": "결합 불성립", "Tundra Size": "결합 불성립(속성 지칭)",
 "Prairie Length": "결합 불성립(속성 지칭)", "Marsh Weight": "결합 불성립(속성 지칭)",
 "Cove Distance": "결합 불성립", "Cliff Range": "결합 불성립",
 "Cavern Limit": "결합 불성립", "Oasis Type": "결합 불성립(분류 대상 부자연)",
 "Dune Clock": "결합 불성립", "Whale Time": "결합 불성립",
 "Dolphin Speed": "결합 불성립", "Penguin Depth": "결합 불성립",
 "Flamingo Height": "결합 불성립", "Turtle Width": "결합 불성립",
 "Moose Temperature": "결합 불성립", "Bison Pressure": "결합 불성립",
 "Reindeer Load": "결합 불성립", "Tuition Workbook": "워크북 대상 불분명",
 "Downtime Workbook": "워크북 대상 불분명", "Crop Mode": "기능 토글로 읽혀 제품 불분명",
 "Fundraising Quantity": "수량 대상 불분명", "Constituent Login": "제품 불분명",
 "Brand Analysis": "분석 대상 불분명", "Manuscript Coach": "코칭 대상 불분명",
 "Dispatch Habit": "결합 불성립", "Activation Workbook": "워크북 대상 불분명",
 "Patch Mode": "기능 토글로 읽혀 제품 불분명", "Configuration Spec": "사양 참조로 제품 불분명",
 "Chat Quantity": "수량 대상 불분명", "Logistics Analysis": "분석 대상 불분명",
 "Allergen Habit": "결합 불성립", "Lawyer Diagram": "도식 대상 불분명",
 "Attorney Volume": "결합 불성립", "Court Seal": "결합 불성립",
 "Judge Usage": "사용 지칭으로 제품 불분명", "Drainpipe App": "배수관 지칭으로 앱 용도 불분명",
 "Jury Spec": "사양 참조로 제품 불분명", "Lane Quantity": "수량 대상 불분명",
 "Walkthrough Login": "제품 불분명", "Liability Analysis": "분석 대상 불분명",
 "Garnishment Coach": "코칭 대상 불분명", "Flooring Habit": "결합 불성립",
 "Lawsuit Lab": "랩 지칭으로 제품 불분명", "Divorce Office": "사무실 지칭으로 제품 불분명",
 "Custody Update": "업데이트 지칭으로 제품 불분명", "Immigration Entry": "항목·입국 중의로 불분명",
 "Testament Format": "형식 지칭으로 제품 불분명", "Notary Count": "카운트 대상 불분명",
 "Guardianship Warranty": "결합 불성립", "Trademark Limit": "결합 불성립",
 "Bankruptcy Workbook": "워크북 대상 불분명", "Copyright Mode": "기능 토글로 읽혀 제품 불분명",
 "Consolidation Spec": "사양 참조로 제품 불분명", "Staging Quantity": "수량 대상 불분명",
 "Beneficiary Login": "제품 불분명", "Seniority Analysis": "분석 대상 불분명",
 "Waterproofing Coach": "코칭 대상 불분명", "Mentorship Habit": "결합 불성립",
 "Migraine Repository": "결합 불성립", "Skydiving Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Acne Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Snowboarding Result": "결과 지칭으로 제품 불분명",
 "Eczema Streak": "앱 기능 지칭으로 제품 불분명", "Ziplining Comparison": "비교 대상 불분명",
 "Psoriasis Proposal": "제안 대상 불분명", "Sledding Copy": "복사·원고 중의로 불분명",
 "Vertigo Reading": "독서·측정 중의로 불분명", "Diving Deadline": "결합 불성립",
 "Arthritis Duration": "기간 속성 지칭으로 제품명 부자연", "Sailing Progress": "진행 대상 불분명",
 "Menopause Authorization": "결합 불성립", "Rafting Rating": "평가 대상 불분명",
 "Pregnancy Agreement": "결합 불성립", "Climbing Case": "결합 불성립(Case 계열 기각 선례)",
 "Fertility Match": "매칭 대상 불분명", "Biking Ping": "결합 불성립",
 "Thyroid Model": "모델 지칭으로 제품 불분명", "Golf Broadcast": "결합 불성립",
 "Cholesterol Barcode": "결합 불성립", "Fishing Invoice": "결합 불성립",
 "Hypertension Renewal": "결합 불성립", "Camping Deposit": "결합 불성립",
 "Anemia Certification": "결합 불성립", "Glamping Revision": "결합 불성립",
 "Heartburn Payment": "결합 불성립", "Stargazing Predictor": "예측 대상 불분명",
 "Constipation Seal": "결합 불성립", "Canyon Expense": "결합 불성립",
 "Sprain Newsletter": "결합 불성립", "Geyser Inventory": "결합 불성립",
 "Fracture Claim": "결합 불성립", "Fjord Onboarding": "결합 불성립",
 "Insulin Checkin": "결합 불성립", "Savanna Size": "결합 불성립(속성 지칭)",
 "Tundra Length": "결합 불성립(속성 지칭)", "Prairie Weight": "결합 불성립(속성 지칭)",
 "Marsh Distance": "결합 불성립", "Cove Range": "결합 불성립",
 "Cliff Limit": "결합 불성립", "Cavern Type": "결합 불성립(분류 대상 부자연)",
 "Oasis Clock": "결합 불성립", "Dune Time": "결합 불성립",
 "Whale Speed": "결합 불성립", "Dolphin Depth": "결합 불성립",
 "Penguin Height": "결합 불성립", "Flamingo Width": "결합 불성립",
 "Turtle Temperature": "결합 불성립", "Moose Pressure": "결합 불성립",
 "Bison Load": "결합 불성립", "Reindeer Voltage": "결합 불성립",
 "Tuition Workbook SKIP": "", "Downtime Mode": "기능 토글로 읽혀 제품 불분명",
 "Crop Spec": "사양 참조로 제품 불분명", "Fundraising Login": "제품 불분명",
 "Constituent Analysis": "분석 대상 불분명", "Brand Coach": "코칭 대상 불분명",
 "Manuscript Habit": "결합 불성립", "Activation Mode": "기능 토글로 읽혀 제품 불분명",
}
for k in [k for k in R if k.endswith(" SKIP")]:
    del R[k]
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
out = base + r"\_dec_c5.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
