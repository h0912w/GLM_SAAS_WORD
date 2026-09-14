# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk17_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Insurance App": (0.55, "보험 가입·청구 관리 앱(실재)"),
 "Insurance Tips": (0.55, "Insurance App 승인 선례의 Tips 평행"),
 "Rental App": (0.55, "임대 물건·계약 관리 앱(실재)"),
 "Rental Tips": (0.55, "Rental App 승인 선례의 Tips 평행"),
 "Roofing App": (0.55, "지붕 시공·점검 관리 앱(실재)"),
 "Roofing Tips": (0.55, "Roofing App 승인 선례의 Tips 평행"),
 "Chord App": (0.55, "기타 코드 학습·검색 앱(실재)"),
 "Chord Tips": (0.55, "Chord App 승인 선례의 Tips 평행"),
 "Membership App": (0.55, "멤버십 등록·갱신 관리 앱(실재)"),
 "Withholding App": (0.6, "원천징수 세금 계산 관리 앱(실재)"),
 "Hiking App": (0.55, "등산 코스·기록 관리 앱(실재)"),
 "Customs Tips": (0.55, "Customs App 승인 선례의 Tips 평행"),
 "Officiant Tips": (0.55, "Officiant App 승인 선례의 Tips 평행"),
 "Skydiving Guide": (0.55, "스카이다이빙 입문 가이드 콘텐츠(Ziplining Guide 평행)"),
 "Biking Video": (0.55, "자전거 라이딩 가이드 영상(Golf Video 평행)"),
 "Thyroid Diary": (0.55, "갑상선 증상 기록 일지(Hypertension Diary 평행)"),
 "Biking Diary": (0.55, "자전거 라이딩 기록 일지(Camping Diary 평행)"),
}

R_DUP = {
 "Foreclosure Advice": "직전 승인 Foreclosure Tips와 동일 기능 의미 중복",
 "Customs Advice": "직전 승인 Customs Tips와 동일 기능 의미 중복",
 "Officiant Advice": "이번 배치 승인 Officiant Tips와 동일 기능 의미 중복",
}

R = {
 "Sprain Brightness": "결합 불성립", "Geyser Frequency": "결합 불성립",
 "Fracture Compatibility": "상태 명사로 제품명 부자연", "Fjord Capacity": "상태 명사로 제품명 부자연",
 "Insulin Usage": "사용 지칭으로 제품 불분명", "Savanna Condition": "상태 명사로 제품명 부자연",
 "Tundra Humidity": "결합 불성립", "Prairie Episode": "결합 불성립",
 "Marsh Cycle": "주기 지칭으로 제품 불분명", "Cove Breakdown": "내역·고장 중의로 불분명",
 "Cliff Sensor": "결합 불성립", "Cavern Reception": "리셉션·수신 중의로 불분명",
 "Oasis Followup": "후속 지칭으로 제품 불분명", "Dune Approval": "승인 지칭으로 제품 불분명",
 "Whale Matrix": "행렬·매트릭스 중의로 불분명", "Dolphin Evaluation": "평가 대상 불분명",
 "Penguin Questionnaire": "설문 대상 불분명", "Flamingo Utilization": "활용 지칭으로 제품 불분명",
 "Turtle Benefit": "혜택 지칭으로 제품 불분명", "Moose Requirement": "요건 지칭으로 제품 불분명",
 "Bison Depreciation": "결합 불성립", "Reindeer Resignation": "결합 불성립",
 "Safety Workbook": "워크북 대상 불분명", "Ductwork Mode": "기능 토글로 읽혀 제품 불분명",
 "Lockout Spec": "사양 참조로 제품 불분명", "Turnaround Quantity": "수량 대상 불분명",
 "Packing Login": "제품 불분명", "Watermark Analysis": "분석 대상 불분명",
 "Seating Coach": "코칭 대상 불분명", "Scratch Mode": "선례 기각(App 기각) 계열",
 "Wrench Spec": "사양 참조로 제품 불분명", "Attraction Quantity": "수량 대상 불분명",
 "Trumpet Login": "제품 불분명", "Chargeback Coach": "코칭 대상 불분명",
 "Discovery Habit": "결합 불성립", "Lawyer Helper": "도우미 대상 불분명",
 "Attorney Quote": "인용·견적 중의로 불분명", "Court Width": "결합 불성립",
 "Judge Opinion": "판사 대상 결합 부자연", "Minor Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Video Workbook": "워크북 대상 불분명", "Survey Mode": "기능 토글로 읽혀 제품 불분명",
 "Cover Spec": "사양 참조로 제품 불분명", "Recording Quantity": "수량 대상 불분명",
 "Dine Analysis": "분석 대상 불분명", "Neuter Coach": "코칭 대상 불분명",
 "Whitening Habit": "결합 불성립", "Jury Path": "경로 지칭으로 제품 불분명",
 "Lawsuit Companion": "동반자 명사 결합 불성립", "Divorce Note": "메모 대상 불분명",
 "Custody Quota": "할당량 결합 불성립", "Immigration Version": "버전 지칭으로 제품 불분명",
 "Testament Schematic": "도식 지칭으로 제품 불분명", "Notary Guarantee": "결합 불성립",
 "Mediation Invoice": "결합 불성립", "Guardianship Weight": "결합 불성립(속성 지칭)",
 "Trademark Reception": "리셉션·수신 중의로 불분명", "Test Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Patent Workbook": "워크북 대상 불분명", "Drayage Mode": "기능 토글로 읽혀 제품 불분명",
 "Realtor Spec": "사양 참조로 제품 불분명", "Carrier Quantity": "수량 대상 불분명",
 "Union Login": "제품 불분명", "Insulation Analysis": "분석 대상 불분명",
 "Tutoring Coach": "코칭 대상 불분명", "Pothole Habit": "결합 불성립",
 "Copyright Wave": "파도 중의로 불분명", "Migraine Reference": "참조 대상 불분명",
 "Insomnia Diagnostic": "진단 대상 불분명", "Acne Rating": "평가 대상 불분명",
 "Snowboarding Case": "결합 불성립(Case 계열 기각 선례)", "Eczema Match": "매칭·경기 중의로 불분명",
 "Ziplining Ping": "결합 불성립", "Psoriasis Model": "모델 지칭으로 제품 불분명",
 "Sledding Broadcast": "결합 불성립", "Vertigo Barcode": "결합 불성립",
 "Diving Invoice": "결합 불성립", "Arthritis Renewal": "결합 불성립",
 "Sailing Deposit": "결합 불성립", "Menopause Certification": "결합 불성립",
 "Rafting Revision": "결합 불성립", "Pregnancy Payment": "결합 불성립",
 "Climbing Predictor": "예측 대상 불분명", "Fertility Seal": "결합 불성립",
 "Golf Newsletter": "결합 불성립", "Cholesterol Inventory": "결합 불성립",
 "Fishing Checkin": "결합 불성립", "Hypertension Size": "결합 불성립(속성 지칭)",
 "Camping Distance": "결합 불성립", "Anemia Range": "결합 불성립",
 "Glamping Clock": "결합 불성립", "Heartburn Time": "결합 불성립",
 "Stargazing Height": "결합 불성립", "Constipation Width": "결합 불성립",
 "Birdwatching Load": "결합 불성립", "Concussion Voltage": "결합 불성립",
 "Canyon Brightness": "결합 불성립", "Sprain Frequency": "결합 불성립",
 "Geyser Compatibility": "상태 명사로 제품명 부자연", "Fracture Capacity": "상태 명사로 제품명 부자연",
 "Fjord Usage": "사용 지칭으로 제품 불분명", "Insulin Condition": "상태 명사로 제품명 부자연",
 "Savanna Humidity": "결합 불성립", "Tundra Episode": "결합 불성립",
 "Prairie Cycle": "주기 지칭으로 제품 불분명", "Marsh Breakdown": "내역·고장 중의로 불분명",
 "Cove Sensor": "결합 불성립", "Cliff Reception": "리셉션·수신 중의로 불분명",
 "Cavern Followup": "후속 지칭으로 제품 불분명", "Oasis Approval": "승인 지칭으로 제품 불분명",
 "Dune Matrix": "행렬·매트릭스 중의로 불분명", "Whale Evaluation": "평가 대상 불분명",
 "Dolphin Questionnaire": "설문 대상 불분명", "Penguin Utilization": "활용 지칭으로 제품 불분명",
 "Flamingo Benefit": "혜택 지칭으로 제품 불분명", "Turtle Requirement": "요건 지칭으로 제품 불분명",
 "Moose Depreciation": "결합 불성립", "Bison Resignation": "결합 불성립",
 "Reindeer Hazard": "결합 불성립", "Safety Mode": "기능 토글로 읽혀 제품 불분명",
 "Ductwork Spec": "사양 참조로 제품 불분명", "Lockout Quantity": "수량 대상 불분명",
 "Turnaround Login": "제품 불분명", "Packing Analysis": "분석 대상 불분명",
 "Watermark Coach": "코칭 대상 불분명", "Seating Habit": "결합 불성립",
 "Scratch Spec": "선례 기각(App 기각) 계열", "Wrench Quantity": "수량 대상 불분명",
 "Attraction Login": "제품 불분명", "Trumpet Analysis": "분석 대상 불분명",
 "Chargeback Habit": "결합 불성립", "Lawyer Stage": "단계 대상 불분명",
 "Attorney Warranty": "결합 불성립", "Court Temperature": "결합 불성립",
 "Judge Gift": "결합 불성립", "Minor Advice": "선례 기각(App 기각)의 Advice 불가",
 "Video Mode": "기능 토글로 읽혀 제품 불분명", "Survey Spec": "사양 참조로 제품 불분명",
 "Cover Quantity": "수량 대상 불분명", "Recording Login": "제품 불분명",
 "Dine Coach": "코칭 대상 불분명", "Neuter Habit": "결합 불성립",
 "Jury Point": "점수 지칭으로 제품 불분명", "Lawsuit Register": "등록 대상 불분명",
 "Divorce Tag": "태그 지칭으로 제품 불분명", "Custody Tab": "탭 지칭으로 제품 불분명",
 "Immigration Link": "링크 지칭으로 제품 불분명", "Testament Layout": "레이아웃 지칭으로 제품 불분명",
 "Notary Record": "기록 대상 불분명", "Mediation Renewal": "결합 불성립",
 "Guardianship Distance": "결합 불성립", "Trademark Followup": "후속 지칭으로 제품 불분명",
 "Test Advice": "선례 기각(App 기각)의 Advice 불가", "Foreclosure Workbook": "워크북 대상 불분명",
 "Patent Mode": "기능 토글로 읽혀 제품 불분명", "Drayage Spec": "사양 참조로 제품 불분명",
 "Realtor Quantity": "수량 대상 불분명", "Carrier Login": "제품 불분명",
 "Union Analysis": "분석 대상 불분명", "Insulation Coach": "코칭 대상 불분명",
 "Tutoring Habit": "결합 불성립", "Copyright Path": "경로 지칭으로 제품 불분명",
 "Migraine Forecast": "예측 대상 불분명", "Insomnia Progress": "진행 대상 불분명",
 "Skydiving Rating": "평가 대상 불분명", "Acne Agreement": "결합 불성립",
 "Snowboarding Match": "매칭·경기 중의로 불분명", "Eczema Validation": "결합 불성립",
 "Ziplining Model": "모델 지칭으로 제품 불분명", "Psoriasis Availability": "상태 명사로 제품명 부자연",
 "Sledding Barcode": "결합 불성립", "Vertigo Appointment": "약속 대상 불분명",
 "Diving Renewal": "결합 불성립", "Arthritis Quote": "인용·견적 중의로 불분명",
 "Sailing Certification": "결합 불성립", "Menopause Nomination": "결합 불성립",
 "Rafting Payment": "결합 불성립", "Pregnancy Verification": "결합 불성립",
 "Climbing Seal": "결합 불성립", "Fertility Review": "리뷰 대상 불분명",
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
out = base + r"\_dec_c18.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
