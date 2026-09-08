import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk11_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk11_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "트롬본 연습 알림 관리로 명확 (Notification 라인)"),
    6: (0.6, "어금니 진료 평가로 명확 - 치과 실무 (Evaluation 라인)"),
    7: (0.6, "장난감 확인 설문으로 명확"),
    10: (0.6, "점화 장치 요건 관리로 명확"),
    13: (0.6, "계단 운반 안전 위험 관리로 명확 - 물리 위험 실존"),
    19: (0.6, "리사이탈 소식·갱신 관리로 명확 (Update 라인)"),
    23: (0.6, "코드 연습 공지 관리로 명확 (Announcement·Notification 라인)"),
    24: (0.6, "템포 참조 자료 관리로 명확 (Reference 라인)"),
    26: (0.6, "합주단 비용 환불 처리 관리로 명확 (Payment 라인 준용)"),
    29: (0.6, "증서 후속 조치 관리로 명확 (Followup 라인)"),
    30: (0.6, "분유 적합성 평가로 명확 - 육아 실무 (Evaluation 라인)"),
    31: (0.6, "메일룸 확인 설문으로 명확"),
    34: (0.6, "파산 절차 요건 관리로 명확"),
    44: (0.6, "멜로디 진행 지도 관리로 명확 (Map 라인)"),
    48: (0.6, "환자 확인 설문으로 명확"),
    53: (0.6, "기타 연습 알림 관리로 명확 (Alert 라인)"),
    54: (0.6, "바이올린 레슨 자문 관리로 명확 (Advisory 라인)"),
    58: (0.6, "마케팅 참여율 평가로 명확 - 마케팅 실무 (Evaluation 라인)"),
    59: (0.6, "방송 확인 설문으로 명확"),
    63: (0.6, "플루트 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    66: (0.6, "트럼펫 연습 알림 관리로 명확 (Notification 라인)"),
    67: (0.6, "클라리넷 레슨 예약 관리로 명확 (Appointment 라인)"),
    69: (0.6, "연금 상품·수령 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    70: (0.6, "초과근무 확인 설문으로 명확"),
    73: (0.6, "발렛 요건 관리로 명확"),
    76: (0.6, "트랙터 운용 안전 위험 관리로 명확 - 농기계 사고 위험 실존"),
    81: (0.6, "하프 연습 점검 관리로 명확 (Check 라인)"),
    86: (0.6, "만돌린 시뮬레이션 도구로 명확 (Simulator 라인)"),
    88: (0.6, "진드기 검사 평가로 명확 - 수의 실무 (Evaluation 라인)"),
    89: (0.6, "어금니 확인 설문으로 명확"),
    92: (0.6, "투약 요건 관리로 명확"),
    102: (0.6, "오디션 자문 관리로 명확 (Advisory 라인)"),
    105: (0.6, "코드 계산기로 명확 - 실재 도구"),
    108: (0.6, "합주단 경비 관리로 명확 (Expense 라인)"),
    111: (0.6, "부동산 증서 거래 승인 관리로 명확 (Approval 라인)"),
    112: (0.6, "상판 시공 품질 평가로 명확 - 건설 실무 (Evaluation 라인)"),
    113: (0.6, "분유 확인 설문으로 명확"),
    116: (0.6, "스트레칭 요건 관리로 명확"),
    118: (0.6, "석조 작업 안전 위험 관리로 명확 - 물리 위험 실존"),
    121: (0.6, "교법 진도 트래커로 명확 (Tracker 라인)"),
    130: (0.6, "음정 연습 포털 관리로 명확 - 구체 서비스 지시 (Portal 라인)"),
    132: (0.6, "등록 요건 관리로 명확"),
    135: (0.6, "기타 코드 차트 관리로 명확 (Chart 라인)"),
    140: (0.6, "공문서 기록물 평가로 명확 - 기록물 관리 실무 (Evaluation 라인)"),
    141: (0.6, "참여 확인 설문으로 명확"),
    150: (0.6, "클라리넷 레슨 피드백 관리로 명확 (Feedback 라인)"),
    152: (0.6, "연금 확인 설문으로 명확"),
    158: (0.6, "용접 작업 안전 위험 관리로 명확 - 화상 위험 실존"),
    164: (0.6, "오보에 자문 관리로 명확 (Advisory 라인)"),
    167: (0.6, "타악 연습 진단 도구로 명확 (Diagnostic 라인)"),
    170: (0.6, "진드기 확인 설문으로 명확"),
    173: (0.6, "제품 요건 관리로 명확"),
    182: (0.6, "리사이탈 프로그램 초안 관리로 명확 (Sketch 라인 준용)"),
    186: (0.6, "코드 변환기로 명확 - 실재 도구"),
    188: (0.6, "레퍼토리 곡 선정 피드백 관리로 명확 (Feedback 라인)"),
    189: (0.6, "합주단 소식지 관리로 명확 (Newsletter 라인)"),
    193: (0.6, "보험계약자 인수 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    194: (0.6, "상판 확인 설문으로 명확"),
    197: (0.6, "곡 수록 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "비올라 식별자 결합은 Identifier 불성립",
    3: "타액 기간 결합은 Duration 속성어 불성립",
    4: "만돌린 검증 결합은 Verification 불성립",
    5: "아코디언 와트 결합은 Wattage 불성립",
    8: "제품 활용률 결합 불성립 - Utilization",
    9: "투약 혜택 결합은 Benefit 추상 불명확",
    11: "림 감가상각 결합은 대상 불성립",
    12: "관용구 사직 결합은 Resignation 불성립",
    14: "촬영지에 보증인 결합 불성립",
    15: "장식에 튜너 결합 불성립",
    16: "하모니카 릴레이 결합은 Relay 불성립",
    17: "레슨 규모·음계 결합은 Scale 다의어 불명확",
    18: "연습 베이 결합은 Bay 불성립",
    20: "오디션 회람 결합은 Circular 불성립",
    21: "조율 지분 결합은 Stake 불성립",
    22: "이론 선불·전진 결합은 Advance 다의어 불명확",
    25: "레퍼토리 바코드 결합은 불성립",
    27: "반주자 압력 결합은 Pressure 속성어 불성립",
    28: "메트로놈 주기 결합은 Cycle 불성립",
    32: "곡집 활용률 결합 불성립 - Utilization",
    33: "스트레칭 혜택 결합은 Benefit 추상 불명확",
    35: "석조 사직 결합은 Resignation 불성립",
    36: "집안일에 위험 결합 불성립",
    37: "보관에 보증인 결합 불성립",
    38: "교법에 튜너 결합 불성립",
    39: "캠프 릴레이 결합은 Relay 불성립",
    40: "합창 연쇄 결합은 Cascade 추상 불성립",
    41: "퇴직 신호 결합은 Signal 불성립",
    42: "오케스트라 루프 결합은 Loop 추상 불성립",
    43: "유산 파도 결합은 Wave 추상 불성립",
    45: "리듬 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    46: "비트 실험실 결합은 Lab 불성립",
    47: "피치 구역 결합은 Zone 불성립",
    49: "등록 혜택 결합은 Benefit 추상 불명확",
    50: "세탁 주문에 보증인 결합 불성립",
    51: "장례 구성에 튜너 결합 불성립",
    52: "피아노 격자 결합은 Grid 추상 불성립",
    55: "드럼 체험·재판 결합은 Trial 다의어 불명확",
    56: "보컬 계좌·계정 결합은 Account 다의어 불명확",
    57: "우쿨렐레 전압 결합은 Voltage 불성립",
    60: "롤백 감가상각 결합 불성립",
    61: "스크리닝에 위험 결합 불성립",
    62: "티켓팅에 보증인 결합 불성립",
    64: "첼로 양식 결합은 Form 다의어 불명확",
    65: "색소폰 요금(교통) 결합은 Fare 기각 라인",
    68: "베이스 고장 분석 결합은 Breakdown 불성립",
    71: "비계 활용률 결합 불성립 - Utilization",
    72: "바코드 혜택 결합은 불성립",
    74: "숙제 감가상각 결합 불성립",
    75: "용접 사직 결합은 Resignation 불성립",
    77: "기부에 보증인 결합 불성립",
    78: "투표에 튜너 결합 불성립",
    79: "오르간 규모·음계 결합은 Scale 다의어 불명확",
    80: "검인 흔적 결합은 Trail 불성립",
    82: "오보에 회람 결합은 Circular 불성립",
    83: "비올라 범주 결합은 Category 속성어 불성립",
    84: "트롬본 키트 결합은 Kit 불성립",
    85: "타액 음량 결합은 Volume 속성어 불성립",
    87: "아코디언 밝기 결합은 Brightness 속성어 불성립",
    90: "장난감 활용률 결합 불성립 - Utilization",
    91: "제품 혜택 결합은 Benefit 추상 불명확",
    93: "점화 장치 감가상각 결합 불성립",
    94: "림 사직 결합은 대상 불성립",
    95: "관용구에 위험 결합 불성립",
    96: "계단에 보증인 결합 불성립",
    97: "촬영지에 튜너 결합 불성립",
    98: "하모니카 금고 결합은 Vault 추상 불성립",
    99: "레슨 경로 결합은 Route 불성립",
    100: "연습 게시글 결합은 Post 다의어 불명확",
    101: "리사이탈 피드·사료 결합은 Feed 다의어 불명확",
    103: "조율 마진 결합은 Margin 기각 라인",
    104: "이론 벌금 결합은 Penalty 기각 라인",
    106: "템포 예측 결합은 Forecast 불성립",
    107: "레퍼토리 예약 결합은 대상 불성립",
    109: "반주자 하중 결합은 Load 불성립",
    110: "메트로놈 고장 분석 결합은 Breakdown 불성립",
    114: "메일룸 활용률 결합 불성립 - Utilization",
    115: "곡집 혜택 결합은 Benefit 추상 불명확",
    117: "파산 감가상각 결합 불성립",
    119: "집안일에 보증인 결합 불성립",
    120: "보관에 튜너 결합 불성립",
    122: "캠프 금고 결합은 Vault 추상 불성립",
    123: "합창 브리지 결합은 Bridge 기각 라인",
    124: "퇴직 감시 결합은 Watch 도구형 기각 라인",
    125: "오케스트라 격자 결합은 Grid 추상 불성립",
    126: "유산 경로 결합은 Path 추상 불성립",
    127: "멜로디 틀 결합은 Frame 불성립",
    128: "리듬 게시판 결합은 Board 다의어 불명확",
    129: "비트 역 결합은 Station 불성립",
    131: "환자 활용률 결합 불성립 - Utilization",
    133: "세탁 주문에 튜너 결합 불성립",
    134: "피아노 파도 결합은 Wave 추상 불성립",
    136: "바이올린 탄원 결합은 Petition 불성립",
    137: "드럼 그래프 결합은 Graph 불성립",
    138: "보컬 케이스·소송 결합은 Case 다의어 불명확",
    139: "우쿨렐레 와트 결합은 Wattage 불성립",
    142: "방송 활용률 결합 불성립 - Utilization",
    143: "롤백 사직 결합은 Resignation 불성립",
    144: "스크리닝에 보증인 결합 불성립",
    145: "티켓팅에 튜너 결합 불성립",
    146: "플루트 실험실 결합은 Lab 불성립",
    147: "첼로 카드 결합은 Card 다의어 불명확",
    148: "색소폰 세금 결합은 Tax 기각 라인",
    149: "트럼펫 키트 결합은 Kit 불성립",
    151: "베이스 센서 결합은 Sensor 불성립",
    153: "초과근무 활용률 결합 불성립 - Utilization",
    154: "비계 혜택 결합은 Benefit 추상 불명확",
    155: "바코드 요건 결합은 불성립",
    156: "발렛 감가상각 결합 불성립",
    157: "숙제 사직 결합은 Resignation 불성립",
    159: "트랙터에 보증인 결합 불성립",
    160: "기부에 튜너 결합 불성립",
    161: "오르간 경로 결합은 Route 불성립",
    162: "검인 사슬 결합은 Chain 불성립",
    163: "하프 악보·채점 결합은 Score 다의어 - 악보로 오독 위험",
    165: "비올라 속성 결합은 Attribute 불성립",
    166: "트롬본 개수 결합은 Count 불성립",
    168: "만돌린 예측기 결합은 Predictor 불성립",
    169: "아코디언 빈도 결합은 Frequency 속성어 불성립",
    171: "어금니 활용률 결합 불성립 - Utilization",
    172: "장난감 혜택 결합은 Benefit 추상 불명확",
    174: "투약 감가상각 결합 불성립",
    175: "점화 장치 사직 결합은 Resignation 불성립",
    176: "림 위험 결합은 대상 불성립",
    177: "관용구에 보증인 결합 불성립",
    178: "계단에 튜너 결합 불성립",
    179: "하모니카 컴퍼스 결합은 Compass 추상 불성립",
    180: "레슨 궤도 결합은 Rail 불성립",
    181: "연습 항구 결합은 Harbor 불성립",
    183: "오디션 탄원 결합은 Petition 불성립",
    184: "조율 벌금 결합은 Fine 기각 라인",
    185: "이론 마크업 결합은 Markup 기각 라인",
    187: "템포 마감 결합은 대상 불성립",
    190: "반주자 전압 결합은 Voltage 불성립",
    191: "메트로놈 센서 결합은 Sensor 불성립",
    192: "증서 매트릭스 결합은 Matrix 추상 불성립",
    195: "분유 활용률 결합 불성립 - Utilization",
    196: "메일룸 혜택 결합은 Benefit 추상 불명확",
    198: "스트레칭 감가상각 결합 불성립",
    199: "파산 사직 결합은 Resignation 불성립",
    200: "석조에 보증인 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 59, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 141, len(REJECT_REASON)
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
