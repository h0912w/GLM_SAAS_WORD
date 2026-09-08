import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk7_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk7_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "수분 상태(hydration) 평가로 명확 - 임상 실무 (Evaluation 라인)"),
    4: (0.6, "신탁 인테이크 설문으로 명확"),
    7: (0.6, "피트니스 시설 이용·설치 요건 관리로 명확"),
    13: (0.6, "합창단 출석·진도 추적으로 명확 (Tracker 라인)"),
    29: (0.6, "바이올린 수강 바우처 관리로 명확 (Voucher 라인)"),
    33: (0.6, "견종 확인 설문으로 명확"),
    39: (0.6, "첼로 진도 차트 관리로 명확 (Chart 라인)"),
    44: (0.6, "독자 반응·만족 평가로 명확 - 출판 실무 (Evaluation 라인)"),
    45: (0.6, "카풀 인테이크 설문으로 명확"),
    48: (0.6, "클라우드 구축 요건 관리로 명확"),
    61: (0.6, "만돌린 수강 등록 갱신 관리로 명확 (Renewal 라인)"),
    63: (0.6, "결혼식 장식 품질·선호 평가로 명확 (Evaluation 라인)"),
    64: (0.6, "지붕 점검 인테이크 설문으로 명확"),
    67: (0.6, "역류 방지 장치 요건 관리로 명확"),
    73: (0.6, "레슨 스튜디오 예약·관리로 명확 - 실재 시설"),
    74: (0.6, "연습 기록 등록부 관리로 명확 (Registry 라인)"),
    75: (0.6, "연주회 준비 메모 관리로 명확 (Memo 라인 준용)"),
    76: (0.6, "오디션 수강권 바우처 관리로 명확 (Voucher 라인)"),
    80: (0.6, "연속 연습 기록 관리로 명확 (Streak 라인)"),
    82: (0.6, "합주 공연비 결제 관리로 명확"),
    87: (0.6, "레슨 방식 효과 평가로 명확 (Evaluation 라인)"),
    88: (0.6, "수분 섭취 자가 설문으로 명확"),
    91: (0.6, "목공 시공 요건 관리로 명확"),
    105: (0.6, "장례 구성(arrangement) 평가로 명확 - 장례 실무 (Evaluation 라인)"),
    107: (0.6, "비행 훈련·운항 요건 관리로 명확"),
    113: (0.6, "바이올린 성취 배지 관리로 명확 (Badge 라인)"),
    123: (0.6, "색소폰 예약 확인 관리로 명확 (Confirmation 라인)"),
    125: (0.6, "클라리넷 강사·학생 매칭 관리로 명확 (Match 라인)"),
    127: (0.6, "투표 시스템·절차 평가로 명확 - 행정 실무 (Evaluation 라인)"),
    128: (0.6, "독자 설문으로 명확"),
    131: (0.6, "비밀번호 규정 요건 관리로 명확"),
    137: (0.6, "오르간 레슨 스튜디오 예약 관리로 명확 (Studio 라인)"),
    140: (0.6, "오보에 수강 바우처 관리로 명확 (Voucher 라인)"),
    142: (0.6, "트롬본 연주 지침 매뉴얼 관리로 명확 (Playbook 라인 준용)"),
    144: (0.6, "만돌린 레슨비 견적 관리로 명확 (Quote 라인)"),
    146: (0.6, "촬영지(location) 평가로 명확 - 촬영 실무 (Evaluation 라인)"),
    147: (0.6, "장식 선호 설문으로 명확"),
    157: (0.6, "연습 일정 캘린더 관리로 명확 (Calendar 라인)"),
    170: (0.6, "창고·보관 시설 평가로 명확 - 시설 실무 (Evaluation 라인)"),
    171: (0.6, "레슨 방식 선호 설문으로 명확"),
    174: (0.6, "공제 적용 요건 관리로 명확"),
    186: (0.6, "리듬 패턴 지도 관리로 명확 (Map 라인)"),
    188: (0.6, "세탁 주문 처리 품질 평가로 명확 (Evaluation 라인)"),
    189: (0.6, "장례 구성 확인 설문으로 명확"),
    190: (0.6, "선박 운항·검사 요건 관리로 명확"),
    195: (0.6, "기타 학원 운영 사무 관리로 명확 (Office 라인)"),
    198: (0.6, "보컬 발성 진단으로 명확 (Diagnostic 라인)"),
    200: (0.6, "티켓 판매·운영 평가로 명확 - 행사 실무 (Evaluation 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "곡집 에피소드 결합은 Episode 불명확",
    2: "교법 행렬 결합은 Matrix 추상 불성립",
    5: "공제 활용률 결합 불성립 - Utilization",
    6: "목공 혜택 결합은 Benefit 추상 불명확",
    8: "캠프에 감가상각 결합 불성립",
    9: "자세 사직 결합은 Resignation 불성립",
    10: "자산에 위험 결합 불성립",
    11: "유예(grace)에 보증인 결합 불성립",
    12: "옥상에 튜너 결합 불성립",
    14: "퇴직 허브 결합은 Hub 추상 불성립",
    15: "오케스트라 릴레이 결합은 Relay 불성립",
    16: "유산 나침반 결합은 Compass 불명확 은유",
    17: "멜로디 연쇄 결합은 Cascade 추상 불성립",
    18: "리듬 범위 결합은 Scope 불명확",
    19: "비트 경로 결합은 Path 추상 불성립",
    20: "피치 베이스 결합은 Base 추상 불성립",
    21: "선박 활용률 결합 불성립 - Utilization",
    22: "비행 혜택 결합은 Benefit 추상 불명확",
    23: "키웨이 사직 결합은 Resignation 불성립",
    24: "용어집에 위험 결합 불성립",
    25: "이사에 보증인 결합 불성립",
    26: "촬영에 튜너 결합 불성립",
    27: "피아노 금고 결합은 Vault 추상 불성립",
    28: "기타 로케이터 결합은 검색 대상 불명확",
    30: "드럼 부과금 결합은 Levy 불성립",
    31: "보컬 기간 결합은 Duration 속성어 불성립",
    32: "우쿨렐레 유형 결합은 Type 속성어 불성립",
    34: "치과 차트 활용률 결합 불성립 - Utilization",
    35: "활력징후에 감가상각 결합 불성립",
    36: "반복(recurring) 사직 결합은 Resignation 불성립",
    37: "랙에 튜너 결합 불성립",
    38: "플루트 파도 결합은 Wave 추상 불성립",
    40: "색소폰 청원 결합은 Petition 기각 라인",
    41: "트럼펫 그래프 결합은 Graph 불명확",
    42: "클라리넷 케이스·사건 결합은 Case 다의어 불명확",
    43: "베이스 와트 결합은 Wattage 불성립",
    46: "라우터 활용률 결합 불성립 - Utilization",
    47: "비밀번호 혜택 결합은 Benefit 추상 불명확",
    49: "문의에 감가상각 결합 불성립",
    50: "이력서 사직 결합은 Resignation 불성립",
    51: "연사에 위험 결합 불성립",
    52: "배출가스에 보증인 결합 불성립",
    53: "셰프에 튜너 결합 불성립",
    54: "오르간 데크 결합은 Deck 불성립",
    55: "검인 역 결합은 Probate 추상 기각 라인",
    56: "하프 로비 결합은 Lobby 불성립",
    57: "오보에 패스 결합은 합격·통행 다의어 불명확",
    58: "비올라 가치 결합은 Value 속성어 불성립",
    59: "트롬본 라벨 결합은 Label 불성립",
    60: "타악 비교 결합은 비교 대상 불명확",
    62: "아코디언 시간 결합은 Time 속성어 불성립",
    65: "밸브 활용률 결합 불성립 - Utilization",
    66: "세차천 혜택 결합은 Benefit 추상 불명확",
    68: "사파리에 감가상각 결합 불성립",
    69: "하모니카 사직 결합은 Resignation 불성립",
    70: "용량에 위험 결합 불성립",
    71: "거래에 보증인 결합 불성립",
    72: "화물에 튜너 결합 불성립",
    77: "조율 부채 결합은 Debt 불성립",
    78: "이론 마커 결합은 Marker 불성립",
    79: "코드 개요 결합은 Outline 불성립",
    81: "레퍼토리 케이스 결합은 Case 다의어 불명확",
    83: "반주자 한도 결합은 Limit 속성어 불성립",
    84: "메트로놈 와트 결합은 Wattage 불성립",
    85: "증서 용량 결합은 Capacity 속성어 불성립",
    86: "곡집 주기 결합은 Cycle 기각 라인",
    89: "신탁 활용률 결합 불성립 - Utilization",
    90: "공제 혜택 결합은 Benefit 추상 불명확",
    92: "피트니스에 감가상각 결합 불성립",
    93: "캠프 사직 결합은 Resignation 불성립",
    94: "자세에 위험 결합 불성립",
    95: "자산에 보증인 결합 불성립",
    96: "유예(grace)에 튜너 결합 불성립",
    97: "합창 흐름 결합은 Flow 추상 불성립",
    98: "퇴직 데스크 결합은 Desk 추상 불성립",
    99: "오케스트라 금고 결합은 Vault 추상 불성립",
    100: "유산 비컨 결합은 Beacon 추상 불성립",
    101: "멜로디 브리지 결합은 Bridge 기각 라인",
    102: "리듬 루프 결합은 Loop 추상 불성립",
    103: "비트 포인트 결합은 Point 불명확",
    104: "피치 코어 결합은 Core 추상 불성립",
    106: "선박 혜택 결합은 Benefit 추상 불명확",
    108: "키웨이에 위험 결합 불성립",
    109: "용어집에 보증인 결합 불성립",
    110: "이사에 튜너 결합 불성립",
    111: "피아노 나침반 결합은 Compass 불명확 은유",
    112: "기타 파인더 결합은 검색 대상 불명확",
    114: "드럼 기한·회비 결합은 Due 다의어 불명확",
    115: "보컬 음량 결합은 Volume 다의어 불명확",
    116: "우쿨렐레 시계 결합은 Clock 불성립",
    117: "견종 활용률 결합 불성립 - Utilization",
    118: "치과 차트 혜택 결합은 Benefit 추상 불명확",
    119: "활력징후 사직 결합은 Resignation 불성립",
    120: "반복(recurring)에 위험 결합 불성립",
    121: "플루트 경로 결합은 Path 추상 불성립",
    122: "첼로 빈 결합은 Bin 기각 라인",
    124: "트럼펫 라벨 결합은 Label 불성립",
    126: "베이스 밝기 결합은 Brightness 속성어 불성립",
    129: "카풀 활용률 결합 불성립 - Utilization",
    130: "라우터 혜택 결합은 Benefit 추상 불명확",
    132: "클라우드에 감가상각 결합 불성립",
    133: "문의 사직 결합은 Resignation 불성립",
    134: "이력서에 위험 결합 불성립",
    135: "연사에 보증인 결합 불성립",
    136: "배출가스에 튜너 결합 불성립",
    138: "검인 터미널 결합은 Probate 추상 기각 라인",
    139: "하프 티커 결합은 Ticker 불성립",
    141: "비올라 지분 결합은 Stake 불성립",
    143: "타악 제안서 결합은 Proposal 불성립",
    145: "아코디언 속도 결합은 Speed 속성어 불성립",
    148: "지붕 활용률 결합 불성립 - Utilization",
    149: "밸브 혜택 결합은 Benefit 추상 불명확",
    150: "세차천에 요건 결합 불성립",
    151: "역류에 감가상각 결합 불성립",
    152: "사파리 사직 결합은 Resignation 불성립",
    153: "하모니카에 위험 결합 불성립",
    154: "용량에 보증인 결합 불성립",
    155: "거래에 튜너 결합 불성립",
    156: "레슨 실험실 결합은 Lab 불성립",
    158: "리사이탈 태그 결합은 Tag 불성립",
    159: "오디션 배지 결합은 배지 부여 대상 불성립",
    160: "조율 펀드 결합은 Fund 불성립",
    161: "이론 균형 결합은 Balance 불성립",
    162: "코드 렌더링 결합은 Rendering 불성립",
    163: "템포 등급 결합은 등급 부여 대상 불성립 - 도구 대상",
    164: "곡목에 매칭 결합 불성립 - Match는 강사·학생 매칭 라인",
    165: "합주 검증 결합은 Verification 불성립",
    166: "반주자 유형 결합은 Type 속성어 불성립",
    167: "메트로놈 밝기 결합은 Brightness 속성어 불성립",
    168: "증서 사용량 결합 불성립 - Usage 지표어",
    169: "곡집 고장·분석 결합은 Breakdown 불명확",
    172: "수분 활용률 결합 불성립 - Utilization",
    173: "신탁 혜택 결합은 Benefit 추상 불명확",
    175: "목공에 감가상각 결합 불성립",
    176: "피트니스 사직 결합은 Resignation 불성립",
    177: "캠프에 위험 결합 불성립",
    178: "자세에 보증인 결합 불성립",
    179: "자산에 튜너 결합 불성립",
    180: "합창 허브 결합은 Hub 추상 불성립",
    181: "퇴직 레이더 결합은 Radar 추상 불성립",
    182: "오케스트라 나침반 결합은 Compass 불명확 은유",
    183: "유산 대장간 결합은 Forge 불성립",
    184: "멜로디 신호 결합은 Signal 추상 불성립",
    185: "리듬 격자 결합은 Grid 추상 불성립",
    187: "음정에 장부 결합 불성립",
    191: "비행에 감가상각 결합 불성립",
    192: "키웨이에 보증인 결합 불성립",
    193: "용어집에 튜너 결합 불성립",
    194: "피아노 비컨 결합은 Beacon 추상 불성립",
    196: "바이올린 스텁 결합은 Stub 불성립",
    197: "드럼 보조금 결합은 Subsidy 불성립",
    199: "우쿨렐레 시간 결합은 Time 속성어 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 48, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 152, len(REJECT_REASON)
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
