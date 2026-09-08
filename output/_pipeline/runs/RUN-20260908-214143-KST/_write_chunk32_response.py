import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk31_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk31_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    8: (0.6, "통역 세미나 전단으로 실재 (Seminar 연동 Flyer)"),
    9: (0.7, "면접관 교육으로 실재 (도메인 실무 개념)"),
    10: (0.6, "와이파이 설정 핸드북으로 실재 (Handbook 라인)"),
    30: (0.7, "수의 혈액 검사 교육으로 실재 (도메인 실무 개념)"),
    31: (0.6, "틀니 관리 핸드북으로 실재 (Handbook 라인)"),
    60: (0.6, "타코 식당 테이블로 성립 (Table 라인)"),
    68: (0.6, "배낭여행 예약 확정서로 성립 (Confirmation 라인)"),
    70: (0.6, "패러세일링 투어 계획으로 성립 (Plan 라인)"),
    91: (0.6, "치수과 도해 자료로 실재 (Schematic 라인)"),
    93: (0.7, "세탁 수거 배달 교육으로 실재 (도메인 실무 개념)"),
    101: (0.7, "객실 턴오버 청소 교육으로 실재 (도메인 실무 개념)"),
    102: (0.6, "세탁 접수 핸드북으로 실재 (Handbook 라인)"),
    112: (0.6, "면접관 핸드북으로 실재 (Handbook 라인)"),
    121: (0.6, "카페 클래스 스튜디오로 실재 (Studio 클래스 공간 라인)"),
    132: (0.6, "수의 혈액 검사 핸드북으로 실재 (Handbook 라인)"),
    145: (0.6, "스노클링 투어 일정으로 성립 (Calendar 라인)"),
    148: (0.6, "카약 안전 경보로 성립 (Alert 라인)"),
    190: (0.6, "부정교합 매뉴얼로 실재 (Manual 라인)"),
    195: (0.6, "세탁 수거 배달 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "일정 일정표 결합은 Schedule 추상 불성립",
    2: "처방 상담 소견 결합 불명확",
    3: "컨테이너 권고 결합 불명확",
    4: "자격 인증 세미나 결합 불명확",
    5: "매장량 선물 결합은 Reserve 다의어 불성립",
    6: "송풍기 리트리트 결합 불성립",
    7: "자물쇠 토너먼트 결합 불성립",
    11: "차량 진단 일정표 결합 불명확",
    12: "서빙 소견 결합 불명확",
    13: "구충제 권고 결합 불명확",
    14: "치실 세미나 결합 불명확",
    15: "책읽기 선물 결합 불성립 - Gift",
    16: "소파 클리닝 리트리트 결합 불성립",
    17: "컬러링 토너먼트 결합 불성립",
    18: "연고 전단 결합 불명확",
    19: "카페 데크 결합 불성립",
    20: "다이너 디렉터리 결합은 Directory 다의어 불성립",
    21: "비스트로 역사 결합 불성립",
    22: "피자집 회람 결합은 Circular 다의어 불성립",
    23: "데리 규칙 결합은 Rule 불성립",
    24: "디저트 도해 결합 불명확",
    25: "포장 비교 결합은 Comparison 불성립",
    26: "브런치 가용성 결합은 Availability 불성립",
    27: "베이커리 비용 결합은 Expense 불성립",
    28: "제과 밝기 속성 결합은 Brightness 불성립",
    29: "베이글 조율기 결합은 Tuner 불성립",
    32: "배변 훈련 일정표 결합 불명확",
    33: "헤어 커트 소견 결합 불명확",
    34: "복약 상담 권고 결합 불명확",
    35: "커패시터 세미나 결합 불명확",
    36: "스마트 도어락 선물 결합 불성립 - Gift",
    37: "클럽하우스 리트리트 결합 불성립",
    38: "스키 토너먼트 결합 불성립",
    39: "연주 곡목 전단 결합 불성립",
    40: "도넛 감시 결합은 Watch 다의어 불성립",
    41: "에스프레소 패널 결합은 Panel 추상 불성립",
    42: "라떼 동반자 결합은 Companion 불성립",
    43: "칫솔 작전 결합은 Ops 불성립",
    44: "스노클링 등록소 결합은 Registry 다의어 불성립",
    45: "칵테일 키오스크 결합은 Kiosk 불성립",
    46: "치약 만 결합은 Bay 다의어 불성립",
    47: "카약 명단 결합은 Roster 다의어 불성립",
    48: "바리스타 전광판 결합은 Ticker 불성립",
    49: "구강청격 선 결합은 Line 불성립",
    50: "폭포 리포트 결합 불성립",
    51: "펍 점수 결합은 Score 불성립",
    52: "마우스가드 메모 결합은 Note 다의어 불성립",
    53: "일몰 프로필 결합 불성립",
    54: "스테이크하우스 수준 속성 결합은 Level 불성립",
    55: "스마일 요율 속성 결합은 Rate 불성립",
    56: "수변 피드 결합은 Feed 추상 불성립",
    57: "스시 색인 결합은 Index 다의어 불성립",
    58: "호흡 티켓 결합 불성립",
    59: "보드워크 주문 결합은 Order 다의어 불성립",
    61: "코골이 전표 결합은 Slip 다의어 불성립",
    62: "해변 슬롯 결합은 Slot 다의어 불성립",
    63: "면집 전표 결합은 Stub 다의어 불성립",
    64: "교합 정산 결합은 Statement 다의어 불성립",
    65: "전망 한도 결합은 Quota 속성어 불성립",
    66: "해산물 회람 결합은 Circular 다의어 불성립",
    67: "치과 권고 결합은 Advisory 불성립",
    69: "교정의 품목 결합은 Item 다의어 불성립",
    71: "치위 세금 결합은 Tax 불성립",
    72: "야생동물 합계 결합은 Sum 불성립",
    73: "치실 현금 결합은 Cash 불성립",
    74: "라군 청구 결합은 Charge 다의어 불성립",
    75: "치석 관세 결합은 Tariff 불성립",
    76: "빙하 지분 결합은 Stake 불성립",
    77: "불소 번호 속성 결합은 Number 불성립",
    78: "화산 링크 결합은 Link 불성립",
    79: "실런트 식별자 결합은 Identifier 불성립",
    80: "당일여행 속성 결합은 Attribute 불성립",
    81: "치은염 일련번호 결합은 Serial 불성립",
    82: "요트 서명 결합은 Signature 불성립",
    83: "이갈이 이자 결합은 Interest 불성립",
    84: "산책로 과세 결합은 Levy 불성립",
    85: "구취 할인 결합은 Discount 불성립",
    86: "우릴 선수금 결합은 Advance 불성립",
    87: "치주염 상환 결합은 Redemption 불성립",
    88: "사막 시험 결합은 Trial 다의어 불성립",
    89: "부정교합 라벨 결합은 Label 불성립",
    90: "와이너리 워크시트 결합 불명확",
    92: "치주 개요 결합은 Outline 불성립",
    94: "서비스 핸드북 결합은 Service 다의어 불성립",
    95: "제품 판매 일정표 결합 불명확",
    96: "복약 순응도 소견 결합 불명확",
    97: "선석 권고 결합 불명확",
    98: "압축기 리트리트 결합 불성립",
    99: "도어 실린더 토너먼트 결합 불성립",
    100: "인화 교정쇄 전단 결합은 Proof 다의어 불성립",
    103: "장례 사전 계획 일정표 결합 불명확",
    104: "일정 소견 결합은 Schedule 추상 불성립",
    105: "처방 상담 권고 결합 불명확",
    106: "컨테이너 세미나 결합 불명확",
    107: "자격 인증 선물 결합 불성립 - Gift",
    108: "매장량 리트리트 결합은 Reserve 다의어 불성립",
    109: "송풍기 토너먼트 결합 불성립",
    110: "자물쇠 전단 결합 불명확",
    111: "평점 교육 결합은 Rating 다의어 불명확",
    113: "와이파이 일정표 결합 불명확",
    114: "차량 진단 소견 결합 불명확",
    115: "서빙 권고 결합 불명확",
    116: "구충제 세미나 결합 불명확",
    117: "치실 선물 결합 불성립 - Gift",
    118: "책읽기 리트리트 결합 불성립",
    119: "소파 클리닝 토너먼트 결합 불성립",
    120: "컬러링 전단 결합 불성립",
    122: "다이너 탐색기 결합은 Locator 불성립",
    123: "비스트로 파일 결합은 File 다의어 불성립",
    124: "피자집 권고 결합은 Advisory 불성립",
    125: "데리 세부 결합은 Detail 불성립",
    126: "디저트 배치도 결합은 Layout 불성립",
    127: "포장 제안 결합은 Proposal 불성립",
    128: "브런치 자격 결합은 Eligibility 불성립",
    129: "베이커리 뉴스레터 결합은 Newsletter 다의어 불성립",
    130: "제과 빈도 속성 결합은 Frequency 불성립",
    131: "베이글 튜토리얼 결합 불명확",
    133: "틀니 일정표 결합 불명확",
    134: "배변 훈련 소견 결합 불명확",
    135: "헤어 커트 권고 결합 불명확",
    136: "복약 상담 세미나 결합 불명확",
    137: "커패시터 선물 결합 불성립 - Gift",
    138: "스마트 도어락 리트리트 결합 불성립",
    139: "클럽하우스 토너먼트 결합 불성립",
    140: "스키 전단 결합 불명확",
    141: "도넛 범위 결합은 Scope 추상 불성립",
    142: "에스프레소 저울 결합은 Scale 다의어 불성립",
    143: "라떼 등기부 결합은 Register 다의어 불성립",
    144: "칫솔 플레이북 결합은 Playbook 전면 기각",
    146: "칵테일 만 결합은 Bay 다의어 불성립",
    147: "치약 게시물 결합은 Post 다의어 불성립",
    149: "바리스타 선 결합은 Line 불성립",
    150: "구강청격 창 결합은 Window 불성립",
    151: "폭포 기록 결합은 Log 위치 추상 불성립",
    152: "펍 메모 결합은 Note 다의어 불성립",
    153: "마우스가드 태그 결합은 Tag 다의어 불성립",
    154: "일몰 상태 결합은 Status 불성립",
    155: "스테이크하우스 요율 속성 결합은 Rate 불성립",
    156: "스마일 갱신 결합은 Update 불성립",
    157: "수변 초안 결합은 Draft 다의어 불성립",
    158: "스시 티켓 결합 불성립",
    159: "호흡 견적 결합은 Estimate 불성립",
    160: "보드워크 청구서 결합은 Bill 불성립",
    161: "타코 전표 결합은 Slip 다의어 불성립",
    162: "코골이 샘플 결합은 Sample 다의어 불성립",
    163: "해변 통행 결합은 Pass 다의어 불성립",
    164: "면집 정산 결합은 Statement 다의어 불성립",
    165: "교합 메모 결합은 Memo 다의어 불성립",
    166: "전망 탭 결합은 Tab 다의어 불성립",
    167: "해산물 권고 결합은 Advisory 불성립",
    168: "치과 청원 결합은 Petition 불성립",
    169: "배낭여행 정리 결합은 Recap 다의어 불성립",
    170: "교정의 단위 결합은 Unit 다의어 불성립",
    171: "패러세일링 비용 속성 결합은 Cost 불성립",
    172: "치위 대출 결합은 Loan 불성립",
    173: "야생동물 부채 결합은 Debt 불성립",
    174: "치실 판매 결합은 Sale 다의어 불성립",
    175: "라군 의무 결합은 Duty 불성립",
    176: "치석 가치 속성 결합은 Value 불성립",
    177: "빙하 마진 속성 결합은 Margin 불성립",
    178: "불소 버전 결합은 Version 불성립",
    179: "화산 규칙 결합은 Rule 불성립",
    180: "실런트 분류 결합은 Category 불성립",
    181: "당일여행 필드 결합은 Field 불성립",
    182: "치은염 토큰 결합은 Token 불성립",
    183: "요트 마커 결합은 Marker 불성립",
    184: "이갈이 자산 결합은 Asset 불성립",
    185: "산책로 기한 결합은 Due 불성립",
    186: "구취 연체 결합은 Arrears 불성립",
    187: "우릴 벌칙 결합은 Penalty 불성립",
    188: "치주염 연장 결합은 Extension 불성립",
    189: "사막 그래프 결합은 Graph 불성립",
    191: "와이너리 도해 결합 불명확",
    192: "치수과 배치도 결합은 Layout 불성립",
    193: "치주 렌더링 결합은 Rendering 불성립",
    194: "용품 공급 교육 결합은 Supply 추상 불명확",
    196: "서비스 일정표 결합은 Service 다의어 불성립",
    197: "제품 판매 소견 결합 불명확",
    198: "복약 순응도 권고 결합 불명확",
    199: "선석 세미나 결합 불명확",
    200: "압축기 토너먼트 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 19, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 181, len(REJECT_REASON)
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
