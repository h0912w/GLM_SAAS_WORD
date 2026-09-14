# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk2_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Migraine Kit": (0.55, "편두통 케어 키트(Insomnia Kit 승인 선례 평행)"),
 "Acne Recorder": (0.55, "여드름 발작 기록(Eczema Recorder 승인 선례 평행)"),
 "Canyon Review": (0.55, "협곡 투어 리뷰 콘텐츠(Geyser/Fjord Review 평행)"),
 "Geyser Video": (0.55, "간헐천 분출 영상 콘텐츠(실검색)"),
 "Sailing Forecast": (0.55, "해상 기상·항해 예보(실재)"),
 "Climbing Guide": (0.55, "클라이밍 루트 가이드(Golf/Biking Guide 평행)"),
 "Fracture Diary": (0.55, "골절 재활 기록 일지(Insulin Diary 평행)"),
 "Sprain Video": (0.55, "염좌 처치·재활 영상 가이드(Fracture Video 평행)"),
 "Crop App": (0.55, "작물 관리 앱(실재)"),
 "Patch App": (0.55, "보안 패치 관리 앱(실재)"),
 "Configuration Tips": (0.55, "Configuration App 승인 선례의 Tips 평행"),
 "Consolidation Tips": (0.55, "Consolidation App 승인 선례의 Tips 평행"),
 "Downtime App": (0.55, "설비 다운타임 추적 앱(실재)"),
 "Activation App": (0.55, "유심·서비스 개통 앱(실재)"),
 "Copyright App": (0.55, "저작물 등록·로열티 관리 앱(실재)"),
 "Immigration Advisory": (0.55, "이민 절차 자문 콘텐츠(Mediation Advisory 승인 선례 평행)"),
 "Immigration Petition": (0.55, "이민 신청서·청원 관리(실재 업무)"),
 "Lawsuit Ledger": (0.55, "소송 비용 장부 관리(Ledger Coach 승인 선례)"),
 "Divorce Calendar": (0.55, "이혼 절차 일정 관리(Custody Calendar 승인 선례 평행)"),
 "Custody History": (0.55, "양육 기록 이력 조회(Custody Log 승인 선례 평행)"),
 "Jury Tips": (0.55, "배심 참여 팁(Jury App 승인 선례의 Tips 평행)"),
 "Crop Tips": (0.55, "Crop App 승인 선례의 Tips 평행"),
 "Patch Tips": (0.55, "Patch App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Fundraising Advice": "직전 승인 Fundraising Tips와 동일 기능 의미 중복",
 "Chat Advice": "직전 승인 Chat Tips와 동일 기능 의미 중복",
 "Lane Advice": "직전 승인 Lane Tips와 동일 기능 의미 중복",
 "Staging Advice": "직전 승인 Staging Tips와 동일 기능 의미 중복",
 "Configuration Advice": "이번 배치 승인 Configuration Tips와 동일 기능 의미 중복",
 "Jury Advice": "이번 배치 승인 Jury Tips와 동일 기능 의미 중복",
}

R = {
 "Seniority Workbook": "워크북 대상 불분명", "Waterproofing Mode": "기능 토글로 읽혀 제품 불분명",
 "Mentorship Spec": "사양 참조로 제품 불분명", "Curfew Quantity": "수량 대상 불분명",
 "Author Login": "제품 불분명", "Notice Coach": "코칭 대상 불분명",
 "Exhaust Habit": "결합 불성립", "Insomnia Repository": "결합 불성립",
 "Skydiving Generator": "생성 대상 불분명", "Snowboarding Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Eczema Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Ziplining Stage": "단계 대상 불분명",
 "Psoriasis Result": "결과 지칭으로 제품 불분명", "Sledding Trend": "결합 불성립",
 "Vertigo Comparison": "비교 대상 불분명", "Diving Record": "기록 대상 불분명",
 "Arthritis Copy": "복사·원고 중의로 불분명", "Menopause Deadline": "결합 불성립",
 "Rafting Diagnostic": "진단 대상 불분명", "Pregnancy Progress": "진행 대상 불분명",
 "Fertility Rating": "평가 대상 불분명", "Biking Account": "결합 불성립",
 "Thyroid Case": "결합 불성립(Case 계열 기각 선례)", "Golf Lookup": "탐색 대상 불분명",
 "Cholesterol Ping": "결합 불성립", "Fishing Eligibility": "결합 불성립",
 "Hypertension Broadcast": "결합 불성립", "Camping Feedback": "결합 불성립",
 "Anemia Invoice": "결합 불성립", "Glamping Warranty": "결합 불성립",
 "Heartburn Deposit": "결합 불성립", "Stargazing Correction": "결합 불성립",
 "Constipation Revision": "결합 불성립", "Birdwatching Simulator": "결합 불성립",
 "Concussion Predictor": "예측 대상 불분명", "Sprain Recipe": "결합 불성립",
 "Fjord Refund": "결합 불성립", "Insulin Expense": "결합 불성립",
 "Savanna Newsletter": "결합 불성립", "Tundra Inventory": "결합 불성립",
 "Prairie Claim": "결합 불성립", "Marsh Onboarding": "결합 불성립",
 "Cove Checkin": "결합 불성립", "Cliff Size": "결합 불성립(속성 지칭)",
 "Cavern Length": "결합 불성립(속성 지칭)", "Oasis Weight": "결합 불성립(속성 지칭)",
 "Dune Distance": "결합 불성립", "Whale Range": "결합 불성립",
 "Dolphin Limit": "결합 불성립", "Penguin Type": "결합 불성립(분류 대상 부자연)",
 "Flamingo Clock": "결합 불성립", "Turtle Time": "결합 불성립",
 "Moose Speed": "결합 불성립", "Bison Depth": "결합 불성립",
 "Reindeer Height": "결합 불성립", "Fundraising Workbook": "워크북 대상 불분명",
 "Constituent Workbook": "워크북 대상 불분명", "Brand Mode": "기능 토글로 읽혀 제품 불분명",
 "Manuscript Spec": "사양 참조로 제품 불분명", "Dispatch Quantity": "수량 대상 불분명",
 "Threat Analysis": "분석 대상 불분명", "Provisioning Coach": "코칭 대상 불분명",
 "Queue Habit": "결합 불성립", "Logistics Mode": "기능 토글로 읽혀 제품 불분명",
 "Allergen Quantity": "수량 대상 불분명", "Nutrition Coach": "코칭 대상 불분명",
 "Naptime Habit": "결합 불성립", "Lawyer Graph": "그래프 대상 불분명",
 "Attorney Reference": "참조 대상 불분명", "Court Payment": "결합 불성립",
 "Judge Brightness": "결합 불성립", "Walkthrough Workbook": "워크북 대상 불분명",
 "Liability Mode": "기능 토글로 읽혀 제품 불분명", "Garnishment Spec": "사양 참조로 제품 불분명",
 "Flooring Quantity": "수량 대상 불분명", "Elective Login": "제품 불분명",
 "Resident Analysis": "분석 대상 불분명", "Photo Coach": "코칭 대상 불분명",
 "Rating Habit": "결합 불성립", "Testament Identifier": "식별자 지칭으로 제품 불분명",
 "Notary Outline": "개요 대상 불분명", "Mediation Copy": "복사·원고 중의로 불분명",
 "Guardianship Feedback": "결합 불성립", "Trademark Length": "길이 결합 부자연",
 "Patent Cycle": "주기 지칭으로 제품 불분명", "Beneficiary Workbook": "워크북 대상 불분명",
 "Seniority Mode": "기능 토글로 읽혀 제품 불분명", "Waterproofing Spec": "사양 참조로 제품 불분명",
 "Mentorship Quantity": "수량 대상 불분명", "Curfew Login": "제품 불분명",
 "Author Analysis": "분석 대상 불분명", "Notice Habit": "결합 불성립",
 "Migraine Count": "카운트 대상 불분명", "Insomnia Announcement": "결합 불성립",
 "Skydiving Recorder": "기록 대상 불분명", "Acne Estimator": "산출 대상 불분명",
 "Snowboarding Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Eczema Guardian": "감시자 명사 결합 불성립",
 "Ziplining Result": "결과 지칭으로 제품 불분명", "Psoriasis Streak": "앱 기능 지칭으로 제품 불분명",
 "Sledding Comparison": "비교 대상 불분명", "Vertigo Proposal": "제안 대상 불분명",
 "Diving Copy": "복사·원고 중의로 불분명", "Arthritis Reading": "독서·측정 중의로 불분명",
 "Sailing Deadline": "결합 불성립", "Menopause Duration": "기간 속성 지칭으로 제품명 부자연",
 "Rafting Progress": "진행 대상 불분명", "Pregnancy Authorization": "결합 불성립",
 "Climbing Rating": "평가 대상 불분명", "Fertility Agreement": "결합 불성립",
 "Biking Case": "결합 불성립(Case 계열 기각 선례)", "Thyroid Match": "매칭 대상 불분명",
 "Golf Ping": "결합 불성립", "Cholesterol Model": "모델 지칭으로 제품 불분명",
 "Fishing Broadcast": "결합 불성립", "Hypertension Barcode": "결합 불성립",
 "Camping Invoice": "결합 불성립", "Anemia Renewal": "결합 불성립",
 "Glamping Deposit": "결합 불성립", "Heartburn Certification": "결합 불성립",
 "Stargazing Revision": "결합 불성립", "Constipation Payment": "결합 불성립",
 "Birdwatching Predictor": "예측 대상 불분명", "Concussion Seal": "결합 불성립",
 "Canyon Recipe": "결합 불성립", "Geyser Diary": "결합 불성립(개인 일지 형식 부재)",
 "Fracture Refund": "결합 불성립", "Fjord Expense": "결합 불성립",
 "Insulin Newsletter": "결합 불성립", "Savanna Inventory": "결합 불성립",
 "Tundra Claim": "결합 불성립", "Prairie Onboarding": "결합 불성립",
 "Marsh Checkin": "결합 불성립", "Cove Size": "결합 불성립(속성 지칭)",
 "Cliff Length": "결합 불성립(속성 지칭)", "Cavern Weight": "결합 불성립(속성 지칭)",
 "Oasis Distance": "결합 불성립", "Dune Range": "결합 불성립",
 "Whale Limit": "결합 불성립", "Dolphin Type": "결합 불성립(분류 대상 부자연)",
 "Penguin Clock": "결합 불성립", "Flamingo Time": "결합 불성립",
 "Turtle Speed": "결합 불성립", "Moose Depth": "결합 불성립",
 "Bison Height": "결합 불성립", "Reindeer Width": "결합 불성립",
 "Fundraising Workbook SKIP": "", "Constituent Mode": "기능 토글로 읽혀 제품 불분명",
 "Brand Spec": "사양 참조로 제품 불분명", "Manuscript Quantity": "수량 대상 불분명",
 "Dispatch Login": "제품 불분명", "Threat Coach": "코칭 대상 불분명",
 "Provisioning Habit": "결합 불성립", "Chat Workbook": "워크북 대상 불분명",
 "Logistics Spec": "사양 참조로 제품 불분명", "Allergen Login": "제품 불분명",
 "Nutrition Habit": "결합 불성립", "Lawyer Label": "레이블 대상 불분명",
 "Attorney Forecast": "예측 대상 불분명", "Court Verification": "검증 대상 불분명",
 "Judge Frequency": "주파수·빈도 중의로 불분명", "Lane Workbook": "워크북 대상 불분명",
 "Walkthrough Mode": "기능 토글로 읽혀 제품 불분명", "Liability Spec": "사양 참조로 제품 불분명",
 "Garnishment Quantity": "수량 대상 불분명", "Flooring Login": "제품 불분명",
 "Elective Analysis": "분석 대상 불분명", "Resident Coach": "코칭 대상 불분명",
 "Photo Habit": "결합 불성립", "Lawsuit Board": "게시판·이사회 중의로 불분명",
 "Divorce Directory": "디렉터리 대상 불분명", "Custody File": "파일 지칭으로 제품 불분명",
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
out = base + r"\_dec_c3.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
