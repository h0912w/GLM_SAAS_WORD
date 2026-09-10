# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk35_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Proofing Tips": (0.55, "번역 교정 팁(App→Tips 평행)"),
 "Trip Coach": (0.55, "여행 계획 코칭(실재)"),
 "Sightseeing Tips": (0.55, "관광 팁(App→Tips 평행)"),
 "Review Coach": (0.55, "성과 평가 작성 코칭(실재)"),
 "Traveler App": (0.6, "여행자 프로필·계획 앱(실재)"),
 "Mandolin Tips": (0.55, "만돌린 연습 팁(App→Tips 평행)"),
 "Severance Analysis": (0.6, "퇴직금 수준 분석(실재)"),
 "Patent Newsletter": (0.55, "특허 뉴스레터(콘텐츠 실재)"),
 "Referendum App": (0.6, "주민투표 정보 앱(시빅테크 실재)"),
 "Story Tips": (0.55, "스토리 작성 팁(App→Tips 평행)"),
 "Style Coach": (0.6, "퍼스널 스타일 코칭(실재 시장)"),
 "Sailing Kit": (0.55, "항해 장비 키트(Climbing Kit 평행)"),
 "Cholesterol Helper": (0.55, "지질 관리 도우미(Hypertension Helper 평행)"),
 "Compressor App": (0.55, "압축기 모니터링 앱(실재)"),
 "Clarinet Workbook": (0.55, "클라리넷 교본 워크북(메서드북 실재)"),
 "Softener App": (0.6, "정수기(연수기) 관리 앱(실재)"),
 "Traveler Tips": (0.55, "여행자 팁(App→Tips 평행)"),
 "Indemnity Analysis": (0.55, "배상 보험 데이터 분석(Analysis 평행)"),
 "Severance Coach": (0.55, "퇴직 협상 코칭(실재)"),
 "Rubric App": (0.65, "채점 기준표(rubric) 생성 앱(실재 시장)"),
 "Referendum Tips": (0.55, "주민투표 안내 팁(App→Tips 평행)"),
 "Internship Workbook": (0.55, "인턴십 준비 워크북(커리어 서식 실재)"),
 "Implant Analysis": (0.55, "임플란트 증례 분석(치과 실무 실재)"),
 "Lullaby Coach": (0.55, "수면(자장가) 코칭(실재)"),
 "Fertility Recorder": (0.55, "배략 주기 기록(주기 트래커 실재)"),
 "Golf Helper": (0.55, "골프 게임 보조 도우미(실재)"),
}
R_DUP = {
 "Unpacking Advice": "동일 배치 승인된 Unpacking App/Tips와 동일 기능 의미 중복",
 "Clarinet Advice": "동일 배치 승인된 Clarinet App/Tips와 동일 기능 의미 중복",
 "Vaccine Advice": "동일 배치 승인된 Vaccine App/Tips와 동일 기능 의미 중복",
 "Proofing Advice": "동일 배치 승인된 Proofing App/Tips와 동일 기능 의미 중복",
 "Sightseeing Advice": "동일 배치 승인된 Sightseeing App/Tips와 동일 기능 의미 중복",
 "Mandolin Advice": "동일 배치 승인된 Mandolin App/Tips와 동일 기능 의미 중복",
 "Story Advice": "동일 배치 승인된 Story App/Tips와 동일 기능 의미 중복",
 "Internship Advice": "동일 배치 승인된 Internship App/Tips와 동일 기능 의미 중복",
}
R = {
 "Penguin Invoice": "결합 불성립", "Flamingo Renewal": "갱신 대상 불분명",
 "Turtle Quote": "인용·견적 중의로 대상 불분명", "Moose Warranty": "결합 불성립",
 "Bison Deposit": "결합 불성립", "Reindeer Certification": "결합 불성립",
 "Cylinder App": "제품 불분명(자물쇠 실린더·가스 실린더 중의)", "Proofing Tips SKIP": "",
 "Proof Workbook": "워크북 대상 불분명", "Invitation Mode": "기능 토글로 읽혀 제품 불분명",
 "Eviction Spec": "사양 참조로 제품 불분명", "Algae Quantity": "수량 대상 불분명",
 "Upholstery Login": "제품 불분명", "Sink Analysis": "분석 대상 불분명",
 "Trip Coach SKIP": "", "Vocal Habit": "결합 불성립",
 "Plunger App": "제품 불분명", "Sightseeing Tips SKIP": "",
 "Consent Workbook": "워크북 대상 불분명", "Escrow Mode": "기능 토글로 읽혀 제품 불분명",
 "Statute Spec": "사양 참조로 제품 불분명", "Backorder Quantity": "수량 대상 불분명",
 "Binder Analysis": "분석 대상 불분명", "Review Coach SKIP": "",
 "Lien Habit": "결합 불성립", "Lawyer Stake": "결합 불성립",
 "Attorney Rendering": "결합 불성립", "Court Volume": "결합 불성립",
 "Judge Predictor": "예측 대상 불분명", "Jury Capacity": "결합 불성립",
 "Traveler App SKIP": "", "Mandolin Tips SKIP": "",
 "Remittance Workbook": "워크북 대상 불분명", "Lawsuit Mode": "기능 토글로 읽혀 제품 불분명",
 "Trailer Spec": "사양 참조로 제품 불분명", "Contingency Quantity": "수량 대상 불분명",
 "Indemnity Login": "제품 불분명", "Severance Analysis SKIP": "",
 "Painting Coach": "코칭 대상 불분명", "Prerequisite Habit": "결합 불성립",
 "Divorce Studio": "결합 불성립", "Custody Locator": "탐색 대상 불분명",
 "Immigration Level": "결합 불성립", "Testament Petition": "절차 용어 부정확로 대상 불분명",
 "Notary Identifier": "결합 불성립", "Mediation Sketch": "제품성 불분명",
 "Guardianship Comparison": "비교 대상 불분명", "Trademark Eligibility": "상태 명사로 제품 불분명",
 "Patent Newsletter SKIP": "", "Copyright Compatibility": "결합 불성립",
 "Referendum App SKIP": "", "Story Tips SKIP": "",
 "Attendance Workbook": "워크북 대상 불분명", "Transmission Mode": "기능 토글로 읽혀 제품 불분명",
 "Donut Spec": "사양 참조로 제품 불분명", "Euthanasia Quantity": "수량 대상 불분명",
 "Implant Login": "제품 불분명", "Lullaby Analysis": "분석 대상 불분명",
 "Style Coach SKIP": "", "Substitution Habit": "결합 불성립",
 "Migraine Format": "결합 불성립", "Insomnia Balance": "결합 불성립",
 "Skydiving Due": "결합 불성립", "Acne Subsidy": "결합 불성립",
 "Snowboarding Penalty": "결합 불성립", "Eczema Markup": "마크업 대상 불분명",
 "Ziplining Trial": "결합 불성립", "Psoriasis Graph": "그래프 대상 불분명",
 "Sledding Worksheet": "워크시트 근거 약함", "Vertigo Diagram": "도식 대상 불분명",
 "Diving Sketch": "제품성 불분명", "Arthritis Outline": "개요 대상 불분명",
 "Sailing Kit SKIP": "", "Menopause Count": "카운트 대상 불분명",
 "Rafting Widget": "결합 불성립", "Pregnancy Repository": "결합 불성립",
 "Climbing Converter": "변환 대상 불분명(Climbing Calculator와 중복 우려)",
 "Fertility Generator": "생성 대상 불분명", "Biking Checker": "검사 대상 불분명",
 "Thyroid Detector": "탐지 대상 불분명", "Golf Guardian": "감시 대상 불분명",
 "Cholesterol Helper SKIP": "", "Fishing Streak": "결합 불성립",
 "Hypertension Rank": "결합 불성립", "Camping Proposal": "제안 대상 불분명",
 "Anemia Guarantee": "결합 불성립", "Glamping Reading": "수치 대상 불분명",
 "Heartburn Reference": "결합 불성립", "Stargazing Duration": "결합 불성립",
 "Constipation Volume": "결합 불성립", "Birdwatching Authorization": "결합 불성립",
 "Concussion Template": "결합 불성립", "Canyon Rating": "평가 대상 불분명",
 "Sprain Agreement": "결합 불성립", "Geyser Reply": "결합 불성립",
 "Fracture Account": "결합 불성립", "Fjord Case": "결합 불성립",
 "Insulin Match": "결합 불성립", "Savanna Validation": "결합 불성립",
 "Tundra Lookup": "탐색 대상 불분명", "Prairie Ping": "결합 불성립",
 "Marsh Model": "결합 불성립", "Cove Availability": "상태 명사로 제품명 부자연",
 "Cliff Eligibility": "결합 불성립", "Cavern Broadcast": "결합 불성립",
 "Oasis Barcode": "결합 불성립", "Dune Appointment": "약속 대상 불분명",
 "Whale Feedback": "결합 불성립", "Dolphin Invoice": "결합 불성립",
 "Penguin Renewal": "갱신 대상 불분명", "Flamingo Quote": "인용·견적 중의로 대상 불분명",
 "Turtle Warranty": "결합 불성립", "Moose Deposit": "결합 불성립",
 "Bison Certification": "결합 불성립", "Reindeer Nomination": "결합 불성립",
 "Compressor App SKIP": "", "Cylinder Tips": "팁 대상 불분명",
 "Unpacking Workbook": "워크북 대상 불분명", "Proof Mode": "기능 토글로 읽혀 제품 불분명",
 "Invitation Spec": "사양 참조로 제품 불분명", "Eviction Quantity": "수량 대상 불분명",
 "Algae Login": "제품 불분명", "Upholstery Analysis": "분석 대상 불분명",
 "Sink Coach": "코칭 대상 불분명", "Trip Habit": "결합 불성립",
 "Rinse App": "제품 불분명", "Plunger Tips": "팁 대상 불분명",
 "Clarinet Workbook SKIP": "", "Consent Mode": "기능 토글로 읽혀 제품 불분명",
 "Escrow Spec": "사양 참조로 제품 불분명", "Statute Quantity": "수량 대상 불분명",
 "Backorder Login": "제품 불분명", "Binder Coach": "코칭 대상 불분명",
 "Review Habit": "결합 불성립", "Lawyer Margin": "결합 불성립",
 "Attorney Notification": "알림 대상 불분명", "Court Diagnostic": "진단 대상 불분명",
 "Judge Seal": "결합 불성립", "Jury Usage": "결합 불성립",
 "Softener App SKIP": "", "Traveler Tips SKIP": "",
 "Vaccine Workbook": "워크북 대상 불분명", "Remittance Mode": "기능 토글로 읽혀 제품 불분명",
 "Lawsuit Spec": "사양 참조로 제품 불분명", "Trailer Quantity": "수량 대상 불분명",
 "Contingency Login": "제품 불분명", "Indemnity Analysis SKIP": "",
 "Severance Coach SKIP": "", "Painting Habit": "결합 불성립",
 "Divorce Lab": "결합 불성립", "Custody Finder": "탐색 대상 불분명",
 "Immigration Rate": "결합 불성립", "Testament Confirmation": "결합 불성립",
 "Notary Category": "결합 불성립", "Mediation Outline": "개요 대상 불분명",
 "Guardianship Proposal": "제안 대상 불분명", "Trademark Broadcast": "결합 불성립",
 "Patent Inventory": "결합 불성립", "Copyright Capacity": "결합 불성립",
 "Rubric App SKIP": "", "Referendum Tips SKIP": "",
 "Internship Workbook SKIP": "", "Attendance Mode": "기능 토글로 읽혀 제품 불분명",
 "Transmission Spec": "사양 참조로 제품 불분명", "Donut Quantity": "수량 대상 불분명",
 "Euthanasia Login": "제품 불분명", "Implant Analysis SKIP": "",
 "Lullaby Coach SKIP": "", "Style Habit": "결합 불성립",
 "Migraine Serial": "결합 불성립", "Insomnia Interest": "결합 불성립",
 "Skydiving Subsidy": "결합 불성립", "Acne Discount": "판촉 계열 기각 선례",
 "Snowboarding Markup": "마크업 대상 불분명", "Eczema Redemption": "결합 불성립",
 "Ziplining Graph": "그래프 대상 불분명", "Psoriasis Label": "결합 불성립",
 "Sledding Diagram": "도식 대상 불분명", "Vertigo Schematic": "도식 대상 불분명(Vertigo Diagram 기각 선례)",
 "Diving Outline": "개요 대상 불분명", "Arthritis Rendering": "결합 불성립",
 "Sailing Count": "카운트 대상 불분명", "Menopause Message": "메시지 대상 불분명",
 "Rafting Repository": "결합 불성립", "Pregnancy Announcement": "이벤트 명칭으로 제품 불분명",
 "Climbing Generator": "생성 대상 불분명", "Fertility Recorder SKIP": "",
 "Biking Detector": "탐지 대상 불분명", "Thyroid Timer": "결합 불성립",
 "Golf Helper SKIP": "", "Cholesterol Stage": "단계 대상 불분명",
 "Fishing Rank": "결합 불성립",
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
out = base + r"\_dec_c35.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
