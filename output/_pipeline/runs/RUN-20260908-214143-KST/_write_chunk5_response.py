import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk4_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk4_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "화산 활동 타임라인으로 실재 (Timeline 라인)"),
    10: (0.6, "산책 체험 바우처로 성립 (Voucher 라인)"),
    15: (0.6, "교정 치료 확정 통지로 성립 (Confirmation 라인)"),
    19: (0.6, "가격 책정 실무 교육으로 실재 (Tutorial 라인)"),
    20: (0.6, "묘지 핸드북으로 실재 (Handbook 라인)"),
    21: (0.6, "수수료 정산 일정표로 성립 (Timetable 라인)"),
    23: (0.6, "전세 선박 추천 서비스로 실재 (Recommendation 라인)"),
    24: (0.6, "연료 실무 세미나로 실재 (Seminar 라인)"),
    28: (0.6, "번역 서비스 전단으로 성립 (Flyer 라인)"),
    29: (0.6, "재고 관리 교육으로 실재 (Tutorial 라인)"),
    30: (0.6, "수선 핸드북으로 실재 (Handbook 라인)"),
    31: (0.6, "장례 절차 일정표로 성립 (Timetable 라인)"),
    34: (0.6, "항만 세미나로 실재 (Seminar 라인)"),
    38: (0.6, "도어락 홍보 전단으로 실재 (Flyer 라인)"),
    40: (0.6, "로드트립 계획 튜토리얼로 실재 (Tutorial 라인)"),
    41: (0.6, "아코디언 핸드북으로 실재 (Handbook 라인)"),
    42: (0.6, "알레르기 면역치료 일정표로 성립 (Timetable 라인)"),
    44: (0.6, "섀시 대여 추천으로 성립 (Recommendation 라인)"),
    45: (0.6, "계약 변경 세미나로 성립 (Seminar 라인)"),
    49: (0.6, "논문 첨삭 서비스 전단으로 성립 (Flyer 라인)"),
    52: (0.6, "피자 주문 상태 알림으로 성립 (Alert 라인)"),
    57: (0.6, "베이커리 순위 서비스로 실재 (Rank 라인)"),
    59: (0.6, "베이글 리뷰 콘텐츠로 명확 (Review 음식 리뷰)"),
    62: (0.6, "반주자 실무 튜토리얼로 실재 (Tutorial 라인)"),
    63: (0.6, "질병 핸드북으로 실재 (Handbook 라인)"),
    64: (0.6, "채무 상환 일정표로 성립 (Timetable 라인)"),
    66: (0.6, "이사 지역 추천으로 실재 (Recommendation 라인)"),
    67: (0.6, "소송 세미나로 실재 (Seminar 라인)"),
    71: (0.6, "카페 홍보 전단으로 실재 (Flyer 라인)"),
    87: (0.6, "호흡 훈련 계획 도구로 성립 (Planner 라인)"),
    88: (0.6, "해변 산책로 상태 모니터링으로 성립 (Monitor 라인)"),
    89: (0.6, "타코 음식 저널로 실재 (Journal 라인)"),
    91: (0.6, "해변 시설 디렉터리로 성립 (Directory 라인)"),
    95: (0.6, "해산물 특가 알림으로 성립 (Alert 라인)"),
    96: (0.6, "치과 차팅으로 실재 (Chart 라인)"),
    99: (0.6, "패러세일링 운행 기록으로 성립 (Report 라인)"),
    105: (0.6, "빙하 상태 갱신으로 실재 (Update 라인)"),
    106: (0.6, "불소 도포 요약으로 성립 (Summary 라인)"),
    107: (0.6, "화산 경보 알림으로 실재 (Reminder 라인)"),
    108: (0.6, "실런트 시술 견적으로 성립 (Estimate 라인)"),
    109: (0.6, "당일여행 요금 청구로 성립 (Bill 라인)"),
    119: (0.6, "와이너리 투어 입장료로 성립 (Fee 라인)"),
    122: (0.6, "청소 검수 교육으로 실재 (Tutorial 라인)"),
    123: (0.6, "가격 핸드북으로 실재 (Handbook 라인)"),
    124: (0.6, "묘지 예약 일정표로 성립 (Timetable 라인)"),
    127: (0.6, "전세 세미나로 실재 (Seminar 라인)"),
    131: (0.6, "잠금 서비스 전단으로 실재 (Flyer 라인)"),
    132: (0.6, "제설 실무 튜토리얼로 실재 (Tutorial 라인)"),
    133: (0.6, "재고 핸드북으로 실재 (Handbook 라인)"),
    134: (0.6, "수선 실무 일정표로 성립 (Timetable 라인)"),
    137: (0.6, "리콜 세미나로 실재 (Seminar 라인)"),
    141: (0.6, "코일 교체 홍보 전단으로 실재 (Flyer 라인)"),
    143: (0.6, "배수 트랩 시공 튜토리얼로 실재 (Tutorial 라인)"),
    144: (0.6, "로드트립 핸드북으로 실재 (Handbook 라인)"),
    145: (0.6, "아코디언 수업 시간표로 실재 (Timetable 라인)"),
    146: (0.6, "알레르기 진료 소견으로 성립 (Opinion 라인)"),
    152: (0.6, "사이딩 홍보 전단으로 실재 (Flyer 라인)"),
    154: (0.6, "비스트로 투어 코스로 성립 (Trail 물리 코스)"),
    156: (0.6, "음식점 대기 번호표로 실재 (Ticket 구체 서비스)"),
    157: (0.6, "디저트 준비 계획으로 성립 (Plan 라인)"),
    162: (0.6, "베이글 레시피 콘텐츠로 실재 (Recipe 라인)"),
    165: (0.6, "와인 교육 튜토리얼로 실재 (Tutorial 라인)"),
    166: (0.6, "반주자 핸드북으로 실재 (Handbook 라인)"),
    169: (0.6, "플랫베드 운송 추천으로 성립 (Recommendation 라인)"),
    170: (0.6, "지역 설명회 세미나로 성립 (Seminar 라인)"),
    175: (0.6, "카페인 섭취 추적으로 실재 (Tracker 라인)"),
    191: (0.6, "호흡 훈련 일정 스케줄러로 성립 (Scheduler 라인)"),
    193: (0.6, "타코집 등록 목록으로 성립 (Registry 라인)"),
    194: (0.6, "수면검사 일정 캘린더로 성립 (Calendar 라인)"),
    196: (0.6, "축제 라면 부스로 실재 (Booth 공간)"),
    199: (0.6, "어종 시세 차트로 실재 (Chart 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "치석 서류 결합은 File 다의어 불명확",
    2: "빙하 요율 속성 결합은 Rate 불성립",
    3: "불소 초안 결합은 Draft 다의어 불성립",
    5: "실런트 티켓 결합 불성립",
    6: "당일여행 주문 결합은 Order 다의어 불성립",
    7: "치은염 코드 결합 불성립",
    8: "요트 표 결합은 Table 다의어 불성립",
    9: "이갈이 슬롯 결합은 Slot 다의어 불성립",
    11: "구취 정산 결합은 Statement 불성립",
    12: "우릴 한도 결합은 Quota 속성어 불성립",
    13: "치주염 요약 결합은 Brief 다의어 불성립",
    14: "사막 권고 결합은 Advisory 불성립",
    16: "와이너리 항목 결합은 Entry 다의어 불성립",
    17: "치수과 항목 결합은 Item 다의어 불성립",
    18: "치주과 비용 속성 결합은 Cost 불성립",
    22: "조제 의견 결합 불성립",
    25: "교대 선물 결합 불성립 - Gift",
    26: "필터 리트리트 결합 불성립",
    27: "마스터키 토너먼트 결합 불성립",
    32: "체크아웃 의견 결합 불성립",
    33: "리콜 추천 결합 불성립",
    35: "로그북 선물 결합 불성립 - Gift",
    36: "폐사 리트리트 결합 불성립",
    37: "코일 토너먼트 결합 불성립",
    39: "카페 주기 속성 결합은 Cycle 불성립",
    43: "송금 의견 결합 불성립",
    46: "잔존물 선물 결합 불성립 - Gift",
    47: "연금 리트리트 결합 불성립",
    48: "사이딩 토너먼트 결합 불성립",
    50: "다이너 금고 결합은 Vault 추상 불성립",
    51: "비스트로 레일 결합은 Rail 다의어 불성립",
    53: "데리 색인 결합은 Index 다의어 불성립",
    54: "디저트 단위 결합은 Unit 다의어 불성립",
    55: "포장 형식 결합은 Format 불성립",
    56: "브런치 스케치 결합은 Sketch 불성립",
    58: "페이스트리 검증 결합은 Validation 다의어 불성립",
    60: "도넛 온도 속성 결합은 Temperature 불성립",
    61: "에스프레소 활용 속성 결합은 Utilization 불성립",
    65: "플랫베드 의견 결합 불성립",
    68: "피부양자 선물 결합 불성립 - Gift",
    69: "캐비닛 리트리트 결합 불성립",
    70: "철회 토너먼트 결합은 Withdrawal 다의어 불성립",
    72: "칫솔 흐름 결합은 Flow 추상 불성립",
    73: "스노클링 레이더 결합은 Radar 추상 불성립",
    74: "칵테일 신호 결합은 Signal 추상 불성립",
    75: "치약 시계 결합은 Watch 다의어 불성립",
    76: "카약 격자 결합은 Grid 추상 불성립",
    77: "바리스타 기지 결합은 Base 추상 불성립",
    78: "구강청격 핵심 결합은 Core 추상 불성립",
    79: "폭포 갑판 결합은 Deck 불성립",
    80: "펍 존 결합은 Zone 불성립",
    81: "마우스가드 포털 결합은 Portal 불명확",
    82: "선셋 패널 결합은 Panel 불성립",
    83: "스테이크하우스 사슬 결합은 Chain 다의어 불성립",
    84: "스마일 링 결합은 Ring 불성립",
    85: "수변 연결점 결합은 Nexus 추상 불성립",
    86: "스시 조수 결합은 Assistant 불명확",
    90: "코골이 등록부 결합 불명확",
    92: "면집 계수기 결합은 Counter 다의어 불성립",
    93: "교합 부스 결합 불성립",
    94: "전망 만 결합은 Bay 불성립",
    97: "배낭여행 여권 결합은 Passport 불성립",
    98: "교정의 창 결합은 Window 다의어 불성립",
    100: "치위 시트 결합은 Sheet 다의어 불성립",
    101: "야생동물 점수 결합은 Score 불성립",
    102: "치실 프로필 결합 불성립",
    103: "라군 뷰 결합은 View 추상 불성립",
    104: "치석 수준 속성 결합은 Level 불성립",
    110: "치은염 목록 결합 불성립",
    111: "요트 전표 결합은 Slip 다의어 불성립",
    112: "이갈이 통행 결합은 Pass 다의어 불성립",
    113: "산책로 배지 결합 불성립",
    114: "구취 메모 결합 불성립",
    115: "우릴 탭 결합은 Tab 다의어 불성립",
    116: "치주염 회람 결합은 Circular 다의어 불성립",
    117: "사막 청원 결합은 Petition 불성립",
    118: "부정교합 정리 결합은 Recap 다의어 불성립",
    120: "치수과 단위 결합은 Unit 다의어 불성립",
    121: "치주과 가격 속성 결합은 Price 불성립",
    125: "수수료 의견 결합 불성립",
    126: "조제 추천 결합 불명확",
    128: "연료 선물 결합 불성립 - Gift",
    129: "교대 리트리트 결합 불성립",
    130: "필터 토너먼트 결합 불성립",
    135: "추모 의견 결합 불성립",
    136: "체크아웃 추천 결합 불명확",
    138: "항만 선물 결합 불성립 - Gift",
    139: "로그북 리트리트 결합 불성립",
    140: "폐사 토너먼트 결합 불성립",
    142: "카페 고장 결합은 Breakdown 다의어 불성립",
    147: "송금 추천 결합 불명확",
    148: "섀시 세미나 결합 성립 여부 불명확",
    149: "계약 변경 선물 결합 불성립 - Gift",
    150: "잔존물 리트리트 결합 불성립",
    151: "연금 토너먼트 결합 불성립",
    153: "다이너 나침반 결합은 Compass 추상 불성립",
    155: "피자집 차트 결합 불성립",
    158: "포장 일련번호 결합은 Serial 불성립",
    159: "브런치 개요 결합은 Outline 불성립",
    160: "베이커리 추세 결합은 Trend 불성립",
    161: "페이스트리 조회 결합은 Lookup 불성립",
    163: "도넛 압력 속성 결합은 Pressure 불성립",
    164: "에스프레소 혜택 결합은 Benefit 불성립",
    167: "질병 일정표 결합 불성립",
    168: "채무자 의견 결합 불성립",
    171: "소송 선물 결합 불성립 - Gift",
    172: "피부양자 리트리트 결합 불성립",
    173: "캐비닛 토너먼트 결합 불성립",
    174: "철회 전단 결합은 Withdrawal 다의어 불성립",
    176: "칫솔 허브 결합은 Hub 불성립",
    177: "스노클링 릴레이 결합은 Relay 불성립",
    178: "칵테일 시계 결합은 Watch 다의어 불성립",
    179: "치약 스코프 결합은 Scope 불성립",
    180: "카약 파도 결합은 Wave 추상 불성립",
    181: "바리스타 핵심 결합은 Core 추상 불성립",
    182: "구강청격 장부 결합은 Ledger 불성립",
    183: "폭포 스튜디오 결합 불명확",
    184: "펍 포털 결합은 Portal 불명확",
    185: "마우스가드 콘솔 결합은 Console 불성립",
    186: "선셋 저울 결합은 Scale 다의어 불성립",
    187: "스테이크하우스 링 결합은 Ring 불성립",
    188: "스마일 관문 결합은 Gate 불성립",
    189: "수변 지도집 결합은 Atlas 추상 불성립",
    190: "스시 계획 결합 불성립",
    192: "복도 동반자 결합은 Companion 불명확",
    195: "해변 탐색기 결합은 Locator 불명확",
    197: "교합 키오스크 결합은 Kiosk 불성립",
    198: "전망 게시 결합은 Post 다의어 불성립",
    200: "치과 상자 결합은 Bin 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 71, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 129, len(REJECT_REASON)
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
