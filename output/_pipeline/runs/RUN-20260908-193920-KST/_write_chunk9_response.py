import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk8_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk8_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "치과 차트 작성 기준 요건 관리로 명확"),
    8: (0.6, "트럼펫 연주 지침 매뉴얼 관리로 명확 (Playbook 라인 준용)"),
    11: (0.6, "기부금 운용·처리 평가로 명확 - 비영리 실무 (Evaluation 라인)"),
    12: (0.6, "투표 의견 설문으로 명확"),
    15: (0.6, "네트워크 구축 요건 관리로 명확"),
    24: (0.6, "오보에 성취 배지 관리로 명확 (Badge 라인)"),
    26: (0.6, "트롬본 연습 워크시트 관리로 명확 (Worksheet 라인)"),
    30: (0.6, "이사 계단 운반 조건 평가로 명확 - 이사 실무 (Evaluation 라인)"),
    31: (0.6, "촬영지 확인 설문으로 명확"),
    34: (0.6, "밸브 규격·점검 요건 관리로 명확"),
    41: (0.6, "연습실 디렉터리 관리로 명확 (Directory 라인)"),
    46: (0.6, "코드 연습 알림 관리로 명확 (Notification·Alert 라인)"),
    49: (0.6, "합주 시뮬레이션 도구로 명확 - 실재 도구"),
    54: (0.6, "아이 집안일 수행 평가로 명확 - 육아 실무 (Evaluation 라인)"),
    55: (0.6, "보관 시설 인테이크 설문으로 명확"),
    58: (0.6, "신탁 설립 요건 관리로 명확"),
    72: (0.6, "세탁 주문 확인 설문으로 명확"),
    81: (0.6, "보컬 연습 진도 관리로 명확 (Progress 라인)"),
    83: (0.6, "서류 전형(screening) 평가로 명확 - 채용 실무 (Evaluation 라인)"),
    84: (0.6, "티켓 구매 설문으로 명확"),
    85: (0.6, "견종 등록·사육 요건 관리로 명확"),
    89: (0.6, "플루트 레슨 진행 지도로 명확 (Map 라인)"),
    92: (0.6, "트럼펫 연습 워크시트 관리로 명확 (Worksheet 라인)"),
    95: (0.6, "트랙터 상태·구매 평가로 명확 - 농업 실무 (Evaluation 라인)"),
    96: (0.6, "기부 인테이크 설문으로 명확"),
    99: (0.6, "카풀 참가 요건 관리로 명확"),
    110: (0.6, "트롬본 운주법 다이어그램 관리로 명확 (Diagram 라인)"),
    111: (0.6, "타악 연습 기록 관리로 명확 (Record 라인)"),
    112: (0.6, "만돌린 레슨 예약금 관리로 명확 (Deposit 라인)"),
    114: (0.6, "번역 관용구(idiom) 처리 평가로 명확 - 통번역 실무 (Evaluation 라인)"),
    115: (0.6, "계단 작업 확인 설문으로 명확"),
    118: (0.6, "지붕 시공·점검 요건 관리로 명확"),
    138: (0.6, "석조 시공 품질 평가로 명확 - 건설 실무 (Evaluation 라인)"),
    139: (0.6, "집안일 확인 설문으로 명확"),
    142: (0.6, "수분 섭취 권장 기준 관리로 명확"),
    145: (0.6, "목공 작업 안전 위험 관리로 명확 - 물리 위험 실존 (Callout Hazard 준용)"),
    159: (0.6, "운항 안전 위험 관리로 명확 - 항공 안전 실무 (물리 위험 라인)"),
    161: (0.6, "기타 연습 부스 예약 관리로 명확 (Booth 라인)"),
    162: (0.6, "바이올린 레슨 메모 관리로 명확 (Memo 라인)"),
    166: (0.6, "스크리닝 인테이크 설문으로 명확"),
    173: (0.6, "색소폰 수강료 관리로 명확 (Fee 라인, Tuning Fee 준용)"),
    174: (0.6, "트럼펫 운주법 다이어그램 관리로 명확 (Diagram 라인)"),
    177: (0.6, "용접 품질 평가로 명확 - 제조 실무 (Evaluation 라인)"),
    178: (0.6, "트랙터 확인 설문으로 명확"),
    189: (0.6, "하프 출연 명단 관리로 명확 (Roll 라인)"),
    192: (0.6, "트롬본 구조·운주 도식 관리로 명확 (Schematic 라인)"),
    194: (0.6, "만돌린 인증 관리로 명확 (Certification 라인)"),
    197: (0.6, "관용구 확인 설문으로 명확"),
    200: (0.6, "장식 시공 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "견종 혜택 결합은 Benefit 추상 불명확",
    3: "활력징후에 위험 결합 불성립",
    4: "반복(recurring)에 보증인 결합 불성립",
    5: "플루트 포인트 결합은 Point 불명확",
    6: "첼로 여권 결합은 Passport 기각 라인",
    7: "색소폰 회고 결합은 Recap 불성립",
    9: "클라리넷 검증 결합은 Validation 불성립",
    10: "베이스 빈도 결합은 Frequency 속성어 불성립",
    13: "독자 활용률 결합 불성립 - Utilization",
    14: "카풀 혜택 결합은 Benefit 추상 불명확",
    16: "비밀번호에 감가상각 결합 불성립",
    17: "클라우드 사직 결합은 Resignation 불성립",
    18: "문의에 위험 결합 불성립",
    19: "이력서에 보증인 결합 불성립",
    20: "연사에 튜너 결합 불성립",
    21: "오르간 실험실 결합은 Lab 불성립",
    22: "검인 센터 결합은 Probate 추상 기각 라인",
    23: "하프 라인 결합은 Line 추상 불명확",
    25: "비올라 마진 결합은 Margin 기각 라인",
    27: "타악 보증 결합은 Guarantee 불성립",
    28: "만돌린 보증 결합은 Warranty 불성립",
    29: "아코디언 깊이 결합은 Depth 속성어 불성립",
    32: "장식 활용률 결합 불성립 - Utilization",
    33: "지붕 혜택 결합은 Benefit 추상 불명확",
    35: "세차천에 감가상각 결합 불성립",
    36: "역류 사직 결합은 Resignation 불성립",
    37: "사파리에 위험 결합 불성립",
    38: "하모니카에 보증인 결합 불성립",
    39: "용량에 튜너 결합 불성립",
    40: "레슨 역 결합은 Station 불성립",
    42: "리사이탈 프로필 결합은 Profile 불성립",
    43: "오디션 스텁 결합은 Stub 불성립",
    44: "조율 현금 결합은 Cash 불성립",
    45: "이론 이자 결합은 Interest 기각 라인",
    47: "템포 추세 결합은 Trend 불성립",
    48: "레퍼토리 검증 결합은 Validation 불성립",
    50: "반주자 시계 결합은 Clock 불성립",
    51: "메트로놈 빈도 결합은 Frequency 속성어 불성립",
    52: "증서 상태·조건 결합은 Condition 다의어 불명확",
    53: "곡집 센서 결합은 Sensor 불성립",
    56: "교법 활용률 결합 불성립 - Utilization",
    57: "수분 혜택 결합은 Benefit 추상 불명확",
    59: "공제에 감가상각 결합 불성립",
    60: "목공 사직 결합은 Resignation 불성립",
    61: "피트니스에 위험 결합 불성립",
    62: "캠프에 보증인 결합 불성립",
    63: "자세에 튜너 결합 불성립",
    64: "합창 데스크 결합은 Desk 추상 불성립",
    65: "퇴직 릴레이 결합은 Relay 불성립",
    66: "오케스트라 비컨 결합은 Beacon 추상 불성립",
    67: "유산 연쇄 결합은 Cascade 추상 불성립",
    68: "멜로디 감시 결합은 Watch 도구형 기각 라인",
    69: "리듬 파도 결합은 Wave 추상 불성립",
    70: "비트 틀 결합은 Frame 불성립",
    71: "피치 게시판 결합은 Board 다의어 불명확",
    73: "장례 구성 활용률 결합 불성립 - Utilization",
    74: "선박에 감가상각 결합 불성립",
    75: "비행 사직 결합은 Resignation 불성립",
    76: "키웨이에 튜너 결합 불성립",
    77: "피아노 대장간 결합은 Forge 불성립",
    78: "기타 카운터 결합은 Counter 불성립",
    79: "바이올린 명세서·진술 결합은 Statement 다의어 불명확",
    80: "드럼 할인 결합은 Discount 불성립",
    82: "우쿨렐레 속도 결합은 Speed 속성어 불성립",
    86: "치과 차트에 감가상각 결합 불성립",
    87: "활력징후에 보증인 결합 불성립",
    88: "반복(recurring)에 튜너 결합 불성립",
    90: "첼로 로비 결합은 Lobby 불성립",
    91: "색소폰 항목·입장 결합은 Entry 다의어 불명확",
    93: "클라리넷 조회 결합은 Lookup 불성립",
    94: "베이스 호환성 결합은 Compatibility 불성립",
    97: "투표 활용률 결합 불성립 - Utilization",
    98: "독자 혜택 결합은 Benefit 추상 불명확",
    100: "라우터에 감가상각 결합 불성립",
    101: "비밀번호 사직 결합은 Resignation 불성립",
    102: "클라우드에 위험 결합 불성립",
    103: "문의에 보증인 결합 불성립",
    104: "이력서에 튜너 결합 불성립",
    105: "오르간 역 결합은 Station 불성립",
    106: "검인 구역 결합은 Probate 추상 기각 라인",
    107: "하프 창·기간 결합은 Window 다의어 불명확",
    108: "오보에 스텁 결합은 Stub 불성립",
    109: "비올라 벌금 결합은 Fine 기각 라인",
    113: "아코디언 높이 결합은 Height 속성어 불성립",
    116: "촬영지 활용률 결합 불성립 - Utilization",
    117: "장식 혜택 결합은 Benefit 추상 불명확",
    119: "밸브에 감가상각 결합 불성립",
    120: "세차천 사직 결합은 Resignation 불성립",
    121: "역류에 위험 결합 불성립",
    122: "사파리에 보증인 결합 불성립",
    123: "하모니카에 튜너 결합 불성립",
    124: "레슨 터미널 결합은 Terminal 불성립",
    125: "연습 로케이터 결합은 검색 대상 불명확",
    126: "리사이탈 상태 결합은 Status 불성립",
    127: "오디션 명세서·진술 결합은 Statement 다의어 불명확",
    128: "조율 판매 결합은 Sale 불성립",
    129: "이론 자산 결합은 Asset 단독 불명확",
    130: "코드 키트 결합은 Kit 불성립",
    131: "템포 비교 결합은 비교 대상 불명확",
    132: "레퍼토리 조회 결합은 Lookup 불성립",
    133: "합주 예측기 결합은 Predictor 불성립",
    134: "반주자 시간 결합은 Time 속성어 불성립",
    135: "메트로놈 호환성 결합은 Compatibility 불성립",
    136: "증서 습도 결합은 Humidity 불성립",
    137: "곡집에 접수 결합 불성립",
    140: "보관 시설 활용률 결합 불성립 - Utilization",
    141: "교법 혜택 결합은 Benefit 추상 불명확",
    143: "신탁에 감가상각 결합 불성립",
    144: "공제 사직 결합은 Resignation 불성립",
    146: "피트니스에 보증인 결합 불성립",
    147: "캠프에 튜너 결합 불성립",
    148: "합창 레이더 결합은 Radar 추상 불성립",
    149: "퇴직 금고 결합은 Vault 추상 불성립",
    150: "오케스트라 대장간 결합은 Forge 불성립",
    151: "유산 브리지 결합은 Bridge 기각 라인",
    152: "멜로디 범위 결합은 Scope 불명확",
    153: "리듬 경로 결합은 Path 추상 불성립",
    154: "비트 베이스 결합은 Base 추상 불성립",
    155: "피치 데크 결합은 Deck 불성립 - 스타트업 발표자료 오독 위험",
    156: "주문 활용률 결합 불성립 - Utilization",
    157: "장례 구성 혜택 결합은 Benefit 추상 불명확",
    158: "선박 사직 결합은 Resignation 불성립",
    160: "피아노 연쇄 결합은 Cascade 추상 불성립",
    163: "드럼 체납 결합은 Arrears 기각 라인",
    164: "보컬에 승인 결합 불성립 - 승인 대상 불성립",
    165: "우쿨렐레 깊이 결합은 Depth 속성어 불성립",
    167: "티켓팅 활용률 결합 불성립 - Utilization",
    168: "견종에 감가상각 결합 불성립",
    169: "치과 차트 사직 결합은 Resignation 불성립",
    170: "활력징후에 튜너 결합 불성립",
    171: "플루트 틀 결합은 Frame 불성립",
    172: "첼로 티커 결합은 Ticker 불성립",
    175: "클라리넷 핑 결합은 Ping 불성립",
    176: "베이스 용량 결합은 Capacity 속성어 불성립",
    179: "기부 활용률 결합 불성립 - Utilization",
    180: "투표 혜택 결합은 Benefit 추상 불명확",
    181: "독자에 요건 결합 불성립",
    182: "카풀에 감가상각 결합 불성립",
    183: "라우터 사직 결합은 Resignation 불성립",
    184: "비밀번호에 위험 결합 불성립",
    185: "클라우드에 보증인 결합 불성립",
    186: "문의에 튜너 결합 불성립",
    187: "오르간 터미널 결합은 Terminal 불성립",
    188: "검인 포털 결합은 Probate 도구형 기각 라인",
    190: "오보에 명세서·진술 결합은 Statement 다의어 불명확",
    191: "비올라 번호 결합은 Number 불성립",
    193: "타악 사본·광고문 결합은 Copy 다의어 불명확",
    195: "아코디언 폭 결합은 Width 속성어 불성립",
    196: "림 평가 결합은 평가 대상 불성립",
    198: "계단 활용률 결합 불성립 - Utilization",
    199: "촬영지 혜택 결합은 Benefit 추상 불명확",
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
