# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk49_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Dispatch App": (0.65, "배차 디스패치 앱(실재 시장)"),
 "Allergen App": (0.6, "식품 알레르기 유발물질 관리 앱(실재)"),
 "Flooring App": (0.6, "바닥재 시공 견적 앱(실재)"),
 "Elective Tips": (0.55, "선택과목 신청 팁(App→Tips 평행)"),
 "Mentorship App": (0.65, "멘토링 매칭 앱(실재 시장)"),
 "Curfew Tips": (0.55, "귀가 관리 팁(App→Tips 평행)"),
 "Insomnia Kit": (0.55, "수면 케어 키트(Eczema Kit 평행, 실재)"),
 "Eczema Recorder": (0.55, "아토피 발작 기록(Psoriasis Recorder 평행)"),
 "Menopause Record": (0.55, "폐경 증상 기록(Vertigo Recorder 평행)"),
 "Thyroid Guide": (0.55, "갑상선 관리 가이드(Hypertension Guide 평행)"),
 "Manuscript App": (0.55, "원고 투고·관리 앱(실재)"),
 "Dispatch Tips": (0.55, "배차 운영 팁(App→Tips 평행)"),
 "Allergen Tips": (0.55, "알레르기 관리 팁(App→Tips 평행)"),
 "Garnishment App": (0.6, "임금 압류 관리 앱(급여 소프트웨어 실재)"),
 "Flooring Tips": (0.55, "바닥재 시공 팁(App→Tips 평행)"),
 "Waterproofing App": (0.55, "방수 시공 앱(업계 실재)"),
 "Mentorship Tips": (0.55, "멘토링 팁(App→Tips 평행)"),
 "Biking Guide": (0.55, "자전거 라이딩 가이드(트레일 가이드 실재)"),
}
R_DUP = {
 "Threat Advice": "동일 배치 승인된 Threat App/Tips와 동일 기능 의미 중복",
 "Resident Advice": "동일 배치 승인된 Resident App/Tips와 동일 기능 의미 중복",
 "Author Advice": "동일 배치 승인된 Author App/Tips와 동일 기능 의미 중복",
 "Pregnancy Forecast": "동일 배치 승인된 Pregnancy Calculator와 기능 중복 우려(Fertility Estimator 기각 선례)",
 "Custody Note": "동일 배치 승인된 Custody Log와 기능 중복 우려",
 "Elective Advice": "동일 배치 승인된 Elective App/Tips와 동일 기능 의미 중복",
 "Curfew Advice": "동일 배치 승인된 Curfew App/Tips와 동일 기능 의미 중복",
}
R = {
 "Cavern Newsletter": "결합 불성립", "Oasis Inventory": "결합 불성립",
 "Dune Claim": "결합 불성립", "Whale Onboarding": "결합 불성립",
 "Dolphin Checkin": "결합 불성립", "Penguin Size": "결합 불성립",
 "Flamingo Length": "결합 불성립", "Turtle Weight": "결합 불성립",
 "Moose Distance": "결합 불성립", "Bison Range": "결합 불성립",
 "Reindeer Limit": "결합 불성립", "Dispatch App SKIP": "",
 "Provisioning Workbook": "워크북 대상 불분명", "Queue Mode": "기능 토글로 읽혀 제품 불분명",
 "Sourcing Spec": "사양 참조로 제품 불분명", "Badge Quantity": "수량 대상 불분명",
 "Trade Login": "제품 불분명", "Treatment Habit": "결합 불성립",
 "Allergen App SKIP": "", "Nutrition Workbook": "워크북 대상 불분명",
 "Naptime Mode": "기능 토글로 읽혀 제품 불분명", "Staffing Spec": "사양 참조로 제품 불분명",
 "Termite Quantity": "수량 대상 불분명", "Mowing Login": "제품 불분명",
 "Turnover Analysis": "분석 대상 불분명", "Intake Coach": "코칭 대상 불분명",
 "Preplanning Habit": "결합 불성립", "Lawyer Advance": "결합 불성립",
 "Attorney Comparison": "비교 대상 불분명", "Court Warranty": "결합 불성립",
 "Judge Width": "결합 불성립", "Jury Opinion": "결합 불성립",
 "Flooring App SKIP": "", "Photo Workbook": "워크북 대상 불분명",
 "Rating Mode": "기능 토글로 읽혀 제품 불분명", "Interviewer Spec": "사양 참조로 제품 불분명",
 "Wifi Quantity": "수량 대상 불분명", "Diagnosis Login": "제품 불분명",
 "Waiter Analysis": "분석 대상 불분명", "Deworming Coach": "코칭 대상 불분명",
 "Flossing Habit": "결합 불성립", "Lawsuit Path": "결합 불성립",
 "Divorce Companion": "결합 불성립(동반자 중의로 대상 불분명)", "Custody Score": "결합 불성립",
 "Immigration Memo": "결합 불성립", "Testament Fine": "결합 불성립(벌금 중의)",
 "Notary Manual": "설명 대상 불분명(Fertility Manual 기각 선례)", "Mediation Rank": "결합 불성립",
 "Guardianship Model": "결합 불성립", "Trademark Newsletter": "결합 불성립",
 "Patent Compatibility": "상태 명사로 제품명 부자연", "Copyright Timetable": "결합 불성립",
 "Mentorship App SKIP": "", "Notice Mode": "기능 토글로 읽혀 제품 불분명",
 "Exhaust Spec": "사양 참조로 제품 불분명", "Bagel Quantity": "수량 대상 불분명",
 "Bloodwork Login": "제품 불분명", "Denture Analysis": "분석 대상 불분명",
 "Potty Coach": "코칭 대상 불분명", "Trim Habit": "결합 불성립",
 "Migraine Layout": "결합 불성립", "Skydiving Widget": "결합 불성립",
 "Acne Repository": "결합 불성립", "Snowboarding Generator": "생성 대상 불분명",
 "Ziplining Detector": "탐지 대상 불분명", "Psoriasis Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Sledding Helper": "도우미 대상 불분명(Sailing Helper 기각 선례)", "Vertigo Stage": "단계 대상 불분명",
 "Diving Rank": "결합 불성립", "Arthritis Trend": "결합 불성립",
 "Sailing Guarantee": "결합 불성립", "Rafting Reference": "결합 불성립",
 "Climbing Volume": "결합 불성립", "Fertility Diagnostic": "진단 대상 불분명",
 "Biking Template": "결합 불성립", "Thyroid Guide SKIP": "",
 "Golf Reply": "결합 불성립", "Cholesterol Account": "결합 불성립",
 "Fishing Validation": "결합 불성립", "Hypertension Lookup": "탐색 대상 불분명",
 "Camping Availability": "상태 명사로 제품명 부자연", "Anemia Eligibility": "결합 불성립",
 "Glamping Appointment": "약속 대상 불분명", "Heartburn Feedback": "결합 불성립",
 "Stargazing Quote": "인용·견적 중의로 대상 불분명", "Constipation Warranty": "결합 불성립",
 "Birdwatching Nomination": "결합 불성립", "Concussion Correction": "결합 불성립",
 "Canyon Payment": "결합 불성립", "Sprain Verification": "결합 불성립",
 "Geyser Simulator": "결합 불성립", "Fracture Predictor": "예측 대상 불분명",
 "Fjord Seal": "결합 불성립", "Insulin Review": "결합 불성립",
 "Savanna Recipe": "결합 불성립", "Tundra Video": "결합 불성립",
 "Prairie Diary": "결합 불성립", "Marsh Refund": "결합 불성립",
 "Cove Expense": "결합 불성립", "Cliff Newsletter": "결합 불성립",
 "Cavern Inventory": "결합 불성립", "Oasis Claim": "결합 불성립",
 "Dune Onboarding": "결합 불성립", "Whale Checkin": "결합 불성립",
 "Dolphin Size": "결합 불성립", "Penguin Length": "결합 불성립",
 "Flamingo Weight": "결합 불성립", "Turtle Distance": "결합 불성립",
 "Moose Range": "결합 불성립", "Bison Limit": "결합 불성립",
 "Reindeer Type": "결합 불성립", "Manuscript App SKIP": "",
 "Threat Workbook": "워크북 대상 불분명", "Provisioning Mode": "기능 토글로 읽혀 제품 불분명",
 "Queue Spec": "사양 참조로 제품 불분명", "Sourcing Quantity": "수량 대상 불분명",
 "Badge Login": "제품 불분명", "Trade Analysis": "분석 대상 불분명",
 "Nutrition Mode": "기능 토글로 읽혀 제품 불분명", "Naptime Spec": "사양 참조로 제품 불분명",
 "Staffing Quantity": "수량 대상 불분명", "Termite Login": "제품 불분명",
 "Mowing Analysis": "분석 대상 불분명", "Turnover Coach": "코칭 대상 불분명",
 "Intake Habit": "결합 불성립", "Lawyer Penalty": "결합 불성립",
 "Attorney Proposal": "제안 대상 불분명", "Court Deposit": "결합 불성립",
 "Judge Temperature": "결합 불성립", "Jury Gift": "결합 불성립",
 "Garnishment App SKIP": "", "Resident Workbook": "워크북 대상 불분명",
 "Photo Mode": "기능 토글로 읽혀 제품 불분명", "Rating Spec": "사양 참조로 제품 불분명",
 "Interviewer Quantity": "수량 대상 불분명", "Wifi Login": "제품 불분명",
 "Diagnosis Analysis": "분석 대상 불분명", "Waiter Coach": "코칭 대상 불분명",
 "Deworming Habit": "결합 불성립", "Lawsuit Point": "결합 불성립",
 "Divorce Register": "결합 불성립(등기부 중의로 제품 불분명)", "Immigration Quota": "결합 불성립",
 "Testament Number": "수치 지칭 부자연", "Notary Worksheet": "학습지 근거 약함",
 "Mediation Trend": "결합 불성립", "Guardianship Availability": "상태 명사로 제품명 부자연",
 "Trademark Inventory": "결합 불성립", "Patent Capacity": "상태 명사로 제품명 부자연",
 "Copyright Opinion": "결합 불성립", "Waterproofing App SKIP": "",
 "Author Workbook": "워크북 대상 불분명", "Notice Spec": "사양 참조로 제품 불분명",
 "Exhaust Quantity": "수량 대상 불분명", "Bagel Login": "제품 불분명",
 "Bloodwork Analysis": "분석 대상 불분명", "Denture Coach": "코칭 대상 불분명",
 "Potty Habit": "결합 불성립", "Migraine Sketch": "제품성 불분명",
 "Insomnia Count": "카운트 대상 불분명", "Skydiving Repository": "결합 불성립",
 "Acne Announcement": "결합 불성립", "Snowboarding Recorder": "기록 대상 불분명",
 "Eczema Estimator": "산출 대상 불분명", "Ziplining Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Psoriasis Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Sledding Stage": "단계 대상 불분명",
 "Vertigo Result": "결합 불성립", "Diving Trend": "결합 불성립",
 "Arthritis Comparison": "비교 대상 불분명", "Sailing Record": "기록 대상 불분명",
 "Menopause Copy": "결합 불성립", "Rafting Forecast": "결합 불성립",
 "Pregnancy Deadline": "결합 불성립", "Climbing Diagnostic": "진단 대상 불분명",
 "Fertility Progress": "진행 대상 불분명", "Thyroid Rating": "평가 대상 불분명",
 "Golf Account": "결합 불성립", "Cholesterol Case": "결합 불성립(Case 계열 기각 선례)",
 "Fishing Lookup": "탐색 대상 불분명", "Hypertension Ping": "결합 불성립",
 "Camping Eligibility": "결합 불성립", "Anemia Broadcast": "결합 불성립",
 "Glamping Feedback": "결합 불성립",
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
out = base + r"\_dec_c49.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
