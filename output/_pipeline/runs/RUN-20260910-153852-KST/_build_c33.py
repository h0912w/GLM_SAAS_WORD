# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk32_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Checkin App": (0.55, "행사·투숙 체크인 관리 앱(실재)"),
 "Checkin Tips": (0.55, "Checkin App 승인 선례의 Tips 평행"),
 "Transcript Tips": (0.55, "Transcript App 승인 선례의 Tips 평행"),
 "Cargo Tips": (0.55, "Cargo App 승인 선례의 Tips 평행"),
 "Livestream Tips": (0.55, "Livestream App 승인 선례의 Tips 평행"),
 "Thumbnail Tips": (0.55, "Thumbnail App 승인 선례의 Tips 평행"),
 "Skillset App": (0.55, "보유 역량 평가·관리 앱(Assessment App 평행)"),
 "Skillset Tips": (0.55, "Skillset App 승인 선례의 Tips 평행"),
 "Transponder App": (0.55, "통행료 트랜스폰더 관리 앱(실재)"),
 "Transponder Tips": (0.55, "Transponder App 승인 선례의 Tips 평행"),
 "Return App": (0.55, "상품 반품 처리 관리 앱(실재)"),
 "Channel App": (0.55, "판매·파트너 채널 관리 앱(실재)"),
 "Chiller App": (0.55, "냉각 설비 점검·관리 앱(실재)"),
 "Insulin App": (0.55, "인슐린 투여 기록 관리 앱(Sedation App 평행)"),
 "Insulin Tips": (0.55, "Insulin App 승인 선례의 Tips 평행"),
 "Immigration Manual": (0.55, "이민 절차 안내 매뉴얼(Patent Handbook 평행)"),
 "Snowboarding Diary": (0.55, "스노보드 기록 일지(Rafting Diary 평행)"),
}

R_DUP = {
 "Transcript Advice": "이번 배치 승인 Transcript Tips와 동일 기능 의미 중복",
 "Defect Advice": "직전 승인 Defect Tips와 동일 기능 의미 중복",
 "Churn Advice": "직전 승인 Churn Tips와 동일 기능 의미 중복",
 "Cargo Advice": "이번 배치 승인 Cargo Tips와 동일 기능 의미 중복",
 "Livestream Advice": "이번 배치 승인 Livestream Tips와 동일 기능 의미 중복",
 "Tuneup Advice": "직전 승인 Tuneup Tips와 동일 기능 의미 중복",
 "Thumbnail Advice": "이번 배치 승인 Thumbnail Tips와 동일 기능 의미 중복",
}

R = {
 "Biking Frequency": "결합 불성립", "Thyroid Compatibility": "상태 명사로 제품명 부자연",
 "Golf Condition": "상태 명사로 제품명 부자연", "Cholesterol Humidity": "결합 불성립",
 "Fishing Breakdown": "내역·고장 중의로 불분명", "Hypertension Sensor": "결합 불성립",
 "Camping Approval": "승인 지칭으로 제품 불분명", "Anemia Matrix": "행렬·매트릭스 중의로 불분명",
 "Glamping Utilization": "활용 지칭으로 제품 불분명", "Heartburn Benefit": "혜택 지칭으로 제품 불분명",
 "Stargazing Resignation": "결합 불성립", "Constipation Hazard": "결합 불성립",
 "Birdwatching Tutorial": "terrain 대상 결합 불성립", "Concussion Handbook": "terrain 대상 결합 불성립",
 "Canyon Opinion": "terrain 대상 결합 불성립", "Sprain Gift": "결합 불성립",
 "Geyser Retreat": "terrain 대상 결합 불성립", "Fracture Tournament": "terrain 대상 결합 불성립",
 "Fjord Flyer": "terrain 대상 결합 불성립", "Savanna Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Tundra Advice": "선례 기각(App 기각) 계열", "Prairie Workbook": "선례 기각(App 기각) 계열",
 "Marsh Mode": "선례 기각(App 기각) 계열", "Cove Spec": "선례 기각(App 기각) 계열",
 "Cliff Quantity": "선례 기각(App 기각) 계열", "Cavern Login": "선례 기각(App 기각) 계열",
 "Oasis Analysis": "선례 기각(App 기각) 계열", "Dune Coach": "선례 기각(App 기각) 계열",
 "Whale Habit": "선례 기각(App 기각) 계열", "Dolphin Tracker": "선례 기각(App 기각) 계열",
 "Penguin Flow": "선례 기각(App 기각) 계열", "Flamingo Hub": "선례 기각(App 기각) 계열",
 "Turtle Desk": "선례 기각(App 기각) 계열", "Moose Radar": "선례 기각(App 기각) 계열",
 "Bison Relay": "선례 기각(App 기각) 계열", "Reindeer Vault": "선례 기각(App 기각) 계열",
 "Yield Workbook": "선례 기각(App 기각) 계열", "Consumption Mode": "기능 토글로 읽혀 제품 불분명",
 "Campaign Spec": "사양 참조로 제품 불분명", "Attribution Login": "제품 불분명",
 "Syndication Analysis": "분석 대상 불분명", "Bandwidth Habit": "선례 기각(App 기각) 계열",
 "Rights App": "권리 대상 불분명", "Churn Advice2": "",
 "Firewall Workbook": "워크북 대상 불분명", "Migration Mode": "선례 기각(App 기각) 계열",
 "Knowledge Spec": "사양 참조로 제품 불분명", "Assessment Quantity": "수량 대상 불분명",
 "Catering Login": "제품 불분명", "Lawyer Lookup": "탐색 대상 불분명",
 "Attorney Type": "결합 불성립(분류 대상 부자연)", "Court Guarantor": "보증인 명사 결합 불성립",
 "Tuneup Advice2": "", "Server Workbook": "워크북 대상 불분명",
 "Spay Mode": "기능 토글로 읽혀 제품 불분명", "Braces Spec": "사양 참조로 제품 불분명",
 "Snack Quantity": "수량 대상 불분명", "Curtain Login": "제품 불분명",
 "Facial Analysis": "분석 대상 불분명", "Tablet Coach": "선례 기각(App 기각) 계열",
 "Freon Habit": "선례 기각(App 상표 기각) 계열", "Judge Watch": "선례 기각(App 기각) 계열(Watch 중의)",
 "Jury Engine": "엔진 지칭으로 제품 불분명", "Lawsuit Form": "서식 대상 불분명(Divorce Draft 기각 평행)",
 "Divorce Badge": "배지 지칭으로 제품 불분명", "Custody Stake": "지분·말뚝 중의로 불분명",
 "Testament Comparison": "비교 대상 불분명(Comparison 기각 라인)", "Notary Feedback": "결합 불성립",
 "Mediation Range": "결합 불성립", "Fjord App": "지명 지칭으로 제품 불분명",
 "Insulin Tips2": "", "Savanna Advice": "선례 기각(App 기각) 계열",
 "Tundra Workbook": "선례 기각(App 기각) 계열", "Prairie Mode": "선례 기각(App 기각) 계열",
 "Marsh Spec": "선례 기각(App 기각) 계열", "Cove Quantity": "선례 기각(App 기각) 계열",
 "Cliff Login": "선례 기각(App 기각) 계열", "Cavern Analysis": "선례 기각(App 기각) 계열",
 "Oasis Coach": "선례 기각(App 기각) 계열", "Dune Habit": "선례 기각(App 기각) 계열",
 "Whale Tracker": "선례 기각(App 기각) 계열", "Dolphin Flow": "선례 기각(App 기각) 계열",
 "Penguin Hub": "선례 기각(App 기각) 계열", "Flamingo Desk": "선례 기각(App 기각) 계열",
 "Turtle Radar": "선례 기각(App 기각) 계열", "Moose Relay": "선례 기각(App 기각) 계열",
 "Bison Vault": "선례 기각(App 기각) 계열", "Reindeer Compass": "선례 기각(App 기각) 계열",
 "Migraine Warranty": "결합 불성립", "Insomnia Revision": "결합 불성립",
 "Skydiving Predictor": "예측 대상 불분명", "Acne Seal": "결합 불성립",
 "Eczema Refund": "결합 불성립", "Ziplining Inventory": "결합 불성립",
 "Psoriasis Claim": "결합 불성립", "Sledding Size": "결합 불성립(속성 지칭)",
 "Vertigo Length": "결합 불성립(속성 지칭)", "Diving Range": "결합 불성립",
 "Arthritis Limit": "결합 불성립", "Sailing Time": "결합 불성립",
 "Menopause Speed": "결합 불성립", "Rafting Width": "결합 불성립",
 "Pregnancy Temperature": "결합 불성립", "Climbing Voltage": "결합 불성립",
 "Fertility Wattage": "결합 불성립", "Biking Compatibility": "상태 명사로 제품명 부자연",
 "Thyroid Capacity": "상태 명사로 제품명 부자연", "Golf Humidity": "결합 불성립",
 "Cholesterol Episode": "결합 불성립", "Fishing Sensor": "결합 불성립",
 "Hypertension Reception": "리셉션·수신 중의로 불분명", "Camping Matrix": "행렬·매트릭스 중의로 불분명",
 "Anemia Evaluation": "평가 대상 불분명", "Glamping Benefit": "혜택 지칭으로 제품 불분명",
 "Heartburn Requirement": "요건 지칭으로 제품 불분명", "Stargazing Hazard": "결합 불성립",
 "Constipation Guarantor": "보증인 명사 결합 불성립", "Birdwatching Handbook": "terrain 대상 결합 불성립",
 "Concussion Timetable": "terrain 대상 결합 불성립", "Canyon Gift": "결합 불성립",
 "Sprain Retreat": "terrain 대상 결합 불성립", "Geyser Tournament": "terrain 대상 결합 불성립",
 "Fracture Flyer": "terrain 대상 결합 불성립", "Rights Tips": "선례 기각(App 기각)의 Tips 평행 불가",
 "Defect Workbook": "워크북 대상 불분명", "Yield Mode": "선례 기각(App 기각) 계열",
 "Consumption Spec": "사양 참조로 제품 불분명", "Campaign Quantity": "수량 대상 불분명",
 "Attribution Analysis": "분석 대상 불분명", "Syndication Coach": "코칭 대상 불분명",
 "Segment App2": "", "Cargo Advice2": "",
 "Churn Workbook": "워크북 대상 불분명", "Firewall Mode": "기능 토글로 읽혀 제품 불분명",
 "Migration Spec": "선례 기각(App 기각) 계열", "Knowledge Quantity": "수량 대상 불분명",
 "Assessment Login": "제품 불분명", "Catering Analysis": "분석 대상 불분명",
 "Lawyer Ping": "결합 불성립", "Attorney Clock": "결합 불성립",
 "Court Tuner": "튜너 기능 지칭으로 제품 불분명", "Channel App2": "",
 "Livestream Advice2": "", "Tuneup Workbook": "워크북 대상 불분명",
 "Server Mode": "기능 토글로 읽혀 제품 불분명", "Spay Spec": "사양 참조로 제품 불분명",
 "Braces Quantity": "수량 대상 불분명", "Snack Login": "제품 불분명",
 "Curtain Analysis": "분석 대상 불분명", "Facial Coach": "코칭 대상 불분명",
 "Tablet Habit": "선례 기각(App 기각) 계열", "Judge Scope": "선례 기각(App 기각) 계열(Scope 기능 지칭)",
 "Jury Assistant": "조수 지칭으로 제품 불분명(Assistant 기각 라인)", "Lawsuit Card": "카드(신용·명함) 중의로 불분명",
 "Divorce Stub": "잔단·티어 중의로 불분명", "Custody Margin": "마진·여백 중의로 불분명",
 "Immigration Worksheet": "워크시트 대상 불분명(Workbook 계열)", "Testament Proposal": "제안서 대상 불분명(proposal 기각 라인)",
 "Notary Invoice": "결합 불성립", "Mediation Limit": "결합 불성립",
 "Guardianship Matrix": "행렬·매트릭스 중의로 불분명", "Chiller App2": "",
 "Hallway Advice": "선례 기각(App 기각) 계열", "Barbecue Mode": "기능 토글로 읽혀 제품 불분명",
 "Theory Spec": "선례 기각(App 기각) 계열", "Visit Quantity": "수량 대상 불분명",
 "Installment Login": "제품 불분명", "Trademark Analysis": "분석 대상 불분명",
 "Crossdock Coach": "코칭 대상 불분명", "Valuation Habit": "결합 불성립",
 "Patent Base": "기반 지칭으로 제품 불분명(Base 기각 라인)",
 "Segment App": "고객 데이터 플랫폼 상표(Segment) 중의로 불분명",
 "Guardianship Approval": "승인 지칭으로 제품 불분명",
 "Barbecue Workbook": "워크북 대상 불분명",
 "Hallway Workbook": "워크북 대상 불분명",
 "Theory Mode": "선례 기각(App 기각) 계열",
 "Visit Spec": "사양 참조로 제품 불분명",
 "Installment Quantity": "수량 대상 불분명",
 "Trademark Login": "제품 불분명",
 "Crossdock Analysis": "분석 대상 불분명",
 "Valuation Coach": "코칭 대상 불분명",
 "Broker Habit": "결합 불성립",
 "Patent Frame": "프레임(액자·구조) 중의로 불분명",
 "Copyright Manager": "관리자 지칭으로 제품 불분명(Manager 기각 라인)",
}
del R["Churn Advice2"]
del R["Tuneup Advice2"]
del R["Insulin Tips2"]
del R["Segment App2"]
del R["Cargo Advice2"]
del R["Channel App2"]
del R["Livestream Advice2"]
del R["Chiller App2"]
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
