# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk15_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Allergy App": (0.6, "알레르기 관리 앱(실재 카테고리)"),
 "Wire Tips": (0.55, "송금 팁(App→Tips 평행)"),
 "Illness App": (0.55, "질병 경과 기록 앱(symptom tracker 실재)"),
 "Debtor Tips": (0.55, "채무 회수 팁(App→Tips 평행)"),
 "Agenda App": (0.6, "행사 안건·일정 관리 앱(실재 카테고리)"),
 "Financing Tips": (0.55, "차량 금융 팁(App→Tips 평행)"),
 "Scheduling App": (0.6, "방제 일정 관리 앱(현장 서비스 스케줄링 실재)"),
 "Snow Tips": (0.55, "제설 운영 팁(App→Tips 평행)"),
 "Accordion App": (0.6, "아코디언 학습 앱(악기 학습 실재)"),
 "Allergy Tips": (0.55, "알레르기 관리 팁(App→Tips 평행)"),
 "Patent Agreement": (0.55, "특허 계약 관리(Copyright Agreement 평행)"),
 "Accompanist App": (0.55, "반주자 매칭 앱(실재 서비스)"),
 "Illness Tips": (0.55, "질병 관리 팁(App→Tips 평행)"),
}
R_DUP = {
 "Divorce Advice": "동일 배치 승인된 Divorce App/Handbook/Tutorial/Tips와 동일 기능 의미 중복",
 "Flatbed Advice": "동일 배치 승인된 Flatbed App/Tips와 동일 기능 의미 중복",
 "Compliance Advice": "동일 배치 승인된 Compliance App/Tips와 동일 기능 의미 중복",
 "Inventory Advice": "동일 배치 승인된 Inventory App/Tips와 동일 기능 의미 중복",
 "Wire Advice": "동일 배치 승인된 Wire App/Tips와 동일 기능 의미 중복",
 "Debtor Advice": "동일 배치 승인된 Debtor App/Tips와 동일 기능 의미 중복",
}
R = {
 "Recall Spec": "결합 불성립", "Port Quantity": "수량 대상 불분명",
 "Logbook Login": "결합 불성립", "Tailings Analysis": "분석 대상 불분명",
 "Coil Coach": "코칭 대상 불분명", "Keypad Habit": "결합 불성립",
 "Lawyer Slot": "결합 불성립", "Attorney Version": "결합 불성립",
 "Court Outline": "제품성 불분명", "Judge Deadline": "판사 대상 기한 불성립",
 "Jury Verification": "결합 불성립", "Lawsuit Frequency": "결합 불성립",
 "Chassis Workbook": "워크북 대상 불분명", "Amendment Mode": "기능 토글로 읽혀 제품 불분명",
 "Salvage Spec": "결합 불성립", "Pension Quantity": "수량 대상 불분명",
 "Siding Login": "결합 불성립", "Thesis Analysis": "분석 대상 불분명",
 "Meeting Coach": "코칭 대상 불분명", "Headline Habit": "결합 불성립",
 "Custody Ledger": "결합 불성립", "Immigration Registry": "결합 불성립",
 "Testament Status": "결합 불성립", "Notary Tab": "결합 불성립",
 "Mediation Fine": "결합 불성립", "Guardianship Extension": "결합 불성립",
 "Trademark Timer": "결합 불성립", "Patent Rating": "평가 대상 불분명",
 "Copyright Payment": "결합 불성립",
 "Neighborhood Workbook": "워크북 대상 불분명", "Litigation Mode": "기능 토글로 읽혀 제품 불분명",
 "Dependent Spec": "결합 불성립", "Cabinetry Quantity": "수량 대상 불분명",
 "Withdrawal Login": "결합 불성립", "Latte Analysis": "분석 대상 불분명",
 "Behavior Coach": "코칭 대상 불분명", "Toothbrush Habit": "결합 불성립",
 "Migraine Advisory": "안내 대상 불분명", "Insomnia Fee": "결합 불성립",
 "Skydiving Cost": "활동 비용 근거 약함(Sledding Cost 기각 선례)",
 "Acne Price": "가격 지칭 부자연", "Snowboarding Sum": "결합 불성립",
 "Eczema Debt": "결합 불성립", "Ziplining Sale": "결합 불성립",
 "Psoriasis Charge": "결합 불성립", "Sledding Tariff": "결합 불성립",
 "Vertigo Value": "결합 불성립", "Diving Fine": "결합 불성립",
 "Arthritis Number": "수치 지칭 부자연", "Sailing Rule": "결합 불성립",
 "Menopause Detail": "결합 불성립", "Rafting Attribute": "결합 불성립",
 "Pregnancy Field": "결합 불성립", "Climbing Token": "결합 불성립",
 "Fertility Signature": "결합 불성립", "Biking Interest": "결합 불성립",
 "Thyroid Asset": "결합 불성립", "Golf Subsidy": "결합 불성립",
 "Cholesterol Discount": "결합 불성립", "Fishing Penalty": "결합 불성립",
 "Hypertension Markup": "결합 불성립", "Camping Trial": "결합 불성립",
 "Anemia Graph": "그래프 대상 불분명", "Glamping Worksheet": "학습지 근거 약함",
 "Heartburn Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Stargazing Sketch": "제품성 불분명", "Constipation Outline": "제품성 불분명",
 "Birdwatching Kit": "키트 대상 불분명", "Concussion Count": "대상 불분명",
 "Canyon Total": "결합 불성립", "Sprain Widget": "위젯 대상 불분명",
 "Geyser Repository": "결합 불성립", "Fracture Announcement": "결합 불성립",
 "Fjord Calculator": "계산 대상 불분명", "Insulin Converter": "변환 대상 불분명",
 "Savanna Generator": "생성 대상 불분명", "Tundra Recorder": "기록 대상 불분명",
 "Prairie Estimator": "산출 대상 불분명", "Marsh Checker": "검사 대상 불분명",
 "Cove Detector": "탐지 대상 불분명", "Cliff Timer": "결합 불성립",
 "Cavern Workshop": "결합 불성립", "Oasis Guardian": "감시 대상 불분명",
 "Dune Helper": "결합 불성립", "Whale Stage": "결합 불성립",
 "Dolphin Result": "결합 불성립", "Penguin Streak": "결합 불성립",
 "Flamingo Rank": "결합 불성립", "Turtle Trend": "결합 불성립",
 "Moose Comparison": "비교 대상 불분명", "Bison Proposal": "제안 대상 불분명",
 "Reindeer Guarantee": "결합 불성립",
 "Appointment Workbook": "워크북 대상 불분명", "Waiver Spec": "결합 불성립",
 "Immunization Quantity": "수량 대상 불분명", "Family Login": "결합 불성립",
 "Chemical Analysis": "분석 대상 불분명",
 "Alteration Workbook": "워크북 대상 불분명", "Memorial Mode": "기능 토글로 읽혀 제품 불분명",
 "Checkout Spec": "결합 불성립", "Recall Quantity": "수량 대상 불분명",
 "Port Login": "결합 불성립", "Logbook Analysis": "분석 대상 불분명",
 "Tailings Coach": "코칭 대상 불분명", "Coil Habit": "결합 불성립",
 "Lawyer Pass": "결합 불성립", "Attorney Link": "결합 불성립",
 "Court Rendering": "렌더링 대상 불분명", "Judge Duration": "결합 불성립",
 "Jury Simulator": "서비스 대상 불분명", "Lawsuit Compatibility": "결합 불성립",
 "Divorce Workbook": "워크북 대상 불분명", "Chassis Mode": "기능 토글로 읽혀 제품 불분명",
 "Amendment Spec": "결합 불성립", "Salvage Quantity": "수량 대상 불분명",
 "Pension Login": "결합 불성립", "Siding Analysis": "분석 대상 불분명",
 "Thesis Coach": "코칭 대상 불분명", "Meeting Habit": "결합 불성립",
 "Custody Board": "결합 불성립", "Immigration Calendar": "일정 대상 불분명(Immigration Scheduler 기각 선례)",
 "Testament View": "결합 불성립", "Notary Bulletin": "결합 불성립",
 "Mediation Number": "수치 지칭 부자연", "Guardianship Trial": "결합 불성립",
 "Trademark Workshop": "결합 불성립", "Copyright Verification": "검증 대상 불분명",
 "Flatbed Workbook": "워크북 대상 불분명", "Neighborhood Mode": "기능 토글로 읽혀 제품 불분명",
 "Litigation Spec": "결합 불성립", "Dependent Quantity": "수량 대상 불분명",
 "Cabinetry Login": "결합 불성립", "Withdrawal Analysis": "분석 대상 불분명",
 "Latte Coach": "코칭 대상 불분명", "Behavior Habit": "결합 불성립",
 "Migraine Petition": "결합 불성립", "Insomnia Item": "항목 대상 불분명",
 "Skydiving Price": "가격 지칭 부자연", "Acne Fare": "결합 불성립",
 "Snowboarding Debt": "결합 불성립", "Eczema Fund": "자금 근거 약함",
 "Ziplining Charge": "결합 불성립", "Psoriasis Duty": "결합 불성립",
 "Sledding Value": "결합 불성립", "Vertigo Stake": "결합 불성립",
 "Diving Number": "수치 지칭 부자연", "Arthritis Version": "결합 불성립",
 "Sailing Detail": "결합 불성립", "Menopause Identifier": "결합 불성립",
 "Rafting Field": "결합 불성립", "Pregnancy Format": "결합 불성립",
 "Climbing Signature": "결합 불성립", "Fertility Marker": "결합 불성립",
 "Biking Asset": "결합 불성립", "Thyroid Levy": "결합 불성립",
 "Golf Discount": "결합 불성립", "Cholesterol Arrears": "결합 불성립",
 "Fishing Markup": "결합 불성립", "Hypertension Redemption": "결합 불성립",
 "Camping Graph": "그래프 대상 불분명", "Anemia Label": "결합 불성립",
 "Glamping Diagram": "교육 다이어그램 축은 동물·지형에서만 확인",
 "Heartburn Schematic": "회로도 어휘 부자연", "Stargazing Outline": "지형은 공예 오트라인 대상 아님",
 "Constipation Rendering": "렌더링 대상 불분명", "Birdwatching Count": "대상 불분명",
 "Concussion Message": "결합 불성립", "Canyon Widget": "위젯 대상 불분명",
 "Sprain Repository": "결합 불성립", "Geyser Announcement": "결합 불성립",
 "Fracture Calculator": "계산 대상 불분명", "Fjord Converter": "변환 대상 불분명",
 "Insulin Generator": "생성 대상 불분명", "Savanna Recorder": "기록 대상 불분명",
 "Tundra Estimator": "산출 대상 불분명", "Prairie Checker": "검사 대상 불분명",
 "Marsh Detector": "탐지 대상 불분명", "Cove Timer": "결합 불성립",
 "Cliff Workshop": "결합 불성립", "Cavern Guardian": "감시 대상 불분명",
 "Oasis Helper": "결합 불성립",
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
out = base + r"\_dec_c15.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
