import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk16_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk16_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "합주 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    16: (0.6, "보컬 레슨 피드백 관리로 명확 (Feedback 라인)"),
    18: (0.6, "자부담 확인 설문으로 명확"),
    20: (0.6, "카탈로그 요건 관리로 명확 (Requirement 라인)"),
    30: (0.6, "결혼식 축사 품질 평가로 명확 - 웨딩 플래닝 실무 (Evaluation 라인)"),
    33: (0.6, "세탁기 설치·교체 요건 관리로 명확 (Requirement 라인)"),
    46: (0.6, "만돌린 레슨 온보딩 관리로 명확 (Onboarding 라인)"),
    47: (0.6, "아코디언 레슨 후속 관리로 명확 (Followup 라인)"),
    48: (0.6, "차량 섀시 검사 평가로 명확 - 물류 검사 실무 (Evaluation 라인)"),
    49: (0.6, "계약 변경 확인 설문으로 명확"),
    52: (0.6, "외장재 시공 요건 관리로 명확 (Requirement 라인)"),
    59: (0.6, "레슨 일정 플래너로 명확 (Planner 라인)"),
    60: (0.6, "연습 보고서 관리로 명확 (Report 라인)"),
    61: (0.6, "리사이탈 출연 목록 관리로 명확 (List 라인)"),
    64: (0.6, "음악이론 정리 스케치 관리로 명확 (Sketch 라인)"),
    70: (0.6, "급여 실무 피부양자 자격 평가로 명확 - HR 실무 (Evaluation 라인)"),
    71: (0.6, "목공 확인 설문으로 명확"),
    73: (0.6, "보모 고용 요건 관리로 명확 (Requirement 라인)"),
    78: (0.6, "부동산 증서 처리 진행 추적으로 명확 (Tracker 라인)"),
    90: (0.6, "기부자 자격·등급 평가로 명확 - 비영리 실무 (Evaluation 라인)"),
    97: (0.6, "보컬 수강료 청구서 관리로 명확 (Invoice 라인)"),
    109: (0.6, "클라리넷 운지법 연습 시뮬레이터로 실재 도구 (Simulator 라인)"),
    110: (0.6, "사진 보정 품질 평가로 명확 - 사진 실무 (Evaluation 라인)"),
    111: (0.6, "축사 확인 설문으로 명확"),
    113: (0.6, "세차 폼 장비 요건 관리로 명확 (Requirement 라인)"),
    119: (0.6, "오르간 레슨 플래너로 명확 (Planner 라인)"),
    121: (0.6, "하프 편곡·연주 초안 관리로 명확 (Draft 라인)"),
    126: (0.6, "만돌린 레슨 출석 체크인으로 명확 (Checkin 라인)"),
    127: (0.6, "아코디언 레슨 신청 승인 관리로 명확 (Approval 라인)"),
    128: (0.6, "송금 거래 리스크 평가로 명확 - 금융 컴플라이언스 실무 (Evaluation 라인)"),
    129: (0.6, "섀시 확인 설문으로 명확"),
    132: (0.6, "연금 자격 요건 관리로 명확 (Requirement 라인)"),
    139: (0.6, "레슨 일정 스케줄러로 명확 (Scheduler 라인)"),
    140: (0.6, "연습 로그 관리로 명확 (Log 라인)"),
    145: (0.6, "코드 연습 스트릭 관리로 명확 (Streak 라인)"),
    147: (0.6, "레퍼토리 연주 연습 시뮬레이터로 실재 도구 (Simulator 라인)"),
    150: (0.6, "보험 소송 리스크 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    151: (0.6, "피부양자 확인 설문으로 명확"),
    170: (0.6, "전력·가스 계량기 검침 평가로 명확 - 유틸리티 실무 (Evaluation 라인)"),
    171: (0.6, "기부자 확인 설문으로 명확"),
    172: (0.6, "편집 품질 요건 관리로 명확 (Requirement 라인)"),
    175: (0.6, "기타 연습·악기 점검 관리로 명확 (Check 라인)"),
    178: (0.6, "보컬 수강 갱신 관리로 명확 (Renewal 라인)"),
    179: (0.6, "우쿨렐레 레슨 후속 관리로 명확 (Followup 라인)"),
    180: (0.6, "법률 사건 평가로 명확 - 로펌 실무 (Evaluation 라인)"),
    182: (0.6, "채용 요건 관리로 명확 (Requirement 라인)"),
    187: (0.6, "첼로 연습 소식·갱신 관리로 명확 (Update 라인)"),
    191: (0.6, "편집 확인 설문으로 명확"),
    193: (0.6, "수영장 탁도 기준 요건 관리로 명확 (Requirement 라인)"),
    199: (0.6, "오르간 레슨 스케줄러로 명확 (Scheduler 라인)"),
    200: (0.6, "검인 사건 대장 관리로 명확 - Register 기록물 라인"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "합창 베이스 결합은 Base 추상 불성립",
    2: "퇴직 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    4: "유산 스테이션 결합은 Station 불성립",
    5: "멜로디 존 결합은 Zone 불성립",
    6: "리듬 저울 결합은 Scale 다의어 불명확",
    7: "비트 체인 결합은 Chain 추상 불성립",
    8: "피치 대성지도 결합은 Atlas 추상 불성립",
    9: "편집 활용률 결합 불성립 - Utilization",
    10: "배포 사직 결합은 Resignation 불성립",
    11: "등록에 튜너 결합 불성립",
    12: "피아노 실험실 결합은 Lab 불성립",
    13: "기타 카드 결합은 Card 다의어 불명확",
    14: "바이올린 세금 결합은 Tax 기각 라인",
    15: "드럼 키트 결합은 악기 자체 지칭, 서비스 대상 불성립",
    17: "우쿨렐레 센서 결합은 Sensor 불성립",
    19: "채용 활용률 결합 불성립 - Utilization",
    21: "점유 감가상각 결합 불성립",
    22: "코호트 사직 결합은 Resignation 불성립",
    23: "농약에 보증인 결합 불성립",
    24: "변전소에 튜너 결합 불성립",
    25: "플루트 흔적 결합은 Trail 불성립",
    26: "첼로 수준 결합은 Level 속성어 불성립",
    27: "색소폰 가치 결합은 Value 속성어 불성립",
    28: "트럼펫 추정기 결합은 불성립",
    29: "클라리넷 검증 결합은 Verification 불성립",
    31: "탁도 활용률 결합 불성립 - Utilization",
    32: "폼 혜택 결합은 Benefit 추상 불명확",
    34: "호스텔 감가상각 결합 불성립",
    35: "베이스 사직 결합은 Resignation 불성립",
    36: "분류(triage)에 위험 결합 불성립",
    37: "배당에 보증인 결합 불성립",
    38: "패러리걸에 튜너 결합 불성립",
    39: "오르간 조수 결합은 Assistant 불명확 기각 라인",
    40: "검인 모니터 결합은 Probate 도구형 기각 라인",
    41: "하프 피드 결합은 Feed 불성립",
    42: "오보에 요금(교통) 결합은 Fare 기각 라인",
    43: "비올라 연체금 결합은 Due 다의어 불명확",
    44: "트롬본 검사기 결합은 불성립",
    45: "타액 검증 결합은 Validation 불성립",
    50: "잔존물 활용률 결합 불성립 - Utilization",
    51: "연금 혜택 결합은 Benefit 추상 불명확",
    53: "논문 감가상각 결합 불성립",
    54: "회의 사직 결합은 Resignation 불성립",
    55: "헤드라인에 위험 결합 불성립",
    56: "우선순위에 보증인 결합 불성립",
    57: "헤드헌터에 튜너 결합 불성립",
    58: "하모니카 경로 결합은 Path 추상 불성립",
    62: "오디션 세금 결합은 Tax 기각 라인",
    63: "조율 일련번호 결합은 Serial 불성립",
    65: "코드 결과 결합은 Result 불명확",
    66: "템포 계좌 결합은 Account 다의어 불명확",
    67: "레퍼토리 검증 결합은 Verification 불성립",
    68: "합주 유형 결합은 Type 속성어 불성립",
    69: "반주자 고장 분석 결합은 Breakdown 불성립",
    72: "행동 혜택 결합은 Benefit 추상 불명확",
    74: "메트로놈 사직 결합은 Resignation 불성립",
    75: "운동에 위험 결합 불성립",
    76: "수취인에 보증인 결합 불성립",
    77: "탱커에 튜너 결합 불성립",
    79: "곡집 릴레이 결합은 Relay 불성립",
    80: "교법 신호 결합은 Signal 추상 불성립",
    81: "캠프 경로 결합은 Path 추상 불성립",
    82: "합창 코어 결합은 Core 불성립",
    83: "퇴직 게시판 결합은 Board 다의어 불명확",
    84: "오케스트라 실험실 결합은 Lab 불성립",
    85: "유산 터미널 결합은 Terminal 불성립",
    86: "멜로디 포털 결합은 추상 음악어에 Portal 불성립",
    87: "리듬 경로 결합은 Route 불성립",
    88: "비트 링 결합은 Ring 불성립",
    89: "피치 관리자 결합은 Keeper 불명확 기각 라인",
    91: "편집 혜택 결합은 Benefit 추상 불명확",
    92: "배포에 물리 위험 결합 불성립",
    93: "피아노 스테이션 결합은 Station 불성립",
    94: "기타 악보·시트 결합은 Sheet 다의어 불명확",
    95: "바이올린 대출 결합은 Loan 기각 라인",
    96: "드럼 개수 결합은 Count 속성어 불성립",
    98: "우쿨렐레 접수 결합은 Reception 불성립",
    99: "자부담 활용률 결합 불성립 - Utilization",
    100: "채용 혜택 결합은 Benefit 추상 불명확",
    101: "카탈로그 감가상각 결합 불성립",
    102: "점유 사직 결합은 Resignation 불성립",
    103: "코호트에 위험 결합 불성립",
    104: "농약에 튜너 결합 불성립",
    105: "플루트 체인 결합은 Chain 추상 불성립",
    106: "첼로 요율 결합은 Rate 속성어 불성립",
    107: "색소폰 지분 결합은 Stake 불성립",
    108: "트럼펫 검사기 결합은 불성립",
    112: "탁도 혜택 결합은 Benefit 추상 불명확",
    114: "세탁기 감가상각 결합 불성립",
    115: "호스텔 사직 결합은 Resignation 불성립",
    116: "베이스에 위험 결합 불성립",
    117: "분류(triage)에 보증인 결합 불성립",
    118: "배당에 튜너 결합 불성립",
    120: "검인 동반자 결합은 Probate 도구형 기각 라인",
    122: "오보에 세금 결합은 Tax 기각 라인",
    123: "비올라 보조금 결합은 Subsidy 기각 라인",
    124: "트롬본 탐지기 결합은 불성립",
    125: "타액 조회 결합은 Lookup 불성립",
    130: "계약 변경 활용률 결합 불성립 - Utilization",
    131: "잔존물 혜택 결합은 Benefit 추상 불명확",
    133: "외장재 감가상각 결합 불성립",
    134: "논문 사직 결합은 Resignation 불성립",
    135: "회의에 위험 결합 불성립",
    136: "헤드라인에 보증인 결합 불성립",
    137: "우선순위에 튜너 결합 불성립",
    138: "하모니카 포인트 결합은 Point 불성립",
    141: "리사이탈 표 결합은 Table 다의어 불명확",
    142: "오디션 대출 결합은 Loan 기각 라인",
    143: "조율 토큰 결합은 Token 불성립",
    144: "이론 개요 결합은 Outline 불성립",
    146: "템포 케이스 결합은 Case 다의어 불명확",
    148: "합주 시계 결합은 불성립",
    149: "반주자 센서 결합은 Sensor 불성립",
    152: "목공 활용률 결합 불성립 - Utilization",
    153: "행동에 요건 결합 불성립",
    154: "보모 감가상각 결합 불성립",
    155: "메트로놈에 위험 결합 불성립",
    156: "운동에 보증인 결합 불성립",
    157: "수취인에 튜너 결합 불성립",
    158: "증서 흐름 결합은 Flow 불성립",
    159: "곡집 금고 결합은 Vault 불성립",
    160: "교법 감시 결합은 Watch 불성립",
    161: "캠프 포인트 결합은 Point 불성립",
    162: "합창 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    163: "퇴직 데크 결합은 Deck 불성립",
    164: "오케스트라 스테이션 결합은 Station 불성립",
    165: "유산 센터 결합은 Center 불성립",
    166: "멜로디 콘솔 결합은 Console 도구형 불성립",
    167: "리듬 궤도 결합은 Rail 불성립",
    168: "비트 관문 결합은 Gate 불성립",
    169: "피치 관리자 결합은 Manager 불성립",
    173: "배포에 보증인 결합 불성립",
    174: "피아노 터미널 결합은 Terminal 불성립",
    176: "바이올린 합계 결합은 Sum 불성립",
    177: "드럼 메시지 결합은 Message 불성립",
    181: "자부담 혜택 결합은 Benefit 추상 불명확",
    183: "카탈로그 사직 결합은 Resignation 불성립",
    184: "점유에 위험 결합 불성립",
    185: "코호트에 보증인 결합 불성립",
    186: "플루트 링 결합은 Ring 불성립",
    188: "색소폰 마진 결합은 Margin 기각 라인",
    189: "트럼펫 탐지기 결합은 불성립",
    190: "클라리넷 예측기 결합은 Predictor 불성립",
    192: "축사 활용률 결합 불성립 - Utilization",
    194: "폼 감가상각 결합 불성립",
    195: "세탁기 사직 결합은 Resignation 불성립",
    196: "호스텔에 위험 결합 불성립",
    197: "베이스에 보증인 결합 불성립",
    198: "분류(triage)에 튜너 결합 불성립",
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
