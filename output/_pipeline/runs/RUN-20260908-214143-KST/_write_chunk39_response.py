import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk38_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk38_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "바닥재 시공 서비스 전단으로 실재 (Flyer 라인)"),
    6: (0.6, "비스트로 청구서로 성립 (Bill 라인)"),
    14: (0.7, "상처 드레싱 교육으로 실재 (도메인 실무 개념)"),
    15: (0.6, "파산 절차 핸드북으로 실재 (Handbook 라인)"),
    19: (0.6, "연공제 세미나로 실재 (Seminar 라인)"),
    23: (0.6, "저자 출간 지원 안내 전단으로 실재 (Flyer 라인)"),
    25: (0.6, "도넛 만들기 체험 스튜디오로 성립 (Studio 라인)"),
    29: (0.6, "스노클링 스팟 해도로 성립 (Chart 라인 준용)"),
    47: (0.6, "해변 리조트 예약 확정서로 성립 (Confirmation 라인)"),
    78: (0.7, "인프라 프로비저닝 교육으로 실재 (도메인 실무 개념)"),
    86: (0.7, "보안 패치 관리 교육으로 실재 (도메인 실무 개념)"),
    91: (0.6, "영양 상담 서비스 전단으로 실재 (Flyer 라인)"),
    92: (0.7, "차량 하부 세척 교육으로 실재 (도메인 실무 개념)"),
    93: (0.6, "배수관 시공 핸드북으로 실재 (Handbook 라인)"),
    99: (0.6, "급여 압류 처리 세미나 안내 전단으로 실재 (Flyer 라인)"),
    102: (0.6, "비스트로 영수증으로 성립 (Receipt 라인)"),
    110: (0.7, "템포 훈련 교육으로 실재 (도메인 실무 개념)"),
    111: (0.6, "상처 드레싱 핸드북으로 실재 (Handbook 라인)"),
    115: (0.6, "보험 수익자 설계 세미나로 실재 (Seminar 라인)"),
    134: (0.6, "일몰 투어 견적으로 성립 (Estimate 라인 준용)"),
    164: (0.6, "이갈이 치료 매뉴얼로 실재 (Manual 라인)"),
    166: (0.6, "구취 스케치 자료로 실재 (Sketch 라인)"),
    174: (0.7, "위협 분석 교육으로 실재 (도메인 실무 개념)"),
    175: (0.6, "인프라 프로비저닝 핸드북으로 실재 (Handbook 라인)"),
    182: (0.7, "통신 서비스 개통 교육으로 실재 (도메인 실무 개념)"),
    183: (0.6, "보안 패치 관리 핸드북으로 실재 (Handbook 라인)"),
    188: (0.7, "수영장 동절기 관리 교육으로 실재 (도메인 실무 개념)"),
    189: (0.6, "차량 하부 세척 핸드북으로 실재 (Handbook 라인)"),
    195: (0.6, "배상책임 보험 안내 전단으로 실재 (Flyer 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "배상책임 리트리트 결합 불성립",
    2: "급여 압류 토너먼트 결합 불성립",
    4: "카페 사슬 결합은 Chain 다의어 불명확",
    5: "다이너 여권 결합은 Passport 다의어 불성립",
    7: "피자집 대출 결합은 Loan 불성립",
    8: "데리 과세 결합은 Levy 불성립",
    9: "디저트 변환기 결합은 Converter 추상 불성립",
    10: "포장 양식 결합은 Template 불성립",
    11: "브런치 수정 결합은 Revision 불성립",
    12: "베이커리 시간 결합은 Time 불성립",
    13: "제과 행렬 결합은 Matrix 불성립",
    16: "화물 통합 일정표 결합 불명확",
    17: "홈 스테이징 소견 결합 불명확",
    18: "보험 수익자 권고 결합 불명확",
    20: "방수 선물 결합 불성립 - Gift",
    21: "멘토링 리트리트 결합 불성립",
    22: "통행금지 토너먼트 결합은 Curfew 불성립",
    24: "베이글 책상 결합은 Desk 불성립",
    26: "에스프레소 계획기 결합은 Planner 추상 불성립",
    27: "라떼 만 결합은 Bay 불성립",
    28: "칫솔 항구 결합은 Harbor 불성립",
    30: "칵테일 보고서 결합은 Report 불성립",
    31: "치약 기록 결합은 Log 다의어 불성립",
    32: "카약 시트 결합은 Sheet 다의어 불성립",
    33: "바리스타 상태 결합은 Status 다의어 불성립",
    34: "구강청격 뷰 결합은 View 다의어 불성립",
    35: "폭포 수준 속성 결합은 Level 불성립",
    36: "펍 타임라인 결합 불성립",
    37: "마우스가드 알림 결합은 Reminder 불성립",
    38: "일몰 티켓 결합 불성립",
    39: "스테이크하우스 코드 결합은 Code 불성립",
    40: "스마일 목록 결합은 List 불성립",
    41: "수변 전표 결합은 Slip 다의어 불성립",
    42: "스시 배지 결합은 Badge 다의어 불성립",
    43: "호흡 전표 결합은 Stub 다의어 불성립",
    44: "보드워크 메모 결합은 Memo 다의어 불성립",
    45: "타코 회람 결합은 Circular 다의어 불성립",
    46: "코골이 권고 결합은 Advisory 불성립",
    48: "면집 품목 결합은 Item 다의어 불성립",
    49: "교합 단위 결합은 Unit 다의어 불성립",
    50: "전망 비용 속성 결합은 Cost 불성립",
    51: "해산물 대출 결합은 Loan 불성립",
    52: "치과 합계 결합은 Sum 불성립",
    53: "배낭여행 기금 결합은 Fund 불성립",
    54: "교정의 의무 결합은 Duty 불성립",
    55: "패러세일링 관세 결합은 Tariff 불성립",
    56: "치위 벌금 결합은 Fine 불성립",
    57: "야생동물 버전 결합은 Version 불성립",
    58: "치실 세부 결합은 Detail 불성립",
    59: "라군 분류 결합은 Category 불성립",
    60: "치석 형식 결합은 Format 불성립",
    61: "빙하 토큰 결합은 Token 불성립",
    62: "불소 잔액 결합은 Balance 불성립",
    63: "화산 자산 결합은 Asset 불성립",
    64: "실런트 보조금 결합은 Subsidy 불성립",
    65: "당일여행 연체 결합은 Arrears 불성립",
    66: "치은염 가산율 결합은 Markup 불성립",
    67: "요트 연장 결합은 Extension 불성립",
    68: "이갈이 라벨 결합은 Label 불성립",
    69: "산책로 워크시트 결합 불명확",
    70: "구취 배치도 결합은 Layout 불성립",
    71: "우릴 개요 결합은 Outline 불성립",
    72: "치주염 키트 결합은 Kit 불성립",
    73: "사막 메시지 결합은 Message 불성립",
    74: "부정교합 위젯 결합은 Widget 불성립",
    75: "와이너리 공지 결합은 Announcement 불성립",
    76: "치수과 변환기 결합은 Converter 추상 불성립",
    77: "치주 견적기 결합은 Estimator 추상 불성립",
    79: "대기열 핸드북 결합은 Queue 추상 불명확",
    80: "인재 소싱 일정표 결합 불명확",
    81: "명찰 소견 결합은 Badge 다의어 불명확",
    82: "트레이드 권고 결합은 Trade 다의어 불명확",
    83: "수의 처방 선물 결합 불성립 - Gift",
    84: "치료 리트리트 결합은 Treatment 추상 불성립",
    85: "결제 전단 결합은 Billing 추상 불명확",
    87: "설정 핸드북 결합은 Configuration 추상 불명확",
    88: "채팅 일정표 결합은 Chat 추상 불명확",
    89: "물류 권고 결합은 Logistics 추상 불명확",
    90: "알레르기 선물 결합 불성립 - Gift",
    94: "관광객 일정표 결합은 Tourist 불명확",
    95: "타악기 소견 결합 불명확",
    96: "운송 경로 선물 결합은 Lane 다의어 불성립",
    97: "부동산 점검 리트리트 결합은 Walkthrough 다의어 불성립",
    98: "배상책임 토너먼트 결합 불성립",
    100: "카페 고리 결합은 Ring 불성립",
    101: "다이너 로비 결합은 Lobby 다의어 불성립",
    103: "피자집 합계 결합은 Sum 불성립",
    104: "데리 기한 결합은 Due 불성립",
    105: "디저트 생성기 결합은 Generator 추상 불성립",
    106: "포장 가이드 결합은 Guide 추상 불성립",
    107: "브런치 결제 결합은 Payment 불성립",
    108: "베이커리 속도 속성 결합은 Speed 불성립",
    109: "제과 평가 결합은 Evaluation 불성립",
    112: "파산 일정표 결합 불명확",
    113: "화물 통합 소견 결합 불명확",
    114: "홈 스테이징 권고 결합 불명확",
    116: "연공 선물 결합 불성립 - Gift",
    117: "방수 리트리트 결합 불성립",
    118: "멘토링 토너먼트 결합 불성립",
    119: "통행금지 전단 결합은 Curfew 불명확",
    120: "베이글 레이더 결합은 Radar 추상 불성립",
    121: "도넛 실험실 결합은 Lab 추상 불성립",
    122: "에스프레소 일정관리자 결합은 Scheduler 추상 불성립",
    123: "라떼 게시 결합은 Post 다의어 불성립",
    124: "칫솔 명단 결합은 Roster 다의어 불성립",
    125: "스노클링 창고 결합은 Bin 다의어 불성립",
    126: "칵테일 기록 결합은 Log 다의어 불성립",
    127: "치약 서식 결합은 Form 다의어 불성립",
    128: "카약 점검 결합은 Check 불성립",
    129: "바리스타 뷰 결합은 View 다의어 불성립",
    130: "구강청격 이력 결합은 History 불성립",
    131: "폭포 요율 속성 결합은 Rate 불성립",
    132: "펍 알림 결합은 Reminder 불성립",
    133: "마우스가드 색인 결합은 Index 다의어 불성립",
    135: "스테이크하우스 목록 결합은 List 불성립",
    136: "스마일 식탁 결합은 Table 다의어 불성립",
    137: "수변 샘플 결합은 Sample 다의어 불성립",
    138: "스시 전표 결합은 Stub 다의어 불성립",
    139: "호흡 정산 결합은 Statement 다의어 불성립",
    140: "보드워크 한도 결합은 Quota 불성립",
    141: "타코 권고 결합은 Advisory 불성립",
    142: "코골이 청원 결합은 Petition 불성립",
    143: "해변 요약 결합은 Recap 불성립",
    144: "면집 단위 결합은 Unit 다의어 불성립",
    145: "교합 계획 결합은 Bite 다의어 불명확",
    146: "전망 가격 속성 결합은 Price 불성립",
    147: "해산물 합계 결합은 Sum 불성립",
    148: "치과 부채 결합은 Debt 불성립",
    149: "배낭여행 현금 결합은 Cash 불성립",
    150: "교정의 수당 결합은 Allowance 불성립",
    151: "패러세일링 가치 속성 결합은 Value 불성립",
    152: "치위 번호 속성 결합은 Number 불성립",
    153: "야생동물 링크 결합은 Link 불성립",
    154: "치실 식별자 결합은 Identifier 불성립",
    155: "라군 속성 결합은 Attribute 불성립",
    156: "치석 일련번호 결합은 Serial 불성립",
    157: "빙하 서명 결합은 Signature 불성립",
    158: "불소 이자 결합은 Interest 불성립",
    159: "화산 과세 결합은 Levy 불성립",
    160: "실런트 할인 결합은 Discount 불성립",
    161: "당일여행 선수금 결합은 Advance 불성립",
    162: "치은염 리딤 결합은 Redemption 불성립",
    163: "요트 시험 결합은 Trial 다의어 불성립",
    165: "산책로 도해 결합 불명확",
    167: "우릴 렌더링 결합은 Rendering 불성립",
    168: "치주염 횟수 결합은 Count 불성립",
    169: "사막 총액 결합은 Total 불성립",
    170: "부정교합 저장소 결합은 Repository 불성립",
    171: "와이너리 계산기 결합은 Calculator 추상 불성립",
    172: "치수과 생성기 결합은 Generator 추상 불성립",
    173: "치주 점검기 결합은 Checker 추상 불성립",
    176: "대기열 일정표 결합은 Queue 추상 불명확",
    177: "인재 소싱 소견 결합 불명확",
    178: "명찰 권고 결합은 Badge 다의어 불명확",
    179: "트레이드 세미나 결합은 Trade 다의어 불명확",
    180: "수의 처방 리트리트 결합 불성립",
    181: "치료 토너먼트 결합은 Treatment 추상 불성립",
    184: "설정 일정표 결합은 Configuration 추상 불명확",
    185: "채팅 소견 결합은 Chat 추상 불명확",
    186: "물류 세미나 결합은 Logistics 추상 불명확",
    187: "알레르기 리트리트 결합 불성립",
    190: "배수관 일정표 결합 불명확",
    191: "관광객 소견 결합은 Tourist 불명확",
    192: "타악기 권고 결합 불명확",
    193: "운송 경로 리트리트 결합은 Lane 다의어 불성립",
    194: "부동산 점검 토너먼트 결합은 Walkthrough 다의어 불성립",
    196: "카페 관문 결합은 Gate 불성립",
    197: "다이너 전광판 결합은 Ticker 불성립",
    198: "비스트로 코드 결합은 Code 불성립",
    199: "피자집 부채 결합은 Debt 불성립",
    200: "데리 보조금 결합은 Subsidy 불성립",
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
