# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk5_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Notary Message": (0.55, "공증 기한·진행 안내 메시지(Notary Notification 승인 선례 평행)"),
 "Pool App": (0.55, "수영장 관리·수질 균형 앱(실재)"),
 "Pool Tips": (0.55, "Pool App 승인 선례의 Tips 평행"),
 "Surfing Tips": (0.55, "Surfing App 승인 선례의 Tips 평행"),
 "Bid Tips": (0.55, "Bid App 승인 선례의 Tips 평행"),
 "Stewardship App": (0.6, "기부자 관리·감사 커뮤니케이션 앱(실재)"),
 "Winterization App": (0.55, "월동 준비·동파 방지 관리 앱(실재 서비스 카테고리)"),
 "Panic App": (0.55, "긴급 호출 패닉 버튼 앱(실재)"),
 "Migraine Calculator": (0.55, "편두통 트리거·카페인 한도 계산기(Acne Calculator 평행)"),
 "Insomnia Checker": (0.55, "수면 질 체크(Eczema/Acne Checker 평행)"),
 "Acne Helper": (0.55, "여드름 관리 도우미(Psoriasis/Eczema Helper 평행)"),
 "Menopause Guide": (0.55, "폐경 단계별 가이드 콘텐츠(Fertility/Pregnancy Guide 평행)"),
 "Adjuster App": (0.6, "보험 손해사정 업무 앱(실재)"),
 "Stargazing Review": (0.55, "별보 명소·장비 리뷰(Fjord/Birdwatching Review 평행)"),
 "Birdwatching Diary": (0.55, "조류 관찰 일지(birding journal 실재)"),
 "Psoriasis Record": (0.55, "건선 증상 기록(Vertigo/Menopause Record 승인 선례 평행)"),
}

R_DUP = {
 "Tourist Advice": "이번 배치 승인 Tourist Tips와 동일 기능 의미 중복",
 "Tempo Advice": "이번 배치 승인 Tempo Tips와 동일 기능 의미 중복",
 "Surfing Advice": "이번 배치 승인 Surfing Tips와 동일 기능 의미 중복",
 "Fulfillment Advice": "직전 승인 Fulfillment Tips와 동일 기능 의미 중복",
 "Content Advice": "직전 승인 Content Tips와 동일 기능 의미 중복",
}

R = {
 "Patch Spec": "사양 참조로 제품 불분명", "Configuration Quantity": "수량 대상 불분명",
 "Chat Login": "제품 불분명", "Logistics Coach": "코칭 대상 불분명",
 "Lawyer Schematic": "도식 대상 불분명", "Attorney Diagnostic": "진단 대상 불분명",
 "Court Review": "리뷰 대상 불분명", "Judge Condition": "상태 명사로 제품명 부자연",
 "Undercarriage App": "하부 지칭으로 앱 용도 불분명", "Undercarriage Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Drainpipe Tips": "선례 기각(App 기각)의 Tips 평행 불가", "Drainpipe Advice": "선례 기각(App 기각)의 Advice 불가",
 "Percussion Workbook": "워크북 대상 불분명", "Jury Quantity": "수량 대상 불분명",
 "Lane Login": "제품 불분명", "Walkthrough Analysis": "분석 대상 불분명",
 "Liability Coach": "코칭 대상 불분명", "Garnishment Habit": "결합 불성립",
 "Lawsuit Station": "스테이션 지칭으로 제품 불분명", "Divorce Counter": "카운터 지칭으로 제품 불분명",
 "Custody Feed": "피드 기능 지칭으로 제품 불분명", "Immigration Fee": "수수료 지칭으로 제품 불분명",
 "Testament Serial": "일련번호 지칭으로 제품 불분명", "Mediation Duration": "기간 속성 지칭으로 제품명 부자연",
 "Guardianship Deposit": "결합 불성립", "Trademark Type": "결합 불성립(분류 대상 부자연)",
 "Patent Approval": "승인 지칭으로 제품 불분명", "Bandage Workbook": "워크북 대상 불분명",
 "Bankruptcy Mode": "기능 토글로 읽혀 제품 불분명", "Copyright Spec": "사양 참조로 제품 불분명",
 "Consolidation Quantity": "수량 대상 불분명", "Staging Login": "제품 불분명",
 "Beneficiary Analysis": "분석 대상 불분명", "Seniority Coach": "코칭 대상 불분명",
 "Waterproofing Habit": "결합 불성립", "Migraine Announcement": "결합 불성립",
 "Insomnia Estimator": "산출 대상 불분명", "Skydiving Workshop": "결합 불성립(Workshop 계열 기각 선례)",
 "Acne Guardian": "감시자 명사 결합 불성립", "Snowboarding Streak": "앱 기능 지칭으로 제품 불분명",
 "Eczema Rank": "순위 대상 불분명", "Ziplining Proposal": "제안 대상 불분명",
 "Psoriasis Guarantee": "결합 불성립", "Sledding Reading": "독서·측정 중의로 불분명",
 "Vertigo Reference": "참조 대상 불분명", "Diving Duration": "기간 속성 지칭으로 제품명 부자연",
 "Arthritis Volume": "결합 불성립", "Sailing Authorization": "결합 불성립",
 "Menopause Template": "결합 불성립", "Rafting Agreement": "결합 불성립",
 "Pregnancy Reply": "결합 불성립", "Climbing Match": "매칭·경기 중의로 불분명",
 "Fertility Validation": "결합 불성립", "Biking Model": "모델 지칭으로 제품 불분명",
 "Thyroid Availability": "상태 명사로 제품명 부자연", "Golf Barcode": "결합 불성립",
 "Cholesterol Appointment": "약속 대상 불분명", "Fishing Renewal": "결합 불성립",
 "Hypertension Quote": "인용·견적 중의로 불분명", "Camping Certification": "결합 불성립",
 "Anemia Nomination": "결합 불성립", "Glamping Payment": "결합 불성립",
 "Heartburn Verification": "결합 불성립", "Stargazing Seal": "결합 불성립",
 "Constipation Review": "리뷰 대상 불분명", "Concussion Refund": "결합 불성립",
 "Canyon Newsletter": "결합 불성립", "Sprain Inventory": "결합 불성립",
 "Geyser Claim": "결합 불성립", "Fracture Onboarding": "결합 불성립",
 "Fjord Checkin": "결합 불성립", "Insulin Size": "결합 불성립(속성 지칭)",
 "Savanna Length": "결합 불성립(속성 지칭)", "Tundra Weight": "결합 불성립(속성 지칭)",
 "Prairie Distance": "결합 불성립", "Marsh Range": "결합 불성립",
 "Cove Limit": "결합 불성립", "Cliff Type": "결합 불성립(분류 대상 부자연)",
 "Cavern Clock": "결합 불성립", "Oasis Time": "결합 불성립",
 "Dune Speed": "결합 불성립", "Whale Depth": "결합 불성립",
 "Dolphin Height": "결합 불성립", "Penguin Width": "결합 불성립",
 "Flamingo Temperature": "결합 불성립", "Turtle Pressure": "결합 불성립",
 "Moose Load": "결합 불성립", "Bison Voltage": "결합 불성립",
 "Reindeer Wattage": "결합 불성립", "Amenity Workbook": "워크북 대상 불분명",
 "Tuition Mode": "기능 토글로 읽혀 제품 불분명", "Downtime Spec": "사양 참조로 제품 불분명",
 "Crop Quantity": "수량 대상 불분명", "Fundraising Analysis": "분석 대상 불분명",
 "Constituent Coach": "코칭 대상 불분명", "Brand Habit": "결합 불성립",
 "Circulation Workbook": "워크북 대상 불분명", "Activation Spec": "사양 참조로 제품 불분명",
 "Patch Quantity": "수량 대상 불분명", "Configuration Login": "제품 불분명",
 "Chat Analysis": "분석 대상 불분명", "Logistics Habit": "결합 불성립",
 "Lawyer Layout": "배치 대상 불분명", "Attorney Progress": "진행 대상 불분명",
 "Court Recipe": "결합 불성립", "Judge Humidity": "결합 불성립",
 "Tourist Workbook": "워크북 대상 불분명", "Percussion Mode": "기능 토글로 읽혀 제품 불분명",
 "Jury Login": "제품 불분명", "Lane Analysis": "분석 대상 불분명",
 "Walkthrough Coach": "코칭 대상 불분명", "Liability Habit": "결합 불성립",
 "Lawsuit Terminal": "단말·터미널 중의로 불분명", "Divorce Booth": "부스 지칭으로 제품 불분명",
 "Custody Draft": "초안 대상 불분명", "Immigration Item": "항목 지칭으로 제품 불분명",
 "Testament Token": "토큰 기능 지칭으로 제품 불분명", "Notary Total": "합계 지칭으로 제품 불분명",
 "Mediation Volume": "결합 불성립", "Guardianship Certification": "결합 불성립",
 "Trademark Clock": "결합 불성립", "Patent Matrix": "행렬·매트릭스 중의로 불분명",
 "Tempo Workbook": "워크북 대상 불분명", "Bandage Mode": "기능 토글로 읽혀 제품 불분명",
 "Bankruptcy Spec": "사양 참조로 제품 불분명", "Copyright Quantity": "수량 대상 불분명",
 "Consolidation Login": "제품 불분명", "Staging Analysis": "분석 대상 불분명",
 "Beneficiary Coach": "코칭 대상 불분명", "Seniority Habit": "결합 불성립",
 "Skydiving Guardian": "감시자 명사 결합 불성립", "Snowboarding Rank": "순위 대상 불분명",
 "Eczema Trend": "결합 불성립", "Ziplining Guarantee": "결합 불성립",
 "Sledding Reference": "참조 대상 불분명", "Vertigo Forecast": "예측 대상 불분명",
 "Diving Volume": "결합 불성립", "Arthritis Diagnostic": "진단 대상 불분명",
 "Sailing Template": "결합 불성립", "Rafting Reply": "결합 불성립",
 "Pregnancy Account": "결합 불성립", "Climbing Validation": "결합 불성립",
 "Fertility Lookup": "탐색 대상 불분명", "Biking Availability": "상태 명사로 제품명 부자연",
 "Thyroid Eligibility": "결합 불성립", "Golf Appointment": "약속 대상 불분명",
 "Cholesterol Feedback": "결합 불성립", "Fishing Quote": "인용·견적 중의로 불분명",
 "Hypertension Warranty": "결합 불성립", "Camping Nomination": "결합 불성립",
 "Anemia Correction": "결합 불성립", "Glamping Verification": "결합 불성립",
 "Heartburn Simulator": "결합 불성립", "Constipation Recipe": "결합 불성립",
 "Birdwatching Refund": "결합 불성립", "Concussion Expense": "결합 불성립",
 "Canyon Inventory": "결합 불성립", "Sprain Claim": "결합 불성립",
 "Geyser Onboarding": "결합 불성립", "Fracture Checkin": "결합 불성립",
 "Fjord Size": "결합 불성립(속성 지칭)", "Insulin Length": "결합 불성립(속성 지칭)",
 "Savanna Weight": "결합 불성립(속성 지칭)", "Tundra Distance": "결합 불성립",
 "Prairie Range": "결합 불성립", "Marsh Limit": "결합 불성립",
 "Cove Type": "결합 불성립(분류 대상 부자연)", "Cliff Clock": "결합 불성립",
 "Cavern Time": "결합 불성립", "Oasis Speed": "결합 불성립",
 "Dune Depth": "결합 불성립", "Whale Height": "결합 불성립",
 "Dolphin Width": "결합 불성립", "Penguin Temperature": "결합 불성립",
 "Flamingo Pressure": "결합 불성립", "Turtle Load": "결합 불성립",
 "Moose Voltage": "결합 불성립", "Bison Wattage": "결합 불성립",
 "Reindeer Brightness": "결합 불성립",
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
out = base + r"\_dec_c6.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
