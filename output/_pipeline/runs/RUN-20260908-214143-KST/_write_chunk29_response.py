import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk28_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk28_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    17: (0.7, "스마트 도어락 설치 교육으로 실재 (도메인 실무 개념)"),
    22: (0.6, "상속 계획 세미나로 실재 (Seminar 라인)"),
    47: (0.6, "타코 케이터링 견적으로 성립 (Estimate 견적)"),
    57: (0.6, "패러세일링 투어 예약 확정서로 성립 (Confirmation 라인)"),
    59: (0.6, "야생동물 관람 투어 계획으로 성립 (Plan 라인)"),
    79: (0.6, "치주 관리 매뉴얼로 실재 (Manual 라인)"),
    80: (0.6, "압축기 유지보수 핸드북으로 실재 (Handbook 라인)"),
    99: (0.7, "치실 사용법 교육으로 실재 (도메인 실무 개념)"),
    100: (0.6, "아동 책읽기 핸드북으로 실재 (Handbook 라인)"),
    108: (0.6, "라이선싱 세미나 전단으로 실재 (Flyer 라인)"),
    117: (0.6, "베이커리 리뷰로 실재 (Review 맛 평가 독해)"),
    120: (0.7, "커패시터 점검 교체 교육으로 실재 (도메인 실무 개념)"),
    121: (0.6, "스마트 도어락 핸드북으로 실재 (Handbook 라인)"),
    155: (0.6, "전망대 이용 바우처로 성립 (Voucher 라인)"),
    182: (0.6, "치주 실무 워크시트로 실재 (Worksheet 실무 자료)"),
    191: (0.7, "컨테이너 운송 절차 교육으로 실재 (도메인 실무 개념)"),
    196: (0.6, "통역 실무 세미나로 실재 (Seminar 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "조합 자물쇠 세미나 결합 불명확",
    2: "어휘 선물 결합 불성립 - Gift",
    3: "이사 정산 리트리트 결합 불성립",
    4: "사진 라이선스 토너먼트 결합 불성립",
    5: "등록관 전단 결합은 Registrar 다의어 불명확",
    6: "카페 지도 결합은 Map 불성립",
    7: "다이너 등기부 결합은 Register 다의어 불성립",
    8: "비스트로 점수 결합은 Score 불성립",
    9: "피자집 정산 결합은 Statement 다의어 불성립",
    10: "데리 지분 결합은 Stake 불성립",
    11: "디저트 시험 결합은 Trial 다의어 불성립",
    12: "포장 조력자 결합은 Helper 불성립",
    13: "브런치 케이스 결합은 Case 다의어 불성립",
    14: "베이커리 봉인 결합은 Seal 다의어 불성립",
    15: "제과 폭 속성 결합은 Width 불성립",
    16: "베이글 혜택 결합은 Benefit 불성립",
    18: "클럽하우스 핸드북 결합 불명확",
    19: "스키 일정표 결합 불명확",
    20: "연주 곡목 소견 결합 불명확",
    21: "병원 권고 결합 불명확",
    23: "벌크 선물 결합 불성립 - Gift",
    24: "유사 매물 리트리트 결합 불성립",
    25: "보험금 토너먼트 결합 불성립",
    26: "수습 전단 결합 불명확",
    27: "도넛 나침반 결합은 Compass 추상 불성립",
    28: "에스프레소 스테이션 결합은 Station 불성립",
    29: "라떼 관리자 결합은 Manager 불성립",
    30: "칫솔 보조원 결합은 Assistant 불성립",
    31: "스노클링 감시자 결합은 Monitor 불성립",
    32: "칵테일 디렉터리 결합 불성립",
    33: "치약 탐색기 결합은 Locator 불성립",
    34: "카약 계수기 결합은 Counter 다의어 불성립",
    35: "바리스타 명단 결합은 Roster 불성립",
    36: "구강청격 경보 결합 불성립",
    37: "폭포 여권 결합은 Passport 다의어 불성립",
    38: "펍 리포트 결합 불성립",
    39: "마우스가드 기록 결합은 Log 불성립",
    40: "일몰 카드 결합은 Card 다의어 불성립",
    41: "스테이크하우스 태그 결합은 Tag 다의어 불성립",
    42: "스마일 프로필 결합 불성립",
    43: "수변 뷰 결합은 View 추상 불성립",
    44: "스시 갱신 결합은 Update 불성립",
    45: "호흡 피드 결합은 Feed 추상 불성립",
    46: "보드워크 요약 결합은 Summary 불성립",
    48: "코골이 주문 결합은 Order 다의어 불성립",
    49: "해변 영수증 결합 불성립",
    50: "면집 전표 결합은 Slip 다의어 불성립",
    51: "교합 샘플 결합은 Sample 다의어 불성립",
    52: "전망 통행 결합은 Pass 다의어 불성립",
    53: "해산물 정산 결합은 Statement 다의어 불성립",
    54: "치과 메모 결합은 Memo 다의어 불성립",
    55: "배낭여행 탭 결합은 Tab 다의어 불성립",
    56: "교정의 권고 결합은 Advisory 불성립",
    58: "치위 품목 결합은 Item 다의어 불성립",
    60: "치실 운임 속성 결합은 Fare 불성립",
    61: "라군 대출 결합은 Loan 불성립",
    62: "치석 기금 결합은 Fund 불성립",
    63: "빙하 판매 결합은 Sale 다의어 불성립",
    64: "불소 수당 결합은 Allowance 불성립",
    65: "화산 가치 속성 결합은 Value 불성립",
    66: "실런트 벌금 결합은 Fine 불성립",
    67: "당일여행 버전 결합은 Version 불성립",
    68: "치은염 세부 결합은 Detail 불성립",
    69: "요트 분류 결합은 Category 불성립",
    70: "이갈이 형식 결합은 Format 불성립",
    71: "산책로 토큰 결합은 Token 불성립",
    72: "구취 잔액 결합은 Balance 불성립",
    73: "우릴 자산 결합은 Asset 불성립",
    74: "치주염 보조금 결합은 Subsidy 불성립",
    75: "사막 연체 결합은 Arrears 불성립",
    76: "부정교합 벌칙 결합은 Penalty 불성립",
    77: "와이너리 상환 결합은 Redemption 불성립",
    78: "치수과 시험 결합은 Trial 다의어 불성립",
    81: "도어 실린더 일정표 결합 불명확",
    82: "번역 교정 소견 결합 불명확",
    83: "짐 풀기 권고 결합 불명확",
    84: "인화 교정쇄 세미나 결합은 Proof 다의어 불명확",
    85: "초대장 선물 결합 불성립 - Gift",
    86: "퇴거 리트리트 결합 불성립",
    87: "수영장 조류 토너먼트 결합 불성립",
    88: "차량 시트 전단 결합 불명확",
    89: "자격 인증 교육 결합 불명확",
    90: "매장량 핸드북 결합은 Reserve 다의어 불명확",
    91: "송풍기 일정표 결합 불명확",
    92: "자물쇠 소견 결합 불명확",
    93: "통역 권고 결합 불명확",
    94: "이사 경로 세미나 결합은 Route 추상 불성립",
    95: "사진 조명 선물 결합 불성립 - Gift",
    96: "하객 선물 리트리트 결합은 Favor 다의어 불명확",
    97: "입주자 토너먼트 결합 불성립",
    98: "기술자 전단 결합은 Technician 불명확",
    101: "소파 클리닝 일정표 결합 불명확",
    102: "컬러링 소견 결합 불명확",
    103: "연고 권고 결합 불명확",
    104: "가습기 세미나 결합 불명확",
    105: "조합 자물쇠 선물 결합 불성립 - Gift",
    106: "어휘 리트리트 결합 불성립",
    107: "이사 정산 토너먼트 결합 불성립",
    109: "카페 틀 결합은 Frame 불성립",
    110: "다이너 작전 결합은 Ops 불성립",
    111: "비스트로 메모 결합은 Note 다의어 불성립",
    112: "피자집 메모 결합은 Memo 다의어 불성립",
    113: "데리 마진 속성 결합은 Margin 불성립",
    114: "디저트 그래프 결합은 Graph 불성립",
    115: "포장 무대 결합은 Stage 불성립",
    116: "브런치 매치 결합은 Match 불성립",
    118: "제과 온도 속성 결합은 Temperature 불성립",
    119: "베이글 요건 결합은 Requirement 불성립",
    122: "클럽하우스 일정표 결합 불명확",
    123: "스키 소견 결합 불명확",
    124: "연주 곡목 권고 결합 불명확",
    125: "병원 세미나 결합 불명확",
    126: "상속 선물 결합 불성립 - Gift",
    127: "벌크 리트리트 결합 불성립",
    128: "유사 매물 토너먼트 결합 불성립",
    129: "보험금 전단 결합 불명확",
    130: "도넛 등대 결합은 Beacon 추상 불성립",
    131: "에스프레소 단말 결합은 Terminal 불성립",
    132: "라떼 엔진 결합은 Engine 추상 불성립",
    133: "칫솔 플래너 결합은 Planner 불성립",
    134: "스노클링 동반자 결합은 Companion 불성립",
    135: "칵테일 탐색기 결합은 Locator 불성립",
    136: "치약 탐색기 결합은 Finder 불성립",
    137: "카약 부스 결합은 Booth 불성립",
    138: "바리스타 경보 결합은 Alert 불성립",
    139: "구강청격 차트 결합은 Chart 불성립",
    140: "폭포 로비 결합은 Lobby 불성립",
    141: "펍 기록 결합은 Log 위치 추상 불성립",
    142: "마우스가드 서식 결합은 Form 다의어 불성립",
    143: "일몰 시트 결합은 Sheet 다의어 불성립",
    144: "스테이크하우스 프로필 결합 불성립",
    145: "스마일 상태 결합은 Status 불성립",
    146: "수변 역사 결합 불성립",
    147: "스시 피드 결합은 Feed 추상 불성립",
    148: "호흡 초안 결합은 Draft 다의어 불성립",
    149: "보드워크 타임라인 결합 불성립",
    150: "타코 주문 결합은 Order 다의어 불성립",
    151: "코골이 청구서 결합 불성립",
    152: "해변 코드 결합은 Code 불성립",
    153: "면집 샘플 결합은 Sample 다의어 불성립",
    154: "교합 슬롯 결합은 Slot 다의어 불성립",
    156: "해산물 메모 결합은 Memo 다의어 불성립",
    157: "치과 한도 결합은 Quota 속성어 불성립",
    158: "배낭여행 회람 결합은 Bulletin 다의어 불성립",
    159: "교정의 청원 결합은 Petition 불성립",
    160: "패러세일링 정리 결합은 Recap 다의어 불성립",
    161: "치위 단위 결합은 Unit 다의어 불성립",
    162: "야생동물 비용 속성 결합은 Cost 불성립",
    163: "치실 세금 결합은 Tax 불성립",
    164: "라군 합계 결합은 Sum 불성립",
    165: "치석 현금 결합은 Cash 불성립",
    166: "빙하 청구 결합은 Charge 다의어 불성립",
    167: "불소 관세 결합은 Tariff 불성립",
    168: "화산 지분 결합은 Stake 불성립",
    169: "실런트 번호 속성 결합은 Number 불성립",
    170: "당일여행 링크 결합은 Link 불성립",
    171: "치은염 식별자 결합은 Identifier 불성립",
    172: "요트 속성 결합은 Attribute 불성립",
    173: "이갈이 일련번호 결합은 Serial 불성립",
    174: "산책로 서명 결합은 Signature 불성립",
    175: "구취 이자 결합은 Interest 불성립",
    176: "우릴 과세 결합은 Levy 불성립",
    177: "치주염 할인 결합은 Discount 불성립",
    178: "사막 선수금 결합은 Advance 불성립",
    179: "부정교합 가산율 결합은 Markup 불성립",
    180: "와이너리 연장 결합은 Extension 불성립",
    181: "치수과 그래프 결합은 Graph 불성립",
    183: "압축기 일정표 결합 불명확",
    184: "도어 실린더 소견 결합 불명확",
    185: "번역 교정 권고 결합 불명확",
    186: "짐 풀기 세미나 결합 불명확",
    187: "인화 교정쇄 선물 결합 불성립 - Gift",
    188: "초대장 리트리트 결합 불성립",
    189: "퇴거 토너먼트 결합 불성립",
    190: "수영장 조류 전단 결합 불명확",
    192: "자격 인증 핸드북 결합 불명확",
    193: "매장량 일정표 결합 불성립",
    194: "송풍기 소견 결합 불명확",
    195: "자물쇠 권고 결합 불명확",
    197: "이사 경로 선물 결합은 Route 추상 불성립",
    198: "사진 조명 리트리트 결합 불성립",
    199: "하객 선물 토너먼트 결합은 Favor 다의어 불명확",
    200: "입주자 전단 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 17, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 183, len(REJECT_REASON)
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
