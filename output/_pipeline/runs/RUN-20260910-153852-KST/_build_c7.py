# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk6_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Stewardship Tips": (0.55, "Stewardship App 승인 선례의 Tips 평행"),
 "Winterization Tips": (0.55, "Winterization App 승인 선례의 Tips 평행"),
 "Panic Tips": (0.55, "Panic App 승인 선례의 Tips 평행"),
 "Adjuster Tips": (0.55, "Adjuster App 승인 선례의 Tips 평행"),
 "Rotation App": (0.6, "교대·순환 근무 로테이션 관리 앱(실재)"),
 "Vow App": (0.55, "결혼 서원·축사 작성 앱(vow 작성 도구 실재)"),
 "Thermocouple App": (0.55, "열전쌍 온도 측정·보정 앱(산업 측정기 연동 실재)"),
 "Thermocouple Tips": (0.55, "Thermocouple App 승인 선례의 Tips 평행"),
 "Sailing Guide": (0.55, "항해·해상 가이드 콘텐츠(Golf/Biking Guide 평행)"),
 "Constipation Video": (0.55, "변비 완화 운동·식이 영상 가이드(Fracture Video 평행)"),
 "Stargazing Video": (0.55, "관측 가이드 영상(Birdwatching Video 평행)"),
 "Constipation Diary": (0.55, "배변·식이 기록 일지(배변일지 실재, Fracture Diary 평행)"),
 "Custody Timeline": (0.55, "양육 절차 타임라인 기록(Custody History 평행)"),
 "Immigration Plan": (0.55, "비자 절차 로드맵 관리(Immigration Brief 평행)"),
 "Patent Questionnaire": (0.55, "발명 공개 문진 관리(실재 업무)"),
 "Guardianship Nomination": (0.55, "후견인 지정 서류 관리(Immigration Petition 평행)"),
}

R_DUP = {
 "Bid Advice": "직전 승인 Bid Tips와 동일 기능 의미 중복",
 "Pool Advice": "직전 승인 Pool Tips와 동일 기능 의미 중복",
 "Stewardship Advice": "이번 배치 승인 Stewardship Tips와 동일 기능 의미 중복",
 "Winterization Advice": "이번 배치 승인 Winterization Tips와 동일 기능 의미 중복",
 "Panic Advice": "이번 배치 승인 Panic Tips와 동일 기능 의미 중복",
}

R = {
 "Fulfillment Workbook": "워크북 대상 불분명", "Amenity Mode": "기능 토글로 읽혀 제품 불분명",
 "Tuition Spec": "사양 참조로 제품 불분명", "Downtime Quantity": "수량 대상 불분명",
 "Crop Login": "제품 불분명", "Fundraising Coach": "코칭 대상 불분명",
 "Constituent Habit": "결합 불성립", "Content Workbook": "워크북 대상 불분명",
 "Circulation Mode": "기능 토글로 읽혀 제품 불분명", "Activation Quantity": "수량 대상 불분명",
 "Patch Login": "제품 불분명", "Configuration Analysis": "분석 대상 불분명",
 "Chat Coach": "코칭 대상 불분명", "Lawyer Sketch": "스케치 대상 불분명",
 "Attorney Authorization": "결합 불성립", "Court Video": "영상 대상 불분명",
 "Judge Episode": "결합 불성립", "Undercarriage Advice": "선례 기각(App 기각)의 Advice 불가",
 "Drainpipe Workbook": "워크북 대상 불분명", "Tourist Mode": "기능 토글로 읽혀 제품 불분명",
 "Percussion Spec": "사양 참조로 제품 불분명", "Jury Analysis": "분석 대상 불분명",
 "Lane Coach": "코칭 대상 불분명", "Walkthrough Habit": "결합 불성립",
 "Lawsuit Center": "센터 지칭으로 제품 불분명", "Divorce Kiosk": "키오스크 지칭으로 제품 불분명",
 "Custody Summary": "요약 지칭으로 제품 불분명", "Immigration Unit": "단위·부서 중의로 불분명",
 "Testament Signature": "서명 지칭으로 제품 불분명", "Notary Widget": "위젯 기능 지칭으로 제품 불분명",
 "Mediation Diagnostic": "진단 대상 불분명", "Trademark Time": "결합 불성립",
 "Patent Evaluation": "평가 대상 불분명", "Pool Workbook": "워크북 대상 불분명",
 "Surfing Workbook": "워크북 대상 불분명", "Tempo Mode": "기능 토글로 읽혀 제품 불분명",
 "Bandage Spec": "사양 참조로 제품 불분명", "Bankruptcy Quantity": "수량 대상 불분명",
 "Copyright Login": "제품 불분명", "Consolidation Analysis": "분석 대상 불분명",
 "Staging Coach": "코칭 대상 불분명", "Beneficiary Habit": "결합 불성립",
 "Migraine Converter": "변환 대상 불분명", "Insomnia Detector": "탐지 대상 불분명",
 "Skydiving Helper": "도우미 대상 불분명", "Acne Stage": "단계 대상 불분명",
 "Snowboarding Trend": "결합 불성립", "Eczema Comparison": "비교 대상 불분명",
 "Ziplining Record": "기록 대상 불분명", "Psoriasis Copy": "복사·원고 중의로 불분명",
 "Sledding Forecast": "예측 대상 불분명", "Vertigo Deadline": "결합 불성립",
 "Diving Diagnostic": "진단 대상 불분명", "Arthritis Progress": "진행 대상 불분명",
 "Menopause Rating": "평가 대상 불분명", "Rafting Account": "결합 불성립",
 "Pregnancy Case": "결합 불성립(Case 계열 기각 선례)", "Climbing Lookup": "탐색 대상 불분명",
 "Fertility Ping": "결합 불성립", "Biking Eligibility": "결합 불성립",
 "Thyroid Broadcast": "결합 불성립", "Golf Feedback": "결합 불성립",
 "Cholesterol Invoice": "결합 불성립", "Fishing Warranty": "결합 불성립",
 "Hypertension Deposit": "결합 불성립", "Camping Correction": "결합 불성립",
 "Anemia Revision": "결합 불성립", "Glamping Simulator": "결합 불성립",
 "Heartburn Predictor": "예측 대상 불분명", "Stargazing Recipe": "결합 불성립",
 "Birdwatching Expense": "결합 불성립", "Concussion Newsletter": "결합 불성립",
 "Canyon Claim": "결합 불성립", "Sprain Onboarding": "결합 불성립",
 "Geyser Checkin": "결합 불성립", "Fracture Size": "결합 불성립(속성 지칭)",
 "Fjord Length": "결합 불성립(속성 지칭)", "Insulin Weight": "결합 불성립(속성 지칭)",
 "Savanna Distance": "결합 불성립", "Tundra Range": "결합 불성립",
 "Prairie Limit": "결합 불성립", "Marsh Type": "결합 불성립(분류 대상 부자연)",
 "Cove Clock": "결합 불성립", "Cliff Time": "결합 불성립",
 "Cavern Speed": "결합 불성립", "Oasis Depth": "결합 불성립",
 "Dune Height": "결합 불성립", "Whale Width": "결합 불성립",
 "Dolphin Temperature": "결합 불성립", "Penguin Pressure": "결합 불성립",
 "Flamingo Load": "결합 불성립", "Turtle Voltage": "결합 불성립",
 "Moose Wattage": "결합 불성립", "Bison Brightness": "결합 불성립",
 "Reindeer Frequency": "결합 불성립", "Bid Workbook": "워크북 대상 불분명",
 "Fulfillment Mode": "기능 토글로 읽혀 제품 불분명", "Amenity Spec": "사양 참조로 제품 불분명",
 "Tuition Quantity": "수량 대상 불분명", "Downtime Login": "제품 불분명",
 "Crop Analysis": "분석 대상 불분명", "Fundraising Habit": "결합 불성립",
 "Content Mode": "기능 토글로 읽혀 제품 불분명", "Circulation Spec": "사양 참조로 제품 불분명",
 "Activation Login": "제품 불분명", "Patch Analysis": "분석 대상 불분명",
 "Configuration Coach": "코칭 대상 불분명", "Chat Habit": "결합 불성립",
 "Lawyer Outline": "개요 대상 불분명", "Attorney Template": "템플릿 대상 불분명",
 "Court Diary": "일지 대상 불분명", "Judge Cycle": "주기 지칭으로 제품 불분명",
 "Undercarriage Workbook": "워크북 대상 불분명", "Drainpipe Mode": "기능 토글로 읽혀 제품 불분명",
 "Tourist Spec": "사양 참조로 제품 불분명", "Percussion Quantity": "수량 대상 불분명",
 "Jury Coach": "코칭 대상 불분명", "Lane Habit": "결합 불성립",
 "Lawsuit Zone": "존 지칭으로 제품 불분명", "Divorce Bay": "베이 지칭으로 제품 불분명",
 "Testament Marker": "마커 기능 지칭으로 제품 불분명", "Notary Repository": "결합 불성립",
 "Mediation Progress": "진행 대상 불분명", "Guardianship Correction": "결합 불성립",
 "Trademark Speed": "결합 불성립", "Pool Workbook": "워크북 대상 불분명",
 "Surfing Mode": "기능 토글로 읽혀 제품 불분명", "Tempo Spec": "사양 참조로 제품 불분명",
 "Bandage Quantity": "수량 대상 불분명", "Bankruptcy Login": "제품 불분명",
 "Copyright Analysis": "분석 대상 불분명", "Consolidation Coach": "코칭 대상 불분명",
 "Staging Habit": "결합 불성립", "Migraine Generator": "생성 대상 불분명",
 "Insomnia Timer": "결합 불성립(Timer 계열 기각 선례)", "Skydiving Stage": "단계 대상 불분명",
 "Acne Result": "결과 지칭으로 제품 불분명", "Snowboarding Comparison": "비교 대상 불분명",
 "Eczema Proposal": "제안 대상 불분명", "Ziplining Copy": "복사·원고 중의로 불분명",
 "Psoriasis Reading": "독서·측정 중의로 불분명", "Sledding Deadline": "결합 불성립",
 "Vertigo Duration": "기간 속성 지칭으로 제품명 부자연", "Diving Progress": "진행 대상 불분명",
 "Arthritis Authorization": "결합 불성립", "Sailing Rating": "평가 대상 불분명",
 "Menopause Agreement": "결합 불성립", "Rafting Case": "결합 불성립(Case 계열 기각 선례)",
 "Pregnancy Match": "매칭 대상 불분명", "Climbing Ping": "결합 불성립",
 "Fertility Model": "모델 지칭으로 제품 불분명", "Biking Broadcast": "결합 불성립",
 "Thyroid Barcode": "결합 불성립", "Golf Invoice": "결합 불성립",
 "Cholesterol Renewal": "결합 불성립", "Fishing Deposit": "결합 불성립",
 "Hypertension Certification": "결합 불성립", "Camping Revision": "결합 불성립",
 "Anemia Payment": "결합 불성립", "Glamping Predictor": "예측 대상 불분명",
 "Heartburn Seal": "결합 불성립", "Birdwatching Newsletter": "결합 불성립",
 "Concussion Inventory": "결합 불성립", "Canyon Onboarding": "결합 불성립",
 "Sprain Checkin": "결합 불성립", "Geyser Size": "결합 불성립(속성 지칭)",
 "Fracture Length": "결합 불성립(속성 지칭)", "Fjord Weight": "결합 불성립(속성 지칭)",
 "Insulin Distance": "결합 불성립", "Savanna Range": "결합 불성립",
 "Tundra Limit": "결합 불성립", "Prairie Type": "결합 불성립(분류 대상 부자연)",
 "Marsh Clock": "결합 불성립", "Cove Time": "결합 불성립",
 "Cliff Speed": "결합 불성립", "Cavern Depth": "결합 불성립",
 "Oasis Height": "결합 불성립", "Dune Width": "결합 불성립",
 "Whale Temperature": "결합 불성립", "Dolphin Pressure": "결합 불성립",
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
out = base + r"\_dec_c7.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
