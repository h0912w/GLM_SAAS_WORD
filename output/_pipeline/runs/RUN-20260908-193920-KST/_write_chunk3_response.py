import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk2_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk2_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "재산 자산 감가상각 관리로 명확 (Marina·Landlord 라인)"),
    3: (0.6, "임대 자산 위험(화재·파손) 요인 관리로 명확 - 물리 위험 실존"),
    9: (0.6, "잔류 염소 수질 평가로 명확 (Evaluation 라인)"),
    10: (0.6, "세차 고객 인테이크·만족 설문으로 명확"),
    13: (0.6, "피아노 설치·레슨 요건(방음·공간) 관리로 명확"),
    19: (0.6, "바이올린 수강권·공연 티켓 관리로 명확 (학원 운영)"),
    21: (0.6, "연속 연습 기록(스트릭) 관리로 명확 - 게이미피케이션 표준"),
    23: (0.6, "약제집 평가로 명확 - 병원 약제 심사 실무 (Evaluation 라인)"),
    25: (0.6, "HVAC 출동 접수 요건 관리로 명확"),
    30: (0.6, "첼로 강사·업체 디렉터리 관리로 명확"),
    33: (0.6, "클라리넷 과제·시험 준비 마감 관리로 명확"),
    35: (0.6, "러닝머신 상태·안전 평가로 명확 (Evaluation 라인)"),
    36: (0.6, "영유아 등록 인테이크 설문으로 명확"),
    39: (0.6, "멀칭 시공 요건 관리로 명확"),
    40: (0.6, "가구 자산 감가상각 관리로 명확 - 사무·가정 회계 실무"),
    47: (0.6, "하프 학원 운영 사무 관리로 명확"),
    52: (0.6, "만돌린 강사·학생 매칭 관리로 명확"),
    53: (0.6, "아코디언 악기 재고 관리로 명확"),
    55: (0.6, "퇴직연금 베스팅 현황 평가로 명확 (Evaluation 라인)"),
    56: (0.6, "배수로 점검 인테이크 설문으로 명확"),
    58: (0.6, "기고 투고 요건 관리로 명확"),
    66: (0.6, "오디션 접수 티켓 관리로 명확"),
    70: (0.6, "템포(BPM) 변환 도구로 명확 - 실재 음악 도구"),
    71: (0.6, "연주 곡 준비 마감 관리로 명확"),
    80: (0.6, "호흡 기능 평가로 명확 - 임상 실무 (Evaluation 라인)"),
    81: (0.6, "은퇴 준비 상태 설문으로 명확"),
    83: (0.6, "오케스트라 단원 오디션 요건 관리로 명확"),
    92: (0.6, "임대 규정 위반 평가로 명확 (Evaluation 라인)"),
    96: (0.6, "투숙·시설 요건 관리로 명확"),
    97: (0.6, "피아노 자산 감가상각 관리로 명확 - 고가 자산 회계 실무"),
    101: (0.6, "기타 연습 계획 관리로 명확"),
    102: (0.6, "바이올린 수리·레슨 견적 관리로 명확 (Quote 라인 준용)"),
    104: (0.6, "보컬 실력 등급 관리로 명확 (Score·Level 라인 준용)"),
    105: (0.6, "우쿨렐레 학원 뉴스레터 발송 관리로 명확"),
    106: (0.6, "예약 대기자 우선순위 평가로 명확 (Evaluation 라인)"),
    107: (0.6, "신규 약제 신청 설문으로 명확"),
    114: (0.6, "색소폰 레슨 바우처·교환권 관리로 명확"),
    118: (0.6, "치통 원인 평가로 명확 (Evaluation 라인)"),
    119: (0.6, "러닝머신 회원 인테이크 설문으로 명확"),
    122: (0.6, "방역 시공 요건 관리로 명확"),
    131: (0.6, "오보에 수강권·공연 티켓 관리로 명확"),
    138: (0.6, "보험 지급(settlement) 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    139: (0.6, "퇴직연금 가입 설문으로 명확"),
    147: (0.6, "연습 관리 매니저로 명확 (학원 운영)"),
    153: (0.6, "템포·리듬 패턴 생성 도구로 명확 (Percussion Generator 준용)"),
    155: (0.6, "합주 리허설 예약 관리로 명확 (Appointment 라인)"),
    162: (0.6, "합창 단원·합주 평가로 명확 (Evaluation 라인)"),
    163: (0.6, "호흡 상태 자가 인테이크 설문으로 명확"),
    171: (0.6, "선율 연습 진도 추적으로 명확 (Rhythm Tracker 준용)"),
    175: (0.6, "결혼 의식 진행 평가로 명확 (Evaluation 라인)"),
    179: (0.6, "수전 설치·규격 요건 관리로 명확"),
    180: (0.6, "호텔 자산 감가상각 관리로 명확 - 시설 자산 회계 실무"),
    184: (0.6, "레슨 일정 자동 스케줄링으로 명확 (학원 운영)"),
    188: (0.6, "우쿨렐레 악기 재고 관리로 명확"),
    189: (0.6, "예약 대기 등록 설문으로 명확"),
    191: (0.6, "전세 운항 계약 요건 관리로 명확"),
    196: (0.6, "연습 성취 배지 관리로 명확 - 게이미피케이션 표준"),
    200: (0.6, "애견 호텔(케넬) 시설·서비스 평가로 명확 (Evaluation 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "신고서 사직 결합은 Resignation 불성립",
    4: "멜로디에 보증인 결합 불성립",
    5: "수면에 튜너 결합 불성립",
    6: "리듬 허브 결합은 Hub 추상 불성립",
    7: "비트 금고 결합은 Vault 추상 불성립",
    8: "피치 연쇄 결합은 Cascade 추상 불성립",
    11: "수전 활용률 결합 불성립 - Utilization",
    12: "호텔 혜택 결합은 Benefit 추상 불명확",
    14: "송장 사직 결합은 Resignation 불성립",
    15: "사건서류에 위험 등록 불성립 - 문서 대상",
    16: "배송에 보증인 결합 불성립",
    17: "임차인에 튜너 결합 불성립",
    18: "기타 도우미 결합은 Assistant 은유 불명확 - Helper 라인 준용",
    20: "드럼 식별자 결합은 Identifier 불성립",
    22: "우쿨렐레 경비 결합은 대상 불충분으로 불명확",
    24: "전세 활용률 결합 불성립 - Utilization",
    26: "금고에 감가상각 결합 불성립",
    27: "배경망에 보증인 결합 불성립",
    28: "작가에 튜너 결합 불성립",
    29: "플루트 릴레이 결합은 Relay 불성립",
    31: "색소폰 패스 결합은 합격·통행 다의어 불명확",
    32: "트럼펫 자산 결합 불성립",
    34: "베이스 한도 결합은 Limit 속성어 불성립",
    37: "보행기 활용률 결합 불성립 - Utilization",
    38: "방역 혜택 결합은 Benefit 추상 불명확",
    41: "얼룩 사직 결합은 Resignation 불성립",
    42: "화장 대상에 위험 등록 불성립",
    43: "커트에 보증인 결합 불성립",
    44: "약사에 튜너 결합 불성립",
    45: "오르간 범위 결합은 Scope 불명확",
    46: "검인 파도 결합은 Wave 추상 불성립",
    48: "오보에 지수·색인 결합은 Index 불명확",
    49: "비올라 운임 결합은 Fare 교통 요금 어휘 불성립",
    50: "트롬본 부과금 결합은 Levy 불성립",
    51: "타악 견적기 결합은 Estimator 불성립",
    54: "하모니카 고장·분석 결합은 Breakdown 불명확",
    57: "논문 활용률 결합 불성립 - Utilization",
    59: "심각도에 감가상각 결합 불성립",
    60: "애프터파티에 위험 등록 불성립",
    61: "타이어에 보증인 결합 불성립",
    62: "Litter 다의어 도메인 기각 라인 + Tuner 불성립",
    63: "레슨 루프 결합은 Loop 추상 불성립",
    64: "연습 관리인 결합은 Keeper 불명확 은유",
    65: "리사이탈 로비 결합은 Lobby 불성립",
    67: "튜닝 회고 결합은 Recap 불성립",
    68: "이론 버전 결합은 Version 속성어 불성립",
    69: "코드 마크업 결합은 Markup 다의어 불명확",
    72: "앙상블 바코드 결합은 Barcode 불성립",
    73: "반주자에 환불 결합 불성립 - 인적 대상",
    74: "메트로놈 한도 결합은 Limit 속성어 불성립",
    75: "증서 속도 결합은 Speed 속성어 불성립",
    76: "곡집 압력 결합은 Pressure 불성립",
    77: "교법 용량 결합은 Capacity 불성립",
    78: "캠프 고장·분석 결합은 Breakdown 불명확",
    79: "합창 행렬 결합은 Matrix 추상 불성립",
    82: "우산보험 활용률 결합 불성립 - Utilization",
    84: "명상에 감가상각 결합 불성립",
    85: "재산 사직 결합은 Resignation 불성립",
    86: "신고서에 위험 결합 불성립",
    87: "보증인은 임차 측 실무 - 임대인에 결합 불성립",
    88: "멜로디에 튜너 결합 불성립",
    89: "리듬 데스크 결합은 Desk 추상 불성립",
    90: "비트 나침반 결합은 Compass 불명확 은유",
    91: "피치 브리지 결합은 Bridge 기각 라인",
    93: "잔류 염소에 설문 결합 불성립 - 응답 대상 불성립",
    94: "세차 활용률 결합 불성립 - Utilization",
    95: "수전 혜택 결합은 Benefit 추상 불명확",
    98: "송장에 위험 결합 불성립",
    99: "사건서류에 보증인 결합 불성립",
    100: "배송에 튜너 결합 불성립",
    103: "드럼 카테고리 결합은 Category 속성어 불성립",
    108: "전세 혜택 결합은 Benefit 추상 불명확",
    109: "출동에 감가상각 결합 불성립",
    110: "금고 사직 결합은 Resignation 불성립",
    111: "배경망에 튜너 결합 불성립",
    112: "플루트 금고 결합은 Vault 추상 불성립",
    113: "첼로 로케이터 결합은 검색 대상 불명확",
    115: "트럼펫 부과금 결합은 Levy 불성립",
    116: "클라리넷 기간 결합은 Duration 속성어 불성립",
    117: "베이스 유형 결합은 Type 속성어 불성립",
    120: "영유아 활용률 결합 불성립 - Utilization",
    121: "보행기 혜택 결합은 Benefit 추상 불명확",
    123: "멀칭에 감가상각 결합 불성립",
    124: "가구 사직 결합은 Resignation 불성립",
    125: "얼룩에 위험 결합 불성립",
    126: "화장에 보증인 결합 불성립",
    127: "커트에 튜너 결합 불성립",
    128: "오르간 루프 결합은 Loop 추상 불성립",
    129: "검인 경로 결합은 도구형 절차 안내로 Probate 기각 라인",
    130: "하프 카운터 결합은 Counter 불성립",
    132: "비올라 세금 결합은 Tax 불성립",
    133: "트롬본 기한·회비 결합은 Due 다의어 불명확",
    134: "타악 검사기 결합은 Checker 불명확",
    135: "만돌린 검증 결합은 Validation 불성립",
    136: "아코디언 클레임 결합은 Claim 불성립",
    137: "하모니카 센서 결합은 Sensor 불성립",
    140: "배수로 활용률 결합 불성립 - Utilization",
    141: "논문 혜택 결합은 Benefit 추상 불명확",
    142: "바이라인에 감가상각 결합 불성립",
    143: "심각도 사직 결합은 Resignation 불성립",
    144: "애프터파티에 보증인 결합 불성립",
    145: "타이어에 튜너 결합 불성립",
    146: "레슨 격자 결합은 Grid 추상 불성립",
    148: "리사이탈 티커 결합은 Ticker 불성립",
    149: "오디션에 견적 결합 불성립",
    150: "튜닝 항목·입장 결합은 Entry 다의어 불명확",
    151: "이론 링크 결합은 Link 추상 불성립",
    152: "코드 상환 결합은 Redemption 불성립",
    154: "레퍼토리 기간 결합은 Duration 속성어 불성립",
    156: "반주자에 경비 결합 불성립 - 인적 대상",
    157: "메트로놈 유형 결합은 Type 속성어 불성립",
    158: "증서 깊이 결합은 Depth 속성어 불성립",
    159: "곡집 하중 결합은 Load 속성어 불성립",
    160: "교법 사용량 결합 불성립 - Usage 지표어",
    161: "캠프 센서 결합은 Sensor 불성립",
    164: "퇴직 활용률 결합 불성립 - Utilization",
    165: "우산보험 혜택 결합은 Benefit 추상 불명확",
    166: "오케스트라에 감가상각 결합 불성립",
    167: "명상 사직 결합은 Resignation 불성립",
    168: "finance 재산 문맥에 hazard 물리 위험 어휘 결합 불성립 - 도메인 불일치",
    169: "신고서에 보증인 결합 불성립",
    170: "임대인에 튜너 결합 불성립",
    172: "리듬 레이더 결합은 Radar 추상 불성립",
    173: "비트 비컨 결합은 Beacon 추상 불성립",
    174: "피치 신호 결합은 Signal 추상 불성립",
    176: "위반에 설문 결합 불성립 - 응답 대상 불성립",
    177: "잔류 염소 활용률 결합 불성립 - Utilization",
    178: "세차 혜택 결합은 Benefit 추상 불명확",
    181: "피아노 사직 결합은 Resignation 불성립",
    182: "송장에 보증인 결합 불성립",
    183: "사건서류에 튜너 결합 불성립",
    185: "바이올린 주문·순서 결합은 Order 다의어 불명확",
    186: "드럼 속성 결합은 Attribute 속성어 불성립",
    187: "보컬 추세 결합은 Trend 불성립",
    190: "약제집 활용률 결합 불성립 - Utilization",
    192: "출동 사직 결합은 Resignation 불성립",
    193: "금고에 위험 등록 불성립 - 안전 설비 자체",
    194: "플루트 나침반 결합은 Compass 불명확 은유",
    195: "첼로 파인더 결합은 검색 대상 불명확",
    197: "트럼펫 기한·회비 결합은 Due 다의어 불명확",
    198: "클라리넷 음량·권 결합은 Volume 다의어 불명확",
    199: "베이스 시계 결합은 Clock 불성립",
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
