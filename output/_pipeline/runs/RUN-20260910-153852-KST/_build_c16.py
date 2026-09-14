# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk15_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Survey App": (0.55, "설문 설계·응답 분석 앱(실재)"),
 "Survey Tips": (0.55, "Survey App 승인 선례의 Tips 평행"),
 "Video App": (0.55, "동영상 촬영·편집 앱(실재)"),
 "Patent App": (0.55, "특허 검색·출원 관리 앱(실재)"),
 "Safety App": (0.55, "안전 점검·사고 신고 앱(실재)"),
 "Drayage App": (0.55, "컨테이너 드레이지 운송 관리 앱(실재)"),
 "Drayage Tips": (0.55, "Drayage App 승인 선례의 Tips 평행"),
 "Realtor Tips": (0.55, "Realtor App 승인 선례의 Tips 평행"),
 "Wrench Tips": (0.55, "Wrench App 승인 선례의 Tips 평행"),
 "Cover Tips": (0.55, "Cover App 승인 선례의 Tips 평행"),
 "Ductwork Tips": (0.55, "Ductwork App 승인 선례의 Tips 평행"),
 "Golf Video": (0.55, "골프 스윙 레슨 영상(Video 평행)"),
 "Cholesterol Diary": (0.55, "콜레스테롤 기록 일지(Hypertension Diary 평행)"),
 "Golf Diary": (0.55, "골프 스코어·라운드 기록 일지(실재)"),
 "Migraine Record": (0.55, "편두통 발작 기록(Vertigo Record 평행)"),
 "Testament Manual": (0.55, "유언장 작성 절차 안내 매뉴얼(Patent Handbook 평행)"),
}

R_DUP = {
 "Attraction Advice": "직전 승인 Attraction Tips와 동일 기능 의미 중복",
 "Recording Advice": "직전 승인 Recording Tips와 동일 기능 의미 중복",
 "Carrier Advice": "직전 승인 Carrier Tips와 동일 기능 의미 중복",
 "Lockout Advice": "직전 승인 Lockout Tips와 동일 기능 의미 중복",
 "Wrench Advice": "이번 배치 승인 Wrench Tips와 동일 기능 의미 중복",
 "Cover Advice": "이번 배치 승인 Cover Tips와 동일 기능 의미 중복",
 "Realtor Advice": "이번 배치 승인 Realtor Tips와 동일 기능 의미 중복",
}

R = {
 "Buff Analysis": "분석 대상 불분명", "Leak Coach": "코칭 대상 불분명",
 "Tour Habit": "결합 불성립", "Scratch App": "유명 코딩 플랫폼 상표(Scratch) 연상 유사",
 "Attraction Workbook": "워크북 대상 불분명", "Trumpet Workbook": "워크북 대상 불분명",
 "Chargeback Spec": "사양 참조로 제품 불분명", "Discovery Quantity": "수량 대상 불분명",
 "Rider Coach": "코칭 대상 불분명", "Candidate Habit": "결합 불성립",
 "Lawyer Detector": "탐지 대상 불분명", "Attorney Appointment": "약속 대상 불분명",
 "Court Time": "결합 불성립", "Judge Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Dine Mode": "기능 토글로 읽혀 제품 불분명", "Neuter Spec": "사양 참조로 제품 불분명",
 "Whitening Quantity": "수량 대상 불분명", "Diaper Login": "제품 불분명",
 "Wardrobe Analysis": "분석 대상 불분명", "Waxing Coach": "코칭 대상 불분명",
 "Syrup Habit": "결합 불성립", "Jury Scope": "범위 지칭으로 제품 불분명",
 "Lawsuit Assistant": "도우미 기능 지칭으로 제품 불분명", "Divorce Card": "신용카드·카드 중의로 불분명",
 "Custody Badge": "배지 지칭으로 제품 불분명", "Immigration Stake": "지분·말뚝 중의로 불분명",
 "Testament Label": "라벨 지칭으로 제품 불분명", "Notary Rank": "순위 대상 불분명",
 "Mediation Broadcast": "결합 불성립", "Guardianship Onboarding": "결합 불성립",
 "Trademark Episode": "결합 불성립", "Patent Flyer": "전단·비행체 중의로 불분명",
 "Union Workbook": "워크북 대상 불분명", "Insulation Mode": "기능 토글로 읽혀 제품 불분명",
 "Tutoring Spec": "사양 참조로 제품 불분명", "Pothole Quantity": "수량 대상 불분명",
 "Newsletter Login": "제품 불분명", "Benefits Analysis": "분석 대상 불분명",
 "Complaint Coach": "코칭 대상 불분명", "Bumper Habit": "결합 불성립",
 "Copyright Watch": "시계·감시 중의로 불분명", "Migraine Guarantee": "결합 불성립",
 "Insomnia Forecast": "예측 대상 불분명", "Skydiving Diagnostic": "진단 대상 불분명",
 "Acne Progress": "진행 대상 불분명", "Snowboarding Rating": "평가 대상 불분명",
 "Eczema Agreement": "결합 불성립", "Ziplining Case": "결합 불성립(Case 계열 기각 선례)",
 "Psoriasis Match": "매칭·경기 중의로 불분명", "Sledding Ping": "결합 불성립",
 "Vertigo Model": "모델 지칭으로 제품 불분명", "Diving Broadcast": "결합 불성립",
 "Arthritis Barcode": "결합 불성립", "Sailing Invoice": "결합 불성립",
 "Menopause Renewal": "결합 불성립", "Rafting Deposit": "결합 불성립",
 "Pregnancy Certification": "결합 불성립", "Climbing Revision": "결합 불성립",
 "Fertility Payment": "결합 불성립", "Biking Predictor": "예측 대상 불분명",
 "Thyroid Seal": "결합 불성립", "Fishing Newsletter": "결합 불성립",
 "Hypertension Inventory": "결합 불성립", "Camping Checkin": "결합 불성립",
 "Anemia Size": "결합 불성립(속성 지칭)", "Glamping Distance": "결합 불성립",
 "Heartburn Range": "결합 불성립", "Stargazing Clock": "결합 불성립",
 "Constipation Time": "결합 불성립", "Birdwatching Height": "결합 불성립",
 "Concussion Width": "결합 불성립", "Canyon Pressure": "결합 불성립",
 "Sprain Load": "결합 불성립", "Geyser Voltage": "결합 불성립",
 "Fracture Wattage": "결합 불성립", "Fjord Brightness": "결합 불성립",
 "Insulin Frequency": "결합 불성립", "Savanna Compatibility": "상태 명사로 제품명 부자연",
 "Tundra Capacity": "상태 명사로 제품명 부자연", "Prairie Usage": "사용 지칭으로 제품 불분명",
 "Marsh Condition": "상태 명사로 제품명 부자연", "Cove Humidity": "결합 불성립",
 "Cliff Episode": "결합 불성립", "Cavern Cycle": "주기 지칭으로 제품 불분명",
 "Oasis Breakdown": "내역·고장 중의로 불분명", "Dune Sensor": "결합 불성립",
 "Whale Reception": "리셉션·수신 중의로 불분명", "Dolphin Followup": "후속 지칭으로 제품 불분명",
 "Penguin Approval": "승인 지칭으로 제품 불분명", "Flamingo Matrix": "행렬·매트릭스 중의로 불분명",
 "Turtle Evaluation": "평가 대상 불분명", "Moose Questionnaire": "설문 대상 불분명",
 "Bison Utilization": "활용 지칭으로 제품 불분명", "Reindeer Benefit": "혜택 지칭으로 제품 불분명",
 "Turnaround Workbook": "워크북 대상 불분명", "Packing Mode": "기능 토글로 읽혀 제품 불분명",
 "Watermark Spec": "사양 참조로 제품 불분명", "Seating Quantity": "수량 대상 불분명",
 "Skimmer Analysis": "분석 대상 불분명", "Buff Coach": "코칭 대상 불분명",
 "Leak Habit": "결합 불성립", "Scratch Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Trumpet Mode": "기능 토글로 읽혀 제품 불분명", "Chargeback Quantity": "수량 대상 불분명",
 "Discovery Login": "제품 불분명", "Rider Habit": "결합 불성립",
 "Lawyer Timer": "결합 불성립(Timer 계열 기각 선례)", "Attorney Feedback": "결합 불성립",
 "Court Speed": "결합 불성립", "Judge Tutorial": "판사 대상 튜토리얼 결합 부자연",
 "Recording Workbook": "워크북 대상 불분명", "Dine Spec": "사양 참조로 제품 불분명",
 "Neuter Quantity": "수량 대상 불분명", "Whitening Login": "제품 불분명",
 "Diaper Analysis": "분석 대상 불분명", "Wardrobe Coach": "코칭 대상 불분명",
 "Waxing Habit": "결합 불성립", "Jury Loop": "반복 지칭으로 제품 불분명",
 "Lawsuit Planner": "계획 대상 불분명", "Divorce Sheet": "서식·시트 중의로 불분명",
 "Custody Stub": "전표 지칭으로 제품 불분명", "Immigration Margin": "마진 지칭으로 제품 불분명",
 "Notary Trend": "결합 불성립", "Mediation Barcode": "결합 불성립",
 "Guardianship Checkin": "결합 불성립", "Trademark Cycle": "주기 지칭으로 제품 불분명",
 "Carrier Workbook": "워크북 대상 불분명", "Union Mode": "기능 토글로 읽혀 제품 불분명",
 "Insulation Spec": "사양 참조로 제품 불분명", "Tutoring Quantity": "수량 대상 불분명",
 "Pothole Login": "제품 불분명", "Newsletter Analysis": "분석 대상 불분명",
 "Benefits Coach": "코칭 대상 불분명", "Complaint Habit": "결합 불성립",
 "Copyright Scope": "범위 지칭으로 제품 불분명", "Insomnia Deadline": "결합 불성립",
 "Skydiving Progress": "진행 대상 불분명", "Acne Authorization": "결합 불성립",
 "Snowboarding Agreement": "결합 불성립", "Eczema Reply": "결합 불성립",
 "Ziplining Match": "매칭·경기 중의로 불분명", "Psoriasis Validation": "결합 불성립",
 "Sledding Model": "모델 지칭으로 제품 불분명", "Vertigo Availability": "상태 명사로 제품명 부자연",
 "Diving Barcode": "결합 불성립", "Arthritis Appointment": "약속 대상 불분명",
 "Sailing Renewal": "결합 불성립", "Menopause Quote": "인용·견적 중의로 불분명",
 "Rafting Certification": "결합 불성립", "Pregnancy Nomination": "결합 불성립",
 "Climbing Payment": "결합 불성립", "Fertility Verification": "결합 불성립",
 "Biking Seal": "결합 불성립", "Thyroid Review": "리뷰 대상 불분명",
 "Cholesterol Refund": "결합 불성립", "Fishing Inventory": "결합 불성립",
 "Hypertension Claim": "결합 불성립", "Camping Size": "결합 불성립(속성 지칭)",
 "Anemia Length": "결합 불성립(속성 지칭)", "Glamping Range": "결합 불성립",
 "Heartburn Limit": "결합 불성립", "Stargazing Time": "결합 불성립",
 "Constipation Speed": "결합 불성립", "Birdwatching Width": "결합 불성립",
 "Concussion Temperature": "결합 불성립", "Canyon Load": "결합 불성립",
 "Sprain Voltage": "결합 불성립", "Geyser Wattage": "결합 불성립",
 "Fracture Brightness": "결합 불성립", "Fjord Frequency": "결합 불성립",
 "Insulin Compatibility": "상태 명사로 제품명 부자연", "Savanna Capacity": "상태 명사로 제품명 부자연",
 "Tundra Usage": "사용 지칭으로 제품 불분명", "Prairie Condition": "상태 명사로 제품명 부자연",
 "Marsh Humidity": "결합 불성립", "Cove Episode": "결합 불성립",
 "Cliff Cycle": "주기 지칭으로 제품 불분명",
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
out = base + r"\_dec_c16.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
