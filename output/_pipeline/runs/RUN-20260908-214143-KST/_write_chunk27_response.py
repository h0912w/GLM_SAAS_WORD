import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk26_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk26_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "상속 절차 핸드북으로 실재 (Handbook 라인)"),
    34: (0.6, "해변 입장 티켓으로 성립 (Ticket 라인)"),
    35: (0.6, "면요리 영수증으로 성립 (Receipt 라인)"),
    43: (0.6, "치위 시술 예약 확정서로 성립 (Confirmation 라인)"),
    65: (0.7, "이사 후 짐 풀기 정리 교육으로 실재 (도메인 실무 개념)"),
    74: (0.7, "통역 실무 교육으로 실재 (도메인 실무 개념)"),
    84: (0.7, "연고 도포법 교육으로 실재 (도메인 실무 개념)"),
    85: (0.6, "가습기 관리 핸드북으로 실재 (Handbook 라인)"),
    89: (0.6, "사진 라이선싱 세미나로 실재 (Seminar 라인)"),
    97: (0.6, "피자집 이용 바우처로 성립 (Voucher 라인)"),
    105: (0.7, "연주 곡목 확장 교육으로 실재 (도메인 실무 개념)"),
    114: (0.6, "국민투표 안내 전단으로 실재 (Flyer 라인)"),
    125: (0.6, "폭포 안전 경보로 성립 (Alert 라인)"),
    141: (0.6, "해산물 이용 바우처로 성립 (Voucher 라인)"),
    168: (0.7, "번역 교정 실무 교육으로 실재 (도메인 실무 개념)"),
    169: (0.6, "짐 풀기 정리 핸드북으로 실재 (Handbook 라인)"),
    178: (0.7, "자물쇠 사용 재설정 교육으로 실재 (도메인 실무 개념)"),
    179: (0.6, "통역 실무 핸드북으로 실재 (Handbook 라인)"),
    188: (0.7, "헤어 컬러링 교육으로 실재 (도메인 실무 개념)"),
    189: (0.6, "연고 도포법 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "베이글 매트릭스 결합은 Matrix 추상 불성립",
    2: "병원 튜토리얼 결합 불명확",
    4: "벌크 일정표 결합 불명확",
    5: "유사 매물 소견 결합 불명확",
    6: "보험금 권고 결합 불명확",
    7: "수습 세미나 결합 불명확",
    8: "데크 선물 결합 불성립 - Gift",
    9: "루브릭 리트리트 결합 불성립",
    10: "국민투표 토너먼트 결합 불성립",
    11: "스토리 전단 결합 불명확",
    12: "도넛 책상 결합은 Desk 불성립",
    13: "에스프레소 게시판 결합은 Board 다의어 불성립",
    14: "라떼 문 결합은 Gate 불성립",
    15: "칫솔 지도집 결합은 Atlas 불성립",
    16: "스노클링 엔진 결합은 Engine 추상 불성립",
    17: "칵테일 플레이북 결합은 Playbook 불성립",
    18: "치약 저널 결합은 Journal 다의어 불성립",
    19: "카약 디렉터리 결합 불성립",
    20: "바리스타 키오스크 결합은 Kiosk 불성립",
    21: "구강청격 만 결합은 Bay 불성립",
    22: "폭표 명단 결합은 Roster 불성립",
    23: "펍 전광판 결합은 Ticker 불성립",
    24: "마우스가드 라인 결합은 Line 다의어 불성립",
    25: "일몰 굴림 결합은 Roll 불성립",
    26: "스테이크하우스 시트 결합은 Sheet 다의어 불성립",
    27: "스마일 점검 결합은 Check 불성립",
    28: "수변 메모 결합은 Note 다의어 불성립",
    29: "스시 역사 결합 불성립",
    30: "호흡 파일 결합은 File 불성립",
    31: "보드워크 요율 속성 결합은 Rate 불성립",
    32: "타코 타임라인 결합 불성립",
    33: "코골이 알림 결합은 Reminder 불성립",
    36: "교합 코드 결합은 Code 불성립",
    37: "전망 표 결합은 Table 다의어 불성립",
    38: "해산물 통행 결합은 Pass 다의어 불성립",
    39: "치과 바우처 결합 불명확",
    40: "배낭여행 전표 결합은 Stub 다의어 불성립",
    41: "교정의 탭 결합은 Tab 다의어 불성립",
    42: "패러세일링 브리핑 결합은 Brief 다의어 불성립",
    44: "야생동물 항목 결합은 Entry 다의어 불성립",
    45: "치실 단위 결합은 Unit 다의어 불성립",
    46: "라군 비용 속성 결합은 Cost 불성립",
    47: "치석 세금 결합은 Tax 불성립",
    48: "빙하 합계 결합은 Sum 불성립",
    49: "불소 현금 결합은 Cash 불성립",
    50: "화산 청구 결합은 Charge 다의어 불성립",
    51: "실런트 관세 결합은 Tariff 불성립",
    52: "당일여행 지분 결합은 Stake 불성립",
    53: "치은염 번호 속성 결합은 Number 불성립",
    54: "요트 링크 결합은 Link 불성립",
    55: "이갈이 식별자 결합은 Identifier 불성립",
    56: "산책로 속성 결합은 Attribute 불성립",
    57: "구취 일련번호 결합은 Serial 불성립",
    58: "우릴 서명 결합은 Signature 불성립",
    59: "치주염 이자 결합은 Interest 불성립",
    60: "사막 과세 결합은 Levy 불성립",
    61: "부정교합 보조금 결합은 Subsidy 불성립",
    62: "와이너리 연체 결합은 Arrears 불성립",
    63: "치수과 벌칙 결합은 Penalty 불성립",
    64: "치주과 연장 결합은 Extension 불성립",
    66: "인화 교정쇄 핸드북 결합은 Proof 다의어 불명확",
    67: "초대장 일정표 결합 불명확",
    68: "퇴거 소견 결합 불명확",
    69: "수영장 조류 권고 결합 불명확",
    70: "차량 시트 세미나 결합 불명확",
    71: "싱크대 선물 결합 불성립 - Gift",
    72: "여행 리트리트 결합 불성립",
    73: "보컬 토너먼트 결합 불성립",
    75: "이사 경로 핸드북 결합은 Route 추상 불성립",
    76: "사진 조명 일정표 결합 불명확",
    77: "하객 선물 소견 결합은 Favor 다의어 불명확",
    78: "입주자 권고 결합 불명확",
    79: "기술자 세미나 결합은 Technician 불명확",
    80: "린스 선물 결합 불성립 - Gift",
    81: "뚫어락 리트리트 결합 불성립",
    82: "관광 토너먼트 결합 불성립",
    83: "클라리넷 전단 결합 불명확",
    86: "다이얼 조합 일정표 결합 불명확",
    87: "어휘 소견 결합 불명확",
    88: "이사 정산 권고 결합 불명확",
    90: "등록관 선물 결합 불성립 - Gift",
    91: "조경 리트리트 결합 불성립",
    92: "수영장 개시 토너먼트 결합 불성립",
    93: "버킷 전단 결합 불명확",
    94: "카페 파도 결합은 Wave 추상 불성립",
    95: "다이너 스케줄러 결합은 Scheduler 불성립",
    96: "비스트로 카드 결합은 Card 다의어 불성립",
    98: "데리 수당 결합은 Allowance 불성립",
    99: "디저트 가산율 결합은 Markup 불성립",
    100: "포장 타이머 결합은 Timer 불성립",
    101: "브런치 합의 결합은 Agreement 불성립",
    102: "베이커리 검증 결합은 Verification 불성립",
    103: "제과 속도 속성 결합은 Speed 불성립",
    104: "베이글 평가 결합은 Evaluation 불성립",
    106: "병원 핸드북 결합 불명확",
    107: "상속 일정표 결합 불명확",
    108: "벌크 소견 결합 불명확",
    109: "유사 매물 권고 결합 불명확",
    110: "보험금 세미나 결합 불명확",
    111: "수습 선물 결합 불성립 - Gift",
    112: "데크 리트리트 결합 불성립",
    113: "루브릭 토너먼트 결합 불성립",
    115: "도넛 레이더 결합은 Radar 추상 불성립",
    116: "에스프레소 갑판 결합은 Deck 불성립",
    117: "라떼 연결점 결합은 Nexus 불성립",
    118: "칫솔 관리인 결합은 Keeper 불성립",
    119: "스노클링 보조원 결합은 Assistant 불성립",
    120: "칵테일 저널 결합은 Journal 다의어 불성립",
    121: "치약 등록부 결합은 Registry 불성립",
    122: "카약 탐색기 결합은 Locator 불성립",
    123: "바리스타 만 결합은 Bay 불성립",
    124: "구강청격 게시 결합은 Post 다의어 불성립",
    126: "펍 라인 결합은 Line 다의어 불성립",
    127: "마우스가드 창 결합은 Window 불성립",
    128: "일몰 리포트 결합 불성립",
    129: "스테이크하우스 점검 결합은 Check 불성립",
    130: "스마일 점수 결합은 Score 불성립",
    131: "수변 태그 결합은 Tag 다의어 불성립",
    132: "스시 파일 결합은 File 불성립",
    133: "호흡 수준 속성 결합은 Level 불성립",
    134: "보드워크 갱신 결합은 Update 불성립",
    135: "타코 알림 결합은 Reminder 불성립",
    136: "코골이 색인 결합은 Index 다의어 불성립",
    137: "해변 견적 결합 불성립",
    138: "면집 코드 결합은 Code 불성립",
    139: "교합 목록 결합은 List 다의어 불성립",
    140: "전망 전표 결합은 Slip 다의어 불성립",
    142: "치과 배지 결합은 Badge 불성립",
    143: "배낭여행 정산 결합은 Statement 다의어 불성립",
    144: "교정의 회람 결합은 Bulletin 다의어 불성립",
    145: "패러세일링 회람 결합은 Circular 다의어 불성립",
    146: "치위 정리 결합은 Recap 다의어 불성립",
    147: "야생동물 요금 속성 결합은 Fee 불성립",
    148: "치실 계획 결합 불성립",
    149: "라군 가격 속성 결합은 Price 불성립",
    150: "치석 대출 결합은 Loan 불성립",
    151: "빙하 부채 결합은 Debt 불성립",
    152: "불소 판매 결합은 Sale 다의어 불성립",
    153: "화산 의무 결합은 Duty 불성립",
    154: "실런트 가치 속성 결합은 Value 불성립",
    155: "당일여행 마진 속성 결합은 Margin 불성립",
    156: "치은염 버전 결합은 Version 불성립",
    157: "요트 규칙 결합은 Rule 불성립",
    158: "이갈이 분류 결합은 Category 불성립",
    159: "산책로 분야 결합은 Field 불성립",
    160: "구취 토큰 결합은 Token 불성립",
    161: "우릴 표식 결합은 Marker 불성립",
    162: "치주염 자산 결합은 Asset 불성립",
    163: "사막 기한 결합은 Due 불성립",
    164: "부정교합 할인 결합은 Discount 불성립",
    165: "와이너리 선수금 결합은 Advance 불성립",
    166: "치수과 가산율 결합은 Markup 불성립",
    167: "치주과 시험 결합은 Trial 다의어 불성립",
    170: "인화 교정쇄 일정표 결합 불성립",
    171: "초대장 소견 결합 불명확",
    172: "퇴거 권고 결합 불명확",
    173: "수영장 조류 세미나 결합 불명확",
    174: "차량 시트 선물 결합 불성립 - Gift",
    175: "싱크대 리트리트 결합 불성립",
    176: "여행 토너먼트 결합 불성립",
    177: "보컬 전단 결합 불명확",
    180: "이사 경로 일정표 결합 불성립",
    181: "사진 조명 소견 결합 불명확",
    182: "하객 선물 권고 결합은 Favor 다의어 불명확",
    183: "입주자 세미나 결합 불명확",
    184: "기술자 선물 결합 불성립 - Gift",
    185: "린스 리트리트 결합 불성립",
    186: "뚫어락 토너먼트 결합 불성립",
    187: "관광 전단 결합 불명확",
    190: "가습기 일정표 결합 불명확",
    191: "다이얼 조합 소견 결합 불명확",
    192: "어휘 권고 결합 불명확",
    193: "이사 정산 세미나 결합 불명확",
    194: "사진 라이선스 선물 결합 불성립 - Gift",
    195: "등록관 리트리트 결합 불성립",
    196: "조경 토너먼트 결합 불성립",
    197: "수영장 개시 전단 결합 불명확",
    198: "카페 길 결합은 Path 불성립",
    199: "다이너 감시자 결합은 Monitor 불성립",
    200: "비스트로 시트 결합은 Sheet 다의어 불성립",
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
