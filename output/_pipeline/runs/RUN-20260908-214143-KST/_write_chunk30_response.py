import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk29_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk29_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.7, "구충제 투여 교육으로 실재 (도메인 실무 개념)"),
    2: (0.6, "치실 사용법 핸드북으로 실재 (Handbook 라인)"),
    19: (0.6, "제빵 레시피로 명확 (레시피 관리 독해)"),
    22: (0.7, "약국 복약 상담 교육으로 실재 (도메인 실무 개념)"),
    23: (0.6, "커패시터 유지보수 핸드북으로 실재 (Handbook 라인)"),
    31: (0.6, "유사 매물 세미나 전단으로 실재 (Seminar 연동 Flyer)"),
    33: (0.6, "에스프레소 클래스 센터로 실재 (Center 클래스 공간 라인)"),
    45: (0.6, "일몰 시간 확인으로 성립 (Chart/Calendar 계열)"),
    52: (0.6, "타코 트럭 청구서로 성립 (Bill 라인)"),
    61: (0.6, "교정 치료 예약 확정서로 성립 (Confirmation 라인)"),
    63: (0.6, "위생 치료 계획으로 성립 (Plan 라인)"),
    84: (0.6, "치주 도해 자료로 실재 (Diagram 실무 자료)"),
    85: (0.7, "선석 예약 운용 교육으로 실재 (도메인 실무 개념)"),
    92: (0.6, "퇴거 세미나 전단으로 실재 (Seminar 연동 Flyer)"),
    93: (0.7, "처방 상담 교육으로 실재 (도메인 실무 개념)"),
    94: (0.6, "컨테이너 운송 핸드북으로 실재 (Handbook 라인)"),
    103: (0.7, "서빙 서비스 교육으로 실재 (도메인 실무 개념)"),
    104: (0.6, "구충제 투여 핸드북으로 실재 (Handbook 라인)"),
    124: (0.7, "헤어 커트 교육으로 실재 (도메인 실무 개념)"),
    125: (0.6, "복약 상담 핸드북으로 실재 (Handbook 라인)"),
    154: (0.6, "타코 트럭 영수증으로 성립 (Receipt 라인)"),
    185: (0.6, "치수 치료 매뉴얼로 실재 (Manual 라인)"),
    186: (0.6, "치주 도해 자료로 실재 (Diagram 계열)"),
    187: (0.7, "복약 순응도 교육으로 실재 (도메인 실무 개념)"),
    188: (0.6, "선석 운용 핸드북으로 실재 (Handbook 라인)"),
    196: (0.6, "처방 상담 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    3: "책읽기 일정표 결합 불명확",
    4: "소파 클리닝 소견 결합 불명확",
    5: "컬러링 권고 결합 불명확",
    6: "연고 세미나 결합 불명확",
    7: "가습기 선물 결합 불성립 - Gift",
    8: "조합 자물쇠 리트리트 결합 불성립",
    9: "어휘 토너먼트 결합 불성립",
    10: "이사 정산 전단 결합 불명확",
    11: "카페 기반 결합은 Base 추상 불성립",
    12: "다이너 플레이북 결합은 Playbook 전면 기각",
    13: "비스트로 태그 결합은 Tag 다의어 불성립",
    14: "피자집 한도 결합은 Quota 속성어 불성립",
    15: "데리 벌금 결합은 Fine 불성립",
    16: "디저트 라벨 결합은 Label 불성립",
    17: "포장 결과 결합은 Result 불성립",
    18: "브런치 검증 결합은 Validation 불성립",
    20: "제과 압력 속성 결합은 Pressure 불성립",
    21: "베이글 감가상각 결합은 Depreciation 불성립",
    24: "스마트 도어락 일정표 결합 불명확",
    25: "클럽하우스 소견 결합 불명확",
    26: "스키 권고 결합 불명확",
    27: "연주 곡목 세미나 결합 불명확",
    28: "병원 선물 결합 불성립 - Gift",
    29: "상속 리트리트 결합 불성립",
    30: "벌크 토너먼트 결합 불성립",
    32: "도넛 대장간 결합은 Forge 추상 불성립",
    34: "라떼 보조원 결합은 Assistant 불성립",
    35: "칫솔 스케줄러 결합은 Scheduler 불성립",
    36: "스노클링 등기부 결합은 Register 다의어 불성립",
    37: "칵테일 탐색기 결합은 Finder 불성립",
    38: "치약 사무실 결합은 Office 불성립",
    39: "카약 키오스크 결합은 Kiosk 불성립",
    40: "바리스타 차트 결합은 Chart 불성립",
    41: "구강청격 창고 결합은 Bin 다의어 불성립",
    42: "폭포 전광판 결합은 Ticker 불성립",
    43: "펍 서식 결합은 Form 다의어 불성립",
    44: "마우스가드 카드 결합은 Card 다의어 불성립",
    46: "스테이크하우스 상태 결합은 Status 불성립",
    47: "스마일 뷰 결합은 View 추상 불성립",
    48: "수변 파일 결합은 File 다의어 불성립",
    49: "스시 초안 결합은 Draft 다의어 불성립",
    50: "호흡 요약 결합은 Summary 불성립",
    51: "보드워크 알림 결합은 Reminder 불성립",
    53: "코골이 영수증 결합 불성립",
    54: "해변 목록 결합은 List 불성립",
    55: "면집 슬롯 결합은 Slot 다의어 불성립",
    56: "교합 통행 결합은 Pass 다의어 불성립",
    57: "전망 배지 결합은 Badge 다의어 불성립",
    58: "해산물 한도 결합은 Quota 속성어 불성립",
    59: "치과 탭 결합은 Tab 다의어 불성립",
    60: "배낭여행 요약 결합은 Brief 다의어 불성립",
    62: "패러세일링 입장 결합은 Entry 다의어 불성립",
    64: "야생동물 가격 속성 결합은 Price 불성립",
    65: "치실 대출 결합은 Loan 불성립",
    66: "라군 부채 결합은 Debt 불성립",
    67: "치석 판매 결합은 Sale 다의어 불성립",
    68: "빙하 의무 결합은 Duty 불성립",
    69: "불소 가치 속성 결합은 Value 불성립",
    70: "화산 마진 속성 결합은 Margin 불성립",
    71: "실런트 버전 결합은 Version 불성립",
    72: "당일여행 규칙 결합은 Rule 불성립",
    73: "치은염 분류 결합은 Category 불성립",
    74: "요트 필드 결합은 Field 불성립",
    75: "이갈이 토큰 결합은 Token 불성립",
    76: "산책로 마커 결합은 Marker 불성립",
    77: "구취 자산 결합은 Asset 불성립",
    78: "우릴 기한 결합은 Due 불성립",
    79: "치주염 연체 결합은 Arrears 불성립",
    80: "사막 벌칙 결합은 Penalty 불성립",
    81: "부정교합 상환 결합은 Redemption 불성립",
    82: "와이너리 시험 결합은 Trial 다의어 불성립",
    83: "치수과 라벨 결합은 Label 불성립",
    86: "압축기 소견 결합 불명확",
    87: "도어 실린더 권고 결합 불명확",
    88: "인화 교정쇄 세미나 결합 불명확",
    89: "짐 풀기 선물 결합 불성립 - Gift",
    90: "인화 교정쇄 리트리트 결합은 Proof 다의어 불성립",
    91: "초대장 토너먼트 결합 불성립",
    95: "자격 인증 일정표 결합 불명확",
    96: "매장량 소견 결합은 Reserve 다의어 불성립",
    97: "송풍기 권고 결합 불명확",
    98: "자물쇠 세미나 결합 불명확",
    99: "통역 선물 결합 불성립 - Gift",
    100: "이사 경로 리트리트 결합은 Route 추상 불성립",
    101: "사진 조명 토너먼트 결합 불성립",
    102: "하객 선물 전단 결합은 Favor 다의어 불명확",
    105: "치실 일정표 결합 불명확",
    106: "책읽기 소견 결합 불명확",
    107: "소파 클리닝 권고 결합 불명확",
    108: "컬러링 세미나 결합 불명확",
    109: "연고 선물 결합 불성립 - Gift",
    110: "가습기 리트리트 결합 불성립",
    111: "조합 자물쇠 토너먼트 결합 불성립",
    112: "어휘 전단 결합 불성립",
    113: "카페 핵심 결합은 Core 추상 불성립",
    114: "다이너 일지 결합은 Journal 다의어 불성립",
    115: "비스트로 프로필 결합 불성립",
    116: "피자집 탭 결합은 Tab 다의어 불성립",
    117: "데리 번호 속성 결합은 Number 불성립",
    118: "디저트 매뉴얼 결합 불명확",
    119: "포장 연승 결합은 Streak 불성립",
    120: "브런치 탐색 결합은 Lookup 불성립",
    121: "베이커리 영상 결합 불명확",
    122: "제과 적재 결합은 Load 불성립",
    123: "베이글 사직 결합은 Resignation 불성립",
    126: "커패시터 일정표 결합 불명확",
    127: "스마트 도어락 소견 결합 불명확",
    128: "클럽하우스 권고 결합 불명확",
    129: "스키 세미나 결합 불명확",
    130: "연주 곡목 선물 결합 불성립 - Gift",
    131: "병원 리트리트 결합 불성립",
    132: "상속 토너먼트 결합 불성립",
    133: "벌크 전단 결합 불명확",
    134: "도넛 폭포 결합은 Cascade 추상 불성립",
    135: "에스프레소 구역 결합은 Zone 불성립",
    136: "라떼 플래너 결합은 Planner 불성립",
    137: "칫솔 감시자 결합은 Monitor 불성립",
    138: "스노클링 작전 결합은 Ops 불성립",
    139: "칵테일 사무실 결합은 Office 불성립",
    140: "치약 계수기 결합은 Counter 다의어 불성립",
    141: "카약 만 결합은 Bay 다의어 불성립",
    142: "바리스타 창고 결합은 Bin 다의어 불성립",
    143: "구강청격 여권 결합은 Passport 다의어 불성립",
    144: "폭포 선 결합은 Line 불성립",
    145: "펍 카드 결합은 Card 다의어 불성립",
    146: "마우스가드 시트 결합은 Sheet 다의어 불성립",
    147: "일몰 점수 결합은 Score 불성립",
    148: "스테이크하우스 뷰 결합은 View 추상 불성립",
    149: "스마일 역사 결합 불성립",
    150: "수변 수준 속성 결합은 Level 불성립",
    151: "스시 요약 결합은 Summary 불성립",
    152: "호흡 타임라인 결합 불성립",
    153: "보드워크 색인 결합은 Index 다의어 불성립",
    155: "코골이 코드 결합은 Code 불성립",
    156: "해변 식탁 결합은 travel Table 불성립",
    157: "면집 통행 결합은 Pass 다의어 불성립",
    158: "교합 바우처 결합은 치과 바우처 불성립",
    159: "전망 전표 결합은 Stub 다의어 불성립",
    160: "해산물 탭 결합은 Tab 다의어 불성립",
    161: "치과 회람 결합은 Bulletin 다의어 불성립",
    162: "배낭여행 회람 결합은 Circular 다의어 불성립",
    163: "교정의 정리 결합은 Recap 다의어 불성립",
    164: "패러세일링 요금 속성 결합은 Fee 불성립",
    165: "치위 비용 속성 결합은 Cost 불성립",
    166: "야생동물 운임 속성 결합은 Fare 불성립",
    167: "치실 합계 결합은 Sum 불성립",
    168: "라군 기금 결합은 Fund 불성립",
    169: "치석 청구 결합은 Charge 다의어 불성립",
    170: "빙하 수당 결합은 Allowance 불성립",
    171: "불소 지분 결합은 Stake 불성립",
    172: "화산 벌금 결합은 Fine 불성립",
    173: "실런트 링크 결합은 Link 불성립",
    174: "당일여행 세부 결합은 Detail 불성립",
    175: "치은염 속성 결합은 Attribute 불성립",
    176: "요트 형식 결합은 Format 불성립",
    177: "이갈이 서명 결합은 Signature 불성립",
    178: "산책로 잔액 결합은 Balance 불성립",
    179: "구취 과세 결합은 Levy 불성립",
    180: "우릴 보조금 결합은 Subsidy 불성립",
    181: "치주염 선수금 결합은 Advance 불성립",
    182: "사막 가산율 결합은 Markup 불성립",
    183: "부정교합 연장 결합은 Extension 불성립",
    184: "와이너리 그래프 결합은 Graph 불성립",
    189: "압축기 권고 결합 불명확",
    190: "도어 실린더 세미나 결합 불명확",
    191: "인화 교정쇄 선물 결합 불성립 - Gift",
    192: "짐 풀기 리트리트 결합 불성립",
    193: "인화 교정쇄 토너먼트 결합은 Proof 다의어 불성립",
    194: "초대장 전단 결합 불명확",
    195: "일정 교육 결합은 Schedule 추상 불명확",
    197: "컨테이너 일정표 결합 불명확",
    198: "자격 인증 소견 결합 불명확",
    199: "매장량 권고 결합은 Reserve 다의어 불성립",
    200: "송풍기 세미나 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 26, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 174, len(REJECT_REASON)
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
