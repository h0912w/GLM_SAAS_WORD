# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk22_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Exam App": (0.55, "시험 준비·일정 관리 앱(실재)"),
 "Exam Tips": (0.55, "Exam App 승인 선례의 Tips 평행"),
 "Hygiene App": (0.55, "위생 점검·관리 앱(실재)"),
 "Hygiene Tips": (0.55, "Hygiene App 승인 선례의 Tips 평행"),
 "Cistern App": (0.55, "저수조 점검·관리 앱(실재)"),
 "Cistern Tips": (0.55, "Cistern App 승인 선례의 Tips 평행"),
 "Bakery App": (0.55, "베이커리 주문·재고 관리 앱(실재)"),
 "Grooming App": (0.55, "반려동물 미용 예약 관리 앱(실재)"),
 "Loyalty App": (0.55, "포인트·로열티 프로그램 관리 앱(실재)"),
 "Wheel App": (0.55, "타이어·휠 정비 관리 앱(실재)"),
 "Migraine Guide": (0.55, "편두통 관리 가이드 콘텐츠(Eczema Guide 평행)"),
 "Rafting Diary": (0.55, "래프팅 기록 일지(Camping Diary 평행)"),
 "Sedation Tips": (0.55, "Sedation App 승인 선례의 Tips 평행"),
 "Souvenir Tips": (0.55, "Souvenir App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Playtime Advice": "직전 승인 Playtime Tips와 동일 기능 의미 중복",
 "Curriculum Advice": "직전 승인 Curriculum Tips와 동일 기능 의미 중복",
 "Sedation Advice": "이번 배치 승인 Sedation Tips와 동일 기능 의미 중복",
 "Trombone Advice": "직전 승인 Trombone Tips와 동일 기능 의미 중복",
 "Souvenir Advice": "이번 배치 승인 Souvenir Tips와 동일 기능 의미 중복",
}

R = {
 "Mediation Payment": "결합 불성립", "Guardianship Height": "결합 불성립",
 "Trademark Depreciation": "결합 불성립", "Conditioner Workbook": "워크북 대상 불분명",
 "Pickup Mode": "기능 토글로 읽혀 제품 불분명", "Ductless Spec": "사양 참조로 제품 불분명",
 "Fob Quantity": "수량 대상 불분명", "Fence Login": "제품 불분명",
 "Hiking Analysis": "분석 대상 불분명", "Chord Coach": "코칭 대상 불분명",
 "Test Habit": "선례 기각(App 기각) 계열", "Patent Flow": "흐름 지칭으로 제품 불분명",
 "Copyright Deck": "갑판·카드 중의로 불분명", "Insomnia Case": "결합 불성립(Case 계열 기각 선례)",
 "Skydiving Ping": "결합 불성립", "Acne Model": "모델 지칭으로 제품 불분명",
 "Snowboarding Barcode": "결합 불성립", "Eczema Appointment": "약속 대상 불분명",
 "Ziplining Renewal": "결합 불성립", "Psoriasis Quote": "인용·견적 중의로 불분명",
 "Sledding Certification": "결합 불성립", "Vertigo Nomination": "결합 불성립",
 "Diving Payment": "결합 불성립", "Arthritis Verification": "결합 불성립",
 "Sailing Seal": "결합 불성립", "Menopause Review": "리뷰 대상 불분명",
 "Pregnancy Refund": "결합 불성립", "Climbing Inventory": "결합 불성립",
 "Fertility Claim": "결합 불성립", "Biking Size": "결합 불성립(속성 지칭)",
 "Thyroid Length": "결합 불성립(속성 지칭)", "Golf Range": "결합 불성립",
 "Cholesterol Limit": "결합 불성립", "Fishing Time": "결합 불성립",
 "Hypertension Speed": "결합 불성립", "Camping Width": "결합 불성립",
 "Anemia Temperature": "결합 불성립", "Glamping Voltage": "결합 불성립",
 "Heartburn Wattage": "결합 불성립", "Stargazing Compatibility": "상태 명사로 제품명 부자연",
 "Constipation Capacity": "상태 명사로 제품명 부자연", "Birdwatching Humidity": "결합 불성립",
 "Concussion Episode": "결합 불성립", "Canyon Breakdown": "내역·고장 중의로 불분명",
 "Sprain Sensor": "결합 불성립", "Geyser Reception": "리셉션·수신 중의로 불분명",
 "Fracture Followup": "후속 지칭으로 제품 불분명", "Fjord Approval": "승인 지칭으로 제품 불분명",
 "Insulin Matrix": "행렬·매트릭스 중의로 불분명", "Savanna Evaluation": "평가 대상 불분명",
 "Tundra Questionnaire": "설문 대상 불분명", "Prairie Utilization": "활용 지칭으로 제품 불분명",
 "Marsh Benefit": "혜택 지칭으로 제품 불분명", "Cove Requirement": "요건 지칭으로 제품 불분명",
 "Cliff Depreciation": "결합 불성립", "Cavern Resignation": "결합 불성립",
 "Oasis Hazard": "결합 불성립", "Dune Guarantor": "보증인 명사 결합 불성립",
 "Whale Tuner": "튜너 기능 지칭으로 제품 불분명", "Dolphin Tutorial": "동물 대상 결합 불성립",
 "Penguin Handbook": "동물 대상 결합 불성립", "Flamingo Timetable": "동물 대상 결합 불성립",
 "Turtle Opinion": "동물 대상 결합 불성립", "Moose Gift": "결합 불성립",
 "Bison Retreat": "동물 대상 결합 불성립", "Reindeer Tournament": "동물 대상 결합 불성립",
 "Incident Workbook": "워크북 대상 불분명", "Season Spec": "선례 기각(App 기각) 계열",
 "Garment Login": "제품 불분명", "Membership Coach": "코칭 대상 불분명",
 "Insurance Habit": "결합 불성립", "Fleet Mode": "기능 토글로 읽혀 제품 불분명",
 "Blast Spec": "선례 기각(App 기각) 계열", "Vent Quantity": "수량 대상 불분명",
 "Rekeying Login": "제품 불분명", "Rental Habit": "결합 불성립",
 "Lawyer Copy": "복사·원고 중의로 불분명", "Attorney Predictor": "예측 대상 불분명",
 "Court Usage": "사용 지칭으로 제품 불분명", "Savings Mode": "기능 토글로 읽혀 제품 불분명",
 "Judge Spec": "선례 기각(App 기각) 계열", "Forwarder Quantity": "수량 대상 불분명",
 "Showing Login": "제품 불분명", "Exclusion Analysis": "선례 기각(App 기각) 계열",
 "Withholding Coach": "선례 기각(App 기각) 계열", "Roofing Habit": "결합 불성립",
 "Jury Lab": "실험실 중의로 불분명", "Lawsuit Office": "사무실 중의로 불분명",
 "Divorce Feed": "피드 지칭으로 제품 불분명", "Custody Fee": "수수료 결합 불성립",
 "Immigration Token": "토큰 지칭으로 제품 불분명", "Testament Widget": "위젯 지칭으로 제품 불분명",
 "Notary Progress": "진행 대상 불분명", "Mediation Verification": "결합 불성립",
 "Guardianship Width": "결합 불성립", "Trademark Resignation": "결합 불성립",
 "Playtime Workbook": "워크북 대상 불분명", "Conditioner Mode": "기능 토글로 읽혀 제품 불분명",
 "Pickup Spec": "사양 참조로 제품 불분명", "Ductless Quantity": "수량 대상 불분명",
 "Fob Login": "제품 불분명", "Fence Analysis": "분석 대상 불분명",
 "Hiking Coach": "코칭 대상 불분명", "Chord Habit": "결합 불성립",
 "Patent Hub": "허브 지칭으로 제품 불분명", "Copyright Studio": "스튜디오 중의로 불분명",
 "Migraine Rating": "평가 대상 불분명", "Insomnia Match": "매칭·경기 중의로 불분명",
 "Skydiving Model": "모델 지칭으로 제품 불분명", "Acne Availability": "상태 명사로 제품명 부자연",
 "Snowboarding Appointment": "약속 대상 불분명", "Eczema Feedback": "결합 불성립",
 "Ziplining Quote": "인용·견적 중의로 불분명", "Psoriasis Warranty": "결합 불성립",
 "Sledding Nomination": "결합 불성립", "Vertigo Correction": "결합 불성립",
 "Diving Verification": "결합 불성립", "Arthritis Simulator": "결합 불성립",
 "Sailing Review": "리뷰 대상 불분명", "Menopause Recipe": "결합 불성립",
 "Rafting Refund": "결합 불성립", "Pregnancy Expense": "결합 불성립",
 "Climbing Claim": "결합 불성립", "Fertility Onboarding": "결합 불성립",
 "Biking Length": "결합 불성립(속성 지칭)", "Thyroid Weight": "결합 불성립(속성 지칭)",
 "Golf Limit": "결합 불성립", "Cholesterol Type": "결합 불성립(분류 대상 부자연)",
 "Fishing Speed": "결합 불성립", "Hypertension Depth": "결합 불성립",
 "Camping Temperature": "결합 불성립", "Anemia Pressure": "결합 불성립",
 "Glamping Wattage": "결합 불성립", "Heartburn Brightness": "결합 불성립",
 "Stargazing Capacity": "상태 명사로 제품명 부자연", "Constipation Usage": "사용 지칭으로 제품 불분명",
 "Birdwatching Episode": "결합 불성립", "Concussion Cycle": "주기 지칭으로 제품 불분명",
 "Canyon Sensor": "결합 불성립", "Sprain Reception": "리셉션·수신 중의로 불분명",
 "Geyser Followup": "후속 지칭으로 제품 불분명", "Fracture Approval": "승인 지칭으로 제품 불분명",
 "Fjord Matrix": "행렬·매트릭스 중의로 불분명", "Insulin Evaluation": "평가 대상 불분명",
 "Savanna Questionnaire": "설문 대상 불분명", "Tundra Utilization": "활용 지칭으로 제품 불분명",
 "Prairie Benefit": "혜택 지칭으로 제품 불분명", "Marsh Requirement": "요건 지칭으로 제품 불분명",
 "Cove Depreciation": "결합 불성립", "Cliff Resignation": "결합 불성립",
 "Cavern Hazard": "결합 불성립", "Oasis Guarantor": "보증인 명사 결합 불성립",
 "Dune Tuner": "튜너 기능 지칭으로 제품 불분명", "Whale Tutorial": "동물 대상 결합 불성립",
 "Dolphin Handbook": "동물 대상 결합 불성립", "Penguin Timetable": "동물 대상 결합 불성립",
 "Flamingo Opinion": "동물 대상 결합 불성립", "Turtle Gift": "결합 불성립",
 "Moose Retreat": "동물 대상 결합 불성립", "Bison Tournament": "동물 대상 결합 불성립",
 "Reindeer Flyer": "동물 대상 결합 불성립", "Curriculum Workbook": "워크북 대상 불분명",
 "Incident Mode": "기능 토글로 읽혀 제품 불분명", "Season Quantity": "선례 기각(App 기각) 계열",
 "Garment Analysis": "분석 대상 불분명", "Membership Habit": "결합 불성립",
 "Fleet Spec": "사양 참조로 제품 불분명", "Blast Quantity": "선례 기각(App 기각) 계열",
 "Vent Login": "제품 불분명", "Rekeying Analysis": "분석 대상 불분명",
 "Lawyer Reading": "독서·측정 중의로 불분명", "Attorney Seal": "결합 불성립",
 "Court Condition": "상태 명사로 제품명 부자연", "Trombone Workbook": "워크북 대상 불분명",
 "Savings Spec": "사양 참조로 제품 불분명", "Judge Quantity": "선례 기각(App 기각) 계열",
 "Forwarder Login": "제품 불분명", "Showing Analysis": "분석 대상 불분명",
 "Exclusion Coach": "선례 기각(App 기각) 계열", "Withholding Habit": "선례 기각(App 기각) 계열",
 "Jury Station": "역·정거장 중의로 불분명",
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
out = base + r"\_dec_c23.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
