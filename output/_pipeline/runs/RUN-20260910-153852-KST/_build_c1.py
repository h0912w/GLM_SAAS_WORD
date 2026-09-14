# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Falcon Ledger": (0.7, "기록물 결합 명확(골든셋)"),
 "Quantum Notary": (0.7, "전자 공증 개념 결합 명확(골든셋)"),
 "Geyser Predictor": (0.55, "간헐천 분출 예측 앱(Old Faithful 실재)"),
 "Fjord Review": (0.55, "피오르 투어 리뷰 콘텐츠(X Review 관용구)"),
 "Savanna Video": (0.55, "사바나 사파리 영상 콘텐츠(Video 관용구)"),
 "Whale Size": (0.55, "고래 크기 비교 콘텐츠(실검색 장르, 속성 명사 실재 결합)"),
 "Brand App": (0.55, "브랜드 자산 관리 앱(실재)"),
 "Manuscript Tips": (0.55, "원고 작성 팁(Tips 관용구)"),
 "Sourcing Login": (0.55, "리크루팅 소싱 포털 접속(포털 청중 명확, Paralegal Login 선례)"),
 "Logistics App": (0.55, "행사 물류 관리 앱(실재)"),
 "Staffing Login": (0.55, "인력 운영 포털 접속(포털 청중 명확)"),
 "Interviewer Login": (0.55, "면접관 일정 포털 접속(포털 청중 명확)"),
 "Lawyer Markup": (0.55, "법률 문서 마크업·레드라인(실재 업무)"),
 "Court Certification": (0.55, "법원 인증 서류 대행·관리(실재 업무)"),
 "Liability App": (0.6, "배상책임 보험 관리 앱(실재)"),
 "Garnishment Tips": (0.55, "Garnishment App 승인 선례의 Tips 평행"),
 "Seniority App": (0.6, "연공서열·근속 관리 앱(실재)"),
 "Waterproofing Tips": (0.55, "Waterproofing App 승인 선례의 Tips 평행"),
 "Notary Diagram": (0.55, "공증 절차 도식 콘텐츠(Diagram 관용구 계열)"),
 "Trademark Claim": (0.55, "상표 청구·침해 대응 관리(실재 법률 업무)"),
 "Patent Usage": (0.55, "특허 사용 현황·로열티 관리(실재)"),
 "Insomnia Message": (0.55, "수면 루틴 리마인드 메시지(Message 관용구)"),
 "Acne Calculator": (0.55, "치료 비용 계산기(Cholesterol Calculator 승인 선례 평행)"),
 "Eczema Checker": (0.55, "증상 체크 가이드(Cholesterol Checker 승인 선례 평행)"),
 "Insulin Video": (0.55, "인슐린 주입법 영상 가이드(실재 콘텐츠)"),
 "Lawsuit Map": (0.55, "소송 통계 지도 콘텐츠(Map 관용구)"),
 "Constituent App": (0.6, "주민 민원·소통 앱(실재)"),
 "Brand Tips": (0.55, "Brand App 승인 선례의 Tips 평행"),
 "Logistics Tips": (0.55, "Logistics App 승인 선례의 Tips 평행"),
 "Walkthrough App": (0.6, "매물 가상 워크스루 투어 앱(실재)"),
 "Liability Tips": (0.55, "Liability App 승인 선례의 Tips 평행"),
 "Seniority Tips": (0.55, "Seniority App 승인 선례의 Tips 평행"),
 "Beneficiary App": (0.6, "수익자 지정 관리 앱(실재)"),
 "Divorce Playbook": (0.55, "이혼 절차 플레이북(Custody Playbook 승인 선례)"),
 "Immigration Bulletin": (0.55, "비자 공고 브리틴 콘텐츠(Visa Bulletin 실재)"),
 "Skydiving Calculator": (0.55, "체험 비용 계산기(Calculator 관용구)"),
 "Psoriasis Helper": (0.55, "증상 관리 도우미(Arthritis/Vertigo Helper 승인 선례 평행)"),
}

R_DUP = {
 "Dispatch Advice": "기존 승인 Dispatch App/Tips와 동일 기능 의미 중복",
 "Allergen Advice": "기존 승인 Allergen App/Tips와 동일 기능 의미 중복",
 "Mentorship Advice": "기존 승인 Mentorship App/Tips와 동일 기능 의미 중복",
 "Waterproofing Advice": "이번 배치 승인 Waterproofing Tips와 동일 기능 의미 중복",
 "Garnishment Advice": "이번 배치 승인 Garnishment Tips와 동일 기능 의미 중복",
 "Manuscript Advice": "이번 배치 승인 Manuscript Tips와 동일 기능 의미 중복",
 "Flooring Advice": "기존 승인 Flooring App/Tips와 동일 기능 의미 중복",
 "Whale Length": "이번 배치 승인 Whale Size와 동일 장르(고래 크기 비교) 의미 중복",
}

R = {
 "Slack Messenger": "유명 SaaS 상표 Slack과 혼동(골든셋)", "Photoshop Canvas": "유명 상표 Photoshop과 혼동(골든셋)",
 "Data Thing": "무의미 결합(골든셋)", "Ledger Sentinel": "감시자 명사 결합 불성립(골든셋)",
 "Ledger Watchman": "감시자 명사 결합 불성립(골든셋)",
 "Fracture Seal": "결합 불성립", "Insulin Recipe": "조리법 대상 불분명",
 "Tundra Diary": "결합 불성립(개인 일지 형식 부재)", "Prairie Refund": "결합 불성립",
 "Marsh Expense": "결합 불성립", "Cove Newsletter": "결합 불성립",
 "Cliff Inventory": "결합 불성립", "Cavern Claim": "결합 불성립",
 "Oasis Onboarding": "결합 불성립", "Dune Checkin": "결합 불성립",
 "Dolphin Length": "결합 불성립(속성 지칭)", "Penguin Weight": "결합 불성립(속성 지칭)",
 "Flamingo Distance": "결합 불성립", "Turtle Range": "결합 불성립",
 "Moose Limit": "결합 불성립", "Reindeer Clock": "결합 불성립",
 "Bison Type": "결합 불성립(분류 대상 부자연)", "Reindeer Time": "결합 불성립",
 "Threat Mode": "기능 토글로 읽혀 제품 불분명", "Provisioning Spec": "사양 참조로 제품 불분명",
 "Queue Quantity": "수량 대상 불분명", "Badge Analysis": "분석 대상 불분명",
 "Trade Coach": "코칭 대상 불분명", "Nutrition Spec": "사양 참조로 제품 불분명",
 "Naptime Quantity": "수량 대상 불분명", "Termite Analysis": "분석 대상 불분명",
 "Mowing Coach": "코칭 대상 불분명", "Turnover Habit": "결합 불성립",
 "Attorney Guarantee": "결합 불성립", "Judge Pressure": "결합 불성립",
 "Jury Retreat": "물러남·수련회 중의로 결합 불성립", "Elective Workbook": "워크북 대상 불분명",
 "Resident Mode": "기능 토글로 읽혀 제품 불분명", "Photo Spec": "사양 참조로 제품 불분명",
 "Rating Quantity": "수량 대상 불분명", "Wifi Analysis": "분석 대상 불분명",
 "Diagnosis Coach": "코칭 대상 불분명", "Waiter Habit": "결합 불성립",
 "Divorce Ops": "운영 약어로 제품 불분명", "Custody Tag": "태그 대상 불분명",
 "Immigration Tab": "탭 기능 조각으로 제품 불분명", "Testament Version": "버전 지칭으로 제품 불분명",
 "Mediation Comparison": "비교 대상 불분명", "Guardianship Eligibility": "상태 명사로 제품명 부자연",
 "Copyright Gift": "결합 불성립", "Curfew Workbook": "워크북 대상 불분명",
 "Author Mode": "기능 토글로 읽혀 제품 불분명", "Notice Quantity": "수량 대상 불분명",
 "Exhaust Login": "소비자 물건 도메인 로그인으로 제품 불분명", "Bagel Analysis": "분석 대상 불분명",
 "Bloodwork Coach": "코칭 대상 불분명", "Denture Habit": "결합 불성립",
 "Migraine Outline": "개요 대상 불분명", "Skydiving Announcement": "결합 불성립",
 "Snowboarding Estimator": "산출 대상 불분명", "Ziplining Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Psoriasis Guardian": "감시자 명사 결합 불성립", "Sledding Result": "결과 지칭으로 제품 불분명",
 "Vertigo Streak": "앱 기능 지칭으로 제품 불분명", "Diving Comparison": "비교 대상 불분명",
 "Arthritis Proposal": "제안 대상 불분명", "Sailing Copy": "복사·원고 중의로 불분명",
 "Menopause Reading": "독서·측정값 중의로 불분명", "Rafting Deadline": "결합 불성립",
 "Pregnancy Duration": "기간 속성 지칭으로 제품명 부자연", "Climbing Progress": "진행 대상 불분명",
 "Fertility Authorization": "결합 불성립", "Biking Rating": "평가 대상 불분명(코스 난이도는 Trail Rating으로 검색)",
 "Thyroid Agreement": "결합 불성립", "Golf Case": "결합 불성립(Case 계열 기각 선례)",
 "Cholesterol Match": "매칭 대상 불분명", "Fishing Ping": "결합 불성립",
 "Hypertension Model": "모델 지칭으로 제품 불분명", "Camping Broadcast": "결합 불성립",
 "Anemia Barcode": "결합 불성립", "Glamping Invoice": "결합 불성립",
 "Heartburn Renewal": "결합 불성립", "Stargazing Deposit": "결합 불성립",
 "Constipation Certification": "결합 불성립", "Birdwatching Revision": "결합 불성립",
 "Concussion Payment": "결합 불성립", "Canyon Simulator": "결합 불성립",
 "Sprain Predictor": "예측 대상 불분명", "Geyser Seal": "결합 불성립",
 "Fracture Review": "리뷰 대상 불분명(병원·의사 리뷰가 아님)", "Fjord Recipe": "결합 불성립",
 "Savanna Diary": "결합 불성립(개인 일지 형식 부재)", "Tundra Refund": "결합 불성립",
 "Prairie Expense": "결합 불성립", "Marsh Newsletter": "결합 불성립",
 "Cove Inventory": "결합 불성립", "Cliff Claim": "결합 불성립",
 "Cavern Onboarding": "결합 불성립", "Oasis Checkin": "결합 불성립",
 "Dune Size": "결합 불성립(속성 지칭)", "Dolphin Weight": "결합 불성립(속성 지칭)",
 "Penguin Distance": "결합 불성립", "Flamingo Range": "결합 불성립",
 "Turtle Limit": "결합 불성립", "Moose Type": "결합 불성립(분류 대상 부자연)",
 "Bison Clock": "결합 불성립", "Dispatch Workbook": "워크북 대상 불분명",
 "Threat Spec": "사양 참조로 제품 불분명", "Provisioning Quantity": "수량 대상 불분명",
 "Queue Login": "제품 불분명", "Sourcing Analysis": "분석 대상 불분명",
 "Badge Coach": "코칭 대상 불분명", "Trade Habit": "결합 불성립",
 "Allergen Workbook": "워크북 대상 불분명", "Nutrition Quantity": "수량 대상 불분명",
 "Naptime Login": "소비자 앱 로그인으로 제품 불분명", "Staffing Analysis": "분석 대상 불분명",
 "Termite Coach": "코칭 대상 불분명", "Mowing Habit": "결합 불성립",
 "Lawyer Redemption": "환수·속죄 중의로 결합 불성립", "Attorney Record": "기록 대상 불분명",
 "Court Nomination": "결합 불성립", "Judge Load": "물리 부하 중의로 결합 불성립",
 "Jury Tournament": "결합 불성립", "Flooring Workbook": "워크북 대상 불분명",
 "Elective Mode": "기능 토글로 읽혀 제품 불분명", "Resident Spec": "사양 참조로 제품 불분명",
 "Photo Quantity": "수량 대상 불분명", "Rating Login": "제품 불분명",
 "Interviewer Analysis": "분석 대상 불분명", "Wifi Coach": "코칭 대상 불분명",
 "Diagnosis Habit": "결합 불성립", "Lawsuit Frame": "결합 불성립",
 "Custody Profile": "프로필 지칭으로 제품 불분명", "Testament Link": "결합 불성립",
 "Notary Schematic": "회로·배선 도로 대상 불분명", "Mediation Proposal": "제안 대상 불분명",
 "Guardianship Broadcast": "결합 불성립", "Trademark Onboarding": "온보딩 대상 불분명",
 "Patent Condition": "상태 명사로 제품명 부자연", "Copyright Retreat": "결합 불성립",
 "Mentorship Workbook": "워크북 대상 불분명", "Curfew Mode": "기능 토글로 읽혀 제품 불분명",
 "Author Spec": "사양 참조로 제품 불분명", "Notice Login": "제품 불분명",
 "Exhaust Analysis": "분석 대상 불분명", "Bagel Coach": "코칭 대상 불분명",
 "Bloodwork Habit": "결합 불성립", "Migraine Rendering": "렌더링 대상 불분명",
 "Insomnia Total": "결합 불성립", "Acne Converter": "변환 대상 불분명",
 "Snowboarding Checker": "체크 대상 불분명", "Eczema Detector": "탐지 대상 불분명",
 "Ziplining Guardian": "감시자 명사 결합 불성립", "Sledding Streak": "앱 기능 지칭으로 제품 불분명",
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
out = base + r"\_dec_c1.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
