import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk13_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk13_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    10: (0.6, "스테이크하우스 목록으로 성립 (Registry 업소 목록 독해)"),
    13: (0.6, "스시 주문 키오스크로 실재 (Kiosk 실물 공간)"),
    28: (0.6, "사파리 투어 입장권으로 성립 (Ticket 라인)"),
    40: (0.6, "산책 코스 계획으로 성립 (Plan 라인)"),
    49: (0.6, "디지털 아카이빙 교육으로 실재 (Tutorial 라인)"),
    50: (0.6, "운전 핸드북으로 실재 (Handbook 라인)"),
    58: (0.6, "식품 규정 안내 전단으로 실재 (Flyer 라인)"),
    59: (0.6, "광고 지면 배치 교육으로 실재 (Tutorial 라인)"),
    68: (0.6, "차량 감정 안내 전단으로 실재 (Flyer 라인)"),
    69: (0.6, "차량 점검 교육으로 실재 (Tutorial 라인)"),
    70: (0.6, "카페 운영 핸드북으로 실재 (Handbook 라인)"),
    90: (0.6, "리모델링 교육으로 실재 (Tutorial 라인)"),
    91: (0.6, "보험 조정 핸드북으로 실재 (Handbook 라인)"),
    131: (0.6, "사파리 투어 견적으로 성립 (Estimate 견적)"),
    140: (0.6, "치은염 치료 예약 확정서로 성립 (Confirmation 라인)"),
    152: (0.6, "광고 소재 제작 교육으로 실재 (Tutorial 라인)"),
    153: (0.6, "아카이브 핸드북으로 실재 (Handbook 라인)"),
    157: (0.6, "CI/CD 파이프라인 세미나로 실재 (Seminar 라인)"),
    161: (0.6, "차량 금융 안내 전단으로 실재 (Flyer 라인)"),
    162: (0.6, "투표 절차 안내 교육으로 실재 (Tutorial 라인)"),
    163: (0.6, "광고 배치 핸드북으로 실재 (Handbook 라인)"),
    167: (0.6, "경계 보안 세미나로 실재 (Seminar 라인)"),
    171: (0.6, "피드백 세미나 모집 전단으로 실재 (Flyer 라인)"),
    173: (0.6, "차량 점검 핸드북으로 실재 (Handbook 라인)"),
    176: (0.6, "잇몸 케어 제품 추천 가이드로 실재 (Recommendation 라인)"),
    177: (0.6, "아동 공예 세미나로 실재 (Seminar 라인)"),
    181: (0.6, "제습기 안내 전단으로 실재 (Flyer 라인)"),
    183: (0.6, "비스트로 목록으로 성립 (Registry 업소 목록 독해)"),
    188: (0.6, "브런치 요리 워크샵으로 실재 (Workshop 교육 행사)"),
    193: (0.6, "냉장 컨테이너 운송 교육으로 실재 (Tutorial 라인)"),
    194: (0.6, "리모델링 핸드북으로 실재 (Handbook 라인)"),
    198: (0.6, "편입 설명회로 실재 (Seminar 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "칵테일 역 결합은 Station 다의어 불성립",
    2: "치약 터미널 결합은 Terminal 불성립",
    3: "카약 포털 결합은 Portal 불성립",
    4: "바리스타 산책로 결합은 Trail 불성립",
    5: "구강청격 사슬 결합은 Chain 불성립",
    6: "폭포 연결점 결합은 Nexus 불성립",
    7: "펍 플래너 결합 불성립",
    8: "마우스가드 스케줄러 결합 불성립",
    9: "선셋 동반자 결합은 Companion 불명확",
    11: "스마일 캘린더 결합 불성립",
    12: "수변 탐색기 결합은 Locator 불명확",
    14: "호흡 만 결합은 Bay 불성립",
    15: "보드워크 항구 결합은 Harbor 불성립",
    16: "타코 여권 결합은 Passport 다의어 불성립",
    17: "코골이 로비 결합은 Lobby 불성립",
    18: "해변 선 결합은 Line 다의어 불성립",
    19: "면집 기록 결합 불성립",
    20: "교합 서식 결합은 Form 다의어 불성립",
    21: "전망 시트 결합은 Sheet 다의어 불성립",
    22: "해산물 태그 결합은 Tag 다의어 불성립",
    23: "치과 프로필 결합 불성립",
    24: "배낭여행 뷰 결합은 View 추상 불성립",
    25: "교정의 요율 속성 결합은 Rate 불성립",
    26: "패러세일링 피드 결합은 Feed 추상 불성립",
    27: "치위 알림 결합 불성립",
    29: "치실 청구서 결합 불성립",
    30: "라군 코드 결합은 Code 불성립",
    31: "치석 전표 결합은 Slip 다의어 불성립",
    32: "빙하 슬롯 결합은 Slot 다의어 불성립",
    33: "불소 배지 결합 불성립",
    34: "화산 정산 결합은 Statement 불성립",
    35: "실런트 탭 결합은 Tab 다의어 불성립",
    36: "당일여행 요약 결합은 Brief 다의어 불성립",
    37: "치은염 청원 결합은 Petition 불성립",
    38: "요트 정리 결합은 Recap 다의어 불성립",
    39: "이갈이 항목 결합은 Item 다의어 불성립",
    41: "구취 요금 결합은 Fare 다의어 불성립",
    42: "우릴 대출 결합 불성립",
    43: "치주염 기금 결합 불성립",
    44: "사막 판매 결합은 Sale 다의어 불성립",
    45: "부정교합 의무 결합 불성립",
    46: "와이너리 관세 결합은 Tariff 불성립",
    47: "치수과 지분 결합은 Stake 불성립",
    48: "치주과 번호 속성 결합은 Number 불성립",
    51: "로밍 일정표 결합 불명확",
    52: "감사 소견 결합 불명확",
    53: "파이프라인 권고 결합 불명확",
    54: "환불 세미나 결합 불명확",
    55: "추천서 선물 결합 불성립 - Gift",
    56: "안건 리트리트 결합 불성립",
    57: "금융 토너먼트 결합 불성립",
    60: "피드 핸드북 결합 불명확",
    61: "허가 일정표 결합 불명확",
    62: "네트워크 소견 결합 불명확",
    63: "경계 권고 결합 불명확",
    64: "런북 세미나 결합 불명확",
    65: "콜백 선물 결합 불성립 - Gift",
    66: "리퍼럴 리트리트 결합 불성립",
    67: "피드백 토너먼트 결합 불성립",
    71: "진드기 일정표 결합 불명확",
    72: "잇몸 소견 결합 불명확",
    73: "공예 권고 결합 불명확",
    74: "식기세척기 세미나 결합 불명확",
    75: "블로우 선물 결합 불성립 - Gift",
    76: "흡입기 리트리트 결합 불성립",
    77: "제습기 토너먼트 결합 불성립",
    78: "마감로크 전단 결합 불명확",
    79: "다이너 장부 결합은 Ledger 불성립",
    80: "비스트로 일지 결합 불명확",
    81: "피자집 프로필 결합 불성립",
    82: "데리 한도 결합은 Quota 속성어 불성립",
    83: "디저트 마진 속성 결합은 Margin 불성립",
    84: "포장 시험 결합은 Trial 다의어 불성립",
    85: "브런치 타이머 결합은 Timer 불성립",
    86: "베이커리 평점 속성 결합은 Rating 불성립",
    87: "제과 수정 결합은 Revision 불성립",
    88: "베이글 시계 결합은 Clock 불성립",
    89: "도넛 승인 결합은 Approval 불성립",
    92: "교육 일정표 결합 불명확",
    93: "패티오 소견 결합 불명확",
    94: "편입 권고 결합 불명확",
    95: "구 세미나 결합 불명확 - Ward",
    96: "기사 선물 결합 불성립 - Gift",
    97: "적성 리트리트 결합 불성립",
    98: "네트워킹 토너먼트 결합 불성립",
    99: "라디에이터 전단 결합 불명확",
    100: "에스프레소 추적기 결합은 Tracker 불성립",
    101: "라떼 파도 결합은 Wave 추상 불성립",
    102: "칫솔 지점 결합은 Point 불성립",
    103: "스노클링 기반 결합은 Base 추상 불성립",
    104: "칵테일 터미널 결합은 Terminal 불성립",
    105: "치약 센터 결합은 Center 불성립",
    106: "카약 콘솔 결합은 Console 불성립",
    107: "바리스타 사슬 결합은 Chain 불성립",
    108: "구강청격 고리 결합은 Ring 불성립",
    109: "폭포 지도집 결합은 Atlas 추상 불성립",
    110: "펍 스케줄러 결합 불성립",
    111: "마우스가드 모니터 결합 불성립",
    112: "선셋 등록부 결합 불성립",
    113: "스테이크하우스 캘린더 결합 불명확",
    114: "스마일 디렉터리 결합 불성립",
    115: "수변 탐색기 결합은 Finder 불명확",
    116: "스시 만 결합은 Bay 불성립",
    117: "호흡 게시 결합은 Post 다의어 불성립",
    118: "보드워크 명부 결합은 Roster 불성립",
    119: "타코 로비 결합은 Lobby 불성립",
    120: "코골이 전광판 결합은 Ticker 불성립",
    121: "해변 창 결합은 Window 다의어 불성립",
    122: "면집 서식 결합은 Form 다의어 불성립",
    123: "교합 카드 결합은 Card 다의어 불성립",
    124: "전망 검사 결합 불명확",
    125: "해산물 프로필 결합 불성립",
    126: "치과 상태 결합은 Status 불성립",
    127: "배낭여행 이력 결합 불성립",
    128: "교정의 갱신 결합 불성립",
    129: "패러세일링 초안 결합은 Draft 다의어 불성립",
    130: "치위 색인 결합은 Index 다의어 불성립",
    132: "치실 영수증 결합 불성립",
    133: "라군 목록 결합 불명확",
    134: "치석 샘플 결합은 Sample 다의어 불성립",
    135: "빙하 통행 결합은 Pass 다의어 불성립",
    136: "불소 전표 결합은 Stub 불성립",
    137: "화산 메모 결합은 Memo 다의어 불성립",
    138: "실런트 회람 결합은 Bulletin 다의어 불성립",
    139: "당일여행 회람 결합은 Circular 다의어 불성립",
    141: "요트 항목 결합은 Entry 다의어 불성립",
    142: "이갈이 단위 결합은 Unit 다의어 불성립",
    143: "산책로 비용 속성 결합은 Cost 불성립",
    144: "구취 세금 결합은 Tax 불성립",
    145: "우릴 합계 결합은 Sum 다의어 불성립",
    146: "치주염 현금 결합 불성립",
    147: "사막 청구 결합은 Charge 다의어 불성립",
    148: "부정교합 수당 결합 불성립",
    149: "와이너리 가치 결합은 Value 불성립",
    150: "치수과 마진 속성 결합은 Margin 불성립",
    151: "치주과 버전 결합은 Version 불성립",
    154: "운전 일정표 결합 불명확",
    155: "로밍 소견 결합 불명확",
    156: "감사 권고 결합 불명확",
    158: "환불 선물 결합 불성립 - Gift",
    159: "추천서 리트리트 결합 불성립",
    160: "안건 토너먼트 결합 불성립",
    164: "피드 일정표 결합 불명확",
    165: "허가 소견 결합 불명확",
    166: "네트워크 권고 결합 불명확",
    168: "런북 선물 결합 불성립 - Gift",
    169: "콜백 리트리트 결합 불성립",
    170: "리퍼럴 토너먼트 결합 불성립",
    172: "랜야드 튜토리얼 결합 불명확",
    174: "카페 일정표 결합 불명확",
    175: "진드기 소견 결합 불명확",
    178: "식기세척기 선물 결합 불성립 - Gift",
    179: "블로우 리트리트 결합 불성립",
    180: "흡입기 토너먼트 결합 불성립",
    182: "다이너 게시판 결합은 Board 다의어 불성립",
    184: "피자집 상태 결합은 Status 불성립",
    185: "데리 탭 결합은 Tab 다의어 불성립",
    186: "디저트 벌금 결합은 Fine 불성립",
    187: "포장 그래프 결합은 Graph 불성립",
    189: "베이커리 협약 결합은 Agreement 불성립",
    190: "제과 결제 결합은 Payment 불성립",
    191: "베이글 시간 결합은 Time 불성립",
    192: "도넛 행렬 결합은 Matrix 불성립",
    195: "보험 조정 일정표 결합 불명확",
    196: "교육 소견 결합 불명확",
    197: "패티오 권고 결합 불명확",
    199: "구 선물 결합 불성립 - Ward Gift",
    200: "기사 리트리트 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 32, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 168, len(REJECT_REASON)
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
