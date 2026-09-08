import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk17_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk17_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    8: (0.6, "교육 안내 전단으로 실재 (Flyer 라인)"),
    22: (0.6, "주문 키오스크로 실재 (Kiosk 실물 단말)"),
    61: (0.6, "컨시어지 업무 교육으로 실재 (Tutorial 라인)"),
    62: (0.6, "채점 핸드북으로 실재 (Handbook 라인)"),
    68: (0.6, "운전 교육 안내 전단으로 실재 (Flyer 라인)"),
    77: (0.6, "퇴직 절차 교육으로 실재 (Tutorial 라인)"),
    78: (0.6, "도장 시공 핸드북으로 실재 (Handbook 라인)"),
    88: (0.6, "비스트로 부스석으로 실재 (Booth 실물 공간)"),
    95: (0.6, "제과 레시피 영상으로 실재 (Video 콘텐츠)"),
    98: (0.6, "스타일링 튜토리얼로 실재 (Tutorial 라인)"),
    99: (0.6, "대체약 핸드북으로 실재 (Handbook 라인)"),
    118: (0.6, "펍 이벤트 캘린더로 성립 (Calendar 라인)"),
    136: (0.6, "교정 치료 견적으로 성립 (Estimate 견적)"),
    137: (0.6, "해양 레저 이용 명세서로 성립 (Bill 실물 청구)"),
    145: (0.6, "화산 투어 예약 확정서로 성립 (Confirmation 라인)"),
    160: (0.6, "공급업체 관리 교육으로 실재 (Tutorial 라인)"),
    161: (0.6, "컨시어지 핸드북으로 실재 (Handbook 라인)"),
    168: (0.7, "건설 유치권 절차 교육으로 실재 (도메인 실무 개념)"),
    176: (0.6, "보험 배상 절차 교육으로 실재 (도메인 실무 개념)"),
    177: (0.6, "퇴직 핸드북으로 실재 (Handbook 라인)"),
    185: (0.6, "차량 점검 안내 전단으로 실재 (Flyer 라인)"),
    188: (0.6, "비스트로 주문 키오스크로 실재 (Kiosk 실물 단말)"),
    198: (0.6, "자장가 가창 교육으로 실재 (Tutorial 라인)"),
    199: (0.6, "스타일 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "카지노 일정표 결합 불명확",
    2: "합주 소견 결합 불명확",
    3: "부상 권고 결합 불명확",
    4: "채권자 세미나 결합 불명확",
    5: "냉장 컨테이너 선물 결합 불성립 - Gift",
    6: "리모델링 리트리트 결합 불성립",
    7: "보험 조정 토너먼트 결합 불성립",
    9: "에스프레소 나침반 결합은 Compass 추상 불성립",
    10: "라떼 장부 결합은 Ledger 불성립",
    11: "칫솔 갑판 결합은 Deck 불성립",
    12: "스노클링 기지 결합은 Station 불성립",
    13: "칵테일 경로 결합은 Route 불성립",
    14: "치약 레일 결합은 Rail 불성립",
    15: "카약 고리 결합은 Ring 불성립",
    16: "바리스타 엔진 결합은 Engine 추상 불성립",
    17: "구강청격 보조원 결합은 Assistant 불성립",
    18: "폭포 감시자 결합은 Monitor 불성립",
    19: "펍 등록부 결합 불성립",
    20: "마우스가드 캘린더 결합 불성립",
    21: "일몰 탐색기 결합은 Locator 불성립",
    23: "스마일 만 결합은 Bay 불성립",
    24: "수변 항구 결합은 Harbor 불성립",
    25: "스시 여권 결합은 Passport 다의어 불성립",
    26: "호흡 로비 결합은 Lobby 불성립",
    27: "보드워크 라인 결합은 Line 다의어 불성립",
    28: "타코 서식 결합은 Form 다의어 불성립",
    29: "코골이 카드 결합은 Card 다의어 불성립",
    30: "해변 점검 결합 불성립",
    31: "면집 프로필 결합 불성립",
    32: "교합 상태 결합은 Status 불성립",
    33: "전망 역사 결합 불명확",
    34: "해산물 갱신 결합은 Update 불성립",
    35: "치과 피드 결합은 Feed 추상 불성립",
    36: "배낭여행 요약 결합 불성립",
    37: "교정의 티켓 결합 불명확",
    38: "패러세일링 주문 결합은 Order 다의어 불성립",
    39: "치위 목록 결합 불명확",
    40: "야생동물 전표 결합은 Slip 다의어 불성립",
    41: "치실 통행 결합은 Pass 다의어 불성립",
    42: "라군 배지 결합은 Badge 불성립",
    43: "치석 메모 결합은 Memo 다의어 불성립",
    44: "빙하 탭 결합은 Tab 불성립",
    45: "불소 회람 결합은 Circular 다의어 불성립",
    46: "화산 청원 결합은 Petition 불성립",
    47: "실런트 항목 결합은 Entry 다의어 불성립",
    48: "당일여행 품목 결합은 Item 다의어 불성립",
    49: "치은염 비용 속성 결합은 Cost 불성립",
    50: "요트 운임 속성 결합은 Fare 불성립",
    51: "이갈이 합계 결합은 Sum 불성립",
    52: "산책로 기금 결합은 Fund 불성립",
    53: "구취 청구 결합은 Charge 다의어 불성립",
    54: "우릴 수당 결합은 Allowance 불성립",
    55: "치주염 지분 결합은 Stake 불성립",
    56: "사막 벌금 결합은 Fine 불성립",
    57: "부정교합 버전 결합은 Version 불성립",
    58: "와이너리 규칙 결합은 Rule 불성립",
    59: "치수과 식별자 결합은 Identifier 불성립",
    60: "치주과 분야 결합은 Field 불성립",
    63: "토양 소견 결합 불명확",
    64: "약정 세미나 결합은 Pledge 다의어 불명확",
    65: "공청회 선물 결합 불성립 - Gift",
    66: "소재 리트리트 결합 불성립",
    67: "아카이브 토너먼트 결합 불성립",
    69: "번들 튜토리얼 결합 불명확",
    70: "동문 일정표 결합 불명확",
    71: "처리량 소견 결합은 Throughput 속성어 불성립",
    72: "사일로 권고 결합 불명확",
    73: "장부 선물 결합 불성립 - Gift",
    74: "투표 리트리트 결합 불성립",
    75: "배치 토너먼트 결합 불성립",
    76: "피드 전단 결합은 Feed 추상 불성립",
    79: "선수과목 일정표 결합 불명확",
    80: "예산 소견 결합 불명확",
    81: "캡션 권고 결합 불명확",
    82: "감정 분석 세미나 결합 불명확",
    83: "리크루터 선물 결합 불성립 - Gift",
    84: "랜야드 리트리트 결합 불성립",
    85: "점검 토너먼트 결합 불성립",
    86: "카페 전단 결합 불명확",
    87: "다이너 구역 결합은 Zone 불성립",
    89: "피자집 피드 결합은 Feed 추상 불성립",
    90: "데리 정리 결합은 Recap 다의어 불성립",
    91: "디저트 분류 결합은 Category 불성립",
    92: "포장 스케치 결합은 Sketch 불성립",
    93: "브런치 트렌드 결합은 Trend 불성립",
    94: "베이커리 핑 결합 불성립",
    96: "베이글 적재 결합은 Load 불성립",
    97: "도넛 사임 결합 불성립",
    100: "놀이터 일정표 결합 불명확",
    101: "카지노 소견 결합 불명확",
    102: "합주 권고 결합 불명확",
    103: "부상 세미나 결합 불명확",
    104: "채권자 선물 결합 불성립 - Gift",
    105: "냉장 컨테이너 리트리트 결합 불성립",
    106: "리모델링 토너먼트 결합 불성립",
    107: "보험 조정 전단 결합 불명확",
    108: "에스프레소 등대 결합은 Beacon 불성립",
    109: "라떼 게시판 결합은 Board 다의어 불성립",
    110: "칫솔 스튜디오 결합 불명확",
    111: "스노클링 터미널 결합은 Terminal 불성립",
    112: "칵테일 레일 결합은 Rail 불성립",
    113: "치약 오솔길 결합은 Trail 불성립",
    114: "카약 문 결합은 Gate 불성립",
    115: "바리스타 보조원 결합은 Assistant 불성립",
    116: "구강청격 플래너 결합은 Planner 불성립",
    117: "폭포 동반자 결합은 Companion 불성립",
    119: "마우스가드 디렉터리 결합 불성립",
    120: "일몰 탐색기 결합은 Finder 불성립",
    121: "스테이크하우스 만 결합은 Bay 불성립",
    122: "스마일 게시 결합은 Post 다의어 불성립",
    123: "수변 명단 결합은 Roster 불성립",
    124: "스시 로비 결합은 Lobby 불성립",
    125: "호흡 전광판 결합은 Ticker 불성립",
    126: "보드워크 창 결합은 Window 불성립",
    127: "타코 카드 결합은 Card 다의어 불성립",
    128: "코골이 시트 결합은 Sheet 다의어 불성립",
    129: "해변 점수 결합은 Score 불성립",
    130: "면집 상태 결합은 Status 불성립",
    131: "교합 뷰 결합은 View 추상 불성립",
    132: "전망 파일 결합은 File 불성립",
    133: "해산물 피드 결합은 Feed 추상 불성립",
    134: "치과 초안 결합은 Draft 다의어 불성립",
    135: "배낭여행 타임라인 결합 불성립",
    138: "치위 표 결합은 Table 다의어 불성립",
    139: "야생동물 샘플 결합은 Sample 다의어 불성립",
    140: "치실 바우처 결합 불명확",
    141: "라군 전표 결합은 Stub 불성립",
    142: "치석 한도 결합은 Quota 속성어 불성립",
    143: "빙하 회람 결합은 Bulletin 다의어 불성립",
    144: "불소 권고 결합은 Advisory 불성립",
    146: "실런트 요금 결합은 Fee 불성립",
    147: "당일여행 단위 결합은 Unit 다의어 불성립",
    148: "치은염 가격 속성 결합은 Price 불성립",
    149: "요트 세금 결합은 Tax 불성립",
    150: "이갈이 부채 결합은 Debt 불성립",
    151: "산책로 현금 결합은 Cash 불성립",
    152: "구취 의무 결합은 Duty 불성립",
    153: "우릴 관세 결합은 Tariff 불성립",
    154: "치주염 마진 속성 결합은 Margin 불성립",
    155: "사막 번호 속성 결합은 Number 불성립",
    156: "부정교합 링크 결합은 Link 불성립",
    157: "와이너리 세부 결합은 Detail 불성립",
    158: "치수과 분류 결합은 Category 불성립",
    159: "치주과 형식 결합은 Format 불성립",
    162: "채점 일정표 결합 불명확",
    163: "토양 권고 결합 불명확",
    164: "약정 선물 결합 불성립 - Gift",
    165: "공청회 리트리트 결합 불성립",
    166: "소재 토너먼트 결합 불성립",
    167: "아카이브 전단 결합 불명확",
    169: "번들 핸드북 결합 불명확",
    170: "동문 소견 결합 불명확",
    171: "처리량 권고 결합은 Throughput 속성어 불성립",
    172: "사일로 세미나 결합 불명확",
    173: "장부 리트리트 결합 불성립",
    174: "투표 토너먼트 결합 불성립",
    175: "배치 전단 결합 불명확",
    178: "도장 일정표 결합 불명확",
    179: "선수과목 소견 결합 불명확",
    180: "예산 권고 결합 불명확",
    181: "캡션 세미나 결합 불명확",
    182: "감정 분석 선물 결합 불성립 - Gift",
    183: "리크루터 리트리트 결합 불성립",
    184: "랜야드 토너먼트 결합 불성립",
    186: "카페 추적기 결합은 Tracker 불성립",
    187: "다이너 포털 결합은 Portal 불성립",
    189: "피자집 초안 결합은 Draft 다의어 불성립",
    190: "데리 항목 결합은 Entry 다의어 불성립",
    191: "디저트 속성 결합은 Attribute 불성립",
    192: "포장 개요 결합은 Outline 불성립",
    193: "브런치 비교 결합은 Comparison 불성립",
    194: "베이커리 모델 결합은 Model 다의어 불성립",
    195: "제과 일지 결합 불명확",
    196: "베이글 전압 속성 결합은 Voltage 불성립",
    197: "도넛 위험 결합은 Hazard 불성립",
    200: "대체약 일정표 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 24, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 176, len(REJECT_REASON)
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
