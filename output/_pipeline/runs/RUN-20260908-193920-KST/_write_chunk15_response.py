import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk14_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk14_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    6: (0.6, "멜로디 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    10: (0.6, "배포 확인 설문으로 명확"),
    11: (0.6, "행사 등록 요건 관리로 명확"),
    17: (0.6, "보컬 수업 가능 시간 관리로 명확 (Availability 라인)"),
    19: (0.6, "객실 점유율 평가로 명확 - 숙박 실무 (Evaluation 라인)"),
    20: (0.6, "코호트 확인 설문으로 명확"),
    22: (0.6, "변전소 요건 관리로 명확"),
    29: (0.6, "트럼펫 연습 공지 관리로 명확 (Announcement 라인)"),
    30: (0.6, "클라리넷 인증 관리로 명확 (Certification 라인)"),
    31: (0.6, "호스텔 서비스 평가로 명확 - 여행 실무 (Evaluation 라인)"),
    32: (0.6, "베이스 확인 설문으로 명확"),
    35: (0.6, "패러리걸 업무 요건 관리로 명확"),
    42: (0.6, "하프 연습 이력 관리로 명확 (History 라인)"),
    46: (0.6, "타액 수강 계약 관리로 명확 (Agreement 라인)"),
    47: (0.6, "만돌린 환불 처리 관리로 명확 (Refund 라인)"),
    49: (0.6, "학위논문 심사 평가로 명확 - 교육 실무 (Evaluation 라인)"),
    50: (0.6, "회의 확인 설문으로 명확"),
    53: (0.6, "헤드헌터 요건 관리로 명확"),
    61: (0.6, "리사이탈 비용 견적 관리로 명확 (Estimate 라인)"),
    64: (0.6, "음악이론 매뉴얼 관리로 명확 (Manual 라인)"),
    65: (0.6, "코드 연습 타이머로 명확 (Timer 라인)"),
    73: (0.6, "탱커 운송 요건 관리로 명확"),
    79: (0.6, "곡집 학습 트래커로 명확 (Tracker 라인)"),
    94: (0.6, "기타 출연 명단 관리로 명확 (Roll 라인)"),
    95: (0.6, "바이올린 연습 계획 관리로 명확 (Plan 라인)"),
    96: (0.6, "드럼 악곡 스케치 관리로 명확 (Sketch 라인)"),
    97: (0.6, "보컬 수강 자격 관리로 명확 (Eligibility 라인)"),
    99: (0.6, "카탈로그 품질 평가로 명확 - 리테일 실무 (Evaluation 라인)"),
    100: (0.6, "점유 확인 설문으로 명확"),
    102: (0.6, "농약 사용 요건 관리로 명확"),
    111: (0.6, "클라리넷 출연 추천 관리로 명확 (Nomination 라인)"),
    112: (0.6, "세탁기 설치·점검 평가로 명확 - 배관 실무 (Evaluation 라인)"),
    113: (0.6, "호스텔 확인 설문으로 명확"),
    116: (0.6, "배당 요건 관리로 명확"),
    128: (0.6, "만돌린 경비 관리로 명확 (Expense 라인)"),
    130: (0.6, "외장재 시공 품질 평가로 명확 - 건설 실무 (Evaluation 라인)"),
    131: (0.6, "논문 확인 설문으로 명확"),
    134: (0.6, "우선순위 요건 관리로 명확"),
    142: (0.6, "공연 진행 순서 관리로 명확 (Order 라인)"),
    143: (0.6, "오디션 계획 관리로 명확 (Plan 라인)"),
    145: (0.6, "이론 워크시트 관리로 명확 (Worksheet 라인)"),
    146: (0.6, "코드 워크숍 운영 관리로 명확 (Workshop 라인)"),
    147: (0.6, "템포 참조 가이드 관리로 명확 (Guide 라인)"),
    151: (0.6, "보모 자격·수행 평가로 명확 - 육아 실무 (Evaluation 라인)"),
    154: (0.6, "수취인 요건 관리로 명확"),
    168: (0.6, "리듬 트레이닝 포털 관리로 명확 - 구체 서비스 지시 (Portal 라인)"),
    174: (0.6, "기타 연습 리포트 관리로 명확 (Report 라인)"),
    179: (0.6, "카탈로그 확인 설문으로 명확"),
    191: (0.6, "세차 폼·코팅 품질 평가로 명확 - 세차 실무 (Evaluation 라인)"),
    192: (0.6, "세탁기 확인 설문으로 명확"),
    195: (0.6, "환자 분류 기준 요건 관리로 명확"),
    198: (0.6, "배송 화물 손상 위험 관리로 명확 - 물리 위험 실존 (Shipment 준용)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "캠프 신호 결합은 Signal 불성립",
    2: "합창 파도 결합은 Wave 추상 불성립",
    3: "퇴직 포인트 결합은 Point 불성립",
    4: "오케스트라 베이스 결합은 Base 추상 불성립",
    5: "유산 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    7: "리듬 센터 결합은 Center 불성립",
    8: "비트 패널 결합은 Panel 불성립",
    9: "피치 흔적 결합은 Trail 불성립",
    12: "환자에 보증인 결합 불성립",
    13: "피아노 코어 결합은 Core 불성립",
    14: "기타 창·기간 결합은 Window 다의어 불명확",
    15: "바이올린 단위 결합은 Unit 불성립",
    16: "드럼 배치 결합은 Layout 불성립",
    18: "우쿨렐레 상태·조건 결합은 Condition 다의어 불명확",
    21: "농약 혜택 결합은 Benefit 추상 불명확",
    23: "기록물 사직 결합은 Resignation 불성립",
    24: "참여에 위험 결합 불성립",
    25: "방송에 보증인 결합 불성립",
    26: "플루트 콘솔 결합은 Console 도구형 불성립",
    27: "첼로 프로필 결합은 Profile 불성립",
    28: "색소폰 판매 결합은 Sale 불성립",
    33: "분류(triage) 활용률 결합 불성립 - Utilization",
    34: "배당 혜택 결합은 Benefit 추상 불명확",
    36: "택배 감가상각 결합 불성립",
    37: "연금에 위험 결합 불성립",
    38: "초과근무에 보증인 결합 불성립",
    39: "비계에 튜너 결합 불성립",
    40: "오르간 연결점 결합은 Nexus 추상 불성립",
    41: "검인 관리자 결합은 Manager 불성립",
    43: "오보에 항목 결합은 Item 다의어 불명확",
    44: "비올라 마커 결합은 Marker 불성립",
    45: "트롬본 계산기 결합은 불성립",
    48: "아코디언 에피소드 결합은 Episode 불성립",
    51: "헤드라인 활용률 결합 불성립 - Utilization",
    52: "우선순위 혜택 결합은 Benefit 추상 불명확",
    54: "굿즈 감가상각 결합 불성립",
    55: "진드기에 위험 결합 불성립",
    56: "어금니에 보증인 결합 불성립",
    57: "장난감에 튜너 결합 불성립",
    58: "하모니카 감시 결합은 Watch 도구형 기각 라인",
    59: "레슨 지도 결합은 Atlas 추상 불성립",
    60: "연습 로비 결합은 Lobby 불성립",
    62: "오디션 단위 결합은 Unit 불성립",
    63: "조율 식별자 결합은 Identifier 불성립",
    66: "템포 템플릿 결합은 불성립",
    67: "레퍼토리 인증 결합은 불성립",
    68: "합주 길이 결합은 Length 속성어 불성립",
    69: "반주자 사용률 결합은 Usage 불성립",
    70: "메트로놈 설문 결합은 불성립",
    71: "운동 활용률 결합 불성립 - Utilization",
    72: "수취인 혜택 결합은 Benefit 추상 불명확",
    74: "증서 감가상각 결합 불성립",
    75: "계약자 사직 결합은 Resignation 불성립",
    76: "상판에 위험 결합 불성립",
    77: "분유에 보증인 결합 불성립",
    78: "메일룸에 튜너 결합 불성립",
    80: "교법 컴퍼스 결합은 Compass 추상 불성립",
    81: "캠프 감시 결합은 Watch 도구형 기각 라인",
    82: "합창 경로 결합은 Path 추상 불성립",
    83: "퇴직 지도 결합은 Map 불성립 - 대상 불성립",
    84: "오케스트라 코어 결합은 Core 불성립",
    85: "유산 게시판 결합은 Board 다의어 불명확",
    86: "멜로디 실험실 결합은 Lab 불성립",
    87: "리듬 구역 결합은 Zone 불성립",
    88: "비트 규모·음계 결합은 Scale 다의어 불명확",
    89: "피치 사슬 결합은 Chain 불성립",
    90: "배포 활용률 결합 불성립 - Utilization",
    91: "등록 감가상각 결합 불성립",
    92: "환자에 튜너 결합 불성립",
    93: "피아노 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    98: "우쿨렐레 습도 결합은 Humidity 불성립",
    101: "코호트 활용률 결합 불성립 - Utilization",
    103: "변전소 감가상각 결합 불성립",
    104: "기록물에 위험 결합 불성립",
    105: "참여에 보증인 결합 불성립",
    106: "방송에 튜너 결합 불성립",
    107: "플루트 패널 결합은 Panel 불성립",
    108: "첼로 상태 결합은 Status 불성립",
    109: "색소폰 청구 결합은 Charge 다의어 불명확",
    110: "트럼펫 계산기 결합은 불성립",
    114: "베이스 활용률 결합 불성립 - Utilization",
    115: "분류(triage) 혜택 결합은 Benefit 추상 불명확",
    117: "패러리걸 감가상각 결합 불성립",
    118: "택배 사직 결합은 Resignation 불성립",
    119: "연금에 보증인 결합 불성립",
    120: "초과근무에 튜너 결합 불성립",
    121: "오르간 지도 결합은 Atlas 추상 불성립",
    122: "검인 엔진 결합은 Engine 추상 불성립",
    123: "하프 파일 결합은 File 다의어 불명확",
    124: "오보에 단위 결합은 Unit 불성립",
    125: "비올라 잔액·균형 결합은 Balance 다의어 불명확",
    126: "트롬본 변환기 결합은 불성립",
    127: "타액 회신 결합은 Reply 불성립",
    129: "아코디언 주기 결합은 Cycle 불성립",
    132: "회의 활용률 결합 불성립 - Utilization",
    133: "헤드라인 혜택 결합은 Benefit 추상 불명확",
    135: "헤드헌터 감가상각 결합 불성립",
    136: "굿즈 사직 결합은 Resignation 불성립",
    137: "진드기에 보증인 결합 불성립",
    138: "어금니에 튜너 결합 불성립",
    139: "하모니카 범위 결합은 Scope 불명확",
    140: "레슨 관리인 결합은 Keeper 불성립",
    141: "연습 티커 결합은 Ticker 불성립",
    144: "조율 범주 결합은 Category 속성어 불성립",
    148: "레퍼토리 추천 결합은 불성립",
    149: "합주 무게 결합은 Weight 속성어 불성립",
    150: "반주자 상태·조건 결합은 Condition 다의어 불명확",
    152: "메트로놈 활용률 결합 불성립 - Utilization",
    153: "운동 혜택 결합은 Benefit 추상 불명확",
    155: "탱커 감가상각 결합 불성립",
    156: "증서 사직 결합은 Resignation 불성립",
    157: "계약자에 위험 결합 불성립",
    158: "상판에 보증인 결합 불성립",
    159: "분유에 튜너 결합 불성립",
    160: "곡집 흐름 결합은 Flow 추상 불성립",
    161: "교법 비컨 결합은 Beacon 추상 불성립",
    162: "캠프 범위 결합은 Scope 불명확",
    163: "합창 포인트 결합은 Point 불성립",
    164: "퇴직 틀 결합은 Frame 불성립",
    165: "오케스트라 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    166: "유산 데크 결합은 Deck 불성립",
    167: "멜로디 역 결합은 Station 불성립",
    169: "비트 경로 결합은 Route 불성립",
    170: "피치 반지 결합은 Ring 불성립",
    171: "배포 혜택 결합은 Benefit 추상 불명확",
    172: "등록 사직 결합은 Resignation 불성립",
    173: "피아노 게시판 결합은 Board 다의어 불명확",
    175: "바이올린 비용 결합은 Cost 속성어 불성립",
    176: "드럼 개요 결합은 Outline 불성립",
    177: "보컬 방송 결합은 Broadcast 불성립",
    178: "우쿨렐레 에피소드 결합은 Episode 불성립",
    180: "점유 활용률 결합 불성립 - Utilization",
    181: "코호트 혜택 결합은 Benefit 추상 불명확",
    182: "농약 감가상각 결합 불성립",
    183: "변전소 사직 결합은 Resignation 불성립",
    184: "기록물에 보증인 결합 불성립",
    185: "참여에 튜너 결합 불성립",
    186: "플루트 규모·음계 결합은 Scale 다의어 불명확",
    187: "첼로 뷰 결합은 View 불성립",
    188: "색소폰 의무·관세 결합은 Duty 다의어 불명확",
    189: "트럼펫 변환기 결합은 불성립",
    190: "클라리넷 정정 결합은 Correction 불성립",
    193: "호스텔 활용률 결합 불성립 - Utilization",
    194: "베이스 혜택 결합은 Benefit 추상 불명확",
    196: "배당 감가상각 결합 불성립",
    197: "패러리걸 사직 결합은 Resignation 불성립",
    199: "연금에 튜너 결합 불성립",
    200: "오르간 관리인 결합은 Keeper 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 52, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 148, len(REJECT_REASON)
covered = set(APPROVE) | set(TRADEMARK_REJECT) | set(DUP_REJECT) | set(REJECT_REASON)
missing = sorted(set(range(1, n + 1)) - covered)
extra = sorted(covered - set(range(1, n + 1)))
assert covered == set(range(1, n + 1)), f"missing={missing} extra={extra}"
overlap = (set(APPROVE) & set(TRADEMARK_REJECT)) | (set(APPROVE) & set(DUP_REJECT)) | (set(APPROVE) & set(REJECT_REASON)) | (set(TRADEMARK_REJECT) & set(DUP_REJECT)) | (set(TRADEMARK_REJECT) & set(REJECT_REASON)) | (set(DUP_REJECT) & set(REJECT_REASON))
assert not overlap, f"overlapping indices: {sorted(overlap)}"

decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in APPROVE:
        conf, reason = APPROVE[i]
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": conf, "reason": reason})
    elif i in TRADEMARK_REJECT:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": True, "duplication": True, "trademark": False},
                          "confidence": 0.7, "reason": TRADEMARK_REJECT[i]})
    elif i in DUP_REJECT:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": True, "duplication": False, "trademark": True},
                          "confidence": 0.7, "reason": DUP_REJECT[i]})
    else:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": False, "duplication": True, "trademark": True},
                          "confidence": 0.7, "reason": REJECT_REASON[i]})

assert len(decisions) == n
approved = sum(1 for d in decisions if d["approve"])
kst = timezone(timedelta(hours=9))
resp = {
    "decisions": decisions,
    "judged_at": datetime.now(kst).isoformat(),
    "judged_by": "main-orchestrator",
    "request_hash": req["request_hash"],
    "round": req["round"],
    "run_id": req["run_id"],
    "stage": req["stage"],
}
with open(RESP, "w", encoding="utf-8", newline="\n") as f:
    json.dump(resp, f, ensure_ascii=False, indent=2)
print(f"written: {RESP}")
print(f"approve={approved} reject={len(decisions)-approved}")
