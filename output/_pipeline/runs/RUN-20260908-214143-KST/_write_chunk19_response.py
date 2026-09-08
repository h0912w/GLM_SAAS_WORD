import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk18_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk18_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    7: (0.6, "리모델링 안내 전단으로 실재 (Flyer 라인)"),
    11: (0.6, "스노클링 강습 센터로 실재 (Center 실물 시설)"),
    12: (0.6, "칵테일 바 투어 코스로 실재 (Trail 물리 코스)"),
    18: (0.6, "펍 목록으로 실재 (Directory 라인)"),
    23: (0.6, "수변 안전 경보로 성립 (Alert 라인)"),
    28: (0.6, "코골이 검사로 성립 (Check 검사 독해)"),
    37: (0.6, "패러세일링 이용 영수증으로 성립 (Receipt 라인)"),
    47: (0.6, "당일여행 일정 계획으로 성립 (Plan 라인)"),
    61: (0.6, "공급업체 핸드북으로 실재 (Handbook 라인)"),
    64: (0.6, "토양 관리 세미나로 실재 (Seminar 라인)"),
    67: (0.6, "크리에이티브 세미나 전단으로 실재 (Flyer 라인)"),
    69: (0.6, "건설 유치권 핸드북으로 실재 (도메인 실무 개념)"),
    75: (0.6, "선거 안내 전단으로 실재 (Flyer 라인)"),
    76: (0.7, "부동산 조건부 계약 교육으로 실재 (도메인 실무 개념)"),
    77: (0.6, "보험 배상 핸드북으로 실재 (Handbook 라인)"),
    81: (0.6, "예산 편성 세미나로 실재 (Seminar 라인)"),
    98: (0.6, "임플란트 관리 교육으로 실재 (Tutorial 라인)"),
    99: (0.6, "자장가 핸드북으로 실재 (Handbook 라인)"),
    103: (0.6, "카지노 게임 강습 세미나로 실재 (Seminar 라인)"),
    109: (0.6, "라떼아트 클래스 스튜디오로 실재 (Studio 클래스 공간)"),
    136: (0.6, "교정 치료 청구서로 성립 (Bill 실물 청구)"),
    144: (0.6, "불소 도포 예약 확정서로 성립 (Confirmation 라인)"),
    160: (0.6, "연차 신청 절차 교육으로 실재 (Tutorial 라인)"),
    176: (0.6, "트레일러 연결 운전 교육으로 실재 (Tutorial 라인)"),
    177: (0.7, "조건부 계약 핸드북으로 실재 (도메인 실무 개념)"),
    185: (0.6, "채용 안내 전단으로 실재 (Flyer 라인)"),
    192: (0.6, "포장 주문 완료 알림으로 성립 (Notification 라인)"),
    199: (0.6, "임플란트 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "놀이터 소견 결합 불명확",
    2: "카지노 권고 결합 불명확",
    3: "합주 세미나 결합 불명확",
    4: "부상 선물 결합 불성립 - Gift",
    5: "채권자 리트리트 결합 불성립",
    6: "냉장 컨테이너 토너먼트 결합 불성립",
    8: "에스프레소 대장간 결합은 Forge 불성립",
    9: "라떼 갑판 결합은 Deck 불성립",
    10: "칫솔 실험실 결합은 Lab 불성립",
    13: "치약 사슬 결합은 Chain 불성립",
    14: "카약 연결점 결합은 Nexus 불성립",
    15: "바리스타 플래너 결합은 Planner 불성립",
    16: "구강청격 스케줄러 결합은 Scheduler 불성립",
    17: "폭포 등기부 결합은 Register 다의어 불성립",
    19: "마우스가드 탐색기 결합은 Locator 불성립",
    20: "일몰 사무실 결합은 Office 불성립",
    21: "스테이크하우스 게시 결합은 Post 다의어 불성립",
    22: "스마일 항구 결합은 Harbor 불성립",
    24: "스시 전광판 결합은 Ticker 불성립",
    25: "호흡 라인 결합은 Line 다의어 불성립",
    26: "보드워크 굴림 결합은 Roll 불성립",
    27: "타코 시트 결합은 Sheet 다의어 불성립",
    29: "해변 메모 결합은 Note 다의어 불성립",
    30: "면집 뷰 결합은 View 추상 불성립",
    31: "교합 이력 결합 불성립",
    32: "전망 수준 속성 결합은 Level 불성립",
    33: "해산물 초안 결합은 Draft 다의어 불성립",
    34: "치과 요약 결합은 Summary 불성립",
    35: "배낭여행 알림 결합은 Reminder 불성립",
    36: "교정의 주문 결합은 Order 다의어 불성립",
    38: "치위 전표 결합은 Slip 다의어 불성립",
    39: "야생동물 슬롯 결합은 Slot 다의어 불성립",
    40: "치실 배지 결합은 Badge 불성립",
    41: "라군 정산 결합은 Statement 불성립",
    42: "치석 탭 결합은 Tab 불성립",
    43: "빙하 요약 결합은 Brief 다의어 불성립",
    44: "불소 청원 결합은 Petition 불성립",
    45: "화산 정리 결합은 Recap 다의어 불성립",
    46: "실런트 품목 결합은 Item 다의어 불성립",
    48: "치은염 운임 결합은 Fare 불성립",
    49: "요트 대출 결합은 Loan 불성립",
    50: "이갈이 기금 결합은 Fund 불성립",
    51: "산책로 판매 결합은 Sale 다의어 불성립",
    52: "구취 수당 결합은 Allowance 불성립",
    53: "우릴 가치 결합은 Value 불성립",
    54: "치주염 벌금 결합은 Fine 불성립",
    55: "사막 버전 결합은 Version 불성립",
    56: "부정교합 규칙 결합은 Rule 불성립",
    57: "와이너리 식별자 결합은 Identifier 불성립",
    58: "치수과 속성 결합은 Attribute 불성립",
    59: "치주과 일련번호 결합은 Serial 불성립",
    60: "건설 변경 결합은 Change 다의어 불명확",
    62: "컨시어지 일정표 결합 불명확",
    63: "채점 소견 결합 불명확",
    65: "약정 리트리트 결합 불성립",
    66: "공청회 토너먼트 결합 불성립",
    68: "인사 고과 교육 결합은 Review 다의어 불명확",
    70: "번들 일정표 결합 불명확",
    71: "동문 권고 결합 불명확",
    72: "처리량 세미나 결합은 Throughput 속성어 불성립",
    73: "사일로 선물 결합 불성립 - Gift",
    74: "장부 토너먼트 결합 불성립",
    78: "퇴직 일정표 결합 불명확",
    79: "도장 소견 결합 불명확",
    80: "선수과목 권고 결합 불명확",
    82: "캡션 선물 결합 불성립 - Gift",
    83: "감정 분석 리트리트 결합 불성립",
    84: "리크루터 토너먼트 결합 불성립",
    85: "랜야드 전단 결합 불성립",
    86: "카페 흐름 결합은 Flow 불성립",
    87: "다이너 콘솔 결합은 Console 불성립",
    88: "비스트로 만 결합은 Bay 불성립",
    89: "피자집 요약 결합은 Summary 불성립",
    90: "데리 요금 결합은 Fee 불성립",
    91: "디저트 분야 결합은 Field 불성립",
    92: "포장 렌더링 결합은 Rendering 불성립",
    93: "브런치 제안 결합은 Proposal 불성립",
    94: "베이커리 가용성 속성 결합은 Availability 불성립",
    95: "제과 환불 결합은 Refund 불성립",
    96: "베이글 와트 속성 결합은 Wattage 불성립",
    97: "도넛 보증인 결합은 Guarantor 불성립",
    100: "스타일 일정표 결합 불명확",
    101: "대체약 소견 결합 불명확",
    102: "놀이터 권고 결합 불명확",
    104: "합주 선물 결합 불성립 - Gift",
    105: "부상 리트리트 결합 불성립",
    106: "채권자 토너먼트 결합 불성립",
    107: "냉장 컨테이너 전단 결합 불명확",
    108: "에스프레소 폭포 결합은 Cascade 불성립",
    110: "칫솔 기지 결합은 Station 불성립",
    111: "스노클링 구역 결합은 Zone 불성립",
    112: "칵테일 사슬 결합은 Chain 불성립",
    113: "치약 고리 결합은 Ring 불성립",
    114: "카약 지도집 결합은 Atlas 불성립",
    115: "바리스타 스케줄러 결합은 Scheduler 불성립",
    116: "구강청격 감시자 결합은 Monitor 불성립",
    117: "폭표 작전 결합은 Ops 불성립",
    118: "펍 탐색기 결합은 Locator 불성립",
    119: "마우스가드 탐색기 결합은 Finder 불성립",
    120: "일몰 계수기 결합은 Counter 다의어 불성립",
    121: "스테이크하우스 항구 결합은 Harbor 불성립",
    122: "스마일 명단 결합은 Roster 불성립",
    123: "수변 도표 결합 불명확",
    124: "스시 라인 결합은 Line 다의어 불성립",
    125: "호흡 창 결합은 Window 불성립",
    126: "보드워크 리포트 결합 불성립",
    127: "타코 점검 결합 불성립",
    128: "코골이 점수 결합은 Score 불성립",
    129: "해변 태그 결합은 Tag 다의어 불성립",
    130: "면집 역사 결합 불성립",
    131: "교합 파일 결합은 File 불성립",
    132: "전망 요율 속성 결합은 Rate 불성립",
    133: "해산물 요약 결합은 Summary 불성립",
    134: "치과 타임라인 결합 불성립",
    135: "배낭여행 색인 결합은 Index 다의어 불성립",
    137: "패러세일링 코드 결합은 Code 불성립",
    138: "치위 샘플 결합은 Sample 다의어 불성립",
    139: "야생동물 통행 결합은 Pass 다의어 불성립",
    140: "치실 전표 결합은 Stub 불성립",
    141: "라군 메모 결합은 Memo 다의어 불성립",
    142: "치석 회람 결합은 Bulletin 다의어 불성립",
    143: "빙하 회람 결합은 Circular 다의어 불성립",
    145: "화산 입장 결합은 Entry 다의어 불성립",
    146: "실런트 단위 결합은 Unit 다의어 불성립",
    147: "당일여행 비용 속성 결합은 Cost 불성립",
    148: "치은염 세금 결합은 Tax 불성립",
    149: "요트 합계 결합은 Sum 불성립",
    150: "이갈이 현금 결합은 Cash 불성립",
    151: "산책로 청구 결합은 Charge 다의어 불성립",
    152: "구취 관세 결합은 Tariff 불성립",
    153: "우릴 지분 결합은 Stake 불성립",
    154: "치주염 번호 속성 결합은 Number 불성립",
    155: "사막 링크 결합은 Link 불성립",
    156: "부정교합 세부 결합은 Detail 불성립",
    157: "와이너리 분류 결합은 Category 불성립",
    158: "치수과 분야 결합은 Field 불성립",
    159: "치주과 토큰 결합은 Token 불성립",
    161: "건설 변경 핸드북 결합은 Change 다의어 불명확",
    162: "공급업체 일정표 결합 불명확",
    163: "컨시어지 소견 결합 불명확",
    164: "채점 권고 결합 불명확",
    165: "토양 선물 결합 불성립 - Gift",
    166: "약정 토너먼트 결합 불성립",
    167: "공청회 전단 결합은 Hearing 다의어 불명확",
    168: "보험 바인더 교육 결합은 Binder 다의어 불명확",
    169: "인사 고과 핸드북 결합은 Review 다의어 불명확",
    170: "유치권 일정표 결합 불명확",
    171: "번들 소견 결합 불명확",
    172: "동문 세미나 결합 불명확",
    173: "처리량 선물 결합 불성립 - Gift",
    174: "사일로 리트리트 결합 불성립",
    175: "장부 전단 결합 불명확",
    178: "보험 배상 일정표 결합 불명확",
    179: "퇴직 소견 결합 불명확",
    180: "도장 권고 결합 불명확",
    181: "선수과목 세미나 결합 불명확",
    182: "예산 선물 결합 불성립 - Gift",
    183: "캡션 리트리트 결합 불성립",
    184: "감정 분석 토너먼트 결합 불성립",
    186: "카페 허브 결합은 Hub 불성립",
    187: "다이너 패널 결합은 Panel 불성립",
    188: "비스트로 게시 결합은 Post 다의어 불성립",
    189: "피자집 타임라인 결합 불성립",
    190: "데리 품목 결합은 Item 다의어 불성립",
    191: "디저트 형식 결합은 Format 불성립",
    193: "브런치 보증 결합은 Guarantee 불성립",
    194: "베이커리 자격 속성 결합은 Eligibility 불성립",
    195: "제과 경비 결합은 Expense 불성립",
    196: "베이글 밝기 속성 결합은 Brightness 불성립",
    197: "도넛 조율기 결합은 Tuner 불성립",
    198: "안락사 교육 결합 불명확",
    200: "자장가 일정표 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 28, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 172, len(REJECT_REASON)
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
