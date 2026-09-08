import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk21_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk21_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "놀이터 안내 전단으로 실재 (Flyer 라인)"),
    12: (0.6, "펍 주문 키오스크로 실재 (Kiosk 실물 단말)"),
    36: (0.6, "치석 제거 예약 확정서로 성립 (Confirmation 라인)"),
    54: (0.6, "결제 절차 안내 교육으로 실재 (Tutorial 라인)"),
    55: (0.6, "계약 수정 핸드북으로 실재 (Handbook 라인)"),
    58: (0.6, "연차 제도 세미나로 실재 (Seminar 라인)"),
    62: (0.6, "채점 연수 안내 전단으로 실재 (Flyer 라인)"),
    63: (0.7, "환자 동의 절차 교육으로 실재 (도메인 실무 개념)"),
    64: (0.6, "에스크로 핸드북으로 실재 (Handbook 라인)"),
    71: (0.6, "연수기 설치 교육으로 실재 (Tutorial 라인)"),
    72: (0.6, "여행자 가이드북으로 실재 (Handbook 라인)"),
    80: (0.6, "도장 시공 안내 전단으로 실재 (Flyer 라인)"),
    89: (0.6, "베이커리 청구서로 성립 (Invoice 청구 문서)"),
    92: (0.6, "스토리텔링 교육으로 실재 (Tutorial 라인)"),
    93: (0.6, "인턴십 핸드북으로 실재 (Handbook 라인)"),
    128: (0.6, "치과 치료 청구서로 성립 (Bill 실물 청구)"),
    138: (0.6, "불소 도포 계획으로 성립 (Plan 라인)"),
    154: (0.6, "결제 핸드북으로 실재 (Handbook 라인)"),
    157: (0.6, "보험 보장 세미나로 실재 (Seminar 라인)"),
    162: (0.6, "클라리넷 레슨 튜토리얼로 실재 (Tutorial 라인)"),
    163: (0.6, "환자 동의 핸드북으로 실재 (Handbook 라인)"),
    172: (0.6, "연수기 핸드북으로 실재 (Handbook 라인)"),
    180: (0.6, "퇴직 안내 전단으로 실재 (Flyer 라인)"),
    184: (0.6, "피자집 계산서로 성립 (Bill 실물 청구)"),
    192: (0.6, "국민투표 절차 교육으로 실재 (Tutorial 라인)"),
    193: (0.6, "스토리 핸드북으로 실재 (Handbook 라인)"),
    197: (0.6, "도넛 만들기 세미나로 실재 (Seminar 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "에스프레소 고리 결합은 Loop 불성립",
    3: "라떼 구역 결합은 Zone 불성립",
    4: "칫솔 콘솔 결합은 Console 불성립",
    5: "스노클링 경로 결합은 Route 불성립",
    6: "칵테일 관리인 결합은 Keeper 불성립",
    7: "치약 관리자 결합은 Manager 불성립",
    8: "카약 플래너 결합은 Planner 불성립",
    9: "바리스타 플레이북 결합은 Playbook 불성립",
    10: "구강청격 일지 결합은 Journal 불성립",
    11: "폭표 디렉터리 결합 불성립",
    13: "마우스가드 만 결합은 Bay 불성립",
    14: "일몰 항구 결합은 Harbor 불성립",
    15: "스테이크하우스 여권 결합은 Passport 다의어 불성립",
    16: "스마일 로비 결합은 Lobby 불성립",
    17: "수변 라인 결합은 Line 다의어 불성립",
    18: "스시 서식 결합은 Form 다의어 불성립",
    19: "호흡 카드 결합은 Card 다의어 불성립",
    20: "보드워크 점검 결합 불성립",
    21: "타코 상태 결합은 Status 불성립",
    22: "코골이 뷰 결합은 View 추상 불성립",
    23: "해변 파일 결합은 File 불성립",
    24: "면집 피드 결합은 Feed 추상 불성립",
    25: "교합 초안 결합은 Draft 다의어 불성립",
    26: "전망 타임라인 결합 불성립",
    27: "해산물 견적 결합 불명확",
    28: "치과 주문 결합은 Order 다의어 불성립",
    29: "배낭여행 영수증 결합 불명확",
    30: "교정의 전표 결합은 Slip 다의어 불성립",
    31: "패러세일링 슬롯 결합은 Slot 다의어 불성립",
    32: "치위 전표 결합은 Stub 불성립",
    33: "야생동물 메모 결합은 Memo 다의어 불성립",
    34: "치실 회람 결합은 Bulletin 다의어 불성립",
    35: "라군 회람 결합은 Circular 다의어 불성립",
    37: "빙하 입장 결합은 Entry 다의어 불성립",
    38: "불소 단위 결합은 Unit 다의어 불성립",
    39: "화산 비용 속성 결합은 Cost 불성립",
    40: "실런트 세금 결합은 Tax 불성립",
    41: "당일여행 합계 결합은 Sum 불성립",
    42: "치은염 현금 결합은 Cash 불성립",
    43: "요트 청구 결합은 Charge 다의어 불성립",
    44: "이갈이 관세 결합은 Tariff 불성립",
    45: "산책로 지분 결합은 Stake 불성립",
    46: "구취 번호 속성 결합은 Number 불성립",
    47: "우릴 링크 결합은 Link 불성립",
    48: "치주염 식별자 결합은 Identifier 불성립",
    49: "사막 속성 결합은 Attribute 불성립",
    50: "부정교합 형식 결합은 Format 불성립",
    51: "와이너리 토큰 결합은 Token 불성립",
    52: "치수과 표식 결합은 Marker 불성립",
    53: "치주과 자산 결합은 Asset 불성립",
    56: "팔레트 일정표 결합 불명확",
    57: "보험 보장 권고 결합 불명확",
    59: "건설 변경 선물 결합 불성립 - Gift",
    60: "공급업체 리트리트 결합 불성립",
    61: "컨시어지 토너먼트 결합 불성립",
    65: "법령 일정표 결합 불명확",
    66: "백오더 소견 결합 불명확",
    67: "보험 바인더 세미나 결합은 Binder 다의어 불성립",
    68: "인사 고과 선물 결합 불성립 - Gift",
    69: "유치권 리트리트 결합 불성립",
    70: "번들 토너먼트 결합 불성립",
    73: "만돌린 일정표 결합 불명확",
    74: "접종 소견 결합 불명확",
    75: "송금 권고 결합 불명확",
    76: "트레일러 세미나 결합 불명확",
    77: "조건부 계약 선물 결합 불성립 - Gift",
    78: "보험 배상 리트리트 결합 불성립",
    79: "퇴직 토너먼트 결합 불성립",
    81: "카페 나침반 결합은 Compass 불성립",
    82: "다이너 사슬 결합은 Chain 불성립",
    83: "비스트로 수거함 결합은 Bin 불성립",
    84: "피자집 주문 결합은 Order 다의어 불성립",
    85: "데리 운임 결합은 Fare 불성립",
    86: "디저트 잔액 결합은 Balance 불성립",
    87: "포장 위젯 결합은 Widget 불성립",
    88: "브런치 예보 결합은 Forecast 불성립",
    90: "제과 체크인 결합 불성립",
    91: "베이글 상태 결합은 Condition 불성립",
    94: "출석 일정표 결합 불명확",
    95: "변속기 소견 결합 불명확",
    96: "도넛 권고 결합 불명확",
    97: "안락사 세미나 결합 불명확",
    98: "임플란트 선물 결합 불성립 - Gift",
    99: "자장가 리트리트 결합 불성립",
    100: "스타일 토너먼트 결합 불성립",
    101: "대체약 전단 결합 불명확",
    102: "에스프레소 격자 결합은 Grid 불성립",
    103: "라떼 포털 결합은 Portal 불성립",
    104: "칫솔 패널 결합은 Panel 불성립",
    105: "스노클링 레일 결합은 Rail 불성립",
    106: "칵테일 관리자 결합은 Manager 불성립",
    107: "치약 엔진 결합은 Engine 추상 불성립",
    108: "카약 스케줄러 결합은 Scheduler 불성립",
    109: "바리스타 일지 결합은 Journal 불성립",
    110: "구강청격 등록부 결합은 Registry 불성립",
    111: "폭포 탐색기 결합은 Locator 불성립",
    112: "펍 만 결합은 Bay 불성립",
    113: "마우스가드 게시 결합은 Post 다의어 불성립",
    114: "일몰 명단 결합은 Roster 불성립",
    115: "스테이크하우스 로비 결합은 Lobby 불성립",
    116: "스마일 전광판 결합은 Ticker 불성립",
    117: "수변 창 결합은 Window 불성립",
    118: "스시 카드 결합은 Card 다의어 불성립",
    119: "호흡 시트 결합은 Sheet 다의어 불성립",
    120: "보드워크 점수 결합은 Score 불성립",
    121: "타코 뷰 결합은 View 추상 불성립",
    122: "코골이 역사 결합 불성립",
    123: "해변 수준 속성 결합은 Level 불성립",
    124: "면집 초안 결합은 Draft 다의어 불성립",
    125: "교합 요약 결합은 Summary 불성립",
    126: "전망 알림 결합은 Reminder 불성립",
    127: "해산물 주문 결합은 Order 다의어 불성립",
    129: "배낭여행 코드 결합은 Code 불성립",
    130: "교정의 샘플 결합은 Sample 다의어 불성립",
    131: "패러세일링 통행 결합은 Pass 다의어 불성립",
    132: "치위 정산 결합은 Statement 불성립",
    133: "야생동물 한도 결합은 Quota 속성어 불성립",
    134: "치실 요약 결합은 Brief 다의어 불성립",
    135: "라군 권고 결합은 Advisory 불성립",
    136: "치석 정리 결합은 Recap 다의어 불성립",
    137: "빙하 요금 결합은 Fee 불성립",
    139: "화산 가격 속성 결합은 Price 불성립",
    140: "실런트 대출 결합은 Loan 불성립",
    141: "당일여행 부채 결합은 Debt 불성립",
    142: "치은염 판매 결합은 Sale 다의어 불성립",
    143: "요트 의무 결합은 Duty 불성립",
    144: "이갈이 가치 결합은 Value 불성립",
    145: "산책로 마진 속성 결합은 Margin 불성립",
    146: "구취 버전 결합은 Version 불성립",
    147: "우릴 규칙 결합은 Rule 불성립",
    148: "치주염 분류 결합은 Category 불성립",
    149: "사막 분야 결합은 Field 불성립",
    150: "부정교합 일련번호 결합은 Serial 불성립",
    151: "와이너리 서명 결합은 Signature 불성립",
    152: "치수과 잔액 결합은 Balance 불성립",
    153: "치주과 과세 결합은 Levy 불성립",
    155: "계약 수정 일정표 결합 불명확",
    156: "팔레트 소견 결합 불명확",
    158: "연차 선물 결합 불성립 - Gift",
    159: "건설 변경 리트리트 결합은 Change 다의어 불성립",
    160: "공급업체 토너먼트 결합 불성립",
    161: "컨시어지 전단 결합 불명확",
    164: "에스크로 일정표 결합 불명확",
    165: "법령 소견 결합 불명확",
    166: "백오더 권고 결합 불명확",
    167: "보험 바인더 선물 결합 불성립 - Gift",
    168: "인사 고과 리트리트 결합은 Review 다의어 불성립",
    169: "유치권 토너먼트 결합 불성립",
    170: "번들 전단 결합 불명확",
    171: "세차 버킷 교육 결합 불명확",
    173: "여행자 일정표 결합 불명확",
    174: "만돌린 소견 결합 불명확",
    175: "접종 권고 결합 불명확",
    176: "송금 세미나 결합 불명확",
    177: "트레일러 선물 결합 불성립 - Gift",
    178: "조건부 계약 리트리트 결합 불성립",
    179: "보험 배상 토너먼트 결합 불성립",
    181: "카페 등대 결합은 Beacon 불성립",
    182: "다이너 고리 결합은 Ring 불성립",
    183: "비스트로 여권 결합은 Passport 다의어 불성립",
    185: "데리 세금 결합은 Tax 불성립",
    186: "디저트 이자 결합은 Interest 불성립",
    187: "포장 저장소 결합은 Repository 불성립",
    188: "브런치 마감 결합은 Deadline 불성립",
    189: "베이커리 갱신 결합 불성립",
    190: "제과 크기 속성 결합은 Size 불성립",
    191: "베이글 습도 결합 불성립",
    194: "인턴십 일정표 결합 불명확",
    195: "출석 소견 결합 불명확",
    196: "변속기 권고 결합 불명확",
    198: "안락사 선물 결합 불성립 - Gift",
    199: "임플란트 리트리트 결합 불성립",
    200: "자장가 토너먼트 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 27, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 173, len(REJECT_REASON)
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
