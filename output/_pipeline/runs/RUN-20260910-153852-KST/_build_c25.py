# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk24_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Salary App": (0.55, "급여 계산·명세 관리 앱(실재)"),
 "Salary Tips": (0.55, "Salary App 승인 선례의 Tips 평행"),
 "Sponsor App": (0.55, "스폰서십 계약·혜택 관리 앱(실재)"),
 "Sponsor Tips": (0.55, "Sponsor App 승인 선례의 Tips 평행"),
 "Invite App": (0.55, "행사 초대장 발송·관리 앱(실재)"),
 "Invite Tips": (0.55, "Invite App 승인 선례의 Tips 평행"),
 "Publisher App": (0.55, "콘텐츠 발행·구독 관리 앱(실재)"),
 "Offer App": (0.55, "채용 오퍼·제안 관리 앱(실재)"),
 "Divorce Timeline": (0.55, "이혼 절차 일정 관리(Timetable/Calendar 절차 명사 선례 평행)"),
 "Divorce Reminder": (0.55, "이혼 절차 기한 알림 관리(Notification 절차 명사 선례 평행)"),
 "Custody Plan": (0.55, "양육 계획 수립·관리(Plan 절차 명사 선례 평행)"),
 "Notary Guide": (0.55, "공증 절차 안내 가이드(Patent Handbook 평행)"),
 "Lawyer Deadline": (0.55, "법률 절차 마감일 관리(Notary Deadline 평행)"),
 "Trademark Tutorial": (0.55, "상표 등록 절차 튜토리얼(Patent Handbook 평행)"),
 "Sailing Diary": (0.55, "세일링 항해 기록 일지(Rafting Diary 평행)"),
}

R_DUP = {
 "Windshield Advice": "이번 배치 승인 Windshield Tips와 동일 기능 의미 중복",
 "Reservation Advice": "이번 배치 승인 Reservation Tips와 동일 기능 의미 중복",
 "Coping Advice": "이번 배치 승인 Coping Tips와 동일 기능 의미 중복",
}

R = {
 "Savings Login": "제품 불분명", "Judge Analysis": "선례 기각(App 기각) 계열",
 "Forwarder Coach": "코칭 대상 불분명", "Showing Habit": "결합 불성립",
 "Jury Center": "센터 지칭으로 제품 불분명", "Lawsuit Kiosk": "키오스크 지칭으로 제품 불분명",
 "Divorce Reminder2": "", "Custody Cost": "비용 결합 불성립",
 "Immigration Balance": "잔액·균형 중의로 불분명", "Testament Calculator": "계산 도구 지칭으로 제품 불분명",
 "Mediation Seal": "결합 불성립", "Guardianship Load": "결합 불성립",
 "Trademark Tuner": "튜너 기능 지칭으로 제품 불분명", "Background Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Bakery Workbook": "워크북 대상 불분명", "Exam Mode": "기능 토글로 읽혀 제품 불분명",
 "Sedation Spec": "사양 참조로 제품 불분명", "Playtime Quantity": "수량 대상 불분명",
 "Conditioner Login": "제품 불분명", "Pickup Analysis": "분석 대상 불분명",
 "Ductless Coach": "코칭 대상 불분명", "Fob Habit": "결합 불성립",
 "Patent Relay": "릴레이·중계 중의로 불분명", "Copyright Terminal": "터미널 중의로 불분명",
 "Migraine Account": "결합 불성립", "Insomnia Ping": "결합 불성립",
 "Skydiving Broadcast": "결합 불성립", "Acne Barcode": "결합 불성립",
 "Snowboarding Renewal": "결합 불성립", "Eczema Quote": "인용·견적 중의로 불분명",
 "Ziplining Certification": "결합 불성립", "Psoriasis Nomination": "결합 불성립",
 "Sledding Payment": "결합 불성립", "Vertigo Verification": "결합 불성립",
 "Diving Seal": "결합 불성립", "Arthritis Review": "리뷰 대상 불분명",
 "Menopause Refund": "결합 불성립", "Rafting Inventory": "결합 불성립",
 "Pregnancy Claim": "결합 불성립", "Climbing Size": "결합 불성립(속성 지칭)",
 "Fertility Length": "결합 불성립(속성 지칭)", "Biking Range": "결합 불성립",
 "Thyroid Limit": "결합 불성립", "Golf Time": "결합 불성립",
 "Cholesterol Speed": "결합 불성립", "Fishing Width": "결합 불성립",
 "Hypertension Temperature": "결합 불성립", "Camping Voltage": "결합 불성립",
 "Anemia Wattage": "결합 불성립", "Glamping Compatibility": "상태 명사로 제품명 부자연",
 "Heartburn Capacity": "상태 명사로 제품명 부자연", "Stargazing Humidity": "결합 불성립",
 "Constipation Episode": "결합 불성립", "Birdwatching Sensor": "결합 불성립",
 "Concussion Reception": "리셉션·수신 중의로 불분명", "Canyon Approval": "승인 지칭으로 제품 불분명",
 "Sprain Matrix": "행렬·매트릭스 중의로 불분명", "Geyser Evaluation": "평가 대상 불분명",
 "Fracture Questionnaire": "설문 대상 불분명", "Fjord Utilization": "활용 지칭으로 제품 불분명",
 "Insulin Benefit": "혜택 지칭으로 제품 불분명", "Savanna Requirement": "요건 지칭으로 제품 불분명",
 "Tundra Depreciation": "결합 불성립", "Prairie Resignation": "결합 불성립",
 "Marsh Hazard": "결합 불성립", "Cove Guarantor": "보증인 명사 결합 불성립",
 "Cliff Tuner": "튜너 기능 지칭으로 제품 불분명", "Cavern Tutorial": "terrain 대상 결합 불성립",
 "Oasis Handbook": "terrain 대상 결합 불성립", "Dune Timetable": "terrain 대상 결합 불성립",
 "Whale Opinion": "동물 대상 결합 불성립", "Dolphin Gift": "결합 불성립",
 "Penguin Retreat": "동물 대상 결합 불성립", "Flamingo Tournament": "동물 대상 결합 불성립",
 "Turtle Flyer": "동물 대상 결합 불성립", "Moose App": "동물 지칭으로 제품 불분명",
 "Bison Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Reindeer Advice": "선례 기각(App 기각) 계열",
 "Grooming Workbook": "워크북 대상 불분명", "Hygiene Mode": "기능 토글로 읽혀 제품 불분명",
 "Curriculum Quantity": "수량 대상 불분명", "Incident Login": "제품 불분명",
 "Season Coach": "선례 기각(App 기각) 계열", "Loyalty Workbook": "워크북 대상 불분명",
 "Fleet Analysis": "분석 대상 불분명", "Blast Coach": "선례 기각(App 기각) 계열",
 "Vent Habit": "결합 불성립", "Attorney Video": "직함 대상 영상 결합 부자연(Judge Handbook 기각 선례)",
 "Court Cycle": "주기 지칭으로 제품 불분명", "Coping Workbook": "워크북 대상 불분명",
 "Wheel Workbook": "워크북 대상 불분명", "Cistern Mode": "기능 토글로 읽혀 제품 불분명",
 "Souvenir Spec": "사양 참조로 제품 불분명", "Trombone Quantity": "수량 대상 불분명",
 "Savings Analysis": "분석 대상 불분명", "Judge Coach": "선례 기각(App 기각) 계열",
 "Forwarder Habit": "결합 불성립", "Jury Zone": "구역 지칭으로 제품 불분명",
 "Lawsuit Bay": "베이 지칭으로 제품 불분명", "Custody Plan2": "",
 "Immigration Interest": "이자·관심 중의로 불분명", "Testament Converter": "변환 도구 지칭으로 제품 불분명",
 "Notary Rating": "평가 대상 불분명", "Mediation Review": "리뷰 대상 불분명",
 "Guardianship Voltage": "결합 불성립", "Trademark Tutorial2": "",
 "Windshield Workbook": "워크북 대상 불분명", "Bakery Mode": "기능 토글로 읽혀 제품 불분명",
 "Exam Spec": "사양 참조로 제품 불분명", "Sedation Quantity": "수량 대상 불분명",
 "Playtime Login": "제품 불분명", "Conditioner Analysis": "분석 대상 불분명",
 "Pickup Coach": "코칭 대상 불분명", "Ductless Habit": "결합 불성립",
 "Patent Vault": "금고 지칭으로 제품 불분명", "Copyright Center": "센터 지칭으로 제품 불분명",
 "Migraine Case": "결합 불성립(Case 계열 기각 선례)", "Insomnia Model": "모델 지칭으로 제품 불분명",
 "Skydiving Barcode": "결합 불성립", "Acne Appointment": "약속 대상 불분명",
 "Snowboarding Quote": "인용·견적 중의로 불분명", "Eczema Warranty": "결합 불성립",
 "Ziplining Nomination": "결합 불성립", "Psoriasis Correction": "결합 불성립",
 "Sledding Verification": "결합 불성립", "Vertigo Simulator": "결합 불성립",
 "Diving Review": "리뷰 대상 불분명", "Arthritis Recipe": "결합 불성립",
 "Sailing Refund": "결합 불성립", "Menopause Expense": "결합 불성립",
 "Rafting Claim": "결합 불성립", "Pregnancy Onboarding": "결합 불성립",
 "Climbing Length": "결합 불성립(속성 지칭)", "Fertility Weight": "결합 불성립(속성 지칭)",
 "Biking Limit": "결합 불성립", "Thyroid Type": "결합 불성립(분류 대상 부자연)",
 "Golf Speed": "결합 불성립", "Cholesterol Depth": "결합 불성립",
 "Fishing Temperature": "결합 불성립", "Hypertension Pressure": "결합 불성립",
 "Camping Wattage": "결합 불성립", "Anemia Brightness": "결합 불성립",
 "Glamping Capacity": "상태 명사로 제품명 부자연", "Heartburn Usage": "사용 지칭으로 제품 불분명",
 "Stargazing Episode": "결합 불성립", "Constipation Cycle": "주기 지칭으로 제품 불분명",
 "Birdwatching Reception": "리셉션·수신 중의로 불분명", "Concussion Followup": "후속 지칭으로 제품 불분명",
 "Canyon Matrix": "행렬·매트릭스 중의로 불분명", "Sprain Evaluation": "평가 대상 불분명",
 "Geyser Questionnaire": "설문 대상 불분명", "Fracture Utilization": "활용 지칭으로 제품 불분명",
 "Fjord Benefit": "혜택 지칭으로 제품 불분명", "Insulin Requirement": "요건 지칭으로 제품 불분명",
 "Savanna Depreciation": "결합 불성립", "Tundra Resignation": "결합 불성립",
 "Prairie Hazard": "결합 불성립", "Marsh Guarantor": "보증인 명사 결합 불성립",
 "Cove Tuner": "튜너 기능 지칭으로 제품 불분명", "Cliff Tutorial": "terrain 대상 결합 불성립",
 "Cavern Handbook": "terrain 대상 결합 불성립", "Oasis Timetable": "terrain 대상 결합 불성립",
 "Dune Opinion": "terrain 대상 결합 불성립", "Whale Gift": "결합 불성립",
 "Dolphin Retreat": "동물 대상 결합 불성립", "Penguin Tournament": "동물 대상 결합 불성립",
 "Flamingo Flyer": "동물 대상 결합 불성립", "Turtle App": "동물 지칭으로 제품 불분명",
 "Moose Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Bison Advice": "선례 기각(App 기각) 계열",
 "Reindeer Workbook": "선례 기각(App 기각) 계열", "Reservation Workbook": "워크북 대상 불분명",
 "Grooming Mode": "기능 토글로 읽혀 제품 불분명", "Hygiene Spec": "사양 참조로 제품 불분명",
 "Curriculum Login": "제품 불분명", "Incident Analysis": "분석 대상 불분명",
 "Season Habit": "선례 기각(App 기각) 계열", "Loyalty Mode": "기능 토글로 읽혀 제품 불분명",
 "Fleet Coach": "코칭 대상 불분명", "Blast Habit": "선례 기각(App 기각) 계열",
 "Lawyer Duration": "기간 속성 지칭으로 제품 불분명", "Attorney Diary": "일지 대상 불분명(Lawyer Record 기각 선례)",
 "Court Breakdown": "내역·고장 중의로 불분명", "Background Advice": "선례 기각(App 기각) 계열",
 "Wheel Mode": "기능 토글로 읽혀 제품 불분명",
}
del R["Divorce Reminder2"]
del R["Custody Plan2"]
del R["Trademark Tutorial2"]
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
out = base + r"\_dec_c25.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
