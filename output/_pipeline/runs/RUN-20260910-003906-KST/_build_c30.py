# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk30_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {
 "Trip App": (0.6, "여행 일정 관리 앱(실재 카테고리)"),
 "Vocal Tips": (0.55, "발성 훈련 팁(App→Tips 평행)"),
 "Coverage Login": (0.55, "보험 가입자 포털 접속(실재)"),
 "Leave Analysis": (0.6, "휴가 사용 패턴 분석(HR 실재)"),
 "Review App": (0.65, "성과 평가 관리 앱(실재 카테고리)"),
 "Lien Tips": (0.55, "유치권 등록 팁(App→Tips 평행)"),
 "Ledger Analysis": (0.6, "장부 데이터 분석(Copay Analysis 평행)"),
 "Lawsuit Opinion": (0.55, "소송 사건 평가 의견(법률 세컨드 오피니언 실재)"),
 "Painting App": (0.65, "도장 시공 관리 앱(실재)"),
 "Prerequisite Tips": (0.55, "선수과목 안내 팁(App→Tips 평행)"),
 "Cafe Analysis": (0.6, "카페 매출 분석(POS 분석 실재)"),
 "Gum Habit": (0.55, "잇몸 관리 습관 트래커(실재)"),
 "Divorce Path": (0.55, "이혼 절차 단계별 안내(실재)"),
 "Immigration Check": (0.6, "이민 사건 상태 조회(실재)"),
 "Trademark Reply": (0.6, "상표 심사 의견서 대응(실재 업무)"),
 "Style App": (0.65, "헤어·스타일링 앱(실재 카테고리)"),
 "Substitution Tips": (0.55, "의약품 대체 팁(App→Tips 평행)"),
 "Renovation Analysis": (0.6, "리모델링 비용·범위 분석(실재)"),
 "Sailing Manual": (0.55, "항해 매뉴얼(콘텐츠 형식 실재)"),
 "Fertility Kit": (0.55, "가임력 검사 키트 관리(실재 카테고리)"),
 "Golf Calculator": (0.65, "골프 핸디캡 계산기(실검색 실재)"),
 "Hypertension Checker": (0.55, "혈압 수치 확인 도구(가정 혈압 측정 실재)"),
 "Canyon Forecast": (0.6, "협곡 날씨·홍수 예보(실재)"),
 "Prairie Guide": (0.55, "초원 탐방 가이드(여행 콘텐츠 실재)"),
 "Trip Tips": (0.55, "여행 준비 팁(App→Tips 평행)"),
 "Coverage Analysis": (0.6, "보장 공백 분석(실재)"),
 "Binder App": (0.55, "보험 인수증(Binder) 발행 앱(실재 업무)"),
 "Review Tips": (0.55, "성과 평가 작성 팁(App→Tips 평행)"),
 "Ledger Coach": (0.55, "장부 기장 코칭(Gum Coach 평행)"),
 "Lawyer Fund": (0.55, "변호사 고객 신탁자금 관리(IOLTA 실재)"),
 "Severance App": (0.6, "퇴직금 계산·관리 앱(실재)"),
 "Painting Tips": (0.55, "도장 시공 팁(App→Tips 평행)"),
 "Budget Workbook": (0.55, "예산 계획 워크북(실재 서식)"),
 "Checkup Analysis": (0.55, "차량 점검 데이터 분석(실재)"),
 "Cafe Coach": (0.55, "카페 운영 코칭(실재)"),
 "Custody Companion": (0.6, "공동양육 동반 도구(실재 카테고리)"),
 "Immigration Score": (0.6, "이민 점수 계산기(CRS 실재)"),
 "Patent Predictor": (0.55, "특허 등록 가능성 예측(실재 카테고리)"),
 "Lullaby App": (0.65, "자장가·수면 사운드 앱(실재 카테고리)"),
 "Style Tips": (0.55, "스타일링 팁(App→Tips 평행)"),
 "Reefer Analysis": (0.6, "냉장 컨테이너 온도 분석(콜드체인 실재)"),
 "Renovation Coach": (0.55, "리모델링 진행 코칭(실재)"),
 "Sailing Worksheet": (0.55, "항해 기록 워크시트(실재 서식)"),
 "Climbing Kit": (0.55, "클라이밍 장비 키트(실재 카테고리)"),
}
R_DUP = {
 "Bundle Advice": "동일 배치 승인된 Bundle App/Tips와 동일 기능 의미 중복",
 "Budget Advice": "동일 배치 승인된 Budget App/Tips와 동일 기능 의미 중복",
 "Playground Advice": "동일 배치 승인된 Playground App/Tips와 동일 기능 의미 중복",
 "Vocal Advice": "동일 배치 승인된 Vocal App/Tips와 동일 기능 의미 중복",
 "Lien Advice": "동일 청크 승인된 Lien Tips와 동일 기능 의미 중복",
 "Prerequisite Advice": "동일 배치 승인된 Prerequisite App/Tips와 동일 기능 의미 중복",
 "Substitution Advice": "동일 배치 승인된 Substitution App/Tips와 동일 기능 의미 중복",
}
R = {
 "Whale Match": "결합 불성립", "Dolphin Validation": "결합 불성립",
 "Penguin Lookup": "탐색 대상 불분명(Moose Lookup 기각 선례)", "Flamingo Ping": "결합 불성립",
 "Turtle Model": "결합 불성립", "Moose Availability": "상태 명사로 제품명 부자연",
 "Bison Eligibility": "결합 불성립", "Reindeer Broadcast": "결합 불성립",
 "Payment Workbook": "워크북 대상 불분명", "Redline Mode": "기능 토글로 읽혀 제품 불분명",
 "Pallet Spec": "사양 참조로 제품 불분명", "Change Coach": "코칭 대상 불분명",
 "Vendor Habit": "결합 불성립", "Alumni Mode": "기능 토글로 읽혀 제품 불분명",
 "Throughput Spec": "사양 참조로 제품 불분명", "Silo Quantity": "수량 대상 불분명",
 "Ballot Coach": "코칭 대상 불분명", "Placement Habit": "결합 불성립",
 "Lawyer Debt": "결합 불성립", "Attorney Graph": "그래프 대상 불분명",
 "Court Proposal": "제안 대상 불분명", "Judge Warranty": "결합 불성립",
 "Jury Width": "결합 불성립", "Painting App SKIP": "",
 "Lawsuit Gift SKIP": "", "Prerequisite Tips SKIP": "",
 "Caption Workbook": "워크북 대상 불분명", "Sentiment Mode": "기능 토글로 읽혀 제품 불분명",
 "Recruiter Spec": "결합 불성립", "Lanyard Quantity": "수량 대상 불분명",
 "Checkup Login": "로그인 화면명으로 제품 불분명", "Flea Coach": "코칭 대상 불분명",
 "Divorce Wave SKIP": "", "Custody Monitor": "감시 대상 불분명",
 "Immigration Card SKIP": "", "Testament Stub": "결합 불성립",
 "Notary Value": "결합 불성립", "Mediation Extension": "연장 대상 불분명",
 "Guardianship Timer": "결합 불성립", "Patent Simulator": "시뮬레이션 대상 불분명",
 "Copyright Height": "결합 불성립", "Casino Workbook": "워크북 대상 불분명",
 "Ensemble Mode": "기능 토글로 읽혀 제품 불분명", "Injury Spec": "결합 불성립",
 "Creditor Quantity": "수량 대상 불분명", "Reefer Login": "제품 불분명(장비 자체 지시)",
 "Adjustment Coach": "코칭 대상 불분명", "Training Habit": "결합 불성립",
 "Migraine Number": "결합 불성립", "Insomnia Identifier": "결합 불성립",
 "Skydiving Format": "결합 불성립", "Acne Serial": "결합 불성립",
 "Snowboarding Balance": "결합 불성립", "Eczema Interest": "결합 불성립",
 "Ziplining Due": "결합 불성립", "Psoriasis Subsidy": "결합 불성립",
 "Sledding Advance": "결합 불성립", "Vertigo Penalty": "결합 불성립",
 "Diving Extension": "연장 대상 불분명", "Arthritis Trial": "대상 불분명(임상시험·체험판 중의)",
 "Menopause Worksheet": "워크시트 근거 약함(Pregnancy Worksheet 기각 선례)",
 "Rafting Layout": "결합 불성립", "Pregnancy Sketch": "제품성 불분명",
 "Climbing Notification": "알림 내용 불특정", "Biking Total": "결합 불성립",
 "Thyroid Widget": "결합 불성립", "Cholesterol Converter": "변환 대상 불분명",
 "Fishing Estimator": "산출 대상 불분명", "Camping Workshop": "결합 불성립",
 "Anemia Guardian": "감시 대상 불분명", "Glamping Result": "결합 불성립",
 "Heartburn Streak": "결합 불성립", "Stargazing Comparison": "비교 대상 불분명",
 "Constipation Proposal": "제안 대상 불분명", "Birdwatching Copy": "결합 불성립",
 "Concussion Reading": "수치 대상 불분명", "Sprain Deadline": "결합 불성립",
 "Geyser Duration": "결합 불성립", "Fracture Volume": "결합 불성립",
 "Fjord Diagnostic": "진단 대상 불분명", "Insulin Progress": "대상 불분명",
 "Savanna Authorization": "결합 불성립", "Tundra Template": "결합 불성립",
 "Marsh Rating": "평가 대상 불분명", "Cove Agreement": "결합 불성립",
 "Cliff Reply": "결합 불성립", "Cavern Account": "결합 불성립",
 "Oasis Case": "결합 불성립", "Dune Match": "결합 불성립",
 "Whale Validation": "결합 불성립", "Dolphin Lookup": "탐색 대상 불분명",
 "Penguin Ping": "결합 불성립", "Flamingo Model": "결합 불성립",
 "Turtle Availability": "상태 명사로 제품명 부자연", "Moose Eligibility": "결합 불성립",
 "Bison Broadcast": "결합 불성립", "Reindeer Barcode": "결합 불성립",
 "Sink App": "제품 불분명", "Payment Mode": "기능 토글로 읽혀 제품 불분명",
 "Redline Spec": "결합 불성립", "Pallet Quantity": "수량 대상 불분명",
 "Leave Coach": "코칭 대상 불분명", "Change Habit": "결합 불성립",
 "Bundle Workbook": "워크북 대상 불분명", "Alumni Spec": "결합 불성립",
 "Caption Mode": "기능 토글로 읽혀 제품 불분명",
 "Sentiment Spec": "결합 불성립", "Recruiter Quantity": "수량 대상 불분명",
 "Lanyard Login": "결합 불성립", "Flea Habit": "결합 불성립",
 "Throughput Quantity": "수량 대상 불분명", "Silo Login": "로그인 화면명으로 제품 불분명",
 "Ballot Habit": "결합 불성립", "Attorney Label": "결합 불성립",
 "Court Guarantee": "결합 불성립", "Judge Deposit": "결합 불성립",
 "Jury Temperature": "결합 불성립", "Lawsuit Gift": "결합 불성립",
 "Divorce Point": "결합 불성립", "Immigration Sheet SKIP": "",
 "Testament Statement": "결합 불성립", "Notary Stake": "결합 불성립",
 "Mediation Trial": "결합 불성립", "Guardianship Workshop": "결합 불성립",
 "Trademark Account": "계정 대상 불분명", "Copyright Width": "결합 불성립",
 "Playground Workbook": "워크북 대상 불분명", "Casino Mode": "기능 토글로 읽혀 제품 불분명",
 "Ensemble Spec": "결합 불성립", "Injury Quantity": "수량 대상 불분명",
 "Creditor Login": "제품 불분명", "Renovation Coach SKIP": "",
 "Adjustment Habit": "결합 불성립", "Migraine Version": "결합 불성립",
 "Insomnia Category": "결합 불성립", "Skydiving Serial": "결합 불성립",
 "Acne Token": "결합 불성립", "Snowboarding Interest": "결합 불성립",
 "Eczema Asset": "결합 불성립", "Ziplining Subsidy": "결합 불성립",
 "Psoriasis Discount": "판촉 계열 기각 선례", "Sledding Penalty": "결합 불성립",
 "Vertigo Markup": "결합 불성립", "Diving Trial": "결합 불성립",
 "Arthritis Graph": "그래프 대상 불분명", "Menopause Diagram": "도식 대상 불분명(Pregnancy Diagram 기각 선례)",
 "Rafting Sketch": "제품성 불분명", "Pregnancy Outline": "개요 대상 불분명",
 "Fertility Count": "카운트 대상 불분명", "Biking Widget": "결합 불성립",
 "Thyroid Repository": "결합 불성립", "Golf Converter": "변환 대상 불분명",
 "Cholesterol Generator": "생성 대상 불분명", "Fishing Checker": "검사 대상 불분명",
 "Hypertension Detector": "탐지 대상 불분명", "Camping Guardian": "감시 대상 불분명",
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
out = base + r"\_dec_c30.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
