# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk33_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Mediation Worksheet": (0.55, "조정 준비 워크시트(실무 서식 실재)"),
 "Trademark Lookup": (0.6, "상표 데이터베이스 조회(실검색 실재)"),
 "Transmission App": (0.55, "변속기 수리 예약·관리 앱(실재)"),
 "Donut Tips": (0.55, "도넛 제조 팁(App→Tips 평행)"),
 "Ensemble Coach": (0.55, "합주 코칭(실재)"),
 "Diving Worksheet": (0.55, "다이빙 로그 워크시트(실재 서식)"),
 "Rafting Kit": (0.55, "래프팅 장비 키트(Climbing Kit 평행)"),
 "Hypertension Helper": (0.55, "혈압 관리 도우미(Glamping Helper 평행)"),
 "Fracture Guide": (0.55, "골절 회복 가이드(콘텐츠 실재)"),
 "Proof App": (0.65, "사진 교정쇄(proofing) 갤러리 앱(실재 시장)"),
 "Invitation Tips": (0.55, "초대장 작성 팁(App→Tips 평행)"),
 "Consent App": (0.65, "동의서 관리 앱(의료·개인정보 실재)"),
 "Escrow Tips": (0.55, "에스크로 이용 팁(App→Tips 평행)"),
 "Bundle Analysis": (0.6, "번들 상품 성과 분석(이커머스 실재)"),
 "Remittance App": (0.7, "해외 송금 앱(실재 시장)"),
 "Lawsuit Tips": (0.55, "소송 준비 팁(App→Tips 평행)"),
 "Budget Analysis": (0.65, "예산 분석(실재)"),
 "Divorce Ledger": (0.55, "이혼 재산 분할 장부(실재)"),
 "Patent Diary": (0.55, "발명 일지(발명자 노트 관행 실재)"),
 "Attendance App": (0.7, "출석 관리 앱(실재 시장)"),
 "Transmission Tips": (0.55, "변속기 관리 팁(App→Tips 평행)"),
 "Diving Diagram": (0.55, "다이빙 프로파일 도식(다이빙 테이블 실재)"),
 "Anemia Trend": (0.55, "혈색소 추이 기록(검사 추적 실재)"),
 "Heartburn Record": (0.55, "역류 증상 기록(Constipation Record 평행)"),
 "Geyser Guide": (0.55, "간헐천 관람 가이드(실재)"),
 "Unpacking App": (0.55, "이사 후 언패킹 체크리스트 앱(실재)"),
 "Proof Tips": (0.55, "사진 교정쇄 운영 팁(App→Tips 평행)"),
 "Vocal Analysis": (0.6, "발성·음정 분석(실재 카테고리)"),
 "Clarinet App": (0.65, "클라리넷 운지·연습 앱(실재 카테고리)"),
 "Consent Tips": (0.55, "동의서 작성 팁(App→Tips 평행)"),
}
R_DUP = {
 "Euthanasia Advice": "동일 배치 승인된 Euthanasia App/Tips와 동일 기능 의미 중복",
 "Eviction Advice": "동일 배치 승인된 Eviction App/Tips와 동일 기능 의미 중복",
 "Statute Advice": "동일 배치 승인된 Statute App/Tips와 동일 기능 의미 중복",
 "Trailer Advice": "동일 배치 승인된 Trailer App/Tips와 동일 기능 의미 중복",
 "Donut Advice": "동일 배치 승인된 Donut App/Tips와 동일 기능 의미 중복",
 "Invitation Advice": "동일 배치 승인된 Invitation App/Tips와 동일 기능 의미 중복",
 "Escrow Advice": "동일 배치 승인된 Escrow App/Tips와 동일 기능 의미 중복",
}
R = {
 "Notary Version": "결합 불성립", "Mediation Worksheet SKIP": "",
 "Guardianship Result": "결합 불성립", "Trademark Lookup SKIP": "",
 "Patent Video": "결합 불성립", "Copyright Voltage": "결합 불성립",
 "Transmission App SKIP": "", "Donut Tips SKIP": "",
 "Implant Workbook": "워크북 대상 불분명", "Lullaby Mode": "기능 토글로 읽혀 제품 불분명",
 "Style Spec": "사양 참조로 제품 불분명", "Substitution Quantity": "수량 대상 불분명",
 "Playground Login": "제품 불분명", "Casino Analysis": "분석 대상 불분명",
 "Ensemble Coach SKIP": "", "Injury Habit": "결합 불성립",
 "Migraine Identifier": "결합 불성립", "Insomnia Serial": "결합 불성립",
 "Skydiving Balance": "결합 불성립", "Acne Interest": "결합 불성립",
 "Snowboarding Subsidy": "결합 불성립", "Eczema Discount": "판촉 계열 기각 선례",
 "Ziplining Penalty": "결합 불성립", "Psoriasis Markup": "마크업 대상 불분명",
 "Sledding Trial": "결합 불성립", "Vertigo Graph": "그래프 대상 불분명",
 "Diving Worksheet SKIP": "", "Arthritis Diagram": "도식 대상 불분명",
 "Sailing Sketch": "제품성 불분명(Rafting Sketch 기각 선례)",
 "Menopause Outline": "개요 대상 불분명", "Rafting Kit SKIP": "",
 "Pregnancy Count": "카운트 대상 불분명(Fertility Count 기각 선례)",
 "Climbing Widget": "결합 불성립", "Fertility Repository": "결합 불성립",
 "Biking Converter": "변환 대상 불분명", "Thyroid Generator": "생성 대상 불분명",
 "Golf Checker": "검사 대상 불분명", "Cholesterol Detector": "탐지 대상 불분명",
 "Fishing Guardian": "감시 대상 불분명", "Hypertension Helper SKIP": "",
 "Camping Streak": "결합 불성립", "Anemia Rank": "결합 불성립",
 "Glamping Proposal": "제안 대상 불분명", "Heartburn Guarantee": "결합 불성립",
 "Stargazing Reading": "수치 대상 불분명", "Constipation Reference": "결합 불성립",
 "Birdwatching Duration": "결합 불성립", "Concussion Volume": "결합 불성립",
 "Canyon Progress": "결합 불성립", "Sprain Authorization": "결합 불성립",
 "Geyser Template": "결합 불성립", "Fracture Guide SKIP": "",
 "Fjord Rating": "평가 대상 불분명", "Insulin Agreement": "결합 불성립",
 "Savanna Reply": "결합 불성립", "Tundra Account": "결합 불성립",
 "Prairie Case": "결합 불성립", "Marsh Match": "결합 불성립",
 "Cove Validation": "결합 불성립", "Cliff Lookup": "탐색 대상 불분명",
 "Cavern Ping": "결합 불성립", "Oasis Model": "결합 불성립",
 "Dune Availability": "상태 명사로 제품명 부자연", "Whale Eligibility": "결합 불성립",
 "Dolphin Broadcast": "결합 불성립", "Penguin Barcode": "결합 불성립",
 "Flamingo Appointment": "약속 대상 불분명", "Turtle Feedback": "결합 불성립",
 "Moose Invoice": "결합 불성립", "Bison Renewal": "갱신 대상 불분명",
 "Reindeer Quote": "인용·견적 중의로 대상 불분명", "Proof App SKIP": "",
 "Invitation Tips SKIP": "", "Algae Workbook": "워크북 대상 불분명",
 "Upholstery Mode": "기능 토글로 읽혀 제품 불분명", "Sink Spec": "사양 참조로 제품 불분명",
 "Trip Quantity": "수량 대상 불분명", "Vocal Login": "제품 불분명",
 "Payment Coach": "코칭 대상 불분명", "Redline Habit": "결합 불성립",
 "Consent App SKIP": "", "Escrow Tips SKIP": "",
 "Backorder Workbook": "워크북 대상 불분명", "Binder Spec": "사양 참조로 제품 불분명",
 "Review Quantity": "수량 대상 불분명", "Lien Login": "제품 불분명",
 "Bundle Analysis SKIP": "", "Alumni Habit": "결합 불성립",
 "Lawyer Allowance": "결합 불성립", "Attorney Layout": "결합 불성립",
 "Court Forecast": "결합 불성립", "Judge Payment": "결합 불성립",
 "Jury Brightness": "결합 불성립", "Remittance App SKIP": "",
 "Lawsuit Tips SKIP": "", "Contingency Workbook": "워크북 대상 불분명",
 "Indemnity Mode": "기능 토글로 읽혀 제품 불분명", "Severance Spec": "사양 참조로 제품 불분명",
 "Painting Quantity": "수량 대상 불분명", "Prerequisite Login": "제품 불분명",
 "Budget Analysis SKIP": "", "Caption Coach": "코칭 대상 불분명",
 "Sentiment Habit": "결합 불성립", "Divorce Ledger SKIP": "",
 "Custody Registry": "공적 등록부로 읽혀 제품 불분명", "Immigration View": "결합 불성립",
 "Testament Brief": "결합 불성립", "Notary Link": "결합 불성립",
 "Mediation Diagram": "도식 대상 불분명", "Guardianship Streak": "결합 불성립",
 "Trademark Ping": "결합 불성립", "Patent Diary SKIP": "",
 "Copyright Wattage": "결합 불성립", "Attendance App SKIP": "",
 "Transmission Tips SKIP": "", "Euthanasia Workbook": "워크북 대상 불분명",
 "Implant Mode": "기능 토글로 읽혀 제품 불분명", "Lullaby Spec": "사양 참조로 제품 불분명",
 "Style Quantity": "수량 대상 불분명", "Substitution Login": "제품 불분명",
 "Playground Analysis": "분석 대상 불분명", "Casino Coach": "코칭 대상 불분명",
 "Ensemble Habit": "결합 불성립", "Migraine Category": "결합 불성립",
 "Insomnia Token": "결합 불성립", "Skydiving Interest": "결합 불성립",
 "Acne Asset": "결합 불성립", "Snowboarding Discount": "판촉 계열 기각 선례",
 "Eczema Arrears": "결합 불성립", "Ziplining Markup": "마크업 대상 불분명",
 "Psoriasis Redemption": "결합 불성립", "Sledding Graph": "그래프 대상 불분명",
 "Vertigo Label": "결합 불성립", "Diving Diagram SKIP": "",
 "Arthritis Schematic": "도식 대상 불분명(Arthritis Diagram 기각 선례)",
 "Sailing Outline": "개요 대상 불분명", "Menopause Rendering": "결합 불성립",
 "Rafting Count": "카운트 대상 불분명", "Pregnancy Message": "메시지 대상 불분명",
 "Climbing Repository": "결합 불성립", "Fertility Announcement": "결합 불성립",
 "Biking Generator": "생성 대상 불분명", "Thyroid Recorder": "기록 대상 불분명(자가 측정 불가)",
 "Golf Detector": "탐지 대상 불분명", "Cholesterol Timer": "결합 불성립",
 "Fishing Helper": "도움 대상 불분명", "Hypertension Stage": "단계 대상 불분명",
 "Camping Rank": "결합 불성립", "Anemia Trend SKIP": "",
 "Glamping Guarantee": "결합 불성립", "Heartburn Record SKIP": "",
 "Stargazing Reference": "결합 불성립", "Constipation Forecast": "결합 불성립",
 "Birdwatching Volume": "결합 불성립", "Concussion Diagnostic": "진단 대상 불분명",
 "Canyon Authorization": "결합 불성립", "Sprain Template": "결합 불성립",
 "Geyser Guide SKIP": "", "Fracture Rating": "평가 대상 불분명",
 "Fjord Agreement": "결합 불성립", "Insulin Reply": "결합 불성립",
 "Savanna Account": "결합 불성립", "Tundra Case": "결합 불성립",
 "Prairie Match": "결합 불성립", "Marsh Validation": "결합 불성립",
 "Cove Lookup": "탐색 대상 불분명", "Cliff Ping": "결합 불성립",
 "Cavern Model": "결합 불성립", "Oasis Availability": "상태 명사로 제품명 부자연",
 "Dune Eligibility": "결합 불성립", "Whale Broadcast": "결합 불성립",
 "Dolphin Barcode": "결합 불성립", "Penguin Appointment": "약속 대상 불분명",
 "Flamingo Feedback": "결합 불성립", "Turtle Invoice": "결합 불성립",
 "Moose Renewal": "갱신 대상 불분명", "Bison Quote": "인용·견적 중의로 대상 불분명",
 "Reindeer Warranty": "결합 불성립", "Unpacking App SKIP": "",
 "Proof Tips SKIP": "", "Eviction Workbook": "워크북 대상 불분명",
 "Algae Mode": "기능 토글로 읽혀 제품 불분명", "Upholstery Spec": "사양 참조로 제품 불분명",
 "Sink Quantity": "수량 대상 불분명", "Trip Login": "제품 불분명",
 "Vocal Analysis SKIP": "", "Payment Habit": "결합 불성립",
 "Clarinet App SKIP": "", "Consent Tips SKIP": "",
 "Statute Workbook": "워크북 대상 불분명", "Backorder Mode": "기능 토글로 읽혀 제품 불분명",
 "Binder Quantity": "수량 대상 불분명", "Review Login": "제품 불분명",
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
out = base + r"\_dec_c33.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
