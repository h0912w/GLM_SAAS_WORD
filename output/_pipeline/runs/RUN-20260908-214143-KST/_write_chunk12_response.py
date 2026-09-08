import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk11_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk11_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "수변 여행 일지로 성립 (Journal 라인)"),
    7: (0.6, "보드워크 안내 부스로 실재 (Booth 실물 공간)"),
    9: (0.6, "코골이 감지 알림으로 실재 (Alert 라인)"),
    15: (0.6, "치과 검진으로 성립 (Check 라인)"),
    22: (0.6, "라군 투어 견적으로 성립 (Estimate 견적)"),
    23: (0.6, "스케일링 영수증으로 성립 (Receipt 라인)"),
    31: (0.6, "이갈이 시술 예약 확정서로 성립 (Confirmation 라인)"),
    41: (0.6, "CI/CD 파이프라인 구축 교육으로 실재 (Tutorial 라인)"),
    42: (0.6, "환불 핸드북으로 실재 (Handbook 라인)"),
    46: (0.6, "식품 규정 준수 세미나로 실재 (Seminar 라인)"),
    49: (0.6, "접종 안내 전단으로 실재 (Flyer 라인)"),
    50: (0.6, "경계 보안 교육으로 실재 (Tutorial 라인)"),
    51: (0.6, "런북 핸드북으로 실재 (Handbook 라인)"),
    55: (0.6, "감정 평가 세미나로 실재 (Seminar 라인)"),
    59: (0.6, "세션 모집 전단으로 실재 (Flyer 라인)"),
    61: (0.6, "아동 공예 교육으로 실재 (Tutorial 라인)"),
    62: (0.6, "식기세척기 핸드북으로 실재 (Handbook 라인)"),
    65: (0.6, "제습기 추천 가이드로 실재 (Recommendation 라인)"),
    70: (0.6, "웨딩케이크 안내 전단으로 실재 (Flyer 라인)"),
    82: (0.6, "편입 준비 교육으로 실재 (Tutorial 라인)"),
    91: (0.6, "유모차 안내 전단으로 실재 (Flyer 라인)"),
    94: (0.6, "스노클링 코스로 실재 (Path 물리 코스)"),
    109: (0.6, "보드워크 키오스크로 실재 (Kiosk 실물 공간)"),
    111: (0.6, "코골이 기록 차트로 성립 (Chart 라인)"),
    128: (0.6, "화산 투어 바우처로 성립 (Voucher 라인)"),
    135: (0.6, "구취 관리 계획으로 성립 (Plan 라인)"),
    143: (0.6, "보안 감사 교육으로 실재 (Tutorial 라인)"),
    144: (0.6, "파이프라인 핸드북으로 실재 (Handbook 라인)"),
    148: (0.6, "자동차 금융 설명회로 실재 (Seminar 라인)"),
    152: (0.6, "네트워크 구축 교육으로 실재 (Tutorial 라인)"),
    153: (0.6, "경계 보안 핸드북으로 실재 (Handbook 라인)"),
    157: (0.6, "조직 피드백 세미나로 실재 (Seminar 라인)"),
    161: (0.6, "X-ray 안내 전단으로 실재 (Flyer 라인)"),
    163: (0.6, "잇몸 관리 교육으로 실재 (Tutorial 라인)"),
    164: (0.6, "아동 공예 핸드북으로 실재 (Handbook 라인)"),
    167: (0.6, "흡입기 선택 가이드로 실재 (Recommendation 라인)"),
    172: (0.6, "사진 고객 모집 전단으로 실재 (Flyer 라인)"),
    181: (0.7, "제과 자격 인증 프로그램으로 실재 (Certification 도메인 실무)"),
    184: (0.6, "패티오 시공 교육으로 실재 (Tutorial 라인)"),
    185: (0.6, "편입 핸드북으로 실재 (Handbook 라인)"),
    189: (0.6, "비즈니스 네트워킹 세미나로 실재 (Seminar 라인)"),
    193: (0.6, "교정 안내 전단으로 실재 (Flyer 라인)"),
    196: (0.6, "스노클링 포인트 가이드로 실재 (Point 지점 독해)"),
    197: (0.6, "칵테일 클래스 스튜디오로 실재 (Studio 실물 공간)"),
    199: (0.6, "카약 강습 대여 센터로 실재 (Center 물리 시설)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "선셋 조수 결합은 Assistant 불명확",
    2: "스테이크하우스 등록부 결합 불성립",
    3: "스마일 운영 결합은 Ops 불성립",
    5: "스시 탐색기 결합은 Finder 불명확",
    6: "호흡 사무실 결합 불성립",
    8: "타코 명부 결합 불성립",
    10: "해변 수거함 결합은 Bin 불성립",
    11: "면집 선 결합은 Line 다의어 불성립",
    12: "교합 창 결합은 Window 다의어 불성립",
    13: "전망 리포트 결합 불성립",
    14: "해산물 시트 결합은 Sheet 다의어 불성립",
    16: "배낭여행 메모 결합은 Note 다의어 불성립",
    17: "교정의 뷰 결합은 View 추상 불성립",
    18: "패러세일링 파일 결합은 File 다의어 불성립",
    19: "치위 피드 결합은 Feed 추상 불성립",
    20: "야생동물 요약 결합 불성립",
    21: "치실 색인 결합은 Index 다의어 불성립",
    24: "빙하 목록 결합 불명확",
    25: "불소 샘플 결합은 Sample 다의어 불성립",
    26: "화산 통행 결합은 Pass 다의어 불성립",
    27: "실런트 전표 결합은 Stub 불성립",
    28: "당일여행 메모 결합은 Memo 다의어 불성립",
    29: "치은염 회람 결합은 Bulletin 다의어 불성립",
    30: "요트 회람 결합은 Circular 다의어 불성립",
    32: "산책로 항목 결합은 Entry 다의어 불성립",
    33: "구취 단위 결합은 Unit 다의어 불성립",
    34: "우릴 비용 속성 결합은 Cost 불성립",
    35: "치주염 세금 결합은 Tax 불성립",
    36: "사막 합계 결합은 Sum 다의어 불성립",
    37: "부정교합 기금 결합 불성립",
    38: "와이너리 판매 결합은 Sale 다의어 불성립",
    39: "치수과 의무 결합 불성립",
    40: "치주과 가치 결합은 Value 불성립",
    43: "추천서 일정표 결합 불명확",
    44: "안건 의견 결합 불명확",
    45: "금융 권고 결합 불명확",
    47: "예약 선물 결합 불성립 - Gift",
    48: "동의서 토너먼트 결합 불성립",
    52: "콜백 일정표 결합 불명확",
    53: "리퍼럴 의견 결합 불명확",
    54: "피드백 권고 결합 불명확",
    56: "프랜차이즈 선물 결합 불성립 - Gift",
    57: "퇴원 리트리트 결합 불성립",
    58: "X-ray 토너먼트 결합 불성립",
    60: "카페 위험 결합은 Hazard 불성립",
    63: "블로우 일정표 결합 불명확",
    64: "흡입기 소견 결합 불명확",
    66: "마감로크 세미나 결합 불명확",
    67: "문법 선물 결합 불성립 - Gift",
    68: "엘리베이터 리트리트 결합 불성립",
    69: "고객 토너먼트 결합 불성립",
    71: "다이너 지도 결합 불성립",
    72: "비스트로 동반자 결합은 Companion 불명확",
    73: "피자집 검사 결합 불명확",
    74: "데리 배지 결합 불성립",
    75: "디저트 수당 결합 불성립",
    76: "포장 벌금 결합 불성립",
    77: "브런치 녹음기 결합 불성립",
    78: "베이커리 진행 결합은 Progress 추상 불성립",
    79: "제과 예치금 결합은 Deposit 다의어 불성립",
    80: "베이글 거리 속성 결합은 Distance 불성립",
    81: "도넛 분석 결합은 Breakdown 다의어 불성립",
    83: "구 핸드북 결합 불명확 - Ward",
    84: "기사 일정표 결합 불명확",
    85: "적성 의견 결합 불명확",
    86: "네트워킹 권고 결합 불명확",
    87: "라디에이터 세미나 결합 불명확",
    88: "에스프레소 선물 결합 불성립 - Gift",
    89: "식이 리트리트 결합 불성립",
    90: "교정 토너먼트 결합 불성립",
    92: "라떼 시계 결합은 Watch 다의어 불성립",
    93: "칫솔 고리 결합은 Loop 추상 불성립",
    95: "칵테일 갑판 결합은 Deck 불성립",
    96: "치약 스튜디오 결합 불성립",
    97: "카약 터미널 결합은 Terminal 불성립",
    98: "바리스타 저울 결합은 Scale 다의어 불성립",
    99: "구강청격 경로 결합은 Route 불성립",
    100: "폭포 사슬 결합은 Chain 불성립",
    101: "펍 관리자 결합은 Manager 불명확",
    102: "마우스가드 엔진 결합은 Engine 추상 불성립",
    103: "선셋 플래너 결합 불성립",
    104: "스테이크하우스 운영 결합은 Ops 불성립",
    105: "스마일 플레이북 결합 불성립",
    106: "수변 등록부 결합 불명확",
    107: "스시 사무실 결합 불성립",
    108: "호흡 계수기 결합은 Counter 다의어 불성립",
    110: "타코 알림 결합 불명확",
    112: "해변 여권 결합은 Passport 다의어 불성립",
    113: "면집 창 결합은 Window 다의어 불성립",
    114: "교합 순서 결합은 Roll 다의어 불성립",
    115: "전망 기록 결합 불성립",
    116: "해산물 검사 결합 불명확",
    117: "치과 점수 결합은 Score 불성립",
    118: "배낭여행 태그 결합은 Tag 다의어 불성립",
    119: "교정의 이력 결합 불성립",
    120: "패러세일링 수준 속성 결합은 Level 불성립",
    121: "치위 초안 결합은 Draft 다의어 불성립",
    122: "야생동물 타임라인 결합 불성립",
    123: "치실 티켓 결합 불성립",
    124: "라군 주문 결합은 Order 다의어 불성립",
    125: "치석 코드 결합은 Code 불성립",
    126: "빙하 표 결합은 Table 다의어 불성립",
    127: "불소 슬롯 결합은 Slot 다의어 불성립",
    129: "실런트 정산 결합은 Statement 불성립",
    130: "당일여행 한도 결합은 Quota 속성어 불성립",
    131: "치은염 요약 결합은 Brief 다의어 불성립",
    132: "요트 권고 결합은 Advisory 불성립",
    133: "이갈이 정리 결합은 Recap 다의어 불성립",
    134: "산책로 요금 결합은 Fee 불성립",
    136: "우릴 가격 속성 결합은 Price 불성립",
    137: "치주염 대출 결합 불성립",
    138: "사막 부채 결합 불성립",
    139: "부정교합 현금 결합 불성립",
    140: "와이너리 청구 결합은 Charge 다의어 불성립",
    141: "치수과 수당 결합 불성립",
    142: "치주과 지분 결합은 Stake 불성립",
    145: "환불 일정표 결합 불명확",
    146: "추천서 의견 결합 불명확",
    147: "안건 권고 결합 불명확",
    149: "규정 선물 결합 불성립 - Gift",
    150: "예약 리트리트 결합 불성립",
    151: "동의서 전단 결합 불명확",
    154: "런북 일정표 결합 불명확",
    155: "콜백 의견 결합 불명확",
    156: "리퍼럴 권고 결합 불명확",
    158: "감정 선물 결합 불성립 - Gift",
    159: "프랜차이즈 리트리트 결합 불성립",
    160: "퇴원 토너먼트 결합 불성립",
    162: "카페 보증인 결합은 Guarantor 불성립",
    165: "식기세척기 일정표 결합 불명확",
    166: "블로우 소견 결합 불명확",
    168: "제습기 세미나 결합 불명확",
    169: "마감로크 선물 결합 불성립 - Gift",
    170: "문법 리트리트 결합 불성립",
    171: "엘리베이터 토너먼트 결합 불성립",
    173: "다이너 액자 결합은 Frame 불성립",
    174: "비스트로 등록부 결합 불성립",
    175: "피자집 점수 결합은 Score 불성립",
    176: "데리 전표 결합은 Stub 불성립",
    177: "디저트 관세 결합은 Tariff 불성립",
    178: "포장 마진 결합은 Markup 불성립",
    179: "브런치 견적기 결합은 Estimator 불성립",
    180: "베이커리 인가 결합은 Authorization 불성립",
    182: "베이글 범위 결합은 Range 다의어 불성립",
    183: "도넛 센서 결합은 Sensor 불성립",
    186: "구 일정표 결합 불명확 - Ward",
    187: "기사 의견 결합 불명확",
    188: "적성 권고 결합 불명확",
    190: "라디에이터 선물 결합 불성립 - Gift",
    191: "에스프레소 리트리트 결합 불성립",
    192: "식이 토너먼트 결합 불성립",
    194: "라떼 스코프 결합은 Scope 불성립",
    195: "칫솔 격자 결합은 Grid 추상 불성립",
    198: "치약 실험실 결합은 Lab 불성립",
    200: "바리스타 경로 결합은 Route 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 45, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 155, len(REJECT_REASON)
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
