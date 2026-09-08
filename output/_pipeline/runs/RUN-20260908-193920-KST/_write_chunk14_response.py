import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk13_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk13_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    5: (0.6, "타액 연습 템플릿 관리로 명확 (Template 라인)"),
    8: (0.6, "문의 우선순위 평가로 명확 - 고객지원 실무 (Evaluation 라인)"),
    9: (0.6, "헤드헌터 확인 설문으로 명확"),
    19: (0.6, "연습 진도 차트 관리로 명확 (Chart 라인)"),
    20: (0.6, "리사이탈 리마인더 관리로 명확 (Notification·Alert 라인)"),
    24: (0.6, "코드 추정기로 명확 - 실재 도구"),
    25: (0.6, "템포 진단 도구로 명확 (Diagnostic 라인)"),
    27: (0.6, "합주단 온보딩 관리로 명확 (Onboarding 라인)"),
    30: (0.6, "수취인 검증 평가로 명확 - 금융 실무 (Evaluation 라인)"),
    31: (0.6, "탱커 확인 설문으로 명확"),
    34: (0.6, "상판 시공 요건 관리로 명확"),
    44: (0.6, "합주 배치 지도 관리로 명확 (Map 라인)"),
    48: (0.6, "비트 제작 포털 관리로 명확 - 구체 서비스 지시 (Portal 라인)"),
    55: (0.6, "바이올린 수강료 관리로 명확 (Fee 라인)"),
    56: (0.6, "드럼 운주 다이어그램 관리로 명확 (Diagram 라인)"),
    59: (0.6, "농약 확인 설문으로 명확"),
    61: (0.6, "기록물 요건 관리로 명확"),
    65: (0.6, "첼로 연습 노트 관리로 명확 (Note 라인)"),
    70: (0.6, "환자 분류(triage) 평가로 명확 - 의료 실무 (Evaluation 라인)"),
    71: (0.6, "배당 확인 설문으로 명확"),
    76: (0.6, "비계 작업 안전 위험 관리로 명확 - 추락 위험 실존"),
    85: (0.6, "타액 연주 가이드 관리로 명확 (Guide 라인)"),
    86: (0.6, "만돌린 연습 영상 관리로 명확 (Video 라인)"),
    88: (0.6, "헤드라인 품질 평가로 명확 - 미디어 실무 (Evaluation 라인)"),
    89: (0.6, "우선순위 확인 설문으로 명확"),
    101: (0.6, "오디션 응시료 관리로 명확 (Fee 라인)"),
    104: (0.6, "코드 검사기로 명확 - 실재 도구"),
    107: (0.6, "합주단 출석 체크 관리로 명확 (Checkin 라인)"),
    110: (0.6, "운동 처방·수행 평가로 명확 - 건강 실무 (Evaluation 라인)"),
    111: (0.6, "수취인 확인 설문으로 명확"),
    114: (0.6, "계약자 가입 요건 관리로 명확"),
    130: (0.6, "배포 결과 평가로 명확 - DevOps 실무 (Evaluation 라인)"),
    137: (0.6, "드럼 구조 도식 관리로 명확 (Schematic 라인)"),
    140: (0.6, "교육 코호트(기수) 평가로 명확 - 교육 실무 (Evaluation 라인)"),
    146: (0.6, "플루트 수강 포털 관리로 명확 - 구체 서비스 지시 (Portal 라인)"),
    150: (0.6, "클라리넷 레슨 예약금 관리로 명확 (Deposit 라인)"),
    151: (0.6, "베이스 연주 실력 평가로 명확 (Evaluation 라인)"),
    152: (0.6, "분류(triage) 확인 설문으로 명확"),
    155: (0.6, "택배 요건 관리로 명확"),
    163: (0.6, "오보에 수강료 관리로 명확 (Fee 라인)"),
    165: (0.6, "트롬본 연습 공지 관리로 명확 (Announcement 라인)"),
    166: (0.6, "타액 연습 평점 관리로 명확 (Rating 라인)"),
    167: (0.6, "만돌린 연습 일지 관리로 명확 (Diary 라인)"),
    169: (0.6, "회의 운영 평가로 명확 - 공공 실무 (Evaluation 라인)"),
    170: (0.6, "헤드라인 확인 설문으로 명확"),
    173: (0.6, "굿즈 요건 관리로 명확"),
    181: (0.6, "리사이탈 티켓 판매 관리로 명확 (Ticket 라인)"),
    185: (0.6, "코드 감지기로 명확 - 실재 도구"),
    191: (0.6, "운동 확인 설문으로 명확"),
    194: (0.6, "증서 거래 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "하프 프로필 결합은 Profile 불성립",
    2: "오보에 회고 결합은 Recap 불성립",
    3: "비올라 일련번호 결합은 Serial 불성립",
    4: "트롬본 위젯 결합은 Widget 불성립",
    6: "만돌린 조리법 결합은 Recipe 불성립",
    7: "아코디언 사용률 결합은 Usage 불성립",
    10: "굿즈 활용률 결합 불성립 - Utilization",
    11: "진드기 요건 결합은 요건 대상 불성립",
    12: "어금니 감가상각 결합 불성립",
    13: "장난감 사직 결합은 Resignation 불성립",
    14: "제품에 위험 결합 불성립",
    15: "투약에 보증인 결합 불성립",
    16: "점화 장치에 튜너 결합 불성립",
    17: "하모니카 연쇄 결합은 Cascade 추상 불성립",
    18: "레슨 반지 결합은 Ring 불성립",
    21: "오디션 항목·입장 결합은 Entry 다의어 불명확",
    22: "조율 링크 결합은 Link 불성립",
    23: "이론 체험·재판 결합은 Trial 다의어 불명확",
    26: "레퍼토리 견적 결합은 불성립",
    28: "반주자 빈도 결합은 Frequency 속성어 불성립",
    29: "메트로놈 승인 결합은 불성립",
    32: "증서 활용률 결합 불성립 - Utilization",
    33: "계약자 혜택 결합은 Benefit 추상 불명확",
    35: "분유 감가상각 결합 불성립",
    36: "메일룸 사직 결합은 Resignation 불성립",
    37: "곡집에 위험 결합 불성립",
    38: "스트레칭에 보증인 결합 불성립",
    39: "파산에 튜너 결합 불성립",
    40: "교법 레이더 결합은 Radar 추상 불성립",
    41: "캠프 연쇄 결합은 Cascade 추상 불성립",
    42: "합창 루프 결합은 Loop 추상 불성립",
    43: "퇴직 파도 결합은 Wave 추상 불성립",
    45: "유산 베이스 결합은 Base 추상 불성립",
    46: "멜로디 게시판 결합은 Board 다의어 불명확",
    47: "리듬 역 결합은 Station 불성립",
    49: "피치 경로 결합은 Route 불성립",
    50: "등록 활용률 결합 불성립 - Utilization",
    51: "환자 사직 결합은 Resignation 불성립",
    52: "등록에 보증인 결합 불성립",
    53: "피아노 틀 결합은 Frame 불성립",
    54: "기타 티커 결합은 Ticker 불성립",
    57: "보컬 핑 결합은 Ping 불성립",
    58: "우쿨렐레 용량 결합은 Capacity 속성어 불성립",
    60: "변전소 활용률 결합 불성립 - Utilization",
    62: "참여 감가상각 결합 불성립",
    63: "방송 사직 결합은 Resignation 불성립",
    64: "플루트 구역 결합은 Zone 불성립",
    66: "색소폰 기금 결합은 Fund 불성립",
    67: "트럼펫 위젯 결합은 Widget 불성립",
    68: "클라리넷 보증 결합은 Warranty 불성립",
    69: "베이스 매트릭스 결합은 Matrix 추상 불성립",
    72: "패러리걸 활용률 결합 불성립 - Utilization",
    73: "택배 혜택 결합은 Benefit 추상 불명확",
    74: "연금 감가상각 결합 불성립",
    75: "초과근무 사직 결합은 Resignation 불성립",
    77: "바코드에 보증인 결합 불성립",
    78: "발렛에 튜너 결합 불성립",
    79: "오르간 반지 결합은 Ring 불성립",
    80: "검인 지도 결합은 Atlas 추상 불성립",
    81: "하프 상태 결합은 Status 불성립",
    82: "오보에 항목·입장 결합은 Entry 다의어 불명확",
    83: "비올라 토큰 결합은 Token 불성립",
    84: "트롬본 저장소 결합은 Repository 기술용어 불명확",
    87: "아코디언 상태·조건 결합은 Condition 다의어 불명확",
    90: "헤드헌터 활용률 결합 불성립 - Utilization",
    91: "굿즈 혜택 결합은 Benefit 추상 불명확",
    92: "진드기 감가상각 결합 불성립",
    93: "어금니 사직 결합은 Resignation 불성립",
    94: "장난감에 위험 결합 불성립",
    95: "제품에 보증인 결합 불성립",
    96: "투약에 튜너 결합 불성립",
    97: "하모니카 브리지 결합은 Bridge 기각 라인",
    98: "레슨 관문 결합은 Gate 불성립",
    99: "연습 통 결합은 Bin 불성립",
    100: "리사이탈 색인 결합은 Index 불성립",
    102: "조율 규칙 결합은 Rule 불성립",
    103: "이론 그래프 결합은 Graph 불성립",
    105: "템포 진도 결합은 대상 불성립",
    106: "레퍼토리 보증 결합은 Warranty 불성립",
    108: "반주자 호환성 결합은 Compatibility 불성립",
    109: "메트로놈 매트릭스 결합은 Matrix 추상 불성립",
    112: "탱커 활용률 결합 불성립 - Utilization",
    113: "증서 혜택 결합은 Benefit 추상 불명확",
    115: "상판 감가상각 결합 불성립",
    116: "분유 사직 결합은 Resignation 불성립",
    117: "메일룸에 위험 결합 불성립",
    118: "곡집에 보증인 결합 불성립",
    119: "스트레칭에 튜너 결합 불성립",
    120: "교법 릴레이 결합은 Relay 불성립",
    121: "캠프 브리지 결합은 Bridge 기각 라인",
    122: "합창 격자 결합은 Grid 추상 불성립",
    123: "퇴직 경로 결합은 Path 추상 불성립",
    124: "오케스트라 틀 결합은 Frame 불성립",
    125: "유산 코어 결합은 Core 불성립",
    126: "멜로디 데크 결합은 Deck 불성립",
    127: "리듬 터미널 결합은 Terminal 불성립",
    128: "비트 콘솔 결합은 Console 도구형 불성립",
    129: "피치 궤도 결합은 Rail 불성립",
    131: "등록 혜택 결합은 Benefit 추상 불명확",
    132: "환자에 위험 결합 불성립",
    133: "등록에 튜너 결합 불성립",
    134: "피아노 베이스 결합은 Base 추상 불성립",
    135: "기타 라인 결합은 Line 추상 불명확",
    136: "바이올린 항목 결합은 Item 다의어 불명확",
    138: "보컬 모델 결합은 Model 속성어·다의어 불명확",
    139: "우쿨렐레 사용률 결합은 Usage 불성립",
    141: "농약 활용률 결합 불성립 - Utilization",
    142: "변전소 혜택 결합은 Benefit 추상 불명확",
    143: "기록물 감가상각 결합 불성립",
    144: "참여 사직 결합은 Resignation 불성립",
    145: "방송에 위험 결합 불성립",
    147: "첼로 태그 결합은 Tag 불성립",
    148: "색소폰 현금 결합은 Cash 불성립",
    149: "트럼펫 저장소 결합은 Repository 기술용어 불명확",
    153: "배당 활용률 결합 불성립 - Utilization",
    154: "패러리걸 혜택 결합은 Benefit 추상 불명확",
    156: "연금 사직 결합은 Resignation 불성립",
    157: "초과근무에 위험 결합 불성립",
    158: "비계에 보증인 결합 불성립",
    159: "바코드에 튜너 결합 불성립",
    160: "오르간 관문 결합은 Gate 불성립",
    161: "검인 관리인 결합은 Keeper 불성립",
    162: "하프 뷰 결합은 View 불성립",
    164: "비올라 서명 결합은 Signature 다의어 불명확",
    168: "아코디언 습도 결합은 Humidity 불성립",
    171: "우선순위 활용률 결합 불성립 - Utilization",
    172: "헤드헌터 혜택 결합은 Benefit 추상 불명확",
    174: "진드기 사직 결합은 Resignation 불성립",
    175: "어금니에 위험 결합 불성립",
    176: "장난감에 보증인 결합 불성립",
    177: "제품에 튜너 결합 불성립",
    178: "하모니카 신호 결합은 Signal 불성립",
    179: "레슨 연결점 결합은 Nexus 추상 불성립",
    180: "연습 여권 결합은 Passport 기각 라인",
    182: "오디션 항목 결합은 Item 다의어 불명확",
    183: "조율 세부 결합은 Detail 속성어 불성립",
    184: "이론 라벨 결합은 Label 불성립",
    186: "템포 승인 결합은 불성립",
    187: "레퍼토리 예약금 결합은 불성립",
    188: "합주 규모 결합은 Size 속성어 불성립",
    189: "반주자 용량 결합은 Capacity 속성어 불성립",
    190: "메트로놈 평가 결합은 대상 불성립",
    192: "수취인 활용률 결합 불성립 - Utilization",
    193: "탱커 혜택 결합은 Benefit 추상 불명확",
    195: "계약자 감가상각 결합 불성립",
    196: "상판 사직 결합은 Resignation 불성립",
    197: "분유에 위험 결합 불성립",
    198: "메일룸에 보증인 결합 불성립",
    199: "곡집에 튜너 결합 불성립",
    200: "교법 금고 결합은 Vault 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 50, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 150, len(REJECT_REASON)
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
