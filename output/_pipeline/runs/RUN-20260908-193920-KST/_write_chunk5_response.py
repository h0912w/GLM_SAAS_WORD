import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk4_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk4_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "BPM 측정 확인 도구로 명확 - 실재 도구 (Tempo 계열 준용)"),
    2: (0.6, "연주 곡 숙달 진도 관리로 명확"),
    3: (0.6, "합주단 등록·계약 갱신 관리로 명확 (Renewal 라인)"),
    9: (0.6, "캠프 등록 승인 관리로 명확 (Approval 라인)"),
    10: (0.6, "자산(wealth) 평가로 명확 - 금융 실무 (Evaluation 라인)"),
    19: (0.6, "재산 자산 현황 추적으로 명확 (Tracker 라인)"),
    24: (0.6, "번역 용어집 품질 평가로 명확 - 통번역 실무 (Evaluation 라인)"),
    25: (0.6, "이사 인테이크 설문으로 명확"),
    28: (0.6, "임대 규정 위반 처리 요건 관리로 명확"),
    33: (0.6, "피아노 조율 관리로 명확 - 실재 서비스(조율사)"),
    34: (0.6, "기타 학생·악기 등록부 관리로 명확 (Registry 라인 준용)"),
    38: (0.6, "우쿨렐레 수강 출결 체크인 관리로 명확"),
    40: (0.6, "예약 대기 자격 요건 관리로 명확"),
    44: (0.6, "첼로 연습 부스 예약 관리로 명확 (Harp Booth 준용)"),
    45: (0.6, "레슨 메모 관리로 명확 (Diary 라인 준용)"),
    47: (0.6, "클라리넷 예약 승인 관리로 명확 (Approval 라인 준용)"),
    49: (0.6, "연사·발표자 평가로 명확 - 행사 실무 (Evaluation 라인)"),
    50: (0.6, "배출가스 검사 인테이크 설문으로 명확"),
    62: (0.6, "오보에 레슨비 영수증 관리로 명확 (Receipt 라인)"),
    66: (0.6, "만돌린 강사 가용 시간 관리로 명확 (Availability 라인)"),
    69: (0.6, "약물 용량(dosage) 평가로 명확 - 임상 실무 (Evaluation 라인)"),
    70: (0.6, "투자 성향 인테이크 설문으로 명확"),
    73: (0.6, "보험 합의 처리 요건 관리로 명확"),
    78: (0.6, "레슨 커리큘럼 진행 지도로 명확 (Map 라인)"),
    79: (0.6, "연습 일정 스케줄러로 명확 (Scheduler 라인)"),
    80: (0.6, "연주회 운영 보고 관리로 명확 (Summary 라인 준용)"),
    82: (0.6, "조율 계획 관리로 명확 (Plan 라인)"),
    85: (0.6, "오디오 BPM 자동 감지 도구로 명확 - 실재 도구 (Tempo 계열 준용)"),
    86: (0.6, "연주 곡목 선정 승인 관리로 명확 (Approval 라인 준용)"),
    87: (0.6, "합주 공연 견적 관리로 명확 (Quote 라인)"),
    88: (0.6, "신규 반주자 온보딩 관리로 명확 (Onboarding 라인)"),
    94: (0.6, "자세(posture) 평가로 명확 - 임상 실무 (Evaluation 라인)"),
    95: (0.6, "자산 상태 인테이크 설문으로 명확"),
    98: (0.6, "합창단 단원 모집 요건 관리로 명확"),
    108: (0.6, "열쇠 키웨이(keyway) 사양 평가로 명확 - 자물쇠 실무 (Evaluation 라인)"),
    109: (0.6, "고객 용어 선호 확인 설문으로 명확"),
    112: (0.6, "결혼식 의식 진행 요건 관리로 명확"),
    118: (0.6, "피아노 연습 진도 추적으로 명확 (Tracker 라인)"),
    120: (0.6, "바이올린 곡목·자료 리스트 관리로 명확 (List 라인)"),
    122: (0.6, "보컬 연습 기록 관리로 명확 (Record 라인)"),
    134: (0.6, "이력서(resume) 평가로 명확 - 채용 실무 (Evaluation 라인)"),
    135: (0.6, "연사 인테이크 설문으로 명확"),
    138: (0.6, "애견 호텔 이용·접종 요건 관리로 명확 - 실무 요건"),
    144: (0.6, "오르간 레슨 진행 지도로 명확 (Map 라인)"),
    151: (0.6, "만돌린 수강 자격 관리로 명확 (Eligibility 라인)"),
    153: (0.6, "하모니카 연주·제품 평가로 명확 (Evaluation 라인)"),
    154: (0.6, "복약 문진 설문으로 명확"),
    157: (0.6, "계약 부속 조항 요건 관리로 명확"),
    163: (0.6, "연습 진도 모니터링으로 명확 (Monitor 라인)"),
    164: (0.6, "연주회 운영 기록 관리로 명확 (Journal 라인 준용)"),
    165: (0.6, "오디션 지원자 리스트 관리로 명확 (List 라인)"),
    168: (0.6, "코드 참조 매뉴얼 관리로 명확 (Playbook·Reference 라인 준용)"),
    169: (0.6, "템포·연습 시간 측정 타이머로 명확 - 실재 도구 (Timer 라인)"),
    172: (0.6, "반주자 스케줄 체크인 관리로 명확"),
    177: (0.6, "캠프 만족·안전 평가로 명확 (Evaluation 라인)"),
    178: (0.6, "자세 상태 자가 설문으로 명확"),
    181: (0.6, "옥상 시설 점검 요건 관리로 명확"),
    186: (0.6, "오케스트라 리허설·단원 현황 추적으로 명확 (Tracker 라인)"),
    192: (0.6, "열쇠 사양 확인 설문으로 명확"),
    195: (0.6, "촬영 조건 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    4: "반주자에 클레임 결합 불성립",
    5: "메트로놈 속도 결합은 Speed 속성어 불성립",
    6: "증서 온도 결합은 Temperature 속성어 불성립",
    7: "곡집 밝기 결합은 Brightness 속성어 불성립",
    8: "교법 에피소드 결합은 Episode 불명확",
    11: "유예(grace) 설문 결합은 Grace 다의어 불명확",
    12: "옥상 활용률 결합 불성립 - Utilization",
    13: "합창 혜택 결합은 Benefit 추상 불명확",
    14: "호흡에 요건 결합 불성립 - 대상 불명확",
    15: "퇴직에 감가상각 결합 불성립",
    16: "우산보험 사직 결합은 Resignation 불성립",
    17: "오케스트라에 보증인 결합 불성립",
    18: "명상에 튜너 결합 불성립",
    20: "멜로디 데스크 결합은 Desk 추상 불성립",
    21: "리듬 나침반 결합은 Compass 불명확 은유",
    22: "비트 브리지 결합은 Bridge 기각 라인",
    23: "피치 루프 결합은 Loop 추상 불성립",
    26: "촬영 활용률 결합 불성립 - Utilization",
    27: "의식 혜택 결합은 Benefit 추상 불명확",
    29: "잔류 염소에 감가상각 결합 불성립",
    30: "세차 사직 결합은 Resignation 불성립",
    31: "수전에 위험 결합 불성립",
    32: "호텔에 보증인 결합 불성립",
    35: "바이올린 코드 부호 결합은 Code 다의어 불명확 - chord 오독 위험",
    36: "드럼 일련번호 결합은 Serial 불성립",
    37: "보컬 보증 결합은 Guarantee 불성립",
    39: "랙 활용률 결합 불성립 - Utilization",
    41: "약제집에 감가상각 결합 불성립",
    42: "출동에 튜너 결합 불성립",
    43: "플루트 연쇄 결합은 Cascade 추상 불성립",
    46: "트럼펫 체납 결합은 Arrears 기각 라인",
    48: "베이스 깊이 결합은 Depth 속성어 불성립",
    51: "셰프 활용률 결합 불성립 - Utilization",
    52: "애견 호텔 혜택 결합은 Benefit 추상 불명확",
    53: "치통에 요건 결합 불성립",
    54: "러닝머신에 감가상각 결합 불성립",
    55: "영유아 사직 결합은 Resignation 불성립",
    56: "보행기에 위험 등록 불성립",
    57: "방역에 보증인 결합 불성립",
    58: "멀칭에 튜너 결합 불성립",
    59: "오르간 포인트 결합은 Point 불명확",
    60: "검인 베이스 결합은 Probate 추상 기각 라인",
    61: "하프 게시물·우편 결합은 Post 다의어 불명확",
    63: "비올라 펀드 결합은 Fund 불성립",
    64: "트롬본 선급 결합은 Advance 기각 라인",
    65: "타악 수호자 결합은 Guardian 불명확 은유",
    67: "아코디언 길이 결합은 Length 속성어 불성립",
    68: "하모니카 행렬 결합은 Matrix 추상 불성립",
    71: "화물 활용률 결합 불성립 - Utilization",
    72: "부속 조항 혜택 결합은 Benefit 추상 불명확",
    74: "베스팅에 감가상각 결합 불성립",
    75: "배수로 사직 결합은 Resignation 불성립",
    76: "논문에 위험 결합 불성립",
    77: "바이라인에 튜너 결합 불성립",
    81: "오디션 코드 부호 결합은 Code 다의어 불명확",
    83: "이론 카테고리 결합은 Category 속성어 불성립",
    84: "코드 라벨 결합은 Label 불성립",
    89: "메트로놈 깊이 결합은 Depth 속성어 불성립",
    90: "증서 압력 결합은 Pressure 속성어 불성립",
    91: "곡집 빈도 결합은 Frequency 속성어 불성립",
    92: "교법 주기 결합은 Cycle 기각 라인",
    93: "캠프 행렬 결합은 Matrix 추상 불성립",
    96: "유예(grace) 활용률 결합 불성립 - Utilization + 다의어",
    97: "옥상 혜택 결합은 Benefit 추상 불명확",
    99: "호흡에 감가상각 결합 불성립",
    100: "퇴직 사직 결합은 Resignation 불성립",
    101: "우산보험에 위험 결합 불성립",
    102: "오케스트라에 튜너 결합 불성립",
    103: "유산 흐름 결합은 Flow 추상 불성립",
    104: "멜로디 레이더 결합은 Radar 추상 불성립",
    105: "리듬 비컨 결합은 Beacon 추상 불성립",
    106: "비트 신호 결합은 Signal 추상 불성립",
    107: "피치 격자 결합은 Grid 추상 불성립",
    110: "이사 활용률 결합 불성립 - Utilization",
    111: "촬영 혜택 결합은 Benefit 추상 불명확",
    113: "위반에 감가상각 결합 불성립",
    114: "잔류 염소 사직 결합은 Resignation 불성립",
    115: "세차에 위험 결합 불성립",
    116: "수전에 보증인 결합 불성립",
    117: "호텔에 튜너 결합 불성립",
    119: "기타 운영 옵스 결합은 Ops 불성립",
    121: "드럼 토큰 결합은 Token 기각 라인",
    123: "우쿨렐레 크기 결합은 Size 속성어 불성립",
    124: "반복(recurring) 평가 결합은 Recurring 속성어 불명확",
    125: "랙 혜택 결합은 Benefit 추상 불명확",
    126: "대기자에 감가상각 결합 불성립",
    127: "약제집 사직 결합은 Resignation 불성립",
    128: "플루트 브리지 결합은 Bridge 기각 라인",
    129: "첼로 키오스크 결합은 Kiosk 불성립",
    130: "색소폰 할당량 결합은 Quota 불성립",
    131: "트럼펫 선급 결합은 Advance 기각 라인",
    132: "클라리넷 템플릿 결합은 Template 불성립",
    133: "베이스 높이 결합은 Height 속성어 불성립",
    136: "배출가스 활용률 결합 불성립 - Utilization",
    137: "셰프 혜택 결합은 Benefit 추상 불명확",
    139: "치통에 감가상각 결합 불성립",
    140: "러닝머신 사직 결합은 Resignation 불성립",
    141: "영유아에 위험 결합 불성립",
    142: "보행기에 보증인 결합 불성립",
    143: "방역에 튜너 결합 불성립",
    145: "검인 코어 결합은 Probate 추상 기각 라인",
    146: "하프 항구 결합은 Harbor 불명확 은유",
    147: "오보에 코드 부호 결합은 Code 다의어 불명확",
    148: "비올라 현금 결합은 Cash 불성립",
    149: "트롬본 벌금 결합은 Penalty 기각 라인",
    150: "타악 도우미 결합은 Helper 불명확 은유",
    152: "아코디언 무게 결합은 Weight 속성어 불성립",
    155: "거래 활용률 결합 불성립 - Utilization",
    156: "화물 혜택 결합은 Benefit 추상 불명확",
    158: "보험 합의에 감가상각 결합 불성립",
    159: "베스팅 사직 결합은 Resignation 불성립",
    160: "배수로에 위험 결합 불성립",
    161: "논문에 보증인 결합 불성립",
    162: "레슨 틀 결합은 Frame 불성립",
    166: "조율 비용 결합은 Cost 속성어 불성립",
    167: "이론 속성 결합은 Attribute 속성어 불성립",
    170: "레퍼토리 템플릿 결합은 Template 불성립",
    171: "합주단 보증 결합은 Warranty 불성립",
    173: "메트로놈 높이 결합은 Height 속성어 불성립",
    174: "증서 하중 결합은 Load 속성어 불성립",
    175: "곡집 호환성 결합은 Compatibility 불성립",
    176: "교법 고장·분석 결합은 Breakdown 불명확",
    179: "자산 활용률 결합 불성립 - Utilization",
    180: "유예 혜택 결합은 Benefit 추상 불명확 + Grace 다의어",
    182: "합창에 감가상각 결합 불성립",
    183: "호흡 사직 결합은 Resignation 불성립",
    184: "퇴직에 위험 결합 불성립",
    185: "우산보험에 보증인 결합 불성립",
    187: "유산 허브 결합은 Hub 추상 불성립",
    188: "멜로디 릴레이 결합은 Relay 불성립",
    189: "리듬 대장간 결합은 Forge 불성립",
    190: "비트 감시 결합은 Watch 도구형 기각 라인",
    191: "피치 파도 결합은 Wave 추상 불성립",
    193: "용어집 활용률 결합 불성립 - Utilization",
    194: "이사 혜택 결합은 Benefit 추상 불명확",
    196: "의식에 감가상각 결합 불성립",
    197: "위반 사직 결합은 Resignation 불성립",
    198: "잔류 염소에 위험 결합 불성립",
    199: "세차에 보증인 결합 불성립",
    200: "수전에 튜너 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 60, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 140, len(REJECT_REASON)
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
