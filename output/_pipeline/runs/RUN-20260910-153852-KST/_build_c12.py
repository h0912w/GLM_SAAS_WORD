# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk11_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Skimmer App": (0.55, "수영장 스키머 청소·관리 앱(니치 실재)"),
 "Skimmer Tips": (0.55, "Skimmer App 승인 선례의 Tips 평행"),
 "Camping Video": (0.55, "캠핑장 소개 영상(Glamping Video 평행)"),
 "Anemia Diary": (0.55, "빈혈 증상 기록 일지(Heartburn Diary 평행)"),
 "Diaper App": (0.55, "기저귀 교체 기록·재고 알림 앱(실재)"),
 "Diaper Tips": (0.55, "Diaper App 승인 선례의 Tips 평행"),
 "Newsletter App": (0.6, "뉴스레터 발행·구독 관리 앱(실재)"),
 "Newsletter Tips": (0.55, "Newsletter App 승인 선례의 Tips 평행"),
 "Discovery App": (0.55, "콘텐츠 발견·추천 앱(실재)"),
 "Whitening App": (0.55, "치아 미백 관리 앱(실재)"),
 "Pothole App": (0.55, "포트홀 신고·추적 앱(실재)"),
 "Lawyer Calculator": (0.55, "변호사 수수료 계산기(Notary Calculator 평행)"),
 "Attorney Lookup": (0.55, "변호사 검색 도구(탐색 대상 명확)"),
 "Patent Tutorial": (0.55, "특허 출원 튜토리얼 콘텐츠(실재)"),
 "Patent Handbook": (0.55, "특허 실무 핸드북 콘텐츠(Guide류 관용구)"),
 "Camping Diary": (0.55, "캠핑 기록 일지(Birdwatching Diary 평행)"),
 "Wardrobe Tips": (0.55, "Wardrobe App 승인 선례의 Tips 평행"),
 "Benefits Tips": (0.55, "Benefits App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Leak Advice": "직전 승인 Leak Tips와 동일 기능 의미 중복",
 "Rider Advice": "직전 승인 Rider Tips와 동일 기능 의미 중복",
 "Waxing Advice": "직전 승인 Waxing Tips와 동일 기능 의미 중복",
 "Wardrobe Advice": "이번 배치 승인 Wardrobe Tips와 동일 기능 의미 중복",
 "Benefits Advice": "이번 배치 승인 Benefits Tips와 동일 기능 의미 중복",
 "Complaint Advice": "직전 승인 Complaint Tips와 동일 기능 의미 중복",
}

R = {
 "Climbing Invoice": "결합 불성립", "Fertility Renewal": "결합 불성립",
 "Biking Deposit": "결합 불성립", "Thyroid Certification": "결합 불성립",
 "Golf Revision": "결합 불성립", "Cholesterol Payment": "결합 불성립",
 "Fishing Predictor": "예측 대상 불분명", "Hypertension Seal": "결합 불성립",
 "Glamping Newsletter": "결합 불성립", "Heartburn Inventory": "결합 불성립",
 "Stargazing Checkin": "결합 불성립", "Constipation Size": "결합 불성립(속성 지칭)",
 "Birdwatching Distance": "결합 불성립", "Concussion Range": "결합 불성립",
 "Canyon Type": "결합 불성립(분류 대상 부자연)", "Sprain Clock": "결합 불성립",
 "Geyser Time": "결합 불성립", "Fracture Speed": "결합 불성립",
 "Fjord Depth": "결합 불성립", "Insulin Height": "결합 불성립",
 "Savanna Width": "결합 불성립", "Tundra Temperature": "결합 불성립",
 "Prairie Pressure": "결합 불성립", "Marsh Load": "결합 불성립",
 "Cove Voltage": "결합 불성립", "Cliff Wattage": "결합 불성립",
 "Cavern Brightness": "결합 불성립", "Oasis Frequency": "결합 불성립",
 "Dune Compatibility": "상태 명사로 제품명 부자연", "Whale Capacity": "상태 명사로 제품명 부자연",
 "Dolphin Usage": "사용 지칭으로 제품 불분명", "Penguin Condition": "상태 명사로 제품명 부자연",
 "Flamingo Humidity": "결합 불성립", "Turtle Episode": "결합 불성립",
 "Moose Cycle": "주기 지칭으로 제품 불분명", "Bison Breakdown": "내역·고장 중의로 불분명",
 "Reindeer Sensor": "결합 불성립", "Buff Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Buff Advice": "선례 기각(App 기각)의 Advice 불가", "Tour Workbook": "워크북 대상 불분명",
 "Drum Mode": "기능 토글로 읽혀 제품 불분명", "Provider Spec": "사양 참조로 제품 불분명",
 "Warehouse Analysis": "분석 대상 불분명", "Adjuster Habit": "결합 불성립",
 "Candidate Workbook": "워크북 대상 불분명", "Warranty Mode": "기능 토글로 읽혀 제품 불분명",
 "Restock Spec": "사양 참조로 제품 불분명", "Shuttle Quantity": "수량 대상 불분명",
 "Classroom Login": "제품 불분명", "Calibration Analysis": "분석 대상 불분명",
 "Rotation Coach": "코칭 대상 불분명", "Lawyer Announcement": "공지 대상 불분명",
 "Court Length": "결합 불성립", "Judge Utilization": "활용 지칭으로 제품 불분명",
 "Jury Compass": "컴퍼스 기능 지칭으로 제품 불분명", "Lawsuit Ring": "링 지칭으로 제품 불분명",
 "Divorce Ticker": "티커 기능 지칭으로 제품 불분명", "Custody List": "목록 지칭으로 제품 불분명",
 "Immigration Cash": "결합 불성립", "Testament Advance": "결합 불성립",
 "Notary Timer": "결합 불성립(Timer 계열 기각 선례)", "Mediation Match": "매칭 대상 불분명",
 "Syrup Workbook": "워크북 대상 불분명", "Zoning Mode": "기능 토글로 읽혀 제품 불분명",
 "Guardianship Video": "영상 대상 불분명", "Trademark Brightness": "결합 불성립",
 "Copyright Vault": "금고 지칭으로 제품 불분명", "Migraine Stage": "단계 대상 불분명",
 "Insomnia Comparison": "비교 대상 불분명", "Skydiving Copy": "복사·원고 중의로 불분명",
 "Acne Reading": "독서·측정 중의로 불분명", "Snowboarding Duration": "기간 속성 지칭으로 제품명 부자연",
 "Eczema Volume": "결합 불성립", "Ziplining Authorization": "결합 불성립",
 "Psoriasis Template": "결합 불성립", "Sledding Agreement": "결합 불성립",
 "Vertigo Reply": "결합 불성립", "Diving Match": "매칭·경기 중의로 불분명",
 "Arthritis Validation": "결합 불성립", "Sailing Model": "모델 지칭으로 제품 불분명",
 "Menopause Availability": "상태 명사로 제품명 부자연", "Rafting Barcode": "결합 불성립",
 "Pregnancy Appointment": "약속 대상 불분명", "Climbing Renewal": "결합 불성립",
 "Fertility Quote": "인용·견적 중의로 불분명", "Biking Certification": "결합 불성립",
 "Thyroid Nomination": "결합 불성립", "Golf Payment": "결합 불성립",
 "Cholesterol Verification": "결합 불성립", "Fishing Seal": "결합 불성립",
 "Hypertension Review": "리뷰 대상 불분명", "Anemia Refund": "결합 불성립",
 "Glamping Inventory": "결합 불성립", "Heartburn Claim": "결합 불성립",
 "Stargazing Size": "결합 불성립(속성 지칭)", "Constipation Length": "결합 불성립(속성 지칭)",
 "Birdwatching Range": "결합 불성립", "Concussion Limit": "결합 불성립",
 "Canyon Clock": "결합 불성립", "Sprain Time": "결합 불성립",
 "Geyser Speed": "결합 불성립", "Fracture Depth": "결합 불성립",
 "Fjord Height": "결합 불성립", "Insulin Width": "결합 불성립",
 "Savanna Temperature": "결합 불성립", "Tundra Pressure": "결합 불성립",
 "Prairie Load": "결합 불성립", "Marsh Voltage": "결합 불성립",
 "Cove Wattage": "결합 불성립", "Cliff Brightness": "결합 불성립",
 "Cavern Frequency": "결합 불성립", "Oasis Compatibility": "상태 명사로 제품명 부자연",
 "Dune Capacity": "상태 명사로 제품명 부자연", "Whale Usage": "사용 지칭으로 제품 불분명",
 "Dolphin Condition": "상태 명사로 제품명 부자연", "Penguin Humidity": "결합 불성립",
 "Flamingo Episode": "결합 불성립", "Turtle Cycle": "주기 지칭으로 제품 불분명",
 "Moose Breakdown": "내역·고장 중의로 불분명", "Bison Sensor": "결합 불성립",
 "Reindeer Reception": "리셉션·수신 중의로 불분명", "Leak Workbook": "워크북 대상 불분명",
 "Tour Mode": "기능 토글로 읽혀 제품 불분명", "Drum Spec": "사양 참조로 제품 불분명",
 "Provider Quantity": "수량 대상 불분명", "Warehouse Coach": "코칭 대상 불분명",
 "Rider Workbook": "워크북 대상 불분명", "Candidate Mode": "기능 토글로 읽혀 제품 불분명",
 "Warranty Spec": "사양 참조로 제품 불분명", "Restock Quantity": "수량 대상 불분명",
 "Shuttle Login": "제품 불분명", "Classroom Analysis": "분석 대상 불분명",
 "Calibration Coach": "코칭 대상 불분명", "Rotation Habit": "결합 불성립",
 "Attorney Ping": "결합 불성립", "Court Weight": "결합 불성립",
 "Judge Benefit": "혜택 지칭으로 제품 불분명", "Waxing Workbook": "워크북 대상 불분명",
 "Syrup Mode": "기능 토글로 읽혀 제품 불분명", "Zoning Spec": "사양 참조로 제품 불분명",
 "Bolt Quantity": "수량 대상 불분명", "Linguist Login": "제품 불분명",
 "Damage Analysis": "분석 대상 불분명", "Vow Habit": "결합 불성립",
 "Jury Beacon": "비컨 기능 지칭으로 제품 불분명", "Lawsuit Gate": "게이트 지칭으로 제품 불분명",
 "Divorce Line": "라인 지칭으로 제품 불분명", "Custody Table": "테이블 지칭으로 제품 불분명",
 "Immigration Sale": "결합 불성립", "Testament Penalty": "결합 불성립",
 "Notary Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Mediation Validation": "결합 불성립",
 "Guardianship Diary": "일지 대상 불분명", "Trademark Frequency": "결합 불성립",
 "Complaint Workbook": "워크북 대상 불분명", "Bumper Mode": "기능 토글로 읽혀 제품 불분명",
 "Pastry Spec": "사양 참조로 제품 불분명", "Anesthesia Login": "제품 불분명",
 "Fieldtrip Analysis": "분석 대상 불분명", "Polish Coach": "코칭 대상 불분명",
 "Copyright Compass": "컴퍼스 기능 지칭으로 제품 불분명", "Migraine Result": "결과 지칭으로 제품 불분명",
 "Insomnia Proposal": "제안 대상 불분명", "Skydiving Reading": "독서·측정 중의로 불분명",
 "Acne Reference": "참조 대상 불분명", "Snowboarding Volume": "결합 불성립",
 "Bolt Spec": "사양 참조로 제품 불분명", "Linguist Quantity": "수량 대상 불분명",
 "Damage Login": "제품 불분명", "Vow Coach": "코칭 대상 불분명",
 "Bumper Workbook": "워크북 대상 불분명", "Pastry Mode": "기능 토글로 읽혀 제품 불분명",
 "Anesthesia Quantity": "수량 대상 불분명", "Fieldtrip Login": "제품 불분명",
 "Polish Analysis": "분석 대상 불분명", "Thermocouple Habit": "결합 불성립",
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
out = base + r"\_dec_c12.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
