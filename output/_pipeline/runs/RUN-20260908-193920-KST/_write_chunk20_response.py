import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk19_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk19_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "오르간 연습 플레이북 관리로 명확 (Playbook 라인)"),
    3: (0.6, "검인 기한 캘린더 관리로 명확 (Calendar 라인)"),
    4: (0.6, "하프 레슨 견적 관리로 명확 (Estimate 라인)"),
    10: (0.6, "수영장 계절 마감(closing) 평가로 명확 - 수영장 관리 실무 (Evaluation 라인)"),
    11: (0.6, "스펀지 확인 설문으로 명확"),
    14: (0.6, "아코디언 레슨 요건 관리로 명확 (Requirement 라인)"),
    20: (0.6, "레슨 일지 관리로 명확 (Journal 라인)"),
    21: (0.6, "연습 메모 관리로 명확 (Memo·Note 라인)"),
    22: (0.6, "리사이탈 성취 배지 관리로 명확 (Badge 라인)"),
    26: (0.6, "코드 연습 기록 관리로 명확 (Record 라인)"),
    28: (0.6, "레퍼토리 연습 일지 관리로 명확 (Diary 라인)"),
    30: (0.6, "포도원·와이너리 평가로 명확 - 여행 실무 (Evaluation 라인)"),
    31: (0.6, "반주자 확인 설문으로 명확"),
    34: (0.6, "평상형 트럭 운송 요건 관리로 명확 (Requirement 라인)"),
    52: (0.6, "생산 기준 요건 관리로 명확 (Requirement 라인)"),
    60: (0.6, "보컬 발성 교정 관리로 명확 - 보컬 코칭 실재"),
    61: (0.6, "세차 코팅 품질 평가로 명확 - 세차 실무 (Evaluation 라인)"),
    62: (0.6, "변기 확인 설문으로 명확"),
    72: (0.6, "클라리넷 수강료 환불 관리로 명확 (Refund 라인)"),
    73: (0.6, "항구 시설 평가로 명확 - 해운 실무 (Evaluation 라인)"),
    74: (0.6, "운행 기록부 확인 설문으로 명확"),
    77: (0.6, "전자 잠금 키패드 요건 관리로 명확 (Requirement 라인)"),
    82: (0.6, "오르간 연습 일지 관리로 명확 (Journal 라인)"),
    83: (0.6, "검인 전문가 디렉터리 관리로 명확 (Directory 라인)"),
    84: (0.6, "하프 공연 순서 관리로 명확 (Order 라인)"),
    87: (0.6, "트롬본 연습 스트릭 관리로 명확 (Streak 라인)"),
    88: (0.6, "타액 레슨 예약 관리로 명확 (Appointment 라인)"),
    90: (0.6, "제설 서비스 평가로 명확 - 시설 관리 실무 (Evaluation 라인)"),
    91: (0.6, "마감 확인 설문으로 명확"),
    94: (0.6, "로드트립 준비 요건 관리로 명확 (Requirement 라인)"),
    100: (0.6, "레슨 등록 명부 관리로 명확 (Registry 라인)"),
    110: (0.6, "연석(curb) 시공 평가로 명확 - 시설 관리 실무 (Evaluation 라인)"),
    111: (0.6, "포도원 확인 설문으로 명확"),
    114: (0.6, "채무자 심사 요건 관리로 명확 (Requirement 라인)"),
    131: (0.6, "비트 연습 플래너로 명확 (Planner 라인)"),
    132: (0.6, "음정 기록 대장 관리로 명확 (Register 라인)"),
    135: (0.6, "계량기 작업 감전 위험 관리로 명확 - 물리 위험 실존"),
    138: (0.6, "기타 연습 이력 관리로 명확 (History 라인)"),
    142: (0.6, "수영장 라이너(방수포) 평가로 명확 - 수영장 관리 실무 (Evaluation 라인)"),
    143: (0.6, "코팅 확인 설문으로 명확"),
    146: (0.6, "우쿨렐레 레슨 요건 관리로 명확 (Requirement 라인)"),
    150: (0.6, "첼로 공연 티켓 관리로 명확 (Ticket 라인)"),
    152: (0.6, "트럼펫 연습 스트릭 관리로 명확 (Streak 라인)"),
    153: (0.6, "클라리넷 지출 관리로 명확 (Expense 라인)"),
    154: (0.6, "항구 확인 설문으로 명확"),
    157: (0.6, "코일 점검 요건 관리로 명확 (Requirement 라인)"),
    163: (0.6, "오르간 등록부 관리로 명확 (Registry 라인)"),
    165: (0.6, "하프 청구서 관리로 명확 (Bill 라인)"),
    168: (0.6, "트롬본 숙련 등급 관리로 명확 (Rank 라인)"),
    169: (0.6, "타액 레슨 피드백 관리로 명확 (Feedback 라인)"),
    171: (0.6, "웨딩케이크 시식 평가로 명확 - 웨딩 실무 (Evaluation 라인)"),
    172: (0.6, "제설 확인 설문으로 명확"),
    175: (0.6, "배수 트랩 점검 요건 관리로 명확 (Requirement 라인)"),
    180: (0.6, "하모니카 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    181: (0.6, "레슨 일정 캘린더로 명확 (Calendar 라인)"),
    183: (0.6, "리사이탈 정산 명세 관리로 명확 (Statement 명세 라인)"),
    191: (0.6, "연석 확인 설문으로 명확"),
    194: (0.6, "질병 진료 기준 요건 관리로 명확 (Requirement 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "베이스 데스크 결합은 Desk 추상 불성립",
    5: "오보에 판매 결합은 Sale 기각 라인",
    6: "비올라 상환·구제 결합은 Redemption 불성립",
    7: "트롬본 결과 결합은 Result 불명확",
    8: "타액 바코드 결합은 Barcode 불성립",
    9: "만돌린 한도 결합은 Limit 속성어 불성립",
    12: "트랩 활용률 결합 불성립 - Utilization",
    13: "로드트립 혜택 결합은 Benefit 추상 불명확",
    15: "송금 사직 결합은 Resignation 불성립",
    16: "섀시에 위험 결합 불성립",
    17: "계약 변경에 보증인 결합 불성립",
    18: "잔존물에 튜너 결합 불성립",
    19: "하모니카 게시판 결합은 Board 다의어 불명확",
    23: "오디션 요금 결합은 Charge 다의어 불명확",
    24: "조율 부과금 결합은 Levy 기각 라인",
    25: "이론 합계 결합은 Total 불성립",
    27: "템포 가용성 결합은 불성립",
    29: "합주 온도 결합은 Temperature 불성립",
    32: "질병 활용률 결합 불성립 - Utilization",
    33: "채무자 혜택 결합은 Benefit 추상 불명확",
    35: "동네 감가상각 결합 불성립",
    36: "소송 사직 결합은 Resignation 불성립",
    37: "피부양자에 위험 결합 불성립",
    38: "목공에 보증인 결합 불성립",
    39: "메트로놈 데스크 결합은 Desk 추상 불성립",
    40: "증서 나침반 결합은 Compass 추상 불성립",
    41: "곡집 신호 결합은 Signal 추상 불성립",
    42: "교법 포인트 결합은 Point 불성립",
    43: "캠프 게시판 결합은 Board 다의어 불명확",
    44: "합창 터미널 결합은 Terminal 불성립",
    45: "퇴직 존 결합은 Zone 불성립",
    46: "오케스트라 패널 결합은 Panel 불성립",
    47: "유산 경로 결합은 Route 불성립",
    48: "멜로디 체인 결합은 Chain 추상 불성립",
    49: "리듬 대성지도 결합은 Atlas 추상 불성립",
    50: "비트 조수 결합은 Assistant 불명확 기각 라인",
    51: "피치 동반자 결합은 Companion 불명확 기각 라인",
    53: "수확 감가상각 결합 불성립",
    54: "계량기 사직 결합은 Resignation 불성립",
    55: "기부자에 위험 결합 불성립",
    56: "피아노 저울 결합은 Scale 다의어 불명확",
    57: "기타 뷰 결합은 View 불성립",
    58: "바이올린 의무 결합은 Duty 다의어 불명확",
    59: "드럼 변환기 결합은 불성립",
    63: "휴가 활용률 결합 불성립 - Utilization",
    64: "우쿨렐레 혜택 결합은 Benefit 추상 불명확",
    65: "계정 조정 감가상각 결합 불성립",
    66: "사건 사직 결합은 Resignation 불성립",
    67: "자부담에 튜너 결합 불성립",
    68: "플루트 엔진 결합은 Engine 추상 불성립",
    69: "첼로 색인 결합은 Index 불성립",
    70: "색소폰 세부 결합은 Detail 속성어 불성립",
    71: "트럼펫 결과 결합은 Result 불명확",
    75: "광미 활용률 결합 불성립 - Utilization",
    76: "코일 혜택 결합은 Benefit 추상 불명확",
    78: "이중언어 감가상각 결합 불성립",
    79: "편집에 위험 결합 불성립",
    80: "축사에 보증인 결합 불성립",
    81: "베이스 레이더 결합은 Radar 추상 불성립",
    85: "오보에 요금 결합은 Charge 다의어 불명확",
    86: "비올라 연장 결합은 Extension 불성립",
    89: "만돌린 유형 결합은 Type 속성어 불성립",
    92: "스펀지 활용률 결합 불성립 - Utilization",
    93: "트랩 혜택 결합은 Benefit 추상 불명확",
    95: "아코디언 감가상각 결합 불성립",
    96: "송금에 위험 결합 불성립",
    97: "섀시에 보증인 결합 불성립",
    98: "계약 변경에 튜너 결합 불성립",
    99: "하모니카 데크 결합은 Deck 불성립",
    101: "연습 태그 결합은 Tag 불성립",
    102: "리사이탈 표 Stub 결합은 불명확",
    103: "오디션 의무 결합은 Duty 다의어 불명확",
    104: "조율 연체 결합은 Due 다의어 불명확",
    105: "이론 위젯 결합은 Widget 불성립",
    106: "코드 사본 결합은 Copy 불성립",
    107: "템포 자격 결합은 불성립",
    108: "레퍼토리 환불 결합은 불성립",
    109: "합주 압력 결합은 Pressure 불성립",
    112: "반주자 활용률 결합 불성립 - Utilization",
    113: "질병 혜택 결합은 Benefit 추상 불명확",
    115: "평상형 트럭 감가상각 결합 불성립",
    116: "동네 사직 결합은 Resignation 불성립",
    117: "소송에 위험 결합 불성립",
    118: "피부양자에 보증인 결합 불성립",
    119: "목공에 튜너 결합 불성립",
    120: "메트로놈 레이더 결합은 Radar 추상 불성립",
    121: "증서 등대 결합은 Beacon 추상 불성립",
    122: "곡집 감시 결합은 Watch 불성립",
    123: "교법 지도 결합은 불성립",
    124: "캠프 데크 결합은 Deck 불성립",
    125: "합창 센터 결합은 Center 불성립",
    126: "퇴직 포털 결합은 추상 재산어에 Portal 불성립",
    127: "오케스트라 저울 결합은 Scale 다의어 불명확",
    128: "유산 궤도 결합은 Rail 불성립",
    129: "멜로디 링 결합은 Ring 불성립",
    130: "리듬 관리자 결합은 Keeper 불명확 기각 라인",
    133: "생산 감가상각 결합 불성립",
    134: "수확 사직 결합은 Resignation 불성립",
    136: "기부자에 보증인 결합 불성립",
    137: "피아노 경로 결합은 Route 불성립",
    139: "바이올린 수당 결합은 Allowance 기각 라인",
    140: "드럼 생성기 결합은 불성립",
    141: "보컬 개정 결합은 Revision 불성립",
    144: "변기 활용률 결합 불성립 - Utilization",
    145: "휴가 혜택 결합은 Benefit 추상 불명확",
    147: "계정 조정 사직 결합은 Resignation 불성립",
    148: "사건에 위험 결합 불성립",
    149: "플루트 조수 결합은 Assistant 불명확 기각 라인",
    151: "색소폰 식별자 결합은 Identifier 불성립",
    155: "운행 기록부 활용률 결합 불성립 - Utilization",
    156: "광미 혜택 결합은 Benefit 추상 불명확",
    158: "키패드 감가상각 결합 불성립",
    159: "이중언어 사직 결합은 Resignation 불성립",
    160: "편집에 보증인 결합 불성립",
    161: "축사에 튜너 결합 불성립",
    162: "베이스 릴레이 결합은 Relay 불성립",
    164: "검인 탐색기 결합은 Probate 도구형 기각 라인",
    166: "오보에 의무 결합은 Duty 다의어 불명확",
    167: "비올라 시험 결합은 Trial 다의어 불명확",
    170: "만돌린 시계 결합은 불성립",
    173: "마감 활용률 결합 불성립 - Utilization",
    174: "스펀지 혜택 결합은 Benefit 추상 불명확",
    176: "로드트립 감가상각 결합 불성립",
    177: "아코디언 사직 결합은 Resignation 불성립",
    178: "송금에 보증인 결합 불성립",
    179: "섀시에 튜너 결합 불성립",
    182: "연습 프로필 결합은 Profile 불성립",
    184: "오디션 수당 결합은 Allowance 기각 라인",
    185: "조율 보조금 결합은 Subsidy 기각 라인",
    186: "이론 저장소 결합은 Repository 기술용어 불성립",
    187: "코드 독보 결합은 Reading 다의어 불명확",
    188: "템포 방송 결합은 불성립",
    189: "레퍼토리 지출 결합은 불성립",
    190: "합주 부하 결합은 Load 불성립",
    192: "포도원 활용률 결합 불성립 - Utilization",
    193: "반주자 혜택 결합은 Benefit 추상 불명확",
    195: "채무자 감가상각 결합 불성립",
    196: "평상형 트럭 사직 결합은 Resignation 불성립",
    197: "동네에 위험 결합 불성립",
    198: "소송에 보증인 결합 불성립",
    199: "피부양자에 튜너 결합 불성립",
    200: "메트로놈 릴레이 결합은 Relay 불성립",
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
