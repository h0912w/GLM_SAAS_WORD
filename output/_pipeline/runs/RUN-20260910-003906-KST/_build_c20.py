# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk20_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Feedback App": (0.6, "행사 피드백 수집 앱(실재 카테고리)"),
 "Appraisal Tips": (0.55, "차량 감정 팁(App→Tips 평행)"),
 "Elevator App": (0.6, "엘리베이터 유지보수 관리 앱(실재)"),
 "Client Tips": (0.55, "고객 관리 팁(App→Tips 평행)"),
 "Divorce Tracker": (0.55, "이혼 절차 진행 추적(Divorce 제품군 실재)"),
 "Custody Portal": (0.55, "공동양육 소통 포털(실재)"),
 "Espresso App": (0.55, "에스프레소 추출 관리 앱(실재)"),
 "Diet Tips": (0.55, "반려동물 식단 팁(App→Tips 평행)"),
 "Migraine Cost": (0.55, "편두통 치료 비용(건강 비용 축)"),
 "Hearing App": (0.55, "공청회·심리 일정 추적 앱(실재)"),
 "Creative Tips": (0.55, "크리에이티브 운영 팁(App→Tips 평행)"),
 "Referral App": (0.6, "직원 추천 채용 앱(실재 카테고리)"),
 "Feedback Tips": (0.55, "피드백 수집 팁(App→Tips 평행)"),
 "Lawyer Brief": (0.55, "법률 의견서 관리(실무 문서 실재)"),
 "Syntax App": (0.55, "구문 학습·검증 앱(실재)"),
 "Elevator Tips": (0.55, "엘리베이터 관리 팁(App→Tips 평행)"),
 "Client Advice": "R_DUP_PLACEHOLDER",
 "Radiator App": (0.55, "라디에이터·냉각계통 관리 앱(실재)"),
 "Espresso Tips": (0.55, "에스프레소 팁(App→Tips 평행)"),
}
del A["Client Advice"]
R_DUP = {
 "Franchise Advice": "동일 배치 승인된 Franchise App/Tips와 동일 기능 의미 중복",
 "Cake Advice": "동일 배치 승인된 Cake App/Tips와 동일 기능 의미 중복",
 "Orthodontics Advice": "동일 배치 승인된 Orthodontics App/Tips와 동일 기능 의미 중복",
 "Archive Advice": "동일 배치 승인된 Archive App/Tips와 동일 기능 의미 중복",
 "Appraisal Advice": "동일 배치 승인된 Appraisal App/Tips와 동일 기능 의미 중복",
 "Client Advice": "동일 배치 승인된 Client App/Tips와 동일 기능 의미 중복",
 "Diet Advice": "동일 배치 승인된 Diet App/Tips와 동일 기능 의미 중복",
}
R = {
 "Agenda Analysis": "분석 대상 불분명", "Financing Coach": "코칭 대상 불분명",
 "Compliance Habit": "결합 불성립",
 "Discharge Workbook": "워크북 대상 불분명", "Xray Mode": "기능 토글로 읽혀 제품 불분명",
 "Session Spec": "결합 불성립", "Milestone Quantity": "수량 대상 불분명",
 "Wellness Login": "결합 불성립", "Scheduling Analysis": "분석 대상 불분명",
 "Snow Coach": "코칭 대상 불분명", "Inventory Habit": "결합 불성립",
 "Lawyer Bulletin": "결합 불성립", "Attorney Serial": "결합 불성립",
 "Court Announcement": "결합 불성립", "Judge Agreement": "판사 대상 합의 불성립",
 "Jury Expense": "결합 불성립", "Lawsuit Sensor": "탐지 대상 불분명",
 "Closing Mode": "기능 토글로 읽혀 제품 불분명", "Sponge Spec": "결합 불성립",
 "Trap Quantity": "수량 대상 불분명", "Roadtrip Login": "결합 불성립",
 "Accordion Analysis": "분석 대상 불분명", "Allergy Coach": "코칭 대상 불분명",
 "Wire Habit": "결합 불성립",
 "Custody Portal R_DUP_PLACEHOLDER": "",
 "Immigration Bay": "시설 지칭으로 불성립", "Testament Summary": "Testament 계열 기각 선례",
 "Notary Fee": "결합 불성립", "Mediation Field": "결합 불성립",
 "Guardianship Sketch": "제품성 불분명", "Trademark Comparison": "비교 대상 불분명",
 "Patent Model": "결합 불성립", "Copyright Refund": "결합 불성립",
 "Stroller Workbook": "워크북 대상 불분명", "Spa Mode": "기능 토글로 읽혀 제품 불분명",
 "Curb Quantity": "수량 대상 불분명", "Vineyard Login": "결합 불성립",
 "Accompanist Analysis": "분석 대상 불분명", "Illness Coach": "코칭 대상 불분명",
 "Debtor Habit": "결합 불성립",
 "Insomnia Sum": "결합 불성립", "Skydiving Sale": "결합 불성립",
 "Acne Charge": "결합 불성립", "Snowboarding Value": "결합 불성립",
 "Eczema Stake": "결합 불성립", "Ziplining Number": "수치 지칭 부자연",
 "Psoriasis Version": "결합 불성립", "Sledding Detail": "결합 불성립",
 "Vertigo Identifier": "결합 불성립", "Diving Field": "결합 불성립",
 "Arthritis Format": "결합 불성립", "Sailing Signature": "결합 불성립",
 "Menopause Marker": "결합 불성립", "Rafting Asset": "결합 불성립",
 "Pregnancy Levy": "결합 불성립", "Climbing Discount": "결합 불성립",
 "Fertility Arrears": "결합 불성립", "Biking Markup": "결합 불성립",
 "Thyroid Redemption": "결합 불성립", "Golf Graph": "그래프 대상 불분명",
 "Cholesterol Label": "결합 불성립", "Fishing Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Hypertension Schematic": "회로도 어휘 부자연", "Camping Outline": "지형은 공예 오트라인 대상 아님",
 "Anemia Rendering": "렌더링 대상 불분명", "Glamping Count": "대상 불분명",
 "Heartburn Message": "결합 불성립", "Stargazing Repository": "결합 불성립",
 "Constipation Announcement": "결합 불성립", "Birdwatching Generator": "생성 대상 불분명",
 "Concussion Recorder": "기록 대상 불분명", "Canyon Checker": "검사 대상 불분명",
 "Sprain Detector": "탐지 대상 불분명", "Geyser Timer": "결합 불성립",
 "Fracture Workshop": "결합 불성립", "Fjord Guardian": "감시 대상 불분명",
 "Insulin Helper": "결합 불성립", "Savanna Stage": "결합 불성립",
 "Tundra Result": "결합 불성립", "Prairie Streak": "결합 불성립",
 "Marsh Rank": "결합 불성립", "Cove Trend": "결합 불성립",
 "Cliff Comparison": "비교 대상 불분명", "Cavern Proposal": "제안 대상 불분명",
 "Oasis Guarantee": "결합 불성립", "Dune Record": "기록 대상 불분명",
 "Whale Copy": "결합 불성립", "Dolphin Reading": "결합 불성립",
 "Penguin Reference": "결합 불성립", "Flamingo Forecast": "예측 대상 불분명",
 "Turtle Deadline": "결합 불성립", "Moose Duration": "결합 불성립",
 "Bison Volume": "결합 불성립", "Reindeer Diagnostic": "진단 대상 불분명",
 "Driver Workbook": "워크북 대상 불분명", "Roaming Mode": "기능 토글로 읽혀 제품 불분명",
 "Audit Spec": "결합 불성립", "Pipeline Quantity": "수량 대상 불분명",
 "Refund Login": "결합 불성립", "Reference Analysis": "분석 대상 불분명",
 "Agenda Coach": "코칭 대상 불분명", "Financing Habit": "결합 불성립",
 "Franchise Workbook": "워크북 대상 불분명", "Discharge Mode": "기능 토글로 읽혀 제품 불분명",
 "Xray Spec": "결합 불성립", "Session Quantity": "수량 대상 불분명",
 "Milestone Login": "결합 불성립", "Wellness Analysis": "분석 대상 불분명",
 "Scheduling Coach": "코칭 대상 불분명", "Snow Habit": "결합 불성립",
 "Attorney Token": "결합 불성립", "Court Calculator": "계산 대상 불분명",
 "Judge Reply": "판사 대상 회신 불성립", "Jury Newsletter": "결합 불성립",
 "Lawsuit Reception": "결합 불성립",
 "Cake Workbook": "워크북 대상 불분명", "Closing Spec": "결합 불성립",
 "Sponge Quantity": "수량 대상 불분명", "Trap Login": "결합 불성립",
 "Roadtrip Analysis": "분석 대상 불분명", "Accordion Coach": "코칭 대상 불분명",
 "Allergy Habit": "결합 불성립",
 "Divorce Flow": "결합 불성립", "Custody Console": "결합 불성립",
 "Immigration Post": "시설 지칭으로 불성립", "Testament Timeline": "Testament 계열 기각 선례",
 "Notary Item": "항목 대상 불분명", "Mediation Format": "결합 불성립",
 "Guardianship Outline": "지형은 공예 오트라인 대상 아님", "Trademark Proposal": "제안 대상 불분명",
 "Patent Availability": "상태 명사로 제품명 부자연", "Copyright Expense": "결합 불성립",
 "Orthodontics Workbook": "워크북 대상 불분명", "Stroller Mode": "기능 토글로 읽혀 제품 불분명",
 "Spa Spec": "결합 불성립", "Curb Login": "결합 불성립",
 "Vineyard Analysis": "분석 대상 불분명", "Accompanist Coach": "코칭 대상 불분명",
 "Illness Habit": "결합 불성립",
 "Migraine Price": "가격 지칭 부자연", "Insomnia Debt": "결합 불성립",
 "Skydiving Charge": "결합 불성립", "Acne Duty": "결합 불성립",
 "Snowboarding Stake": "결합 불성립", "Eczema Margin": "결합 불성립",
 "Ziplining Version": "결합 불성립", "Psoriasis Link": "결합 불성립",
 "Sledding Identifier": "결합 불성립", "Vertigo Category": "결합 불성립",
 "Diving Format": "결합 불성립", "Arthritis Serial": "결합 불성립",
 "Sailing Marker": "결합 불성립", "Menopause Balance": "결합 불성립",
 "Rafting Levy": "결합 불성립", "Pregnancy Due": "결합 불성립",
 "Climbing Arrears": "결합 불성립", "Fertility Advance": "결합 불성립",
 "Biking Redemption": "결합 불성립", "Thyroid Extension": "결합 불성립",
 "Golf Label": "결합 불성립", "Cholesterol Manual": "설명 대상 불분명",
 "Fishing Schematic": "회로도 어휘 부자연", "Hypertension Layout": "결합 불성립",
 "Camping Rendering": "렌더링 대상 불분명", "Anemia Notification": "결합 불성립",
 "Glamping Message": "결합 불성립", "Heartburn Total": "결합 불성립",
 "Stargazing Announcement": "결합 불성립", "Constipation Calculator": "계산 대상 불분명",
 "Birdwatching Recorder": "기록 대상 불분명", "Concussion Estimator": "산출 대상 불분명",
 "Canyon Detector": "탐지 대상 불분명", "Sprain Timer": "결합 불성립",
 "Geyser Workshop": "결합 불성립", "Fracture Guardian": "감시 대상 불분명",
 "Fjord Helper": "결합 불성립",
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
out = base + r"\_dec_c20.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
