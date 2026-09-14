# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk7_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Warehouse App": (0.6, "창고·재고 관리 앱(실재)"),
 "Warehouse Tips": (0.55, "Warehouse App 승인 선례의 Tips 평행"),
 "Calibration App": (0.6, "측정기 교정 이력 관리 앱(실재)"),
 "Calibration Tips": (0.55, "Calibration App 승인 선례의 Tips 평행"),
 "Rotation Tips": (0.55, "Rotation App 승인 선례의 Tips 평행"),
 "Vow Tips": (0.55, "Vow App 승인 선례의 Tips 평행"),
 "Polish App": (0.55, "광택·폴리싱 서비스 앱(실재)"),
 "Polish Tips": (0.55, "Polish App 승인 선례의 Tips 평행"),
 "Classroom App": (0.6, "교실 수업 관리 앱(실재)"),
 "Damage App": (0.55, "파손 접수·정산 관리 앱(실재)"),
 "Fieldtrip App": (0.55, "현장학습 계획·승인 관리 앱(실재)"),
 "Custody Reminder": (0.55, "양육 일정·기한 알림(Notary Reminder 승인 선례 평행)"),
 "Lawyer Notification": (0.55, "사건·기한 알림(Notary Notification 승인 선례 평행)"),
 "Notary Calculator": (0.55, "공증 수수료·기한 계산기(Acne/Insomnia Calculator 평행)"),
 "Attorney Guide": (0.55, "변호사 선정 가이드 콘텐츠(Guide 관용구)"),
 "Arthritis Guide": (0.55, "관절염 관리 가이드 콘텐츠(Fertility/Menopause Guide 평행)"),
 "Stargazing Diary": (0.55, "관측 기록 일지(Birdwatching Diary 평행)"),
 "Migraine Recorder": (0.55, "편두통 발작 기록(Acne/Eczema Recorder 평행)"),
 "Eczema Record": (0.55, "습진 증상 기록(Psoriasis/Vertigo Record 평행)"),
 "Lawsuit Portal": (0.55, "소송 진행 확인 포털(Immigration Portal 승인 선례 평행)"),
 "Jury Tracker": (0.55, "배심 통지·참여 상태 추적(Jury App 선례 평행)"),
 "Glamping Review": (0.55, "글램핑 숙소 리뷰(Fjord/Geyser Review 평행)"),
}

R_DUP = {
 "Thermocouple Advice": "직전 승인 Thermocouple Tips와 동일 기능 의미 중복",
 "Vow Advice": "직전 승인 Vow Tips와 동일 기능 의미 중복",
 "Rotation Advice": "직전 승인 Rotation Tips와 동일 기능 의미 중복",
 "Adjuster Advice": "직전 승인 Adjuster Tips와 동일 기능 의미 중복",
}

R = {
 "Penguin Load": "결합 불성립", "Flamingo Voltage": "결합 불성립",
 "Turtle Wattage": "결합 불성립", "Moose Brightness": "결합 불성립",
 "Bison Frequency": "결합 불성립", "Reindeer Compatibility": "상태 명사로 제품명 부자연",
 "Bid Mode": "기능 토글로 읽혀 제품 불분명", "Fulfillment Spec": "사양 참조로 제품 불분명",
 "Amenity Quantity": "수량 대상 불분명", "Tuition Login": "제품 불분명",
 "Downtime Analysis": "분석 대상 불분명", "Crop Coach": "코칭 대상 불분명",
 "Stewardship Workbook": "워크북 대상 불분명", "Content Spec": "사양 참조로 제품 불분명",
 "Circulation Quantity": "수량 대상 불분명", "Activation Analysis": "분석 대상 불분명",
 "Patch Coach": "코칭 대상 불분명", "Configuration Habit": "결합 불성립",
 "Lawyer Rendering": "렌더링 대상 불분명", "Court Refund": "결합 불성립",
 "Judge Breakdown": "내역·고장 중의로 불분명", "Winterization Workbook": "워크북 대상 불분명",
 "Undercarriage Mode": "기능 토글로 읽혀 제품 불분명", "Drainpipe Spec": "사양 참조로 제품 불분명",
 "Tourist Quantity": "수량 대상 불분명", "Percussion Login": "제품 불분명",
 "Jury Habit": "결합 불성립", "Divorce Post": "게시물·우편 중의로 불분명",
 "Immigration Cost": "비용 지칭으로 제품 불분명", "Testament Balance": "잔액·균형 중의로 불분명",
 "Notary Announcement": "결합 불성립", "Mediation Authorization": "결합 불성립",
 "Guardianship Revision": "결합 불성립", "Trademark Depth": "결합 불성립",
 "Patent Utilization": "활용 지칭으로 제품 불분명", "Panic Workbook": "워크북 대상 불분명",
 "Pool Mode": "기능 토글로 읽혀 제품 불분명", "Surfing Spec": "사양 참조로 제품 불분명",
 "Tempo Quantity": "수량 대상 불분명", "Bandage Login": "제품 불분명",
 "Bankruptcy Analysis": "분석 대상 불분명", "Copyright Coach": "코칭 대상 불분명",
 "Consolidation Habit": "결합 불성립", "Insomnia Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Skydiving Result": "결과 지칭으로 제품 불분명", "Acne Streak": "앱 기능 지칭으로 제품 불분명",
 "Snowboarding Proposal": "제안 대상 불분명", "Eczema Guarantee": "결합 불성립",
 "Ziplining Reading": "독서·측정 중의로 불분명", "Psoriasis Reference": "참조 대상 불분명",
 "Sledding Duration": "기간 속성 지칭으로 제품명 부자연", "Vertigo Volume": "결합 불성립",
 "Diving Authorization": "결합 불성립", "Arthritis Template": "결합 불성립",
 "Sailing Agreement": "결합 불성립", "Menopause Reply": "결합 불성립",
 "Rafting Match": "매칭·경기 중의로 불분명", "Pregnancy Validation": "결합 불성립",
 "Climbing Model": "모델 지칭으로 제품 불분명", "Fertility Availability": "상태 명사로 제품명 부자연",
 "Biking Barcode": "결합 불성립", "Thyroid Appointment": "약속 대상 불분명",
 "Golf Renewal": "결합 불성립", "Cholesterol Quote": "인용·견적 중의로 불분명",
 "Fishing Certification": "결합 불성립", "Hypertension Nomination": "결합 불성립",
 "Camping Payment": "결합 불성립", "Anemia Verification": "결합 불성립",
 "Glamping Seal": "결합 불성립", "Heartburn Review": "리뷰 대상 불분명",
 "Constipation Refund": "결합 불성립", "Birdwatching Inventory": "결합 불성립",
 "Concussion Claim": "결합 불성립", "Canyon Checkin": "결합 불성립",
 "Sprain Size": "결합 불성립(속성 지칭)", "Geyser Length": "결합 불성립(속성 지칭)",
 "Fracture Weight": "결합 불성립(속성 지칭)", "Fjord Distance": "결합 불성립",
 "Insulin Range": "결합 불성립", "Savanna Limit": "결합 불성립",
 "Tundra Type": "결합 불성립(분류 대상 부자연)", "Prairie Clock": "결합 불성립",
 "Marsh Time": "결합 불성립", "Cove Speed": "결합 불성립",
 "Cliff Depth": "결합 불성립", "Cavern Height": "결합 불성립",
 "Oasis Width": "결합 불성립", "Dune Temperature": "결합 불성립",
 "Whale Pressure": "결합 불성립", "Dolphin Load": "결합 불성립",
 "Penguin Voltage": "결합 불성립", "Flamingo Wattage": "결합 불성립",
 "Turtle Brightness": "결합 불성립", "Moose Frequency": "결합 불성립",
 "Bison Compatibility": "상태 명사로 제품명 부자연", "Reindeer Capacity": "상태 명사로 제품명 부자연",
 "Adjuster Workbook": "워크북 대상 불분명", "Bid Spec": "사양 참조로 제품 불분명",
 "Fulfillment Quantity": "수량 대상 불분명", "Amenity Login": "제품 불분명",
 "Tuition Analysis": "분석 대상 불분명", "Downtime Coach": "코칭 대상 불분명",
 "Crop Habit": "결합 불성립", "Stewardship Mode": "기능 토글로 읽혀 제품 불분명",
 "Content Quantity": "수량 대상 불분명", "Circulation Login": "제품 불분명",
 "Activation Coach": "코칭 대상 불분명", "Patch Habit": "결합 불성립",
 "Attorney Rating": "평가 대상 불분명", "Court Expense": "결합 불성립",
 "Judge Sensor": "결합 불성립", "Winterization Mode": "기능 토글로 읽혀 제품 불분명",
 "Undercarriage Spec": "사양 참조로 제품 불분명", "Drainpipe Quantity": "수량 대상 불분명",
 "Tourist Login": "제품 불분명", "Percussion Analysis": "분석 대상 불분명",
 "Lawsuit Console": "콘솔 지칭으로 제품 불분명", "Divorce Harbor": "항구 지칭으로 제품 불분명",
 "Custody Index": "지수·색인 중의로 불분명", "Immigration Price": "가격 지칭으로 제품 불분명",
 "Testament Interest": "이자·관심 중의로 불분명", "Mediation Template": "템플릿 대상 불분명",
 "Guardianship Payment": "결합 불성립", "Trademark Height": "결합 불성립",
 "Patent Benefit": "혜택 지칭으로 제품 불분명", "Thermocouple Workbook": "워크북 대상 불분명",
 "Panic Mode": "기능 토글로 읽혀 제품 불분명", "Pool Spec": "사양 참조로 제품 불분명",
 "Surfing Quantity": "수량 대상 불분명", "Tempo Login": "제품 불분명",
 "Bandage Analysis": "분석 대상 불분명", "Bankruptcy Coach": "코칭 대상 불분명",
 "Copyright Habit": "결합 불성립", "Migraine Estimator": "산출 대상 불분명",
 "Insomnia Guardian": "감시자 명사 결합 불성립", "Skydiving Streak": "앱 기능 지칭으로 제품 불분명",
 "Acne Rank": "순위 대상 불분명", "Snowboarding Guarantee": "결합 불성립",
 "Ziplining Reference": "참조 대상 불분명", "Psoriasis Forecast": "예측 대상 불분명",
 "Sledding Volume": "결합 불성립", "Vertigo Diagnostic": "진단 대상 불분명",
 "Diving Template": "결합 불성립", "Sailing Reply": "결합 불성립",
 "Menopause Account": "결합 불성립", "Rafting Validation": "결합 불성립",
 "Pregnancy Lookup": "탐색 대상 불분명", "Climbing Availability": "상태 명사로 제품명 부자연",
 "Fertility Eligibility": "결합 불성립", "Biking Appointment": "약속 대상 불분명",
 "Thyroid Feedback": "결합 불성립", "Golf Quote": "인용·견적 중의로 불분명",
 "Cholesterol Warranty": "결합 불성립", "Fishing Nomination": "결합 불성립",
 "Hypertension Correction": "결합 불성립", "Camping Verification": "결합 불성립",
 "Anemia Simulator": "결합 불성립", "Heartburn Recipe": "결합 불성립",
 "Stargazing Refund": "결합 불성립", "Constipation Expense": "결합 불성립",
 "Birdwatching Claim": "결합 불성립", "Concussion Onboarding": "결합 불성립",
 "Canyon Size": "결합 불성립(속성 지칭)", "Sprain Length": "결합 불성립(속성 지칭)",
 "Geyser Weight": "결합 불성립(속성 지칭)", "Fracture Distance": "결합 불성립",
 "Fjord Range": "결합 불성립", "Insulin Limit": "결합 불성립",
 "Savanna Type": "결합 불성립(분류 대상 부자연)", "Tundra Clock": "결합 불성립",
 "Prairie Time": "결합 불성립", "Marsh Speed": "결합 불성립",
 "Cove Depth": "결합 불성립", "Cliff Height": "결합 불성립",
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
out = base + r"\_dec_c8.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
