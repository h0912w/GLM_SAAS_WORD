# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk33_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Subcontractor App": (0.55, "하도급 업체 계약·관리 앱(실재)"),
 "Subcontractor Tips": (0.55, "Subcontractor App 승인 선례의 Tips 평행"),
 "Podcast App": (0.55, "팟캐스트 제작·배포 관리 앱(실재)"),
 "Podcast Tips": (0.55, "Podcast App 승인 선례의 Tips 평행"),
 "Refrigeration App": (0.55, "냉장 설비 점검·관리 앱(실재)"),
 "Roster App": (0.55, "근무표·명단 관리 앱(실재)"),
 "Outreach App": (0.55, "영업 아웃리치 관리 앱(실재)"),
 "Return Tips": (0.55, "Return App 승인 선례의 Tips 평행"),
 "Chiller Tips": (0.55, "Chiller App 승인 선례의 Tips 평행"),
 "Channel Tips": (0.55, "Channel App 승인 선례의 Tips 평행"),
 "Court Tutorial": (0.55, "법원 절차 안내 튜토리얼(Immigration Manual 평행)"),
 "Court Handbook": (0.55, "법원 절차 안내 핸드북(Patent Handbook 평행)"),
}

R_DUP = {
 "Checkin Advice": "이번 배치 승인 Checkin Tips와 동일 기능 의미 중복",
 "Skillset Advice": "이번 배치 승인 Skillset Tips와 동일 기능 의미 중복",
 "Transponder Advice": "이번 배치 승인 Transponder Tips와 동일 기능 의미 중복",
 "Return Advice": "이번 배치 승인 Return Tips와 동일 기능 의미 중복",
 "Channel Advice": "이번 배치 승인 Channel Tips와 동일 기능 의미 중복",
 "Insulin Advice": "이번 배치 승인 Insulin Tips와 동일 기능 의미 중복",
}

R = {
 "Copyright Engine": "엔진 지칭으로 제품 불분명", "Migraine Deposit": "결합 불성립",
 "Insomnia Payment": "결합 불성립", "Skydiving Seal": "결합 불성립",
 "Acne Review": "리뷰 대상 불분명", "Snowboarding Refund": "결합 불성립",
 "Eczema Expense": "결합 불성립", "Ziplining Claim": "결합 불성립",
 "Psoriasis Onboarding": "결합 불성립", "Sledding Length": "결합 불성립(속성 지칭)",
 "Vertigo Weight": "결합 불성립(속성 지칭)", "Diving Limit": "결합 불성립",
 "Arthritis Type": "결합 불성립(분류 대상 부자연)", "Sailing Speed": "결합 불성립",
 "Menopause Depth": "결합 불성립", "Rafting Temperature": "결합 불성립",
 "Pregnancy Pressure": "결합 불성립", "Climbing Wattage": "결합 불성립",
 "Fertility Brightness": "결합 불성립", "Biking Capacity": "상태 명사로 제품명 부자연",
 "Thyroid Usage": "사용 지칭으로 제품 불분명", "Golf Episode": "결합 불성립",
 "Cholesterol Cycle": "주기 지칭으로 제품 불분명", "Fishing Reception": "리셉션·수신 중의로 불분명",
 "Hypertension Followup": "후속 지칭으로 제품 불분명", "Camping Evaluation": "평가 대상 불분명",
 "Anemia Questionnaire": "설문 대상 불분명", "Glamping Requirement": "요건 지칭으로 제품 불분명",
 "Heartburn Depreciation": "결합 불성립", "Stargazing Guarantor": "보증인 명사 결합 불성립",
 "Constipation Tuner": "튜너 기능 지칭으로 제품 불분명", "Birdwatching Timetable": "terrain 대상 결합 불성립",
 "Concussion Opinion": "소견 대상 불분명", "Canyon Retreat": "terrain 대상 결합 불성립",
 "Sprain Tournament": "terrain 대상 결합 불성립", "Geyser Flyer": "terrain 대상 결합 불성립",
 "Fracture App": "골절 상태 지칭으로 용도 불분명", "Fjord Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Savanna Workbook": "선례 기각(App 기각) 계열", "Tundra Mode": "선례 기각(App 기각) 계열",
 "Prairie Spec": "선례 기각(App 기각) 계열", "Marsh Quantity": "선례 기각(App 기각) 계열",
 "Cove Login": "선례 기각(App 기각) 계열", "Cliff Analysis": "선례 기각(App 기각) 계열",
 "Cavern Coach": "선례 기각(App 기각) 계열", "Oasis Habit": "선례 기각(App 기각) 계열",
 "Dune Tracker": "선례 기각(App 기각) 계열", "Whale Flow": "선례 기각(App 기각) 계열",
 "Dolphin Hub": "선례 기각(App 기각) 계열", "Penguin Desk": "선례 기각(App 기각) 계열",
 "Flamingo Radar": "선례 기각(App 기각) 계열", "Turtle Relay": "선례 기각(App 기각) 계열",
 "Moose Vault": "선례 기각(App 기각) 계열", "Bison Compass": "선례 기각(App 기각) 계열",
 "Reindeer Beacon": "선례 기각(App 기각) 계열", "Transcript Workbook": "워크북 대상 불분명",
 "Defect Mode": "기능 토글로 읽혀 제품 불분명", "Yield Spec": "선례 기각(App 기각) 계열",
 "Consumption Quantity": "수량 대상 불분명", "Campaign Login": "제품 불분명",
 "Attribution Coach": "코칭 대상 불분명", "Syndication Habit": "결합 불성립",
 "Segment Tips": "선례 기각(App 상표 기각)의 Tips 평행 불가", "Rights Advice": "선례 기각(App 기각) 계열",
 "Cargo Workbook": "워크북 대상 불분명", "Churn Mode": "기능 토글로 읽혀 제품 불분명",
 "Firewall Spec": "사양 참조로 제품 불분명", "Migration Quantity": "선례 기각(App 기각) 계열",
 "Knowledge Login": "제품 불분명", "Assessment Analysis": "분석 대상 불분명",
 "Catering Coach": "코칭 대상 불분명", "Lawyer Model": "모델(모범·모델링) 중의로 불분명",
 "Attorney Time": "결합 불성립", "Jury Planner": "계획 대상 불분명",
 "Lawsuit Sheet": "시트 대상 불분명(Worksheet 계열)", "Divorce Statement": "진술·명세 중의로 불분명",
 "Custody Fine": "벌금·형용사 중의로 불분명", "Immigration Diagram": "도식 지칭으로 제품 불분명",
 "Testament Guarantee": "보증 결합 불성립", "Notary Renewal": "갱신 대상 불분명",
 "Mediation Type": "결합 불성립(분류 대상 부자연)", "Guardianship Evaluation": "평가 대상 불분명",
 "Thumbnail Workbook": "워크북 대상 불분명", "Hallway Mode": "선례 기각(App 기각) 계열",
 "Barbecue Spec": "사양 참조로 제품 불분명", "Theory Quantity": "선례 기각(App 기각) 계열",
 "Visit Login": "제품 불분명", "Installment Analysis": "분석 대상 불분명",
 "Trademark Coach": "코칭 대상 불분명", "Crossdock Habit": "결합 불성립",
 "Patent Core": "핵심 지칭으로 제품 불분명(Core 기각 라인)", "Copyright Assistant": "조수 지칭으로 제품 불분명(Assistant 기각 라인)",
 "Migraine Certification": "결합 불성립", "Insomnia Verification": "결합 불성립",
 "Skydiving Review": "리뷰 대상 불분명", "Acne Recipe": "결합 불성립",
 "Snowboarding Expense": "결합 불성립", "Eczema Newsletter": "결합 불성립",
 "Ziplining Onboarding": "결합 불성립", "Psoriasis Checkin": "결합 불성립",
 "Sledding Weight": "결합 불성립(속성 지칭)", "Vertigo Distance": "결합 불성립",
 "Diving Type": "결합 불성립(분류 대상 부자연)", "Arthritis Clock": "결합 불성립",
 "Sailing Depth": "결합 불성립", "Menopause Height": "결합 불성립",
 "Rafting Pressure": "결합 불성립", "Pregnancy Load": "결합 불성립",
 "Climbing Brightness": "결합 불성립", "Fertility Frequency": "결합 불성립",
 "Biking Usage": "사용 지칭으로 제품 불분명", "Thyroid Condition": "상태 명사로 제품명 부자연",
 "Golf Cycle": "주기 지칭으로 제품 불분명", "Cholesterol Breakdown": "내역·고장 중의로 불분명",
 "Fishing Followup": "후속 지칭으로 제품 불분명", "Hypertension Approval": "승인 지칭으로 제품 불분명",
 "Camping Questionnaire": "설문 대상 불분명", "Anemia Utilization": "활용 지칭으로 제품 불분명",
 "Glamping Depreciation": "결합 불성립", "Heartburn Resignation": "결합 불성립",
 "Stargazing Tuner": "튜너 기능 지칭으로 제품 불분명", "Constipation Tutorial": "terrain 대상 결합 불성립",
 "Birdwatching Opinion": "terrain 대상 결합 불성립", "Concussion Gift": "결합 불성립",
 "Canyon Tournament": "terrain 대상 결합 불성립", "Sprain Flyer": "terrain 대상 결합 불성립",
 "Geyser App": "지형 지칭으로 제품 불분명", "Fracture Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Fjord Advice": "선례 기각(App 기각) 계열", "Insulin Workbook": "워크북 대상 불분명",
 "Savanna Mode": "선례 기각(App 기각) 계열", "Tundra Spec": "선례 기각(App 기각) 계열",
 "Prairie Quantity": "선례 기각(App 기각) 계열", "Marsh Login": "선례 기각(App 기각) 계열",
 "Cove Analysis": "선례 기각(App 기각) 계열", "Cliff Coach": "선례 기각(App 기각) 계열",
 "Cavern Habit": "선례 기각(App 기각) 계열", "Oasis Tracker": "선례 기각(App 기각) 계열",
 "Dune Flow": "선례 기각(App 기각) 계열", "Whale Hub": "선례 기각(App 기각) 계열",
 "Dolphin Desk": "선례 기각(App 기각) 계열", "Penguin Radar": "선례 기각(App 기각) 계열",
 "Flamingo Relay": "선례 기각(App 기각) 계열", "Turtle Vault": "선례 기각(App 기각) 계열",
 "Moose Compass": "선례 기각(App 기각) 계열", "Bison Beacon": "선례 기각(App 기각) 계열",
 "Reindeer Forge": "선례 기각(App 기각) 계열", "Checkin Workbook": "워크북 대상 불분명",
 "Transcript Mode": "기능 토글로 읽혀 제품 불분명", "Defect Spec": "사양 참조로 제품 불분명",
 "Yield Quantity": "선례 기각(App 기각) 계열", "Consumption Login": "제품 불분명",
 "Campaign Analysis": "분석 대상 불분명", "Attribution Habit": "결합 불성립",
 "Segment Advice": "선례 기각(App 상표 기각) 계열", "Rights Workbook": "선례 기각(App 기각) 계열",
 "Cargo Mode": "기능 토글로 읽혀 제품 불분명", "Churn Spec": "사양 참조로 제품 불분명",
 "Firewall Quantity": "수량 대상 불분명", "Migration Login": "선례 기각(App 기각) 계열",
 "Knowledge Analysis": "분석 대상 불분명", "Assessment Coach": "코칭 대상 불분명",
 "Catering Habit": "결합 불성립", "Lawyer Availability": "가용성 속성 결합 불성립",
 "Attorney Speed": "결합 불성립", "Judge Loop": "선례 기각(App 기각) 계열(Loop 기각 선례)",
 "Skillset Workbook": "워크북 대상 불분명", "Livestream Mode": "기능 토글로 읽혀 제품 불분명",
 "Tuneup Spec": "사양 참조로 제품 불분명", "Server Quantity": "수량 대상 불분명",
 "Spay Login": "제품 불분명", "Braces Analysis": "분석 대상 불분명",
 "Snack Coach": "코칭 대상 불분명", "Curtain Habit": "결합 불성립",
 "Livestream Workbook": "워크북 대상 불분명", "Tuneup Mode": "기능 토글로 읽혀 제품 불분명",
 "Server Spec": "사양 참조로 제품 불분명", "Spay Quantity": "수량 대상 불분명",
 "Braces Login": "제품 불분명", "Snack Analysis": "분석 대상 불분명",
 "Curtain Coach": "코칭 대상 불분명", "Facial Habit": "결합 불성립",
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
out = base + r"\_dec_c34.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
