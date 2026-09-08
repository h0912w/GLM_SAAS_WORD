import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk14_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk14_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "네트워킹 세미나 전단으로 실재 (Flyer 라인)"),
    16: (0.6, "스테이크하우스 목록으로 성립 (Directory 라인)"),
    21: (0.6, "보드워크 안전 알림으로 실재 (Alert 라인)"),
    38: (0.6, "빙하 투어 바우처로 성립 (Voucher 라인)"),
    45: (0.6, "이갈이 관리 계획으로 성립 (Plan 라인)"),
    56: (0.6, "광고 소재 핸드북으로 실재 (Handbook 라인)"),
    59: (0.6, "로밍 요금제 추천 가이드로 실재 (Recommendation 라인)"),
    60: (0.6, "보안 감사 세미나로 실재 (Seminar 라인)"),
    65: (0.6, "비영리 장부 관리 교육으로 성립 (Ledger 실재 장부)"),
    66: (0.6, "투표 핸드북으로 실재 (Handbook 라인)"),
    70: (0.6, "네트워크 세미나로 실재 (Seminar 라인)"),
    74: (0.6, "리퍼럴 프로그램 안내 전단으로 실재 (Flyer 라인)"),
    75: (0.6, "채용 담당자 교육으로 실재 (Tutorial 라인)"),
    79: (0.6, "진드기 예방약 추천 가이드로 실재 (Recommendation 라인)"),
    80: (0.6, "잇몸 관리 세미나로 실재 (Seminar 라인)"),
    84: (0.6, "흡입기 안내 전단으로 실재 (Flyer 라인)"),
    96: (0.6, "채권 관리 교육으로 실재 (Tutorial 라인)"),
    97: (0.6, "냉장 컨테이너 핸드북으로 실재 (Handbook 라인)"),
    105: (0.6, "적성 검사 모집 전단으로 실재 (Flyer 라인)"),
    124: (0.6, "보드워크 안내 차트로 성립 (Chart 라인)"),
    129: (0.6, "교합 점검으로 실재 (Check 라인)"),
    136: (0.6, "치과 치료 견적으로 성립 (Estimate 견적)"),
    137: (0.6, "사파리 투어 청구서로 성립 (Bill 라인)"),
    158: (0.6, "기부 약정 교육으로 실재 (Tutorial 라인)"),
    167: (0.6, "추천서 세미나 모집 전단으로 실재 (Flyer 라인)"),
    168: (0.6, "비영리 회계 핸드북으로 성립 (Ledger 실재 장부)"),
    177: (0.6, "고객 감정 분석 교육으로 실재 (Tutorial 라인)"),
    178: (0.6, "채용 담당자 핸드북으로 실재 (Handbook 라인)"),
    186: (0.6, "블로우 서비스 전단으로 실재 (Flyer 라인)"),
    188: (0.6, "비스트로 목록으로 성립 (Directory 라인)"),
    192: (0.6, "포장 운영 매뉴얼로 실재 (Manual 라인)"),
    198: (0.6, "부상 처치 교육으로 실재 (Tutorial 라인)"),
    199: (0.6, "채권자 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "적성 토너먼트 결합 불성립",
    3: "에스프레소 흐름 결합은 Flow 추상 불성립",
    4: "라떼 경로 결합은 Path 불성립",
    5: "칫솔 지도 결합은 Map 불성립",
    6: "스노클링 핵심 결합은 Core 추상 불성립",
    7: "칵테일 센터 결합은 Center 불성립",
    8: "치약 구역 결합은 Zone 불성립",
    9: "카약 패널 결합은 Panel 불성립",
    10: "바리스타 고리 결합은 Ring 불성립",
    11: "구강청격 문 결합은 Gate 불성립",
    12: "폭포 관리인 결합은 Keeper 불성립",
    13: "펍 모니터 결합 불성립",
    14: "마우스가드 동반자 결합은 Companion 불명확",
    15: "선셋 운영 결합은 Ops 불성립",
    17: "스마일 탐색기 결합은 Locator 불성립",
    18: "수변 사무실 결합 불성립",
    19: "스시 게시 결합은 Post 다의어 불성립",
    20: "호흡 항구 결합은 Harbor 불성립",
    22: "타코 전광판 결합은 Ticker 불성립",
    23: "코골이 선 결합은 Line 다의어 불성립",
    24: "해변 순서 결합은 Roll 다의어 불성립",
    25: "면집 카드 결합은 Card 다의어 불성립",
    26: "교합 시트 결합은 Sheet 다의어 불성립",
    27: "전망 점수 결합은 Score 불성립",
    28: "해산물 상태 결합은 Status 불성립",
    29: "치과 뷰 결합은 View 추상 불성립",
    30: "배낭여행 파일 결합은 File 다의어 불성립",
    31: "교정의 피드 결합은 Feed 추상 불성립",
    32: "패러세일링 요약 결합 불성립",
    33: "치위 티켓 결합 불성립",
    34: "야생동물 주문 결합은 Order 다의어 불성립",
    35: "치실 코드 결합은 Code 불성립",
    36: "라군 표 결합은 Table 다의어 불성립",
    37: "치석 슬롯 결합은 Slot 다의어 불성립",
    39: "불소 정산 결합은 Statement 불성립",
    40: "화산 한도 결합은 Quota 속성어 불성립",
    41: "실런트 요약 결합은 Brief 다의어 불성립",
    42: "당일여행 권고 결합은 Advisory 불성립",
    43: "치은염 정리 결합은 Recap 다의어 불성립",
    44: "요트 요금 결합은 Fee 불성립",
    46: "산책로 가격 속성 결합은 Price 불성립",
    47: "구취 대출 결합 불성립",
    48: "우릴 부채 결합 불성립",
    49: "치주염 판매 결합은 Sale 다의어 불성립",
    50: "사막 의무 결합 불성립",
    51: "부정교합 관세 결합은 Tariff 불성립",
    52: "와이너리 지분 결합은 Stake 불성립",
    53: "치수과 벌금 결합은 Fine 불성립",
    54: "치주과 링크 결합은 Link 불성립",
    55: "공청회 튜토리얼 결합은 Hearing 다의어 불명확",
    57: "아카이브 일정표 결합 불명확",
    58: "운전 소견 결합 불명확",
    61: "파이프라인 선물 결합 불성립 - Gift",
    62: "환불 리트리트 결합 불성립",
    63: "추천서 토너먼트 결합 불성립",
    64: "안건 전단 결합 불명확",
    67: "배치 일정표 결합 불명확",
    68: "피드 소견 결합 불명확",
    69: "허가 권고 결합 불명확",
    71: "경계 선물 결합 불성립 - Gift",
    72: "런북 리트리트 결합 불성립",
    73: "콜백 토너먼트 결합 불성립",
    76: "랜야드 핸드북 결합 불명확",
    77: "점검 일정표 결합 불명확",
    78: "카페 소견 결합 불명확",
    81: "공예 선물 결합 불성립 - Gift",
    82: "식기세척기 리트리트 결합 불성립",
    83: "블로우 토너먼트 결합 불성립",
    85: "다이너 갑판 결합은 Deck 불성립",
    86: "비스트로 캘린더 결합 불명확",
    87: "피자집 뷰 결합은 View 추상 불성립",
    88: "데리 회람 결합은 Bulletin 다의어 불성립",
    89: "디저트 번호 속성 결합은 Number 불성립",
    90: "포장 라벨 결합은 Label 다의어 불성립",
    91: "브런치 수호자 결합은 Guardian 불성립",
    92: "베이커리 답장 결합은 Reply 불성립",
    93: "제과 검증 결합은 Verification 불성립",
    94: "베이글 속도 속성 결합은 Speed 불성립",
    95: "도넛 평가 결합 불성립",
    98: "리모델링 일정표 결합 불명확",
    99: "보험 조정 소견 결합 불명확",
    100: "교육 권고 결합 불명확",
    101: "패티오 세미나 결합 불명확",
    102: "편입 선물 결합 불성립 - Gift",
    103: "구 리트리트 결합 불성립 - Ward",
    104: "기사 토너먼트 결합 불성립",
    106: "에스프레소 허브 결합은 Hub 불성립",
    107: "라떼 지점 결합은 Point 불성립",
    108: "칫솔 액자 결합은 Frame 불성립",
    109: "스노클링 장부 결합은 Ledger 불성립",
    110: "칵테일 구역 결합은 Zone 불성립",
    111: "치약 포털 결합은 Portal 불성립",
    112: "카약 저울 결합은 Scale 다의어 불성립",
    113: "바리스타 문 결합은 Gate 불성립",
    114: "구강청격 연결점 결합은 Nexus 불성립",
    115: "폭포 관리자 결합은 Manager 불성립",
    116: "펍 동반자 결합은 Companion 불명확",
    117: "마우스가드 등록부 결합 불성립",
    118: "선셋 플레이북 결합 불성립",
    119: "스테이크하우스 탐색기 결합은 Locator 불성립",
    120: "스마일 탐색기 결합은 Finder 불성립",
    121: "수변 계수기 결합은 Counter 다의어 불성립",
    122: "스시 항구 결합은 Harbor 불성립",
    123: "호흡 명부 결합은 Roster 불성립",
    125: "타코 선 결합은 Line 다의어 불성립",
    126: "코골이 창 결합은 Window 다의어 불성립",
    127: "해변 리포트 결합 불성립",
    128: "면집 시트 결합은 Sheet 다의어 불성립",
    130: "전망 메모 결합은 Note 다의어 불성립",
    131: "해산물 뷰 결합은 View 추상 불성립",
    132: "치과 이력 결합 불성립",
    133: "배낭여행 수준 속성 결합은 Level 불성립",
    134: "교정의 초안 결합은 Draft 다의어 불성립",
    135: "패러세일링 타임라인 결합 불성립",
    138: "치실 목록 결합 불명확",
    139: "라군 전표 결합은 Slip 다의어 불성립",
    140: "치석 통행 결합은 Pass 다의어 불성립",
    141: "빙하 배지 결합 불성립",
    142: "불소 메모 결합은 Memo 다의어 불성립",
    143: "화산 탭 결합은 Tab 다의어 불성립",
    144: "실런트 회람 결합은 Circular 다의어 불성립",
    145: "당일여행 청원 결합은 Petition 불성립",
    146: "치은염 항목 결합은 Entry 다의어 불성립",
    147: "요트 항목 결합은 Item 다의어 불성립",
    148: "이갈이 비용 속성 결합은 Cost 불성립",
    149: "산책로 요금 결합은 Fare 다의어 불성립",
    150: "구취 합계 결합은 Sum 다의어 불성립",
    151: "우릴 기금 결합 불성립",
    152: "치주염 청구 결합은 Charge 다의어 불성립",
    153: "사막 수당 결합 불성립",
    154: "부정교합 가치 결합은 Value 불성립",
    155: "와이너리 마진 속성 결합은 Margin 불성립",
    156: "치수과 번호 속성 결합은 Number 불성립",
    157: "치주과 규칙 결합은 Rule 불성립",
    159: "공청회 핸드북 결합은 Hearing 다의어 불명확",
    160: "소재 일정표 결합 불명확",
    161: "아카이브 소견 결합 불명확",
    162: "운전 권고 결합 불명확",
    163: "로밍 세미나 결합 불명확",
    164: "감사 선물 결합 불성립 - Gift",
    165: "파이프라인 리트리트 결합 불성립",
    166: "환불 토너먼트 결합 불성립",
    169: "투표 일정표 결합 불명확",
    170: "배치 소견 결합 불명확",
    171: "피드 권고 결합 불명확",
    172: "허가 세미나 결합 불명확",
    173: "네트워크 선물 결합 불성립 - Gift",
    174: "경계 리트리트 결합 불성립",
    175: "런북 토너먼트 결합 불성립",
    176: "콜백 전단 결합 불명확",
    179: "랜야드 일정표 결합 불명확",
    180: "점검 소견 결합 불명확",
    181: "카페 추천 결합 불명확",
    182: "진드기 세미나 결합 불명확",
    183: "잇몸 선물 결합 불성립 - Gift",
    184: "공예 리트리트 결합 불성립",
    185: "식기세척기 토너먼트 결합 불성립",
    187: "다이너 스튜디오 결합 불성립",
    189: "피자집 이력 결합 불성립",
    190: "데리 요약 결합은 Brief 다의어 불성립",
    191: "디저트 버전 결합은 Version 불성립",
    193: "브런치 조수 결합은 Helper 불성립",
    194: "베이커리 계정 결합은 Account 다의어 불성립",
    195: "제과 시뮬레이터 결합은 Simulator 불성립",
    196: "베이글 깊이 속성 결합은 Depth 불성립",
    197: "도넛 설문지 결합은 Questionnaire 불성립",
    200: "냉장 컨테이너 일정표 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 33, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 167, len(REJECT_REASON)
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
