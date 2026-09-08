import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk17_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk17_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "하프 연습 요약 관리로 명확 (Summary 라인)"),
    4: (0.6, "트롬본 연습 타이머로 실재 도구 (Timer 라인)"),
    8: (0.6, "송금 확인 설문으로 명확"),
    11: (0.6, "보험 잔존물 처리 요건 관리로 명확 (Requirement 라인)"),
    17: (0.6, "하모니카 학습 진도 지도로 명확 (Map 라인)"),
    18: (0.6, "레슨 진행 모니터링으로 명확 (Monitor 라인)"),
    24: (0.6, "코드 숙련 등급 관리로 명확 (Rank 라인)"),
    29: (0.6, "부동산 동네 입지 평가로 명확 - 부동산 실무 (Evaluation 라인)"),
    30: (0.6, "소송 확인 설문으로 명확"),
    40: (0.6, "캠프 배치 지도 관리로 명확 (Map 라인)"),
    49: (0.6, "농작물 수확 평가로 명확 - 농업 실무 (Evaluation 라인)"),
    50: (0.6, "계량기 확인 설문으로 명확"),
    58: (0.6, "보컬 레슨 견적 관리로 명확 (Quote 라인)"),
    59: (0.6, "우쿨렐레 레슨 신청 승인 관리로 명확 (Approval 라인)"),
    60: (0.6, "계정 대사(조정) 평가로 명확 - 회계 실무 (Evaluation 라인)"),
    61: (0.6, "법률 사건 확인 설문으로 명확"),
    62: (0.6, "자부담 기준 요건 관리로 명확 (Requirement 라인)"),
    70: (0.6, "트럼펫 연습 타이머로 실재 도구 (Timer 라인)"),
    72: (0.6, "이중언어 능력 평가로 명확 - 통번역 실무 (Evaluation 라인)"),
    82: (0.6, "하프 연습 타임라인 관리로 명확 (Timeline 라인)"),
    85: (0.6, "트롬본 워크숍 관리로 명확 (Workshop 라인)"),
    88: (0.6, "아코디언 실력 평가로 명확 - 레슨 실무 (Evaluation 라인)"),
    91: (0.6, "계약 변경 요건 관리로 명확 (Requirement 라인)"),
    94: (0.6, "외장재 시공 작업 안전 위험 관리로 명확 - 추락 위험 실존"),
    103: (0.6, "이론 학습 알림 관리로 명확 (Notification 라인)"),
    108: (0.6, "반주 진행 후속 관리로 명확 (Followup 라인)"),
    109: (0.6, "평상형 트럭(flatbed) 운송 평가로 명확 - 물류 실무 (Evaluation 라인)"),
    110: (0.6, "동네 확인 설문으로 명확"),
    113: (0.6, "목공 시공 요건 관리로 명확 (Requirement 라인)"),
    129: (0.6, "제조 생산 평가로 명확 - 제조 실무 (Evaluation 라인)"),
    130: (0.6, "수확 확인 설문으로 명확"),
    140: (0.6, "계정 조정 확인 설문으로 명확"),
    147: (0.6, "첼로 편곡·연주 초안 관리로 명확 (Draft 라인)"),
    149: (0.6, "트럼펫 워크숍 관리로 명확 (Workshop 라인)"),
    151: (0.6, "전자 잠금 키패드 평가로 명확 - 보안 실무 (Evaluation 라인)"),
    152: (0.6, "이중언어 확인 설문으로 명확"),
    154: (0.6, "축사 준비 요건 관리로 명확 (Requirement 라인)"),
    161: (0.6, "검인 절차 안내 플레이북 관리로 명확 (Playbook·Manual 라인)"),
    162: (0.6, "하프 연습 리마인더 관리로 명확 (Reminder 라인)"),
    166: (0.6, "타액 연습실 가용 확인 관리로 명확 (Availability 라인)"),
    168: (0.6, "로드트립 계획 평가로 명확 - 여행 실무 (Evaluation 라인)"),
    169: (0.6, "아코디언 확인 설문으로 명확"),
    171: (0.6, "섀시 점검 요건 관리로 명확 (Requirement 라인)"),
    178: (0.6, "레슨 출석 대장 관리로 명확 (Register 라인)"),
    188: (0.6, "반주자 배정 승인 관리로 명확 (Approval 라인)"),
    189: (0.6, "채무자 신용 평가로 명확 - 금융 실무 (Evaluation 라인)"),
    190: (0.6, "평상형 트럭 확인 설문으로 명확"),
    193: (0.6, "피부양자 자격 요건 관리로 명확 (Requirement 라인)"),
}

TRADEMARK_REJECT = {
    159: "Bass Tracker는 TRACKER Boats의 유명 낚시보트 브랜드 - 상표 유사",
}

DUP_REJECT = {}

REJECT_REASON = {
    2: "오보에 대출 결합은 Loan 기각 라인",
    3: "비올라 할인 결합은 Discount 기각 라인",
    5: "타액 핑 결합은 Ping 불성립",
    6: "만돌린 크기 결합은 Size 속성어 불성립",
    7: "아코디언 행렬 결합은 Matrix 추상 불성립",
    9: "섀시 활용률 결합 불성립 - Utilization",
    10: "계약 변경 혜택 결합은 Benefit 추상 불명확",
    12: "연금 감가상각 결합 불성립",
    13: "외장재 사직 결합은 Resignation 불성립",
    14: "논문에 위험 결합 불성립",
    15: "회의에 보증인 결합 불성립",
    16: "헤드라인에 튜너 결합 불성립",
    19: "연습 양식 결합은 Form 다의어 불명확",
    20: "리사이탈 전표 결합은 Slip 불명확",
    21: "오디션 합계 결합은 Sum 불성립",
    22: "조율 서명 결합은 Signature 불성립",
    23: "이론 렌더링 결합은 Rendering 불성립",
    25: "템포 매칭 결합은 Match가 강사-학생 매칭만 승인",
    26: "레퍼토리 예측기 결합은 Predictor 불성립",
    27: "합주 시간 결합은 Time 속성어 불성립",
    28: "반주자 접수 결합은 Reception 불성립",
    31: "피부양자 활용률 결합 불성립 - Utilization",
    32: "목공 혜택 결합은 Benefit 추상 불명확",
    33: "행동 감가상각 결합 불성립",
    34: "보모 사직 결합은 Resignation 불성립",
    35: "메트로놈에 보증인 결합 불성립",
    36: "운동에 튜너 결합 불성립",
    37: "증서 허브 결합은 Hub 추상 불성립",
    38: "곡집 나침반 결합은 Compass 추상 불성립",
    39: "교법 범위 결합은 Scope 불성립",
    41: "합창 게시판 결합은 Board 다의어 불명확",
    42: "퇴직 스튜디오 결합은 불성립",
    43: "오케스트라 터미널 결합은 Terminal 불성립",
    44: "유산 존 결합은 Zone 불성립",
    45: "멜로디 패널 결합은 Panel 불성립",
    46: "리듬 흔적 결합은 Trail 불성립",
    47: "비트 연결점 결합은 Nexus 추상 불성립",
    48: "피치 엔진 결합은 Engine 추상 불성립",
    51: "기부자 활용률 결합 불성립 - Utilization",
    52: "편집 감가상각 결합 불성립",
    53: "배포에 튜너 결합 불성립",
    54: "피아노 센터 결합은 Center 불성립",
    55: "기타 점수 결합은 Score를 악보로 오독 - 심사 채점 대상 불성립",
    56: "바이올린 부채 결합은 Debt 기각 라인",
    57: "드럼 합계 결합은 Total 불성립",
    63: "채용 감가상각 결합 불성립",
    64: "카탈로그에 위험 결합 불성립",
    65: "점유에 보증인 결합 불성립",
    66: "코호트에 튜너 결합 불성립",
    67: "플루트 관문 결합은 Gate 불성립",
    68: "첼로 피드 결합은 Feed 불성립",
    69: "색소폰 벌금·미세 결합은 Fine 다의어 불명확",
    71: "클라리넷 인장 결합은 Seal 불성립",
    73: "편집 활용률 결합 불성립 - Utilization",
    74: "축사 혜택 결합은 Benefit 추상 불명확",
    75: "탁도 감가상각 결합 불성립",
    76: "폼 사직 결합은 Resignation 불성립",
    77: "세탁기에 위험 결합 불성립",
    78: "호스텔에 보증인 결합 불성립",
    79: "베이스 튜너 결합은 악기 튜너로 오독, 서비스 불성립",
    80: "오르간 모니터 결합은 의료 장기 모니터로 오독 - 불명확",
    81: "검인 운영 결합은 Probate 도구형 기각 라인",
    83: "오보에 합계 결합은 Sum 불성립",
    84: "비올라 연체료 결합은 Arrears 기각 라인",
    86: "타액 모델 결합은 Model 속성어 불성립",
    87: "만돌린 길이 결합은 Length 속성어 불성립",
    89: "송금 활용률 결합 불성립 - Utilization",
    90: "섀시 혜택 결합은 Benefit 추상 불명확",
    92: "잔존물 감가상각 결합 불성립",
    93: "연금 사직 결합은 Resignation 불성립",
    95: "논문에 보증인 결합 불성립",
    96: "회의에 튜너 결합 불성립",
    97: "하모니카 틀 결합은 Frame 불성립",
    98: "레슨 동반자 결합은 Companion 불명확 기각 라인",
    99: "연습 카드 결합은 Card 다의어 불명확",
    100: "리사이탈 샘플 결합은 Sample 불명확",
    101: "오디션 부채 결합은 Debt 기각 라인",
    102: "조율 표식 결합은 Marker 불명확",
    104: "코드 추세 결합은 Trend 불명확",
    105: "템포 검증 결합은 Validation 불성립",
    106: "레퍼토리 인장 결합은 Seal 불성립",
    107: "합주 속도 결합은 Speed 속성어 불성립",
    111: "소송 활용률 결합 불성립 - Utilization",
    112: "피부양자 혜택 결합은 Benefit 추상 불명확",
    114: "행동 사직 결합은 Resignation 불성립",
    115: "보모에 위험 결합 불성립",
    116: "메트로놈에 튜너 결합 불성립",
    117: "증서 데스크 결합은 Desk 추상 불성립",
    118: "곡집 등대 결합은 Beacon 추상 불성립",
    119: "교법 루프 결합은 Loop 추상 불성립",
    120: "캠프 틀 결합은 Frame 불성립",
    121: "합창 데크 결합은 Deck 불성립",
    122: "퇴직 실험실 결합은 Lab 불성립",
    123: "오케스트라 센터 결합은 Center 불성립",
    124: "유산 포털 결합은 추상 재산어에 Portal 불성립",
    125: "멜로디 저울 결합은 Scale 다의어 불명확",
    126: "리듬 체인 결합은 Chain 추상 불성립",
    127: "비트 대성지도 결합은 Atlas 추상 불성립",
    128: "피치 조수 결합은 Assistant 불명확 기각 라인",
    131: "계량기 활용률 결합 불성립 - Utilization",
    132: "기부자 혜택 결합은 Benefit 추상 불명확",
    133: "편집 사직 결합은 Resignation 불성립",
    134: "피아노 존 결합은 Zone 불성립",
    135: "기타 음표·메모 결합은 Note 다의어 불명확",
    136: "바이올린 펀드 결합은 Fund 기각 라인",
    137: "드럼 위젯 결합은 Widget 불성립",
    138: "보컬 보증 결합은 Warranty 불성립",
    139: "우쿨렐레 행렬 결합은 Matrix 추상 불성립",
    141: "사건 활용률 결합 불성립 - Utilization",
    142: "자부담 감가상각 결합 불성립",
    143: "채용 사직 결합은 Resignation 불성립",
    144: "카탈로그에 보증인 결합 불성립",
    145: "점유에 튜너 결합 불성립",
    146: "플루트 연결점 결합은 Nexus 추상 불성립",
    148: "색소폰 번호 결합은 Number 속성어 불성립",
    150: "클라리넷 리뷰 결합은 검토 vs 후기 다의어 불명확",
    153: "편집 혜택 결합은 Benefit 추상 불명확",
    155: "탁도 사직 결합은 Resignation 불성립",
    156: "세차 폼에 위험 결합 불성립",
    157: "세탁기에 보증인 결합 불성립",
    158: "호스텔에 튜너 결합 불성립",
    160: "오르간 동반자 결합은 Companion 불명확 기각 라인",
    163: "오보에 부채 결합은 Debt 기각 라인",
    164: "비올라 선급금 결합은 Advance 기각 라인",
    165: "트롬본 보호자 결합은 Guardian 불명확 기각 라인",
    167: "만돌린 무게 결합은 Weight 속성어 불성립",
    170: "송금 혜택 결합은 Benefit 추상 불명확",
    172: "계약 변경 감가상각 결합 불성립",
    173: "잔존물 사직 결합은 Resignation 불성립",
    174: "연금에 위험 결합 불성립",
    175: "외장재에 보증인 결합 불성립",
    176: "논문에 튜너 결합 불성립",
    177: "하모니카 베이스 결합은 Base 추상 불성립",
    179: "연습 악보·시트 결합은 Sheet 다의어 불명확",
    180: "리사이탈 시간대 결합은 Slot 불명확",
    181: "오디션 펀드 결합은 Fund 기각 라인",
    182: "조율 잔고 결합은 Balance 다의어 불명확",
    183: "이론 키트 결합은 Kit 불명확",
    184: "코드 비교 결합은 Comparison 불명확",
    185: "템포 조회 결합은 Lookup 불성립",
    186: "레퍼토리 리뷰 결합은 검토 vs 후기 다의어 불명확",
    187: "합주 깊이 결합은 Depth 속성어 불성립",
    191: "동네 활용률 결합 불성립 - Utilization",
    192: "소송 혜택 결합은 Benefit 추상 불명확",
    194: "목공 감가상각 결합 불성립",
    195: "행동에 위험 결합 불성립",
    196: "보모에 보증인 결합 불성립",
    197: "메트로놈 추적기 결합은 불성립",
    198: "증서 레이더 결합은 Radar 추상 불성립",
    199: "곡집 대장간 결합은 Forge 불성립",
    200: "교법 격자 결합은 Grid 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 48, len(APPROVE)
assert len(TRADEMARK_REJECT) == 1, len(TRADEMARK_REJECT)
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
