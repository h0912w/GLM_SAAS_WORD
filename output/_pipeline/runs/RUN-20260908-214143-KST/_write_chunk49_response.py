import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk48_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk48_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    9: (0.6, "챠지백 대응 핸드북으로 실재 (Handbook 라인)"),
    11: (0.6, "보험 특약 세미나로 실재 (Seminar 라인)"),
    15: (0.6, "셔틀 서비스 전단으로 실재 (Flyer 라인)"),
    16: (0.7, "동영상 제작 교육으로 실재 (미디어 실무 개념)"),
    17: (0.6, "설문 설계 핸드북으로 실재 (Handbook 라인)"),
    24: (0.6, "옷장정리 서비스 전단으로 실재 (Flyer 라인)"),
    27: (0.6, "비스트로 예약 확인서로 성립 (Confirmation 라인 준용)"),
    34: (0.7, "부동산 중개 교육으로 실재 (부동산 실무 개념)"),
    39: (0.6, "보도 파손 보수 세미나로 실재 (Seminar 라인)"),
    43: (0.6, "범퍼 수리 서비스 전단으로 실재 (Flyer 라인)"),
    56: (0.6, "폭포 투어 바우처로 성립 (Voucher 라인 준용)"),
    81: (0.6, "치석 관리 매뉴얼로 실재 (Manual 라인)"),
    83: (0.6, "불소 도포 도식 학습자료로 실재 (dental 도해 계열)"),
    99: (0.7, "의료 서비스 제공자 대상 교육으로 실재 (헬스케어 실무 개념)"),
    101: (0.6, "손해사정 세미나로 실재 (Seminar 라인)"),
    104: (0.6, "호텔 편의시설 안내 전단으로 실재 (Flyer 라인)"),
    105: (0.7, "트럼펫 레슨으로 실재 (음악 강습 서비스)"),
    111: (0.6, "재입고 안내 전단으로 실재 (Flyer 라인)"),
    112: (0.6, "동영상 제작 핸드북으로 실재 (Handbook 라인)"),
    119: (0.6, "기저귀 서비스 전단으로 실재 (Flyer 라인)"),
    129: (0.7, "드리야지 단거리 운송 교육으로 실재 (물류 실무 개념)"),
    130: (0.6, "부동산 중개 핸드북으로 실재 (Handbook 라인)"),
    134: (0.6, "과외 세미나로 실재 (Seminar 라인)"),
    148: (0.6, "카약 투어 청구서로 성립 (Bill 라인 준용)"),
    157: (0.6, "수변 여행 플랜으로 성립 (Plan 라인 준용)"),
    176: (0.6, "치석 관리 워크시트로 실재 (Worksheet 라인)"),
    194: (0.7, "드럼 레슨으로 실재 (음악 강습 서비스)"),
    195: (0.6, "의료 서비스 제공자 핸드북으로 실재 (Handbook 라인)"),
    199: (0.6, "풀필먼트 서비스 전단으로 실재 (Flyer 라인)"),
    200: (0.6, "관광 명소 안내 교육으로 실재 (관광 실무 개념)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "치수과 판독 결합은 Reading 다의어 불성립",
    2: "치주 기한 속성 결합은 Deadline 불성립",
    3: "창고 일정표 결합 불명확",
    4: "손해사정 권고 결합 불명확",
    5: "입찰 선물 결합 불성립 - Gift",
    6: "풀필먼트 리트리트 결합 불성립",
    7: "어메니티 토너먼트 결합 불성립",
    8: "등록금 전단 결합은 Tuition 결합 불성립",
    10: "증거개시 일정표 결합 불명확",
    12: "채용 후보자 선물 결합 불성립 - Gift",
    13: "하자보증 리트리트 결합 불성립",
    14: "재고 보충 토너먼트 결합 불성립",
    18: "자기소개서 일정표 결합 불명확",
    19: "이벤트 녹화 소견 결합 불명확",
    20: "외식 세미나 결합은 Dine 단독 결합 불명확",
    21: "중성화 선물 결합 불성립 - Gift",
    22: "치아미백 리트리트 결합 불성립",
    23: "기저귀 토너먼트 결합 불성립",
    25: "카페 탐색기 결합은 Finder 추상 불성립",
    26: "다이너 요율 속성 결합은 Rate 불성립",
    28: "피자집 속성 결합은 Attribute 불성립",
    29: "델리 통지 결합은 Notification 불성립",
    30: "디저트 참고자료 결합은 Reference 불성립",
    31: "포장 보증 결합은 음식 서비스와 결합 불성립",
    32: "브런치 범위 속성 결합은 Range 불성립",
    33: "베이커리 접수 결합은 Reception 다의어 불성립",
    35: "보험사 핸드북 결합은 Carrier 다의어 불명확",
    36: "노사 관계 일정표 결합 불명확",
    37: "단열 시공 소견 결합 불명확",
    38: "과외 권고 결합 불명확",
    40: "뉴스레터 선물 결합 불성립 - Gift",
    41: "복리후생 리트리트 결합 불성립",
    42: "민원 토너먼트 결합 불성립",
    44: "제과 추적기 결합은 Tracker 추상 불성립",
    45: "베이글 장부 결합은 Ledger 불성립",
    46: "도넛 조수 결합은 Assistant 추상 불성립",
    47: "에스프레소 알림 결합은 Alert 불성립",
    48: "라떼 태그 결합은 Tag 다의어 불성립",
    49: "칫솔 상태 속성 결합은 Status 불성립",
    50: "스노클링 파일 결합은 File 불성립",
    51: "칵테일 리마인더 결합은 Reminder 불성립",
    52: "치약 색인 결합은 Index 불성립",
    53: "카약 주문 결합은 Order 다의어 불성립",
    54: "바리스타 전표 결합은 Slip 다의어 불성립",
    55: "구강청격 검체 결합은 Sample 다의어 불성립",
    57: "펍 탭 결합은 Tab 다의어 불성립",
    58: "마우스가드 게시물 결합은 Bulletin 다의어 불성립",
    59: "일몰 회람 결합은 Circular 다의어 불성립",
    60: "스테이크하우스 항목 결합은 Entry 다의어 불성립",
    61: "스마일 요금 속성 결합은 Fee 불성립",
    62: "수변 유닛 결합은 Unit 다의어 불성립",
    63: "스시 세금 결합은 Tax 불성립",
    64: "호흡 대출 결합은 Loan 불성립",
    65: "보드워크 부채 결합은 Debt 불성립",
    66: "타코 의무 결합은 Duty 불성립",
    67: "코골이 수당 결합은 Allowance 불성립",
    68: "해변 가치 속성 결합은 Value 불성립",
    69: "면집 번호 속성 결합은 Number 불성립",
    70: "교합 버전 속성 결합은 Version 불성립",
    71: "전망 규칙 결합은 Rule 불성립",
    72: "해산물 속성 결합은 Attribute 불성립",
    73: "치과 필드 결합은 Field 불성립",
    74: "배낭여행 일련번호 결합은 Serial 불성립",
    75: "교정의 잔액 결합은 Balance 불성립",
    76: "패러세일링 자산 결합은 Asset 불성립",
    77: "치위 할인 결합은 Discount 불성립",
    78: "야생동물 선금 결합은 Advance 다의어 불성립",
    79: "치실 리딤 결합은 Redemption 불성립",
    80: "라군 재판 결합은 Trial 다의어 불성립",
    82: "빙하 도해 결합은 여행 서비스와 결합 불명확",
    84: "화산 렌더링 결합은 여행 서비스와 결합 불명확",
    85: "실런트 횟수 결합은 Count 불성립",
    86: "당일여행 합계 결합은 여행 서비스와 결합 불명확",
    87: "치은염 공지 결합은 Announcement 다의어 불성립",
    88: "요트 변환기 결합은 여행 서비스와 결합 불명확",
    89: "이갈이 견적기 결합은 Estimator 추상 불성립",
    90: "산책로 탐지기 결합은 Detector 추상 불성립",
    91: "구취 보호자 결합은 Guardian 추상 불성립",
    92: "우릴 무대 결합은 Stage 다의어 불성립",
    93: "치주염 순위 속성 결합은 Rank 불성립",
    94: "사막 비교 속성 결합은 Comparison 불성립",
    95: "부정교합 보증 속성 결합은 Guarantee 불성립",
    96: "와이너리 사본 결합은 Copy 다의어 불성립",
    97: "치수과 참고자료 결합은 Reference 불성립",
    98: "치주 기간 속성 결합은 Duration 불성립",
    100: "창고 소견 결합 불명확",
    102: "입찰 리트리트 결합 불성립",
    103: "풀필먼트 토너먼트 결합 불성립",
    106: "챠지백 일정표 결합 불명확",
    107: "증거개시 소견 결합 불명확",
    108: "보험 특약 선물 결합 불성립 - Gift",
    109: "채용 후보자 리트리트 결합 불성립",
    110: "하자보증 토너먼트 결합 불성립",
    113: "설문 일정표 결합 불명확",
    114: "자기소개서 소견 결합 불명확",
    115: "이벤트 녹화 권고 결합 불명확",
    116: "외식 선물 결합은 Dine 단독 결합 불명확",
    117: "중성화 리트리트 결합 불성립",
    118: "치아미백 토너먼트 결합 불성립",
    120: "카페 사무실 결합은 Office 다의어 불성립",
    121: "다이너 업데이트 결합은 Update 다의어 불성립",
    122: "비스트로 요약 결합은 Recap 불성립",
    123: "피자집 필드 결합은 Field 불성립",
    124: "델리 키트 결합은 Kit 불성립",
    125: "디저트 예측 속성 결합은 Forecast 불성립",
    126: "포장 보증금 결합은 Deposit 다의어 불명확",
    127: "브런치 한도 속성 결합은 Limit 불성립",
    128: "베이커리 사후관리 결합은 Followup 불성립",
    131: "보험사 일정표 결합은 Carrier 다의어 불명확",
    132: "노사 관계 소견 결합 불명확",
    133: "단열 시공 권고 결합 불명확",
    135: "포트홀 선물 결합 불성립 - Gift",
    136: "뉴스레터 리트리트 결합 불성립",
    137: "복리후생 토너먼트 결합 불성립",
    138: "민원 전단 결합은 불만 서비스와 결합 불성립",
    139: "제과 흐름 결합은 Flow 추상 불성립",
    140: "베이글 보드 결합은 Board 다의어 불성립",
    141: "도넛 계획기 결합은 Planner 추상 불성립",
    142: "에스프레소 차트 결합은 Chart 불성립",
    143: "라떼 프로필 결합은 Profile 다의어 불성립",
    144: "칫솔 전망 속성 결합은 View 불성립",
    145: "스노클링 수준 속성 결합은 Level 불성립",
    146: "칵테일 색인 결합은 Index 불성립",
    147: "치약 티켓 결합은 Ticket 다의어 불성립",
    149: "바리스타 검체 결합은 Sample 다의어 불성립",
    150: "구강청격 슬롯 결합은 Slot 불성립",
    151: "폭포 배지 결합은 Badge 불성립",
    152: "펍 게시물 결합은 Bulletin 다의어 불성립",
    153: "마우스가드 요약 결합은 Brief 다의어 불성립",
    154: "일몰 자문 결합은 Advisory 추상 불성립",
    155: "스테이크하우스 요금 속성 결합은 Fee 불성립",
    156: "스마일 품목 결합은 Item 다의어 불성립",
    158: "스시 대출 결합은 Loan 불성립",
    159: "호흡 합계 결합은 Sum 불성립",
    160: "보드워크 기금 결합은 Fund 불성립",
    161: "타코 수당 결합은 Allowance 불성립",
    162: "코골이 관세 결합은 Tariff 불성립",
    163: "해변 지분 결합은 Stake 불성립",
    164: "면집 버전 속성 결합은 Version 불성립",
    165: "교합 링크 결합은 Link 불성립",
    166: "전망 상세 결합은 Detail 불성립",
    167: "해산물 필드 결합은 Field 불성립",
    168: "치과 형식 결합은 Format 불성립",
    169: "배낭여행 토큰 결합은 Token 불성립",
    170: "교정의 이자 결합은 Interest 불성립",
    171: "패러세일링 부과금 결합은 Levy 불성립",
    172: "치위 연체 결합은 Arrears 불성립",
    173: "야생동물 벌칙 결합은 Penalty 불성립",
    174: "치실 연장 결합은 Extension 불성립",
    175: "라군 그래프 결합은 Graph 불성립",
    177: "빙하 도식 결합은 여행 서비스와 결합 불명확",
    178: "불소 개요 결합은 Outline 불성립",
    179: "화산 통지 결합은 여행 서비스와 결합 불명확",
    180: "실런트 메시지 결합은 Message 불성립",
    181: "당일여행 위젯 결합은 Widget 불성립",
    182: "치은염 계산기 결합은 Calculator 추상 불성립",
    183: "요트 생성기 결합은 여행 서비스와 결합 불명확",
    184: "이갈이 점검기 결합은 Checker 추상 불성립",
    185: "산책로 타이머 결합은 Timer 추상 불성립",
    186: "구취 조력자 결합은 Helper 추상 불성립",
    187: "우릴 결과 속성 결합은 Result 불성립",
    188: "치주염 추이 속성 결합은 Trend 불성립",
    189: "사막 제안 결합은 Proposal 불성립",
    190: "부정교합 기록 속성 결합은 Record 불성립",
    191: "와이너리 판독 결합은 Reading 다의어 불성립",
    192: "치수과 예측 속성 결합은 Forecast 불성립",
    193: "치주 권수 속성 결합은 Volume 불성립",
    196: "창고 권고 결합 불명확",
    197: "손해사정 선물 결합 불성립 - Gift",
    198: "입찰 토너먼트 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 30, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 170, len(REJECT_REASON)
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
