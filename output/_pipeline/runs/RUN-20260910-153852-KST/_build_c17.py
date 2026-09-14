# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk16_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Foreclosure App": (0.55, "경매 물건 검색·관리 앱(실재)"),
 "Foreclosure Tips": (0.55, "Foreclosure App 승인 선례의 Tips 평행"),
 "Customs App": (0.55, "관세 신고·통관 조회 앱(실재)"),
 "Officiant App": (0.55, "주례 일정·예식 관리 앱(실재)"),
 "Judge Timetable": (0.55, "재판 일정 관리(Patent Timetable 평행)"),
 "Safety Tips": (0.55, "Safety App 승인 선례의 Tips 평행"),
 "Video Tips": (0.55, "Video App 승인 선례의 Tips 평행"),
 "Patent Tips": (0.55, "Patent App 승인 선례의 Tips 평행"),
 "Acne Guide": (0.55, "여드름 관리 가이드 콘텐츠(Eczema Guide 평행)"),
 "Thyroid Video": (0.55, "갑상선 관리 영상 가이드(Cholesterol Video 평행)"),
}

R_DUP = {
 "Safety Advice": "이번 배치 승인 Safety Tips와 동일 기능 의미 중복",
 "Survey Advice": "직전 승인 Survey Tips와 동일 기능 의미 중복",
 "Video Advice": "이번 배치 승인 Video Tips와 동일 기능 의미 중복",
 "Patent Advice": "이번 배치 승인 Patent Tips와 동일 기능 의미 중복",
 "Drayage Advice": "직전 승인 Drayage Tips와 동일 기능 의미 중복",
 "Ductwork Advice": "직전 승인 Ductwork Tips와 동일 기능 의미 중복",
}

R = {
 "Cavern Breakdown": "내역·고장 중의로 불분명", "Oasis Sensor": "결합 불성립",
 "Dune Reception": "리셉션·수신 중의로 불분명", "Whale Followup": "후속 지칭으로 제품 불분명",
 "Dolphin Approval": "승인 지칭으로 제품 불분명", "Penguin Matrix": "행렬·매트릭스 중의로 불분명",
 "Flamingo Evaluation": "평가 대상 불분명", "Turtle Questionnaire": "설문 대상 불분명",
 "Moose Utilization": "활용 지칭으로 제품 불분명", "Bison Benefit": "혜택 지칭으로 제품 불분명",
 "Reindeer Requirement": "요건 지칭으로 제품 불분명", "Lockout Workbook": "워크북 대상 불분명",
 "Turnaround Mode": "기능 토글로 읽혀 제품 불분명", "Packing Spec": "사양 참조로 제품 불분명",
 "Watermark Quantity": "수량 대상 불분명", "Seating Login": "제품 불분명",
 "Skimmer Coach": "코칭 대상 불분명", "Buff Habit": "결합 불성립",
 "Scratch Advice": "선례 기각(App 기각)의 Advice 불가", "Wrench Workbook": "워크북 대상 불분명",
 "Attraction Mode": "기능 토글로 읽혀 제품 불분명", "Trumpet Spec": "사양 참조로 제품 불분명",
 "Chargeback Login": "제품 불분명", "Discovery Analysis": "분석 대상 불분명",
 "Lawyer Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Attorney Invoice": "결합 불성립",
 "Court Depth": "결합 불성립", "Judge Handbook": "판사 대상 결합 부자연",
 "Cover Workbook": "워크북 대상 불분명", "Recording Mode": "기능 토글로 읽혀 제품 불분명",
 "Dine Quantity": "수량 대상 불분명", "Neuter Login": "제품 불분명",
 "Whitening Analysis": "분석 대상 불분명", "Diaper Coach": "코칭 대상 불분명",
 "Wardrobe Habit": "결합 불성립", "Jury Grid": "격자 지칭으로 제품 불분명",
 "Lawsuit Scheduler": "스케줄 대상 불분명", "Divorce Check": "검사·수표 중의로 불분명",
 "Custody Statement": "진술서 대상 불분명", "Immigration Fine": "벌금·훌륭한 중의로 불분명",
 "Testament Worksheet": "워크시트 대상 불분명", "Notary Comparison": "비교 대상 불분명",
 "Mediation Appointment": "약속 대상 불분명", "Guardianship Size": "결합 불성립(속성 지칭)",
 "Trademark Breakdown": "내역·고장 중의로 불분명", "Realtor Workbook": "워크북 대상 불분명",
 "Carrier Mode": "기능 토글로 읽혀 제품 불분명", "Union Spec": "사양 참조로 제품 불분명",
 "Insulation Quantity": "수량 대상 불분명", "Tutoring Login": "제품 불분명",
 "Pothole Analysis": "분석 대상 불분명", "Newsletter Coach": "코칭 대상 불분명",
 "Benefits Habit": "결합 불성립", "Copyright Loop": "반복 지칭으로 제품 불분명",
 "Migraine Copy": "복사·원고 중의로 불분명", "Insomnia Duration": "기간 속성 지칭으로 제품명 부자연",
 "Skydiving Authorization": "결합 불성립", "Acne Template": "결합 불성립",
 "Snowboarding Reply": "결합 불성립", "Eczema Account": "결합 불성립",
 "Ziplining Validation": "결합 불성립", "Psoriasis Lookup": "탐색 대상 불분명",
 "Sledding Availability": "상태 명사로 제품명 부자연", "Vertigo Eligibility": "결합 불성립",
 "Diving Appointment": "약속 대상 불분명", "Arthritis Feedback": "결합 불성립",
 "Sailing Quote": "인용·견적 중의로 불분명", "Menopause Warranty": "결합 불성립",
 "Rafting Nomination": "결합 불성립", "Pregnancy Correction": "결합 불성립",
 "Climbing Verification": "결합 불성립", "Fertility Simulator": "결합 불성립",
 "Biking Review": "리뷰 대상 불분명", "Thyroid Recipe": "결합 불성립",
 "Golf Refund": "결합 불성립", "Cholesterol Expense": "결합 불성립",
 "Fishing Claim": "결합 불성립", "Hypertension Onboarding": "결합 불성립",
 "Camping Length": "결합 불성립(속성 지칭)", "Anemia Weight": "결합 불성립(속성 지칭)",
 "Glamping Limit": "결합 불성립", "Heartburn Type": "결합 불성립(분류 대상 부자연)",
 "Stargazing Speed": "결합 불성립", "Constipation Depth": "결합 불성립",
 "Birdwatching Temperature": "결합 불성립", "Concussion Pressure": "결합 불성립",
 "Canyon Voltage": "결합 불성립", "Sprain Wattage": "결합 불성립",
 "Geyser Brightness": "결합 불성립", "Fracture Frequency": "결합 불성립",
 "Fjord Compatibility": "상태 명사로 제품명 부자연", "Insulin Capacity": "상태 명사로 제품명 부자연",
 "Savanna Usage": "사용 지칭으로 제품 불분명", "Tundra Condition": "상태 명사로 제품명 부자연",
 "Prairie Humidity": "결합 불성립", "Marsh Episode": "결합 불성립",
 "Cove Cycle": "주기 지칭으로 제품 불분명", "Cliff Breakdown": "내역·고장 중의로 불분명",
 "Cavern Sensor": "결합 불성립", "Oasis Reception": "리셉션·수신 중의로 불분명",
 "Dune Followup": "후속 지칭으로 제품 불분명", "Whale Approval": "승인 지칭으로 제품 불분명",
 "Dolphin Matrix": "행렬·매트릭스 중의로 불분명", "Penguin Evaluation": "평가 대상 불분명",
 "Flamingo Questionnaire": "설문 대상 불분명", "Turtle Utilization": "활용 지칭으로 제품 불분명",
 "Moose Benefit": "혜택 지칭으로 제품 불분명", "Bison Requirement": "요건 지칭으로 제품 불분명",
 "Reindeer Depreciation": "결합 불성립", "Ductwork Workbook": "워크북 대상 불분명",
 "Lockout Mode": "기능 토글로 읽혀 제품 불분명", "Turnaround Spec": "사양 참조로 제품 불분명",
 "Packing Quantity": "수량 대상 불분명", "Watermark Login": "제품 불분명",
 "Seating Analysis": "분석 대상 불분명", "Skimmer Habit": "결합 불성립",
 "Scratch Workbook": "선례 기각(App 기각) 불가", "Wrench Mode": "기능 토글로 읽혀 제품 불분명",
 "Attraction Spec": "사양 참조로 제품 불분명", "Trumpet Quantity": "수량 대상 불분명",
 "Chargeback Analysis": "분석 대상 불분명", "Discovery Coach": "코칭 대상 불분명",
 "Lawyer Guardian": "감시자 명사 결합 불성립", "Attorney Renewal": "결합 불성립",
 "Court Height": "결합 불성립", "Minor App": "작은·미성년자 중의로 제품 불분명",
 "Survey Workbook": "워크북 대상 불분명", "Cover Mode": "기능 토글로 읽혀 제품 불분명",
 "Recording Spec": "사양 참조로 제품 불분명", "Dine Login": "제품 불분명",
 "Neuter Analysis": "분석 대상 불분명", "Whitening Coach": "코칭 대상 불분명",
 "Diaper Habit": "결합 불성립", "Jury Wave": "파도 중의로 불분명",
 "Lawsuit Monitor": "감시 기능 지칭으로 제품 불분명", "Divorce Score": "점수 대상 불분명",
 "Custody Memo": "메모 대상 불분명", "Immigration Number": "번호 지칭으로 제품 불분명",
 "Testament Diagram": "도식 지칭으로 제품 불분명", "Notary Proposal": "제안 대상 불분명",
 "Mediation Feedback": "결합 불성립", "Guardianship Length": "결합 불성립(속성 지칭)",
 "Trademark Sensor": "결합 불성립", "Test App": "테스트용으로 읽혀 제품 불분명",
 "Drayage Workbook": "워크북 대상 불분명", "Realtor Mode": "기능 토글로 읽혀 제품 불분명",
 "Carrier Spec": "사양 참조로 제품 불분명", "Union Quantity": "수량 대상 불분명",
 "Insulation Login": "제품 불분명", "Tutoring Analysis": "분석 대상 불분명",
 "Pothole Coach": "코칭 대상 불분명", "Newsletter Habit": "결합 불성립",
 "Copyright Grid": "격자 지칭으로 제품 불분명", "Migraine Reading": "독서·측정 중의로 불분명",
 "Insomnia Volume": "결합 불성립", "Skydiving Template": "결합 불성립",
 "Snowboarding Account": "결합 불성립", "Eczema Case": "결합 불성립(Case 계열 기각 선례)",
 "Ziplining Lookup": "탐색 대상 불분명", "Psoriasis Ping": "결합 불성립",
 "Sledding Eligibility": "결합 불성립", "Vertigo Broadcast": "결합 불성립",
 "Diving Feedback": "결합 불성립", "Arthritis Invoice": "결합 불성립",
 "Sailing Warranty": "결합 불성립", "Menopause Deposit": "결합 불성립",
 "Rafting Correction": "결합 불성립", "Pregnancy Revision": "결합 불성립",
 "Climbing Simulator": "결합 불성립", "Fertility Predictor": "예측 대상 불분명",
 "Biking Recipe": "결합 불성립", "Golf Expense": "결합 불성립",
 "Cholesterol Newsletter": "결합 불성립", "Fishing Onboarding": "결합 불성립",
 "Hypertension Checkin": "결합 불성립", "Camping Weight": "결합 불성립(속성 지칭)",
 "Anemia Distance": "결합 불성립", "Glamping Type": "결합 불성립(분류 대상 부자연)",
 "Heartburn Clock": "결합 불성립", "Stargazing Depth": "결합 불성립",
 "Constipation Height": "결합 불성립", "Birdwatching Pressure": "결합 불성립",
 "Concussion Load": "결합 불성립", "Canyon Wattage": "결합 불성립",
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
out = base + r"\_dec_c17.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
