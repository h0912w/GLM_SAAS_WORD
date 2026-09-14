# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk21_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Curriculum App": (0.55, "교육과정 설계·관리 앱(실재)"),
 "Curriculum Tips": (0.55, "Curriculum App 승인 선례의 Tips 평행"),
 "Trombone App": (0.55, "트롬본 레슨·연습 앱(Trumpet App 평행)"),
 "Trombone Tips": (0.55, "Trombone App 승인 선례의 Tips 평행"),
 "Sedation App": (0.55, "진정·수면 마취 기록 관리 앱(Anesthesia App 평행)"),
 "Souvenir App": (0.55, "기념품 판매·재고 관리 앱(실재)"),
 "Patent Tracker": (0.55, "특허 절차 추적 관리(Tracker 절차 명사 선례 평행)"),
 "Testament Message": (0.55, "유언 전달 메시지 관리(Message 절차 명사 선례 평행)"),
 "Pregnancy Video": (0.55, "임신 관리 영상 가이드(Hypertension Video 평행)"),
 "Pregnancy Diary": (0.55, "임신 주차 기록 일지(실재)"),
 "Rafting Video": (0.55, "래프팅 강습 영상 가이드(Golf Video 평행)"),
 "Incident Tips": (0.55, "Incident App 승인 선례의 Tips 평행"),
 "Playtime Tips": (0.55, "Playtime App 승인 선례의 Tips 평행"),
}

R_DUP = {
 "Incident Advice": "직전 승인 Incident Tips와 동일 기능 의미 중복",
 "Conditioner Advice": "직전 승인 Conditioner Tips와 동일 기능 의미 중복",
 "Savings Advice": "직전 승인 Savings Tips와 동일 기능 의미 중복",
 "Fleet Advice": "직전 승인 Fleet Tips와 동일 기능 의미 중복",
}

R = {
 "Ductless Workbook": "워크북 대상 불분명", "Fob Mode": "기능 토글로 읽혀 제품 불분명",
 "Fence Spec": "사양 참조로 제품 불분명", "Hiking Quantity": "수량 대상 불분명",
 "Chord Login": "제품 불분명", "Test Analysis": "선례 기각(App 기각) 계열",
 "Foreclosure Coach": "코칭 대상 불분명", "Patent Habit": "결합 불성립",
 "Copyright Ledger": "장부 지칭으로 제품 불분명", "Migraine Authorization": "결합 불성립",
 "Insomnia Reply": "결합 불성립", "Skydiving Validation": "결합 불성립",
 "Acne Lookup": "탐색 대상 불분명", "Snowboarding Eligibility": "결합 불성립",
 "Eczema Broadcast": "결합 불성립", "Ziplining Feedback": "결합 불성립",
 "Psoriasis Invoice": "결합 불성립", "Sledding Warranty": "결합 불성립",
 "Vertigo Deposit": "결합 불성립", "Diving Correction": "결합 불성립",
 "Arthritis Revision": "결합 불성립", "Sailing Simulator": "결합 불성립",
 "Menopause Predictor": "예측 대상 불분명", "Rafting Recipe": "결합 불성립",
 "Climbing Expense": "결합 불성립", "Fertility Newsletter": "결합 불성립",
 "Biking Onboarding": "결합 불성립", "Thyroid Checkin": "결합 불성립",
 "Golf Weight": "결합 불성립(속성 지칭)", "Cholesterol Distance": "결합 불성립",
 "Fishing Type": "결합 불성립(분류 대상 부자연)", "Hypertension Clock": "결합 불성립",
 "Camping Depth": "결합 불성립", "Anemia Height": "결합 불성립",
 "Glamping Pressure": "결합 불성립", "Heartburn Load": "결합 불성립",
 "Stargazing Brightness": "결합 불성립", "Constipation Frequency": "결합 불성립",
 "Birdwatching Usage": "사용 지칭으로 제품 불분명", "Concussion Condition": "상태 명사로 제품명 부자연",
 "Canyon Episode": "결합 불성립", "Sprain Cycle": "주기 지칭으로 제품 불분명",
 "Geyser Breakdown": "내역·고장 중의로 불분명", "Fracture Sensor": "결합 불성립",
 "Fjord Reception": "리셉션·수신 중의로 불분명", "Insulin Followup": "후속 지칭으로 제품 불분명",
 "Savanna Approval": "승인 지칭으로 제품 불분명", "Tundra Matrix": "행렬·매트릭스 중의로 불분명",
 "Prairie Evaluation": "평가 대상 불분명", "Marsh Questionnaire": "설문 대상 불분명",
 "Cove Utilization": "활용 지칭으로 제품 불분명", "Cliff Benefit": "혜택 지칭으로 제품 불분명",
 "Cavern Requirement": "요건 지칭으로 제품 불분명", "Oasis Depreciation": "결합 불성립",
 "Dune Resignation": "결합 불성립", "Whale Hazard": "결합 불성립",
 "Dolphin Guarantor": "보증인 명사 결합 불성립", "Penguin Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Flamingo Tutorial": "동물 대상 결합 불성립", "Turtle Handbook": "동물 대상 결합 불성립",
 "Moose Timetable": "동물 대상 결합 불성립", "Bison Opinion": "동물 대상 결합 불성립",
 "Reindeer Gift": "결합 불성립", "Season Workbook": "선례 기각(App 기각) 계열",
 "Garment Spec": "사양 참조로 제품 불분명", "Membership Login": "제품 불분명",
 "Insurance Analysis": "분석 대상 불분명", "Customs Coach": "코칭 대상 불분명",
 "Blast Workbook": "선례 기각(App 기각) 계열", "Vent Mode": "기능 토글로 읽혀 제품 불분명",
 "Rekeying Spec": "사양 참조로 제품 불분명", "Rental Analysis": "분석 대상 불분명",
 "Officiant Coach": "코칭 대상 불분명", "Lawyer Guarantee": "결합 불성립",
 "Attorney Verification": "결합 불성립", "Court Compatibility": "상태 명사로 제품명 부자연",
 "Judge Workbook": "선례 기각(App 기각) 계열", "Forwarder Mode": "기능 토글로 읽혀 제품 불분명",
 "Showing Spec": "사양 참조로 제품 불분명", "Exclusion Quantity": "선례 기각(App 기각) 계열",
 "Withholding Login": "제품 불분명", "Roofing Analysis": "분석 대상 불분명",
 "Minor Coach": "선례 기각(App 기각) 계열", "Jury Deck": "갑판·카드 중의로 불분명",
 "Lawsuit Locator": "위치 탐색 대상 불분명", "Divorce Rate": "비율 지칭으로 제품 불분명",
 "Custody Recap": "요약 지칭으로 제품 불분명", "Immigration Format": "형식 지칭으로 제품 불분명",
 "Notary Volume": "결합 불성립", "Mediation Revision": "결합 불성립",
 "Guardianship Depth": "결합 불성립", "Trademark Requirement": "요건 지칭으로 제품 불분명",
 "Pickup Workbook": "워크북 대상 불분명", "Ductless Mode": "기능 토글로 읽혀 제품 불분명",
 "Fob Spec": "사양 참조로 제품 불분명", "Fence Quantity": "수량 대상 불분명",
 "Hiking Login": "제품 불분명", "Chord Analysis": "분석 대상 불분명",
 "Test Coach": "선례 기각(App 기각) 계열", "Foreclosure Habit": "결합 불성립",
 "Copyright Board": "이사회·게시판 중의로 불분명", "Migraine Template": "결합 불성립",
 "Insomnia Account": "결합 불성립", "Skydiving Lookup": "탐색 대상 불분명",
 "Acne Ping": "결합 불성립", "Snowboarding Broadcast": "결합 불성립",
 "Eczema Barcode": "결합 불성립", "Ziplining Invoice": "결합 불성립",
 "Psoriasis Renewal": "결합 불성립", "Sledding Deposit": "결합 불성립",
 "Vertigo Certification": "결합 불성립", "Diving Revision": "결합 불성립",
 "Arthritis Payment": "결합 불성립", "Sailing Predictor": "예측 대상 불분명",
 "Menopause Seal": "결합 불성립", "Climbing Newsletter": "결합 불성립",
 "Fertility Inventory": "결합 불성립", "Biking Checkin": "결합 불성립",
 "Thyroid Size": "결합 불성립(속성 지칭)", "Golf Distance": "결합 불성립",
 "Cholesterol Range": "결합 불성립", "Fishing Clock": "결합 불성립",
 "Hypertension Time": "결합 불성립", "Camping Height": "결합 불성립",
 "Anemia Width": "결합 불성립", "Glamping Load": "결합 불성립",
 "Heartburn Voltage": "결합 불성립", "Stargazing Frequency": "결합 불성립",
 "Constipation Compatibility": "상태 명사로 제품명 부자연", "Birdwatching Condition": "상태 명사로 제품명 부자연",
 "Concussion Humidity": "결합 불성립", "Canyon Cycle": "주기 지칭으로 제품 불분명",
 "Sprain Breakdown": "내역·고장 중의로 불분명", "Geyser Sensor": "결합 불성립",
 "Fracture Reception": "리셉션·수신 중의로 불분명", "Fjord Followup": "후속 지칭으로 제품 불분명",
 "Insulin Approval": "승인 지칭으로 제품 불분명", "Savanna Matrix": "행렬·매트릭스 중의로 불분명",
 "Tundra Evaluation": "평가 대상 불분명", "Prairie Questionnaire": "설문 대상 불분명",
 "Marsh Utilization": "활용 지칭으로 제품 불분명", "Cove Benefit": "혜택 지칭으로 제품 불분명",
 "Cliff Requirement": "요건 지칭으로 제품 불분명", "Cavern Depreciation": "결합 불성립",
 "Oasis Resignation": "결합 불성립", "Dune Hazard": "결합 불성립",
 "Whale Guarantor": "보증인 명사 결합 불성립", "Dolphin Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Penguin Tutorial": "동물 대상 결합 불성립", "Flamingo Handbook": "동물 대상 결합 불성립",
 "Turtle Timetable": "동물 대상 결합 불성립", "Moose Opinion": "동물 대상 결합 불성립",
 "Bison Gift": "결합 불성립", "Reindeer Retreat": "동물 대상 결합 불성립",
 "Season Mode": "선례 기각(App 기각) 계열", "Garment Quantity": "수량 대상 불분명",
 "Membership Analysis": "분석 대상 불분명", "Insurance Coach": "코칭 대상 불분명",
 "Customs Habit": "결합 불성립", "Fleet Workbook": "워크북 대상 불분명",
 "Blast Mode": "선례 기각(App 기각) 계열", "Vent Spec": "사양 참조로 제품 불분명",
 "Rekeying Quantity": "수량 대상 불분명", "Rental Coach": "코칭 대상 불분명",
 "Officiant Habit": "결합 불성립", "Lawyer Record": "기록 대상 불분명",
 "Attorney Simulator": "결합 불성립", "Court Capacity": "상태 명사로 제품명 부자연",
 "Savings Workbook": "워크북 대상 불분명", "Judge Mode": "선례 기각(App 기각) 계열",
 "Forwarder Spec": "사양 참조로 제품 불분명", "Showing Quantity": "수량 대상 불분명",
 "Exclusion Login": "선례 기각(App 기각) 계열", "Withholding Analysis": "분석 대상 불분명",
 "Roofing Coach": "코칭 대상 불분명", "Minor Habit": "선례 기각(App 기각) 계열",
 "Jury Studio": "스튜디오 중의로 불분명", "Lawsuit Finder": "탐색 대상 불분명",
 "Divorce Update": "업데이트 지칭으로 제품 불분명", "Custody Entry": "항목·입장 중의로 불분명",
 "Immigration Serial": "일련번호 지칭으로 제품 불분명", "Testament Total": "합계 지칭으로 제품 불분명",
 "Notary Diagnostic": "진단 대상 불분명",
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
out = base + r"\_dec_c22.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
