# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk23_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Windshield App": (0.55, "앞유리 수리·교체 관리 앱(실재)"),
 "Windshield Tips": (0.55, "Windshield App 승인 선례의 Tips 평행"),
 "Reservation App": (0.55, "예약 접수·관리 앱(실재)"),
 "Reservation Tips": (0.55, "Reservation App 승인 선례의 Tips 평행"),
 "Coping App": (0.55, "스트레스 대처 기술 연습 앱(실재)"),
 "Coping Tips": (0.55, "Coping App 승인 선례의 Tips 평행"),
 "Menopause Video": (0.55, "폐경 관리 영상 가이드(Hypertension Video 평행)"),
 "Menopause Diary": (0.55, "폐경 증상 기록 일지(Hypertension Diary 평행)"),
 "Sailing Video": (0.55, "요트 조종 강습 영상(Golf Video 평행)"),
 "Testament Announcement": (0.55, "유언 관련 공지 관리(Notification 절차 명사 선례 평행)"),
 "Notary Template": (0.55, "공증 문서 템플릿 관리(Testament Kit 평행)"),
 "Bakery Tips": (0.55, "Bakery App 승인 선례의 Tips 평행"),
 "Grooming Tips": (0.55, "Grooming App 승인 선례의 Tips 평행"),
 "Loyalty Tips": (0.55, "Loyalty App 승인 선례의 Tips 평행"),
 "Wheel Tips": (0.55, "Wheel App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Exam Advice": "직전 승인 Exam Tips와 동일 기능 의미 중복",
 "Hygiene Advice": "직전 승인 Hygiene Tips와 동일 기능 의미 중복",
 "Cistern Advice": "직전 승인 Cistern Tips와 동일 기능 의미 중복",
 "Bakery Advice": "이번 배치 승인 Bakery Tips와 동일 기능 의미 중복",
 "Grooming Advice": "이번 배치 승인 Grooming Tips와 동일 기능 의미 중복",
 "Loyalty Advice": "이번 배치 승인 Loyalty Tips와 동일 기능 의미 중복",
 "Wheel Advice": "이번 배치 승인 Wheel Tips와 동일 기능 의미 중복",
}

R = {
 "Lawsuit Counter": "계수·카운터 중의로 불분명", "Divorce Draft": "초안 대상 불분명",
 "Custody Item": "항목 지칭으로 제품 불분명", "Immigration Signature": "서명 대상 불분명",
 "Testament Repository": "저장소 지칭으로 제품 불분명", "Notary Authorization": "결합 불성립",
 "Mediation Simulator": "결합 불성립", "Guardianship Temperature": "결합 불성립",
 "Trademark Hazard": "결합 불성립", "Sedation Workbook": "워크북 대상 불분명",
 "Playtime Mode": "기능 토글로 읽혀 제품 불분명", "Conditioner Spec": "사양 참조로 제품 불분명",
 "Pickup Quantity": "수량 대상 불분명", "Ductless Login": "제품 불분명",
 "Fob Analysis": "분석 대상 불분명", "Fence Coach": "코칭 대상 불분명",
 "Hiking Habit": "결합 불성립", "Patent Desk": "책상·서비스 데스크 중의로 불분명",
 "Copyright Lab": "실험실 중의로 불분명", "Migraine Agreement": "결합 불성립",
 "Insomnia Validation": "결합 불성립", "Skydiving Availability": "상태 명사로 제품명 부자연",
 "Acne Eligibility": "결합 불성립", "Snowboarding Feedback": "결합 불성립",
 "Eczema Invoice": "결합 불성립", "Ziplining Warranty": "결합 불성립",
 "Psoriasis Deposit": "결합 불성립", "Sledding Correction": "결합 불성립",
 "Vertigo Revision": "결합 불성립", "Diving Simulator": "결합 불성립",
 "Arthritis Predictor": "예측 대상 불분명", "Sailing Recipe": "결합 불성립",
 "Rafting Expense": "결합 불성립", "Pregnancy Newsletter": "결합 불성립",
 "Climbing Onboarding": "결합 불성립", "Fertility Checkin": "결합 불성립",
 "Biking Weight": "결합 불성립(속성 지칭)", "Thyroid Distance": "결합 불성립",
 "Golf Type": "결합 불성립(분류 대상 부자연)", "Cholesterol Clock": "결합 불성립",
 "Fishing Depth": "결합 불성립", "Hypertension Height": "결합 불성립",
 "Camping Pressure": "결합 불성립", "Anemia Load": "결합 불성립",
 "Glamping Brightness": "결합 불성립", "Heartburn Frequency": "결합 불성립",
 "Stargazing Usage": "사용 지칭으로 제품 불분명", "Constipation Condition": "상태 명사로 제품명 부자연",
 "Birdwatching Cycle": "주기 지칭으로 제품 불분명", "Concussion Breakdown": "내역·고장 중의로 불분명",
 "Canyon Reception": "리셉션·수신 중의로 불분명", "Sprain Followup": "후속 지칭으로 제품 불분명",
 "Geyser Approval": "승인 지칭으로 제품 불분명", "Fracture Matrix": "행렬·매트릭스 중의로 불분명",
 "Fjord Evaluation": "평가 대상 불분명", "Insulin Questionnaire": "설문 대상 불분명",
 "Savanna Utilization": "활용 지칭으로 제품 불분명", "Tundra Benefit": "혜택 지칭으로 제품 불분명",
 "Prairie Requirement": "요건 지칭으로 제품 불분명", "Marsh Depreciation": "결합 불성립",
 "Cove Resignation": "결합 불성립", "Cliff Hazard": "결합 불성립",
 "Cavern Guarantor": "보증인 명사 결합 불성립", "Oasis Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Dune Tutorial": "동물 대상 결합 불성립", "Whale Handbook": "동물 대상 결합 불성립",
 "Dolphin Timetable": "동물 대상 결합 불성립", "Penguin Opinion": "동물 대상 결합 불성립",
 "Flamingo Gift": "결합 불성립", "Turtle Retreat": "동물 대상 결합 불성립",
 "Moose Tournament": "동물 대상 결합 불성립", "Bison Flyer": "동물 대상 결합 불성립",
 "Reindeer App": "동물 지칭으로 제품 불분명", "Curriculum Mode": "기능 토글로 읽혀 제품 불분명",
 "Incident Spec": "사양 참조로 제품 불분명", "Season Login": "선례 기각(App 기각) 계열",
 "Garment Coach": "코칭 대상 불분명", "Fleet Quantity": "수량 대상 불분명",
 "Blast Login": "선례 기각(App 기각) 계열", "Vent Analysis": "분석 대상 불분명",
 "Rekeying Coach": "코칭 대상 불분명", "Lawyer Reference": "참조 대상 불분명",
 "Attorney Review": "리뷰 대상 불분명", "Court Humidity": "결합 불성립",
 "Background App": "배경화면·신원조회 중의로 불분명", "Souvenir Workbook": "워크북 대상 불분명",
 "Trombone Mode": "기능 토글로 읽혀 제품 불분명", "Savings Quantity": "수량 대상 불분명",
 "Judge Login": "선례 기각(App 기각) 계열", "Forwarder Analysis": "분석 대상 불분명",
 "Showing Coach": "코칭 대상 불분명", "Exclusion Habit": "선례 기각(App 기각) 계열",
 "Jury Terminal": "터미널 중의로 불분명", "Lawsuit Booth": "부스 중의로 불분명",
 "Divorce Summary": "요약 대상 불분명", "Custody Unit": "단위 지칭으로 제품 불분명",
 "Immigration Marker": "표식 지칭으로 제품 불분명", "Mediation Predictor": "예측 대상 불분명",
 "Guardianship Pressure": "결합 불성립",
 "Trademark Guarantor": "보증인 명사 결합 불성립", "Exam Workbook": "워크북 대상 불분명",
 "Sedation Mode": "기능 토글로 읽혀 제품 불분명", "Playtime Spec": "선례 기각(App 기각) 계열",
 "Conditioner Quantity": "수량 대상 불분명", "Pickup Login": "제품 불분명",
 "Ductless Analysis": "분석 대상 불분명", "Fob Coach": "코칭 대상 불분명",
 "Fence Habit": "결합 불성립", "Patent Radar": "레이더 기능 지칭으로 제품 불분명",
 "Copyright Station": "역·정거장 중의로 불분명", "Migraine Reply": "결합 불성립",
 "Insomnia Lookup": "탐색 대상 불분명", "Skydiving Eligibility": "결합 불성립",
 "Acne Broadcast": "결합 불성립", "Snowboarding Invoice": "결합 불성립",
 "Eczema Renewal": "결합 불성립", "Ziplining Deposit": "결합 불성립",
 "Psoriasis Certification": "결합 불성립", "Sledding Revision": "결합 불성립",
 "Vertigo Payment": "결합 불성립", "Diving Predictor": "예측 대상 불분명",
 "Arthritis Seal": "결합 불성립", "Rafting Newsletter": "결합 불성립",
 "Pregnancy Inventory": "결합 불성립", "Climbing Checkin": "결합 불성립",
 "Fertility Size": "결합 불성립(속성 지칭)", "Biking Distance": "결합 불성립",
 "Thyroid Range": "결합 불성립", "Golf Clock": "결합 불성립",
 "Cholesterol Time": "결합 불성립", "Fishing Height": "결합 불성립",
 "Hypertension Width": "결합 불성립", "Camping Load": "결합 불성립",
 "Anemia Voltage": "결합 불성립", "Glamping Frequency": "결합 불성립",
 "Heartburn Compatibility": "상태 명사로 제품명 부자연", "Stargazing Condition": "상태 명사로 제품명 부자연",
 "Constipation Humidity": "결합 불성립", "Birdwatching Breakdown": "내역·고장 중의로 불분명",
 "Concussion Sensor": "결합 불성립", "Canyon Followup": "후속 지칭으로 제품 불분명",
 "Sprain Approval": "승인 지칭으로 제품 불분명", "Geyser Matrix": "행렬·매트릭스 중의로 불분명",
 "Fracture Evaluation": "평가 대상 불분명", "Fjord Questionnaire": "설문 대상 불분명",
 "Insulin Utilization": "활용 지칭으로 제품 불분명", "Savanna Benefit": "혜택 지칭으로 제품 불분명",
 "Tundra Requirement": "요건 지칭으로 제품 불분명", "Prairie Depreciation": "결합 불성립",
 "Marsh Resignation": "결합 불성립", "Cove Hazard": "결합 불성립",
 "Cliff Guarantor": "보증인 명사 결합 불성립", "Cavern Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Oasis Tutorial": "동물 대상 결합 불성립", "Dune Handbook": "동물 대상 결합 불성립",
 "Whale Timetable": "동물 대상 결합 불성립", "Dolphin Opinion": "동물 대상 결합 불성립",
 "Penguin Gift": "결합 불성립", "Flamingo Retreat": "동물 대상 결합 불성립",
 "Turtle Tournament": "동물 대상 결합 불성립", "Moose Flyer": "동물 대상 결합 불성립",
 "Bison App": "동물 지칭으로 제품 불분명", "Reindeer Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Hygiene Workbook": "워크북 대상 불분명", "Curriculum Spec": "사양 참조로 제품 불분명",
 "Incident Quantity": "수량 대상 불분명", "Season Analysis": "선례 기각(App 기각) 계열",
 "Garment Habit": "결합 불성립", "Fleet Login": "제품 불분명",
 "Blast Analysis": "선례 기각(App 기각) 계열", "Vent Coach": "코칭 대상 불분명",
 "Rekeying Habit": "결합 불성립", "Lawyer Forecast": "예측 대상 불분명",
 "Attorney Recipe": "결합 불성립", "Court Episode": "결합 불성립",
 "Cistern Workbook": "워크북 대상 불분명", "Souvenir Mode": "기능 토글로 읽혀 제품 불분명",
 "Trombone Spec": "사양 참조로 제품 불분명",
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
out = base + r"\_dec_c24.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
