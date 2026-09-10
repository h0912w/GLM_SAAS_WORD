# -*- coding: utf-8 -*-
import json
from pathlib import Path

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk1_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Whale Diagram": (0.55, "고래 구조 다이어그램(교육 콘텐츠 실검색)"),
 "Dune Diagram": (0.55, "사구 형성 다이어그램(지리 교육)"),
 "Turtle Outline": (0.55, "거북이 공예 오트라인 인쇄물"),
 "Flamingo Outline": (0.55, "플라밍고 공예 오트라인 인쇄물"),
 "Coating Tips": (0.55, "코팅 관리 팁 콘텐츠"),
 "Vacation Workbook": (0.55, "여행 계획 워크북"),
 "Container Analysis": (0.55, "컨테이너 운영 데이터 분석"),
 "Maintenance Coach": (0.55, "유지보수 코칭 도구"),
 "Courier App": (0.55, "택배 접수 앱"),
 "Mortgage Tips": (0.55, "모기지 팁 콘텐츠"),
 "Overtime Workbook": (0.55, "초과근무 관리 워크북"),
 "Welding Analysis": (0.55, "용접 품질 데이터 분석"),
 "Tractor Coach": (0.55, "농기계 운영 코칭"),
 "Donation Habit": (0.55, "후원 습관 관리"),
 "Lawyer Profile": (0.55, "변호사 프로필 관리"),
 "Lawsuit Newsletter": (0.55, "소송 관련 소식 뉴스레터"),
 "Location Tips": (0.55, "촬영지 선정 팁"),
 "Safari Login": (0.55, "사파리 투어 포털 로그인"),
 "Dosage Coach": (0.55, "복약 코칭 도구"),
 "Trading Habit": (0.55, "매매 습관 분석"),
 "Custody Tracker": (0.55, "양육권 일정 추적"),
 "Immigration Portal": (0.6, "이민 절차 포털"),
 "Notary Feed": (0.55, "공증 제도 소식 피드"),
 "Copyright Agreement": (0.55, "저작권 계약서 관리"),
 "Mailroom App": (0.55, "우편물 관리 앱"),
 "Kayaking Tips": (0.55, "카약 팁 콘텐츠"),
 "Stretch Workbook": (0.55, "스트레칭 연습 워크북"),
 "Chore Coach": (0.55, "집안일 분담 코칭"),
 "Migraine Reminder": (0.55, "편두통 기록·복약 알림"),
 "Dune Worksheet": (0.55, "사구 학습 워크시트(지리 교육)"),
 "Renewal App": (0.55, "임대 갱신 관리 앱"),
 "Liner Tips": (0.55, "수영장 라이너 관리 팁"),
 "Vacation Mode": (0.55, "휴가 부재 모드 설정 도구(관용구)"),
 "Reconciliation Login": (0.55, "회계 조정 포털 로그인"),
 "Matter Analysis": (0.55, "법률 사건 데이터 분석"),
 "Paralegal App": (0.55, "법률보조 업무 앱"),
 "Courier Tips": (0.55, "택배 운영 팁"),
 "Annuity Workbook": (0.55, "연금 계획 워크북"),
 "Valet Login": (0.55, "발레 운영 포털 로그인"),
 "Welding Coach": (0.55, "용접 기술 코칭"),
 "Lawyer Status": (0.55, "사건 진행 상태 확인"),
 "Attorney Fee": (0.55, "변호사 보수 구조 조회"),
 "Divorce Followup": (0.55, "이혼 절차 후속 관리"),
 "Idiom App": (0.55, "관용구 학습 앱"),
 "Safari Analysis": (0.55, "투어 운영 데이터 분석"),
 "Harmonica Coach": (0.55, "하모니카 코칭 도구"),
 "Dosage Habit": (0.55, "복약 습관 관리"),
 "Notary Draft": (0.55, "공증 서류 초안 작성"),
 "Mediation Recap": (0.55, "조정 내용 요약"),
 "Patent Guardian": (0.55, "특허 기한 감시 도구"),
 "Formula App": (0.55, "분유 급여 기록 앱"),
}
R_CLARITY = {
 "Golf Allowance": "결합 불성립", "Cholesterol Tariff": "결합 불성립",
 "Fishing Margin": "결합 불성립", "Hypertension Fine": "결합 불성립",
 "Camping Link": "결합 불성립", "Anemia Rule": "결합 불성립",
 "Glamping Category": "결합 불성립", "Heartburn Attribute": "결합 불성립",
 "Stargazing Serial": "결합 불성립", "Constipation Token": "결합 불성립",
 "Birdwatching Balance": "결합 불성립", "Concussion Interest": "결합 불성립",
 "Canyon Levy": "결합 불성립", "Sprain Due": "결합 불성립",
 "Geyser Subsidy": "결합 불성립", "Fracture Discount": "결합 불성립",
 "Fjord Arrears": "결합 불성립", "Insulin Advance": "결합 불성립",
 "Savanna Penalty": "결합 불성립", "Tundra Markup": "결합 불성립",
 "Prairie Redemption": "결합 불성립", "Marsh Extension": "결합 불성립",
 "Cove Trial": "결합 불성립", "Cliff Graph": "그래프 대상 불분명",
 "Cavern Label": "결합 불성립", "Oasis Manual": "설명 대상 불분명",
 "Dolphin Schematic": "회로도 어휘 부자연", "Penguin Layout": "결합 불성립",
 "Flamingo Sketch": "제품성 불분명", "Moose Rendering": "렌더링 대상 불분명",
 "Bison Notification": "결합 불성립", "Reindeer Kit": "키트 대상 불분명",
 "Liner App": "앱 대상 불분명", "Ukulele Mode": "기능 토글로 읽혀 제품 불분명",
 "Toilet Workbook": "워크북 대상 불분명",
 "Prescription Spec": "결합 불성립", "Reconciliation Quantity": "수량 대상 불분명",
 "Matter Login": "포털 서비스 대상 불분명", "Deductible Habit": "결합 불성립",
 "Annuity Advice": "중복", "Scaffold Mode": "기능 토글로 읽혀 제품 불분명",
 "Barcode Spec": "결합 불성립", "Valet Quantity": "수량 대상 불분명",
 "Homework Login": "결합 불성립", "Attorney Entry": "등록 대상 불분명",
 "Court Signature": "서명 대상 불분명", "Judge Calculator": "계산 대상 불분명",
 "Jury Reply": "결합 불성립", "Divorce Reception": "결합 불성립",
 "Stairs App": "앱 대상 불분명", "Decor Advice": "중복",
 "Roof Workbook": "워크북 대상 불분명", "Valve Mode": "기능 토글로 읽혀 제품 불분명",
 "Microfiber Spec": "결합 불성립", "Backflow Quantity": "수량 대상 불분명",
 "Harmonica Analysis": "분석 대상 불분명", "Testament Kiosk": "결합 불성립",
 "Mediation Confirmation": "확인 대상 불분명", "Guardianship Link": "결합 불성립",
 "Trademark Label": "결합 불성립", "Patent Workshop": "워크숍 주체 불분명",
 "Songbook Advice": "조언 대상 불분명", "Insolvency Mode": "기능 토글로 읽혀 제품 불분명",
 "Copay Spec": "결합 불성립", "Masonry Quantity": "수량 산출 근거 약함",
 "Barista Login": "결합 불성립", "Mouthwash Analysis": "분석 대상 불분명",
 "Storage Habit": "결합 불성립", "Insomnia Bill": "결합 불성립",
 "Skydiving Table": "결합 불성립", "Acne Slip": "결합 불성립",
 "Snowboarding Voucher": "바우처 대상 불분명", "Eczema Badge": "결합 불성립",
 "Ziplining Memo": "결합 불성립", "Psoriasis Quota": "결합 불성립",
 "Sledding Brief": "결합 불성립", "Vertigo Circular": "결합 불성립",
 "Diving Confirmation": "확인 대상 불분명", "Arthritis Recap": "결합 불성립",
 "Sailing Item": "항목 대상 불분명", "Menopause Unit": "결합 불성립",
 "Rafting Price": "가격 지칭 부자연, 비용 정보는 승인된 Rafting Cost와 중복",
 "Pregnancy Fare": "결합 불성립", "Climbing Sum": "결합 불성립",
 "Fertility Debt": "결합 불성립", "Biking Sale": "결합 불성립",
 "Thyroid Charge": "결합 불성립", "Golf Tariff": "결합 불성립",
 "Cholesterol Value": "결합 불성립", "Fishing Fine": "결합 불성립",
 "Hypertension Number": "수치 지칭이 조건명과 결합 시 부자연",
 "Camping Rule": "규칙 대상 불분명", "Anemia Detail": "결합 불성립",
 "Glamping Attribute": "결합 불성립", "Heartburn Field": "결합 불성립",
 "Stargazing Token": "결합 불성립", "Constipation Signature": "결합 불성립",
 "Birdwatching Interest": "결합 불성립", "Concussion Asset": "결합 불성립",
 "Canyon Due": "결합 불성립", "Sprain Subsidy": "결합 불성립",
 "Geyser Discount": "결합 불성립", "Fracture Arrears": "결합 불성립",
 "Fjord Advance": "결합 불성립", "Insulin Penalty": "결합 불성립",
 "Savanna Markup": "결합 불성립", "Tundra Redemption": "결합 불성립",
 "Prairie Extension": "결합 불성립", "Marsh Trial": "결합 불성립",
 "Cove Graph": "그래프 대상 불분명", "Cliff Label": "결합 불성립",
 "Cavern Manual": "설명 대상 불분명", "Oasis Worksheet": "학습지 근거 약함",
 "Whale Schematic": "회로도 어휘 부자연", "Dolphin Layout": "결합 불성립",
 "Penguin Sketch": "제품성 불분명", "Turtle Rendering": "렌더링 대상 불분명",
 "Moose Notification": "결합 불성립", "Bison Kit": "키트 대상 불분명",
 "Reindeer Count": "대상 불분명", "Ukulele Spec": "결합 불성립",
 "Prescription Quantity": "수량 대상 불분명", "Container Coach": "코치 대상 불분명",
 "Maintenance Habit": "결합 불성립", "Overtime Mode": "기능 토글로 읽혀 제품 불분명",
 "Scaffold Spec": "결합 불성립", "Barcode Quantity": "수량 대상 불분명",
 "Homework Analysis": "분석 대상 불분명", "Tractor Habit": "결합 불성립",
 "Court Marker": "표시 대상 불분명", "Judge Converter": "변환 대상 불분명",
 "Jury Account": "계정 대상 불분명", "Lawsuit Inventory": "결합 불성립",
 "Stairs Tips": "계단 단독으로 팁 대상 불분명", "Decor Workbook": "워크북 대상 불분명",
 "Roof Mode": "기능 토글로 읽혀 제품 불분명", "Valve Spec": "결합 불성립",
 "Microfiber Quantity": "수량 대상 불분명", "Backflow Login": "결합 불성립",
 "Custody Flow": "흐름 대상 불분명", "Immigration Console": "콘솔 대상 불분명",
 "Testament Bay": "결합 불성립", "Guardianship Rule": "규칙 대상 불분명",
 "Trademark Manual": "매뉴얼 대상 모호", "Copyright Reply": "결합 불성립",
}
R_DUP = {
 "Toilet Advice": "동일 배치 승인된 Toilet Tips(변기 수리 팁)와 동일 기능 의미 중복",
 "Annuity Advice": "동일 배치 승인된 Annuity Tips(연금 팁)와 동일 기능 의미 중복",
 "Decor Advice": "동일 배치 승인된 Decor Tips(인테리어 팁)와 동일 기능 의미 중복",
 "Mortgage Advice": "동일 배치 승인된 Mortgage Tips(모기지 팁)와 동일 기능 의미 중복",
 "Coating Advice": "동일 배치 승인된 Coating Tips(코팅 팁)와 동일 기능 의미 중복",
 "Location Advice": "동일 배치 승인된 Location Tips(촬영지 팁)와 동일 기능 의미 중복",
}
# Annuity Advice는 R_CLARITY에도 들어가 있음 - R_DUP로 우선 적용
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
    elif t in R_CLARITY:
        reason = R_CLARITY[t]
        if reason == "중복":
            raise SystemExit(f"중복 사유 누락: {t}")
        lines.append(f"{t}\tR\tF\tT\tT\t0.6\t{reason}")
        nr += 1
    else:
        raise SystemExit(f"미판정: {t}")
out = base + r"\_dec_c1.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
