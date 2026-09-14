# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk19_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Vent App": (0.55, "배기·환기 덕트 점검 관리 앱(실재)"),
 "Vent Tips": (0.55, "Vent App 승인 선례의 Tips 평행"),
 "Forwarder App": (0.55, "운송주선(포워더) 화물 관리 앱(실재)"),
 "Forwarder Tips": (0.55, "Forwarder App 승인 선례의 Tips 평행"),
 "Ductless App": (0.55, "덕트리스 에어컨 시공·관리 앱(실재)"),
 "Ductless Tips": (0.55, "Ductless App 승인 선례의 Tips 평행"),
 "Pickup App": (0.55, "수거·픽업 예약 관리 앱(실재)"),
 "Garment Tips": (0.55, "Garment App 승인 선례의 Tips 평행"),
 "Rekeying Tips": (0.55, "Rekeying App 승인 선례의 Tips 평행"),
 "Showing Tips": (0.55, "Showing App 승인 선례의 Tips 평행"),
 "Fob Tips": (0.55, "Fob App 승인 선례의 Tips 평행"),
 "Fertility Video": (0.55, "가임기 관리 영상 가이드(Hypertension Video 평행)"),
 "Climbing Video": (0.55, "클라이밍 기술 영상 가이드(Golf Video 평행)"),
 "Fertility Diary": (0.55, "배란·가임 기록 일지(실재)"),
 "Insomnia Guide": (0.55, "불면 개선 가이드 콘텐츠(Eczema Guide 평행)"),
 "Testament Notification": (0.55, "유언 관련 통지 관리(Notary Notification 평행)"),
}

R_DUP = {
 "Garment Advice": "직전 승인 Garment Tips와 동일 기능 의미 중복",
 "Fence Advice": "직전 승인 Fence Tips와 동일 기능 의미 중복",
 "Rekeying Advice": "직전 승인 Rekeying Tips와 동일 기능 의미 중복",
 "Showing Advice": "이번 배치 승인 Showing Tips와 동일 기능 의미 중복",
 "Fob Advice": "직전 승인 Fob Tips와 동일 기능 의미 중복",
}

R = {
 "Sledding Feedback": "결합 불성립", "Vertigo Invoice": "결합 불성립",
 "Diving Warranty": "결합 불성립", "Arthritis Deposit": "결합 불성립",
 "Sailing Correction": "결합 불성립", "Menopause Revision": "결합 불성립",
 "Rafting Simulator": "결합 불성립", "Pregnancy Predictor": "예측 대상 불분명",
 "Climbing Recipe": "결합 불성립", "Biking Expense": "결합 불성립",
 "Thyroid Newsletter": "결합 불성립", "Golf Onboarding": "결합 불성립",
 "Cholesterol Checkin": "결합 불성립", "Fishing Weight": "결합 불성립(속성 지칭)",
 "Hypertension Distance": "결합 불성립", "Camping Type": "결합 불성립(분류 대상 부자연)",
 "Anemia Clock": "결합 불성립", "Glamping Depth": "결합 불성립",
 "Heartburn Height": "결합 불성립", "Stargazing Pressure": "결합 불성립",
 "Constipation Load": "결합 불성립", "Birdwatching Brightness": "결합 불성립",
 "Concussion Frequency": "결합 불성립", "Canyon Capacity": "상태 명사로 제품명 부자연",
 "Sprain Usage": "사용 지칭으로 제품 불분명", "Geyser Condition": "상태 명사로 제품명 부자연",
 "Fracture Humidity": "결합 불성립", "Fjord Episode": "결합 불성립",
 "Insulin Cycle": "주기 지칭으로 제품 불분명", "Savanna Breakdown": "내역·고장 중의로 불분명",
 "Tundra Sensor": "결합 불성립", "Prairie Reception": "리셉션·수신 중의로 불분명",
 "Marsh Followup": "후속 지칭으로 제품 불분명", "Cove Approval": "승인 지칭으로 제품 불분명",
 "Cliff Matrix": "행렬·매트릭스 중의로 불분명", "Cavern Evaluation": "평가 대상 불분명",
 "Oasis Questionnaire": "설문 대상 불분명", "Dune Utilization": "활용 지칭으로 제품 불분명",
 "Whale Benefit": "혜택 지칭으로 제품 불분명", "Dolphin Requirement": "요건 지칭으로 제품 불분명",
 "Penguin Depreciation": "결합 불성립", "Flamingo Resignation": "결합 불성립",
 "Turtle Hazard": "결합 불성립", "Moose Guarantor": "보증인 명사 결합 불성립",
 "Bison Tuner": "튜너 기능 지칭으로 제품 불분명", "Reindeer Tutorial": "동물 대상 결합 불성립",
 "Membership Workbook": "워크북 대상 불분명", "Insurance Mode": "기능 토글로 읽혀 제품 불분명",
 "Customs Spec": "사양 참조로 제품 불분명", "Safety Login": "제품 불분명",
 "Ductwork Analysis": "분석 대상 불분명", "Lockout Coach": "코칭 대상 불분명",
 "Turnaround Habit": "결합 불성립", "Rental Mode": "기능 토글로 읽혀 제품 불분명",
 "Officiant Spec": "사양 참조로 제품 불분명", "Scratch Analysis": "선례 기각(App 기각) 계열",
 "Wrench Coach": "코칭 대상 불분명", "Attraction Habit": "결합 불성립",
 "Lawyer Rank": "순위 대상 불분명", "Attorney Nomination": "결합 불성립",
 "Court Voltage": "결합 불성립", "Judge Flyer": "전단 중의로 불분명",
 "Season App": "계절 지칭으로 제품 불분명", "Exclusion Advice": "선례 기각(App 기각)의 Advice 불가",
 "Withholding Workbook": "워크북 대상 불분명", "Roofing Mode": "기능 토글로 읽혀 제품 불분명",
 "Minor Spec": "선례 기각(App 기각) 계열", "Video Login": "제품 불분명",
 "Survey Analysis": "분석 대상 불분명", "Cover Coach": "코칭 대상 불분명",
 "Recording Habit": "결합 불성립", "Jury Base": "기반 지칭으로 제품 불분명",
 "Lawsuit Journal": "일지 대상 불분명", "Divorce View": "조회 지칭으로 제품 불분명",
 "Custody Circular": "공문·순환 중의로 불분명", "Immigration Identifier": "식별자 지칭으로 제품 불분명",
 "Testament Rendering": "렌더링 지칭으로 제품 불분명", "Notary Reference": "참조 대상 불분명",
 "Mediation Deposit": "결합 불성립", "Guardianship Type": "결합 불성립(분류 대상 부자연)",
 "Trademark Evaluation": "평가 대상 불분명", "Hiking Workbook": "워크북 대상 불분명",
 "Chord Mode": "기능 토글로 읽혀 제품 불분명", "Test Spec": "선례 기각(App 기각) 계열",
 "Foreclosure Quantity": "수량 대상 불분명", "Patent Login": "제품 불분명",
 "Drayage Analysis": "분석 대상 불분명", "Realtor Coach": "코칭 대상 불분명",
 "Carrier Habit": "결합 불성립", "Copyright Frame": "액자·틀 중의로 불분명",
 "Migraine Volume": "결합 불성립", "Skydiving Account": "결합 불성립",
 "Acne Case": "결합 불성립(Case 계열 기각 선례)", "Snowboarding Ping": "결합 불성립",
 "Eczema Model": "모델 지칭으로 제품 불분명", "Ziplining Broadcast": "결합 불성립",
 "Psoriasis Barcode": "결합 불성립", "Sledding Invoice": "결합 불성립",
 "Vertigo Renewal": "결합 불성립", "Diving Deposit": "결합 불성립",
 "Arthritis Certification": "결합 불성립", "Sailing Revision": "결합 불성립",
 "Menopause Payment": "결합 불성립", "Rafting Predictor": "예측 대상 불분명",
 "Pregnancy Seal": "결합 불성립", "Biking Newsletter": "결합 불성립",
 "Thyroid Inventory": "결합 불성립", "Golf Checkin": "결합 불성립",
 "Cholesterol Size": "결합 불성립(속성 지칭)", "Fishing Distance": "결합 불성립",
 "Hypertension Range": "결합 불성립", "Camping Clock": "결합 불성립",
 "Anemia Time": "결합 불성립", "Glamping Height": "결합 불성립",
 "Heartburn Width": "결합 불성립", "Stargazing Load": "결합 불성립",
 "Constipation Voltage": "결합 불성립", "Birdwatching Frequency": "결합 불성립",
 "Concussion Compatibility": "상태 명사로 제품명 부자연", "Canyon Usage": "사용 지칭으로 제품 불분명",
 "Sprain Condition": "상태 명사로 제품명 부자연", "Geyser Humidity": "결합 불성립",
 "Fracture Episode": "결합 불성립", "Fjord Cycle": "주기 지칭으로 제품 불분명",
 "Insulin Breakdown": "내역·고장 중의로 불분명", "Savanna Sensor": "결합 불성립",
 "Tundra Reception": "리셉션·수신 중의로 불분명", "Prairie Followup": "후속 지칭으로 제품 불분명",
 "Marsh Approval": "승인 지칭으로 제품 불분명", "Cove Matrix": "행렬·매트릭스 중의로 불분명",
 "Cliff Evaluation": "평가 대상 불분명", "Cavern Questionnaire": "설문 대상 불분명",
 "Oasis Utilization": "활용 지칭으로 제품 불분명", "Dune Benefit": "혜택 지칭으로 제품 불분명",
 "Whale Requirement": "요건 지칭으로 제품 불분명", "Dolphin Depreciation": "결합 불성립",
 "Penguin Resignation": "결합 불성립", "Flamingo Hazard": "결합 불성립",
 "Turtle Guarantor": "보증인 명사 결합 불성립", "Moose Tuner": "튜너 기능 지칭으로 제품 불분명",
 "Bison Tutorial": "동물 대상 결합 불성립", "Reindeer Handbook": "동물 대상 결합 불성립",
 "Blast App": "폭파·대량 발송 중의로 불분명", "Membership Mode": "기능 토글로 읽혀 제품 불분명",
 "Insurance Spec": "사양 참조로 제품 불분명", "Customs Quantity": "수량 대상 불분명",
 "Safety Analysis": "분석 대상 불분명", "Ductwork Coach": "코칭 대상 불분명",
 "Lockout Habit": "결합 불성립", "Rental Spec": "사양 참조로 제품 불분명",
 "Officiant Quantity": "수량 대상 불분명", "Scratch Coach": "선례 기각(App 기각) 계열",
 "Wrench Habit": "결합 불성립", "Lawyer Trend": "결합 불성립",
 "Attorney Correction": "결합 불성립", "Court Wattage": "결합 불성립",
 "Judge App": "판사·심사 중의로 제품 불분명", "Exclusion Workbook": "선례 기각(App 기각) 계열",
 "Withholding Mode": "기능 토글로 읽혀 제품 불분명", "Roofing Spec": "사양 참조로 제품 불분명",
 "Minor Quantity": "선례 기각(App 기각) 계열", "Video Analysis": "분석 대상 불분명",
 "Survey Coach": "코칭 대상 불분명", "Cover Habit": "결합 불성립",
 "Jury Core": "핵심 지칭으로 제품 불분명", "Lawsuit Registry": "등록부 지칭으로 제품 불분명",
 "Divorce History": "이력 대상 불분명", "Custody Advisory": "자문 대상 불분명",
 "Immigration Category": "분류 지칭으로 제품 불분명", "Notary Forecast": "예측 대상 불분명",
 "Mediation Certification": "결합 불성립", "Guardianship Clock": "결합 불성립",
 "Trademark Questionnaire": "설문 대상 불분명", "Fence Workbook": "워크북 대상 불분명",
 "Hiking Mode": "기능 토글로 읽혀 제품 불분명", "Chord Spec": "사양 참조로 제품 불분명",
 "Test Quantity": "선례 기각(App 기각) 계열", "Foreclosure Login": "제품 불분명",
 "Patent Analysis": "분석 대상 불분명",
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
out = base + r"\_dec_c20.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
