import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk9_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk9_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "스시집 목록으로 성립 (Registry 라인)"),
    5: (0.6, "호흡 훈련 캘린더로 성립 (Calendar 라인)"),
    13: (0.6, "해산물 시황 보고로 성립 (Report 라인)"),
    14: (0.6, "진료 기록으로 성립 (Log 라인)"),
    16: (0.6, "교정 진료 노트로 성립 (Note 라인)"),
    21: (0.6, "라군 관측 타임라인으로 성립 (Timeline 라인)"),
    27: (0.6, "당일여행 바우처로 성립 (Voucher 라인)"),
    33: (0.6, "우릴 투어 입장료로 성립 (Fee 라인)"),
    34: (0.6, "치주 치료 계획서로 성립 (Plan 라인)"),
    40: (0.6, "차량 할부 교육으로 실재 (Tutorial 라인)"),
    41: (0.6, "위생 핸드북으로 실재 (Handbook 라인)"),
    44: (0.6, "접종 세미나로 실재 (Seminar 라인)"),
    48: (0.6, "검수 서비스 전단으로 실재 (Flyer 라인)"),
    49: (0.6, "피드백 수집 교육으로 실재 (Tutorial 라인)"),
    50: (0.6, "감정 핸드북으로 실재 (Handbook 라인)"),
    52: (0.6, "수의 퇴원 소견으로 성립 (Opinion 라인)"),
    53: (0.6, "촬영 권고로 성립 (Recommendation 라인)"),
    56: (0.6, "시니어 웰니스 리트리트로 실재 (Retreat 여가)"),
    58: (0.6, "제설 서비스 전단으로 실재 (Flyer 라인)"),
    60: (0.6, "제습기 교육으로 실재 (Tutorial 라인)"),
    61: (0.6, "잠금 핸드북으로 실재 (Handbook 라인)"),
    62: (0.6, "문법 수업 시간표로 실재 (Timetable 라인)"),
    65: (0.6, "케이크 제과 강좌로 실재 (Seminar 라인)"),
    68: (0.6, "배수 서비스 전단으로 실재 (Flyer 라인)"),
    75: (0.6, "브런치 이벤트 공지로 성립 (Announcement 라인)"),
    77: (0.6, "제과 청구서로 성립 (Invoice 라인)"),
    78: (0.6, "베이글집 체크인 서비스로 성립 (Checkin 라인)"),
    80: (0.6, "네트워킹 교육으로 실재 (Tutorial 라인)"),
    81: (0.6, "정비 핸드북으로 실재 (Handbook 라인)"),
    82: (0.6, "에스프레소 수업 시간표로 성립 (Timetable 라인)"),
    83: (0.6, "수의 식이 소견으로 성립 (Opinion 라인)"),
    84: (0.6, "교정 치료 권고로 성립 (Recommendation 라인)"),
    86: (0.6, "스파 선물권으로 성립 (Gift 선물권)"),
    88: (0.6, "와이너리 투어 전단으로 실재 (Flyer 라인)"),
    119: (0.6, "야생동물 관측 갱신으로 성립 (Update 라인)"),
    122: (0.6, "스케일링 견적으로 성립 (Estimate 라인)"),
    123: (0.6, "빙하 투어 청구서로 성립 (Bill 라인)"),
    140: (0.6, "안건 작성 교육으로 실재 (Tutorial 라인)"),
    141: (0.6, "할부 핸드북으로 실재 (Handbook 라인)"),
    146: (0.6, "가족 리트리트로 실재 (Retreat 여가)"),
    148: (0.6, "관리 서비스 전단으로 실재 (Flyer 라인)"),
    149: (0.6, "리퍼럴 실무 교육으로 실재 (Tutorial 라인)"),
    150: (0.6, "피드백 핸드북으로 실재 (Handbook 라인)"),
    153: (0.6, "퇴원 권고로 성립 (Recommendation 라인)"),
    154: (0.6, "방사선 세미나로 실재 (Seminar 라인)"),
    160: (0.6, "흡입기 사용 교육으로 실재 (Tutorial 라인)"),
    161: (0.6, "제습기 핸드북으로 실재 (Handbook 라인)"),
    166: (0.6, "선물 케이크로 성립 (Gift 선물권)"),
    168: (0.6, "세차 전단으로 실재 (Flyer 라인)"),
    180: (0.6, "적성 검사 교육으로 실재 (Tutorial 라인)"),
    181: (0.6, "네트워킹 핸드북으로 실재 (Handbook 라인)"),
    184: (0.6, "수의 식이 권고로 성립 (Recommendation 라인)"),
    185: (0.6, "교정 세미나로 실재 (Seminar 라인)"),
    186: (0.6, "유모차 선물로 성립 (Gift 선물권)"),
    187: (0.6, "스파 리트리트로 실재 (Retreat 여가)"),
    188: (0.6, "조경 서비스 전단으로 실재 (Flyer 라인)"),
    197: (0.6, "폭포 투어 코스로 실재 (Route 물리 코스)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "스테이크하우스 플래너 결합 불성립",
    2: "스마일 스케줄러 결합 불성립",
    3: "수변 동반자 결합은 Companion 불명확",
    6: "보드워크 탐색기 결합은 Locator 불명확",
    7: "타코 키오스크 결합은 Kiosk 불성립",
    8: "코골이 만 결합은 Bay 불성립",
    9: "해변 항구 결합은 Harbor 불성립",
    10: "면집 상자 결합은 Bin 불성립",
    11: "교합 여권 결합은 Passport 불성립",
    12: "전망 전광판 결합은 Ticker 불성립",
    15: "배낭여행 카드 결합은 Card 다의어 불성립",
    17: "패러세일링 프로필 결합 불성립",
    18: "치위 서류 결합은 File 다의어 불성립",
    19: "야생동물 요율 속성 결합은 Rate 불성립",
    20: "치실 초안 결합은 Draft 다의어 불성립",
    22: "치석 접수권 결합 불성립",
    23: "빙하 주문 결합은 Order 다의어 불성립",
    24: "불소 코드 결합은 Code 불성립",
    25: "화산 표 결합은 Table 다의어 불성립",
    26: "실런트 슬롯 결합은 Slot 다의어 불성립",
    28: "치은염 정산 결합은 Statement 불성립",
    29: "요트 한도 결합은 Quota 속성어 불성립",
    30: "이갈이 요약 결합은 Brief 다의어 불성립",
    31: "산책로 권고 결합은 Advisory 불성립",
    32: "구취 정리 결합은 Recap 다의어 불성립",
    35: "사막 가격 속성 결합은 Price 불성립",
    36: "부정교합 세금 결합은 Tax 불성립",
    37: "와이너리 합계 결합은 Sum 다의어 불성립",
    38: "치수과 기금 결합 불성립",
    39: "치주과 청구 결합은 Charge 다의어 불성립",
    42: "진료 시간표 결합 불명확",
    43: "동의서 권고 결합 불성립",
    45: "가족 선물 결합 불성립 - Gift",
    46: "약제 리트리트 결합 불성립",
    47: "유지보수 토너먼트 결합 불성립",
    51: "프랜차이즈 일정표 결합 불명확",
    54: "세션 세미나 결합 불명확",
    55: "이정표 선물 결합 불성립 - Gift",
    57: "방제 일정 토너먼트 결합 불성립",
    59: "카페 혜택 결합은 Benefit 불성립",
    63: "엘리베이터 의견 결합 불명확",
    64: "고객 추천 결합 불명확",
    66: "마감 리트리트 결합 불성립",
    67: "세차 토너먼트 결합 불성립",
    69: "다이너 격자 결합은 Grid 추상 불성립",
    70: "비스트로 조수 결합은 Assistant 불명확",
    71: "피자집 기록 결합 불명확",
    72: "데리 샘플 결합은 Sample 다의어 불성립",
    73: "디저트 현금 결합 불성립",
    74: "포장 보조금 결합 불성립",
    76: "베이커리 마감 결합 불명확",
    79: "도넛 상태 속성 결합은 Condition 불성립",
    85: "유모차 세미나 결합 불명확",
    87: "커브 토너먼트 결합 불성립",
    89: "라떼 대장간 결합은 Forge 추상 불성립",
    90: "칫솔 다리 결합은 Bridge 추상 불성립",
    91: "스노클링 스코프 결합은 Scope 불성립",
    92: "칵테일 기지 결합은 Base 추상 불성립",
    93: "치약 핵심 결합은 Core 추상 불성립",
    94: "카약 갑판 결합은 Deck 불성립",
    95: "바리스타 존 결합은 Zone 불성립",
    96: "구강청격 포털 결합은 Portal 불명확",
    97: "폭포 저울 결합은 Scale 다의어 불성립",
    98: "펍 관문 결합은 Gate 불성립",
    99: "마우스가드 연결점 결합은 Nexus 추상 불성립",
    100: "선셋 관리인 결합은 Keeper 불명확",
    101: "스테이크하우스 스케줄러 결합 불성립",
    102: "스마일 모니터 결합 불성립",
    103: "수변 등록부 결합 불성립",
    104: "스시 캘린더 결합 불명확",
    105: "호흡 디렉터리 결합 불명확",
    106: "보드워크 탐색기 결합은 Finder 불명확",
    107: "타코 만 결합은 Bay 불성립",
    108: "코골이 게시 결합은 Post 다의어 불성립",
    109: "해변 명부 결합 불명확",
    110: "면집 여권 결합은 Passport 불성립",
    111: "교합 로비 결합은 Lobby 불성립",
    112: "전망 선 결합은 Line 다의어 불성립",
    113: "해산물 기록 결합 불명확",
    114: "치과 서식 결합은 Form 다의어 불성립",
    115: "배낭여행 시트 결합은 Sheet 다의어 불성립",
    116: "교정의 꼬리표 결합은 Tag 다의어 불성립",
    117: "패러세일링 상태 결합은 Status 불성립",
    118: "치위 수준 속성 결합은 Level 불성립",
    120: "치실 요약 결합 불성립",
    121: "라군 알림 결합 불명확",
    124: "불소 목록 결합 불성립",
    125: "화산 전표 결합은 Slip 다의어 불성립",
    126: "실런트 통행 결합은 Pass 다의어 불성립",
    127: "당일여행 배지 결합 불성립",
    128: "치은염 메모 결합 불성립",
    129: "요트 탭 결합은 Tab 다의어 불성립",
    130: "이갈이 회람 결합은 Circular 다의어 불성립",
    131: "산책로 청원 결합은 Petition 불성립",
    132: "구취 항목 결합은 Entry 다의어 불성립",
    133: "우릴 항목 결합은 Item 다의어 불성립",
    134: "치주염 비용 속성 결합은 Cost 불성립",
    135: "사막 요금 결합은 Fare 다의어 불성립",
    136: "부정교합 대출 결합 불성립",
    137: "와이너리 부채 결합 불성립",
    138: "치수과 현금 결합 불성립",
    139: "치주과 의무 결합 불성립",
    142: "규정 준수 일정표 결합 불명확",
    143: "예약 소견 결합 불성립",
    144: "동의서 세미나 결합 불성립",
    145: "접종 선물 결합 불성립 - Gift",
    147: "약제 토너먼트 결합 불성립",
    151: "감정 일정표 결합 불명확",
    152: "프랜차이즈 평가 결합 불명확",
    155: "세션 선물 결합 불성립 - Gift",
    156: "이정표 리트리트 결합 불성립",
    157: "웰니스 토너먼트 결합 불성립",
    158: "방제 예약 전단 결합 불명확",
    159: "카페 요구사항 결합 불성립",
    162: "잠금 일정표 결합 불명확",
    163: "문법 의견 결합 불명확",
    164: "엘리베이터 추천 결합 불명확",
    165: "고객 세미나 결합 불명확",
    167: "마감 토너먼트 결합 불성립",
    169: "다이너 파도 결합은 Wave 추상 불성립",
    170: "비스트로 플래너 결합 불성립",
    171: "피자집 서식 결합은 Form 다의어 불성립",
    172: "데리 슬롯 결합은 Slot 다의어 불성립",
    173: "디저트 판매 결합은 Sale 다의어 불성립",
    174: "포장 할인 속성 결합은 Discount 불성립",
    175: "브런치 계산기 결합 불명확",
    176: "베이커리 기간 속성 결합은 Duration 불성립",
    177: "제과 갱신 결합 불성립",
    178: "베이글 크기 속성 결합은 Size 불성립",
    179: "도넛 습도 속성 결합은 Humidity 불성립",
    182: "정비 일정표 결합 불명확",
    183: "에스프레소 평가 결합 불명확",
    189: "라떼 폭포 결합은 Cascade 추상 불성립",
    190: "칫솔 신호 결합은 Signal 추상 불성립",
    191: "스노클링 루프 결합은 Loop 추상 불성립",
    192: "칵테일 핵심 결합은 Core 추상 불성립",
    193: "치약 장부 결합은 Ledger 불성립",
    194: "카약 스튜디오 결합 불명확",
    195: "바리스타 포털 결합은 Portal 불명확",
    196: "구강청격 콘솔 결합은 Console 불성립",
    198: "펍 연결점 결합은 Nexus 추상 불성립",
    199: "마우스가드 지도집 결합은 Atlas 추상 불성립",
    200: "선셋 관리자 결합은 Manager 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 57, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 143, len(REJECT_REASON)
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
