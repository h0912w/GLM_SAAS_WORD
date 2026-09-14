# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk1_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Geyser Review": (0.55, "간헐천 투어 리뷰 콘텐츠(Fjord Review 평행, X Review 관용구)"),
 "Fjord Video": (0.55, "피오르 투어 영상 콘텐츠(Video 관용구)"),
 "Insulin Diary": (0.55, "인슐린 투여 기록 일지(당뇨 기록 앱 실재)"),
 "Fracture Video": (0.55, "골절 재활 영상 가이드(Insulin Video 평행)"),
 "Fundraising App": (0.6, "모금 캠페인 관리 앱(실재)"),
 "Chat App": (0.6, "고객 상담 채팅 앱(실재)"),
 "Lane App": (0.55, "물류 라인 운영 앱(실재)"),
 "Walkthrough Tips": (0.55, "Walkthrough App 승인 선례의 Tips 평행"),
 "Staging App": (0.55, "홈 스테이징 계획 앱(실재)"),
 "Beneficiary Tips": (0.55, "Beneficiary App 승인 선례의 Tips 평행"),
 "Configuration App": (0.55, "설정·구성 관리 앱(실재)"),
 "Chat Tips": (0.55, "Chat App 승인 선례의 Tips 평행"),
 "Lane Tips": (0.55, "Lane App 승인 선례의 Tips 평행"),
 "Staging Tips": (0.55, "Staging App 승인 선례의 Tips 평행"),
 "Consolidation App": (0.55, "화물 통합 집하 앱(Lane App 평행)"),
 "Fundraising Tips": (0.55, "Fundraising App 승인 선례의 Tips 평행"),
 "Fertility Guide": (0.55, "불임 치료 가이드 콘텐츠(Thyroid/Hypertension Guide 평행)"),
 "Migraine Notification": (0.55, "복약·발작 기록 알림(Notification 관용구)"),
 "Jury App": (0.55, "배심 통지·참석 관리 앱(jury duty 앱 실재)"),
 "Immigration Brief": (0.55, "비자·이민 소식 브리핑(Immigration Bulletin 평행)"),
 "Divorce Journal": (0.55, "이혼 과정 기록 저널(가이드 저널 실재)"),
 "Constituent Tips": (0.55, "Constituent App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Brand Advice": "직전 승인 Brand Tips와 동일 기능 의미 중복",
 "Logistics Advice": "직전 승인 Logistics Tips와 동일 기능 의미 중복",
 "Constituent Advice": "직전 승인 Constituent Tips와 동일 기능 의미 중복",
 "Seniority Advice": "직전 승인 Seniority Tips와 동일 기능 의미 중복",
 "Walkthrough Advice": "이번 배치 승인 Walkthrough Tips와 동일 기능 의미 중복",
 "Liability Advice": "직전 승인 Liability Tips와 동일 기능 의미 중복",
 "Beneficiary Advice": "이번 배치 승인 Beneficiary Tips와 동일 기능 의미 중복",
}

R = {
 "Vertigo Rank": "순위 대상 불분명", "Diving Proposal": "제안 대상 불분명",
 "Arthritis Guarantee": "결합 불성립", "Sailing Reading": "독서·측정 중의로 불분명",
 "Menopause Reference": "참조 대상 불분명", "Rafting Duration": "기간 속성 지칭으로 제품명 부자연",
 "Pregnancy Volume": "결합 불성립", "Climbing Authorization": "결합 불성립",
 "Fertility Template": "결합 불성립", "Biking Agreement": "결합 불성립",
 "Thyroid Reply": "결합 불성립", "Golf Match": "매칭·경기 중의로 불분명",
 "Cholesterol Validation": "결합 불성립", "Fishing Model": "모델 지칭으로 제품 불분명",
 "Hypertension Availability": "상태 명사로 제품명 부자연", "Camping Barcode": "결합 불성립",
 "Anemia Appointment": "약속 대상 불분명", "Glamping Renewal": "결합 불성립",
 "Heartburn Quote": "인용·견적 중의로 불분명", "Stargazing Certification": "결합 불성립",
 "Constipation Nomination": "결합 불성립", "Birdwatching Payment": "결합 불성립",
 "Concussion Verification": "결합 불성립", "Canyon Predictor": "예측 대상 불분명",
 "Sprain Seal": "결합 불성립", "Fracture Recipe": "결합 불성립",
 "Insulin Refund": "결합 불성립", "Sprain Review": "리뷰 대상 불분명",
 "Savanna Refund": "결합 불성립", "Tundra Expense": "결합 불성립",
 "Prairie Newsletter": "결합 불성립", "Marsh Inventory": "결합 불성립",
 "Cove Claim": "결합 불성립", "Cliff Onboarding": "결합 불성립",
 "Cavern Checkin": "결합 불성립", "Oasis Size": "결합 불성립(속성 지칭)",
 "Dune Length": "결합 불성립(속성 지칭)", "Whale Weight": "결합 불성립(속성 지칭)",
 "Dolphin Distance": "결합 불성립", "Penguin Range": "결합 불성립",
 "Flamingo Limit": "결합 불성립", "Turtle Type": "결합 불성립(분류 대상 부자연)",
 "Moose Clock": "결합 불성립", "Bison Time": "결합 불성립",
 "Reindeer Speed": "결합 불성립", "Manuscript Workbook": "워크북 대상 불분명",
 "Dispatch Mode": "기능 토글로 읽혀 제품 불분명", "Threat Quantity": "수량 대상 불분명",
 "Provisioning Login": "제품 불분명", "Queue Analysis": "분석 대상 불분명",
 "Sourcing Coach": "코칭 대상 불분명", "Badge Habit": "결합 불성립",
 "Allergen Mode": "기능 토글로 읽혀 제품 불분명", "Nutrition Login": "제품 불분명",
 "Naptime Analysis": "분석 대상 불분명", "Staffing Coach": "코칭 대상 불분명",
 "Termite Habit": "결합 불성립", "Lawyer Extension": "연장 지칭으로 제품 불분명",
 "Attorney Copy": "복사·원고 중의로 불분명", "Court Correction": "결합 불성립",
 "Judge Voltage": "결합 불성립", "Jury Flyer": "결합 불성립(전단지 대상 불분명)",
 "Garnishment Workbook": "워크북 대상 불분명", "Flooring Mode": "기능 토글로 읽혀 제품 불분명",
 "Elective Spec": "사양 참조로 제품 불분명", "Resident Quantity": "수량 대상 불분명",
 "Photo Login": "제품 불분명", "Rating Analysis": "분석 대상 불분명",
 "Interviewer Coach": "코칭 대상 불분명", "Wifi Habit": "결합 불성립",
 "Lawsuit Base": "결합 불성립", "Custody Status": "상태 명사로 제품명 부자연",
 "Testament Rule": "결합 불성립", "Notary Layout": "배치 대상 불분명",
 "Mediation Guarantee": "결합 불성립", "Guardianship Barcode": "결합 불성립",
 "Trademark Checkin": "결합 불성립", "Patent Humidity": "결합 불성립",
 "Copyright Tournament": "결합 불성립", "Waterproofing Workbook": "워크북 대상 불분명",
 "Mentorship Mode": "기능 토글로 읽혀 제품 불분명", "Curfew Spec": "사양 참조로 제품 불분명",
 "Author Quantity": "수량 대상 불분명", "Notice Analysis": "분석 대상 불분명",
 "Exhaust Coach": "코칭 대상 불분명", "Bagel Habit": "결합 불성립",
 "Insomnia Widget": "위젯 기능 지칭으로 제품 불분명", "Skydiving Converter": "변환 대상 불분명",
 "Acne Generator": "생성 대상 불분명", "Snowboarding Detector": "탐지 대상 불분명",
 "Eczema Timer": "결합 불성립(Timer 계열 기각 선례)", "Ziplining Helper": "도우미 대상 불분명(Sailing Helper 기각 선례)",
 "Psoriasis Stage": "단계 대상 불분명", "Sledding Rank": "순위 대상 불분명",
 "Vertigo Trend": "결합 불성립", "Diving Guarantee": "결합 불성립",
 "Arthritis Record": "기록 대상 불분명", "Sailing Reference": "참조 대상 불분명",
 "Menopause Forecast": "예측 대상 불분명", "Rafting Volume": "결합 불성립",
 "Pregnancy Diagnostic": "진단 대상 불분명", "Climbing Template": "결합 불성립",
 "Biking Reply": "결합 불성립", "Thyroid Account": "결합 불성립",
 "Golf Validation": "결합 불성립", "Cholesterol Lookup": "탐색 대상 불분명",
 "Fishing Availability": "상태 명사로 제품명 부자연", "Hypertension Eligibility": "결합 불성립",
 "Camping Appointment": "약속 대상 불분명", "Anemia Feedback": "결합 불성립",
 "Glamping Quote": "인용·견적 중의로 불분명", "Heartburn Warranty": "결합 불성립",
 "Stargazing Nomination": "결합 불성립", "Constipation Correction": "결합 불성립",
 "Birdwatching Verification": "결합 불성립", "Concussion Simulator": "결합 불성립",
 "Canyon Seal": "결합 불성립", "Geyser Recipe": "결합 불성립",
 "Fjord Diary": "결합 불성립(개인 일지 형식 부재)", "Savanna Expense": "결합 불성립",
 "Tundra Newsletter": "결합 불성립", "Prairie Inventory": "결합 불성립",
 "Marsh Claim": "결합 불성립", "Cove Onboarding": "결합 불성립",
 "Cliff Checkin": "결합 불성립", "Cavern Size": "결합 불성립(속성 지칭)",
 "Oasis Length": "결합 불성립(속성 지칭)", "Dune Weight": "결합 불성립(속성 지칭)",
 "Whale Distance": "결합 불성립", "Dolphin Range": "결합 불성립",
 "Penguin Limit": "결합 불성립", "Flamingo Type": "결합 불성립(분류 대상 부자연)",
 "Turtle Clock": "결합 불성립", "Moose Time": "결합 불성립",
 "Bison Speed": "결합 불성립", "Reindeer Depth": "결합 불성립",
 "Brand Workbook": "워크북 대상 불분명", "Manuscript Mode": "기능 토글로 읽혀 제품 불분명",
 "Dispatch Spec": "사양 참조로 제품 불분명", "Threat Login": "제품 불분명",
 "Provisioning Analysis": "분석 대상 불분명", "Queue Coach": "코칭 대상 불분명",
 "Sourcing Habit": "결합 불성립", "Logistics Workbook": "워크북 대상 불분명",
 "Allergen Spec": "사양 참조로 제품 불분명", "Nutrition Analysis": "분석 대상 불분명",
 "Naptime Coach": "코칭 대상 불분명", "Staffing Habit": "결합 불성립",
 "Lawyer Trial": "재판 준비 대상 불분명", "Attorney Reading": "독서·측정 중의로 불분명",
 "Court Revision": "결합 불성립", "Judge Wattage": "결합 불성립",
 "Liability Workbook": "워크북 대상 불분명", "Garnishment Mode": "기능 토글로 읽혀 제품 불분명",
 "Flooring Spec": "사양 참조로 제품 불분명", "Elective Quantity": "수량 대상 불분명",
 "Resident Login": "제품 불분명", "Photo Analysis": "분석 대상 불분명",
 "Rating Coach": "코칭 대상 불분명", "Interviewer Habit": "결합 불성립",
 "Lawsuit Core": "결합 불성립", "Divorce Registry": "등기부 중의로 제품 불분명",
 "Custody View": "뷰 기능 지칭으로 제품 불분명", "Immigration Circular": "순환 이주 중의로 불분명",
 "Testament Detail": "세부 지칭으로 제품 불분명", "Notary Sketch": "제품성 불분명",
 "Mediation Record": "기록 대상 불분명", "Guardianship Appointment": "약속 대상 불분명",
 "Trademark Size": "규모 지칭으로 제품 불분명", "Patent Episode": "결합 불성립",
 "Copyright Flyer": "결합 불성립(전단지 대상 불분명)",
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
out = base + r"\_dec_c2.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
