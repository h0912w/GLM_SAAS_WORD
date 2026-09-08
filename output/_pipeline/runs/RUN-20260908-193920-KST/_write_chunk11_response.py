import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk10_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk10_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    5: (0.6, "어린이집 등록 상담 평가로 명확 (Evaluation 라인)"),
    13: (0.6, "보컬 평점 관리로 명확 (Rating 라인)"),
    16: (0.6, "스크리닝 요건 관리로 명확"),
    21: (0.6, "첼로 출연 명단 관리로 명확 (Roll 라인)"),
    22: (0.6, "색소폰 연습 계획 관리로 명확 (Planner 라인 준용)"),
    23: (0.6, "트럼펫 악곡 스케치 관리로 명확 (Sketch 라인)"),
    24: (0.6, "클라리넷 수강 자격 관리로 명확 (Eligibility 라인)"),
    27: (0.6, "발렛 확인 설문으로 명확"),
    30: (0.6, "트랙터 요건 관리로 명확"),
    36: (0.6, "오르간 수강 포털 관리로 명확 - 구체 서비스 지시 (Portal 라인)"),
    45: (0.6, "미용 제품 평가로 명확 - 살론 실무 (Evaluation 라인)"),
    46: (0.6, "투약 확인 설문으로 명확"),
    49: (0.6, "관용구 번역 요건 관리로 명확 - 통번역 실무"),
    57: (0.6, "연습 부스 예약 관리로 명확 (Booth 라인)"),
    65: (0.6, "합주 연습 영상 기록 관리로 명확 (Record 라인 준용)"),
    69: (0.6, "레퍼토리 곡 적합성 평가로 명확 (Evaluation 라인)"),
    70: (0.6, "스트레칭 확인 설문으로 명확"),
    72: (0.6, "석조 시공 요건 관리로 명확"),
    87: (0.6, "등록 확인 설문으로 명확"),
    94: (0.6, "보컬 수강 계약 관리로 명확 (Agreement 라인)"),
    101: (0.6, "첼로 연습 리포트 관리로 명확 (Report 라인)"),
    106: (0.6, "비계 안전 점검 평가로 명확 - 건설 안전 실무 (Evaluation 라인)"),
    110: (0.6, "용접 사양·자격 요건 관리로 명확"),
    122: (0.6, "타악 과제 마감 관리로 명확 (Deadline 라인)"),
    123: (0.6, "만돌린 수강료 결제 관리로 명확 (Payment 라인)"),
    125: (0.6, "장난감 안전·적합성 평가로 명확 - 육아 실무 (Evaluation 라인)"),
    126: (0.6, "제품 확인 설문으로 명확"),
    145: (0.6, "합주 일지 관리로 명확 (Journal·Diary 라인)"),
    149: (0.6, "메일룸 운영 평가로 명확 - 시설관리 실무 (Evaluation 라인)"),
    150: (0.6, "곡집 확인 설문으로 명확"),
    165: (0.6, "비트 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    167: (0.6, "치과 환자 평가로 명확 - 치과 실무 (Evaluation 라인)"),
    172: (0.6, "기타 수강생 명단 관리로 명확 (Roster 라인)"),
    177: (0.6, "방송 편성·품질 평가로 명확 - 미디어 실무 (Evaluation 라인)"),
    178: (0.6, "롤백 요건 관리로 명확"),
    182: (0.6, "첼로 연습 로그 관리로 명확 (Log 라인)"),
    187: (0.6, "초과근무 평가로 명확 - HR 실무 (Evaluation 라인)"),
    188: (0.6, "비계 확인 설문으로 명확"),
    191: (0.6, "숙제 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "멜로디 파도 결합은 Wave 추상 불성립",
    2: "리듬 틀 결합은 Frame 불성립",
    3: "비트 게시판 결합은 Board 다의어 불명확",
    4: "피치 역 결합은 Station 불성립",
    6: "세탁 주문 감가상각 결합 불성립",
    7: "장례 구성 사직 결합은 Resignation 불성립",
    8: "선박에 튜너 결합 불성립",
    9: "피아노 감시 결합은 Watch 도구형 기각 라인",
    10: "기타 기둥·게시글 결합은 Post 다의어 불명확",
    11: "바이올린 회보 결합은 Bulletin 불성립 - 전달 성격 불명확",
    12: "드럼 마크업 결합은 Markup 기각 라인",
    14: "우쿨렐레 온도 결합은 Temperature 속성어 불성립",
    15: "롤백 활용률 결합 불성립 - Utilization",
    17: "티켓팅 감가상각 결합 불성립",
    18: "견종에 보증인 결합 불성립",
    19: "치과 차트에 튜너 결합 불성립",
    20: "플루트 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    25: "베이스 습도 결합은 Humidity 불성립",
    26: "바코드 평가 결합은 평가 대상 불성립",
    28: "숙제 활용률 결합 불성립 - Utilization",
    29: "용접 혜택 결합은 Benefit 추상 불명확",
    31: "기부에 감가상각 결합 불성립",
    32: "투표 사직 결합은 Resignation 불성립",
    33: "독자에 위험 결합 불성립",
    34: "카풀에 보증인 결합 불성립",
    35: "라우터에 튜너 결합 불성립",
    37: "검인 저울·규모 결합은 Scale 불성립",
    38: "하프 양식·형태 결합은 Form 다의어 불명확",
    39: "오보에 탭 결합은 Tab 불성립",
    40: "비올라 규칙 결합은 Rule 불성립",
    41: "트롬본 개요 결합은 Outline 불성립",
    42: "타액 예측 결합은 Forecast 불성립",
    43: "만돌린 개정 결합은 Revision 불성립",
    44: "아코디언 하중 결합은 Load 불성립",
    47: "점화 장치 활용률 결합 불성립 - Utilization",
    48: "림 혜택 결합은 대상 불성립",
    50: "계단 감가상각 결합 불성립",
    51: "촬영지 사직 결합은 Resignation 불성립",
    52: "장식에 위험 결합 불성립",
    53: "지붕에 보증인 결합 불성립",
    54: "밸브에 튜너 결합 불성립",
    55: "하모니카 데스크 결합은 Desk 추상 불성립",
    56: "레슨 콘솔 결합은 Console 도구형 불성립",
    58: "리사이탈 수준 결합은 Level 속성어 불성립",
    59: "오디션 회보 결합은 Bulletin 불성립",
    60: "조율 관세 결합은 Tariff 기각 라인",
    61: "이론 할인 결합은 Discount 기각 라인",
    62: "코드 위젯 결합은 Widget 불성립",
    63: "템포 사본 결합은 Copy 다의어 불명확",
    64: "레퍼토리 자격 결합은 대상 불성립",
    66: "반주자 폭 결합은 Width 속성어 불성립",
    67: "메트로놈 습도 결합은 Humidity 불성립",
    68: "증서 센서 결합은 Sensor 불성립",
    71: "파산 활용률 결합 불성립 - Utilization",
    73: "집안일 감가상각 결합 불성립",
    74: "보관 사직 결합은 Resignation 불성립",
    75: "교법에 위험 결합 불성립",
    76: "수분에 보증인 결합 불성립",
    77: "신탁에 튜너 결합 불성립",
    78: "캠프 데스크 결합은 Desk 추상 불성립",
    79: "합창 비컨 결합은 Beacon 추상 불성립",
    80: "퇴직 연쇄 결합은 Cascade 추상 불성립",
    81: "오케스트라 감시 결합은 Watch 도구형 기각 라인",
    82: "유산 루프 결합은 Loop 추상 불성립",
    83: "멜로디 경로 결합은 Path 추상 불성립",
    84: "리듬 베이스 결합은 Base 추상 불성립",
    85: "비트 데크 결합은 Deck 불성립",
    86: "피치 터미널 결합은 Terminal 불성립",
    88: "세탁 주문 사직 결합은 Resignation 불성립",
    89: "장례 구성에 위험 결합 불성립",
    90: "피아노 범위 결합은 Scope 불명확",
    91: "기타 항구 결합은 Harbor 불성립",
    92: "바이올린 브리핑 결합은 Brief 다의어 불명확",
    93: "드럼 상환·구속 결합은 Redemption 불성립",
    95: "우쿨렐레 압력 결합은 Pressure 속성어 불성립",
    96: "롤백 혜택 결합은 Benefit 추상 불명확",
    97: "스크리닝 감가상각 결합 불성립",
    98: "티켓팅 사직 결합은 Resignation 불성립",
    99: "견종에 튜너 결합 불성립",
    100: "플루트 게시판 결합은 Board 다의어 불명확",
    102: "색소폰 비용 결합은 Cost 속성어 불성립",
    103: "트럼펫 개요 결합은 Outline 불성립",
    104: "클라리넷 방송 결합은 Broadcast 불성립",
    105: "베이스 에피소드 결합은 Episode 불성립",
    107: "바코드 설문 결합은 불성립",
    108: "발렛 활용률 결합 불성립 - Utilization",
    109: "숙제 혜택 결합은 Benefit 추상 불명확",
    111: "트랙터 감가상각 결합 불성립",
    112: "기부 사직 결합은 Resignation 불성립",
    113: "투표에 위험 결합 불성립",
    114: "독자에 보증인 결합 불성립",
    115: "카풀에 튜너 결합 불성립",
    116: "오르간 콘솔 결합은 기기 본체를 지시해 서비스 불성립",
    117: "검인 경로 결합은 Route 불성립",
    118: "하프 카드 결합은 Card 다의어 불명확",
    119: "오보에 회보 결합은 Bulletin 불성립",
    120: "비올라 세부 결합은 Detail 속성어 불성립",
    121: "트롬본 렌더링 결합은 Rendering 불성립",
    124: "아코디언 전압 결합은 Voltage 불성립",
    127: "투약 활용률 결합 불성립 - Utilization",
    128: "점화 장치 혜택 결합은 Benefit 추상 불명확",
    129: "림 요건 결합은 대상 불성립",
    130: "관용구 감가상각 결합 불성립",
    131: "계단 사직 결합은 Resignation 불성립",
    132: "촬영지에 위험 결합 불성립",
    133: "장식에 보증인 결합 불성립",
    134: "지붕에 튜너 결합 불성립",
    135: "하모니카 레이더 결합은 Radar 추상 불성립",
    136: "레슨 패널 결합은 Panel 불성립",
    137: "연습 키오스크 결합은 Kiosk 불성립",
    138: "리사이탈 요율 결합은 Rate 속성어 불성립",
    139: "오디션 브리핑 결합은 Brief 다의어 불명확",
    140: "조율 가치 결합은 Value 속성어 불성립",
    141: "이론 체납 결합은 Arrears 기각 라인",
    142: "코드 저장소 결합은 Repository 기술용어 불명확",
    143: "템포 판독 결합은 Reading 다의어 불명확",
    144: "레퍼토리 방송 결합은 Broadcast 불성립",
    146: "반주자 온도 결합은 Temperature 속성어 불성립",
    147: "메트로놈 에피소드 결합은 Episode 불성립",
    148: "증서 접수 결합은 Reception 불성립",
    151: "스트레칭 활용률 결합 불성립 - Utilization",
    152: "파산 혜택 결합은 Benefit 추상 불명확",
    153: "석조 감가상각 결합 불성립",
    154: "집안일 사직 결합은 Resignation 불성립",
    155: "보관에 위험 결합 불성립",
    156: "교법에 보증인 결합 불성립",
    157: "수분에 튜너 결합 불성립",
    158: "캠프 레이더 결합은 Radar 추상 불성립",
    159: "합창 대장간 결합은 Forge 불성립",
    160: "퇴직 브리지 결합은 Bridge 기각 라인",
    161: "오케스트라 범위 결합은 Scope 불명확",
    162: "유산 격자 결합은 Grid 추상 불성립",
    163: "멜로디 포인트 결합은 Point 불성립",
    164: "리듬 코어 결합은 Core 불성립",
    166: "피치 센터 결합은 Center 불성립",
    168: "등록 활용률 결합 불성립 - Utilization",
    169: "세탁 주문에 위험 결합 불성립",
    170: "장례 구성에 보증인 결합 불성립",
    171: "피아노 루프 결합은 Loop 추상 불성립",
    173: "바이올린 회람 결합은 Circular 불성립",
    174: "드럼 연장 결합은 Extension 불성립",
    175: "보컬 회신 결합은 Reply 불성립",
    176: "우쿨렐레 하중 결합은 Load 불성립",
    179: "스크리닝 사직 결합은 Resignation 불성립",
    180: "티켓팅에 위험 결합 불성립",
    181: "플루트 데크 결합은 Deck 불성립",
    183: "색소폰 가격 결합은 Price 속성어 불성립",
    184: "트럼펫 렌더링 결합은 Rendering 불성립",
    185: "클라리넷 바코드 결합은 불성립",
    186: "베이스 주기 결합은 Cycle 불성립",
    189: "바코드 활용률 결합 불성립 - Utilization",
    190: "발렛 혜택 결합은 Benefit 추상 불명확",
    192: "용접 감가상각 결합 불성립",
    193: "트랙터 사직 결합은 Resignation 불성립",
    194: "기부에 위험 결합 불성립",
    195: "투표에 보증인 결합 불성립",
    196: "독자에 튜너 결합 불성립",
    197: "오르간 패널 결합은 Panel 불성립",
    198: "검인 궤도 결합은 Rail 불성립",
    199: "하프 시트 결합은 Sheet 다의어 불명확",
    200: "오보에 브리핑 결합은 Brief 다의어 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 39, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 161, len(REJECT_REASON)
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
