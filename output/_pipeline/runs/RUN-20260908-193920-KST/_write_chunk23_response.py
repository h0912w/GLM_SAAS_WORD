import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk22_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk22_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "리듬 연습 모니터링 관리로 명확 (Monitor 라인)"),
    2: (0.6, "비트 연습 플레이북 관리로 명확 (Playbook 라인)"),
    3: (0.6, "피치 기록 디렉터리 관리로 명확 (Directory 라인)"),
    9: (0.6, "드럼 워크숍 관리로 명확 (Workshop 라인)"),
    11: (0.6, "마스터키 시공 평가로 명확 - 자물쇠 실무 (Evaluation 라인)"),
    12: (0.6, "용어 확인 설문으로 명확"),
    14: (0.6, "꽃집 요건 관리로 명확 (Requirement 라인)"),
    19: (0.6, "우쿨렐레 연습 추적 관리로 명확 (Tracker 라인)"),
    21: (0.6, "첼로 출연 목록 관리로 명확 (List 라인)"),
    23: (0.6, "트럼펫 연습 기록 관리로 명확 (Record 라인)"),
    26: (0.6, "추모식 요건 관리로 명확 (Requirement 라인)"),
    27: (0.6, "항구 하역 작업 위험 관리로 명확 - 낙하·익수 위험 실존 (Hazard 물리위험 라인)"),
    35: (0.6, "비올라 운주법 도식 관리로 명확 (Schematic 라인)"),
    37: (0.6, "타액 자격 인증 관리로 명확 (Certification 라인)"),
    39: (0.6, "흡입기 사용 평가로 명확 - 약사 실무 (Evaluation 라인)"),
    40: (0.6, "제습기 확인 설문으로 명확"),
    49: (0.6, "레슨 부스 예약 관리로 명확 (Booth 라인)"),
    55: (0.6, "연주 코드 진단 도구로 실재 (Diagnostic 라인)"),
    61: (0.6, "유모차 요건 관리로 명확 (Requirement 라인)"),
    77: (0.6, "비트 연습 일지 관리로 명확 (Journal 라인)"),
    79: (0.6, "화물 요건 관리로 명확 (Requirement 라인)"),
    82: (0.6, "기타 연습 요약 관리로 명확 (Summary 라인)"),
    86: (0.6, "여과 시스템 성능 평가로 명확 - HVAC 실무 (Evaluation 라인)"),
    87: (0.6, "마스터키 시공 확인 설문으로 명확"),
    89: (0.6, "갤러리 요건 관리로 명확 (Requirement 라인)"),
    95: (0.6, "플루트 연습 플레이북 관리로 명확 (Playbook 라인)"),
    100: (0.6, "수선 요건 관리로 명확 (Requirement 라인)"),
    105: (0.6, "오르간 레슨 부스 예약 관리로 명확 (Booth 라인)"),
    111: (0.6, "타액 파트 지명 관리로 명확 (Nomination 라인)"),
    113: (0.6, "블로우아웃 시술 결과 평가로 명확 - 미용 실무 (Evaluation 라인)"),
    114: (0.6, "흡입기 확인 설문으로 명확"),
    117: (0.6, "구문 요건 관리로 명확 (Requirement 라인)"),
    124: (0.6, "연습 소식·갱신 관리로 명확 (Update 라인)"),
    128: (0.6, "음악이론 정답 검사기로 실재 도구 (Checker 라인)"),
    133: (0.6, "채용 적성 평가로 명확 - 채용 실무 (Evaluation 라인)"),
    135: (0.6, "교정 요건 관리로 명확 (Requirement 라인)"),
    140: (0.6, "반주자 일정 추적 관리로 명확 (Tracker 라인)"),
    150: (0.6, "멜로디 작업 플래너로 명확 (Planner 라인)"),
    151: (0.6, "리듬 연습 대장 관리로 명확 (Register 라인)"),
    152: (0.6, "비트 기록 등록부 관리로 명확 (Registry 라인)"),
    157: (0.6, "기타 학습 타임라인 관리로 명확 (Timeline 라인)"),
    160: (0.6, "보컬 레슨 영상 관리로 명확 (Video 라인)"),
    161: (0.6, "여과 확인 설문으로 명확"),
    169: (0.6, "플루트 연습 일지 관리로 명확 (Journal 라인)"),
    174: (0.6, "아동 발달 이정표 평가로 명확 - 육아 실무 (Evaluation 라인)"),
    183: (0.6, "비올라 포지션 스케치 관리로 명확 (Sketch 라인)"),
    184: (0.6, "트롬본 레퍼런스 관리로 명확 (Reference 라인)"),
    185: (0.6, "타액 연주 교정 서비스로 실재 (Correction 라인, Vocal Correction 선례 준용)"),
    187: (0.6, "식기세척기 상태 평가로 명확 - 세탁·청소 설비 실무 (Evaluation 라인)"),
    188: (0.6, "블로우아웃 확인 설문으로 명확"),
    191: (0.6, "자물쇠 홈 가공 요건 관리로 명확 (Requirement 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    4: "화물 혜택 결합은 Benefit 추상 불명확",
    5: "정책 감가상각 결합 불성립",
    6: "피아노 연결점 결합은 Nexus 추상 불성립",
    7: "기타 초안 결합은 Draft 다의어 불명확",
    8: "바이올린 번호 결합은 Number 속성어 불성립",
    10: "보컬 리뷰 결합은 후기/검토 다의어 불명확",
    13: "갤러리 혜택 결합은 Benefit 추상 불명확",
    15: "라이너 사직 결합은 Resignation 불성립",
    16: "코팅에 위험 결합은 서비스 대상 불성립",
    17: "변기에 보증인 결합 불성립",
    18: "휴가에 튜너 결합 불성립",
    20: "플루트 운영 결합은 Ops 불명확",
    22: "색소폰 토큰 결합은 Token 불성립",
    24: "클라리넷 크기 결합은 Size 속성어 불성립",
    25: "수선 혜택 결합은 Benefit 추상 불명확",
    28: "운행 기록부에 보증인 결합 불성립",
    29: "광미에 튜너 결합 불성립",
    30: "베이스 브리지 결합은 악기 브리지로 오독, 서비스 불성립",
    31: "오르간 카운터 결합은 Counter 다의어 불명확",
    32: "검인 구역 결합은 Probate 도구형·Bay 불성립",
    33: "하프 샘플 결합은 Sample 다의어 불명확",
    34: "오보에 벌금·미세 결합은 Fine 다의어 불명확",
    36: "트롬본 사본 결합은 Copy 다의어 불명확",
    38: "만돌린 온도 결합은 Temperature 속성어 불성립",
    41: "자물쇠 홈 활용률 결합 불성립 - Utilization",
    42: "구문 혜택 결합은 Benefit 추상 불명확",
    43: "케이크 사직 결합은 Resignation 불성립",
    44: "제설에 위험 결합은 서비스 대상 불성립",
    45: "마감에 보증인 결합 불성립",
    46: "스펀지에 튜너 결합 불성립",
    47: "아코디언 허브 결합은 Hub 추상 불성립",
    48: "하모니카 포털 결합은 Portal 불성립",
    50: "연습 요율 결합은 Rate 속성어 불성립",
    51: "리사이탈 회람 결합은 Circular 불명확",
    52: "오디션 번호 결합은 Number 속성어 불성립",
    53: "조율 캐시백 결합은 Redemption 기각 라인",
    54: "이론 추정기 결합은 불성립",
    56: "템포에 견적 결합 불성립",
    57: "레퍼토리 크기 결합은 Size 속성어 불성립",
    58: "합주 용량 결합은 Capacity 속성어 불성립",
    59: "식이 활용률 결합 불성립 - Utilization",
    60: "교정 혜택 결합은 Benefit 추상 불명확",
    62: "스파 감가상각 결합 불성립",
    63: "연석에 위험 결합 불성립",
    64: "포도원에 보증인 결합 불성립",
    65: "반주자에 튜너 결합 불성립",
    66: "메트로놈 브리지 결합은 Bridge 추상 불성립",
    67: "증서 순환 결합은 Loop 불성립",
    68: "곡집에 지도 결합은 불성립 (Method Map 기각 선례 준용)",
    69: "교법에 스튜디오 결합은 불명확",
    70: "캠프 포털 결합은 Portal 불성립",
    71: "합창 궤도 결합은 Rail 불성립",
    72: "퇴직 체인 결합은 Chain 추상 불성립",
    73: "오케스트라 연결점 결합은 Nexus 추상 불성립",
    74: "유산 관리자 결합은 Keeper 불명확 기각 라인",
    75: "멜로디 조수 결합은 Assistant 불명확 기각 라인",
    76: "리듬 동반자 결합은 Companion 불명확 기각 라인",
    78: "피치 검색기 결합은 Locator/Finder 불성립",
    80: "정책 사직 결합은 Resignation 불성립",
    81: "피아노 대성지도 결합은 Atlas 추상 불성립",
    83: "바이올린 버전 결합은 Version 속성어 불성립",
    84: "드럼 수호자 결합은 Guardian 추상 불성립",
    85: "보컬 조리법 결합은 Recipe 불성립",
    88: "용어 활용률 결합 불성립 - Utilization",
    90: "꽃집 감가상각 결합 불성립",
    91: "라이너에 위험 결합 불성립",
    92: "코팅에 보증인 결합 불성립",
    93: "변기에 튜너 결합 불성립",
    94: "우쿨렐레 흐름 결합은 Flow 불성립",
    96: "첼로 표 결합은 Table 다의어 불명확",
    97: "색소폰 서명 결합은 Signature 불명확",
    98: "트럼펫 사본 결합은 Copy 다의어 불명확",
    99: "클라리넷 길이 결합은 Length 속성어 불성립",
    101: "추모식 감가상각 결합 불성립",
    102: "항구에 보증인 결합 불성립",
    103: "운행 기록부에 튜너 결합 불성립",
    104: "베이스 신호 결합은 Signal 추상 불성립",
    106: "검인 게시물 결합은 Post 다의어 불명확",
    107: "하프 슬롯 결합은 Slot 불성립",
    108: "오보에 번호 결합은 Number 속성어 불성립",
    109: "비올라 배치도 결합은 Layout 불성립",
    110: "트롬본 읽기 결합은 악보 읽기로 오독, 불명확",
    112: "만돌린 압력 결합은 Pressure 속성어 불성립",
    115: "제습기 활용률 결합 불성립 - Utilization",
    116: "자물쇠 홈 혜택 결합은 Benefit 추상 불명확",
    118: "케이크에 위험 결합은 서비스 대상 불성립",
    119: "제설에 보증인 결합 불성립",
    120: "마감에 튜너 결합 불성립",
    121: "아코디언 책상 결합은 Desk 불성립",
    122: "하모니카 콘솔 결합은 Console 불성립",
    123: "레슨 키오스크 결합은 Kiosk 불성립",
    125: "리사이탈 자문 결합은 Advisory 불명확",
    126: "오디션 버전 결합은 Version 속성어 불성립",
    127: "조율 연장 결합은 Extension 기각 라인",
    129: "코드 진행(chord progression)으로 오독하는 결합은 불명확",
    130: "템포 보증 결합은 Warranty 불성립",
    131: "레퍼토리 길이 결합은 Length 속성어 불성립",
    132: "합주 사용량 결합은 Usage 속성어 불성립",
    134: "식이 혜택 결합은 Benefit 추상 불명확",
    136: "유모차 감가상각 결합 불성립",
    137: "스파 사직 결합은 Resignation 불성립",
    138: "연석에 보증인 결합 불성립",
    139: "포도원에 튜너 결합 불성립",
    141: "메트로놈 신호 결합은 Signal 추상 불성립",
    142: "증서 격자 결합은 Grid 불성립",
    143: "곡집 틀 결합은 Frame 불성립",
    144: "교법 실험실 결합은 Lab 불성립",
    145: "캠프 콘솔 결합은 Console 불성립",
    146: "합창 흔적 결합은 Trail 불성립",
    147: "퇴직 링 결합은 Ring 불성립",
    148: "오케스트라 대성지도 결합은 Atlas 추상 불성립",
    149: "유산 관리자 결합은 Manager 불성립",
    153: "피치 검색기 결합은 Finder 불성립",
    154: "화물 감가상각 결합 불성립",
    155: "정책 위험 결합은 보험 약관 자체와 위험 결합이 서비스로 불성립",
    156: "피아노 관리자 결합은 Keeper 불명확 기각 라인",
    158: "바이올린 링크 결합은 Link 불성립",
    159: "드럼 조수 결합은 Helper 불명확 기각 라인",
    162: "마스터키 활용률 결합 불성립 - Utilization",
    163: "용어 혜택 결합은 Benefit 추상 불명확",
    164: "갤러리 감가상각 결합 불성립",
    165: "꽃집 사직 결합은 Resignation 불성립",
    166: "라이너에 보증인 결합 불성립",
    167: "코팅에 튜너 결합 불성립",
    168: "우쿨렐레 허브 결합은 Hub 추상 불성립",
    170: "첼로 전표 결합은 Slip 불명확",
    171: "색소폰 마커 결합은 Marker 불성립",
    172: "트럼펫 읽기 결합은 악보 읽기로 오독, 불명확",
    173: "클라리넷 무게 결합은 Weight 속성어 불성립",
    175: "수선 감가상각 결합 불성립",
    176: "추모식 사직 결합은 Resignation 불성립",
    177: "항구에 튜너 결합 불성립",
    178: "베이스 시계로 오독하는 Watch 결합은 불성립",
    179: "오르간 키오스크 결합은 Kiosk 불성립",
    180: "검인 항구 결합은 Probate 도구형·Harbor 불성립",
    181: "하프 통과 결합은 Pass 기각 라인",
    182: "오보에 버전 결합은 Version 속성어 불성립",
    186: "만돌린 하중 결합은 Load 속성어 불성립",
    189: "흡입기 활용률 결합 불성립 - Utilization",
    190: "제습기 혜택 결합은 Benefit 추상 불명확",
    192: "구문 감가상각 결합 불성립",
    193: "케이크에 보증인 결합 불성립",
    194: "제설에 튜너 결합 불성립",
    195: "아코디언 레이더 결합은 Radar 추상 불성립",
    196: "하모니카 패널 결합은 Panel 불성립",
    197: "레슨 구역 결합은 Bay 불성립",
    198: "연습 피드 결합은 Feed 불성립",
    199: "리사이탈 청원 결합은 Petition 불성립",
    200: "오디션 링크 결합은 Link 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 51, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 149, len(REJECT_REASON)
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
