# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk3_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Bankruptcy App": (0.6, "파산 절차 관리 앱(실재)"),
 "Bankruptcy Tips": (0.55, "Bankruptcy App 승인 선례의 Tips 평행"),
 "Copyright Tips": (0.55, "Copyright App 승인 선례의 Tips 평행"),
 "Migraine Message": (0.55, "복약·기록 리마인드 메시지(Insomnia Message 평행)"),
 "Insomnia Calculator": (0.55, "수면 시간 계산기(실재 관용구)"),
 "Acne Checker": (0.55, "증상 체크 가이드(Eczema Checker 승인 선례 평행)"),
 "Eczema Helper": (0.55, "증상 관리 도우미(Psoriasis/Arthritis Helper 평행)"),
 "Canyon Video": (0.55, "협곡 투어 영상 콘텐츠(Geyser/Fjord Video 평행)"),
 "Sprain Diary": (0.55, "염좌 재활 기록 일지(Fracture Diary 평행)"),
 "Vertigo Record": (0.55, "어지럼 발작 기록(Menopause Record 승인 선례 평행)"),
 "Pregnancy Guide": (0.55, "임신 주차별 가이드 콘텐츠(Fertility Guide 평행)"),
 "Birdwatching Review": (0.55, "관찰 장비·투어 리뷰 콘텐츠(장비 리뷰 실재)"),
 "Tuition App": (0.6, "학비 납부·관리 앱(실재)"),
 "Tuition Tips": (0.55, "Tuition App 승인 선례의 Tips 평행"),
 "Downtime Tips": (0.55, "Downtime App 승인 선례의 Tips 평행"),
 "Activation Tips": (0.55, "Activation App 승인 선례의 Tips 평행"),
 "Percussion App": (0.55, "타악기 레슨·연습 앱(실재)"),
 "Percussion Tips": (0.55, "Percussion App 승인 선례의 Tips 평행"),
 "Bandage App": (0.55, "응급 처치 가이드 앱(실재)"),
 "Amenity App": (0.55, "투숙객 어메니티 예약 앱(실재)"),
 "Circulation App": (0.55, "발행 부수·배포 관리 앱(실재)"),
 "Tourist App": (0.55, "관광 안내 앱(실재)"),
 "Attorney Deadline": (0.55, "법적 마감 기한 관리(Patent Deadline 승인 선례 평행)"),
 "Notary Notification": (0.55, "공증 기한 알림(Notary Reminder 승인 선례 평행)"),
}

R_DUP = {
 "Consolidation Advice": "직전 승인 Consolidation Tips와 동일 기능 의미 중복",
 "Crop Advice": "직전 승인 Crop Tips와 동일 기능 의미 중복",
 "Patch Advice": "직전 승인 Patch Tips와 동일 기능 의미 중복",
 "Downtime Advice": "이번 배치 승인 Downtime Tips와 동일 기능 의미 중복",
 "Activation Advice": "이번 배치 승인 Activation Tips와 동일 기능 의미 중복",
 "Copyright Advice": "이번 배치 승인 Copyright Tips와 동일 기능 의미 중복",
}

R = {
 "Testament Category": "범주 지칭으로 제품 불분명", "Notary Rendering": "렌더링 대상 불분명",
 "Mediation Reading": "독서·측정 중의로 불분명", "Guardianship Invoice": "결합 불성립",
 "Trademark Weight": "결합 불성립", "Patent Breakdown": "내역 대상 불분명",
 "Seniority Spec": "사양 참조로 제품 불분명", "Waterproofing Quantity": "수량 대상 불분명",
 "Mentorship Login": "제품 불분명", "Curfew Analysis": "분석 대상 불분명",
 "Author Coach": "코칭 대상 불분명", "Skydiving Estimator": "산출 대상 불분명",
 "Snowboarding Guardian": "감시자 명사 결합 불성립", "Ziplining Streak": "앱 기능 지칭으로 제품 불분명",
 "Psoriasis Rank": "순위 대상 불분명", "Sledding Proposal": "제안 대상 불분명",
 "Vertigo Guarantee": "결합 불성립", "Diving Reading": "독서·측정 중의로 불분명",
 "Arthritis Reference": "참조 대상 불분명", "Sailing Duration": "기간 속성 지칭으로 제품명 부자연",
 "Menopause Volume": "결합 불성립", "Rafting Authorization": "결합 불성립",
 "Pregnancy Template": "결합 불성립", "Climbing Agreement": "결합 불성립",
 "Fertility Reply": "결합 불성립", "Biking Match": "매칭·경기 중의로 불분명",
 "Thyroid Validation": "결합 불성립", "Golf Model": "모델 지칭으로 제품 불분명",
 "Cholesterol Availability": "상태 명사로 제품명 부자연", "Fishing Barcode": "결합 불성립",
 "Hypertension Appointment": "약속 대상 불분명", "Camping Renewal": "결합 불성립",
 "Anemia Quote": "인용·견적 중의로 불분명", "Glamping Certification": "결합 불성립",
 "Heartburn Nomination": "결합 불성립", "Stargazing Payment": "결합 불성립",
 "Constipation Verification": "결합 불성립", "Birdwatching Seal": "결합 불성립",
 "Concussion Review": "리뷰 대상 불분명", "Sprain Recipe": "결합 불성립",
 "Geyser Refund": "결합 불성립", "Fracture Expense": "결합 불성립",
 "Fjord Newsletter": "결합 불성립", "Insulin Inventory": "결합 불성립",
 "Savanna Claim": "결합 불성립", "Tundra Onboarding": "결합 불성립",
 "Prairie Checkin": "결합 불성립", "Marsh Size": "결합 불성립(속성 지칭)",
 "Cove Length": "결합 불성립(속성 지칭)", "Cliff Weight": "결합 불성립(속성 지칭)",
 "Cavern Distance": "결합 불성립", "Oasis Range": "결합 불성립",
 "Dune Limit": "결합 불성립", "Whale Type": "결합 불성립(분류 대상 부자연)",
 "Dolphin Clock": "결합 불성립", "Penguin Time": "결합 불성립",
 "Flamingo Speed": "결합 불성립", "Turtle Depth": "결합 불성립",
 "Moose Height": "결합 불성립", "Bison Width": "결합 불성립",
 "Reindeer Temperature": "결합 불성립", "Crop Advice SKIP": "",
 "Fundraising Mode": "기능 토글로 읽혀 제품 불분명", "Constituent Spec": "사양 참조로 제품 불분명",
 "Brand Quantity": "수량 대상 불분명", "Manuscript Login": "제품 불분명",
 "Dispatch Analysis": "분석 대상 불분명", "Threat Habit": "결합 불성립",
 "Configuration Workbook": "워크북 대상 불분명", "Chat Mode": "기능 토글로 읽혀 제품 불분명",
 "Logistics Quantity": "수량 대상 불분명", "Allergen Analysis": "분석 대상 불분명",
 "Lawyer Manual": "설명 대상 불분명(Notary Manual 기각 선례)", "Court Simulator": "결합 불성립",
 "Judge Compatibility": "상태 명사로 제품명 부자연", "Jury Workbook": "워크북 대상 불분명",
 "Lane Mode": "기능 토글로 읽혀 제품 불분명", "Walkthrough Spec": "사양 참조로 제품 불분명",
 "Liability Quantity": "수량 대상 불분명", "Garnishment Login": "제품 불분명",
 "Flooring Analysis": "분석 대상 불분명", "Elective Coach": "코칭 대상 불분명",
 "Resident Habit": "결합 불성립", "Lawsuit Deck": "덱 지칭으로 제품 불분명",
 "Divorce Locator": "탐색 대상 불분명", "Custody Level": "수준 지칭으로 제품 불분명",
 "Immigration Confirmation": "확인 지칭으로 제품 불분명", "Testament Attribute": "속성 지칭으로 제품 불분명",
 "Mediation Reference": "참조 대상 불분명", "Guardianship Renewal": "갱신 절차 지칭으로 제품 불분명",
 "Trademark Distance": "거리 결합 부자연", "Patent Sensor": "센서 결합 불성립",
 "Consolidation Workbook": "워크북 대상 불분명",
 "Staging Mode": "기능 토글로 읽혀 제품 불분명", "Beneficiary Spec": "사양 참조로 제품 불분명",
 "Seniority Quantity": "수량 대상 불분명", "Waterproofing Login": "제품 불분명",
 "Mentorship Analysis": "분석 대상 불분명", "Curfew Coach": "코칭 대상 불분명",
 "Author Habit": "결합 불성립", "Migraine Total": "결합 불성립",
 "Insomnia Converter": "변환 대상 불분명", "Skydiving Checker": "체크 대상 불분명",
 "Acne Detector": "탐지 대상 불분명", "Snowboarding Helper": "도우미 대상 불분명",
 "Eczema Stage": "단계 대상 불분명", "Ziplining Rank": "순위 대상 불분명",
 "Psoriasis Trend": "결합 불성립", "Sledding Guarantee": "결합 불성립",
 "Diving Reference": "참조 대상 불분명", "Arthritis Forecast": "예측 대상 불분명",
 "Sailing Volume": "결합 불성립", "Menopause Diagnostic": "진단 대상 불분명",
 "Rafting Template": "결합 불성립", "Climbing Reply": "결합 불성립",
 "Fertility Account": "결합 불성립", "Biking Validation": "결합 불성립",
 "Thyroid Lookup": "탐색 대상 불분명", "Golf Availability": "상태 명사로 제품명 부자연",
 "Cholesterol Eligibility": "결합 불성립", "Fishing Appointment": "약속 대상 불분명",
 "Hypertension Feedback": "결합 불성립", "Camping Quote": "인용·견적 중의로 불분명",
 "Anemia Warranty": "결합 불성립", "Glamping Nomination": "결합 불성립",
 "Heartburn Correction": "결합 불성립", "Stargazing Verification": "결합 불성립",
 "Constipation Simulator": "결합 불성립", "Concussion Recipe": "결합 불성립",
 "Canyon Diary": "결합 불성립(개인 일지 형식 부재)", "Sprain Refund": "결합 불성립",
 "Geyser Expense": "결합 불성립", "Fracture Newsletter": "결합 불성립",
 "Fjord Inventory": "결합 불성립", "Insulin Claim": "결합 불성립",
 "Savanna Onboarding": "결합 불성립", "Tundra Checkin": "결합 불성립",
 "Prairie Size": "결합 불성립(속성 지칭)", "Marsh Length": "결합 불성립(속성 지칭)",
 "Cove Weight": "결합 불성립(속성 지칭)", "Cliff Distance": "결합 불성립",
 "Cavern Range": "결합 불성립", "Oasis Limit": "결합 불성립",
 "Dune Type": "결합 불성립(분류 대상 부자연)", "Whale Clock": "결합 불성립",
 "Dolphin Time": "결합 불성립", "Penguin Speed": "결합 불성립",
 "Flamingo Depth": "결합 불성립", "Turtle Height": "결합 불성립",
 "Moose Width": "결합 불성립", "Bison Temperature": "결합 불성립",
 "Reindeer Pressure": "결합 불성립", "Crop Workbook": "워크북 대상 불분명",
 "Fundraising Spec": "사양 참조로 제품 불분명", "Constituent Quantity": "수량 대상 불분명",
 "Brand Login": "제품 불분명", "Manuscript Analysis": "분석 대상 불분명",
 "Dispatch Coach": "코칭 대상 불분명", "Patch Workbook": "워크북 대상 불분명",
 "Configuration Mode": "기능 토글로 읽혀 제품 불분명", "Chat Spec": "사양 참조로 제품 불분명",
 "Logistics Login": "제품 불분명", "Allergen Coach": "코칭 대상 불분명",
 "Lawyer Worksheet": "학습지 근거 약함", "Attorney Duration": "기간 속성 지칭으로 제품명 부자연",
 "Court Predictor": "예측 대상 불분명", "Judge Capacity": "상태 명사로 제품명 부자연",
 "Jury Mode": "기능 토글로 읽혀 제품 불분명", "Lane Spec": "사양 참조로 제품 불분명",
 "Walkthrough Quantity": "수량 대상 불분명",
 "Staging Workbook": "워크북 대상 불분명", "Beneficiary Mode": "기능 토글로 읽혀 제품 불분명",
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
out = base + r"\_dec_c4.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
