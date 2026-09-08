import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk39_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk39_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    6: (0.7, "서핑 강습 교육으로 실재 (도메인 실무 개념)"),
    7: (0.6, "템포 훈련 핸드북으로 실재 (Handbook 라인)"),
    11: (0.6, "홈 스테이징 세미나로 실재 (Seminar 라인)"),
    15: (0.6, "멘토링 프로그램 안내 전단으로 실재 (Flyer 라인)"),
    60: (0.6, "이갈이 진료 워크시트로 실재 (Worksheet 라인)"),
    70: (0.6, "위협 분석 핸드북으로 실재 (Handbook 라인)"),
    78: (0.6, "통신 개통 핸드북으로 실재 (Handbook 라인)"),
    84: (0.6, "수영장 동절기 관리 핸드북으로 실재 (Handbook 라인)"),
    88: (0.6, "타악기 레슨 세미나로 실재 (Seminar 라인)"),
    101: (0.6, "수영장 유지관리 교육으로 실재 (도메인 실무 개념)"),
    102: (0.6, "서핑 강습 핸드북으로 실재 (Handbook 라인)"),
    106: (0.6, "화물 통합 운송 세미나로 실재 (Seminar 라인)"),
    110: (0.6, "방수 시공 서비스 전단으로 실재 (Flyer 라인)"),
    124: (0.6, "마우스가드 제작 견적으로 성립 (Estimate 라인 준용)"),
    125: (0.6, "일몰 투어 청구서로 성립 (Bill 라인 준용)"),
    132: (0.6, "타코집 예약 확정서로 성립 (Confirmation 라인)"),
    155: (0.6, "이갈이 도해 자료로 실재 (Diagram 라인)"),
    165: (0.7, "배차 관리 교육으로 실재 (도메인 실무 개념)"),
    169: (0.6, "인재 소싱 세미나로 실재 (Seminar 라인)"),
    172: (0.6, "수의 처방 서비스 안내 전단으로 실재 (Flyer 라인)"),
    173: (0.7, "구독 발행 관리 교육으로 실재 (도메인 실무 개념)"),
    179: (0.6, "알레르기 정보 안내 전단으로 실재 (Flyer 라인)"),
    180: (0.6, "결혼 서약 준비 교육으로 실재 (도메인 실무 개념)"),
    198: (0.6, "수영장 유지관리 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "디저트 기록기 결합은 Recorder 추상 불성립",
    2: "포장 평점 결합은 Rating 다의어 불성립",
    3: "브런치 검증 결합은 Verification 불성립",
    4: "베이커리 깊이 속성 결합은 Depth 불성립",
    5: "제과 설문 결합은 Questionnaire 불성립",
    8: "상처 드레싱 일정표 결합 불명확",
    9: "파산 소견 결합 불명확",
    10: "화물 통합 권고 결합 불명확",
    12: "보험 수익자 선물 결합 불성립 - Gift",
    13: "연공 리트리트 결합 불성립",
    14: "방수 토너먼트 결합 불성립",
    16: "베이글 릴레이 결합은 Relay 불성립",
    17: "도넛 스테이션 결합은 Station 불성립",
    18: "에스프레소 모니터 결합은 Monitor 추상 불성립",
    19: "라떼 항구 결합은 Harbor 불성립",
    20: "칫솔 알림 결합은 Alert 불성립",
    21: "스노클링 여권 결합은 Passport 다의어 불성립",
    22: "칵테일 서식 결합은 Form 다의어 불성립",
    23: "치약 카드 결합은 Card 다의어 불성립",
    24: "카약 점수 결합은 Score 불성립",
    25: "바리스타 이력 결합은 History 불성립",
    26: "구강청격 파일 결합은 File 다의어 불성립",
    27: "폭포 갱신 결합은 Update 불성립",
    28: "펍 색인 결합은 Index 다의어 불성립",
    29: "마우스가드 티켓 결합 불성립",
    30: "일몰 주문 결합은 Order 다의어 불성립",
    31: "스테이크하우스 식탁 결합은 Table 다의어 불성립",
    32: "스마일 전표 결합은 Slip 다의어 불성립",
    33: "수변 슬롯 결합은 Slot 불성립",
    34: "스시 정산 결합은 Statement 다의어 불성립",
    35: "호흡 메모 결합은 Memo 다의어 불성립",
    36: "보드워크 탭 결합은 Tab 다의어 불성립",
    37: "타코 청원 결합은 Petition 불성립",
    38: "코골이 확인 결합은 Confirmation 불명확",
    39: "해변 입장 결합은 Entry 다의어 불성립",
    40: "면집 계획 결합은 Plan 불명확",
    41: "교합 비용 속성 결합은 Cost 불성립",
    42: "전망 요금 속성 결합은 Fare 불성립",
    43: "해산물 부채 결합은 Debt 불성립",
    44: "치과 기금 결합은 Fund 불성립",
    45: "배낭여행 판매 결합은 Sale 다의어 불성립",
    46: "교정의 관세 결합은 Tariff 불성립",
    47: "패러세일링 지분 결합은 Stake 불성립",
    48: "치위 버전 결합은 Version 불성립",
    49: "야생동물 규칙 결합은 Rule 불성립",
    50: "치실 분류 결합은 Category 불성립",
    51: "라군 필드 결합은 Field 불성립",
    52: "치석 토큰 결합은 Token 불성립",
    53: "빙하 마커 결합은 Marker 불성립",
    54: "불소 자산 결합은 Asset 불성립",
    55: "화산 기한 결합은 Due 불성립",
    56: "실런트 연체 결합은 Arrears 불성립",
    57: "당일여행 벌칙 결합은 Penalty 불성립",
    58: "치은염 연장 결합은 Extension 불성립",
    59: "요트 그래프 결합은 Graph 불성립",
    61: "산책로 도식 결합 불명확",
    62: "구취 개요 결합은 Outline 불성립",
    63: "우릴 통지 결합은 Notification 불성립",
    64: "치주염 메시지 결합은 Message 불성립",
    65: "사막 위젯 결합은 Widget 불성립",
    66: "부정교합 공지 결합은 Announcement 불성립",
    67: "와이너리 변환기 결합은 Converter 추상 불성립",
    68: "치수과 기록기 결합은 Recorder 추상 불성립",
    69: "치주 탐지기 결합은 Detector 추상 불성립",
    71: "인프라 프로비저닝 일정표 결합 불명확",
    72: "대기열 소견 결합은 Queue 추상 불명확",
    73: "인재 소싱 권고 결합 불명확",
    74: "명찰 세미나 결합은 Badge 다의어 불명확",
    75: "트레이드 선물 결합은 Trade 다의어 불성립",
    76: "수의 처방 토너먼트 결합 불성립",
    77: "치료 전단 결합은 Treatment 추상 불명확",
    79: "보안 패치 일정표 결합 불명확",
    80: "설정 소견 결합은 Configuration 추상 불명확",
    81: "채팅 권고 결합은 Chat 추상 불명확",
    82: "물류 선물 결합은 Logistics 추상 불성립",
    83: "알레르기 토너먼트 결합 불성립",
    85: "차량 하부 일정표 결합 불명확",
    86: "배수관 소견 결합 불명확",
    87: "관광객 권고 결합은 Tourist 불명확",
    89: "운송 경로 토너먼트 결합은 Lane 다의어 불성립",
    90: "부동산 점검 전단 결합은 Walkthrough 다의어 불명확",
    91: "카페 결합점 결합은 Nexus 불성립",
    92: "다이너 선 결합은 Line 다의어 불성립",
    93: "비스트로 목록 결합은 List 불성립",
    94: "피자집 기금 결합은 Fund 불성립",
    95: "데리 할인 결합은 Discount 불성립",
    96: "디저트 견적기 결합은 Estimator 추상 불성립",
    97: "포장 합의 결합은 Agreement 불성립",
    98: "브런치 시뮬레이터 결합은 Simulator 추상 불성립",
    99: "베이커리 높이 속성 결합은 Height 불성립",
    100: "제과 활용도 결합은 Utilization 불성립",
    103: "템포 일정표 결합 불명확",
    104: "상처 드레싱 소견 결합 불명확",
    105: "파산 권고 결합 불명확",
    107: "홈 스테이징 선물 결합 불성립 - Gift",
    108: "보험 수익자 리트리트 결합 불성립",
    109: "연공 토너먼트 결합 불성립",
    111: "베이글 금고 결합은 Vault 불성립",
    112: "도넛 단말 결합은 Terminal 불성립",
    113: "에스프레소 동반자 결합은 Companion 추상 불성립",
    114: "라떼 명단 결합은 Roster 다의어 불성립",
    115: "칫솔 차트 결합은 Chart 불성립",
    116: "스노클링 로비 결합은 Lobby 다의어 불성립",
    117: "칵테일 카드 결합은 Card 다의어 불성립",
    118: "치약 시트 결합은 Sheet 다의어 불성립",
    119: "카약 메모 결합은 Note 다의어 불성립",
    120: "바리스타 파일 결합은 File 다의어 불성립",
    121: "구강청격 수준 속성 결합은 Level 불성립",
    122: "폭포 피드 결합은 Feed 다의어 불성립",
    123: "펍 티켓 결합 불성립",
    126: "스테이크하우스 전표 결합은 Slip 다의어 불성립",
    127: "스마일 샘플 결합은 Sample 다의어 불성립",
    128: "수변 패스 결합은 Pass 다의어 불성립",
    129: "스시 메모 결합은 Memo 다의어 불성립",
    130: "호흡 한도 결합은 Quota 불성립",
    131: "보드워크 게시물 결합은 Bulletin 다의어 불성립",
    133: "코골이 요약 결합은 Recap 불성립",
    134: "해변 요금 속성 결합은 Fee 불성립",
    135: "면집 비용 속성 결합은 Cost 불성립",
    136: "교합 가격 속성 결합은 Price 불성립",
    137: "전망 세금 결합은 Tax 불성립",
    138: "해산물 기금 결합은 Fund 불성립",
    139: "치과 현금 결합은 Cash 불성립",
    140: "배낭여행 청구 결합은 Charge 다의어 불성립",
    141: "교정의 가치 속성 결합은 Value 불성립",
    142: "패러세일링 마진 속성 결합은 Margin 불성립",
    143: "치위 링크 결합은 Link 불성립",
    144: "야생동물 세부 결합은 Detail 불성립",
    145: "치실 속성 결합은 Attribute 불성립",
    146: "라군 형식 결합은 Format 불성립",
    147: "치석 서명 결합은 Signature 불성립",
    148: "빙하 잔액 결합은 Balance 불성립",
    149: "불소 과세 결합은 Levy 불성립",
    150: "화산 보조금 결합은 Subsidy 불성립",
    151: "실런트 선수금 결합은 Advance 불성립",
    152: "당일여행 가산율 결합은 Markup 불성립",
    153: "치은염 시험 결합은 Trial 다의어 불성립",
    154: "요트 라벨 결합은 Label 불성립",
    156: "산책로 배치도 결합은 Layout 불성립",
    157: "구취 렌더링 결합은 Rendering 불성립",
    158: "우릴 키트 결합은 Kit 불성립",
    159: "치주염 총액 결합은 Total 불성립",
    160: "사막 저장소 결합은 Repository 불성립",
    161: "부정교합 계산기 결합은 Calculator 추상 불성립",
    162: "와이너리 생성기 결합은 Generator 추상 불성립",
    163: "치수과 견적기 결합은 Estimator 추상 불성립",
    164: "치주 타이머 결합은 Timer 추상 불성립",
    166: "위협 분석 일정표 결합 불명확",
    167: "인프라 프로비저닝 소견 결합 불명확",
    168: "대기열 권고 결합은 Queue 추상 불명확",
    170: "명찰 선물 결합은 Badge 다의어 불성립",
    171: "트레이드 리트리트 결합은 Trade 다의어 불성립",
    174: "통신 개통 일정표 결합 불명확",
    175: "보안 패치 소견 결합 불명확",
    176: "설정 권고 결합은 Configuration 추상 불명확",
    177: "채팅 세미나 결합은 Chat 추상 불명확",
    178: "물류 리트리트 결합은 Logistics 추상 불성립",
    181: "수영장 동절기 관리 일정표 결합 불명확",
    182: "차량 하부 소견 결합 불명확",
    183: "배수관 권고 결합 불명확",
    184: "관광객 세미나 결합은 Tourist 불명확",
    185: "타악기 선물 결합 불성립 - Gift",
    186: "운송 경로 전단 결합은 Lane 다의어 불명확",
    187: "카페 지도집 결합은 Atlas 불성립",
    188: "다이너 창 결합은 Window 다의어 불성립",
    189: "비스트로 식탁 결합은 Table 다의어 불성립",
    190: "피자집 현금 결합은 Cash 불성립",
    191: "데리 연체 결합은 Arrears 불성립",
    192: "디저트 점검기 결합은 Checker 추상 불성립",
    193: "포장 회신 결합은 Reply 불성립",
    194: "브런치 예측기 결합은 Predictor 추상 불성립",
    195: "베이커리 폭 속성 결합은 Width 불성립",
    196: "제과 혜택 결합은 Benefit 불성립",
    197: "비상 대응 교육 결합은 Panic 다의어 불명확",
    199: "서핑 일정표 결합 불명확",
    200: "템포 소견 결합 불명확",
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
assert not overlap, f"overlap={sorted(overlap)}"

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
