# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk43_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Storytime App": (0.65, "아동 동화 앱(실재 시장)"),
 "Sofa Tips": (0.55, "소파 클리닝 팁(App→Tips 평행)"),
 "Counseling App": (0.65, "상담 예약 앱(실재 시장)"),
 "Diving Recorder": (0.55, "다이빙 로그 기록(다이브 로그북 실재)"),
 "Camping Guide": (0.55, "캠핑 가이드(캠핑장 가이드 실재)"),
 "Treatment App": (0.55, "치료 경과 관리 앱(치과 실무 실재)"),
 "Preplanning App": (0.65, "장례 사전 계획 앱(실재 시장)"),
 "Schedule Tips": (0.55, "예약 스케줄 팁(App→Tips 평행)"),
 "Flossing App": (0.6, "치실 습관 앱(실재)"),
 "Storytime Tips": (0.55, "동화 읽기 팁(App→Tips 평행)"),
 "Guardianship Guide": (0.55, "후견 절차 가이드(법원 셀프헬프 실재)"),
 "Trim App": (0.55, "헤어 트리밍 예약 앱(살롱 실재)"),
 "Counseling Tips": (0.55, "상담 준비 팁(App→Tips 평행)"),
 "Eczema Kit": (0.55, "아토피 관리 키트(Psoriasis Kit 평행)"),
}
R_DUP = {
 "Coloring Advice": "동일 배치 승인된 Coloring App/Tips와 동일 기능 의미 중복",
 "Keyless Advice": "동일 배치 승인된 Keyless App/Tips와 동일 기능 의미 중복",
 "Billing Advice": "동일 배치 승인된 Billing App/Tips와 동일 기능 의미 중복",
 "Consultation Advice": "동일 배치 승인된 Consultation App/Tips와 동일 기능 의미 중복",
 "Sofa Advice": "동일 배치 승인된 Sofa App/Tips와 동일 기능 의미 중복",
}
R = {
 "Interpreter Login": "제품 불분명", "Route Analysis": "분석 대상 불분명",
 "Lighting Coach": "코칭 대상 불분명", "Favor Habit": "결합 불성립",
 "Lawyer Token": "결합 불성립", "Attorney Checker": "검사 대상 불분명",
 "Court Ping": "결합 불성립", "Judge Length": "결합 불성립",
 "Jury Utilization": "상태 명사로 제품명 부자연", "Ointment Workbook": "워크북 대상 불분명",
 "Humidifier Mode": "기능 토글로 읽혀 제품 불분명", "Combination Spec": "사양 참조로 제품 불분명",
 "Vocabulary Quantity": "수량 대상 불분명", "Reimbursement Login": "제품 불분명",
 "License Analysis": "분석 대상 불분명", "Registrar Coach": "코칭 대상 불분명",
 "Landscaping Habit": "결합 불성립", "Lawsuit Compass": "결합 불성립",
 "Divorce Ring": "결합 불성립", "Custody Lobby": "결합 불성립",
 "Immigration Code": "결합 불성립", "Testament Debt": "결합 불성립",
 "Notary Subsidy": "결합 불성립", "Mediation Recorder": "기록 대상 불분명",
 "Guardianship Template": "결합 불성립", "Trademark Payment": "결합 불성립",
 "Patent Speed": "결합 불성립", "Copyright Questionnaire": "결합 불성립(문서명으로 제품 불분명)",
 "Capacitor Tips": "팁 대상 불분명(Capacitor App 기각 선례)", "Clubhouse Workbook": "워크북 대상 불분명",
 "Skiing Mode": "기능 토글로 읽혀 제품 불분명", "Repertoire Spec": "사양 참조로 제품 불분명",
 "Hospital Quantity": "수량 대상 불분명", "Inheritance Login": "제품 불분명",
 "Bulk Analysis": "분석 대상 불분명", "Comparable Coach": "코칭 대상 불분명",
 "Payout Habit": "결합 불성립", "Migraine Penalty": "결합 불성립",
 "Insomnia Graph": "그래프 대상 불분명", "Skydiving Diagram": "도식 대상 불분명",
 "Acne Schematic": "도식 대상 불분명", "Snowboarding Rendering": "결합 불성립",
 "Eczema Notification": "알림 내용 불특정", "Ziplining Message": "결합 불성립",
 "Psoriasis Total": "결합 불성립", "Sledding Announcement": "결합 불성립",
 "Vertigo Calculator": "계산 대상 불분명", "Arthritis Estimator": "산출 대상 불분명",
 "Sailing Timer": "결합 불성립(Timer 계열 기각 선례)", "Menopause Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Rafting Stage": "단계 대상 불분명", "Pregnancy Result": "결합 불성립",
 "Climbing Trend": "결합 불성립", "Fertility Comparison": "비교 대상 불분명",
 "Biking Record": "기록 대상 불분명(Camping Record 기각 선례)", "Thyroid Copy": "결합 불성립",
 "Golf Forecast": "결합 불성립", "Cholesterol Deadline": "결합 불성립",
 "Fishing Diagnostic": "진단 대상 불분명", "Hypertension Progress": "진행 대상 불분명",
 "Anemia Rating": "평가 대상 불분명", "Glamping Account": "결합 불성립",
 "Heartburn Case": "결합 불성립(Case 계열 기각 선례)", "Stargazing Lookup": "탐색 대상 불분명",
 "Constipation Ping": "결합 불성립", "Birdwatching Eligibility": "결합 불성립",
 "Concussion Broadcast": "결합 불성립", "Canyon Appointment": "약속 대상 불분명",
 "Sprain Feedback": "결합 불성립", "Geyser Invoice": "결합 불성립",
 "Fracture Renewal": "갱신 대상 불분명", "Fjord Quote": "인용·견적 중의로 대상 불분명",
 "Insulin Warranty": "결합 불성립", "Savanna Deposit": "결합 불성립",
 "Tundra Certification": "결합 불성립", "Prairie Nomination": "결합 불성립",
 "Marsh Correction": "결합 불성립", "Cove Revision": "결합 불성립",
 "Cliff Payment": "결합 불성립", "Cavern Verification": "결합 불성립",
 "Oasis Simulator": "결합 불성립", "Dune Predictor": "예측 대상 불분명",
 "Whale Seal": "결합 불성립", "Dolphin Review": "결합 불성립",
 "Penguin Recipe": "결합 불성립", "Flamingo Video": "결합 불성립",
 "Turtle Diary": "결합 불성립", "Moose Refund": "결합 불성립",
 "Bison Expense": "결합 불성립", "Reindeer Newsletter": "결합 불성립",
 "Care Workbook": "워크북 대상 불분명", "Contract Mode": "기능 토글로 읽혀 제품 불분명",
 "Irrigation Spec": "사양 참조로 제품 불분명", "Supply Quantity": "수량 대상 불분명",
 "Delivery Login": "제품 불분명", "Service Analysis": "분석 대상 불분명",
 "Retail Coach": "코칭 대상 불분명", "Adherence Habit": "결합 불성립",
 "Container Workbook": "워크북 대상 불분명", "Certification Mode": "기능 토글로 읽혀 제품 불분명",
 "Reserve Spec": "사양 참조로 제품 불분명", "Blower Quantity": "수량 대상 불분명",
 "Padlock Login": "제품 불분명", "Interpreter Analysis": "분석 대상 불분명",
 "Route Coach": "코칭 대상 불분명", "Lighting Habit": "결합 불성립",
 "Lawyer Signature": "결합 불성립", "Attorney Detector": "탐지 대상 불분명",
 "Court Model": "결합 불성립", "Judge Weight": "결합 불성립",
 "Jury Benefit": "결합 불성립", "Flossing App SKIP": "",
 "Coloring Workbook": "워크북 대상 불분명", "Ointment Mode": "기능 토글로 읽혀 제품 불분명",
 "Humidifier Spec": "사양 참조로 제품 불분명", "Combination Quantity": "수량 대상 불분명",
 "Vocabulary Login": "제품 불분명", "Reimbursement Analysis": "분석 대상 불분명",
 "License Coach": "코칭 대상 불분명", "Registrar Habit": "결합 불성립",
 "Lawsuit Beacon": "결합 불성립", "Divorce Gate": "결합 불성립",
 "Custody Ticker": "결합 불성립", "Immigration List": "결합 불성립",
 "Testament Fund": "결합 불성립", "Notary Discount": "판촉 계열 기각 선례",
 "Mediation Estimator": "산출 대상 불분명", "Trademark Verification": "결합 불성립",
 "Patent Depth": "결합 불성립", "Copyright Utilization": "상태 명사로 제품명 부자연",
 "Trim App SKIP": "", "Capacitor Advice": "팁 대상 불분명",
 "Keyless Workbook": "워크북 대상 불분명", "Clubhouse Mode": "기능 토글로 읽혀 제품 불분명",
 "Skiing Spec": "사양 참조로 제품 불분명", "Repertoire Quantity": "수량 대상 불분명",
 "Hospital Login": "제품 불분명", "Inheritance Analysis": "분석 대상 불분명",
 "Bulk Coach": "코칭 대상 불분명", "Comparable Habit": "결합 불성립",
 "Migraine Markup": "마크업 대상 불분명", "Insomnia Label": "결합 불성립",
 "Skydiving Schematic": "도식 대상 불분명", "Acne Layout": "결합 불성립",
 "Snowboarding Notification": "알림 내용 불특정", "Ziplining Total": "결합 불성립",
 "Psoriasis Widget": "결합 불성립", "Sledding Calculator": "계산 대상 불분명(Rafting Calculator 기각 선례)",
 "Vertigo Converter": "변환 대상 불분명", "Diving Estimator": "산출 대상 불분명",
 "Arthritis Checker": "검사 대상 불분명(Climbing Checker 기각 선례)", "Sailing Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Menopause Guardian": "감시 대상 불분명", "Rafting Result": "결합 불성립",
 "Pregnancy Streak": "결합 불성립", "Climbing Comparison": "비교 대상 불분명",
 "Fertility Proposal": "제안 대상 불분명", "Biking Copy": "결합 불성립",
 "Thyroid Reading": "수치 대상 불분명(Anemia Reading 기각 선례)", "Golf Deadline": "결합 불성립",
 "Cholesterol Duration": "결합 불성립", "Fishing Progress": "진행 대상 불분명",
 "Hypertension Authorization": "결합 불성립", "Camping Rating": "평가 대상 불분명",
 "Anemia Agreement": "결합 불성립", "Glamping Case": "결합 불성립(Case 계열 기각 선례)",
 "Heartburn Match": "결합 불성립(Match 계열 기각 선례)", "Stargazing Ping": "결합 불성립",
 "Constipation Model": "결합 불성립", "Birdwatching Broadcast": "결합 불성립",
 "Concussion Barcode": "결합 불성립", "Canyon Feedback": "결합 불성립",
 "Sprain Invoice": "결합 불성립", "Geyser Renewal": "갱신 대상 불분명",
 "Fracture Quote": "인용·견적 중의로 대상 불분명", "Fjord Warranty": "결합 불성립",
 "Insulin Deposit": "결합 불성립", "Savanna Certification": "결합 불성립",
 "Tundra Nomination": "결합 불성립", "Prairie Correction": "결합 불성립",
 "Marsh Revision": "결합 불성립", "Cove Payment": "결합 불성립",
 "Cliff Verification": "결합 불성립",
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
out = base + r"\_dec_c43.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
