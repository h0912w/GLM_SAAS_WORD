import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk40_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk40_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "파산 절차 세미나로 실재 (Seminar 라인)"),
    6: (0.6, "연공제 교육 안내 전단으로 실재 (Flyer 라인)"),
    8: (0.6, "도넛 체험 센터로 성립 (Center 라인)"),
    19: (0.6, "펍 케이터링 견적으로 성립 (Estimate 라인 준용)"),
    21: (0.6, "일몰 투어 영수증으로 성립 (Receipt 라인 준용)"),
    24: (0.6, "수변 명소 이용권으로 성립 (Voucher 라인 준용)"),
    51: (0.6, "이갈이 도식 학습자료로 실재 (Schematic 라인)"),
    60: (0.6, "치주과 실습 워크숍으로 실재 (Workshop 라인)"),
    61: (0.7, "원고 준비 교육으로 실재 (도메인 실무 개념)"),
    62: (0.6, "배차 관리 핸드북으로 실재 (Handbook 라인)"),
    69: (0.7, "콘텐츠 제작 교육으로 실재 (도메인 실무 개념)"),
    70: (0.6, "구독 발행 관리 핸드북으로 실재 (Handbook 라인)"),
    76: (0.6, "결혼 서약 준비 핸드북으로 실재 (Handbook 라인)"),
    79: (0.6, "배관 실무 세미나로 실재 (Seminar 라인)"),
    92: (0.7, "열전대 점검 교육으로 실재 (도메인 실무 개념)"),
    97: (0.6, "상처 드레싱 교육 세미나로 실재 (Seminar 라인)"),
    101: (0.6, "보험 수익자 지정 안내 전단으로 실재 (Flyer 라인)"),
    115: (0.6, "마우스가드 청구서로 성립 (Bill 라인 준용)"),
    156: (0.7, "브랜드 구축 교육으로 실재 (도메인 실무 개념)"),
    157: (0.6, "원고 준비 핸드북으로 실재 (Handbook 라인)"),
    160: (0.6, "프로비저닝 실무 세미나로 실재 (Seminar 라인)"),
    165: (0.6, "콘텐츠 제작 핸드북으로 실재 (Handbook 라인)"),
    168: (0.6, "보안 패치 관리 세미나로 실재 (Seminar 라인)"),
    172: (0.6, "이사 파손 대응 교육으로 실재 (도메인 실무 개념)"),
    175: (0.6, "차량 하부 세척 세미나로 실재 (Seminar 라인)"),
    186: (0.6, "브런치집 리뷰로 성립 (Review 라인 준용)"),
    189: (0.6, "열전대 점검 핸드북으로 실재 (Handbook 라인)"),
    193: (0.6, "템포 훈련 세미나로 실재 (Seminar 라인)"),
    197: (0.6, "홈 스테이징 서비스 전단으로 실재 (Flyer 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "상처 드레싱 권고 결합 불명확",
    3: "화물 통합 선물 결합 불성립 - Gift",
    4: "홈 스테이징 리트리트 결합 불성립",
    5: "보험 수익자 토너먼트 결합 불성립",
    7: "베이글 나침반 결합은 Compass 추상 불성립",
    9: "에스프레소 등록기 결합은 Register 불성립",
    10: "라떼 알림 결합은 Alert 불성립",
    11: "칫솔 창고 결합은 Bin 다의어 불성립",
    12: "스노클링 전광판 결합은 Ticker 불성립",
    13: "칵테일 시트 결합은 Sheet 다의어 불성립",
    14: "치약 점검 결합은 Check 불성립",
    15: "카약 태그 결합은 Tag 다의어 불성립",
    16: "바리스타 수준 속성 결합은 Level 불성립",
    17: "구강청격 요율 속성 결합은 Rate 불성립",
    18: "폭포 초안 결합은 Draft 다의어 불성립",
    20: "마우스가드 주문 결합은 Order 다의어 불성립",
    22: "스테이크하우스 샘플 결합은 Sample 다의어 불성립",
    23: "스마일 슬롯 결합은 Slot 불성립",
    25: "스시 한도 결합은 Quota 불성립",
    26: "호흡 탭 결합은 Tab 다의어 불성립",
    27: "보드워크 요약 결합은 Brief 다의어 불성립",
    28: "타코 요약 결합은 Recap 불성립",
    29: "코골이 항목 결합은 Entry 다의어 불성립",
    30: "해변 품목 결합은 Item 다의어 불성립",
    31: "면집 가격 속성 결합은 Price 불성립",
    32: "교합 요금 속성 결합은 Fare 불성립",
    33: "전망 대출 결합은 Loan 불성립",
    34: "해산물 현금 결합은 Cash 불성립",
    35: "치과 판매 결합은 Sale 다의어 불성립",
    36: "배낭여행 의무 결합은 Duty 불성립",
    37: "교정의 지분 결합은 Stake 불성립",
    38: "패러세일링 벌금 결합은 Fine 불성립",
    39: "치위 규칙 결합은 Rule 불성립",
    40: "야생동물 식별자 결합은 Identifier 불성립",
    41: "치실 필드 결합은 Field 불성립",
    42: "라군 일련번호 결합은 Serial 불성립",
    43: "치석 마커 결합은 Marker 불성립",
    44: "빙하 이자 결합은 Interest 불성립",
    45: "불소 기한 결합은 Due 불성립",
    46: "화산 할인 결합은 Discount 불성립",
    47: "실런트 벌칙 결합은 Penalty 불성립",
    48: "당일여행 리딤 결합은 Redemption 불성립",
    49: "치은염 그래프 결합은 Graph 불성립",
    50: "요트 매뉴얼 결합 불명확",
    52: "산책로 스케치 결합 불명확",
    53: "구취 통지 결합은 Notification 불성립",
    54: "우릴 횟수 결합은 Count 불성립",
    55: "치주염 위젯 결합은 Widget 불성립",
    56: "사막 공지 결합은 Announcement 불성립",
    57: "부정교합 변환기 결합은 Converter 추상 불성립",
    58: "와이너리 기록기 결합은 Recorder 추상 불성립",
    59: "치수과 점검기 결합은 Checker 추상 불성립",
    63: "위협 분석 소견 결합 불명확",
    64: "프로비저닝 권고 결합 불명확",
    65: "대기열 세미나 결합은 Queue 추상 불명확",
    66: "인재 소싱 선물 결합 불성립 - Gift",
    67: "명찰 리트리트 결합은 Badge 다의어 불성립",
    68: "트레이드 토너먼트 결합은 Trade 다의어 불성립",
    71: "통신 개통 소견 결합 불명확",
    72: "보안 패치 권고 결합 불명확",
    73: "설정 세미나 결합은 Configuration 추상 불명확",
    74: "채팅 선물 결합은 Chat 추상 불성립",
    75: "물류 토너먼트 결합은 Logistics 추상 불성립",
    77: "수영장 동절기 관리 소견 결합 불명확",
    78: "차량 하부 권고 결합 불명확",
    80: "관광객 선물 결합은 Tourist 불성립",
    81: "타악기 리트리트 결합 불성립",
    82: "카페 관리인 결합은 Keeper 추상 불성립",
    83: "다이너 롤 결합은 Roll 다의어 불성립",
    84: "비스트로 전표 결합은 Slip 다의어 불성립",
    85: "피자집 판매 결합은 Sale 다의어 불성립",
    86: "데리 선수금 결합은 Advance 불성립",
    87: "디저트 탐지기 결합은 Detector 추상 불성립",
    88: "포장 계좌 결합은 Account 불성립",
    89: "브런치 봉인 결합은 Seal 불성립",
    90: "베이커리 온도 속성 결합은 Temperature 불성립",
    91: "제과 요건 결합은 Requirement 불성립",
    93: "비상 대응 핸드북 결합은 Panic 다의어 불명확",
    94: "수영장 관리 일정표 결합 불명확",
    95: "서핑 소견 결합 불명확",
    96: "템포 권고 결합 불명확",
    98: "파산 선물 결합 불성립 - Gift",
    99: "화물 통합 리트리트 결합 불성립",
    100: "홈 스테이징 토너먼트 결합 불성립",
    102: "베이글 등대 결합은 Beacon 추상 불성립",
    103: "도넛 구역 결합은 Zone 불성립",
    104: "에스프레소 운영 결합은 Ops 추상 불성립",
    105: "라떼 차트 결합은 Chart 불성립",
    106: "칫솔 여권 결합은 Passport 다의어 불성립",
    107: "스노클링 선 결합은 Line 다의어 불성립",
    108: "칵테일 점검 결합은 Check 불성립",
    109: "치약 점수 결합은 Score 불성립",
    110: "카약 프로필 결합은 Profile 다의어 불성립",
    111: "바리스타 요율 속성 결합은 Rate 불성립",
    112: "구강청격 갱신 결합은 Update 불성립",
    113: "폭포 요약 결합은 Summary 불성립",
    114: "펍 주문 결합은 Order 다의어 불성립",
    116: "일몰 코드 결합은 Code 불성립",
    117: "스테이크하우스 슬롯 결합은 Slot 불성립",
    118: "스마일 패스 결합은 Pass 다의어 불성립",
    119: "수변 배지 결합은 Badge 다의어 불성립",
    120: "스시 탭 결합은 Tab 다의어 불성립",
    121: "호흡 게시물 결합은 Bulletin 다의어 불성립",
    122: "보드워크 회람 결합은 Circular 다의어 불성립",
    123: "타코 항목 결합은 Entry 다의어 불성립",
    124: "코골이 요금 속성 결합은 Fee 불성립",
    125: "해변 단위 결합은 Unit 다의어 불성립",
    126: "면집 요금 속성 결합은 Fare 불성립",
    127: "교합 세금 결합은 Tax 불성립",
    128: "전망 합계 결합은 Sum 불성립",
    129: "해산물 판매 결합은 Sale 다의어 불성립",
    130: "치과 청구 결합은 Charge 다의어 불성립",
    131: "배낭여행 수당 결합은 Allowance 불성립",
    132: "교정의 마진 속성 결합은 Margin 불성립",
    133: "패러세일링 번호 속성 결합은 Number 불성립",
    134: "치위 세부 결합은 Detail 불성립",
    135: "야생동물 분류 결합은 Category 불성립",
    136: "치실 형식 결합은 Format 불성립",
    137: "라군 토큰 결합은 Token 불성립",
    138: "치석 잔액 결합은 Balance 불성립",
    139: "빙하 자산 결합은 Asset 불성립",
    140: "불소 보조금 결합은 Subsidy 불성립",
    141: "화산 연체 결합은 Arrears 불성립",
    142: "실런트 가산율 결합은 Markup 불성립",
    143: "당일여행 연장 결합은 Extension 불성립",
    144: "치은염 라벨 결합은 Label 불성립",
    145: "요트 워크시트 결합 불명확",
    146: "이갈이 배치도 결합은 Layout 불성립",
    147: "산책로 개요 결합은 Outline 불성립",
    148: "구취 키트 결합은 Kit 불성립",
    149: "우릴 메시지 결합은 Message 불성립",
    150: "치주염 저장소 결합은 Repository 불성립",
    151: "사막 계산기 결합은 Calculator 추상 불성립",
    152: "부정교합 생성기 결합은 Generator 추상 불성립",
    153: "와이너리 견적기 결합은 Estimator 추상 불성립",
    154: "치수과 탐지기 결합은 Detector 추상 불성립",
    155: "치주 보호자 결합은 Guardian 추상 불성립",
    158: "배차 일정표 결합 불명확",
    159: "위협 분석 권고 결합 불명확",
    161: "대기열 선물 결합은 Queue 추상 불성립",
    162: "인재 소싱 리트리트 결합 불성립",
    163: "명찰 토너먼트 결합은 Badge 다의어 불성립",
    164: "트레이드 전단 결합은 Trade 다의어 불명확",
    166: "구독 발행 일정표 결합 불명확",
    167: "통신 개통 권고 결합 불명확",
    169: "설정 선물 결합은 Configuration 추상 불성립",
    170: "채팅 리트리트 결합은 Chat 추상 불성립",
    171: "물류 전단 결합은 Logistics 추상 불명확",
    173: "결혼 서약 일정표 결합 불명확",
    174: "수영장 동절기 관리 권고 결합 불명확",
    176: "배수관 선물 결합 불성립 - Gift",
    177: "관광객 리트리트 결합은 Tourist 불성립",
    178: "타악기 토너먼트 결합 불성립",
    179: "카페 관리자 결합은 Manager 추상 불성립",
    180: "다이너 보고서 결합은 Report 불성립",
    181: "비스트로 샘플 결합은 Sample 다의어 불성립",
    182: "피자집 청구 결합은 Charge 다의어 불성립",
    183: "데리 벌칙 결합은 Penalty 불성립",
    184: "디저트 타이머 결합은 Timer 추상 불성립",
    185: "포장 케이스 결합은 Case 다의어 불성립",
    187: "베이커리 압력 속성 결합은 Pressure 불성립",
    188: "제과 감가상각 결합은 Depreciation 불성립",
    190: "비상 대응 일정표 결합은 Panic 다의어 불명확",
    191: "수영장 관리 소견 결합 불명확",
    192: "서핑 권고 결합 불명확",
    194: "상처 드레싱 선물 결합 불성립 - Gift",
    195: "파산 리트리트 결합 불성립",
    196: "화물 통합 토너먼트 결합 불성립",
    198: "베이글 대장간 결합은 Forge 추상 불성립",
    199: "도넛 관문 결합은 Portal 추상 불성립",
    200: "에스프레소 플레이북 결합은 Playbook 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 29, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 171, len(REJECT_REASON)
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
