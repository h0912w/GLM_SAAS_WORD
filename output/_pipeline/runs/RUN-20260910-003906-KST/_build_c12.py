# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk12_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Immunization App": (0.6, "예방접종 기록 관리 앱(실재 카테고리)"),
 "Family Tips": (0.55, "가족 돌봄 팁(App→Tips 평행)"),
 "Recall App": (0.6, "약품 회수(리콜) 관리 앱(실재)"),
 "Port Tips": (0.55, "항만 물류 팁(App→Tips 평행)"),
 "Salvage App": (0.6, "잔존 차량 처리 관리 앱(salvage 실재)"),
 "Pension Tips": (0.55, "연금 관리 팁(App→Tips 평행)"),
 "Dependent App": (0.55, "부양가족 등록 관리 앱(HR 실재)"),
 "Cabinetry Tips": (0.55, "캐비닛 제작 팁(App→Tips 평행)"),
 "Waiver App": (0.6, "면책 동의서 전자 서명 앱(실재 카테고리)"),
 "Immunization Tips": (0.55, "예방접종 안내 팁(App→Tips 평행)"),
 "Checkout App": (0.6, "살롱 결제 관리 앱(실재)"),
 "Recall Tips": (0.55, "회수 관리 팁(App→Tips 평행)"),
 "Amendment App": (0.55, "계약 수정 관리 앱(부동산 실재)"),
 "Salvage Tips": (0.55, "잔존물 처리 팁(App→Tips 평행)"),
 "Litigation App": (0.55, "소송 대응 관리 앱(보험 실재)"),
 "Dependent Tips": (0.55, "부양가족 등록 팁(App→Tips 평행)"),
}
R_DUP = {
 "Chemical Advice": "동일 배치 승인된 Chemical App/Tips와 동일 기능 의미 중복",
 "Logbook Advice": "동일 배치 승인된 Logbook App/Tips와 동일 기능 의미 중복",
 "Siding Advice": "동일 배치 승인된 Siding App/Tips와 동일 기능 의미 중복",
 "Family Advice": "동일 배치 승인된 Family App/Tips와 동일 기능 의미 중복",
 "Port Advice": "동일 배치 승인된 Port App/Tips와 동일 기능 의미 중복",
 "Pension Advice": "동일 배치 승인된 Pension App/Tips와 동일 기능 의미 중복",
 "Cabinetry Advice": "동일 배치 승인된 Cabinetry App/Tips와 동일 기능 의미 중복",
}
R = {
 "Savanna Total": "결합 불성립", "Tundra Widget": "위젯 대상 불분명",
 "Prairie Repository": "결합 불성립", "Marsh Announcement": "결합 불성립",
 "Cove Calculator": "계산 대상 불분명", "Cliff Converter": "변환 대상 불분명",
 "Cavern Generator": "생성 대상 불분명", "Oasis Recorder": "기록 대상 불분명",
 "Dune Estimator": "산출 대상 불분명", "Whale Checker": "검사 대상 불분명",
 "Dolphin Detector": "탐지 대상 불분명", "Penguin Timer": "결합 불성립",
 "Flamingo Workshop": "결합 불성립", "Turtle Guardian": "감시 대상 불분명",
 "Moose Helper": "결합 불성립", "Bison Stage": "결합 불성립",
 "Reindeer Result": "결합 불성립",
 "Maintenance Workbook": "워크북 대상 불분명", "Inspection Mode": "기능 토글로 읽혀 제품 불분명",
 "Pricing Spec": "결합 불성립", "Cemetery Quantity": "수량 대상 불분명",
 "Commission Login": "결합 불성립", "Dispensing Analysis": "분석 대상 불분명",
 "Charter Coach": "코칭 대상 불분명", "Fuel Habit": "결합 불성립",
 "Tailings Workbook": "워크북 대상 불분명", "Coil Mode": "기능 토글로 읽혀 제품 불분명",
 "Keypad Spec": "결합 불성립", "Bilingual Quantity": "수량 대상 불분명",
 "Mileage Login": "결합 불성립", "Editing Analysis": "분석 대상 불분명",
 "Toast Coach": "코칭 대상 불분명", "Deposit Habit": "결합 불성립",
 "Lawyer Code": "결합 불성립", "Attorney Value": "결합 불성립",
 "Court Worksheet": "학습지 근거 약함", "Judge Record": "판사 대상 기록 불성립",
 "Jury Certification": "결합 불성립", "Lawsuit Pressure": "결합 불성립",
 "Divorce Retreat": "결합 불성립",
 "Thesis Workbook": "워크북 대상 불분명", "Meeting Mode": "기능 토글로 읽혀 제품 불분명",
 "Headline Spec": "결합 불성립", "Priority Quantity": "수량 대상 불분명",
 "Headhunter Login": "결합 불성립", "Swag Analysis": "분석 대상 불분명",
 "Screening Coach": "코칭 대상 불분명(Screening 계열)", "Diner Habit": "결합 불성립",
 "Custody Point": "결합 불성립", "Immigration Companion": "동반 대상 불분명",
 "Testament Check": "검사 대상 불분명", "Notary Badge": "결합 불성립",
 "Mediation Allowance": "결합 불성립", "Guardianship Arrears": "결합 불성립",
 "Trademark Generator": "생성 대상 불분명", "Patent Diagnostic": "진단 대상 불분명",
 "Copyright Deposit": "결합 불성립", "Withdrawal Advice": "철회 대상 불분명",
 "Latte Workbook": "워크북 대상 불분명", "Behavior Mode": "기능 토글로 읽혀 제품 불분명",
 "Toothbrush Spec": "결합 불성립", "Nanny Quantity": "수량 대상 불분명",
 "Sidewalk Login": "결합 불성립", "Snorkeling Analysis": "분석 대상 불분명",
 "Metronome Coach": "코칭 대상 불분명", "Workout Habit": "결합 불성립",
 "Migraine Quota": "결합 불성립", "Insomnia Advisory": "안내 대상 불분명",
 "Skydiving Entry": "등록 대상 불분명", "Acne Fee": "결합 불성립",
 "Snowboarding Cost": "활동 비용 근거 약함(Sledding Cost 기각 선례)",
 "Eczema Price": "가격 지칭 부자연", "Ziplining Loan": "결합 불성립",
 "Psoriasis Sum": "결합 불성립", "Sledding Cash": "결합 불성립",
 "Vertigo Sale": "결합 불성립", "Diving Allowance": "결합 불성립",
 "Arthritis Tariff": "결합 불성립", "Sailing Margin": "결합 불성립",
 "Menopause Fine": "결합 불성립", "Rafting Link": "결합 불성립",
 "Pregnancy Rule": "결합 불성립", "Climbing Category": "결합 불성립",
 "Fertility Attribute": "결합 불성립", "Biking Serial": "결합 불성립",
 "Thyroid Token": "결합 불성립", "Golf Balance": "결합 불성립",
 "Cholesterol Interest": "결합 불성립", "Fishing Due": "결합 불성립",
 "Hypertension Subsidy": "결합 불성립", "Camping Advance": "결합 불성립",
 "Anemia Penalty": "결합 불성립", "Glamping Extension": "결합 불성립",
 "Heartburn Trial": "결합 불성립", "Stargazing Manual": "설명 대상 불분명",
 "Constipation Worksheet": "학습지 근거 약함", "Birdwatching Layout": "결합 불성립",
 "Concussion Sketch": "제품성 불분명", "Canyon Rendering": "렌더링 대상 불분명",
 "Sprain Notification": "결합 불성립", "Geyser Kit": "키트 대상 불분명",
 "Fracture Count": "대상 불분명", "Fjord Message": "결합 불성립",
 "Insulin Total": "결합 불성립",
 "Savanna Widget": "위젯 대상 불분명", "Tundra Repository": "결합 불성립",
 "Prairie Announcement": "결합 불성립", "Marsh Calculator": "계산 대상 불분명",
 "Cove Converter": "변환 대상 불분명", "Cliff Generator": "생성 대상 불분명",
 "Cavern Recorder": "기록 대상 불분명", "Oasis Estimator": "산출 대상 불분명",
 "Dune Checker": "검사 대상 불분명", "Whale Detector": "탐지 대상 불분명",
 "Dolphin Timer": "결합 불성립", "Penguin Workshop": "결합 불성립",
 "Flamingo Guardian": "감시 대상 불분명", "Turtle Helper": "결합 불성립",
 "Moose Stage": "결합 불성립", "Bison Result": "결합 불성립",
 "Reindeer Streak": "결합 불성립",
 "Chemical Workbook": "워크북 대상 불분명", "Maintenance Mode": "기능 토글로 읽혀 제품 불분명",
 "Inspection Spec": "결합 불성립", "Pricing Quantity": "수량 대상 불분명",
 "Cemetery Login": "결합 불성립", "Commission Analysis": "분석 대상 불분명",
 "Dispensing Coach": "코칭 대상 불분명", "Charter Habit": "결합 불성립",
 "Logbook Workbook": "워크북 대상 불분명", "Tailings Mode": "기능 토글로 읽혀 제품 불분명",
 "Coil Spec": "결합 불성립", "Keypad Quantity": "수량 대상 불분명",
 "Bilingual Login": "결합 불성립", "Mileage Analysis": "분석 대상 불분명",
 "Editing Coach": "코칭 대상 불분명", "Toast Habit": "결합 불성립",
 "Lawyer List": "목록 대상 불분명(List 축 기각)", "Attorney Stake": "결합 불성립",
 "Court Diagram": "교육 다이어그램 축 대상 아님", "Judge Copy": "결합 불성립",
 "Jury Nomination": "결합 불성립", "Lawsuit Load": "결합 불성립",
 "Divorce Tournament": "결합 불성립",
 "Siding Workbook": "워크북 대상 불분명", "Thesis Mode": "기능 토글로 읽혀 제품 불분명",
 "Meeting Spec": "결합 불성립", "Headline Quantity": "수량 대상 불분명",
 "Priority Login": "결합 불성립", "Headhunter Analysis": "분석 대상 불분명",
 "Swag Coach": "코칭 대상 불분명", "Screening Habit": "결합 불성립(Screening 계열)",
 "Custody Map": "지도 대상 불분명", "Immigration Register": "결합 불성립",
 "Testament Score": "결합 불성립", "Notary Stub": "결합 불성립",
 "Mediation Tariff": "결합 불성립", "Guardianship Advance": "결합 불성립",
 "Trademark Recorder": "기록 대상 불분명", "Patent Progress": "결합 불성립",
 "Copyright Certification": "결합 불성립",
 "Withdrawal Workbook": "워크북 대상 불분명", "Latte Mode": "기능 토글로 읽혀 제품 불분명",
 "Behavior Spec": "결합 불성립", "Toothbrush Quantity": "수량 대상 불분명",
 "Nanny Login": "결합 불성립", "Sidewalk Analysis": "분석 대상 불분명",
 "Snorkeling Coach": "코칭 대상 불분명", "Metronome Habit": "결합 불성립",
 "Migraine Tab": "결합 불성립", "Insomnia Petition": "결합 불성립",
 "Skydiving Fee": "결합 불성립", "Acne Item": "항목 대상 불분명",
 "Snowboarding Price": "가격 지칭 부자연", "Eczema Fare": "결합 불성립",
 "Ziplining Sum": "결합 불성립", "Psoriasis Debt": "결합 불성립",
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
out = base + r"\_dec_c12.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
