import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk5_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk5_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "기타 학습 플레이북 관리로 명확 (Playbook 라인)"),
    7: (0.6, "활력징후(vitals) 평가로 명확 - 요양 실무 (Evaluation 라인)"),
    16: (0.6, "클라리넷 학습 가이드 관리로 명확 (Guide 라인)"),
    18: (0.6, "문의 처리 품질 평가로 명확 - CS 실무 (Evaluation 라인)"),
    19: (0.6, "지원자 인테이크 설문으로 명확"),
    22: (0.6, "셰프 채용·자격 요건 관리로 명확"),
    30: (0.6, "하프 단원·출연 명단 관리로 명확 (Roster 라인)"),
    31: (0.6, "오보에 곡목·자료 리스트 관리로 명확 (List 라인)"),
    37: (0.6, "사파리 투어 품질 평가로 명확 - 여행 실무 (Evaluation 라인)"),
    38: (0.6, "하모니카 인테이크 설문으로 명확"),
    41: (0.6, "화물 적하 요건 관리로 명확"),
    49: (0.6, "연주회 신청 양식 관리로 명확 (Form 라인)"),
    53: (0.6, "코드 연습 워크시트 관리로 명확 - 교육 실재"),
    54: (0.6, "템포 워크숍 운영 관리로 명확 (Workshop 라인)"),
    55: (0.6, "연주 곡목 가이드 관리로 명확 (Guide 라인)"),
    56: (0.6, "합주 공연 예약금 수납 관리로 명확"),
    62: (0.6, "아파트 피트니스 시설 평가로 명확 - 시설 실무 (Evaluation 라인)"),
    63: (0.6, "캠프 인테이크 설문으로 명확"),
    80: (0.6, "이사 조건 요건 관리로 명확"),
    87: (0.6, "기타 연습 일지 관리로 명확 (Journal 라인)"),
    88: (0.6, "바이올린 수강료 전표 관리로 명확 - 실무 용어"),
    90: (0.6, "보컬 시창(악보읽기) 연습 관리로 명확 (Reading 라인)"),
    92: (0.6, "활력징후 문진 설문으로 명확"),
    99: (0.6, "학원 공지·소식 발송 관리로 명확 (Newsletter 라인 준용)"),
    101: (0.6, "클라리넷 연주 평점 관리로 명확 (Rating 라인)"),
    103: (0.6, "클라우드 인프라 평가로 명확 - IT 실무 (Evaluation 라인)"),
    104: (0.6, "문의 인테이크 설문으로 명확"),
    107: (0.6, "배출 기준 요건 관리로 명확"),
    115: (0.6, "하프 레슨·조율 알림 관리로 명확 (Alert 라인)"),
    122: (0.6, "배관 역류(backflow) 검사 평가로 명확 - 배관 실무 (Evaluation 라인)"),
    123: (0.6, "사파리 투어 인테이크 설문으로 명확"),
    126: (0.6, "거래 조건 요건 관리로 명확"),
    133: (0.6, "연습 기록부 관리로 명확 (Register 라인)"),
    135: (0.6, "오디션 접수 전표 관리로 명확 (Slip 라인 준용)"),
    138: (0.6, "코드 지판 다이어그램 관리로 명확 - 기타 교육 실재"),
    140: (0.6, "연주 곡목 평점 관리로 명확 (Rating 라인)"),
    141: (0.6, "합주단 인증 관리로 명확 (Certification 라인)"),
    147: (0.6, "목공 시공 품질 평가로 명확 - 건설 실무 (Evaluation 라인)"),
    148: (0.6, "피트니스 시설 설문으로 명확"),
    151: (0.6, "자산 운용 요건 관리로 명확"),
    163: (0.6, "비행 훈련·안전 평가로 명확 - 항공 실무 (Evaluation 라인)"),
    165: (0.6, "용어 등재 요건 관리로 명확"),
    172: (0.6, "기타 학생 등록부 관리로 명확 (Registry 라인)"),
    175: (0.6, "보컬 참조 자료 관리로 명확 (Reference 라인)"),
    186: (0.6, "수강 계약 관리로 명확"),
    188: (0.6, "비밀번호 강도 평가로 명확 - 보안 실무 (Evaluation 라인)"),
    189: (0.6, "클라우드 요구 확인 설문으로 명확"),
    192: (0.6, "연사 선정 요건 관리로 명확"),
    200: (0.6, "연습 진도 차트 관리로 명확 (Score·Level 라인 준용)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "피아노 흐름 결합은 Flow 추상 불성립",
    3: "바이올린 표 결합은 Table 다의어 불명확",
    4: "드럼 서명·시그니처 결합은 Signature 다의어 불명확",
    5: "보컬 사본·광고문 결합은 Copy 다의어 불명확",
    6: "우쿨렐레 길이 결합은 Length 속성어 불성립",
    8: "반복(recurring) 설문 결합은 Recurring 속성어 불명확",
    9: "랙에 요건 결합 불성립",
    10: "대기자 사직 결합은 Resignation 불성립",
    11: "약제집에 위험 결합 불성립",
    12: "플루트 신호 결합은 Signal 추상 불성립",
    13: "첼로 만·구획 결합은 Bay 불성립",
    14: "색소폰 타브·탭 결합은 Tab 불명확 - 타브악보는 프렛 악기 전용",
    15: "트럼펫 벌금 결합은 Penalty 기각 라인",
    17: "베이스 폭 결합은 Width 속성어 불성립",
    20: "연사 활용률 결합 불성립 - Utilization",
    21: "배출가스 혜택 결합은 Benefit 추상 불명확",
    23: "애견 호텔에 감가상각 결합 불성립",
    24: "치통 사직 결합은 Resignation 불성립",
    25: "러닝머신에 위험 결합 불성립",
    26: "영유아에 보증인 결합 불성립",
    27: "보행기에 튜너 결합 불성립",
    28: "오르간 틀 결합은 Frame 불성립",
    29: "검인 원장 결합은 Probate 도구형 기각 라인",
    32: "비올라 판매 결합은 Sale 불성립",
    33: "트롬본 마크업 결합은 Markup 다의어 불명확",
    34: "타악 무대·단계 결합은 Stage 다의어 불명확",
    35: "만돌린 방송 결합은 Broadcast 불명확",
    36: "아코디언 거리 결합은 Distance 속성어 불성립",
    39: "용량 활용률 결합 불성립 - Utilization",
    40: "거래 혜택 결합은 Benefit 추상 불명확",
    42: "부속 조항에 감가상각 결합 불성립",
    43: "보험 합의 사직 결합은 Resignation 불성립",
    44: "베스팅에 위험 결합 불성립",
    45: "배수로에 보증인 결합 불성립",
    46: "논문에 튜너 결합 불성립",
    47: "레슨 베이스 결합은 Base 추상 불성립",
    48: "연습 동반자 결합은 Companion 불명확 은유",
    50: "오디션 표 결합은 Table 다의어 불명확",
    51: "조율 가격 결합은 Price 속성어 불성립",
    52: "이론 분야 결합은 Field 다의어 불명확",
    57: "반주자 크기 결합은 Size 속성어 불성립",
    58: "메트로놈 폭 결합은 Width 속성어 불성립",
    59: "증서 전압 결합은 Voltage 불성립",
    60: "곡집 용량 결합은 Capacity 속성어 불성립",
    61: "교법 센서 결합은 Sensor 불성립",
    64: "자세 활용률 결합 불성립 - Utilization",
    65: "자산 혜택 결합은 Benefit 추상 불명확",
    66: "유예(grace) 요건 결합은 Grace 다의어 불명확",
    67: "옥상에 감가상각 결합 불성립",
    68: "합창 사직 결합은 Resignation 불성립",
    69: "호흡에 위험 결합 불성립",
    70: "퇴직에 보증인 결합 불성립",
    71: "우산보험에 튜너 결합 불성립",
    72: "오케스트라 흐름 결합은 Flow 추상 불성립",
    73: "유산 데스크 결합은 Desk 추상 불성립",
    74: "멜로디 금고 결합은 Vault 추상 불성립",
    75: "리듬 연쇄 결합은 Cascade 추상 불성립",
    76: "비트 범위 결합은 Scope 불명확",
    77: "피치 경로 결합은 Path 추상 불성립",
    78: "키웨이 활용률 결합 불성립 - Utilization",
    79: "용어집 혜택 결합은 Benefit 추상 불명확",
    81: "촬영에 감가상각 결합 불성립",
    82: "의식 사직 결합은 Resignation 불성립",
    83: "위반에 위험 결합 불성립",
    84: "잔류 염소에 보증인 결합 불성립",
    85: "세차에 튜너 결합 불성립",
    86: "피아노 허브 결합은 Hub 추상 불성립",
    89: "드럼 마커 결합은 Marker 불성립",
    91: "우쿨렐레 무게 결합은 Weight 속성어 불성립",
    93: "반복(recurring) 활용률 결합 불성립 - Utilization + 속성어",
    94: "랙에 감가상각 결합 불성립",
    95: "대기자에 위험 결합 불성립",
    96: "약제집에 보증인 결합 불성립",
    97: "플루트 감시 결합은 Watch 도구형 기각 라인",
    98: "첼로 게시물·우편 결합은 Post 다의어 불명확",
    100: "트럼펫 마크업 결합은 Markup 다의어 불명확",
    102: "베이스 온도 결합은 Temperature 속성어 불성립",
    105: "이력서 활용률 결합 불성립 - Utilization",
    106: "연사 혜택 결합은 Benefit 추상 불명확",
    108: "셰프에 감가상각 결합 불성립",
    109: "애견 호텔 사직 결합은 Resignation 불성립",
    110: "치통에 위험 결합 불성립",
    111: "러닝머신에 보증인 결합 불성립",
    112: "영유아에 튜너 결합 불성립",
    113: "오르간 베이스 결합은 Base 추상 불성립",
    114: "검인 게시판 결합은 Probate 추상 기각 라인",
    116: "오보에 표 결합은 Table 다의어 불명확",
    117: "비올라 요금·충전 결합은 Charge 다의어 불명확",
    118: "트롬본 상환 결합은 Redemption 불성립",
    119: "타악 결과 결합은 Result 불성립",
    120: "만돌린 바코드 결합은 Barcode 불성립",
    121: "아코디언 범위 결합은 Range 속성어 불성립",
    124: "하모니카 활용률 결합 불성립 - Utilization",
    125: "용량 혜택 결합은 Benefit 추상 불명확",
    127: "화물에 감가상각 결합 불성립",
    128: "부속 조항 사직 결합은 Resignation 불성립",
    129: "보험 합의에 위험 결합 불성립",
    130: "베스팅에 보증인 결합 불성립",
    131: "배수로에 튜너 결합 불성립",
    132: "레슨 코어 결합은 Core 추상 불성립",
    134: "리사이탈 카드 결합은 Card 불성립",
    136: "조율 운임 결합은 Fare 교통 어휘 불성립",
    137: "이론 형식 결합은 Format 불성립",
    139: "템포 수호자 결합은 Guardian 불명확 은유",
    142: "반주자 길이 결합은 Length 속성어 불성립",
    143: "메트로놈 온도 결합은 Temperature 속성어 불성립",
    144: "증서 와트 결합은 Wattage 불성립",
    145: "곡집 사용량 결합 불성립 - Usage 지표어",
    146: "교법에 접수 결합 불성립",
    149: "캠프 활용률 결합 불성립 - Utilization",
    150: "자세 혜택 결합은 Benefit 추상 불명확",
    152: "유예(grace)에 감가상각 결합 불성립",
    153: "옥상 사직 결합은 Resignation 불성립",
    154: "합창에 위험 결합 불성립",
    155: "호흡에 보증인 결합 불성립",
    156: "퇴직에 튜너 결합 불성립",
    157: "오케스트라 허브 결합은 Hub 추상 불성립",
    158: "유산 레이더 결합은 Radar 추상 불성립",
    159: "멜로디 나침반 결합은 Compass 불명확 은유",
    160: "리듬 브리지 결합은 Bridge 기각 라인",
    161: "비트 루프 결합은 Loop 추상 불성립",
    162: "피치 포인트 결합은 Point 불명확",
    164: "키웨이 혜택 결합은 Benefit 추상 불명확",
    166: "이사에 감가상각 결합 불성립",
    167: "촬영 사직 결합은 Resignation 불성립",
    168: "의식에 위험 결합 불성립",
    169: "위반에 보증인 결합 불성립",
    170: "잔류 염소에 튜너 결합 불성립",
    171: "피아노 데스크 결합은 Desk 추상 불성립",
    173: "바이올린 샘플 결합은 Sample 기각 라인",
    174: "드럼 균형 결합은 Balance 불성립",
    176: "우쿨렐레 거리 결합은 Distance 속성어 불성립",
    177: "활력징후 활용률 결합 불성립 - Utilization",
    178: "반복(recurring) 혜택 결합은 Benefit 추상 불명확 + 속성어",
    179: "랙 사직 결합은 Resignation 불성립",
    180: "대기자에 보증인 결합 불성립",
    181: "약제집에 튜너 결합 불성립",
    182: "플루트 범위 결합은 Scope 불명확",
    183: "첼로 항구 결합은 Harbor 불명확 은유",
    184: "색소폰 요약·브리핑 결합은 Brief 다의어 불명확",
    185: "트럼펫 상환 결합은 Redemption 불성립",
    187: "베이스 압력 결합은 Pressure 속성어 불성립",
    190: "문의 활용률 결합 불성립 - Utilization",
    191: "이력서 혜택 결합은 Benefit 추상 불명확",
    193: "배출가스에 감가상각 결합 불성립",
    194: "셰프 사직 결합은 Resignation 불성립",
    195: "애견 호텔에 위험 결합 불성립",
    196: "치통에 보증인 결합 불성립",
    197: "러닝머신에 튜너 결합 불성립",
    198: "오르간 코어 결합은 Core 추상 불성립",
    199: "검인 데크 결합은 Probate 추상 기각 라인",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 49, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 151, len(REJECT_REASON)
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
