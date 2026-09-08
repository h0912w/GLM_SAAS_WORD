import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk25_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk25_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "채점 기준 세미나로 실재 (Seminar 라인)"),
    38: (0.6, "야생동물 투어 예약 확정서로 성립 (Confirmation 라인)"),
    59: (0.7, "초대장 작성 교육으로 실재 (도메인 실무 개념)"),
    60: (0.6, "퇴거 절차 핸드북으로 실재 (Handbook 라인)"),
    67: (0.6, "계약 수정 세미나 전단으로 실재 (Flyer 라인)"),
    68: (0.7, "사진 조명 촬영 교육으로 실재 (도메인 실무 개념)"),
    77: (0.6, "에스크로 세미나 전단으로 실재 (Flyer 라인)"),
    78: (0.7, "다이얼 조합 설정 교육으로 실재 (도메인 실무 개념)"),
    79: (0.6, "어휘 학습 핸드북으로 실재 (Handbook 라인)"),
    95: (0.6, "브런치 가이드로 실재 (Guide 라인)"),
    99: (0.7, "상속 절차 교육으로 실재 (도메인 실무 개념)"),
    108: (0.6, "인턴십 안내 전단으로 실재 (Flyer 라인)"),
    116: (0.6, "카약 투어 일정 캘린더로 성립 (Calendar 라인)"),
    132: (0.6, "면요리 청구서로 성립 (Bill 실물 청구)"),
    133: (0.6, "교합 치료 영수증으로 성립 (Receipt 라인)"),
    143: (0.6, "라군 투어 계획으로 성립 (Plan 라인)"),
    163: (0.6, "초대장 작성 핸드북으로 실재 (Handbook 라인)"),
    172: (0.6, "사진 조명 촬영 핸드북으로 실재 (Handbook 라인)"),
    181: (0.7, "가습기 사용 관리 교육으로 실재 (도메인 실무 개념)"),
    182: (0.6, "다이얼 조합 설정 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "국민투표 선물 결합 불성립 - Gift",
    3: "스토리 리트리트 결합 불성립",
    4: "인턴십 토너먼트 결합 불성립",
    5: "출석 전단 결합 불명확",
    6: "도넛 흐름 결합은 Flow 추상 불성립",
    7: "에스프레소 핵심 결합은 Core 추상 불성립",
    8: "라떼 사슬 결합은 Chain 불성립",
    9: "칫솔 문 결합은 Gate 불성립",
    10: "스노클링 관리인 결합은 Keeper 불성립",
    11: "칵테일 등기부 결합은 Register 다의어 불성립",
    12: "치약 작전 결합은 Ops 불성립",
    13: "카약 등록부 결합은 Registry 불성립",
    14: "바리스타 계수기 결합은 Counter 다의어 불성립",
    15: "구강청격 부스 결합은 Booth 불성립",
    16: "폭포 게시 결합은 Post 다의어 불성립",
    17: "펍 여권 결합은 Passport 다의어 불성립",
    18: "마우스가드 로비 결합은 Lobby 불성립",
    19: "일몰 라인 결합은 Line 다의어 불성립",
    20: "스테이크하우스 서식 결합은 Form 다의어 불성립",
    21: "스마일 카드 결합은 Card 다의어 불성립",
    22: "수변 점검 결합은 Check 불성립",
    23: "스시 상태 결합은 Status 불성립",
    24: "호흡 뷰 결합은 View 추상 불성립",
    25: "보드워크 파일 결합은 File 불성립",
    26: "타코 초안 결합은 Draft 다의어 불성립",
    27: "코골이 요약 결합은 Summary 불성립",
    28: "해변 알림 결합은 Reminder 불성립",
    29: "면집 주문 결합은 Order 다의어 불성립",
    30: "교합 청구서 결합 불성립",
    31: "전망 코드 결합은 Code 불성립",
    32: "해산물 샘플 결합은 Sample 다의어 불성립",
    33: "치과 슬롯 결합은 Slot 다의어 불성립",
    34: "배낭여행 바우처 결합 불명확",
    35: "교정의 메모 결합은 Memo 다의어 불성립",
    36: "패러세일링 탭 결합은 Tab 다의어 불성립",
    37: "치위 권고 결합은 Advisory 불성립",
    39: "치실 요금 속성 결합은 Fee 불성립",
    40: "라군 단위 결합은 Unit 다의어 불성립",
    41: "치석 가격 속성 결합은 Price 불성립",
    42: "빙하 세금 결합은 Tax 불성립",
    43: "불소 부채 결합은 Debt 불성립",
    44: "화산 현금 결합은 Cash 불성립",
    45: "실런트 의무 결합은 Duty 불성립",
    46: "당일여행 관세 결합은 Tariff 불성립",
    47: "치은염 마진 속성 결합은 Margin 불성립",
    48: "요트 번호 속성 결합은 Number 불성립",
    49: "이갈이 규칙 결합은 Rule 불성립",
    50: "산책로 식별자 결합은 Identifier 불성립",
    51: "구취 분야 결합은 Field 불성립",
    52: "우릴 일련번호 결합은 Serial 불성립",
    53: "치주염 표식 결합은 Marker 불성립",
    54: "사막 이자 결합은 Interest 불성립",
    55: "부정교합 과세 결합은 Levy 불성립",
    56: "와이너리 보조금 결합은 Subsidy 불성립",
    57: "치수과 연체 결합은 Arrears 불성립",
    58: "치주과 가산율 결합은 Markup 불성립",
    61: "수영장 조류 일정표 결합 불명확",
    62: "차량 시트 소견 결합 불명확",
    63: "싱크대 권고 결합 불명확",
    64: "여행 세미나 결합 불명확",
    65: "보컬 선물 결합 불성립 - Gift",
    66: "결제 토너먼트 결합 불성립",
    69: "하객 선물 핸드북 결합은 Favor 다의어 불명확",
    70: "입주자 일정표 결합 불명확",
    71: "기술자 소견 결합은 Technician 불명확",
    72: "린스 권고 결합 불명확",
    73: "뚫어락 세미나 결합 불명확",
    74: "관광 선물 결합 불성립 - Gift",
    75: "클라리넷 리트리트 결합 불성립",
    76: "동의서 토너먼트 결합 불성립",
    80: "이사 정산 일정표 결합 불명확",
    81: "사진 라이선스 소견 결합 불명확",
    82: "등록관 권고 결합은 Registrar 다의어 불명확",
    83: "조경 세미나 결합 불명확",
    84: "수영장 개시 선물 결합 불성립 - Gift",
    85: "버킷 리트리트 결합 불성립",
    86: "연수기 토너먼트 결합 불성립",
    87: "여행자 전단 결합 불명확",
    88: "카페 루프 결합은 Loop 추상 불성립",
    89: "다이너 보조원 결합은 Assistant 불성립",
    90: "비스트로 기록 결합은 Log 위치 추상 불성립",
    91: "피자집 슬롯 결합은 Slot 다의어 불성립",
    92: "데리 청구 결합은 Charge 다의어 불성립",
    93: "디저트 선수금 결합은 Advance 불성립",
    94: "포장 점검기 결합은 Checker 불성립",
    96: "베이커리 수정 결합은 Revision 불성립",
    97: "제과 시계 결합은 Clock 불성립",
    98: "베이글 승인 결합은 Approval 불성립",
    100: "벌크 핸드북 결합 불명확",
    101: "유사 매물 일정표 결합 불명확",
    102: "보험금 소견 결합 불명확",
    103: "수습 권고 결합 불명확",
    104: "데크 세미나 결합 불명확",
    105: "루브릭 선물 결합 불성립 - Gift",
    106: "국민투표 리트리트 결합 불성립",
    107: "스토리 토너먼트 결합 불성립",
    109: "도넛 허브 결합은 Hub 추상 불성립",
    110: "에스프레소 원장 결합은 Ledger 불성립",
    111: "라떼 링 결합은 Ring 불성립",
    112: "칫솔 연결점 결합은 Nexus 불성립",
    113: "스노클링 관리자 결합은 Manager 불성립",
    114: "칵테일 작전 결합은 Ops 불성립",
    115: "치약 플레이북 결합은 Playbook 불성립",
    117: "바리스타 부스 결합은 Booth 불성립",
    118: "구강청격 키오스크 결합은 Kiosk 불성립",
    119: "폭포 항구 결합은 Harbor 불성립",
    120: "펍 로비 결합은 Lobby 불성립",
    121: "마우스가드 전광판 결합은 Ticker 불성립",
    122: "일몰 창 결합은 Window 불성립",
    123: "스테이크하우스 카드 결합은 Card 다의어 불성립",
    124: "스마일 시트 결합은 Sheet 다의어 불성립",
    125: "수변 점수 결합은 Score 불성립",
    126: "스시 뷰 결합은 View 추상 불성립",
    127: "호흡 역사 결합 불성립",
    128: "보드워크 수준 속성 결합은 Level 불성립",
    129: "타코 요약 결합은 Summary 불성립",
    130: "코골이 타임라인 결합 불성립",
    131: "해변 색인 결합은 Index 다의어 불성립",
    134: "전망 목록 결합은 List 다의어 불성립",
    135: "해산물 슬롯 결합은 Slot 다의어 불성립",
    136: "치과 통행 결합은 Pass 다의어 불성립",
    137: "배낭여행 배지 결합은 Badge 불성립",
    138: "교정의 한도 결합은 Quota 속성어 불성립",
    139: "패러세일링 회람 결합은 Bulletin 다의어 불성립",
    140: "치위 청원 결합은 Petition 불성립",
    141: "야생동물 정리 결합은 Recap 다의어 불성립",
    142: "치실 품목 결합은 Item 다의어 불성립",
    144: "치석 운임 속성 결합은 Fare 불성립",
    145: "빙하 대출 결합은 Loan 불성립",
    146: "불소 기금 결합은 Fund 불성립",
    147: "화산 판매 결합은 Sale 다의어 불성립",
    148: "실런트 수당 결합은 Allowance 불성립",
    149: "당일여행 가치 속성 결합은 Value 불성립",
    150: "치은염 벌금 결합은 Fine 불성립",
    151: "요트 버전 결합은 Version 불성립",
    152: "이갈이 세부 결합은 Detail 불성립",
    153: "산책로 분류 결합은 Category 불성립",
    154: "구취 형식 결합은 Format 불성립",
    155: "우릴 토큰 결합은 Token 불성립",
    156: "치주염 잔액 결합은 Balance 불성립",
    157: "사막 자산 결합은 Asset 불성립",
    158: "부정교합 기한 결합은 Due 불성립",
    159: "와이너리 할인 결합은 Discount 불성립",
    160: "치수과 선수금 결합은 Advance 불성립",
    161: "치주과 상환 결합은 Redemption 불성립",
    162: "인화 교정쇄 교육 결합은 Proof 다의어 불명확",
    164: "퇴거 일정표 결합 불명확",
    165: "수영장 조류 소견 결합 불명확",
    166: "차량 시트 권고 결합 불명확",
    167: "싱크대 세미나 결합 불명확",
    168: "여행 선물 결합 불성립 - Gift",
    169: "보컬 리트리트 결합 불성립",
    170: "결제 전단 결합 불명확",
    171: "이사 경로 교육 결합은 Route 추상 불성립",
    173: "하객 선물 일정표 결합은 Favor 다의어 불명확",
    174: "입주자 소견 결합 불명확",
    175: "기술자 권고 결합은 Technician 불명확",
    176: "린스 세미나 결합 불명확",
    177: "뚫어락 선물 결합 불성립 - Gift",
    178: "관광 리트리트 결합 불성립",
    179: "클라리넷 토너먼트 결합 불성립",
    180: "동의서 전단 결합 불명확",
    183: "어휘 일정표 결합 불명확",
    184: "이사 정산 소견 결합 불명확",
    185: "사진 라이선스 권고 결합 불명확",
    186: "등록관 세미나 결합은 Registrar 다의어 불명확",
    187: "조경 선물 결합 불성립 - Gift",
    188: "수영장 개시 리트리트 결합 불성립",
    189: "버킷 토너먼트 결합 불성립",
    190: "연수기 전단 결합 불명확",
    191: "카페 격자 결합은 Grid 추상 불성립",
    192: "다이너 플래너 결합은 Planner 불성립",
    193: "비스트로 서식 결합은 Form 다의어 불성립",
    194: "피자집 통행 결합은 Pass 다의어 불성립",
    195: "데리 의무 결합은 Duty 불성립",
    196: "디저트 벌칙 결합은 Penalty 불성립",
    197: "포장 탐지기 결합은 Detector 불성립",
    198: "브런치 평점 결합은 Rating 불성립",
    199: "베이커리 결제 결합 불명확",
    200: "제과 시간 결합은 Time 불성립",
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
