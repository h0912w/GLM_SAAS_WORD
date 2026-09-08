import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk6_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk6_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "해변 전망 사무실 임대로 성립 (Office 라인)"),
    9: (0.6, "교정 진행 기록으로 성립 (Log 라인)"),
    11: (0.6, "치위 진료 노트로 성립 (Note 라인)"),
    16: (0.6, "빙하 관측 요약으로 실재 (Summary 라인)"),
    18: (0.6, "화산 투어 견적으로 성립 (Estimate 라인)"),
    19: (0.6, "실런트 시술 영수증으로 성립 (Receipt 라인)"),
    20: (0.6, "당일여행 준비 목록으로 성립 (List 라인)"),
    27: (0.6, "치주 치료 확정 통지로 성립 (Confirmation 라인)"),
    30: (0.6, "와이너리 투어 계획으로 성립 (Plan 라인)"),
    33: (0.6, "가족 돌봄 교육으로 실재 (Tutorial 라인)"),
    34: (0.6, "방제 약제 핸드북으로 실재 (Handbook 라인)"),
    35: (0.6, "유지보수 일정표로 실재 (Timetable 라인)"),
    36: (0.6, "검사 소견서로 성립 (Opinion 라인)"),
    38: (0.6, "묘지 안내 설명회로 성립 (Seminar 라인)"),
    42: (0.6, "항공 유류 서비스 전단으로 성립 (Flyer 라인)"),
    43: (0.6, "발달 이정표 교육 콘텐츠로 실재 (Tutorial 라인)"),
    44: (0.6, "웰니스 핸드북으로 실재 (Handbook 라인)"),
    45: (0.6, "방제 일정표로 실재 (Timetable 라인)"),
    48: (0.6, "수선 실무 세미나로 성립 (Seminar 라인)"),
    52: (0.6, "항만 서비스 전단으로 실재 (Flyer 라인)"),
    54: (0.6, "수영장 동계 마감 핸드북으로 실재 (Handbook 라인)"),
    57: (0.6, "로드트립 코스 추천으로 실재 (Recommendation 라인)"),
    58: (0.6, "아코디언 세미나로 실재 (Seminar 라인)"),
    62: (0.6, "계약 변경 안내 전단으로 성립 (Flyer 라인)"),
    66: (0.6, "케이터링 청구서로 성립 (Bill 라인)"),
    69: (0.6, "브런치 키트로 실재 (Kit 구체 물건)"),
    75: (0.6, "스파 교육 튜토리얼로 실재 (Tutorial 라인)"),
    78: (0.6, "반주자 추천 서비스로 성립 (Recommendation 라인)"),
    79: (0.6, "질병 세미나로 실재 (Seminar 라인)"),
    83: (0.6, "소송 서비스 전단으로 성립 (Flyer 라인)"),
    89: (0.6, "카약 코스 지도로 실재 (Map 물리 코스)"),
    95: (0.6, "선셋 트레일로 실재 (Trail 물리 코스)"),
    118: (0.6, "빙하 변화 타임라인으로 실재 (Timeline 라인)"),
    124: (0.6, "요트 투어 바우처로 실재 (Voucher 라인)"),
    130: (0.6, "사막 투어 입장료로 성립 (Fee 라인)"),
    135: (0.6, "예방접종 교육으로 실재 (Tutorial 라인)"),
    136: (0.6, "가족 돌봄 핸드북으로 실재 (Handbook 라인)"),
    137: (0.6, "약제 살포 일정표로 실재 (Timetable 라인)"),
    144: (0.6, "전세 서비스 전단으로 실재 (Flyer 라인)"),
    145: (0.6, "운동 세션 교육으로 실재 (Tutorial 라인)"),
    146: (0.6, "발달 이정표 핸드북으로 실재 (Handbook 라인)"),
    147: (0.6, "웰니스 일정표로 실재 (Timetable 라인)"),
    154: (0.6, "리콜 공지 전단으로 실재 (Flyer 라인)"),
    156: (0.6, "케이크 제조 교육으로 실재 (Tutorial 라인)"),
    157: (0.6, "수영장 마감 일정표로 실재 (Timetable 라인)"),
    160: (0.6, "로드트립 세미나로 실재 (Seminar 라인)"),
    164: (0.6, "섀시 서비스 전단으로 실재 (Flyer 라인)"),
    168: (0.6, "케이터링 영수증으로 성립 (Receipt 라인)"),
    172: (0.6, "베이커리 판매 기록으로 성립 (Record 라인)"),
    177: (0.6, "유모차 사용 교육으로 실재 (Tutorial 라인)"),
    178: (0.6, "스파 핸드북으로 실재 (Handbook 라인)"),
    180: (0.6, "와인 추천 콘텐츠로 실재 (Recommendation 라인)"),
    181: (0.6, "반주자 세미나로 실재 (Seminar 라인)"),
    185: (0.6, "동네 안내 전단으로 실재 (Flyer 라인)"),
    195: (0.6, "펍 크롤 코스로 실재 (Route 물리 코스)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "코골이 탐색기 결합은 Locator 불명확",
    3: "면집 만 결합은 Bay 불성립",
    4: "교합 게시 결합은 Post 다의어 불성립",
    5: "전망 명부 결합 불명확",
    6: "해산물 여권 결합은 Passport 불성립",
    7: "치과 로비 결합은 Lobby 불성립",
    8: "배낭여행 선 결합은 Line 다의어 불성립",
    10: "패러세일링 카드 결합은 Card 다의어 불성립",
    12: "야생동물 프로필 결합 불성립",
    13: "치실 이력 결합 불성립",
    14: "라군 수준 속성 결합은 Level 불성립",
    15: "치석 피드 결합은 Feed 추상 불성립",
    17: "불소 색인 결합은 Index 다의어 불성립",
    21: "치은염 샘플 결합은 Sample 다의어 불성립",
    22: "요트 통행 결합은 Pass 다의어 불성립",
    23: "이갈이 전표 결합은 Stub 불성립",
    24: "산책 메모 결합 불성립",
    25: "구취 회람 결합은 Bulletin 다의어 불성립",
    26: "우릴 회람 결합은 Circular 다의어 불성립",
    28: "사막 항목 결합은 Entry 다의어 불성립",
    29: "부정교합 항목 결합은 Item 다의어 불성립",
    31: "치수과 가격 속성 결합은 Price 불성립",
    32: "치주과 대출 결합 불성립",
    37: "가격 추천 결합 불명확",
    39: "수수료 선물 결합 불성립 - Gift",
    40: "조제 리트리트 결합 불성립",
    41: "전세 토너먼트 결합 불성립",
    46: "제설 의견 결합 불명확",
    47: "재고 추천 결합 불명확",
    49: "추모 선물 결합 불성립 - Gift",
    50: "체크아웃 리트리트 결합 불성립",
    51: "리콜 토너먼트 결합 불성립",
    53: "카페 후속 연락 결합 불명확",
    55: "세차 일정표 결합 불성립",
    56: "배수 의견 결합 불명확",
    59: "알레르기 선물 결합 불성립 - Gift",
    60: "송금 리트리트 결합 불성립",
    61: "섀시 토너먼트 결합 불성립",
    63: "다이너 폭포 결합은 Cascade 추상 불성립",
    64: "비스트로 관문 결합은 Gate 불성립",
    65: "피자집 로비 결합은 Lobby 불성립",
    67: "디저트 요금 결합은 Fare 다의어 불성립",
    68: "포장 표지 결합은 Marker 다의어 불성립",
    70: "베이커리 보증 결합 불명확",
    71: "페이스트리 가용 결합은 Availability 불성립",
    72: "베이글 환불 결합 불명확",
    73: "도넛 전력 속성 결합은 Wattage 불성립",
    74: "에스프레소 사임 결합 불성립",
    76: "커브 일정표 결합 불성립",
    77: "와이너리 평론 결합 불명확",
    80: "채무자 선물 결합 불성립 - Gift",
    81: "플랫베드 리트리트 결합 불성립",
    82: "동네 토너먼트 결합 불성립",
    84: "라떼 책상 결합은 Desk 불성립",
    85: "칫솔 릴레이 결합은 Relay 불성립",
    86: "스노클링 등대 결합은 Beacon 추상 불성립",
    87: "칵테일 격자 결합은 Grid 추상 불성립",
    88: "치약 파도 결합은 Wave 추상 불성립",
    90: "바리스타 갑판 결합은 Deck 불성립",
    91: "구강청격 스튜디오 결합 불명확",
    92: "폭포 터미널 결합은 Terminal 불성립",
    93: "펍 저울 결합은 Scale 다의어 불성립",
    94: "마우스가드 경로 결합 불성립",
    96: "스테이크하우스 지도집 결합은 Atlas 추상 불성립",
    97: "스마일 관리인 결합은 Keeper 불명확",
    98: "수변 엔진 결합은 Engine 추상 불성립",
    99: "스시 동반자 결합은 Companion 불명확",
    100: "호흡 등록부 결합 불성립",
    101: "보드워크 플레이북 결합 불명확",
    102: "타코 탐색기 결합은 Locator 불명확",
    103: "코골이 탐색기 결합은 Finder 불명확",
    104: "해변 계수기 결합은 Counter 다의어 불성립",
    105: "면집 게시 결합은 Post 다의어 불성립",
    106: "교합 항구 결합은 Harbor 불성립",
    107: "전망 알림 결합 불명확",
    108: "해산물 로비 결합은 Lobby 불성립",
    109: "치과 전광판 결합은 Ticker 불성립",
    110: "배낭여행 창 결합은 Window 다의어 불성립",
    111: "교정의 서식 결합은 Form 다의어 불성립",
    112: "패러세일링 시트 결합은 Sheet 다의어 불성립",
    113: "치위 꼬리표 결합은 Tag 다의어 불성립",
    114: "야생동물 상태 결합은 Status 불성립",
    115: "치실 서류 결합은 File 다의어 불성립",
    116: "라군 요율 속성 결합은 Rate 불성립",
    117: "치석 초안 결합은 Draft 다의어 불성립",
    119: "불소 접수권 결합 불명확",
    120: "화산 주문 결합은 Order 다의어 불성립",
    121: "실런트 코드 결합은 Code 불성립",
    122: "당일여행 표 결합은 Table 다의어 불성립",
    123: "치은염 슬롯 결합은 Slot 다의어 불성립",
    125: "이갈이 정산 결합은 Statement 불성립",
    126: "산책로 한도 결합은 Quota 속성어 불성립",
    127: "구취 요약 결합은 Brief 다의어 불성립",
    128: "우릴 권고 결합은 Advisory 불성립",
    129: "치주염 정리 결합은 Recap 다의어 불성립",
    131: "부정교합 단위 결합은 Unit 다의어 불성립",
    132: "와이너리 비용 속성 결합은 Cost 불성립",
    133: "치수과 요금 결합은 Fare 다의어 불성립",
    134: "치주과 합계 결합은 Sum 다의어 불성립",
    138: "유지보수 의견 결합 불명확",
    139: "검수 권고 결합 불명확",
    140: "가격 세미나 결합 불명확",
    141: "묘지 선물 결합 불성립 - Gift",
    142: "수수료 리트리트 결합 불성립",
    143: "조제 토너먼트 결합 불성립",
    148: "방제 일정 의견 결합 불명확",
    149: "제설 추천 결합 불명확",
    150: "재고 세미나 결합 불명확",
    151: "수선 선물 결합 불성립 - Gift",
    152: "추모 리트리트 결합 불성립",
    153: "체크아웃 토너먼트 결합 불성립",
    155: "카페 승인 결합은 Approval 다의어 불성립",
    158: "세차 의견 결합 불명확",
    159: "배수 권고 결합 불명확",
    161: "아코디언 선물 결합 불성립 - Gift",
    162: "알레르기 리트리트 결합 불성립",
    163: "송금 토너먼트 결합 불성립",
    165: "다이너 다리 결합은 Bridge 추상 불성립",
    166: "비스트로 연결점 결합은 Nexus 추상 불성립",
    167: "피자집 전광판 결합은 Ticker 불성립",
    169: "디저트 세금 결합은 Tax 불성립",
    170: "포장 잔고 결합은 Balance 다의어 불성립",
    171: "브런치 개수 결합은 Count 다의어 불성립",
    173: "페이스트리 자격 결합은 Eligibility 불성립",
    174: "베이글 지출 결합 불성립",
    175: "도넛 밝기 속성 결합은 Brightness 불성립",
    176: "에스프레소 위험 결합 불성립",
    179: "커브 소견 결합 불명확",
    182: "질병 선물 결합 불성립 - Gift",
    183: "채무자 리트리트 결합 불성립",
    184: "플랫베드 토너먼트 결합 불성립",
    186: "라떼 레이더 결합은 Radar 추상 불성립",
    187: "칫솔 금고 결합은 Vault 추상 불성립",
    188: "스노클링 대장간 결합은 Forge 추상 불성립",
    189: "칵테일 파도 결합은 Wave 추상 불성립",
    190: "치약 경로 결합 불성립",
    191: "카약 액자 결합은 Frame 추상 불성립",
    192: "바리스타 스튜디오 결합 불명확",
    193: "구강청격 실험실 결합은 Lab 불성립",
    194: "폭포 센터 결합은 Center 불성립",
    196: "마우스가드 레일 결합은 Rail 다의어 불성립",
    197: "선셋 사슬 결합은 Chain 다의어 불성립",
    198: "스테이크하우스 관리인 결합은 Keeper 불명확",
    199: "스마일 관리자 결합은 Manager 불명확",
    200: "수변 조수 결합은 Assistant 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 55, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 145, len(REJECT_REASON)
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
