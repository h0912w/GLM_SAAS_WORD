# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk36_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Hypertension Trend": (0.55, "혈압 추이 기록(Anemia Trend 평행)"),
 "Anemia Record": (0.55, "혈색소 검사 기록(Constipation Record 평행)"),
 "Concussion Guide": (0.55, "뇌진탕 복귀 가이드(CDC 지침 실재)"),
 "Compressor Tips": (0.55, "압축기 관리 팁(App→Tips 평행)"),
 "Algae Analysis": (0.55, "수조 이끼·수질 분석(실재)"),
 "Technician App": (0.6, "기사 배치·작업 관리 앱(실재 시장)"),
 "Sightseeing Workbook": (0.55, "도시 탐방 워크북(실재 서식)"),
 "Backorder Analysis": (0.6, "재고 부족 분석(공급망 실재)"),
 "Attorney Kit": (0.55, "법률 서류 키트(실재)"),
 "Softener Tips": (0.55, "연수기 관리 팁(App→Tips 평행)"),
 "Mandolin Workbook": (0.55, "만돌린 교본 워크북(메서드북 실재)"),
 "Contingency Analysis": (0.55, "계약 조건부 현황 분석(Analysis 평행)"),
 "Immigration Update": (0.55, "이민 정책·사건 업데이트(실재)"),
 "Patent Claim": (0.6, "특허 청구항 관리(실무 실재)"),
 "Deck App": (0.6, "데크 시공 설계·견적 앱(실재)"),
 "Rubric Tips": (0.55, "루브릭 작성 팁(App→Tips 평행)"),
 "Story Workbook": (0.55, "스토리 기획 워크북(작법 서식 실재)"),
 "Psoriasis Manual": (0.55, "건선 자가관리 매뉴얼(Arthritis Manual 평행)"),
 "Pregnancy Calculator": (0.7, "출산 예정일 계산기(실검색 실재)"),
 "Climbing Recorder": (0.55, "등반 기록(클라이밍 로그북 실재)"),
 "Birdwatching Guide": (0.55, "조류 관찰 가이드(필드 가이드 실재)"),
 "Eviction Analysis": (0.6, "퇴거 위험 분석(프롭테크 실재)"),
 "Occupant App": (0.6, "입주자(점유자) 포털 앱(실재)"),
 "Technician Tips": (0.55, "기사 업무 팁(App→Tips 평행)"),
 "Traveler Workbook": (0.55, "여행 계획 워크북(Trip Workbook 평행)"),
 "Trailer Analysis": (0.55, "트레일러 운영 데이터 분석(Analysis 평행)"),
 "Custody Counter": (0.55, "양육 일수 카운터(공동양육 앱 실재)"),
 "Guardianship Record": (0.55, "후견 재산 보고 기록(연간 보고 의무 실재)"),
 "Probation App": (0.65, "직원 수습 기간 관리 앱(HR 실재)"),
 "Deck Tips": (0.55, "데크 시공 팁(App→Tips 평행)"),
 "Donut Analysis": (0.55, "도넛 매장 매출 분석(Cafe Analysis 평행)"),
}
R_DUP = {
 "Traveler Advice": "동일 배치 승인된 Traveler App/Tips와 동일 기능 의미 중복",
 "Referendum Advice": "동일 배치 승인된 Referendum App/Tips와 동일 기능 의미 중복",
 "Compressor Advice": "동일 배치 승인된 Compressor App/Tips와 동일 기능 의미 중복",
 "Softener Advice": "동일 배치 승인된 Softener App/Tips와 동일 기능 의미 중복",
 "Rubric Advice": "동일 배치 승인된 Rubric App/Tips와 동일 기능 의미 중복",
}
R = {
 "Hypertension Trend SKIP": "", "Camping Guarantee": "결합 불성립",
 "Anemia Record SKIP": "", "Glamping Reference": "결합 불성립",
 "Heartburn Forecast": "결합 불성립", "Stargazing Volume": "결합 불성립",
 "Constipation Diagnostic": "진단 대상 불분명", "Birdwatching Template": "결합 불성립",
 "Concussion Guide SKIP": "", "Canyon Agreement": "결합 불성립",
 "Sprain Reply": "결합 불성립", "Geyser Account": "결합 불성립",
 "Fracture Case": "결합 불성립", "Fjord Match": "결합 불성립",
 "Insulin Validation": "결합 불성립", "Savanna Lookup": "탐색 대상 불분명",
 "Tundra Ping": "결합 불성립", "Prairie Model": "결합 불성립",
 "Marsh Availability": "상태 명사로 제품명 부자연", "Cove Eligibility": "결합 불성립",
 "Cliff Broadcast": "결합 불성립", "Cavern Barcode": "결합 불성립",
 "Oasis Appointment": "약속 대상 불분명", "Dune Feedback": "결합 불성립",
 "Whale Invoice": "결합 불성립", "Dolphin Renewal": "갱신 대상 불분명",
 "Penguin Quote": "인용·견적 중의로 대상 불분명", "Flamingo Warranty": "결합 불성립",
 "Turtle Deposit": "결합 불성립", "Moose Certification": "결합 불성립",
 "Bison Nomination": "결합 불성립", "Reindeer Correction": "결합 불성립",
 "Compressor Tips SKIP": "", "Cylinder Advice": "팁 대상 불분명",
 "Proofing Workbook": "워크북 대상 불분명", "Unpacking Mode": "기능 토글로 읽혀 제품 불분명",
 "Proof Spec": "사양 참조로 제품 불분명", "Invitation Quantity": "수량 대상 불분명",
 "Eviction Login": "제품 불분명", "Algae Analysis SKIP": "",
 "Upholstery Coach": "코칭 대상 불분명", "Sink Habit": "결합 불성립",
 "Technician App SKIP": "", "Rinse Tips": "팁 대상 불분명",
 "Plunger Advice": "팁 대상 불분명", "Sightseeing Workbook SKIP": "",
 "Clarinet Mode": "기능 토글로 읽혀 제품 불분명", "Consent Spec": "사양 참조로 제품 불분명",
 "Escrow Quantity": "수량 대상 불분명", "Statute Login": "제품 불분명",
 "Backorder Analysis SKIP": "", "Binder Habit": "결합 불성립",
 "Lawyer Fine": "결합 불성립", "Attorney Kit SKIP": "",
 "Court Progress": "진행 대상 불분명", "Judge Review": "용어 부정확로 대상 불분명(judicial review)",
 "Jury Condition": "결합 불성립", "Bucket App": "제품 불분명",
 "Softener Tips SKIP": "", "Traveler Advice DUP": "",
 "Mandolin Workbook SKIP": "", "Vaccine Mode": "기능 토글로 읽혀 제품 불분명",
 "Remittance Spec": "사양 참조로 제품 불분명", "Lawsuit Quantity": "수량 대상 불분명",
 "Trailer Login": "제품 불분명", "Contingency Analysis SKIP": "",
 "Indemnity Coach": "코칭 대상 불분명", "Severance Habit": "결합 불성립",
 "Divorce Station": "결합 불성립", "Custody Office": "결합 불성립",
 "Immigration Update SKIP": "", "Testament Recap": "결합 불성립",
 "Notary Attribute": "결합 불성립", "Mediation Rendering": "결합 불성립",
 "Guardianship Guarantee": "결합 불성립", "Trademark Barcode": "결합 불성립",
 "Patent Claim SKIP": "", "Copyright Usage": "대상 불분명",
 "Deck App SKIP": "", "Rubric Tips SKIP": "",
 "Story Workbook SKIP": "", "Internship Mode": "기능 토글로 읽혀 제품 불분명",
 "Attendance Spec": "사양 참조로 제품 불분명", "Transmission Quantity": "수량 대상 불분명",
 "Donut Login": "제품 불분명", "Euthanasia Analysis": "분석 대상 불분명",
 "Implant Coach": "코칭 대상 불분명", "Lullaby Habit": "결합 불성립",
 "Migraine Token": "결합 불성립", "Insomnia Asset": "결합 불성립",
 "Skydiving Discount": "판촉 계열 기각 선례", "Acne Arrears": "결합 불성립",
 "Snowboarding Redemption": "결합 불성립", "Eczema Extension": "연장 대상 불분명",
 "Ziplining Label": "결합 불성립", "Psoriasis Manual SKIP": "",
 "Sledding Schematic": "도식 대상 불분명", "Vertigo Layout": "결합 불성립",
 "Diving Rendering": "결합 불성립", "Arthritis Notification": "알림 내용 불특정",
 "Sailing Message": "결합 불성립", "Menopause Total": "결합 불성립",
 "Rafting Announcement": "결합 불성립", "Pregnancy Calculator SKIP": "",
 "Climbing Recorder SKIP": "", "Fertility Estimator": "Fertility Calculator와 기능 중복 우려",
 "Biking Timer": "결합 불성립", "Thyroid Workshop": "결합 불성립(Camping Workshop 기각 선례)",
 "Golf Stage": "단계 대상 불분명", "Cholesterol Result": "결합 불성립",
 "Fishing Trend": "결합 불성립", "Hypertension Comparison": "비교 대상 불분명",
 "Camping Record": "기록 대상 불분명(Glamping Record 기각 선례)", "Anemia Copy": "결합 불성립",
 "Glamping Forecast": "결합 불성립", "Heartburn Deadline": "결합 불성립",
 "Stargazing Diagnostic": "진단 대상 불분명", "Constipation Progress": "진행 대상 불분명(Fracture Progress 기각 선례)",
 "Birdwatching Guide SKIP": "", "Concussion Rating": "평가 대상 불분명",
 "Canyon Reply": "결합 불성립", "Sprain Account": "결합 불성립",
 "Geyser Case": "결합 불성립", "Fracture Match": "결합 불성립",
 "Fjord Validation": "결합 불성립", "Insulin Lookup": "탐색 대상 불분명",
 "Savanna Ping": "결합 불성립", "Tundra Model": "결합 불성립",
 "Prairie Availability": "상태 명사로 제품명 부자연", "Marsh Eligibility": "결합 불성립",
 "Cove Broadcast": "결합 불성립", "Cliff Barcode": "결합 불성립",
 "Cavern Appointment": "약속 대상 불분명", "Oasis Feedback": "결합 불성립",
 "Dune Invoice": "결합 불성립", "Whale Renewal": "갱신 대상 불분명",
 "Dolphin Quote": "인용·견적 중의로 대상 불분명", "Penguin Warranty": "결합 불성립",
 "Flamingo Deposit": "결합 불성립", "Turtle Certification": "결합 불성립",
 "Moose Nomination": "결합 불성립", "Bison Correction": "결합 불성립",
 "Reindeer Revision": "결합 불성립", "Cylinder Workbook": "워크북 대상 불분명",
 "Proofing Mode": "기능 토글로 읽혀 제품 불분명", "Unpacking Spec": "사양 참조로 제품 불분명",
 "Proof Quantity": "수량 대상 불분명", "Invitation Login": "제품 불분명",
 "Eviction Analysis SKIP": "", "Algae Coach": "코칭 대상 불분명",
 "Upholstery Habit": "결합 불성립", "Occupant App SKIP": "",
 "Technician Tips SKIP": "", "Rinse Advice": "팁 대상 불분명",
 "Plunger Workbook": "워크북 대상 불분명", "Sightseeing Mode": "기능 토글로 읽혀 제품 불분명",
 "Clarinet Spec": "사양 참조로 제품 불분명", "Consent Quantity": "수량 대상 불분명",
 "Escrow Login": "제품 불분명", "Statute Analysis": "분석 대상 불분명",
 "Backorder Coach": "코칭 대상 불분명", "Lawyer Number": "결합 불성립",
 "Attorney Count": "카운트 대상 불분명", "Court Authorization": "결합 불성립",
 "Judge Recipe": "결합 불성립", "Jury Humidity": "결합 불성립",
 "Opening App": "제품 불분명(시즌 오픈 서비스로 읽기 어려움)", "Bucket Tips": "팁 대상 불분명",
 "Traveler Workbook SKIP": "", "Mandolin Mode": "기능 토글로 읽혀 제품 불분명",
 "Vaccine Spec": "사양 참조로 제품 불분명", "Remittance Quantity": "수량 대상 불분명",
 "Lawsuit Login": "제품 불분명", "Trailer Analysis SKIP": "",
 "Contingency Coach": "코칭 대상 불분명", "Indemnity Habit": "결합 불성립",
 "Divorce Terminal": "결합 불성립", "Custody Counter SKIP": "",
 "Immigration Feed": "결합 불성립", "Testament Entry": "결합 불성립",
 "Notary Field": "결합 불성립", "Mediation Notification": "알림 대상 불특정",
 "Guardianship Record SKIP": "", "Trademark Appointment": "약속 대상 불분명",
 "Patent Onboarding": "결합 불성립", "Copyright Condition": "결합 불성립",
 "Probation App SKIP": "", "Deck Tips SKIP": "",
 "Referendum Workbook": "워크북 대상 불분명", "Story Mode": "기능 토글로 읽혀 제품 불분명",
 "Internship Spec": "사양 참조로 제품 불분명", "Attendance Quantity": "수량 대상 불분명",
 "Transmission Login": "제품 불분명", "Donut Analysis SKIP": "",
 "Euthanasia Coach": "코칭 대상 불분명", "Implant Habit": "결합 불성립",
}
for k in [k for k in R if k.endswith(" SKIP") or k.endswith(" DUP")]:
    del R[k]
R["Traveler Advice"] = ""
del R["Traveler Advice"]
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
out = base + r"\_dec_c36.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
