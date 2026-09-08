import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk18_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk18_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "합창 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    9: (0.6, "음악 연습 계획 플래너로 명확 (Planner 라인)"),
    10: (0.6, "생산 확인 설문으로 명확"),
    13: (0.6, "기부자 자격 요건 관리로 명확 (Requirement 라인)"),
    15: (0.6, "피아노 레슨 포털로 명확 - 구체 서비스 (Portal 라인)"),
    19: (0.6, "보컬 레슨 예약금 관리로 명확 (Deposit 라인)"),
    20: (0.6, "우쿨렐레 실력 평가로 명확 - 레슨 실무 (Evaluation 라인)"),
    27: (0.6, "첼로 연습 요약 관리로 명확 (Summary 라인)"),
    31: (0.6, "냉각·열교환 코일 검사 평가로 명확 - HVAC 실무 (Evaluation 라인)"),
    32: (0.6, "키패드 확인 설문으로 명확"),
    34: (0.6, "사진 편집 요건 관리로 명확 (Requirement 라인)"),
    40: (0.6, "오르간 출석 대장 관리로 명확 (Register 라인)"),
    41: (0.6, "검인 절차 기록 일지 관리로 명확 (Journal 라인)"),
    46: (0.6, "타액 수강 자격 확인 관리로 명확 (Eligibility 라인)"),
    48: (0.6, "배수 트랩 점검 평가로 명확 - 배관 실무 (Evaluation 라인)"),
    49: (0.6, "로드트립 확인 설문으로 명확"),
    51: (0.6, "송금 처리 요건 관리로 명확 (Requirement 라인)"),
    59: (0.6, "연습 점검 관리로 명확 (Check 라인)"),
    69: (0.6, "질병 상태 평가로 명확 - 의료 실무 (Evaluation 라인)"),
    70: (0.6, "채무자 확인 설문으로 명확"),
    73: (0.6, "소송 절차 요건 관리로 명확 (Requirement 라인)"),
    85: (0.6, "합주 연습 포털로 명확 - 구체 서비스 (Portal 라인)"),
    90: (0.6, "음악 연습 일정 스케줄러로 명확 (Scheduler 라인)"),
    93: (0.6, "계량기 검침 요건 관리로 명확 (Requirement 라인)"),
    99: (0.6, "드럼 연습 공지 관리로 명확 (Announcement 라인)"),
    100: (0.6, "보컬 자격 인증 관리로 명확 (Certification 라인)"),
    101: (0.6, "휴가 계획 평가로 명확 - 여행 실무 (Evaluation 라인)"),
    102: (0.6, "우쿨렐레 확인 설문으로 명확"),
    104: (0.6, "법률 사건 요건 관리로 명확 (Requirement 라인)"),
    108: (0.6, "첼로 연습 타임라인 관리로 명확 (Timeline 라인)"),
    111: (0.6, "클라리넷 레슨 영상 관리로 명확 (Video 라인)"),
    112: (0.6, "광미(tailings) 처리 평가로 명확 - 광업 실무 (Evaluation 라인)"),
    113: (0.6, "코일 확인 설문으로 명확"),
    122: (0.6, "검인 사건 등기부 관리로 명확 (Registry 라인)"),
    123: (0.6, "하프 공연 티켓 관리로 명확 (Ticket 라인)"),
    129: (0.6, "세차 스펀지 품질 평가로 명확 - 세차 실무 (Evaluation 라인)"),
    130: (0.6, "트랩 확인 설문으로 명확"),
    139: (0.6, "레슨 운영 플레이북 관리로 명확 (Playbook 라인)"),
    140: (0.6, "연습 채점 점수 관리로 명확 - 심사 채점 (Score 라인)"),
    141: (0.6, "리사이탈 이용권 바우처 관리로 명확 (Voucher 라인)"),
    147: (0.6, "레퍼토리 레슨 영상 관리로 명확 (Video 라인)"),
    149: (0.6, "반주자 실력 평가로 명확 - 레슨 실무 (Evaluation 라인)"),
    150: (0.6, "질병 확인 설문으로 명확"),
    153: (0.6, "동네 입지 요건 관리로 명확 (Requirement 라인)"),
    156: (0.6, "목공 작업 안전 위험 관리로 명확 - 기계 부상 위험 실존"),
    170: (0.6, "음정 모니터링 도구로 실재 도구 (Monitor 라인)"),
    172: (0.6, "수확 기준 요건 관리로 명확 (Requirement 라인)"),
    180: (0.6, "보컬 오디션 지명 관리로 명확 (Nomination 라인)"),
    181: (0.6, "변기 설치·수리 평가로 명확 - 배관 실무 (Evaluation 라인)"),
    182: (0.6, "휴가 확인 설문으로 명확"),
    184: (0.6, "계정 조정 기준 요건 관리로 명확 (Requirement 라인)"),
    189: (0.6, "첼로 연습 리마인더 관리로 명확 (Reminder 라인)"),
    192: (0.6, "클라리넷 연습 일기 관리로 명확 (Diary 라인)"),
    193: (0.6, "항공 운행 기록부 평가로 명확 - 항공 실무 (Evaluation 라인)"),
    194: (0.6, "광미 확인 설문으로 명확"),
    197: (0.6, "이중언어 품질 요건 관리로 명확 (Requirement 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "캠프 베이스 결합은 Base 추상 불성립",
    3: "퇴직 스테이션 결합은 Station 불성립",
    4: "오케스트라 존 결합은 Zone 불성립",
    5: "유산 콘솔 결합은 Console 도구형 불성립",
    6: "멜로디 경로 결합은 Route 불성립",
    7: "리듬 링 결합은 Ring 불성립",
    8: "비트 관리자 결합은 Keeper 불명확 기각 라인",
    11: "수확 활용률 결합 불성립 - Utilization",
    12: "계량기 혜택 결합은 Benefit 추상 불명확",
    14: "편집에 위험 결합 불성립",
    16: "기타 태그 결합은 Tag 불성립",
    17: "바이올린 현금 결합은 Cash 기각 라인",
    18: "드럼 저장소 결합은 Repository 기술용어 불성립",
    21: "계정 조정 활용률 결합 불성립 - Utilization",
    22: "사건 혜택 결합은 Benefit 추상 불명확",
    23: "자부담 사직 결합은 Resignation 불성립",
    24: "채용에 위험 결합 불성립",
    25: "카탈로그에 튜너 결합 불성립",
    26: "플루트 대성지도 결합은 Atlas 추상 불성립",
    28: "색소폰 버전 결합은 Version 속성어 불성립",
    29: "트럼펫 보호자 결합은 Guardian 불명확 기각 라인",
    30: "클라리넷 조리법 결합은 Recipe 불성립",
    33: "이중언어 활용률 결합 불성립 - Utilization",
    35: "축사 감가상각 결합 불성립",
    36: "탁도에 위험 결합 불성립",
    37: "폼에 보증인 결합 불성립",
    38: "세탁기에 튜너 결합 불성립",
    39: "베이스 흐름 결합은 Flow 불성립",
    42: "하프 색인 결합은 Index 불성립",
    43: "오보에 펀드 결합은 Fund 기각 라인",
    44: "비올라 과태료 결합은 Penalty 기각 라인",
    45: "트롬본 조수 결합은 Helper 불명확 기각 라인",
    47: "만돌린 거리 결합은 Distance 속성어 불성립",
    50: "아코디언 활용률 결합 불성립 - Utilization",
    52: "섀시 감가상각 결합 불성립",
    53: "계약 변경 사직 결합은 Resignation 불성립",
    54: "잔존물에 위험 결합 불성립",
    55: "연금에 보증인 결합 불성립",
    56: "외장재에 튜너 결합 불성립",
    57: "하모니카 코어 결합은 Core 불성립",
    58: "레슨 운영 결합은 Ops 불명확",
    60: "리사이탈 통행권 결합은 Pass 불명확",
    61: "오디션 현금 결합은 Cash 기각 라인",
    62: "조율 이자·관심 결합은 Interest 기각 라인",
    63: "이론 개수 결합은 Count 속성어 불성립",
    64: "코드 제안 결합은 Proposal 불명확",
    65: "템포 핑 결합은 Ping 불성립",
    66: "레퍼토리 조리법 결합은 Recipe 불성립",
    67: "합주 높이 결합은 Height 속성어 불성립",
    68: "반주자 행렬 결합은 Matrix 추상 불성립",
    71: "평상형 트럭 활용률 결합 불성립 - Utilization",
    72: "동네 혜택 결합은 Benefit 추상 불명확",
    74: "피부양자 감가상각 결합 불성립",
    75: "목공 사직 결합은 Resignation 불성립",
    76: "행동에 보증인 결합 불성립",
    77: "보모에 튜너 결합 불성립",
    78: "메트로놈 흐름 결합은 Flow 불성립",
    79: "증서 릴레이 결합은 Relay 불성립",
    80: "곡집 연쇄 결합은 Cascade 추상 불성립",
    81: "교법 파도 결합은 Wave 추상 불성립",
    82: "캠프 코어 결합은 Core 불성립",
    83: "합창 실험실 결합은 Lab 불성립",
    84: "퇴직 터미널 결합은 Terminal 불성립",
    86: "유산 패널 결합은 Panel 불성립",
    87: "멜로디 궤도 결합은 Rail 불성립",
    88: "리듬 관문 결합은 Gate 불성립",
    89: "비트 관리자 결합은 Manager 불성립",
    91: "생산 활용률 결합 불성립 - Utilization",
    92: "수확 혜택 결합은 Benefit 추상 불명확",
    94: "기부자 감가상각 결합 불성립",
    95: "편집에 보증인 결합 불성립",
    96: "피아노 콘솔 결합은 Console 도구형 불성립",
    97: "기타 프로필 결합은 Profile 불성립",
    98: "바이올린 판매 결합은 Sale 기각 라인",
    103: "계정 조정 혜택 결합은 Benefit 추상 불명확",
    105: "자부담에 위험 결합 불성립",
    106: "채용에 보증인 결합 불성립",
    107: "플루트 관리자 결합은 Keeper 불명확 기각 라인",
    109: "색소폰 링크 결합은 Link 불성립",
    110: "트럼펫 조수 결합은 Helper 불명확 기각 라인",
    114: "키패드 활용률 결합 불성립 - Utilization",
    115: "이중언어 혜택 결합은 Benefit 추상 불명확",
    116: "편집 감가상각 결합 불성립",
    117: "축사 사직 결합은 Resignation 불성립",
    118: "탁도에 보증인 결합 불성립",
    119: "폼에 튜너 결합 불성립",
    120: "베이스 허브 결합은 Hub 추상 불성립",
    121: "오르간 운영 결합은 Ops 불명확",
    124: "오보에 현금 결합은 Cash 기각 라인",
    125: "비올라 마크업 결합은 Markup 기각 라인",
    126: "트롬본 무대 결합은 Stage 다의어 불명확",
    127: "타액 방송 결합은 불명확",
    128: "만돌린 범위 결합은 Range 속성어 불성립",
    131: "로드트립 활용률 결합 불성립 - Utilization",
    132: "아코디언 혜택 결합은 Benefit 추상 불명확",
    133: "송금 감가상각 결합 불성립",
    134: "섀시 사직 결합은 Resignation 불성립",
    135: "계약 변경에 위험 결합 불성립",
    136: "잔존물에 보증인 결합 불성립",
    137: "연금에 튜너 결합 불성립",
    138: "하모니카 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    142: "오디션 판매 결합은 Sale 기각 라인",
    143: "조율 자산 결합은 Asset 단독 불명확",
    144: "이론 메시지 결합은 Message 불성립",
    145: "코드 보증 결합은 Guarantee 불성립",
    146: "템포 모델 결합은 Model 속성어 불성립",
    148: "합주 폭 결합은 Width 속성어 불성립",
    151: "채무자 활용률 결합 불성립 - Utilization",
    152: "평상형 트럭 혜택 결합은 Benefit 추상 불명확",
    154: "소송 감가상각 결합 불성립",
    155: "피부양자 사직 결합은 Resignation 불성립",
    157: "행동에 튜너 결합 불성립",
    158: "메트로놈 허브 결합은 Hub 추상 불성립",
    159: "증서 금고 결합은 Vault 불성립",
    160: "곡집 브리지 결합은 Bridge 기각 라인",
    161: "교법 경로 결합은 Path 추상 불성립",
    162: "캠프 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    163: "합창 스테이션 결합은 Station 불성립",
    164: "퇴직 센터 결합은 Center 불성립",
    165: "오케스트라 콘솔 결합은 Console 도구형 불성립",
    166: "유산 저울 결합은 Scale 다의어 불명확",
    167: "멜로디 흔적 결합은 Trail 불성립",
    168: "리듬 연결점 결합은 Nexus 추상 불성립",
    169: "비트 엔진 결합은 Engine 추상 불성립",
    171: "생산 혜택 결합은 Benefit 추상 불명확",
    173: "계량기 감가상각 결합 불성립",
    174: "기부자 사직 결합은 Resignation 불성립",
    175: "편집에 튜너 결합 불성립",
    176: "피아노 패널 결합은 Panel 불성립",
    177: "기타 상태 결합은 Status 불성립",
    178: "바이올린 요금 결합은 Charge 다의어 불명확",
    179: "드럼 계산기 결합은 불성립",
    183: "우쿨렐레 활용률 결합 불성립 - Utilization",
    185: "사건 감가상각 결합 불성립",
    186: "자부담에 보증인 결합 불성립",
    187: "채용에 튜너 결합 불성립",
    188: "플루트 관리자 결합은 Manager 불성립",
    190: "색소폰 규칙 결합은 Rule 불명확",
    191: "트럼펫 무대 결합은 Stage 다의어 불명확",
    195: "코일 활용률 결합 불성립 - Utilization",
    196: "키패드 혜택 결합은 Benefit 추상 불명확",
    198: "편집 사직 결합은 Resignation 불성립",
    199: "축사에 위험 결합 불성립",
    200: "탁도에 튜너 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 56, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 144, len(REJECT_REASON)
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
