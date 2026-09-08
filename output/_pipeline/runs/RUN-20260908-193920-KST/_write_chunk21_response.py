import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk20_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk20_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "캠프 스튜디오 운영 관리로 명확 (Booth·Studio 라인)"),
    11: (0.6, "비트 연습 스케줄러로 명확 (Scheduler 라인)"),
    13: (0.6, "보험 정책 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    15: (0.6, "수확 작업 안전 위험 관리로 명확 - 물리 위험 실존"),
    22: (0.6, "보컬 수강료 결제 관리로 명확 (Payment 라인)"),
    23: (0.6, "라이너 확인 설문으로 명확"),
    26: (0.6, "휴가 준비 요건 관리로 명확 (Requirement 라인)"),
    30: (0.6, "플루트 연습 플래너로 명확 (Planner 라인)"),
    31: (0.6, "첼로 레슨 견적 관리로 명확 (Estimate 라인)"),
    33: (0.6, "트럼펫 숙련 등급 관리로 명확 (Rank 라인)"),
    34: (0.6, "클라리넷 소식지 관리로 명확 (Newsletter 라인)"),
    37: (0.6, "광미 처리 요건 관리로 명확 (Requirement 라인)"),
    43: (0.6, "오르간 일정 캘린더로 명확 (Calendar 라인)"),
    45: (0.6, "하프 영수증 관리로 명확 (Receipt 라인)"),
    49: (0.6, "타액 수강료 청구서 관리로 명확 (Invoice 라인)"),
    51: (0.6, "케이크 확인 설문으로 명확"),
    54: (0.6, "스펀지 사용 요건 관리로 명확 (Requirement 라인)"),
    60: (0.6, "레슨 디렉터리 관리로 명확 (Directory 라인)"),
    62: (0.6, "리사이탈 메모 관리로 명확 (Memo·Note 라인)"),
    65: (0.6, "이론 수업 공지 관리로 명확 (Announcement 라인)"),
    66: (0.6, "코드 레퍼런스 관리로 명확 (Reference 라인)"),
    68: (0.6, "레퍼토리 소식지 관리로 명확 (Newsletter 라인)"),
    70: (0.6, "스파 시설·서비스 평가로 명확 - 뷰티 실무 (Evaluation 라인)"),
    73: (0.6, "반주자 요건 관리로 명확 (Requirement 라인)"),
    76: (0.6, "평상 트럭 화물 위험 관리로 명확 - 추락 위험 실존"),
    84: (0.6, "합창 연습 포털로 명확 - 구체 서비스 (Portal 라인)"),
    90: (0.6, "비트 연습 진행 모니터링으로 명확 (Monitor 라인)"),
    91: (0.6, "피치 연습 플레이북 관리로 명확 (Playbook 라인)"),
    92: (0.6, "정책 확인 설문으로 명확"),
    93: (0.6, "제조 작업 안전 위험 관리로 명확 - 기계 부상 위험 실존"),
    101: (0.6, "꽃집 서비스 평가로 명확 - 웨딩 실무 (Evaluation 라인)"),
    104: (0.6, "변기 수리 요건 관리로 명확 (Requirement 라인)"),
    109: (0.6, "플루트 레슨 스케줄러로 명확 (Scheduler 라인)"),
    110: (0.6, "첼로 공연 순서 관리로 명확 (Order 라인)"),
    113: (0.6, "클라리넷 악기 재고 관리로 명확 (Inventory 라인)"),
    114: (0.6, "추모식 서비스 평가로 명확 - 장례 실무 (Evaluation 라인)"),
    116: (0.6, "운행 기록부 작성 요건 관리로 명확 (Requirement 라인)"),
    122: (0.6, "오르간 디렉터리 관리로 명확 (Directory 라인)"),
    123: (0.6, "검인 서류 사무 관리로 명확 (Office 라인)"),
    128: (0.6, "타액 수강 갱신 관리로 명확 (Renewal 라인)"),
    132: (0.6, "수영장 마감 요건 관리로 명확 (Requirement 라인)"),
    135: (0.6, "로드트립 운전 안전 위험 관리로 명확 - 사고 위험 실존"),
    143: (0.6, "음악이론 계산기로 실재 도구 (Calculator 라인)"),
    146: (0.6, "레퍼토리 곡목 목록 관리로 명확 (Inventory 라인)"),
    148: (0.6, "유모차 안전 평가로 명확 - 육아 용품 실무 (Evaluation 라인)"),
    149: (0.6, "스파 확인 설문으로 명확"),
    151: (0.6, "포도원 관리 요건으로 명확 (Requirement 라인)"),
    169: (0.6, "피치 연습 일지 관리로 명확 (Journal 라인)"),
    170: (0.6, "화물 운송 평가로 명확 - 물류 실무 (Evaluation 라인)"),
    178: (0.6, "보컬 발성 연습 시뮬레이터로 실재 도구 (Simulator 라인)"),
    179: (0.6, "사진 갤러리 평가로 명확 - 사진 실무 (Evaluation 라인)"),
    180: (0.6, "꽃집 확인 설문으로 명확"),
    182: (0.6, "코팅 시공 요건 관리로 명확 (Requirement 라인)"),
    187: (0.6, "플루트 연습 모니터링으로 명확 (Monitor 라인)"),
    188: (0.6, "첼로 청구서 관리로 명확 (Bill 라인)"),
    192: (0.6, "의복 수선 품질 평가로 명확 - 세탁 실무 (Evaluation 라인)"),
    193: (0.6, "추모식 확인 설문으로 명확"),
    194: (0.6, "항구 운영 요건 관리로 명확 (Requirement 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "증서 대장간 결합은 Forge 불성립",
    2: "곡집 범위 결합은 Scope 불성립",
    3: "교법 틀 결합은 Frame 불성립",
    5: "합창 존 결합은 Zone 불성립",
    6: "퇴직 콘솔 결합은 Console 도구형 불성립",
    7: "오케스트라 경로 결합은 Route 불성립",
    8: "유산 흔적 결합은 Trail 불성립",
    9: "멜로디 관문 결합은 Gate 불성립",
    10: "리듬 관리자 결합은 Manager 불성립",
    12: "피치 운영 결합은 Ops 불명확",
    14: "생산 사직 결합은 Resignation 불성립",
    16: "계량기에 보증인 결합 불성립",
    17: "기부자에 튜너 결합 불성립",
    18: "피아노 궤도 결합은 Rail 불성립",
    19: "기타 파일 결합은 File 다의어 불명확",
    20: "바이올린 관세 결합은 Tariff 기각 라인",
    21: "드럼 녹음기 결합은 불성립",
    24: "코팅 활용률 결합 불성립 - Utilization",
    25: "변기 혜택 결합은 Benefit 추상 불명확",
    27: "우쿨렐레 감가상각 결합 불성립",
    28: "계정 조정에 위험 결합 불성립",
    29: "사건에 보증인 결합 불성립",
    32: "색소폰 분류 결합은 Category 속성어 불성립",
    35: "항구 활용률 결합 불성립 - Utilization",
    36: "운행 기록부 혜택 결합은 Benefit 추상 불명확",
    38: "코일 감가상각 결합 불성립",
    39: "키패드 사직 결합은 Resignation 불성립",
    40: "이중언어에 위험 결합 불성립",
    41: "편집에 튜너 결합 불성립",
    42: "베이스 금고 결합은 Vault 불성립",
    44: "검인 검색기 결합은 Probate 도구형 기각 라인",
    46: "오보에 수당 결합은 Allowance 기각 라인",
    47: "비올라 그래프 결합은 Graph 불성립",
    48: "트롬본 추세 결합은 Trend 불명확",
    50: "만돌린 시간 결합은 Time 속성어 불성립",
    52: "제설 활용률 결합 불성립 - Utilization",
    53: "마감 혜택 결합은 Benefit 추상 불명확",
    55: "트랩 감가상각 결합 불성립",
    56: "로드트립 사직 결합은 Resignation 불성립",
    57: "아코디언에 위험 결합 불성립",
    58: "송금에 튜너 결합 불성립",
    59: "하모니카 실험실 결합은 Lab 불성립",
    61: "연습 상태 결합은 Status 불성립",
    63: "오디션 관세 결합은 Tariff 기각 라인",
    64: "조율 할인 결합은 Discount 기각 라인",
    67: "템포 바코드 결합은 Barcode 불성립",
    69: "합주 전압 결합은 Voltage 불성립",
    71: "연석 활용률 결합 불성립 - Utilization",
    72: "포도원 혜택 결합은 Benefit 추상 불명확",
    74: "질병 감가상각 결합 불성립",
    75: "채무자 사직 결합은 Resignation 불성립",
    77: "동네에 보증인 결합 불성립",
    78: "소송에 튜너 결합 불성립",
    79: "메트로놈 금고 결합은 Vault 불성립",
    80: "증서 연쇄 결합은 Cascade 추상 불성립",
    81: "곡집 루프 결합은 Loop 추상 불성립",
    82: "교법 베이스 결합은 Base 추상 불성립",
    83: "캠프 실험실 결합은 Lab 불성립",
    85: "퇴직 패널 결합은 Panel 불성립",
    86: "오케스트라 궤도 결합은 Rail 불성립",
    87: "유산 체인 결합은 Chain 추상 불성립",
    88: "멜로디 연결점 결합은 Nexus 추상 불성립",
    89: "리듬 엔진 결합은 Engine 추상 불성립",
    94: "수확에 보증인 결합 불성립",
    95: "계량기에 튜너 결합 불성립",
    96: "피아노 흔적 결합은 Trail 불성립",
    97: "기타 수준 결합은 Level 속성어 불성립",
    98: "바이올린 가치 결합은 Value 속성어 불성립",
    99: "드럼 추정기 결합은 불성립",
    100: "보컬 검증 결합은 Verification 불성립",
    102: "라이너 활용률 결합 불성립 - Utilization",
    103: "코팅 혜택 결합은 Benefit 추상 불명확",
    105: "휴가 감가상각 결합 불성립",
    106: "우쿨렐레 사직 결합은 Resignation 불성립",
    107: "계정 조정에 보증인 결합 불성립",
    108: "사건에 튜너 결합 불성립",
    111: "색소폰 속성 결합은 Attribute 불성립",
    112: "트럼펫 추세 결합은 Trend 불명확",
    115: "항구 혜택 결합은 Benefit 추상 불명확",
    117: "광미 감가상각 결합 불성립",
    118: "코일 사직 결합은 Resignation 불성립",
    119: "키패드에 위험 결합 불성립",
    120: "이중언어에 보증인 결합 불성립",
    121: "베이스 나침반 결합은 Compass 추상 불성립",
    124: "하프 코드 결합은 Code 다의어 불명확",
    125: "오보에 관세 결합은 Tariff 기각 라인",
    126: "비올라 라벨 결합은 Label 불성립",
    127: "트롬본 비교 결합은 Comparison 불명확",
    129: "만돌린 속도 결합은 Speed 속성어 불성립",
    130: "케이크 활용률 결합 불성립 - Utilization",
    131: "제설 혜택 결합은 Benefit 추상 불명확",
    133: "스펀지 감가상각 결합 불성립",
    134: "트랩 사직 결합은 Resignation 불성립",
    136: "아코디언에 보증인 결합 불성립",
    137: "하모니카 스테이션 결합은 Station 불성립",
    138: "레슨 장소 검색 결합은 Locator 불성립",
    139: "연습 뷰 결합은 View 불성립",
    140: "리사이탈 한도 결합은 Quota 불성립",
    141: "오디션 가치 결합은 Value 속성어 불성립",
    142: "조율 연체료 결합은 Arrears 기각 라인",
    144: "코드 예측 결합은 Forecast 불성립",
    145: "템포 예약 결합은 불성립",
    147: "합주 와트 결합은 Wattage 불성립",
    150: "연석 혜택 결합은 Benefit 추상 불명확",
    152: "반주자 감가상각 결합 불성립",
    153: "질병 사직 결합은 Resignation 불성립",
    154: "채무자에 위험 결합 불성립",
    155: "평상형 트럭에 보증인 결합 불성립",
    156: "동네에 튜너 결합 불성립",
    157: "메트로놈 나침반 결합은 Compass 추상 불성립",
    158: "증서 브리지 결합은 Bridge 기각 라인",
    159: "곡집 격자 결합은 Grid 추상 불성립",
    160: "교법 코어 결합은 Core 불성립",
    161: "캠프 스테이션 결합은 Station 불성립",
    162: "합창 콘솔 결합은 Console 도구형 불성립",
    163: "퇴직 저울 결합은 Scale 다의어 불명확",
    164: "오케스트라 흔적 결합은 Trail 불성립",
    165: "유산 링 결합은 Ring 불성립",
    166: "멜로디 대성지도 결합은 Atlas 추상 불성립",
    167: "리듬 조수 결합은 Assistant 불명확 기각 라인",
    168: "비트 동반자 결합은 Companion 불명확 기각 라인",
    171: "정책 활용률 결합 불성립 - Utilization",
    172: "생산에 보증인 결합 불성립",
    173: "수확에 튜너 결합 불성립",
    174: "피아노 체인 결합은 Chain 추상 불성립",
    175: "기타 요율 결합은 Rate 속성어 불성립",
    176: "바이올린 지분 결합은 Stake 불성립",
    177: "드럼 검사기 결합은 불성립",
    181: "라이너 혜택 결합은 Benefit 추상 불명확",
    183: "변기 감가상각 결합 불성립",
    184: "휴가 사직 결합은 Resignation 불성립",
    185: "우쿨렐레에 위험 결합 불성립",
    186: "계정 조정에 튜너 결합 불성립",
    189: "색소폰 분야 결합은 Field 다의어 불명확",
    190: "트럼펫 비교 결합은 Comparison 불명확",
    191: "클라리넷 청구 결합은 Claim 다의어 불명확",
    195: "운행 기록부 감가상각 결합 불성립",
    196: "광미 사직 결합은 Resignation 불성립",
    197: "코일에 위험 결합 불성립",
    198: "키패드에 보증인 결합 불성립",
    199: "이중언어에 튜너 결합 불성립",
    200: "베이스 등대 결합은 Beacon 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 58, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 142, len(REJECT_REASON)
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
