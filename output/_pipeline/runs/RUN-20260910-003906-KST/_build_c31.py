# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk31_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Tundra Guide": (0.55, "툰드라 탐방 가이드(Prairie Guide 평행)"),
 "Upholstery App": (0.6, "업홀스터리 청소 예약·관리 앱(실재)"),
 "Sink Tips": (0.55, "싱크 수리·관리 팁(콘텐츠 실재)"),
 "Vocal Workbook": (0.55, "발성 훈련 워크북(Ensemble Workbook 평행)"),
 "Binder Tips": (0.55, "보험 인수증 작성 팁(App→Tips 평행)"),
 "Lien Workbook": (0.55, "유치권 절차 워크북(실재 법률 서식)"),
 "Silo Analysis": (0.55, "사일리 곡물 재고·품질 분석(실재)"),
 "Attorney Manual": (0.55, "변호사 업무 매뉴얼(Lawsuit Handbook 평행)"),
 "Court Record": (0.65, "법원 기록 조회·관리(실재 시장)"),
 "Indemnity App": (0.6, "배상책임 보험 관리 앱(실재)"),
 "Severance Tips": (0.55, "퇴직금 협상 팁(App→Tips 평행)"),
 "Implant App": (0.6, "치과 임플란트 관리 앱(실재 카테고리)"),
 "Lullaby Tips": (0.55, "자장가 활용 팁(App→Tips 평행)"),
 "Creditor Analysis": (0.6, "채권 포트폴리오 분석(실재)"),
 "Sailing Diagram": (0.55, "항해 장비 도식(Rafting Diagram 평행)"),
 "Camping Helper": (0.55, "캠핑 준비 도우미(Glamping Helper 평행)"),
 "Heartburn Trend": (0.55, "역류 증상 추이 기록(Constipation Trend 평행)"),
 "Constipation Record": (0.55, "배변 기록 장부(실재)"),
 "Savanna Guide": (0.55, "사바나 사파리 가이드(여행 콘텐츠 실재)"),
 "Upholstery Tips": (0.55, "업홀스터리 관리 팁(App→Tips 평행)"),
 "Trip Workbook": (0.55, "여행 계획 워크북(실재 서식)"),
 "Pallet Analysis": (0.55, "팔레트 재고 분석(물류 실재)"),
 "Backorder App": (0.65, "재고 부족(backorder) 관리 앱(실재 시장)"),
 "Review Workbook": (0.55, "성과 평가 작성 워크북(실재 서식)"),
 "Alumni Login": (0.55, "동문회 포털 접속(실재)"),
 "Throughput Analysis": (0.65, "생산 처리량 분석(제조 실재)"),
 "Attorney Worksheet": (0.55, "사건 준비 워크시트(실재 서식)"),
 "Court Copy": (0.55, "법원 문서 사본 발급(실재 서비스)"),
 "Contingency App": (0.65, "부동산 계약 조건부(contingency) 관리 앱(실재)"),
 "Indemnity Tips": (0.55, "배상 보험 팁(App→Tips 평행)"),
 "Recruiter Analysis": (0.6, "채용 퍼널 분석(실재)"),
 "Guardianship Helper": (0.55, "후견 등록 절차 도우미(실재)"),
 "Trademark Match": (0.6, "상표 유사성 검색(클리어런스 실재)"),
 "Trademark Case": (0.55, "상표 사건 관리(출원·이의 절차 실재)"),
 "Patent Review": (0.55, "특허 사전 검토(실재 업무)"),
 "Euthanasia App": (0.55, "반려동물 안락사 예약·안내 앱(실재 서비스 카테고리)"),
 "Implant Tips": (0.55, "임플란트 사후관리 팁(App→Tips 평행)"),
 "Style Workbook": (0.55, "스타일 계획 워크북(실재 서식)"),
 "Injury Analysis": (0.55, "부상 데이터 분석(스포츠 의학 실재)"),
 "Fishing Detector": (0.55, "어군 탐지 도구(피셔파인더 실재 카테고리)"),
}
R_DUP = {
 "Trip Advice": "동일 배치 승인된 Trip App/Tips와 동일 기능 의미 중복",
 "Review Advice": "동일 배치 승인된 Review App/Tips와 동일 기능 의미 중복",
 "Painting Advice": "동일 배치 승인된 Painting App/Tips와 동일 기능 의미 중복",
 "Style Advice": "동일 배치 승인된 Style App/Tips와 동일 기능 의미 중복",
 "Sink Advice": "동일 청크 승인된 Sink Tips와 동일 기능 의미 중복",
 "Binder Advice": "동일 배치 승인된 Binder App/Tips와 동일 기능 의미 중복",
 "Severance Advice": "동일 배치 승인된 Severance App/Tips와 동일 기능 의미 중복",
 "Lullaby Advice": "동일 배치 승인된 Lullaby App/Tips와 동일 기능 의미 중복",
}
R = {
 "Anemia Helper": "도움 대상 불분명", "Glamping Streak": "결합 불성립",
 "Heartburn Rank": "결합 불성립", "Stargazing Proposal": "제안 대상 불분명",
 "Constipation Guarantee": "결합 불성립", "Birdwatching Reading": "결합 불성립",
 "Concussion Reference": "결합 불성립(Fracture Reference 기각 선례)",
 "Canyon Deadline": "결합 불성립", "Sprain Duration": "결합 불성립",
 "Geyser Volume": "결합 불성립", "Fracture Diagnostic": "진단 대상 불분명",
 "Fjord Progress": "결합 불성립", "Insulin Authorization": "결합 불성립",
 "Savanna Template": "결합 불성립", "Prairie Rating": "평가 대상 불분명",
 "Marsh Agreement": "결합 불성립", "Cove Reply": "결합 불성립",
 "Cliff Account": "결합 불성립", "Cavern Case": "결합 불성립",
 "Oasis Match": "결합 불성립", "Dune Validation": "결합 불성립",
 "Whale Lookup": "탐색 대상 불분명(Moose Lookup 기각 선례)", "Dolphin Ping": "결합 불성립",
 "Penguin Model": "결합 불성립", "Flamingo Availability": "상태 명사로 제품명 부자연",
 "Turtle Eligibility": "결합 불성립", "Moose Broadcast": "결합 불성립",
 "Bison Barcode": "결합 불성립", "Reindeer Appointment": "약속 대상 불분명",
 "Trip Advice SKIP": "", "Payment Spec": "사양 참조로 제품 불분명",
 "Redline Quantity": "수량 대상 불분명", "Pallet Login": "로그인 화면명으로 제품 불분명",
 "Coverage Coach": "코칭 대상 불분명", "Leave Habit": "결합 불성립",
 "Review Advice SKIP": "", "Bundle Mode": "기능 토글로 읽혀 제품 불분명",
 "Alumni Quantity": "수량 대상 불분명", "Throughput Login": "제품 불분명",
 "Ledger Habit": "결합 불성립", "Lawyer Cash": "결합 불성립",
 "Judge Certification": "결합 불성립", "Jury Pressure": "결합 불성립",
 "Lawsuit Retreat": "결합 불성립", "Painting Advice SKIP": "",
 "Prerequisite Workbook": "워크북 대상 불분명", "Budget Mode": "기능 토글로 읽혀 제품 불분명",
 "Caption Spec": "사양 참조로 제품 불분명", "Sentiment Quantity": "수량 대상 불분명",
 "Recruiter Login": "로그인 화면명으로 제품 불분명", "Lanyard Analysis": "결합 불성립",
 "Silo Coach": "코칭 대상 불분명",
 "Checkup Coach": "코칭 대상 불분명", "Cafe Habit": "결합 불성립",
 "Divorce Map": "지도·로드맵 중의로 대상 불분명", "Custody Register": "등록 대상 불분명",
 "Immigration Note": "결합 불성립", "Testament Memo": "결합 불성립",
 "Notary Margin": "결합 불성립", "Mediation Graph": "그래프 대상 불분명",
 "Guardianship Guardian": "동어 반복으로 결합 불성립", "Trademark Case SKIP": "",
 "Patent Seal": "결합 불성립", "Copyright Temperature": "결합 불성립",
 "Implant App SKIP": "", "Style Advice SKIP": "",
 "Substitution Workbook": "워크북 대상 불분명", "Playground Mode": "기능 토글로 읽혀 제품 불분명",
 "Casino Spec": "사양 참조로 제품 불분명", "Ensemble Quantity": "수량 대상 불분명",
 "Injury Login": "제품 불분명", "Reefer Coach": "코칭 대상 불분명",
 "Renovation Habit": "결합 불성립", "Migraine Link": "결합 불성립",
 "Insomnia Attribute": "결합 불성립", "Skydiving Token": "결합 불성립",
 "Acne Signature": "결합 불성립", "Snowboarding Asset": "결합 불성립",
 "Eczema Levy": "결합 불성립", "Ziplining Discount": "판촉 계열 기각 선례",
 "Psoriasis Arrears": "결합 불성립", "Sledding Markup": "마크업 대상 불분명",
 "Vertigo Redemption": "결합 불성립", "Diving Graph": "그래프 대상 불분명",
 "Arthritis Label": "결합 불성립", "Menopause Schematic": "도식 대상 불분명(Pregnancy Schematic 기각 선례)",
 "Rafting Outline": "개요 대상 불분명", "Pregnancy Rendering": "결합 불성립",
 "Climbing Count": "카운트 대상 불분명", "Fertility Message": "결합 불성립",
 "Biking Repository": "결합 불성립", "Thyroid Announcement": "결합 불성립",
 "Golf Generator": "생성 대상 불분명", "Cholesterol Recorder": "기록 대상 불분명(자가 측정 불가)",
 "Hypertension Timer": "결합 불성립", "Anemia Stage": "단계 대상 불분명",
 "Glamping Rank": "결합 불성립", "Stargazing Guarantee": "결합 불성립",
 "Birdwatching Reference": "결합 불성립(Sprain Reference 기각 선례)",
 "Concussion Forecast": "결합 불성립", "Canyon Duration": "결합 불성립",
 "Sprain Volume": "결합 불성립", "Geyser Diagnostic": "진단 대상 불분명",
 "Fracture Progress": "진행 대상 불분명(Insulin Progress 기각 선례)",
 "Fjord Authorization": "결합 불성립", "Insulin Template": "결합 불성립",
 "Tundra Rating": "평가 대상 불분명", "Prairie Agreement": "결합 불성립",
 "Marsh Reply": "결합 불성립", "Cove Account": "결합 불성립",
 "Cliff Case": "결합 불성립", "Cavern Match": "결합 불성립",
 "Oasis Validation": "결합 불성립", "Dune Lookup": "탐색 대상 불분명",
 "Whale Ping": "결합 불성립", "Dolphin Model": "결합 불성립",
 "Penguin Availability": "상태 명사로 제품명 부자연", "Flamingo Eligibility": "결합 불성립",
 "Turtle Broadcast": "결합 불성립", "Moose Barcode": "결합 불성립",
 "Bison Appointment": "약속 대상 불분명(Reindeer Appointment 기각 선례)",
 "Reindeer Feedback": "결합 불성립", "Algae App": "제품 불분명(풀 자체가 도메인어)",
 "Sink Advice SKIP": "", "Vocal Mode": "기능 토글로 읽혀 제품 불분명",
 "Payment Quantity": "수량 대상 불분명", "Redline Login": "제품 불분명",
 "Coverage Habit": "결합 불성립", "Backorder App SKIP": "",
 "Binder Advice SKIP": "", "Lien Mode": "기능 토글로 읽혀 제품 불분명",
 "Bundle Spec": "사양 참조로 제품 불분명", "Lawyer Sale": "결합 불성립",
 "Judge Nomination": "결합 불성립", "Jury Load": "결합 불성립",
 "Lawsuit Tournament": "결합 불성립", "Severance Advice SKIP": "",
 "Painting Workbook": "워크북 용도 불분명", "Prerequisite Mode": "기능 토글로 읽혀 제품 불분명",
 "Budget Spec": "사양 참조로 제품 불분명", "Caption Quantity": "수량 대상 불분명",
 "Sentiment Login": "제품 불분명", "Lanyard Coach": "코칭 대상 불분명",
 "Checkup Habit": "결합 불성립", "Divorce Frame": "결합 불성립",
 "Custody Ops": "결합 불성립", "Immigration Tag": "결합 불성립",
 "Testament Quota": "결합 불성립", "Notary Fine": "결합 불성립",
 "Mediation Label": "결합 불성립", "Trademark Match SKIP": "",
 "Patent Review SKIP": "", "Copyright Pressure": "결합 불성립",
 "Implant Tips SKIP": "", "Lullaby Advice SKIP": "",
 "Substitution Mode": "기능 토글로 읽혀 제품 불분명", "Playground Spec": "사양 참조로 제품 불분명",
 "Casino Quantity": "수량 대상 불분명", "Ensemble Login": "제품 불분명",
 "Creditor Coach": "코칭 대상 불분명", "Reefer Habit": "결합 불성립",
 "Migraine Rule": "결합 불성립", "Insomnia Field": "결합 불성립",
 "Skydiving Signature": "결합 불성립", "Acne Marker": "표식 대상 불분명",
 "Snowboarding Levy": "결합 불성립",
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
out = base + r"\_dec_c31.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
