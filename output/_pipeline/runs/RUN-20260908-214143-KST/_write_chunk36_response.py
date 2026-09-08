import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk35_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk35_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "관수 기술 세미나로 실재 (Seminar 라인)"),
    11: (0.6, "흰개미 방제 세미나로 실재 (Seminar 라인)"),
    15: (0.6, "장례 사전계획 안내 전단으로 실재 (Flyer 라인)"),
    17: (0.6, "배상책임 보험 핸드북으로 실재 (Handbook 라인)"),
    25: (0.6, "와이파이 구축 서비스 전단으로 실재 (Flyer 라인)"),
    33: (0.6, "브런치 케이터링 견적으로 성립 (Estimate 라인 준용)"),
    36: (0.7, "방수 시공 교육으로 실재 (도메인 실무 개념)"),
    37: (0.6, "멘토링 프로그램 핸드북으로 실재 (Handbook 라인)"),
    44: (0.6, "틀니 진료 안내 전단으로 실재 (Flyer 라인)"),
    92: (0.6, "치주염 도식 학습자료로 실재 (Schematic 라인)"),
    98: (0.7, "수의 처방 실무 교육으로 실재 (도메인 실무 개념)"),
    107: (0.7, "알레르기 유발물질 관리 교육으로 실재 (도메인 실무 개념)"),
    110: (0.6, "요양 인력 운영 세미나로 실재 (Seminar 라인)"),
    135: (0.6, "연공제 이해 교육으로 실재 (도메인 실무 개념)"),
    136: (0.6, "방수 시공 핸드북으로 실재 (Handbook 라인)"),
    143: (0.6, "수의 혈액검사 안내 전단으로 실재 (Flyer 라인)"),
    148: (0.6, "스노클링 만 실물 장소로 성립 (Trail 라인 준용)"),
    159: (0.6, "미소 교정 견적으로 성립 (Estimate 라인 준용)"),
    197: (0.6, "수의 처방 실무 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "돌봄 소견 결합은 Care 추상 불성립",
    2: "방제 계약 권고 결합 불명확",
    4: "용품 공급 선물 결합 불성립 - Gift",
    5: "세탁 수거 배달 리트리트 결합 불성립",
    6: "서비스 토너먼트 결합은 Service 다의어 불성립",
    7: "제품 판매 전단 결합은 Retail 불명확",
    8: "영양 일정표 결합 불명확",
    9: "아기 낮잠 소견 결합 불명확",
    10: "요양 인력 배치 권고 결합 불명확",
    12: "잔디 깎기 선물 결합 불성립 - Gift",
    13: "객실 턴오버 리트리트 결합 불성립",
    14: "세탁 접수 토너먼트 결합 불성립",
    16: "부동산 점검 교육 결합은 Walkthrough 다의어 불명확",
    18: "급여 압류 일정표 결합 불명확",
    19: "바닥재 시공 소견 결합 불명확",
    20: "선택 과목 권고 결합은 Elective 불명확",
    21: "주민 세미나 결합은 Resident 불성립",
    22: "사진 촬영 선물 결합 불성립 - Gift",
    23: "평점 리트리트 결합은 Rating 다의어 불성립",
    24: "면접관 토너먼트 결합 불성립",
    26: "카페 콘솔 결합은 Console 추상 불성립",
    27: "다이너 게시 결합은 Post 다의어 불성립",
    28: "비스트로 타임라인 결합 불성립",
    29: "피자집 단위 결합은 Unit 다의어 불성립",
    30: "데리 토큰 결합은 Token 불성립",
    31: "디저트 메시지 결합은 Message 불성립",
    32: "포장 마감 기한 결합은 Deadline 불성립",
    34: "베이커리 무게 속성 결합은 Weight 불성립",
    35: "제과 주기 결합은 Cycle 불성립",
    38: "통행금지 일정표 결합은 Curfew 불명확",
    39: "저자 소견 결합 불명확",
    40: "공지 세미나 결합은 Notice 다의어 불성립",
    41: "배기 시스템 선물 결합 불성립 - Gift",
    42: "베이글 리트리트 결합 불성립",
    43: "수의 혈액 검사 토너먼트 결합 불성립",
    45: "도넛 프레임 결합은 Frame 불성립",
    46: "에스프레소 결합점 결합은 Nexus 불성립",
    47: "라떼 탐색기 결합은 Locator 추상 불성립",
    48: "칫솔 사무실 결합은 Office 불성립",
    49: "스노클링 키오스크 결합은 Kiosk 불성립",
    50: "칵테일 여권 결합은 Passport 다의어 불성립",
    51: "치약 로비 결합은 Lobby 다의어 불성립",
    52: "카약 창 결합은 Window 다의어 불성립",
    53: "바리스타 시트 결합은 Sheet 다의어 불성립",
    54: "구강청격 점검 결합은 Check 불성립",
    55: "폭포 태그 결합은 Tag 다의어 불성립",
    56: "펍 수준 속성 결합은 Level 불성립",
    57: "마우스가드 요율 속성 결합은 Rate 불성립",
    58: "일몰 피드 결합은 Feed 다의어 불성립",
    59: "스테이크하우스 색인 결합은 Index 다의어 불성립",
    60: "스마일 티켓 결합 불성립",
    61: "수변 주문 결합은 Order 다의어 불성립",
    62: "스시 식탁 결합은 Table 다의어 불성립",
    63: "호흡 전표 결합은 Slip 다의어 불성립",
    64: "보드워크 슬롯 결합은 Slot 불성립",
    65: "타코 정산 결합은 Statement 다의어 불성립",
    66: "코골이 메모 결합은 Memo 다의어 불성립",
    67: "해변 탭 결합은 Tab 다의어 불성립",
    68: "면집 권고 결합은 Advisory 불성립",
    69: "교합 청원 결합은 Petition 불성립",
    70: "전망 요약 결합은 Recap 불성립",
    71: "해산물 단위 결합은 Unit 다의어 불성립",
    72: "치과 의사 계획 결합은 Plan 불명확",
    73: "배낭여행 가격 속성 결합은 Price 불성립",
    74: "교정의 합계 결합은 Sum 불성립",
    75: "패러세일링 기금 결합은 Fund 불성립",
    76: "치위 의무 결합은 Duty 불성립",
    77: "야생동물 관세 결합은 Tariff 불성립",
    78: "치실 마진 속성 결합은 Margin 불성립",
    79: "라군 번호 속성 결합은 Number 불성립",
    80: "치석 규칙 결합은 Rule 불성립",
    81: "빙하 식별자 결합은 Identifier 불성립",
    82: "불소 필드 결합은 Field 불성립",
    83: "화산 일련번호 결합은 Serial 불성립",
    84: "실런트 마커 결합은 Marker 불성립",
    85: "당일여행 이자 결합은 Interest 불성립",
    86: "치은염 기한 결합은 Due 불성립",
    87: "요트 할인 결합은 Discount 불성립",
    88: "이갈이 벌칙 결합은 Penalty 불성립",
    89: "산책로 리딤 결합은 Redemption 불성립",
    90: "구취 그래프 결합은 Graph 불성립",
    91: "우릴 매뉴얼 결합 불명확",
    93: "사막 스케치 결합 불명확",
    94: "부정교합 렌더링 결합은 Rendering 불성립",
    95: "와이너리 키트 결합은 Kit 불성립",
    96: "치수과 메시지 결합은 Message 불성립",
    97: "치주 저장소 결합은 Repository 불성립",
    99: "치료 핸드북 결합은 Treatment 추상 불명확",
    100: "결제 소견 결합은 Billing 추상 불성립",
    101: "돌봄 권고 결합은 Care 추상 불성립",
    102: "방제 계약 세미나 결합 불명확",
    103: "관수 선물 결합 불성립 - Gift",
    104: "용품 공급 리트리트 결합 불성립",
    105: "세탁 수거 배달 토너먼트 결합 불성립",
    106: "서비스 전단 결합은 Service 다의어 불성립",
    108: "영양 소견 결합 불명확",
    109: "아기 낮잠 권고 결합 불명확",
    111: "흰개미 방제 선물 결합 불성립 - Gift",
    112: "잔디 깎기 리트리트 결합 불성립",
    113: "객실 턴오버 토너먼트 결합 불성립",
    114: "세탁 접수 전단 결합 불명확",
    115: "운송 경로 교육 결합은 Lane 다의어 불명확",
    116: "부동산 점검 핸드북 결합은 Walkthrough 다의어 불명확",
    117: "배상책임 일정표 결합 불명확",
    118: "급여 압류 소견 결합 불명확",
    119: "바닥재 시공 권고 결합 불명확",
    120: "선택 과목 세미나 결합은 Elective 불명확",
    121: "주민 선물 결합은 Resident 불성립",
    122: "사진 촬영 리트리트 결합 불성립",
    123: "평점 토너먼트 결합은 Rating 다의어 불성립",
    124: "면접관 전단 결합 불명확",
    125: "카페 패널 결합은 Panel 다의어 불성립",
    126: "다이너 항구 결합은 Harbor 불성립",
    127: "비스트로 알림 결합은 Reminder 불성립",
    128: "피자집 계획 결합은 Plan 불명확",
    129: "데리 서명 결합은 Signature 다의어 불성립",
    130: "디저트 총액 결합은 Total 불성립",
    131: "포장 기간 결합은 Duration 불성립",
    132: "브런치 보증 결합은 Warranty 불성립",
    133: "베이커리 거리 속성 결합은 Distance 불성립",
    134: "제과 고장 결합은 Breakdown 다의어 불성립",
    137: "멘토링 일정표 결합 불명확",
    138: "통행금지 소견 결합은 Curfew 불명확",
    139: "저자 권고 결합 불명확",
    140: "공지 선물 결합은 Notice 다의어 불성립",
    141: "배기 시스템 리트리트 결합 불성립",
    142: "베이글 토너먼트 결합 불성립",
    144: "도넛 베이스 결합은 Base 다의어 불성립",
    145: "에스프레소 지도집 결합은 Atlas 불성립",
    146: "라떼 파인더 결합은 Finder 추상 불성립",
    147: "칫솔 계수기 결합은 Counter 다의어 불성립",
    149: "칵테일 로비 결합은 Lobby 다의어 불성립",
    150: "치약 전광판 결합은 Ticker 불성립",
    151: "카약 롤 결합은 Roll 다의어 불명확",
    152: "바리스타 점검 결합은 Check 불성립",
    153: "구강청격 점수 결합은 Score 불성립",
    154: "폭포 프로필 결합은 Profile 다의어 불성립",
    155: "펍 요율 속성 결합은 Rate 불성립",
    156: "마우스가드 갱신 결합은 Update 불성립",
    157: "일몰 초안 결합은 Draft 다의어 불성립",
    158: "스테이크하우스 티켓 결합 불성립",
    160: "수변 청구 결합은 Bill 불성립",
    161: "스시 전표 결합은 Slip 다의어 불성립",
    162: "호흡 샘플 결합은 Sample 다의어 불성립",
    163: "보드워크 패스 결합은 Pass 다의어 불성립",
    164: "타코 메모 결합은 Memo 다의어 불성립",
    165: "코골이 한도 결합은 Quota 불성립",
    166: "해변 게시물 결합은 Bulletin 다의어 불성립",
    167: "면집 청원 결합은 Petition 불성립",
    168: "교합 확인 결합은 Bite 다의어 불명확",
    169: "전망 입장 결합은 Entry 다의어 불성립",
    170: "해산물 계획 결합은 Plan 불명확",
    171: "치과 비용 속성 결합은 Cost 불성립",
    172: "배낭여행 요금 속성 결합은 Fare 불성립",
    173: "교정의 부채 결합은 Debt 불성립",
    174: "패러세일링 현금 결합은 Cash 불성립",
    175: "치위 수당 결합은 Allowance 불성립",
    176: "야생동물 가치 속성 결합은 Value 불성립",
    177: "치실 벌금 결합은 Fine 불성립",
    178: "라군 버전 결합은 Version 불성립",
    179: "치석 세부 결합은 Detail 불성립",
    180: "빙하 분류 결합은 Category 불성립",
    181: "불소 형식 결합은 Format 불성립",
    182: "화산 토큰 결합은 Token 불성립",
    183: "실런트 잔액 결합은 Balance 불성립",
    184: "당일여행 자산 결합은 Asset 불성립",
    185: "치은염 보조금 결합은 Subsidy 불성립",
    186: "요트 연체 결합은 Arrears 불성립",
    187: "이갈이 가산율 결합은 Markup 불성립",
    188: "산책로 연장 결합은 Extension 불성립",
    189: "구취 라벨 결합은 Label 불성립",
    190: "우릴 워크시트 결합 불명확",
    191: "치주염 배치도 결합은 Layout 불성립",
    192: "사막 개요 결합은 Outline 불성립",
    193: "부정교합 통지 결합은 Notification 불성립",
    194: "와이너리 횟수 결합은 Count 불성립",
    195: "치수과 총액 결합은 Total 불성립",
    196: "치주 공지 결합은 Announcement 불성립",
    198: "치료 일정표 결합은 Treatment 추상 불성립",
    199: "결제 권고 결합은 Billing 추상 불성립",
    200: "돌봄 세미나 결합은 Care 추상 불성립",
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
