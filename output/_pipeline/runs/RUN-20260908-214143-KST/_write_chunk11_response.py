import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk10_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk10_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "스시집 디렉터리로 성립 (Directory 라인)"),
    9: (0.6, "해변 안전 알림 서비스로 성립 (Alert 라인)"),
    23: (0.6, "빙하 투어 영수증으로 성립 (Receipt 라인)"),
    26: (0.6, "실런트 시술 바우처로 성립 (Voucher 라인)"),
    31: (0.6, "산책 투어 예약 확정으로 성립 (Confirmation 라인)"),
    40: (0.6, "추천서 작성 교육으로 실재 (Tutorial 라인)"),
    41: (0.6, "안건 핸드북으로 실재 (Handbook 라인)"),
    48: (0.6, "약제 살포 안내 전단으로 실재 (Flyer 라인)"),
    49: (0.6, "콜백 실무 교육으로 실재 (Tutorial 라인)"),
    50: (0.6, "리퍼럴 핸드북으로 실재 (Handbook 라인)"),
    52: (0.6, "감정 소견서로 성립 (Opinion 라인)"),
    58: (0.6, "웰니스 안내 전단으로 실재 (Flyer 라인)"),
    60: (0.6, "블로우드라이 교육으로 실재 (Tutorial 라인)"),
    61: (0.6, "흡입기 핸드북으로 실재 (Handbook 라인)"),
    68: (0.6, "마감 서비스 전단으로 실재 (Flyer 라인)"),
    77: (0.6, "제과 견적으로 성립 (Quote 견적)"),
    80: (0.6, "기사 작성 교육으로 실재 (Tutorial 라인)"),
    81: (0.6, "적성 핸드북으로 실재 (Handbook 라인)"),
    83: (0.6, "정비 점검 소견서로 성립 (Opinion 라인)"),
    85: (0.6, "식이 세미나로 실재 (Seminar 라인)"),
    109: (0.6, "해변 안내 차트로 성립 (Chart 라인)"),
    121: (0.6, "라군 투어 입장권으로 성립 (Ticket 라인)"),
    122: (0.6, "스케일링 청구서로 성립 (Bill 라인)"),
    133: (0.6, "우릴 투어 계획으로 성립 (Plan 라인)"),
    140: (0.6, "환불 실무 교육으로 실재 (Tutorial 라인)"),
    141: (0.6, "추천서 핸드북으로 실재 (Handbook 라인)"),
    148: (0.6, "가족 서비스 전단으로 실재 (Flyer 라인)"),
    149: (0.6, "런북 작성 교육으로 실재 (Tutorial 라인)"),
    150: (0.6, "콜백 핸드북으로 실재 (Handbook 라인)"),
    154: (0.6, "프랜차이즈 창업 설명회로 실재 (Seminar 라인)"),
    158: (0.6, "발달 안내 전단으로 실재 (Flyer 라인)"),
    160: (0.6, "식기세척기 교육으로 실재 (Tutorial 라인)"),
    161: (0.6, "블로우 핸드북으로 실재 (Handbook 라인)"),
    165: (0.6, "문법 세미나로 실재 (Seminar 라인)"),
    172: (0.6, "데리 바우처로 성립 (Voucher 라인)"),
    176: (0.7, "베이커리 경영 진단으로 성립 (Diagnostic 도메인 실무)"),
    181: (0.6, "기사 핸드북으로 실재 (Handbook 라인)"),
    185: (0.6, "에스프레소 세미나로 실재 (Seminar 라인)"),
    189: (0.6, "스파 전단으로 실재 (Flyer 라인)"),
    198: (0.6, "폭포 트레일로 실재 (Trail 물리 코스)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "스테이크하우스 모니터 결합 불성립",
    2: "스마일 동반자 결합은 Companion 불명확",
    3: "수변 운영 결합은 Ops 불성립",
    5: "호흡 탐색기 결합은 Locator 불명확",
    6: "보드워크 사무실 결합 불성립",
    7: "타코 게시 결합은 Post 다의어 불성립",
    8: "코골이 항구 결합은 Harbor 불성립",
    10: "면집 로비 결합은 Lobby 불성립",
    11: "교합 전광판 결합은 Ticker 불성립",
    12: "전망 창 결합은 Window 다의어 불성립",
    13: "해산물 서식 결합은 Form 다의어 불성립",
    14: "치과 카드 결합은 Card 다의어 불성립",
    15: "배낭여행 점검 결합 불명확",
    16: "교정의 프로필 결합 불성립",
    17: "패러세일링 뷰 결합은 View 추상 불성립",
    18: "치위 요율 속성 결합은 Rate 불성립",
    19: "야생동물 피드 결합은 Feed 추상 불성립",
    20: "치실 타임라인 결합 불성립",
    21: "라군 색인 결합은 Index 다의어 불성립",
    22: "치석 주문 결합은 Order 다의어 불성립",
    24: "불소 표 결합은 Table 다의어 불성립",
    25: "화산 샘플 결합은 Sample 다의어 불성립",
    27: "당일여행 전표 결합은 Stub 불성립",
    28: "치은염 한도 결합은 Quota 속성어 불성립",
    29: "요트 회람 결합은 Bulletin 다의어 불성립",
    30: "이갈이 권고 결합은 Advisory 불성립",
    32: "구취 요금 결합은 Fee 불성립",
    33: "우릴 단위 결합은 Unit 다의어 불성립",
    34: "치주염 가격 속성 결합은 Price 불성립",
    35: "사막 세금 결합은 Tax 불성립",
    36: "부정교합 합계 결합은 Sum 다의어 불성립",
    37: "와이너리 기금 결합 불성립",
    38: "치수과 판매 결합은 Sale 다의어 불성립",
    39: "치주과 수당 결합 불성립",
    42: "할부 일정표 결합 불명확",
    43: "규정 소견 결합 불명확",
    44: "예약 추천 결합 불성립",
    45: "동의서 선물 결합 불성립 - Gift",
    46: "접종 리트리트 결합 불성립",
    47: "가족 토너먼트 결합 불성립",
    51: "피드백 일정표 결합 불명확",
    53: "프랜차이즈 추천 결합 불명확",
    54: "퇴원 세미나 결합 불명확",
    55: "X-ray 선물 결합 불성립 - Gift",
    56: "세션 리트리트 결합 불성립",
    57: "이정표 토너먼트 결합 불성립",
    59: "카페 감가상각 결합 불성립",
    62: "제습기 일정표 결합 불명확",
    63: "잠금 소견 결합 불명확",
    64: "문법 권고 결합 불명확",
    65: "엘리베이터 세미나 결합 불명확",
    66: "고객 선물 결합 불성립 - Gift",
    67: "케이크 리트리트 결합 불성립",
    69: "다이너 경로 결합 불성립",
    70: "비스트로 스케줄러 결합 불성립",
    71: "피자집 카드 결합은 Card 다의어 불성립",
    72: "데리 통행 결합은 Pass 다의어 불성립",
    73: "디저트 청구 결합은 Charge 다의어 불성립",
    74: "포장 체불 결합은 Arrears 불성립",
    75: "브런치 변환기 결합 불성립",
    76: "베이커리 부피 속성 결합은 Volume 불성립",
    78: "베이글 길이 속성 결합은 Length 불성립",
    79: "도넛 에피소드 결합 불성립",
    82: "네트워킹 일정표 결합 불명확",
    84: "에스프레소 추천 결합 불명확",
    86: "교정 선물 결합 불성립 - Gift",
    87: "유모차 리트리트 결합 불성립",
    88: "스파 토너먼트 결합 불성립",
    89: "라떼 다리 결합은 Bridge 추상 불성립",
    90: "칫솔 시계 결합은 Watch 다의어 불성립",
    91: "스노클링 격자 결합은 Grid 추상 불성립",
    92: "칵테일 장부 결합은 Ledger 불성립",
    93: "치약 게시판 결합은 Board 다의어 불성립",
    94: "카약 실험실 결합은 Lab 불성립",
    95: "바리스타 콘솔 결합은 Console 불성립",
    96: "구강청격 패널 결합은 Panel 불성립",
    97: "폭포 레일 결합은 Rail 다의어 불성립",
    98: "펍 지도집 결합은 Atlas 추상 불성립",
    99: "마우스가드 관리인 결합은 Keeper 불명확",
    100: "선셋 엔진 결합은 Engine 추상 불성립",
    101: "스테이크하우스 동반자 결합은 Companion 불명확",
    102: "스마일 등록부 결합 불성립",
    103: "수변 플레이북 결합 불명확",
    104: "스시 탐색기 결합은 Locator 불명확",
    105: "호흡 탐색기 결합은 Finder 불명확",
    106: "보드워크 계수기 결합은 Counter 다의어 불성립",
    107: "타코 항구 결합은 Harbor 불성립",
    108: "코골이 명부 결합 불성립",
    110: "면집 전광판 결합은 Ticker 불성립",
    111: "교합 선 결합은 Line 다의어 불성립",
    112: "전망 순서 결합은 Roll 다의어 불성립",
    113: "해산물 카드 결합은 Card 다의어 불성립",
    114: "치과 시트 결합은 Sheet 다의어 불성립",
    115: "배낭여행 점수 결합은 Score 불성립",
    116: "교정의 상태 결합은 Status 불성립",
    117: "패러세일링 이력 결합 불성립",
    118: "치위 갱신 결합 불성립",
    119: "야생동물 초안 결합은 Draft 다의어 불성립",
    120: "치실 알림 결합 불성립",
    123: "빙하 코드 결합은 Code 불성립",
    124: "불소 전표 결합은 Slip 다의어 불성립",
    125: "화산 슬롯 결합은 Slot 다의어 불성립",
    126: "실런트 배지 결합 불성립",
    127: "당일여행 정산 결합은 Statement 불성립",
    128: "치은염 탭 결합은 Tab 다의어 불성립",
    129: "요트 요약 결합은 Brief 다의어 불성립",
    130: "이갈이 청원 결합은 Petition 불성립",
    131: "산책로 정리 결합은 Recap 다의어 불성립",
    132: "구취 항목 결합은 Item 다의어 불성립",
    134: "치주염 요금 결합은 Fare 다의어 불성립",
    135: "사막 대출 결합 불성립",
    136: "부정교합 부채 결합 불성립",
    137: "와이너리 현금 결합 불성립",
    138: "치수과 청구 결합은 Charge 다의어 불성립",
    139: "치주과 관세 결합 불성립",
    142: "안건 일정표 결합 불명확",
    143: "금융 소견 결합 불명확",
    144: "규정 권고 결합 불명확",
    145: "예약 세미나 결합 불명확",
    146: "동의서 리트리트 결합 불성립",
    147: "접종 토너먼트 결합 불성립",
    151: "리퍼럴 일정표 결합 불명확",
    152: "피드백 의견 결합 불명확",
    153: "감정 추천 결합 불명확",
    155: "퇴원 선물 결합 불성립 - Gift",
    156: "X-ray 리트리트 결합 불성립",
    157: "세션 토너먼트 결합 불성립",
    159: "카페 사임 결합 불성립",
    162: "흡입기 일정표 결합 불명확",
    163: "제습기 소견 결합 불명확",
    164: "잠금 권고 결합 불명확",
    166: "엘리베이터 선물 결합 불성립 - Gift",
    167: "고객 리트리트 결합 불성립",
    168: "케이크 토너먼트 결합 불성립",
    169: "다이너 지점 결합은 Point 불성립",
    170: "비스트로 모니터 결합 불성립",
    171: "피자집 시트 결합은 Sheet 다의어 불성립",
    173: "디저트 의무 결합 불성립",
    174: "포장 선급 결합은 Advance 다의어 불성립",
    175: "브런치 생성기 결합 불성립",
    177: "제과 보증 결합 불성립",
    178: "베이글 무게 속성 결합은 Weight 불성립",
    179: "도넛 주기 결합은 Cycle 불성립",
    180: "구역 관리 튜토리얼 결합 불명확",
    182: "적성 일정표 결합 불명확",
    183: "네트워킹 의견 결합 불명확",
    184: "정비 권고 결합 불명확",
    186: "식이 선물 결합 불성립 - Gift",
    187: "교정 리트리트 결합 불성립",
    188: "유모차 토너먼트 결합 불성립",
    190: "라떼 신호 결합은 Signal 추상 불성립",
    191: "칫솔 스코프 결합은 Scope 불성립",
    192: "스노클링 파도 결합은 Wave 추상 불성립",
    193: "칵테일 게시판 결합은 Board 다의어 불성립",
    194: "치약 갑판 결합은 Deck 불성립",
    195: "카약 역 결합은 Station 다의어 불성립",
    196: "바리스타 패널 결합은 Panel 불성립",
    197: "구강청격 저울 결합은 Scale 다의어 불성립",
    199: "펍 관리인 결합은 Keeper 불명확",
    200: "마우스가드 관리자 결합은 Manager 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 40, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 160, len(REJECT_REASON)
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
