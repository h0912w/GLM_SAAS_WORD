import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk7_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk7_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    6: (0.6, "해변 임대 부스로 실재 (Booth 공간)"),
    14: (0.6, "패러세일링 안전 점검으로 성립 (Check 라인)"),
    18: (0.6, "라군 상태 갱신으로 성립 (Update 라인)"),
    19: (0.6, "치석 진료 요약서로 성립 (Summary 라인)"),
    21: (0.6, "불소 도포 견적으로 성립 (Estimate 라인)"),
    22: (0.6, "화산 투어 청구서로 성립 (Bill 라인)"),
    33: (0.6, "교정 치료 계획서로 성립 (Plan 라인)"),
    37: (0.6, "동의서 실무 교육으로 실재 (Tutorial 라인)"),
    38: (0.6, "예방접종 핸드북으로 실재 (Handbook 라인)"),
    42: (0.6, "검수 세미나로 실재 (Seminar 라인)"),
    46: (0.6, "조제 서비스 전단으로 실재 (Flyer 라인)"),
    47: (0.6, "X-ray 촬영 실무 교육으로 실재 (Tutorial 라인)"),
    48: (0.6, "세션 핸드북으로 실재 (Handbook 라인)"),
    49: (0.6, "발달 이정표 일정표로 성립 (Timetable 라인)"),
    52: (0.6, "제설 세미나로 실재 (Seminar 라인)"),
    58: (0.6, "고객 응대 교육으로 실재 (Tutorial 라인)"),
    59: (0.6, "케이크 핸드북으로 실재 (Handbook 라인)"),
    62: (0.6, "배수 실무 세미나로 성립 (Seminar 라인)"),
    66: (0.6, "송금 서비스 전단으로 성립 (Flyer 라인)"),
    76: (0.6, "베이글 뉴스레터로 실재 (Newsletter 구독 콘텐츠)"),
    79: (0.6, "교정 관리 교육으로 실재 (Tutorial 라인)"),
    80: (0.6, "유모차 핸드북으로 실재 (Handbook 라인)"),
    81: (0.6, "스파 예약 일정표로 실재 (Timetable 라인)"),
    83: (0.6, "와인 세미나로 실재 (Seminar 라인)"),
    87: (0.6, "플랫베드 서비스 전단으로 실재 (Flyer 라인)"),
    104: (0.6, "호흡 훈련 가이드로 성립 (Playbook 라인)"),
    114: (0.6, "배낭여행 후기 보고로 성립 (Report 라인)"),
    124: (0.6, "화산 투어 영수증으로 성립 (Receipt 라인)"),
    127: (0.6, "치은염 치료 바우처로 성립 (Voucher 라인)"),
    132: (0.6, "우릴 투어 예약 확정으로 성립 (Confirmation 라인)"),
    139: (0.6, "동의서 핸드북으로 실재 (Handbook 라인)"),
    140: (0.6, "예방접종 일정표로 실재 (Timetable 라인)"),
    143: (0.6, "유지보수 세미나로 실재 (Seminar 라인)"),
    148: (0.6, "퇴원 안내 교육으로 실재 (Tutorial 라인)"),
    149: (0.6, "X-ray 핸드북으로 실재 (Handbook 라인)"),
    150: (0.6, "세션 일정표로 실재 (Timetable 라인)"),
    152: (0.6, "웰니스 권고 콘텐츠로 성립 (Recommendation 라인)"),
    153: (0.6, "방제 실무 세미나로 성립 (Seminar 라인)"),
    157: (0.6, "추모 행사 전단으로 실재 (Flyer 라인)"),
    158: (0.7, "카페 컨설팅 평가로 성립 (Evaluation 도메인 실무)"),
    160: (0.6, "고객 응대 핸드북으로 실재 (Handbook 라인)"),
    161: (0.6, "케이크 제작 일정표로 성립 (Timetable 라인)"),
    163: (0.6, "세차 세미나로 실재 (Seminar 라인)"),
    167: (0.6, "알레르기 안내 전단으로 실재 (Flyer 라인)"),
    171: (0.6, "데리 메뉴 목록으로 성립 (List 라인)"),
    180: (0.6, "식이 교육으로 실재 (Tutorial 라인)"),
    181: (0.6, "교정 핸드북으로 실재 (Handbook 라인)"),
    188: (0.6, "채무 관리 서비스 전단으로 성립 (Flyer 라인)"),
    198: (0.6, "펍 크롤 트레일로 실재 (Trail 물리 코스)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "스시 등록부 결합 불성립",
    2: "호흡 운영 결합은 Ops 불성립",
    3: "보드워크 저널 결합 불명확",
    4: "타코 탐색기 결합은 Finder 불명확",
    5: "코골이 사무실 결합 불성립",
    7: "면집 항구 결합은 Harbor 불성립",
    8: "교합 명부 결합 불성립",
    9: "전망 안내도 결합 불명확",
    10: "해산물 전광판 결합은 Ticker 불성립",
    11: "치과 선 결합은 Line 다의어 불성립",
    12: "배낭여행 순서 결합은 Roll 다의어 불성립",
    13: "교정의 카드 결합은 Card 다의어 불성립",
    15: "치위 프로필 결합 불성립",
    16: "야생동물 뷰 결합은 View 추상 불성립",
    17: "치실 수준 속성 결합은 Level 불성립",
    20: "빙하 알림 결합 불명확",
    23: "실런트 목록 결합 불명확",
    24: "당일여행 전표 결합은 Slip 다의어 불성립",
    25: "치은염 통행 결합은 Pass 다의어 불성립",
    26: "요트 배지 결합 불성립",
    27: "이갈이 메모 결합 불성립",
    28: "산책로 탭 결합은 Tab 다의어 불성립",
    29: "구취 회람 결합은 Circular 다의어 불성립",
    30: "우릴 청원 결합은 Petition 불성립",
    31: "치주염 항목 결합은 Entry 다의어 불성립",
    32: "사막 항목 결합은 Item 다의어 불성립",
    34: "와이너리 가격 속성 결합은 Price 불성립",
    35: "치수과 세금 결합은 Tax 불성립",
    36: "치주과 부채 결합 불성립",
    39: "가족 방문 일정표 결합 불성립",
    40: "약제 소견 결합 불명확",
    41: "유지보수 권고 결합 불명확",
    43: "가격 선물 결합 불성립 - Gift",
    44: "묘지 리트리트 결합 불성립",
    45: "수수료 토너먼트 결합 불성립",
    50: "웰니스 소견 결합 불명확",
    51: "방제 일정 추천 결합 불명확",
    53: "재고 선물 결합 불성립 - Gift",
    54: "수선 리트리트 결합 불성립",
    55: "추모 토너먼트 결합 불성립",
    56: "체크아웃 전단 결합 불명확",
    57: "카페 행렬 결합은 Matrix 추상 불성립",
    60: "마감 소견 결합 불명확",
    61: "세차 권고 결합 불명확",
    63: "로드트립 선물 결합 불성립 - Gift",
    64: "아코디언 리트리트 결합 불성립",
    65: "알레르기 토너먼트 결합 불성립",
    67: "다이너 신호 결합은 Signal 추상 불성립",
    68: "비스트로 지도집 결합은 Atlas 추상 불성립",
    69: "피자집 선 결합은 Line 다의어 불성립",
    70: "데리 코드 결합은 Code 불성립",
    71: "디저트 대출 결합 불성립",
    72: "포장 이자 결합은 Interest 다의어 불성립",
    73: "브런치 메시지 결합은 Message 불성립",
    74: "베이커리 사본 결합은 Copy 다의어 불성립",
    75: "페이스트리 방송 결합은 Broadcast 다의어 불성립",
    77: "도넛 빈도 속성 결합은 Frequency 불성립",
    78: "에스프레소 보증인 결합 불성립",
    82: "커브 권고 결합 불명확",
    84: "반주자 선물 결합 불성립 - Gift",
    85: "질병 리트리트 결합 불성립",
    86: "채무자 토너먼트 결합 불성립",
    88: "라떼 릴레이 결합은 Relay 불성립",
    89: "칫솔 나침반 결합은 Compass 추상 불성립",
    90: "스노클링 폭포 결합은 Cascade 추상 불성립",
    91: "칵테일 경로 결합 불성립",
    92: "치약 지점 결합은 Point 불성립",
    93: "카약 기지 결합은 Base 추상 불성립",
    94: "바리스타 실험실 결합은 Lab 불성립",
    95: "구강청격 역 결합은 Station 다의어 불성립",
    96: "폭포 존 결합은 Zone 불성립",
    97: "펍 레일 결합은 Rail 다의어 불성립",
    98: "마우스가드 트레일 결합 불성립",
    99: "선셋 링 결합은 Ring 불성립",
    100: "스테이크하우스 관리자 결합은 Manager 불명확",
    101: "스마일 엔진 결합은 Engine 추상 불성립",
    102: "수변 플래너 결합 불명확",
    103: "스시 운영 결합은 Ops 불성립",
    105: "보드워크 등록부 결합 불성립",
    106: "타코 사무실 결합 불성립",
    107: "코골이 계수기 결합은 Counter 다의어 불성립",
    108: "해변 키오스크 결합은 Kiosk 불성립",
    109: "면집 명부 결합 불명확",
    110: "교합 알림 결합 불명확",
    111: "전망 상자 결합은 Bin 불성립",
    112: "해산물 선 결합은 Line 다의어 불성립",
    113: "치과 창 결합은 Window 다의어 불성립",
    115: "교정의 시트 결합은 Sheet 다의어 불성립",
    116: "패러세일링 점수 결합은 Score 불성립",
    117: "치위 상태 결합은 Status 불성립",
    118: "야생동물 이력 결합 불명확",
    119: "치실 요율 속성 결합은 Rate 불성립",
    120: "라군 피드 결합은 Feed 추상 불성립",
    121: "치석 타임라인 결합 불명확",
    122: "빙하 색인 결합은 Index 다의어 불성립",
    123: "불소 주문 결합은 Order 다의어 불성립",
    125: "실런트 표 결합은 Table 다의어 불성립",
    126: "당일여행 샘플 결합은 Sample 다의어 불성립",
    128: "요트 전표 결합은 Stub 불성립",
    129: "이갈이 한도 결합은 Quota 속성어 불성립",
    130: "산책로 회람 결합은 Bulletin 다의어 불성립",
    131: "구취 권고 결합은 Advisory 불성립",
    133: "치주염 요금 결합은 Fee 불성립",
    134: "사막 단위 결합은 Unit 다의어 불성립",
    135: "부정교합 비용 속성 결합은 Cost 불성립",
    136: "와이너리 요금 결합은 Fare 다의어 불성립",
    137: "치수과 대출 결합 불성립",
    138: "치주과 기금 결합 불성립",
    141: "가족 소견 결합 불명확",
    142: "약제 권고 결합 불명확",
    144: "검수 선물 결합 불성립 - Gift",
    145: "가격 리트리트 결합 불성립",
    146: "묘지 토너먼트 결합 불성립",
    147: "수수료 전단 결합 불명확",
    151: "이정표 의견 결합 불명확",
    154: "제설 선물 결합 불성립 - Gift",
    155: "재고 리트리트 결합 불성립",
    156: "수선 토너먼트 결합 불성립",
    159: "엘리베이터 튜토리얼 결합 불명확",
    162: "마감 권고 결합 불명확",
    164: "배수 선물 결합 불성립 - Gift",
    165: "로드트립 리트리트 결합 불성립",
    166: "아코디언 토너먼트 결합 불성립",
    168: "다이너 시계 결합은 Watch 다의어 불성립",
    169: "비스트로 관리인 결합은 Keeper 불명확",
    170: "피자집 창 결합은 Window 다의어 불성립",
    172: "디저트 합계 결합은 Sum 다의어 불성립",
    173: "포장 자산 결합은 Asset 불성립",
    174: "브런치 합계 결합은 Total 불성립",
    175: "베이커리 독해 결합은 Reading 다의어 불성립",
    176: "페이스트리 바코드 결합 불성립",
    177: "베이글 재고 결합 불성립",
    178: "도넛 호환 속성 결합은 Compatibility 불성립",
    179: "에스프레소 조율기 결합 불성립",
    182: "유모차 일정표 결합 불성립",
    183: "스파 소견 결합 불명확",
    184: "커브 세미나 결합 불명확",
    185: "와이너리 선물 결합 불성립 - Gift",
    186: "반주자 리트리트 결합 불성립",
    187: "질병 토너먼트 결합 불성립",
    189: "라떼 금고 결합은 Vault 추상 불성립",
    190: "칫솔 등대 결합은 Beacon 추상 불성립",
    191: "스노클링 다리 결합은 Bridge 추상 불성립",
    192: "칵테일 지점 결합은 Point 불성립",
    193: "치약 지도 결합 불성립",
    194: "카약 핵심 결합은 Core 추상 불성립",
    195: "바리스타 역 결합은 Station 다의어 불성립",
    196: "구강청격 터미널 결합은 Terminal 불성립",
    197: "폭포 포털 결합은 Portal 불명확",
    199: "마우스가드 사슬 결합은 Chain 다의어 불성립",
    200: "선셋 관문 결합은 Gate 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 49, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
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
