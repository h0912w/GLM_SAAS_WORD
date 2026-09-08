import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk21_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk21_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "하프 출연 목록 관리로 명확 (List 라인)"),
    5: (0.6, "비올라 연주 매뉴얼 관리로 명확 (Manual 라인)"),
    7: (0.6, "타액 레슨 견적 관리로 명확 (Quote 라인)"),
    9: (0.6, "번역 구문 품질 평가로 명확 - 통번역 실무 (Evaluation 라인)"),
    11: (0.6, "제설 기준 요건 관리로 명확 (Requirement 라인)"),
    19: (0.6, "연습 이력 관리로 명확 (History 라인)"),
    23: (0.6, "음악이론 변환기로 실재 도구 (Converter 라인)"),
    28: (0.6, "치과 교정 진행 평가로 명확 - 치과 실무 (Evaluation 라인)"),
    29: (0.6, "유모차 확인 설문으로 명확"),
    31: (0.6, "연석 시공 요건 관리로 명확 (Requirement 라인)"),
    47: (0.6, "리듬 연습 플래너로 명확 (Planner 라인)"),
    48: (0.6, "비트 연습 대장 관리로 명확 (Register 라인)"),
    49: (0.6, "피치 기록 등록부 관리로 명확 (Registry 라인)"),
    50: (0.6, "화물 확인 설문으로 명확"),
    54: (0.6, "기타 연습 소식·갱신 관리로 명확 (Update 라인)"),
    58: (0.6, "갤러리 확인 설문으로 명확"),
    60: (0.6, "라이너 교체 요건 관리로 명확 (Requirement 라인)"),
    66: (0.6, "첼로 영수증 관리로 명확 (Receipt 라인)"),
    69: (0.6, "클라리넷 레슨 온보딩 관리로 명확 (Onboarding 라인)"),
    70: (0.6, "수선 확인 설문으로 명확"),
    74: (0.6, "광미 저장시설 위험 관리로 명확 - 댐 붕괴 위험 실존 (Evaluation 근거)"),
    82: (0.6, "비올라 연습 워크시트 관리로 명확 (Worksheet 라인)"),
    86: (0.6, "자물쇠 홈(mortise) 가공 평가로 명확 - 자물쇠 실무 (Evaluation 라인)"),
    87: (0.6, "구문 확인 설문으로 명확"),
    88: (0.6, "케이크 준비 요건 관리로 명확 (Requirement 라인)"),
    94: (0.6, "아코디언 연습 추적 관리로 명확 (Tracker 라인)"),
    96: (0.6, "레슨 사무 관리로 명확 (Office 라인)"),
    104: (0.6, "레퍼토리 습득 온보딩 관리로 명확 (Onboarding 라인)"),
    106: (0.6, "반려동물 식이 평가로 명확 - 수의 실무 (Evaluation 라인)"),
    107: (0.6, "교정 확인 설문으로 명확"),
    125: (0.6, "리듬 연습 스케줄러로 명확 (Scheduler 라인)"),
    127: (0.6, "피치 연습 캘린더로 명확 (Calendar 라인)"),
    129: (0.6, "정책 기준 요건 관리로 명확 (Requirement 라인)"),
    133: (0.6, "드럼 연습 타이머로 실재 도구 (Timer 라인)"),
    135: (0.6, "번역 용어 품질 평가로 명확 - 통번역 실무 (Evaluation 라인)"),
    143: (0.6, "플루트 출석 대장 관리로 명확 (Register 라인)"),
    147: (0.6, "클라리넷 출석 체크인으로 명확 (Checkin 라인)"),
    155: (0.6, "오르간 사무 관리로 명확 (Office 라인)"),
    159: (0.6, "비올라 운주법 도식 관리로 명확 (Diagram 라인)"),
    160: (0.6, "트롬본 연습 기록 관리로 명확 (Record 라인)"),
    161: (0.6, "타액 레슨 예약금 관리로 명확 (Deposit 라인)"),
    163: (0.6, "제습기 성능 평가로 명확 - HVAC 실무 (Evaluation 라인)"),
    164: (0.6, "자물쇠 홈 확인 설문으로 명확"),
    175: (0.6, "리사이탈 브리핑 관리로 명확 (Summary 준용 라인)"),
    181: (0.6, "레퍼토리 습득 체크인으로 명확 (Checkin 라인)"),
    183: (0.6, "식이 확인 설문으로 명확"),
    186: (0.6, "스파 서비스 요건 관리로 명확 (Requirement 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "오르간 장소 검색 결합은 Locator 불성립",
    2: "검인 카운터 결합은 Probate 도구형·Counter 다의어 불성립",
    4: "오보에 가치 결합은 Value 속성어 불성립",
    6: "트롬본 제안 결합은 Proposal 불명확",
    8: "만돌린 깊이 결합은 Depth 속성어 불성립",
    10: "케이크 혜택 결합은 Benefit 추상 불명확",
    12: "마감 감가상각 결합 불성립",
    13: "스펀지 사직 결합은 Resignation 불성립",
    14: "배수 트랩에 위험 결합 불성립",
    15: "로드트립에 보증인 결합 불성립",
    16: "아코디언 튜너 결합은 악기 튜너로 오독, 서비스 불성립",
    17: "하모니카 터미널 결합은 Terminal 불성립",
    18: "레슨 검색기 결합은 Finder 불성립",
    20: "리사이탈 탭 결합은 Tab 불성립",
    21: "오디션 지분 결합은 Stake 불성립",
    22: "조율 선급금 결합은 Advance 기각 라인",
    24: "코드 마감 결합은 불성립",
    25: "템피 피드백 결합은 불성립",
    26: "레퍼토리 청구 결합은 Claim 다의어 불명확",
    27: "합주 밝기 결합은 Brightness 불성립",
    30: "스파 활용률 결합 불성립 - Utilization",
    32: "포도원 감가상각 결합 불성립",
    33: "반주자 사직 결합은 Resignation 불성립",
    34: "질병에 위험 결합 불성립",
    35: "채무자에 보증인 결합 불성립",
    36: "평상형 트럭에 튜너 결합 불성립",
    37: "메트로놈 등대 결합은 Beacon 추상 불성립",
    38: "증서 신호 결합은 Signal 추상 불성립",
    39: "곡집 파도 결합은 Wave 추상 불성립",
    40: "교법 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    41: "캠프 터미널 결합은 Terminal 불성립",
    42: "합창 패널 결합은 Panel 불성립",
    43: "퇴직 경로 결합은 Route 불성립",
    44: "오케스트라 체인 결합은 Chain 추상 불성립",
    45: "유산 관문 결합은 Gate 불성립",
    46: "멜로디 관리자 결합은 Keeper 불명확 기각 라인",
    51: "정책 혜택 결합은 Benefit 추상 불명확",
    52: "생산에 튜너 결합 불성립",
    53: "피아노 링 결합은 Ring 불성립",
    55: "바이올린 마진 결합은 Margin 기각 라인",
    56: "드럼 탐지기 결합은 불성립",
    57: "보컬 예측기 결합은 Predictor 불성립",
    59: "꽃집 활용률 결합 불성립 - Utilization",
    61: "코팅 감가상각 결합 불성립",
    62: "변기 사직 결합은 Resignation 불성립",
    63: "휴가에 위험 결합 불성립",
    64: "우쿨렐레에 보증인 결합 불성립",
    65: "플루트 동반자 결합은 Companion 불명확 기각 라인",
    67: "색소폰 형식 결합은 Format 불성립",
    68: "트럼펫 제안 결합은 Proposal 불명확",
    71: "추모식 활용률 결합 불성립 - Utilization",
    72: "항구 감가상각 결합 불성립",
    73: "운행 기록부 사직 결합은 Resignation 불성립",
    75: "코일에 보증인 결합 불성립",
    76: "키패드에 튜너 결합 불성립",
    77: "베이스 대장간 결합은 Forge 불성립",
    78: "오르간 검색기 결합은 Finder 불성립",
    79: "검인 부스 결합은 Probate 도구형 기각 라인",
    80: "하프 표 결합은 Table 다의어 불명확",
    81: "오보에 지분 결합은 Stake 불성립",
    83: "트롬본 보증 결합은 Guarantee 불성립",
    84: "타액 보증 결합은 Warranty 불성립",
    85: "만돌린 높이 결합은 Height 속성어 불성립",
    89: "제설 감가상각 결합 불성립",
    90: "마감 사직 결합은 Resignation 불성립",
    91: "스펀지에 위험 결합 불성립",
    92: "트랩에 보증인 결합 불성립",
    93: "로드트립에 튜너 결합 불성립",
    95: "하모니카 센터 결합은 Center 불성립",
    97: "연습 파일 결합은 File 다의어 불명확",
    98: "리사이탈 게시판 결합은 Bulletin 불명확",
    99: "오디션 마진 결합은 Margin 기각 라인",
    100: "조율 과태료 결합은 Penalty 기각 라인",
    101: "이론 생성기 결합은 불성립",
    102: "코드 지속시간 결합은 Duration 불성립",
    103: "템포 청구서 결합은 불성립",
    105: "합주 주파수 결합은 Frequency 불성립",
    108: "유모차 활용률 결합 불성립 - Utilization",
    109: "스파 혜택 결합은 Benefit 추상 불명확",
    110: "연석 감가상각 결합 불성립",
    111: "포도원 사직 결합은 Resignation 불성립",
    112: "반주자에 위험 결합 불성립",
    113: "질병에 보증인 결합 불성립",
    114: "채무자에 튜너 결합 불성립",
    115: "메트로놈 대장간 결합은 Forge 불성립",
    116: "증서 감시 결합은 Watch 불성립",
    117: "곡집 경로 결합은 Path 추상 불성립",
    118: "교법 게시판 결합은 Board 다의어 불명확",
    119: "캠프 센터 결합은 Center 불성립",
    120: "합창 저울 결합은 Scale 다의어 불명확",
    121: "퇴직 궤도 결합은 Rail 불성립",
    122: "오케스트라 링 결합은 Ring 불성립",
    123: "유산 연결점 결합은 Nexus 추상 불성립",
    124: "멜로디 관리자 결합은 Manager 불성립",
    126: "비트 운영 결합은 Ops 불명확",
    128: "화물 활용률 결합 불성립 - Utilization",
    130: "피아노 관문 결합은 Gate 불성립",
    131: "기타 피드 결합은 Feed 불성립",
    132: "바이올린 벌금·미세 결합은 Fine 다의어 불명확",
    134: "보컬 인장 결합은 Seal 불성립",
    136: "갤러리 활용률 결합 불성립 - Utilization",
    137: "꽃집 혜택 결합은 Benefit 추상 불명확",
    138: "라이너 감가상각 결합 불성립",
    139: "코팅 사직 결합은 Resignation 불성립",
    140: "변기에 위험 결합 불성립",
    141: "휴가에 보증인 결합 불성립",
    142: "우쿨렐레 튜너 결합은 악기 튜너로 오독, 서비스 불성립",
    144: "첼로 코드 결합은 Code 다의어 불명확",
    145: "색소폰 일련번호 결합은 Serial 불성립",
    146: "트럼펫 보증 결합은 Guarantee 불성립",
    148: "수선 활용률 결합 불성립 - Utilization",
    149: "추모식 혜택 결합은 Benefit 추상 불명확",
    150: "항구 사직 결합은 Resignation 불성립",
    151: "운행 기록부에 위험 결합 불성립",
    152: "광미에 보증인 결합 불성립",
    153: "코일에 튜너 결합 불성립",
    154: "베이스 연쇄 결합은 Cascade 추상 불성립",
    156: "검인 키오스크 결합은 Probate 도구형 기각 라인",
    157: "하프 전표 결합은 Slip 불명확",
    158: "오보에 마진 결합은 Margin 기각 라인",
    162: "만돌린 폭 결합은 Width 속성어 불성립",
    165: "구문 활용률 결합 불성립 - Utilization",
    166: "케이크 감가상각 결합 불성립",
    167: "제설 사직 결합은 Resignation 불성립",
    168: "마감에 위험 결합 불성립",
    169: "스펀지에 보증인 결합 불성립",
    170: "트랩에 튜너 결합 불성립",
    171: "아코디언 흐름 결합은 Flow 불성립",
    172: "하모니카 존 결합은 Zone 불성립",
    173: "레슨 카운터 결합은 Counter 다의어 불명확",
    174: "연습 수준 결합은 Level 속성어 불성립",
    176: "오디션 벌금·미세 결합은 Fine 다의어 불명확",
    177: "조율 마크업 결합은 Markup 기각 라인",
    178: "이론 녹음기 결합은 불성립",
    179: "코드 음량 결합은 Volume 다의어 불명확",
    180: "템포 갱신 결합은 불성립",
    182: "합주 호환성 결합은 Compatibility 불성립",
    184: "교정 활용률 결합 불성립 - Utilization",
    185: "유모차 혜택 결합은 Benefit 추상 불명확",
    187: "연석 사직 결합은 Resignation 불성립",
    188: "포도원에 위험 결합 불성립",
    189: "반주자에 보증인 결합 불성립",
    190: "질병에 튜너 결합 불성립",
    191: "메트로놈 연쇄 결합은 Cascade 추상 불성립",
    192: "증서 범위 결합은 Scope 불성립",
    193: "곡집 포인트 결합은 Point 불성립",
    194: "교법 데크 결합은 Deck 불성립",
    195: "캠프 존 결합은 Zone 불성립",
    196: "합창 경로 결합은 Route 불성립",
    197: "퇴직 흔적 결합은 Trail 불성립",
    198: "오케스트라 관문 결합은 Gate 불성립",
    199: "유산 대성지도 결합은 Atlas 추상 불성립",
    200: "멜로디 엔진 결합은 Engine 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 47, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 153, len(REJECT_REASON)
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
