# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk41_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Glamping Guide": (0.55, "글램핑 사이트 가이드(실재 콘텐츠)"),
 "Contract App": (0.6, "방역 서비스 계약 관리 앱(계약 관리 실재)"),
 "Irrigation Tips": (0.55, "관수 관리 팁(App→Tips 평행)"),
 "Certification App": (0.55, "항공 자격 추적 앱(실재)"),
 "Humidifier Tips": (0.55, "가습기 사용 팁(App→Tips 평행)"),
 "Vocabulary Workbook": (0.55, "어휘 연습 워크북(실재 교재)"),
 "Custody Chart": (0.55, "양육 일정 차트(공동양육 앱 실재)"),
 "Mediation Calculator": (0.55, "합의안 산정 계산기(settlement calc 실재)"),
 "Clubhouse App": (0.6, "HOA 클럽하우스 예약 앱(어메니티 예약 실재)"),
 "Skiing Tips": (0.55, "스키 팁(App→Tips 평행)"),
 "Acne Manual": (0.55, "여드름 자가관리 매뉴얼(Arthritis Manual 평행)"),
 "Psoriasis Kit": (0.55, "건선 관리 키트(Arthritis Kit 평행)"),
 "Diving Calculator": (0.55, "다이빙 계획 계산기(감압 계산 실재)"),
 "Menopause Checker": (0.55, "폐경 단계 자가 확인(Checker 실재)"),
 "Care App": (0.65, "시니어 케어 조율 앱(실재 시장)"),
 "Contract Tips": (0.55, "계약 관리 팁(App→Tips 평행)"),
 "Container App": (0.65, "컨테이너 추적 앱(실재 시장)"),
 "Certification Tips": (0.55, "자격 취득 팁(App→Tips 평행)"),
 "Coloring App": (0.6, "헤어 컬러 시뮬레이션 앱(실재)"),
}
R_DUP = {
 "Menopause Estimator": "동일 배치 승인된 Menopause Calculator와 기능 중복(Fertility Estimator 선례)",
 "Repertoire Advice": "동일 배치 승인된 Repertoire App/Tips와 동일 기능 의미 중복",
 "Irrigation Advice": "동일 배치 승인된 Irrigation App/Tips와 동일 기능 의미 중복",
 "Humidifier Advice": "동일 배치 승인된 Humidifier App/Tips와 동일 기능 의미 중복",
}
R = {
 "Sailing Recorder": "기록 대상 불분명", "Rafting Timer": "결합 불성립(Timer 계열 기각 선례)",
 "Pregnancy Workshop": "결합 불성립(Workshop 계열 기각 선례)", "Climbing Stage": "단계 대상 불분명",
 "Fertility Result": "결합 불성립", "Biking Trend": "결합 불성립",
 "Thyroid Comparison": "비교 대상 불분명", "Golf Record": "기록 대상 불분명",
 "Cholesterol Copy": "결합 불성립", "Fishing Forecast": "결합 불성립",
 "Hypertension Deadline": "결합 불성립", "Camping Diagnostic": "진단 대상 불분명",
 "Anemia Progress": "진행 대상 불분명", "Heartburn Rating": "평가 대상 불분명",
 "Stargazing Account": "결합 불성립", "Constipation Case": "결합 불성립(Case 계열 기각 선례)",
 "Birdwatching Lookup": "탐색 대상 불분명", "Concussion Ping": "결합 불성립",
 "Canyon Availability": "상태 명사로 제품명 부자연", "Sprain Eligibility": "결합 불성립",
 "Geyser Broadcast": "결합 불성립", "Fracture Barcode": "결합 불성립",
 "Fjord Appointment": "약속 대상 불분명", "Insulin Feedback": "결합 불성립",
 "Savanna Invoice": "결합 불성립", "Tundra Renewal": "갱신 대상 불분명",
 "Prairie Quote": "인용·견적 중의로 대상 불분명", "Marsh Warranty": "결합 불성립",
 "Cove Deposit": "결합 불성립", "Cliff Certification": "결합 불성립",
 "Cavern Nomination": "결합 불성립", "Oasis Correction": "결합 불성립",
 "Dune Revision": "결합 불성립", "Whale Payment": "결합 불성립",
 "Dolphin Verification": "결합 불성립", "Penguin Simulator": "결합 불성립",
 "Flamingo Predictor": "예측 대상 불분명", "Turtle Seal": "결합 불성립",
 "Moose Review": "결합 불성립", "Bison Recipe": "결합 불성립",
 "Reindeer Video": "결합 불성립", "Irrigation Tips SKIP": "",
 "Supply Advice": "팁 대상 불분명(Supply App 기각 선례)", "Delivery Workbook": "워크북 대상 불분명",
 "Service Mode": "기능 토글로 읽혀 제품 불분명", "Retail Spec": "사양 참조로 제품 불분명",
 "Adherence Quantity": "수량 대상 불분명", "Berth Login": "제품 불분명",
 "Compressor Habit": "결합 불성립", "Reserve Tips": "팁 대상 불분명(Reserve App 기각 선례)",
 "Blower Advice": "팁 대상 불분명(Blower App 기각 선례)", "Padlock Workbook": "워크북 대상 불분명",
 "Interpreter Mode": "기능 토글로 읽혀 제품 불분명", "Route Spec": "사양 참조로 제품 불분명",
 "Lighting Quantity": "수량 대상 불분명", "Favor Login": "제품 불분명",
 "Occupant Analysis": "분석 대상 불분명", "Technician Coach": "코칭 대상 불분명",
 "Rinse Habit": "결합 불성립", "Lawyer Field": "결합 불성립",
 "Attorney Generator": "생성 대상 불분명", "Court Match": "결합 불성립(Match 계열 기각 선례)",
 "Judge Onboarding": "결합 불성립", "Jury Matrix": "결합 불성립",
 "Ointment App": "제품 불분명(연고 단독 앱 카테고리 약함)", "Combination Advice": "팁 대상 불분명(Combination App 기각 선례)",
 "Reimbursement Mode": "기능 토글로 읽혀 제품 불분명", "License Spec": "사양 참조로 제품 불분명",
 "Registrar Quantity": "수량 대상 불분명", "Landscaping Login": "제품 불분명",
 "Opening Analysis": "분석 대상 불분명", "Bucket Coach": "코칭 대상 불분명",
 "Softener Habit": "결합 불성립", "Lawsuit Radar": "결합 불성립",
 "Divorce Rail": "결합 불성립", "Immigration Order": "결합 불성립",
 "Testament Tax": "결합 불성립(용어 결합 부자연)", "Notary Asset": "결합 불성립",
 "Guardianship Diagnostic": "진단 대상 불분명", "Trademark Nomination": "결합 불성립",
 "Patent Type": "결합 불성립", "Copyright Approval": "결합 불성립",
 "Clubhouse App SKIP": "", "Hospital Workbook": "워크북 대상 불분명",
 "Inheritance Mode": "기능 토글로 읽혀 제품 불분명", "Bulk Spec": "사양 참조로 제품 불분명",
 "Comparable Quantity": "수량 대상 불분명", "Payout Login": "제품 불분명",
 "Probation Analysis": "분석 대상 불분명", "Deck Coach": "코칭 대상 불분명",
 "Rubric Habit": "결합 불성립", "Migraine Discount": "판촉 계열 기각 선례",
 "Insomnia Redemption": "결합 불성립", "Skydiving Label": "결합 불성립",
 "Snowboarding Layout": "결합 불성립", "Eczema Sketch": "제품성 불분명",
 "Ziplining Notification": "알림 내용 불특정", "Sledding Total": "결합 불성립",
 "Vertigo Widget": "결합 불성립", "Arthritis Converter": "변환 대상 불분명",
 "Sailing Estimator": "산출 대상 불분명", "Rafting Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Pregnancy Guardian": "감시 대상 불분명", "Climbing Result": "결합 불성립",
 "Fertility Streak": "결합 불성립", "Biking Comparison": "비교 대상 불분명",
 "Thyroid Proposal": "제안 대상 불분명", "Golf Copy": "결합 불성립",
 "Cholesterol Reading": "수치 대상 불분명(Anemia Reading 기각 선례)", "Fishing Deadline": "결합 불성립",
 "Hypertension Duration": "결합 불성립", "Camping Progress": "진행 대상 불분명",
 "Anemia Authorization": "결합 불성립", "Glamping Rating": "평가 대상 불분명",
 "Heartburn Agreement": "결합 불성립", "Stargazing Case": "결합 불성립(Case 계열 기각 선례)",
 "Constipation Match": "결합 불성립(Match 계열 기각 선례)", "Birdwatching Ping": "결합 불성립",
 "Concussion Model": "결합 불성립", "Canyon Eligibility": "결합 불성립",
 "Sprain Broadcast": "결합 불성립", "Geyser Barcode": "결합 불성립",
 "Fracture Appointment": "약속 대상 불분명", "Fjord Feedback": "결합 불성립",
 "Insulin Invoice": "결합 불성립", "Savanna Renewal": "갱신 대상 불분명",
 "Tundra Quote": "인용·견적 중의로 대상 불분명", "Prairie Warranty": "결합 불성립",
 "Marsh Deposit": "결합 불성립", "Cove Certification": "결합 불성립",
 "Cliff Nomination": "결합 불성립", "Cavern Correction": "결합 불성립",
 "Oasis Revision": "결합 불성립", "Dune Payment": "결합 불성립",
 "Whale Verification": "결합 불성립", "Dolphin Simulator": "결합 불성립",
 "Penguin Predictor": "예측 대상 불분명", "Flamingo Seal": "결합 불성립",
 "Turtle Review": "결합 불성립", "Moose Recipe": "결합 불성립",
 "Bison Video": "결합 불성립", "Reindeer Diary": "결합 불성립",
 "Care App SKIP": "", "Supply Workbook": "워크북 대상 불분명",
 "Delivery Mode": "기능 토글로 읽혀 제품 불분명", "Service Spec": "사양 참조로 제품 불분명",
 "Retail Quantity": "수량 대상 불분명", "Adherence Login": "제품 불분명",
 "Berth Analysis": "분석 대상 불분명", "Container App SKIP": "",
 "Reserve Advice": "팁 대상 불분명", "Blower Workbook": "워크북 대상 불분명",
 "Padlock Mode": "기능 토글로 읽혀 제품 불분명", "Interpreter Spec": "사양 참조로 제품 불분명",
 "Route Quantity": "수량 대상 불분명", "Lighting Login": "제품 불분명",
 "Favor Analysis": "분석 대상 불분명", "Occupant Coach": "코칭 대상 불분명",
 "Technician Habit": "결합 불성립", "Lawyer Format": "결합 불성립",
 "Attorney Recorder": "기록 대상 불분명", "Court Validation": "결합 불성립",
 "Judge Checkin": "결합 불성립", "Jury Evaluation": "결합 불성립",
 "Coloring App SKIP": "", "Ointment Tips": "팁 대상 불분명(Ointment App 기각 선례)",
 "Combination Workbook": "워크북 대상 불분명", "Vocabulary Mode": "기능 토글로 읽혀 제품 불분명",
 "Reimbursement Spec": "사양 참조로 제품 불분명", "License Quantity": "수량 대상 불분명",
 "Registrar Login": "제품 불분명", "Landscaping Analysis": "분석 대상 불분명",
 "Opening Coach": "코칭 대상 불분명", "Bucket Habit": "결합 불성립",
 "Lawsuit Relay": "결합 불성립", "Divorce Trail": "결합 불성립",
 "Custody Bin": "결합 불성립", "Immigration Bill": "결합 불성립",
 "Testament Loan": "결합 불성립", "Notary Levy": "결합 불성립",
 "Mediation Converter": "변환 대상 불분명", "Guardianship Progress": "진행 대상 불분명",
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
out = base + r"\_dec_c41.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
