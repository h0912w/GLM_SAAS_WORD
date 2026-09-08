import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk37_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk37_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    5: (0.6, "흰개미 방제 서비스 전단으로 실재 (Flyer 라인)"),
    6: (0.7, "타악기 레슨 교육으로 실재 (도메인 실무 개념)"),
    9: (0.6, "배상책임 보험 세미나로 실재 (Seminar 라인)"),
    16: (0.6, "비스트로 케이터링 견적으로 성립 (Estimate 라인 준용)"),
    24: (0.7, "화물 통합 운송 교육으로 실재 (도메인 실무 개념)"),
    25: (0.6, "홈 스테이징 핸드북으로 실재 (Handbook 라인)"),
    29: (0.6, "멘토링 세미나로 실재 (Seminar 라인)"),
    48: (0.6, "스테이크하우스 청구서로 성립 (Bill 라인)"),
    79: (0.6, "구취 도해 자료로 실재 (Diagram 라인)"),
    87: (0.7, "인재 소싱 교육으로 실재 (도메인 실무 개념)"),
    100: (0.6, "요양 인력 파견 서비스 전단으로 실재 (Flyer 라인)"),
    102: (0.6, "타악기 레슨 핸드북으로 실재 (Handbook 라인)"),
    109: (0.6, "카페 탐방 코스로 성립 (Trail 라인 준용)"),
    119: (0.7, "파산 절차 교육으로 실재 (도메인 실무 개념)"),
    120: (0.6, "화물 통합 운송 핸드북으로 실재 (Handbook 라인)"),
    124: (0.6, "방수 시공 세미나로 실재 (Seminar 라인)"),
    143: (0.6, "스테이크하우스 영수증으로 성립 (Receipt 라인)"),
    146: (0.6, "스시집 이용권으로 성립 (Voucher 라인)"),
    154: (0.6, "전망 관람 계획으로 성립 (Plan 라인)"),
    174: (0.6, "구취 도식 학습자료로 실재 (Schematic 라인)"),
    183: (0.6, "인재 소싱 핸드북으로 실재 (Handbook 라인)"),
    186: (0.6, "수의 처방 세미나로 실재 (Seminar 라인)"),
    193: (0.6, "알레르기 관리 세미나로 실재 (Seminar 라인)"),
    195: (0.6, "육아 낮잠 교육 안내 전단으로 실재 (Flyer 라인)"),
    196: (0.7, "배수관 시공 교육으로 실재 (도메인 실무 개념)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "알레르기 소견 결합 불명확",
    2: "영양 선물 결합 불성립 - Gift",
    3: "아기 낮잠 리트리트 결합 불성립",
    4: "요양 인력 배치 토너먼트 결합 불성립",
    7: "운송 경로 소견 결합은 Lane 다의어 불명확",
    8: "부동산 점검 권고 결합은 Walkthrough 다의어 불명확",
    10: "급여 압류 선물 결합 불성립 - Gift",
    11: "바닥재 시공 리트리트 결합 불성립",
    12: "선택 과목 토너먼트 결합은 Elective 불명확",
    13: "주민 전단 결합은 Resident 불성립",
    14: "카페 레일 결합은 Rail 추상 불성립",
    15: "다이너 차트 결합은 Chart 불성립",
    17: "피자집 요금 속성 결합은 Fare 불성립",
    18: "데리 이자 결합은 Interest 불성립",
    19: "디저트 공지 결합은 Announcement 불성립",
    20: "포장 진행 결합은 Progress 불성립",
    21: "브런치 추천 결합은 Nomination 불성립",
    22: "베이커리 유형 속성 결합은 Type 불성립",
    23: "제과 후속 결합은 Followup 불성립",
    26: "보험 수익자 일정표 결합 불명확",
    27: "연공 소견 결합 불명확",
    28: "방수 권고 결합 불명확",
    30: "통행금지 선물 결합은 Curfew 불성립",
    31: "저자 리트리트 결합 불성립",
    32: "공지 전단 결합은 Notice 다의어 불성립",
    33: "베이글 흐름 결합은 Flow 추상 불성립",
    34: "도넛 게시판 결합은 Board 다의어 불성립",
    35: "에스프레소 엔진 결합은 Engine 추상 불성립",
    36: "라떼 부스 결합은 Booth 불성립",
    37: "칫솔 만 결합은 Bay 불성립",
    38: "스노클링 명단 결합은 Roster 다의어 불성립",
    39: "칵테일 창 결합은 Window 다의어 불성립",
    40: "치약 롤 결합은 Roll 다의어 불성립",
    41: "카약 서식 결합은 Form 다의어 불성립",
    42: "바리스타 태그 결합은 Tag 다의어 불성립",
    43: "구강청격 프로필 결합은 Profile 다의어 불성립",
    44: "폭포 이력 결합은 History 불성립",
    45: "펍 초안 결합은 Draft 다의어 불성립",
    46: "마우스가드 요약 결합은 Summary 불성립",
    47: "일몰 알림 결합은 Reminder 불성립",
    49: "스마일 영수증 결합은 Receipt 불명확",
    50: "수변 목록 결합은 List 불성립",
    51: "스시 패스 결합은 Pass 다의어 불성립",
    52: "호흡 바우처 결합은 Voucher 불명확",
    53: "보드워크 전표 결합은 Stub 다의어 불성립",
    54: "타코 게시물 결합은 Bulletin 다의어 불성립",
    55: "코골이 요약 결합은 Brief 다의어 불성립",
    56: "해변 권고 결합은 Advisory 불성립",
    57: "면집 항목 결합은 Entry 다의어 불성립",
    58: "교합 요금 속성 결합은 Fee 불성립",
    59: "전망 단위 결합은 Unit 다의어 불성립",
    60: "해산물 요금 속성 결합은 Fare 불성립",
    61: "치과 세금 결합은 Tax 불성립",
    62: "배낭여행 합계 결합은 Sum 불성립",
    63: "교정의 판매 결합은 Sale 다의어 불성립",
    64: "패러세일링 의무 결합은 Duty 불성립",
    65: "치위 지분 결합은 Stake 불성립",
    66: "야생동물 벌금 결합은 Fine 불성립",
    67: "치실 링크 결합은 Link 불성립",
    68: "라군 세부 결합은 Detail 불성립",
    69: "치석 속성 결합은 Attribute 불성립",
    70: "빙하 형식 결합은 Format 불성립",
    71: "불소 서명 결합은 Signature 불성립",
    72: "화산 잔액 결합은 Balance 불성립",
    73: "실런트 과세 결합은 Levy 불성립",
    74: "당일여행 보조금 결합은 Subsidy 불성립",
    75: "치은염 선수금 결합은 Advance 불성립",
    76: "요트 가산율 결합은 Markup 불성립",
    77: "이갈이 시험 결합은 Trial 다의어 불성립",
    78: "산책로 라벨 결합은 Label 불성립",
    80: "우릴 배치도 결합은 Layout 불성립",
    81: "치주염 렌더링 결합은 Rendering 불성립",
    82: "사막 키트 결합은 Kit 불성립",
    83: "부정교합 메시지 결합은 Message 불성립",
    84: "와이너리 위젯 결합은 Widget 불성립",
    85: "치수과 공지 결합은 Announcement 불성립",
    86: "치주 생성기 결합은 Generator 추상 불성립",
    88: "명찰 핸드북 결합은 Badge 다의어 불명확",
    89: "트레이드 일정표 결합은 Trade 다의어 불명확",
    90: "수의 처방 권고 결합 불명확",
    91: "치료 세미나 결합은 Treatment 추상 불명확",
    92: "결제 리트리트 결합은 Billing 추상 불성립",
    93: "돌봄 토너먼트 결합은 Care 추상 불성립",
    94: "방제 계약 전단 결합 불명확",
    95: "채팅 교육 결합은 Chat 추상 불명확",
    96: "물류 일정표 결합은 Logistics 추상 불명확",
    97: "알레르기 권고 결합 불명확",
    98: "영양 리트리트 결합 불성립",
    99: "아기 낮잠 토너먼트 결합 불성립",
    101: "관광객 교육 결합은 Tourist 불명확",
    103: "운송 경로 권고 결합은 Lane 다의어 불명확",
    104: "부동산 점검 세미나 결합은 Walkthrough 다의어 불명확",
    105: "배상책임 선물 결합 불성립 - Gift",
    106: "급여 압류 리트리트 결합 불성립",
    107: "바닥재 시공 토너먼트 결합 불성립",
    108: "선택 과목 전단 결합은 Elective 불명확",
    110: "다이너 창고 결합은 Bin 다의어 불성립",
    111: "비스트로 주문 결합은 Order 다의어 불성립",
    112: "피자집 세금 결합은 Tax 불성립",
    113: "데리 자산 결합은 Asset 불성립",
    114: "디저트 계산기 결합은 Calculator 추상 불성립",
    115: "포장 승인 결합은 Authorization 불성립",
    116: "브런치 정정 결합은 Correction 불성립",
    117: "베이커리 시계 결합은 Clock 불성립",
    118: "제과 승인 결합은 Approval 불성립",
    121: "홈 스테이징 일정표 결합 불명확",
    122: "보험 수익자 소견 결합 불명확",
    123: "연공 권고 결합 불명확",
    125: "멘토링 선물 결합 불성립 - Gift",
    126: "통행금지 리트리트 결합은 Curfew 불성립",
    127: "저자 토너먼트 결합 불성립",
    128: "베이글 허브 결합은 Hub 추상 불성립",
    129: "도넛 데크 결합은 Deck 불성립",
    130: "에스프레소 조수 결합은 Assistant 추상 불성립",
    131: "라떼 키오스크 결합은 Kiosk 불성립",
    132: "칫솔 게시 결합은 Post 다의어 불성립",
    133: "스노클링 알림 결합은 Alert 불성립",
    134: "칵테일 롤 결합은 Roll 다의어 불성립",
    135: "치약 보고서 결합은 Report 불성립",
    136: "카약 카드 결합은 Card 다의어 불성립",
    137: "바리스타 프로필 결합은 Profile 다의어 불성립",
    138: "구강청격 상태 결합은 Status 다의어 불성립",
    139: "폭포 파일 결합은 File 다의어 불성립",
    140: "펍 요약 결합은 Summary 불성립",
    141: "마우스가드 타임라인 결합 불성립",
    142: "일몰 색인 결합은 Index 다의어 불성립",
    144: "스마일 코드 결합은 Code 불성립",
    145: "수변 식탁 결합은 Table 다의어 불성립",
    147: "호흡 배지 결합은 Badge 다의어 불성립",
    148: "보드워크 정산 결합은 Statement 다의어 불성립",
    149: "타코 요약 결합은 Brief 다의어 불성립",
    150: "코골이 회람 결합은 Circular 다의어 불성립",
    151: "해변 청원 결합은 Petition 불성립",
    152: "면집 요금 속성 결합은 Fee 불성립",
    153: "교합 품목 결합은 Item 다의어 불성립",
    155: "해산물 세금 결합은 Tax 불성립",
    156: "치과 대출 결합은 Loan 불성립",
    157: "배낭여행 부채 결합은 Debt 불성립",
    158: "교정의 청구 결합은 Charge 다의어 불성립",
    159: "패러세일링 수당 결합은 Allowance 불성립",
    160: "치위 마진 속성 결합은 Margin 불성립",
    161: "야생동물 번호 속성 결합은 Number 불성립",
    162: "치실 규칙 결합은 Rule 불성립",
    163: "라군 식별자 결합은 Identifier 불성립",
    164: "치석 필드 결합은 Field 불성립",
    165: "빙하 일련번호 결합은 Serial 불성립",
    166: "불소 마커 결합은 Marker 불성립",
    167: "화산 이자 결합은 Interest 불성립",
    168: "실런트 기한 결합은 Due 불성립",
    169: "당일여행 할인 결합은 Discount 불성립",
    170: "치은염 벌칙 결합은 Penalty 불성립",
    171: "요트 리딤 결합은 Redemption 불성립",
    172: "이갈이 그래프 결합은 Graph 불성립",
    173: "산책로 매뉴얼 결합 불명확",
    175: "우릴 스케치 결합 불명확",
    176: "치주염 통지 결합은 Notification 불성립",
    177: "사막 횟수 결합은 Count 불성립",
    178: "부정교합 총액 결합은 Total 불성립",
    179: "와이너리 저장소 결합은 Repository 불성립",
    180: "치수과 계산기 결합은 Calculator 추상 불성립",
    181: "치주 기록기 결합은 Recorder 추상 불성립",
    182: "대기열 교육 결합은 Queue 추상 불명확",
    184: "명찰 일정표 결합은 Badge 다의어 불명확",
    185: "트레이드 소견 결합은 Trade 다의어 불명확",
    187: "치료 선물 결합은 Treatment 추상 불성립",
    188: "결제 토너먼트 결합은 Billing 추상 불성립",
    189: "돌봄 전단 결합은 Care 추상 불명확",
    190: "설정 교육 결합은 Configuration 추상 불명확",
    191: "채팅 핸드북 결합은 Chat 추상 불명확",
    192: "물류 소견 결합은 Logistics 추상 불명확",
    194: "영양 토너먼트 결합 불성립",
    197: "관광객 핸드북 결합은 Tourist 불명확",
    198: "타악기 일정표 결합 불명확",
    199: "운송 경로 세미나 결합은 Lane 다의어 불명확",
    200: "부동산 점검 선물 결합은 Walkthrough 다의어 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 25, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 175, len(REJECT_REASON)
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
