import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk30_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk30_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "사진 조명 세미나 전단으로 실재 (Seminar 연동 Flyer)"),
    5: (0.7, "차량 진단 교육으로 실재 (도메인 실무 개념)"),
    6: (0.6, "서빙 서비스 핸드북으로 실재 (Handbook 라인)"),
    26: (0.7, "배변 훈련 교육으로 실재 (도메인 실무 개념)"),
    27: (0.6, "헤어 커트 핸드북으로 실재 (Handbook 라인)"),
    35: (0.6, "상속 세미나 전단으로 실재 (Seminar 연동 Flyer)"),
    59: (0.6, "면집 이용 바우처로 성립 (Voucher 라인)"),
    87: (0.6, "치수과 실무 워크시트로 실재 (Worksheet 라인)"),
    89: (0.7, "미용실 제품 판매 교육으로 실재 (도메인 실무 개념)"),
    90: (0.6, "복약 순응도 핸드북으로 실재 (Handbook 라인)"),
    97: (0.7, "장례 사전 계획 교육으로 실재 (도메인 실무 개념)"),
    107: (0.7, "와이파이 설정 교육으로 실재 (도메인 실무 개념)"),
    108: (0.6, "차량 진단 핸드북으로 실재 (Handbook 라인)"),
    128: (0.7, "틀니 관리 교육으로 실재 (도메인 실무 개념)"),
    129: (0.6, "배변 훈련 핸드북으로 실재 (Handbook 라인)"),
    189: (0.6, "치수과 도해 자료로 실재 (Diagram 라인)"),
    190: (0.6, "치주 스케치 자료로 실재 (Diagram 계열)"),
    192: (0.6, "미용실 제품 판매 핸드북으로 실재 (Handbook 라인)"),
    199: (0.7, "세탁 접수 절차 교육으로 실재 (도메인 실무 개념)"),
    200: (0.6, "장례 사전 계획 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "자물쇠 선물 결합 불성립 - Gift",
    2: "통역 리트리트 결합 불성립",
    3: "이사 경로 토너먼트 결합은 Route 추상 불성립",
    7: "구충제 일정표 결합 불명확",
    8: "치실 소견 결합 불명확",
    9: "책읽기 권고 결합 불명확",
    10: "소파 클리닝 세미나 결합 불명확",
    11: "컬러링 선물 결합 불성립 - Gift",
    12: "연고 리트리트 결합 불성립",
    13: "가습기 토너먼트 결합 불성립",
    14: "조합 자물쇠 전단 결합 불명확",
    15: "카페 장부 결합은 Ledger 다의어 불성립",
    16: "다이너 등록소 결합은 Registry 다의어 불성립",
    17: "비스트로 상태 결합은 Status 불성립",
    18: "피자집 회람 결합은 Bulletin 다의어 불성립",
    19: "데리 버전 결합은 Version 불성립",
    20: "디저트 워크시트 결합 불명확",
    21: "포장 순위 결합은 Rank 불성립",
    22: "브런치 핑 결합은 Ping 불성립",
    23: "베이커리 일기 결합은 Diary 다의어 불성립",
    24: "제과 전압 속성 결합은 Voltage 불성립",
    25: "베이글 위험 결합은 Hazard 불성립",
    28: "복약 상담 일정표 결합 불명확",
    29: "커패시터 소견 결합 불명확",
    30: "스마트 도어락 권고 결합 불명확",
    31: "클럽하우스 세미나 결합 불명확",
    32: "스키 선물 결합 불성립 - Gift",
    33: "연주 곡목 리트리트 결합 불성립",
    34: "병원 토너먼트 결합 불성립",
    36: "도넛 다리 결합은 Bridge 추상 불성립",
    37: "에스프레소 관문 결합은 Portal 추상 불성립",
    38: "라떼 스케줄러 결합은 Scheduler 불성립",
    39: "칫솔 동반자 결합은 Companion 불성립",
    40: "스노클링 플레이북 결합은 Playbook 전면 기각",
    41: "칵테일 계수기 결합은 Counter 다의어 불성립",
    42: "치약 부스 결합은 Booth 불성립",
    43: "카약 게시물 결합은 Post 다의어 불성립",
    44: "바리스타 여권 결합은 Passport 다의어 불성립",
    45: "구강청격 로비 결합은 Lobby 불성립",
    46: "폭포 창 결합은 Window 불성립",
    47: "펍 시트 결합은 Sheet 다의어 불성립",
    48: "마우스가드 검사 결합 불성립",
    49: "일몰 메모 결합은 Note 다의어 불성립",
    50: "스테이크하우스 역사 결합 불성립",
    51: "스마일 파일 결합은 File 다의어 불성립",
    52: "수변 요율 속성 결합은 Rate 불성립",
    53: "스시 타임라인 결합 불성립",
    54: "호흡 알림 결합은 Reminder 불성립",
    55: "보드워크 티켓 결합 불명확",
    56: "타코 코드 결합은 Code 불성립",
    57: "코골이 목록 결합은 List 불성립",
    58: "해변 전표 결합은 Slip 다의어 불성립",
    60: "교합 배지 결합은 Badge 다의어 불성립",
    61: "전망 정산 결합은 Statement 다의어 불성립",
    62: "해산물 회람 결합은 Bulletin 다의어 불성립",
    63: "치과 요약 결합은 Brief 다의어 불성립",
    64: "배낭여행 권고 결합은 Advisory 불성립",
    65: "교정의 입장 결합은 Entry 다의어 불성립",
    66: "패러세일링 품목 결합은 Item 다의어 불성립",
    67: "치위 가격 속성 결합은 Price 불성립",
    68: "야생동물 세금 결합은 Tax 불성립",
    69: "치실 부채 결합은 Debt 불성립",
    70: "라군 현금 결합은 Cash 불성립",
    71: "치석 의무 결합은 Duty 불성립",
    72: "빙하 관세 결합은 Tariff 불성립",
    73: "불소 마진 속성 결합은 Margin 불성립",
    74: "화산 번호 속성 결합은 Number 불성립",
    75: "실런트 규칙 결합은 Rule 불성립",
    76: "당일여행 식별자 결합은 Identifier 불성립",
    77: "치은염 필드 결합은 Field 불성립",
    78: "요트 일련번호 결합은 Serial 불성립",
    79: "이갈이 마커 결합은 Marker 불성립",
    80: "산책로 이자 결합은 Interest 불성립",
    81: "구취 기한 결합은 Due 불성립",
    82: "우릴 할인 결합은 Discount 불성립",
    83: "치주염 벌칙 결합은 Penalty 불성립",
    84: "사막 상환 결합은 Redemption 불성립",
    85: "부정교합 시험 결합은 Trial 다의어 불성립",
    86: "와이너리 라벨 결합은 Label 불성립",
    88: "치주 배치도 결합은 Layout 불성립",
    91: "선석 일정표 결합 불명확",
    92: "압축기 세미나 결합 불명확",
    93: "도어 실린더 선물 결합 불성립 - Gift",
    94: "인화 교정쇄 리트리트 결합은 Proof 다의어 불성립",
    95: "짐 풀기 토너먼트 결합 불성립",
    96: "인화 교정쇄 전단 결합은 Proof 다의어 불성립",
    98: "일정 핸드북 결합은 Schedule 추상 불성립",
    99: "처방 상담 일정표 결합 불명확",
    100: "컨테이너 소견 결합 불명확",
    101: "자격 인증 권고 결합 불명확",
    102: "매장량 세미나 결합은 Reserve 다의어 불성립",
    103: "송풍기 선물 결합 불성립 - Gift",
    104: "자물쇠 리트리트 결합 불성립",
    105: "통역 토너먼트 결합 불성립",
    106: "이사 경로 전단 결합은 Route 추상 불성립",
    109: "서빙 일정표 결합 불명확",
    110: "구충제 소견 결합 불명확",
    111: "치실 권고 결합 불명확",
    112: "책읽기 세미나 결합 불명확",
    113: "소파 클리닝 선물 결합 불성립 - Gift",
    114: "컬러링 리트리트 결합 불성립",
    115: "연고 토너먼트 결합 불성립",
    116: "가습기 전단 결합 불명확",
    117: "카페 게시판 결합은 Board 다의어 불성립",
    118: "다이너 달력 결합 불명확",
    119: "비스트로 뷰 결합은 View 추상 불성립",
    120: "피자집 요약 결합은 Brief 다의어 불성립",
    121: "데리 링크 결합은 Link 불성립",
    122: "디저트 도해 결합 불명확",
    123: "포장 추세 결합은 Trend 불성립",
    124: "브런치 모델 결합은 Model 불성립",
    125: "베이커리 환불 결합은 Refund 불성립",
    126: "제과 전력 속성 결합은 Wattage 불성립",
    127: "베이글 연대보증 결합은 Guarantor 불성립",
    130: "헤어 커트 일정표 결합 불명확",
    131: "복약 상담 소견 결합 불명확",
    132: "커패시터 권고 결합 불명확",
    133: "스마트 도어락 세미나 결합 불명확",
    134: "클럽하우스 선물 결합 불성립 - Gift",
    135: "스키 리트리트 결합 불성립",
    136: "연주 곡목 토너먼트 결합 불성립",
    137: "병원 전단 결합 불명확",
    138: "도넛 신호 결합은 Signal 추상 불성립",
    139: "에스프레소 콘솔 결합은 Console 추상 불성립",
    140: "라떼 감시자 결합은 Monitor 불성립",
    141: "칫솔 등기부 결합은 Register 다의어 불성립",
    142: "스노클링 일지 결합은 Journal 다의어 불성립",
    143: "칵테일 부스 결합은 Booth 불성립",
    144: "치약 키오스크 결합은 Kiosk 불성립",
    145: "카약 만 결합은 Harbor 다의어 불성립",
    146: "바리스타 로비 결합은 Lobby 불성립",
    147: "구강청격 전광판 결합은 Ticker 불성립",
    148: "폭포 롤 결합은 Roll 다의어 불성립",
    149: "펍 검사 결합은 Check 불성립",
    150: "마우스가드 점수 결합은 Score 불성립",
    151: "일몰 태그 결합은 Tag 다의어 불성립",
    152: "스테이크하우스 파일 결합은 File 다의어 불성립",
    153: "스마일 수준 속성 결합은 Level 불성립",
    154: "수변 갱신 결합은 Update 불성립",
    155: "스시 알림 결합은 Reminder 불성립",
    156: "호흡 색인 결합은 Index 다의어 불성립",
    157: "보드워크 견적 결합은 Estimate 불성립",
    158: "타코 목록 결합은 List 불성립",
    159: "코골이 식탁 결합은 Table 불성립",
    160: "해변 샘플 결합은 Sample 다의어 불성립",
    161: "면집 배지 결합은 Badge 다의어 불성립",
    162: "교합 전표 결합은 Stub 다의어 불성립",
    163: "전망 메모 결합은 Memo 다의어 불성립",
    164: "해산물 요약 결합은 Brief 다의어 불성립",
    165: "치과 회람 결합은 Circular 다의어 불성립",
    166: "배낭여행 청원 결합은 Petition 불성립",
    167: "교정의 요금 속성 결합은 Fee 불성립",
    168: "패러세일링 단위 결합은 Unit 다의어 불성립",
    169: "치위 운임 속성 결합은 Fare 불성립",
    170: "야생동물 대출 결합은 Loan 불성립",
    171: "치실 기금 결합은 Fund 불성립",
    172: "라군 판매 결합은 Sale 다의어 불성립",
    173: "치석 수당 결합은 Allowance 불성립",
    174: "빙하 가치 속성 결합은 Value 불성립",
    175: "불소 벌금 결합은 Fine 불성립",
    176: "화산 버전 결합은 Version 불성립",
    177: "실런트 세부 결합은 Detail 불성립",
    178: "당일여행 분류 결합은 Category 불성립",
    179: "치은염 형식 결합은 Format 불성립",
    180: "요트 토큰 결합은 Token 불성립",
    181: "이갈이 잔액 결합은 Balance 불성립",
    182: "산책로 자산 결합은 Asset 불성립",
    183: "구취 보조금 결합은 Subsidy 불성립",
    184: "우릴 연체 결합은 Arrears 불성립",
    185: "치주염 가산율 결합은 Markup 불성립",
    186: "사막 연장 결합은 Extension 불성립",
    187: "부정교합 그래프 결합은 Graph 불성립",
    188: "와이너리 매뉴얼 결합 불명확",
    191: "서비스 튜토리얼 결합은 Service 다의어 불명확",
    193: "복약 순응도 일정표 결합 불명확",
    194: "선석 소견 결합 불명확",
    195: "압축기 선물 결합 불성립 - Gift",
    196: "도어 실린더 리트리트 결합 불성립",
    197: "인화 교정쇄 토너먼트 결합 불성립",
    198: "짐 풀기 전단 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 20, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 180, len(REJECT_REASON)
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
