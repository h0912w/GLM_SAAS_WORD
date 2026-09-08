import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk8_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk8_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    5: (0.6, "호흡 훈련 일지로 실재 (Journal 라인)"),
    6: (0.6, "보드워크 이벤트 캘린더로 성립 (Calendar 라인)"),
    11: (0.6, "교합 차팅으로 성립 (Chart 라인)"),
    15: (0.6, "배낭여행 기록으로 실재 (Log 라인)"),
    16: (0.6, "교정 검진 서비스로 성립 (Check 라인)"),
    22: (0.6, "스케일링 알림으로 성립 (Reminder 라인)"),
    23: (0.6, "빙하 투어 입장권으로 실재 (Ticket 라인)"),
    24: (0.6, "불소 도포 청구서로 성립 (Bill 라인)"),
    35: (0.6, "사막 투어 계획으로 성립 (Plan 라인)"),
    44: (0.6, "약제 세미나로 실재 (Seminar 라인)"),
    48: (0.6, "묘지 안내 전단으로 실재 (Flyer 라인)"),
    49: (0.6, "프랜차이즈 창업 교육으로 실재 (Tutorial 라인)"),
    50: (0.6, "퇴원 핸드북으로 실재 (Handbook 라인)"),
    51: (0.6, "X-ray 촬영 일정표로 성립 (Timetable 라인)"),
    54: (0.6, "웰니스 세미나로 실재 (Seminar 라인)"),
    58: (0.6, "수선 서비스 전단으로 실재 (Flyer 라인)"),
    60: (0.6, "문법 교육으로 실재 (Tutorial 라인)"),
    62: (0.6, "고객 촬영 일정표로 성립 (Timetable 라인)"),
    64: (0.6, "마감 실무 세미나로 성립 (Seminar 라인)"),
    68: (0.6, "아코디언 레슨 전단으로 실재 (Flyer 라인)"),
    77: (0.6, "제과 상담 예약으로 성립 (Appointment 라인)"),
    80: (0.6, "에스프레소 교육으로 실재 (Tutorial 라인)"),
    81: (0.6, "식이 핸드북으로 실재 (Handbook 라인)"),
    82: (0.6, "교정 조정 일정표로 성립 (Timetable 라인)"),
    84: (0.6, "스파 추천 콘텐츠로 실재 (Recommendation 라인)"),
    86: (0.6, "와이너리 숙박 체험으로 실재 (Retreat 여가)"),
    88: (0.6, "질병 안내 전단으로 실재 (Flyer 라인)"),
    92: (0.6, "칵테일 바 지도로 실재 (Map 물리 코스)"),
    103: (0.6, "수변 상태 모니터링으로 성립 (Monitor 라인)"),
    104: (0.6, "스시 음식 저널로 성립 (Journal 라인)"),
    106: (0.6, "보드워크 상점 디렉터리로 성립 (Directory 라인)"),
    107: (0.6, "타코 축제 부스로 실재 (Booth 공간)"),
    114: (0.6, "치과 진료 보고서로 성립 (Report 라인)"),
    118: (0.6, "치위 진료 이력으로 성립 (History 라인)"),
    121: (0.6, "라군 관측 요약으로 성립 (Summary 라인)"),
    123: (0.6, "빙하 투어 견적으로 성립 (Estimate 라인)"),
    124: (0.6, "불소 도포 영수증으로 성립 (Receipt 라인)"),
    125: (0.6, "화산 투어 목록으로 성립 (List 라인)"),
    140: (0.6, "식품 위생 실무 교육으로 실재 (Tutorial 라인)"),
    143: (0.6, "접종 권고 콘텐츠로 성립 (Recommendation 라인)"),
    144: (0.6, "돌봄 교육 세미나로 성립 (Seminar 라인)"),
    148: (0.6, "요금 안내 전단으로 실재 (Flyer 라인)"),
    149: (0.6, "감정 평가 교육으로 실재 (Tutorial 라인)"),
    150: (0.6, "프랜차이즈 핸드북으로 실재 (Handbook 라인)"),
    152: (0.6, "방사선 판독 소견으로 성립 (Opinion 라인)"),
    154: (0.6, "발달 육아 강좌로 실재 (Seminar 라인)"),
    160: (0.6, "잠금 시공 실무 교육으로 실재 (Tutorial 라인)"),
    161: (0.6, "문법 핸드북으로 실재 (Handbook 라인)"),
    164: (0.6, "케이크 추천 콘텐츠로 성립 (Recommendation 라인)"),
    168: (0.6, "로드트립 안내 전단으로 실재 (Flyer 라인)"),
    177: (0.6, "제과 고객 피드백으로 성립 (Feedback 라인)"),
    180: (0.6, "라디에이터 정비 교육으로 실재 (Tutorial 라인)"),
    181: (0.6, "에스프레소 핸드북으로 실재 (Handbook 라인)"),
    182: (0.6, "급식 일정표로 성립 (Timetable 라인)"),
    183: (0.6, "교정 진료 소견으로 성립 (Opinion 라인)"),
    184: (0.6, "유모차 추천 콘텐츠로 실재 (Recommendation 라인)"),
    185: (0.6, "스파 세미나로 실재 (Seminar 라인)"),
    188: (0.6, "반주자 모집 전단으로 실재 (Flyer 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "스테이크하우스 엔진 결합은 Engine 추상 불성립",
    2: "스마일 조수 결합은 Assistant 불명확",
    3: "수변 스케줄러 결합 불명확",
    4: "스시 플레이북 결합 불명확",
    7: "타코 계수기 결합은 Counter 다의어 불성립",
    8: "코골이 부스 결합 불성립",
    9: "해변 만 결합은 Bay 불성립",
    10: "면집 알림 결합 불명확",
    12: "전망 여권 결합은 Passport 불성립",
    13: "해산물 창 결합은 Window 다의어 불성립",
    14: "치과 순서 결합은 Roll 다의어 불성립",
    17: "패러세일링 메모 결합 불명확",
    18: "치위 뷰 결합은 View 추상 불성립",
    19: "야생동물 서류 결합은 File 다의어 불성립",
    20: "치실 갱신 결합 불성립",
    21: "라군 초안 결합은 Draft 다의어 불성립",
    25: "화산 코드 결합은 Code 불성립",
    26: "실런트 전표 결합은 Slip 다의어 불성립",
    27: "당일여행 슬롯 결합은 Slot 다의어 불성립",
    28: "치은염 배지 결합 불성립",
    29: "요트 정산 결합은 Statement 불성립",
    30: "이갈이 탭 결합은 Tab 다의어 불성립",
    31: "산책로 요약 결합은 Brief 다의어 불성립",
    32: "구취 청원 결합은 Petition 불성립",
    33: "우릴 정리 결합은 Recap 다의어 불성립",
    34: "치주염 항목 결합은 Item 다의어 불성립",
    36: "부정교합 가격 속성 결합은 Price 불성립",
    37: "와이너리 세금 결합은 Tax 불성립",
    38: "치수과 합계 결합은 Sum 다의어 불성립",
    39: "치주과 현금 결합 불성립",
    40: "진료 예약 튜토리얼 결합 불명확",
    41: "동의서 일정표 결합 불성립",
    42: "접종 소견 결합 불명확",
    43: "가족 돌봄 추천 결합 불명확",
    45: "유지보수 선물 결합 불성립 - Gift",
    46: "검수 리트리트 결합 불성립",
    47: "가격 토너먼트 결합 불성립",
    52: "세션 소견 결합 불명확",
    53: "이정표 권고 결합 불명확",
    55: "방제 일정 선물 결합 불성립 - Gift",
    56: "제설 리트리트 결합 불성립",
    57: "재고 토너먼트 결합 불성립",
    59: "카페 설문 결합은 Questionnaire 불성립",
    61: "엘리베이터 핸드북 결합 불명확",
    63: "케이크 소견 결합 불명확",
    65: "세차 선물 결합 불성립 - Gift",
    66: "배수 리트리트 결합 불성립",
    67: "로드트립 토너먼트 결합 불성립",
    69: "다이너 스코프 결합은 Scope 불성립",
    70: "비스트로 관리자 결합은 Manager 불명확",
    71: "피자집 순서 결합은 Roll 다의어 불성립",
    72: "데리 표 결합은 Table 다의어 불성립",
    73: "디저트 부채 결합 불성립",
    74: "포장 부과 결합은 Levy 불성립",
    75: "브런치 위젯 결합은 Widget 추상 불성립",
    76: "베이커리 참조 결합은 Reference 다의어 불성립",
    78: "베이글 청구 결합은 Claim 다의어 불성립",
    79: "도넛 용량 결합은 Capacity 불성립",
    83: "유모차 의견 결합 불명확",
    85: "커브 선물 결합 불성립 - Gift",
    87: "반주자 토너먼트 결합 불성립",
    89: "라떼 나침반 결합은 Compass 추상 불성립",
    90: "칫솔 대장간 결합은 Forge 추상 불성립",
    91: "스노클링 신호 결합은 Signal 추상 불성립",
    93: "치약 액자 결합은 Frame 추상 불성립",
    94: "카약 장부 결합은 Ledger 불성립",
    95: "바리스타 터미널 결합은 Terminal 불성립",
    96: "구강청격 센터 결합은 Center 불성립",
    97: "폭포 콘솔 결합은 Console 불성립",
    98: "펍 사슬 결합은 Chain 다의어 불성립",
    99: "마우스가드 링 결합은 Ring 불성립",
    100: "선셋 연결점 결합은 Nexus 추상 불성립",
    101: "스테이크하우스 조수 결합은 Assistant 불명확",
    102: "스마일 플래너 결합 불명확",
    105: "호흡 등록부 결합 불성립",
    108: "코골이 키오스크 결합은 Kiosk 불성립",
    109: "해변 게시 결합은 Post 다의어 불성립",
    110: "면집 차트 결합 불명확",
    111: "교합 상자 결합은 Bin 불성립",
    112: "전망 로비 결합은 Lobby 불성립",
    113: "해산물 순서 결합은 Roll 다의어 불성립",
    115: "배낭여행 서식 결합은 Form 다의어 불성립",
    116: "교정의 점수 결합은 Score 불성립",
    117: "패러세일링 꼬리표 결합은 Tag 다의어 불성립",
    119: "야생동물 수준 속성 결합은 Level 불성립",
    120: "치실 피드 결합은 Feed 추상 불성립",
    122: "치석 색인 결합은 Index 다의어 불성립",
    126: "실런트 샘플 결합은 Sample 다의어 불성립",
    127: "당일여행 통행 결합은 Pass 다의어 불성립",
    128: "치은염 전표 결합은 Stub 불성립",
    129: "요트 메모 결합 불성립",
    130: "이갈이 회람 결합은 Bulletin 다의어 불성립",
    131: "산책로 회람 결합은 Circular 다의어 불성립",
    132: "구취 확정 결합 불명확",
    133: "우릴 항목 결합은 Entry 다의어 불성립",
    134: "치주염 단위 결합은 Unit 다의어 불성립",
    135: "사막 비용 속성 결합은 Cost 불성립",
    136: "부정교합 요금 결합은 Fare 다의어 불성립",
    137: "와이너리 대출 결합 불성립",
    138: "치수과 부채 결합 불성립",
    139: "치주과 판매 결합은 Sale 다의어 불성립",
    141: "예약 핸드북 결합 불명확",
    142: "동의서 소견 결합 불성립",
    145: "약제 선물 결합 불성립 - Gift",
    146: "유지보수 리트리트 결합 불성립",
    147: "검수 토너먼트 결합 불성립",
    151: "퇴원 일정표 결합 불성립",
    153: "세션 추천 결합 불명확",
    155: "웰니스 선물 결합 불성립 - Gift",
    156: "방제 일정 리트리트 결합 불성립",
    157: "제설 토너먼트 결합 불성립",
    158: "재고 전단 결합 불명확",
    159: "카페 활용 속성 결합은 Utilization 불성립",
    162: "엘리베이터 일정표 결합 불성립",
    163: "고객 의견 결합 불명확",
    165: "마감 선물 결합 불성립 - Gift",
    166: "세차 리트리트 결합 불성립",
    167: "배수 토너먼트 결합 불성립",
    169: "다이너 루프 결합은 Loop 추상 불성립",
    170: "비스트로 엔진 결합은 Engine 추상 불성립",
    171: "피자집 보고 결합 불명확",
    172: "데리 전표 결합은 Slip 다의어 불성립",
    173: "디저트 기금 결합 불성립",
    174: "포장 기한 결합은 Due 다의어 불성립",
    175: "브런치 저장소 결합은 Repository 추상 불성립",
    176: "베이커리 예측 결합 불명확",
    178: "베이글 온보딩 결합 불성립",
    179: "도넛 사용 속성 결합은 Usage 불성립",
    186: "커브 리트리트 결합 불성립",
    187: "와이너리 토너먼트 결합 불성립",
    189: "라떼 등대 결합은 Beacon 추상 불성립",
    190: "칫솔 폭포 결합은 Cascade 추상 불성립",
    191: "스노클링 시계 결합은 Watch 다의어 불성립",
    192: "칵테일 액자 결합은 Frame 추상 불성립",
    193: "치약 기지 결합은 Base 추상 불성립",
    194: "카약 게시판 결합은 Board 다의어 불성립",
    195: "바리스타 센터 결합은 Center 불성립",
    196: "구강청격 존 결합은 Zone 불성립",
    197: "폭포 패널 결합은 Panel 불성립",
    198: "펍 링 결합은 Ring 불성립",
    199: "마우스가드 관문 결합은 Gate 불성립",
    200: "선셋 지도집 결합은 Atlas 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 58, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 142, len(REJECT_REASON)
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
