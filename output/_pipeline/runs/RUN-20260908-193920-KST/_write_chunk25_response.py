import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk24_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk24_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "블로우아웃 요건 관리로 명확 (Requirement 라인)"),
    10: (0.6, "레슨 출석 명부 관리로 명확 (Roster 라인)"),
    11: (0.6, "연습 타임라인 관리로 명확 (Timeline 라인)"),
    14: (0.6, "조율 매뉴얼 관리로 명확 (Manual 라인)"),
    16: (0.6, "코드 연습 평점 관리로 명확 (Rating 라인)"),
    20: (0.6, "파티오 시공 평가로 명확 - 건설 실무 (Evaluation 라인)"),
    22: (0.6, "적성 요건 관리로 명확 (Requirement 라인)"),
    35: (0.6, "유산 절차 스케줄러로 명확 (Scheduler 라인)"),
    36: (0.6, "멜로디 기록 대장 관리로 명확 (Register 라인)"),
    37: (0.6, "리듬 기록 등록부 관리로 명확 (Registry 라인)"),
    41: (0.6, "피아노 연습 플래너로 명확 (Planner 라인)"),
    42: (0.6, "기타 레슨 견적 관리로 명확 (Estimate 라인)"),
    44: (0.6, "드럼 파트 서열 관리로 명확 (Rank 라인)"),
    45: (0.6, "보컬 소식지 관리로 명확 (Announcement 준용 라인)"),
    46: (0.6, "제품 판매 수수료 평가로 명확 - 미용 실무 (Evaluation 라인)"),
    47: (0.6, "조제 확인 설문으로 명확"),
    54: (0.6, "첼로 바우처 관리로 명확 (Voucher 라인)"),
    58: (0.6, "발달 이정표 요건 관리로 명확 (Requirement 라인)"),
    61: (0.6, "오르간 출석 명부 관리로 명확 (Roster 라인)"),
    63: (0.6, "하프 레슨 정산 명세 관리로 명확 (Statement 라인)"),
    67: (0.6, "타액 시뮬레이터로 실재 도구 (Simulator 라인)"),
    69: (0.6, "벼룩 확인 설문으로 명확"),
    72: (0.6, "식기세척기 요건 관리로 명확 (Requirement 라인)"),
    80: (0.6, "레슨 알림 관리로 명확 (Alert 라인)"),
    81: (0.6, "연습 리마인더로 명확 (Reminder 라인)"),
    82: (0.6, "리사이탈 참가비 관리로 명확 (Fee 라인)"),
    84: (0.6, "조율 체크 워크시트 관리로 명확 (Worksheet 라인)"),
    90: (0.6, "직무 교육 평가로 명확 - HR 실무 (Evaluation 라인)"),
    91: (0.6, "파티오 확인 설문으로 명확"),
    92: (0.6, "기능 요건 관리로 명확 (Requirement 라인)"),
    104: (0.6, "오케스트라 일정 플래너로 명확 (Planner 라인)"),
    105: (0.6, "유산 절차 모니터링 관리로 명확 (Monitor 라인)"),
    107: (0.6, "리듬 연습 캘린더로 명확 (Calendar 라인)"),
    108: (0.6, "비트 연습 사무 관리로 명확 (Office 라인)"),
    110: (0.6, "피아노 연습 스케줄러로 명확 (Scheduler 라인)"),
    111: (0.6, "기타 공연 순서 관리로 명확 (Order 라인)"),
    114: (0.6, "보컬 교재·자료 목록 관리로 명확 (Inventory 라인)"),
    115: (0.6, "묘지 관리 평가로 명확 - 장례 실무 (Evaluation 라인)"),
    116: (0.6, "수수료 확인 설문으로 명확"),
    123: (0.6, "첼로 배지 관리로 명확 (Badge 라인)"),
    129: (0.6, "오르간 레슨 알림 관리로 명확 (Alert 라인)"),
    131: (0.6, "하프 레슨 메모 관리로 명확 (Memo 라인)"),
    134: (0.6, "트롬본 연주 진단으로 실재 도구 (Diagnostic 라인)"),
    137: (0.6, "행사 랜야드 품질 평가로 명확 - 행사 실무 (Evaluation 라인)"),
    140: (0.6, "공예 요건 관리로 명확 (Requirement 라인)"),
    148: (0.6, "레슨 진도 차트 관리로 명확 (Chart 라인)"),
    152: (0.6, "조율 절차 도식 관리로 명확 (Diagram 라인)"),
    158: (0.6, "보험 보상 조정 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    159: (0.6, "교육 확인 설문으로 명확"),
    172: (0.6, "오케스트라 일정 스케줄러로 명확 (Scheduler 라인)"),
    174: (0.6, "멜로디 작업 플레이북 관리로 명확 (Playbook 라인)"),
    175: (0.6, "리듬 기록 디렉터리 관리로 명확 (Directory 라인)"),
    178: (0.6, "피아노 연습 모니터링 관리로 명확 (Monitor 라인)"),
    179: (0.6, "기타 레슨 청구서 관리로 명확 (Bill 라인)"),
    183: (0.6, "세탁 요금 구조 평가로 명확 - 세탁 실무 (Evaluation 라인)"),
    184: (0.6, "묘지 확인 설문으로 명확"),
    191: (0.6, "플루트 연습 사무 관리로 명확 (Office 라인)"),
    194: (0.6, "트럼펫 연주 진단으로 실재 도구 (Diagnostic 라인)"),
    198: (0.6, "오르간 진도 차트 관리로 명확 (Chart 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "공예 활용률 결합 불성립 - Utilization",
    2: "식기세척기 혜택 결합은 Benefit 추상 불명확",
    4: "흡입기 감가상각 결합 불성립",
    5: "제습기 사직 결합은 Resignation 불성립",
    6: "자물쇠 홈에 위험 결합 불성립",
    7: "구문에 보증인 결합 불성립",
    8: "아코디언 나침반 결합은 Compass 추상 불성립",
    9: "하모니카 궤도 결합은 Rail 불성립",
    12: "리사이탈 항목 결합은 Entry 다의어 불명확",
    13: "오디션 식별자 결합은 Identifier 불성립",
    15: "이론 수호자 결합은 Guardian 추상 불성립",
    17: "템포에 교정 결합은 불성립",
    18: "레퍼토리 한도 결합은 Limit 속성어 불성립",
    19: "합주 주기 결합은 Cycle 속성어 불성립",
    21: "기능 혜택 결합은 Benefit 추상 불명확",
    23: "식이에 위험 결합 불성립",
    24: "교정에 보증인 결합 불성립",
    25: "유모차에 튜너 결합 불성립",
    26: "반주자 레이더 결합은 Radar 추상 불성립",
    27: "메트로놈 격자 결합은 Grid 불성립",
    28: "증서에 지도 결합은 불성립",
    29: "곡집 게시판 결합은 Board 다의어 불명확",
    30: "교법 존 결합은 Zone 불성립",
    31: "캠프 궤도 결합은 Rail 불성립",
    32: "합창 연결점 결합은 Nexus 추상 불성립",
    33: "퇴직 관리자 결합은 Keeper 불명확 기각 라인",
    34: "오케스트라 조수 결합은 Assistant 불명확 기각 라인",
    38: "비트 검색기 결합은 Finder 불성립",
    39: "피치 키오스크 결합은 Kiosk 불성립",
    40: "화물에 튜너 결합 불성립",
    43: "바이올린 분류 결합은 Category 속성어 불성립",
    48: "여과 감가상각 결합 불성립",
    49: "마스터키 사직 결합은 Resignation 불성립",
    50: "용어에 위험 결합 불성립",
    51: "갤러리에 튜너 결합 불성립",
    52: "우쿨렐레 금고 결합은 Vault 불성립",
    53: "플루트 검색기 결합은 Locator/Finder 불성립",
    55: "색소폰 부과금 결합은 Levy 기각 라인",
    56: "트럼펫 지속시간 결합은 Duration 불성립",
    57: "클라리넷 유형 결합은 Type 속성어 불성립",
    59: "수선에 튜너 결합 불성립",
    60: "베이스 파도 결합은 Wave 추상 불성립",
    62: "검인 상자 결합은 Bin 불성립",
    64: "오보에 식별자 결합은 Identifier 불성립",
    65: "비올라 키트 결합은 Kit 불성립",
    66: "트롬본 음량 결합은 Volume 다의어 불명확",
    68: "만돌린 주파수 결합은 Frequency 불성립",
    70: "잇몸 활용률 결합 불성립 - Utilization",
    71: "공예 혜택 결합은 Benefit 추상 불명확",
    73: "블로우아웃 감가상각 결합 불성립",
    74: "흡입기 사직 결합은 Resignation 불성립",
    75: "제습기에 위험 결합 불성립",
    76: "자물쇠 홈에 보증인 결합 불성립",
    77: "구문에 튜너 결합 불성립",
    78: "아코디언 등대 결합은 Beacon 추상 불성립",
    79: "하모니카 흔적 결합은 Trail 불성립",
    83: "오디션 분류 결합은 Category 속성어 불성립",
    85: "이론 조수 결합은 Helper 불명확 기각 라인",
    86: "코드 계약 결합은 불성립",
    87: "템포 수정 결합은 Revision 기각 라인",
    88: "레퍼토리 유형 결합은 Type 속성어 불성립",
    89: "합주 고장 분석 결합은 Breakdown 다의어 불명확",
    93: "적성 감가상각 결합 불성립",
    94: "식이에 보증인 결합 불성립",
    95: "교정에 튜너 결합 불성립",
    96: "반주자 릴레이 결합은 Relay 불성립",
    97: "메트로놈 파도 결합은 Wave 추상 불성립",
    98: "증서 틀 결합은 Frame 불성립",
    99: "곡집 데크 결합은 Deck 불성립",
    100: "교법 포털 결합은 Portal 불성립",
    101: "캠프 흔적 결합은 Trail 불성립",
    102: "합창 대성지도 결합은 Atlas 추상 불성립",
    103: "퇴직 관리자 결합은 Manager 불성립",
    106: "멜로디 운영 결합은 Ops 불명확",
    109: "피치 구역 결합은 Bay 불성립",
    112: "바이올린 속성 결합은 Attribute 속성어 불성립",
    113: "드럼 추세 결합은 Trend 불성립",
    117: "조제 활용률 결합 불성립 - Utilization",
    118: "여과 사직 결합은 Resignation 불성립",
    119: "마스터키에 위험 결합은 서비스 대상 불성립",
    120: "용어에 보증인 결합 불성립",
    121: "우쿨렐레 나침반 결합은 Compass 추상 불성립",
    122: "플루트 검색기 결합은 Finder 불성립",
    124: "색소폰 기한/분 결합은 Due 다의어 불명확",
    125: "트럼펫 음량 결합은 Volume 다의어 불명확",
    126: "클라리넘 시계 결합은 Clock 불성립",
    127: "이정표 감가상각 결합 불성립",
    128: "베이스 경로 결합은 Path 추상 불성립",
    130: "검인 여권 결합은 Passport 불성립",
    132: "오보에 분류 결합은 Category 속성어 불성립",
    133: "비올라 개수 결합은 Count 속성어 불성립",
    135: "타액 예측기 결합은 Predictor 불성립",
    136: "만돌린 호환성 결합은 Compatibility 불성립",
    138: "벼룩 활용률 결합 불성립 - Utilization",
    139: "잇몸 혜택 결합은 Benefit 추상 불명확",
    141: "식기세척기 감가상각 결합 불성립",
    142: "블로우아웃 사직 결합은 Resignation 불성립",
    143: "흡입기에 위험 결합 불성립",
    144: "제습기에 보증인 결합 불성립",
    145: "자물쇠 홈에 튜너 결합 불성립",
    146: "아코디언 대장간 결합은 Forge 불성립",
    147: "하모니카 체인 결합은 Chain 추상 불성립",
    149: "연습 색인 결합은 Index 다의어 불명확",
    150: "리사이탈 항목 결합은 Item 다의어 불명확",
    151: "오디션 속성 결합은 Attribute 속성어 불성립",
    153: "이론 무대 결합은 불성립",
    154: "코드 답장 결합은 Reply 불성립",
    155: "템포에 결제 결합 불성립",
    156: "레퍼토리 시계 결합은 Clock 불성립",
    157: "합주 센서 결합은 Sensor 불성립",
    160: "파티오 활용률 결합 불성립 - Utilization",
    161: "기능 감가상각 결합 불성립",
    162: "적성 사직 결합은 Resignation 불성립",
    163: "식이에 튜너 결합 불성립",
    164: "반주자 금고 결합은 Vault 불성립",
    165: "메트로놈 경로 결합은 Path 추상 불성립",
    166: "증서 거점 결합은 Base 불성립",
    167: "곡집 스튜디오 결합은 불성립",
    168: "교법 콘솔 결합은 Console 불성립",
    169: "캠프 체인 결합은 Chain 추상 불성립",
    170: "합창 관리자 결합은 Keeper 불명확 기각 라인",
    171: "퇴직 엔진 결합은 Engine 추상 불성립",
    173: "유산 동반자 결합은 Companion 불명확 기각 라인",
    176: "비트 카운터 결합은 Counter 다의어 불명확",
    177: "피치 게시물 결합은 Post 다의어 불명확",
    180: "바이올린 분야 결합은 Field 불성립",
    181: "드럼 비교 결합은 Comparison 불성립",
    182: "보컬 청구 결합은 Claim 다의어 불명확",
    185: "수수료 활용률 결합 불성립 - Utilization",
    186: "조제 혜택 결합은 Benefit 추상 불명확",
    187: "여과에 위험 결합 불성립",
    188: "마스터키에 보증인 결합 불성립",
    189: "용어에 튜너 결합 불성립",
    190: "우쿨렐레 등대 결합은 Beacon 추상 불성립",
    192: "첼로 보관 즉시 결제 증서 결합은 Stub 불성립",
    193: "색소폰 보조금 결합은 Subsidy 기각 라인",
    195: "클라리넷 시간 결합은 Time 속성어 불성립",
    196: "이정표 사직 결합은 Resignation 불성립",
    197: "베이스 포인트 결합은 Point 불성립",
    199: "검인 로비 결합은 Lobby 불성립",
    200: "하프 할당량 결합은 Quota 속성어 불성립",
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
