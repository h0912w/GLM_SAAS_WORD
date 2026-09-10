# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk16_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Reference App": (0.55, "추천인 확인 관리 앱(reference check 실재)"),
 "Agenda Tips": (0.55, "안건·일정 팁(App→Tips 평행)"),
 "Wellness App": (0.6, "시니어 웰니스 관리 앱(실재 카테고리)"),
 "Scheduling Tips": (0.55, "방제 일정 팁(App→Tips 평행)"),
 "Roadtrip App": (0.6, "로드트립 계획 앱(실재 카테고리)"),
 "Accordion Tips": (0.55, "아코디언 연습 팁(App→Tips 평행)"),
 "Vineyard App": (0.6, "와이너리 투어·관리 앱(실재)"),
 "Accompanist Tips": (0.55, "반주 섭외 팁(App→Tips 평행)"),
 "Patent Reply": (0.55, "심사관 의견서 대응 관리(office action 실재)"),
 "Refund App": (0.6, "환불 처리 관리 앱(실재 카테고리)"),
 "Reference Tips": (0.55, "추천인 확인 팁(App→Tips 평행)"),
 "Milestone App": (0.6, "아이 발달 이정표 기록 앱(실재)"),
 "Wellness Tips": (0.55, "웰니스 관리 팁(App→Tips 평행)"),
 "Trap App": (0.55, "배수 트랩 관리 앱(배관 실재)"),
 "Roadtrip Tips": (0.55, "로드트립 팁(App→Tips 평행)"),
 "Curb App": (0.55, "연석 정비 관리 앱(시설 실재)"),
 "Vineyard Tips": (0.55, "와이너리 운영 팁(App→Tips 평행)"),
 "Insomnia Plan": (0.55, "불면증 관리 계획(CBT-I 실재, 건강 관리 플랜 축)"),
}
R_DUP = {
 "Financing Advice": "동일 배치 승인된 Financing App/Tips와 동일 기능 의미 중복",
 "Snow Advice": "동일 배치 승인된 Snow App/Tips와 동일 기능 의미 중복",
 "Allergy Advice": "동일 배치 승인된 Allergy App/Tips와 동일 기능 의미 중복",
 "Illness Advice": "동일 배치 승인된 Illness App/Tips와 동일 기능 의미 중복",
 "Agenda Advice": "동일 배치 승인된 Agenda App/Tips와 동일 기능 의미 중복",
 "Scheduling Advice": "동일 배치 승인된 Scheduling App/Tips와 동일 기능 의미 중복",
 "Accordion Advice": "동일 배치 승인된 Accordion App/Tips와 동일 기능 의미 중복",
 "Accompanist Advice": "동일 배치 승인된 Accompanist App/Tips와 동일 기능 의미 중복",
}
R = {
 "Dune Stage": "결합 불성립", "Whale Result": "결합 불성립",
 "Dolphin Streak": "결합 불성립", "Penguin Rank": "결합 불성립",
 "Flamingo Trend": "결합 불성립", "Turtle Comparison": "비교 대상 불분명",
 "Moose Proposal": "제안 대상 불분명", "Bison Guarantee": "결합 불성립",
 "Reindeer Record": "기록 대상 불분명",
 "Compliance Workbook": "워크북 대상 불분명", "Appointment Mode": "기능 토글로 읽혀 제품 불분명",
 "Waiver Quantity": "수량 대상 불분명", "Immunization Login": "결합 불성립",
 "Family Analysis": "분석 대상 불분명", "Chemical Coach": "코칭 대상 불분명",
 "Inventory Workbook": "워크북 대상 불분명", "Alteration Mode": "기능 토글로 읽혀 제품 불분명",
 "Memorial Spec": "결합 불성립", "Checkout Quantity": "수량 대상 불분명",
 "Recall Login": "결합 불성립", "Port Analysis": "분석 대상 불분명",
 "Logbook Coach": "코칭 대상 불분명", "Tailings Habit": "결합 불성립",
 "Lawyer Voucher": "결합 불성립", "Attorney Rule": "결합 불성립",
 "Court Notification": "결합 불성립", "Judge Volume": "결합 불성립",
 "Jury Predictor": "예측 대상 불분명", "Lawsuit Capacity": "결합 불성립",
 "Compliance Mode": "기능 토글로 읽혀 제품 불분명",
 "Wire Workbook": "워크북 대상 불분명", "Divorce Mode": "기능 토글로 읽혀 제품 불분명",
 "Chassis Spec": "결합 불성립", "Amendment Quantity": "수량 대상 불분명",
 "Salvage Login": "결합 불성립", "Pension Analysis": "분석 대상 불분명",
 "Siding Coach": "코칭 대상 불분명", "Thesis Habit": "결합 불성립",
 "Custody Deck": "결합 불성립", "Immigration Directory": "결합 불성립",
 "Testament History": "이력 대상 불분명(Testament 계열 기각 선례)",
 "Notary Brief": "결합 불성립", "Mediation Version": "결합 불성립",
 "Guardianship Graph": "그래프 대상 불분명", "Trademark Guardian": "감시 대상 불분명",
 "Copyright Simulator": "서비스 대상 불분명",
 "Debtor Workbook": "워크북 대상 불분명", "Flatbed Mode": "기능 토글로 읽혀 제품 불분명",
 "Neighborhood Spec": "결합 불성립", "Litigation Quantity": "수량 대상 불분명",
 "Dependent Login": "결합 불성립", "Cabinetry Analysis": "분석 대상 불분명",
 "Withdrawal Coach": "코칭 대상 불분명", "Latte Habit": "결합 불성립",
 "Migraine Confirmation": "확인 대상 불분명", "Insomnia Unit": "결합 불성립",
 "Skydiving Fare": "결합 불성립", "Acne Tax": "결합 불성립",
 "Snowboarding Fund": "결합 불성립", "Eczema Cash": "결합 불성립",
 "Ziplining Duty": "결합 불성립", "Psoriasis Allowance": "결합 불성립",
 "Sledding Stake": "결합 불성립", "Vertigo Margin": "결합 불성립",
 "Diving Version": "결합 불성립", "Arthritis Link": "결합 불성립",
 "Sailing Identifier": "결합 불성립", "Menopause Category": "결합 불성립",
 "Rafting Format": "결합 불성립", "Pregnancy Serial": "결합 불성립",
 "Climbing Marker": "결합 불성립", "Fertility Balance": "결합 불성립",
 "Biking Levy": "결합 불성립", "Thyroid Due": "결합 불성립",
 "Golf Arrears": "결합 불성립", "Cholesterol Advance": "결합 불성립",
 "Fishing Redemption": "결합 불성립", "Hypertension Extension": "결합 불성립",
 "Camping Label": "결합 불성립", "Anemia Manual": "설명 대상 불분명",
 "Glamping Schematic": "회로도 어휘 부자연", "Heartburn Layout": "결합 불성립",
 "Stargazing Rendering": "렌더링 대상 불분명", "Constipation Notification": "결합 불성립",
 "Birdwatching Message": "결합 불성립", "Concussion Total": "결합 불성립",
 "Canyon Repository": "결합 불성립", "Sprain Announcement": "결합 불성립",
 "Geyser Calculator": "계산 대상 불분명", "Fracture Converter": "변환 대상 불분명",
 "Fjord Generator": "생성 대상 불분명", "Insulin Recorder": "기록 대상 불분명",
 "Savanna Estimator": "산출 대상 불분명", "Tundra Checker": "검사 대상 불분명",
 "Prairie Detector": "탐지 대상 불분명", "Marsh Timer": "결합 불성립",
 "Cove Workshop": "결합 불성립", "Cliff Guardian": "감시 대상 불분명",
 "Cavern Helper": "결합 불성립", "Oasis Stage": "결합 불성립",
 "Dune Result": "결합 불성립", "Whale Streak": "결합 불성립",
 "Dolphin Rank": "결합 불성립", "Penguin Trend": "결합 불성립",
 "Flamingo Comparison": "비교 대상 불분명", "Turtle Proposal": "제안 대상 불분명",
 "Moose Guarantee": "결합 불성립", "Bison Record": "기록 대상 불분명",
 "Reindeer Copy": "결합 불성립",
 "Financing Workbook": "워크북 대상 불분명", "Appointment Spec": "결합 불성립",
 "Waiver Login": "결합 불성립", "Immunization Analysis": "분석 대상 불분명",
 "Family Coach": "코칭 대상 불분명", "Chemical Habit": "결합 불성립",
 "Snow Workbook": "워크북 대상 불분명", "Inventory Mode": "기능 토글로 읽혀 제품 불분명",
 "Alteration Spec": "결합 불성립", "Memorial Quantity": "수량 대상 불분명",
 "Checkout Login": "결합 불성립", "Recall Analysis": "분석 대상 불분명",
 "Port Coach": "코칭 대상 불분명", "Logbook Habit": "결합 불성립",
 "Lawyer Badge": "결합 불성립", "Attorney Detail": "결합 불성립",
 "Court Kit": "키트 대상 불분명", "Judge Diagnostic": "진단 대상 불분명",
 "Jury Seal": "결합 불성립", "Lawsuit Usage": "결합 불성립",
 "Allergy Workbook": "워크북 대상 불분명", "Wire Mode": "기능 토글로 읽혀 제품 불분명",
 "Divorce Spec": "결합 불성립", "Chassis Quantity": "수량 대상 불분명",
 "Amendment Login": "결합 불성립", "Salvage Analysis": "분석 대상 불분명",
 "Pension Coach": "코칭 대상 불분명", "Siding Habit": "결합 불성립",
 "Custody Studio": "결합 불성립", "Immigration Locator": "탐색 대상 불분명",
 "Testament File": "결합 불성립", "Notary Circular": "결합 불성립",
 "Mediation Link": "결합 불성립", "Guardianship Label": "결합 불성립",
 "Trademark Helper": "결합 불성립", "Patent Account": "결합 불성립",
 "Copyright Predictor": "예측 대상 불분명",
 "Illness Workbook": "워크북 대상 불분명", "Debtor Mode": "기능 토글로 읽혀 제품 불분명",
 "Flatbed Spec": "결합 불성립", "Neighborhood Quantity": "수량 대상 불분명",
 "Litigation Login": "결합 불성립", "Dependent Analysis": "분석 대상 불분명",
 "Cabinetry Coach": "코칭 대상 불분명", "Withdrawal Habit": "결합 불성립",
 "Migraine Recap": "결합 불성립",
 "Skydiving Tax": "결합 불성립", "Acne Loan": "결합 불성립",
 "Snowboarding Cash": "결합 불성립", "Eczema Sale": "결합 불성립",
 "Ziplining Allowance": "결합 불성립", "Psoriasis Tariff": "결합 불성립",
 "Sledding Margin": "결합 불성립", "Vertigo Fine": "결합 불성립",
 "Diving Link": "결합 불성립", "Arthritis Rule": "결합 불성립",
 "Sailing Category": "결합 불성립", "Menopause Attribute": "결합 불성립",
 "Rafting Serial": "결합 불성립", "Pregnancy Token": "결합 불성립",
 "Climbing Balance": "결합 불성립", "Fertility Interest": "결합 불성립",
 "Biking Due": "결합 불성립", "Thyroid Subsidy": "결합 불성립",
 "Golf Advance": "결합 불성립",
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
