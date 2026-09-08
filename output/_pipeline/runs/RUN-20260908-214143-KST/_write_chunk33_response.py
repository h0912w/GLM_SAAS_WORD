import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk32_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk32_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "객실 턴오버 핸드북으로 실재 (Handbook 라인)"),
    12: (0.7, "사진 촬영 교육으로 실재 (도메인 실무 개념)"),
    30: (0.6, "제과점 재고 관리로 실재 (재고 관리 실무 독해)"),
    32: (0.7, "배기 시스템 점검 교육으로 실재 (도메인 실무 개념)"),
    49: (0.6, "카약 항해 차트로 실재 (Chart 실재 기록 라인)"),
    59: (0.6, "초밥 케이터링 견적으로 성립 (Estimate 라인)"),
    69: (0.6, "치과 예약 확정서로 성립 (Confirmation 라인)"),
    71: (0.6, "교정 치료 계획으로 성립 (Plan 라인)"),
    91: (0.6, "부정교합 실무 워크시트로 실재 (Worksheet 라인)"),
    93: (0.6, "치수과 스케치 자료로 실재 (Sketch 라인)"),
    95: (0.7, "관수 시스템 교육으로 실재 (도메인 실무 개념)"),
    103: (0.7, "흰개미 방제 교육으로 실재 (도메인 실무 개념)"),
    114: (0.6, "사진 촬영 핸드북으로 실재 (Handbook 라인)"),
    126: (0.6, "피자집 예약 확정서로 성립 (Confirmation 라인)"),
    134: (0.6, "배기 시스템 핸드북으로 실재 (Handbook 라인)"),
    169: (0.6, "해산물 식당 예약 확정서로 성립 (Confirmation 라인)"),
    192: (0.6, "부정교합 도해 자료로 실재 (Diagram 라인)"),
    196: (0.7, "방제 계약 절차 교육으로 실재 (도메인 실무 개념)"),
    197: (0.6, "관수 시스템 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "도어 실린더 전단 결합 불명확",
    2: "잔디 깎기 교육 결합 불명확",
    4: "세탁 접수 일정표 결합 불명확",
    5: "장례 사전 계획 소견 결합 불명확",
    6: "일정 권고 결합은 Schedule 추상 불성립",
    7: "처방 상담 세미나 결합 불명확",
    8: "컨테이너 선물 결합 불성립 - Gift",
    9: "자격 인증 리트리트 결합 불성립",
    10: "매장량 토너먼트 결합은 Reserve 다의어 불성립",
    11: "송풍기 전단 결합 불명확",
    13: "평점 핸드북 결합은 Rating 다의어 불명확",
    14: "면접관 일정표 결합 불명확",
    15: "와이파이 소견 결합 불명확",
    16: "차량 진단 권고 결합 불명확",
    17: "서빙 세미나 결합 불명확",
    18: "구충제 선물 결합 불성립 - Gift",
    19: "치실 리트리트 결합 불성립",
    20: "책읽기 토너먼트 결합 불성립",
    21: "소파 클리닝 전단 결합 불명확",
    22: "카페 실험실 결합은 Lab 다의어 불성립",
    23: "다이너 탐색기 결합은 Finder 불성립",
    24: "비스트로 수준 속성 결합은 Level 불성립",
    25: "피자집 청원 결합은 Petition 불성립",
    26: "데리 식별자 결합은 Identifier 불성립",
    27: "디저트 스케치 결합 불명확",
    28: "포장 보증 결합은 Guarantee 불성립",
    29: "브런치 방송 결합은 Broadcast 불성립",
    31: "제과 호환성 결합은 Compatibility 불성립",
    33: "베이글 핸드북 결합 불명확",
    34: "수의 혈액 검사 일정표 결합 불명확",
    35: "틀니 소견 결합 불명확",
    36: "배변 훈련 권고 결합 불명확",
    37: "헤어 커트 세미나 결합 불명확",
    38: "복약 상담 선물 결합 불성립 - Gift",
    39: "커패시터 리트리트 결합 불성립",
    40: "스마트 도어락 토너먼트 결합 불성립",
    41: "클럽하우스 전단 결합 불명확",
    42: "도넛 고리 결합은 Loop 추상 불성립",
    43: "에스프레소 경로 결합은 Route 추상 불성립",
    44: "라떼 작전 결합은 Ops 불성립",
    45: "칫솔 일지 결합은 Journal 다의어 불성립",
    46: "스노클링 디렉터리 결합은 Directory 다의어 불성립",
    47: "칵테일 게시물 결합은 Post 다의어 불성립",
    48: "치약 만 결합은 Harbor 다의어 불성립",
    50: "바리스타 창 결합은 Window 불성립",
    51: "구강청격 롤 결합은 Roll 다의어 불성립",
    52: "폭포 서식 결합은 Form 다의어 불성립",
    53: "펍 태그 결합은 Tag 다의어 불성립",
    54: "마우스가드 프로필 결합 불성립",
    55: "일몰 뷰 결합은 View 추상 불성립",
    56: "스테이크하우스 갱신 결합은 Update 불성립",
    57: "스마일 피드 결합은 Feed 추상 불성립",
    58: "수변 요약 결합은 Summary 불성립",
    60: "호흡 주문 결합은 Order 다의어 불성립",
    61: "보드워크 영수증 결합 불성립",
    62: "타코 샘플 결합은 Sample 다의어 불성립",
    63: "코골이 슬롯 결합은 Slot 다의어 불성립",
    64: "해변 바우처 결합 불명확",
    65: "면집 메모 결합은 Memo 다의어 불성립",
    66: "교합 한도 결합은 Quota 속성어 불성립",
    67: "전망 회람 결합은 Bulletin 다의어 불성립",
    68: "해산물 청원 결합은 Petition 불성립",
    70: "배낭여행 입장 결합은 Entry 다의어 불성립",
    72: "패러세일링 가격 속성 결합은 Price 불성립",
    73: "치위 합계 결합은 Sum 불성립",
    74: "야생동물 기금 결합은 Fund 불성립",
    75: "치실 청구 결합은 Charge 다의어 불성립",
    76: "라군 수당 결합은 Allowance 불성립",
    77: "치석 지분 결합은 Stake 불성립",
    78: "빙하 벌금 결합은 Fine 불성립",
    79: "불소 링크 결합은 Link 불성립",
    80: "화산 세부 결합은 Detail 불성립",
    81: "실런트 속성 결합은 Attribute 불성립",
    82: "당일여행 형식 결합은 Format 불성립",
    83: "치은염 서명 결합은 Signature 불성립",
    84: "요트 잔액 결합은 Balance 불성립",
    85: "이갈이 과세 결합은 Levy 불성립",
    86: "산책로 보조금 결합은 Subsidy 불성립",
    87: "구취 선수금 결합은 Advance 불성립",
    88: "우릴 가산율 결합은 Markup 불성립",
    89: "치주염 시험 결합은 Trial 다의어 불성립",
    90: "사막 라벨 결합은 Label 불성립",
    92: "와이너리 도해 결합 불명확",
    94: "치주 통지 결합은 Notification 불성립",
    96: "용품 공급 핸드북 결합은 Supply 추상 불성립",
    97: "세탁 수거 배달 일정표 결합 불명확",
    98: "서비스 소견 결합은 Service 다의어 불성립",
    99: "제품 판매 권고 결합 불명확",
    100: "복약 순응도 세미나 결합 불명확",
    101: "선석 선물 결합 불성립 - Gift",
    102: "압축기 전단 결합 불명확",
    104: "잔디 깎기 핸드북 결합 불명확",
    105: "객실 턴오버 일정표 결합 불명확",
    106: "세탁 접수 소견 결합 불명확",
    107: "장례 사전 계획 권고 결합 불명확",
    108: "일정 세미나 결합은 Schedule 추상 불성립",
    109: "처방 상담 선물 결합 불성립 - Gift",
    110: "컨테이너 리트리트 결합 불성립",
    111: "자격 인증 토너먼트 결합 불성립",
    112: "매장량 전단 결합은 Reserve 다의어 불성립",
    113: "거주민 교육 결합은 Resident 불명확",
    115: "평점 일정표 결합은 Rating 다의어 불명확",
    116: "면접관 소견 결합 불명확",
    117: "와이파이 권고 결합 불명확",
    118: "차량 진단 세미나 결합 불명확",
    119: "서빙 선물 결합 불성립 - Gift",
    120: "구충제 리트리트 결합 불성립",
    121: "치실 토너먼트 결합 불성립",
    122: "책읽기 전단 결합 불명확",
    123: "카페 스테이션 결합은 Station 불성립",
    124: "다이너 사무실 결합은 Office 불성립",
    125: "비스트로 요율 속성 결합은 Rate 불성립",
    127: "데리 분류 결합은 Category 불성립",
    128: "디저트 개요 결합은 Outline 불성립",
    129: "포장 기록 결합은 Record 불성립",
    130: "브런치 바코드 결합은 Barcode 불성립",
    131: "베이커리 청구 결합은 Claim 다의어 불성립",
    132: "제과 용량 속성 결합은 Capacity 불성립",
    133: "공지 교육 결합은 Notice 다의어 불명확",
    135: "베이글 일정표 결합 불명확",
    136: "수의 혈액 검사 소견 결합 불명확",
    137: "틀니 권고 결합 불명확",
    138: "배변 훈련 세미나 결합 불명확",
    139: "헤어 커트 선물 결합 불성립 - Gift",
    140: "복약 상담 리트리트 결합 불성립",
    141: "커패시터 토너먼트 결합 불성립",
    142: "스마트 도어락 전단 결합 불명확",
    143: "도넛 격자 결합은 Grid 불성립",
    144: "에스프레소 레일 결합은 Rail 불성립",
    145: "라떼 플레이북 결합은 Playbook 전면 기각",
    146: "칫솔 등록소 결합은 Registry 다의어 불성립",
    147: "스노클링 탐색기 결합은 Locator 불성립",
    148: "칵테일 만 결합은 Harbor 다의어 불성립",
    149: "치약 명단 결합은 Roster 다의어 불성립",
    150: "카약 창고 결합은 Bin 다의어 불성립",
    151: "바리스타 롤 결합은 Roll 다의어 불성립",
    152: "구강청격 리포트 결합 불성립",
    153: "폭포 카드 결합은 Card 다의어 불성립",
    154: "펍 프로필 결합 불성립",
    155: "마우스가드 상태 결합은 Status 불성립",
    156: "일몰 역사 결합 불성립",
    157: "스테이크하우스 피드 결합은 Feed 추상 불성립",
    158: "스마일 초안 결합은 Draft 다의어 불성립",
    159: "수변 타임라인 결합 불성립",
    160: "스시 주문 결합은 Order 다의어 불성립",
    161: "호흡 청구서 결합은 Bill 불성립",
    162: "보드워크 코드 결합은 Code 불성립",
    163: "타코 슬롯 결합은 Slot 다의어 불성립",
    164: "코골이 통행 결합은 Pass 다의어 불성립",
    165: "해변 배지 결합은 Badge 다의어 불성립",
    166: "면집 한도 결합은 Quota 속성어 불성립",
    167: "교합 탭 결합은 Tab 다의어 불성립",
    168: "전망 요약 결합은 Brief 다의어 불성립",
    170: "치과 정리 결합은 Recap 다의어 불성립",
    171: "배낭여행 요금 속성 결합은 Fee 불성립",
    172: "교정의 비용 속성 결합은 Cost 불성립",
    173: "패러세일링 운임 속성 결합은 Fare 불성립",
    174: "치위 부채 결합은 Debt 불성립",
    175: "야생동물 현금 결합은 Cash 불성립",
    176: "치실 의무 결합은 Duty 불성립",
    177: "라군 관세 결합은 Tariff 불성립",
    178: "치석 마진 속성 결합은 Margin 불성립",
    179: "빙하 번호 속성 결합은 Number 불성립",
    180: "불소 규칙 결합은 Rule 불성립",
    181: "화산 식별자 결합은 Identifier 불성립",
    182: "실런트 필드 결합은 Field 불성립",
    183: "당일여행 일련번호 결합은 Serial 불성립",
    184: "치은염 마커 결합은 Marker 불성립",
    185: "요트 이자 결합은 Interest 불성립",
    186: "이갈이 기한 결합은 Due 불성립",
    187: "산책로 할인 결합은 Discount 불성립",
    188: "구취 벌칙 결합은 Penalty 불성립",
    189: "우릴 상환 결합은 Redemption 불성립",
    190: "치주염 그래프 결합은 Graph 불성립",
    191: "사막 매뉴얼 결합 불명확",
    193: "와이너리 배치도 결합은 Layout 불성립",
    194: "치수과 개요 결합은 Outline 불성립",
    195: "치주 키트 결합은 Kit 불성립",
    198: "용품 공급 일정표 결합은 Supply 추상 불성립",
    199: "세탁 수거 배달 소견 결합 불명확",
    200: "서비스 권고 결합은 Service 다의어 불성립",
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
