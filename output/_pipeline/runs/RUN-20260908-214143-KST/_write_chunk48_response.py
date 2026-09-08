import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk47_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk47_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "우릴 생태 체험 워크숍으로 실재 (Workshop 라인)"),
    9: (0.7, "창고 운영 교육으로 실재 (물류 실무 개념)"),
    12: (0.6, "풀필먼트 세미나로 실재 (Seminar 라인)"),
    16: (0.6, "작물 컨설팅 전단으로 실재 (Flyer 라인)"),
    17: (0.7, "증거개시 절차 교육으로 실재 (법률 실무 개념)"),
    20: (0.6, "하자보증 세미나로 실재 (Seminar 라인)"),
    24: (0.6, "계측기 교정 서비스 전단으로 실재 (Flyer 라인)"),
    25: (0.7, "자기소개서 작성 교육으로 실재 (채용 실무 개념)"),
    26: (0.6, "이벤트 녹화 운영 핸드북으로 실재 (Handbook 라인)"),
    29: (0.6, "치아미백 세미나로 실재 (Seminar 라인)"),
    33: (0.6, "복약 안내 전단으로 실재 (Flyer 라인)"),
    43: (0.7, "노사 관계 교육으로 실재 (HR 실무 개념)"),
    44: (0.6, "단열 시공 핸드북으로 실재 (Handbook 라인)"),
    48: (0.6, "복리후생 세미나로 실재 (Seminar 라인)"),
    67: (0.6, "스테이크하우스 예약 확인서로 성립 (Confirmation 라인 준용)"),
    90: (0.6, "불소 도식 학습자료로 실재 (dental 도해 계열)"),
    106: (0.6, "창고 운영 핸드북으로 실재 (Handbook 라인)"),
    108: (0.6, "입찰 작성 세미나로 실재 (Seminar 라인)"),
    112: (0.6, "설비 정지 대응 전단으로 실재 (Flyer 라인)"),
    113: (0.7, "챠지백 대응 교육으로 실재 (금융 실무 개념)"),
    114: (0.6, "증거개시 절차 핸드북으로 실재 (Handbook 라인)"),
    116: (0.6, "채용 세미나로 실재 (Seminar 라인)"),
    120: (0.6, "수업 안내 전단으로 실재 (Flyer 라인)"),
    121: (0.7, "설문 설계 교육으로 실재 (리서치 실무 개념)"),
    122: (0.6, "자기소개서 작성 핸드북으로 실재 (Handbook 라인)"),
    125: (0.6, "중성화 세미나로 실재 (Seminar 라인)"),
    129: (0.6, "왁싱 서비스 전단으로 실재 (Flyer 라인)"),
    136: (0.6, "포장 주문 견적으로 성립 (Quote 라인 준용)"),
    140: (0.6, "노사 관계 핸드북으로 실재 (Handbook 라인)"),
    144: (0.6, "뉴스레터 제작 세미나로 실재 (Seminar 라인)"),
    148: (0.6, "제과 홍보 전단으로 실재 (Flyer 라인)"),
    157: (0.6, "카약 투어 견적으로 성립 (Estimate 라인 준용)"),
    195: (0.6, "구취 임상 워크숍으로 실재 (Workshop 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "구취 탐지기 결합은 Detector 추상 불성립",
    3: "치주염 단계 결합은 Stage 다의어 불성립",
    4: "사막 연승 속성 결합은 Streak 불성립",
    5: "부정교합 추이 속성 결합은 Trend 불성립",
    6: "와이너리 제안 결합은 Proposal 불성립",
    7: "치수과 기록 속성 결합은 Record 불성립",
    8: "치주 참고자료 결합은 Reference 불성립",
    10: "손해사정 일정표 결합 불명확",
    11: "입찰 권고 결합 불명확",
    13: "어메니티 선물 결합 불성립 - Gift",
    14: "등록금 리트리트 결합은 Tuition 결합 불성립",
    15: "설비 정지 토너먼트 결합 불성립",
    18: "보험 특약 소견 결합 불명확",
    19: "채용 후보자 권고 결합 불명확",
    21: "재고 보충 선물 결합 불성립 - Gift",
    22: "셔틀 리트리트 결합 불성립",
    23: "수업 운영 토너먼트 결합 불성립",
    27: "외식 소견 결합은 Dine 단독 결합 불명확",
    28: "중성화 권고 결합 불명확",
    30: "기저귀 선물 결합 불성립 - Gift",
    31: "옷장 정리 리트리트 결합 불성립",
    32: "왁싱 토너먼트 결합 불성립",
    34: "카페 디렉터리 결합은 Directory 불성립",
    35: "다이너 파일 결합은 File 불성립",
    36: "비스트로 자문 결합은 Advisory 추상 불성립",
    37: "피자집 식별자 결합은 Identifier 불성립",
    38: "델리 개요 결합은 매장 운영과 결합 불명확",
    39: "디저트 사본 결합은 Copy 다의어 불성립",
    40: "포장 갱신 결합은 Renewal 불성립",
    41: "브런치 무게 속성 결합은 Weight 불성립",
    42: "베이커리 고장 속성 결합은 Breakdown 불성립",
    45: "과외 일정표 결합 불명확",
    46: "포트홀 소견 결합 불명확",
    47: "뉴스레터 권고 결합 불명확",
    49: "민원 선물 결합 불성립 - Gift",
    50: "범퍼 리트리트 결합 불성립",
    51: "제과 토너먼트 결합 불성립",
    52: "베이글 베이스 결합은 Base 다의어 불성립",
    53: "도넛 관리자 결합은 Manager 추상 불성립",
    54: "에스프레소 항구 결합은 Harbor 불성립",
    55: "라떼 점수 결합은 Score 불성립",
    56: "칫솔 태그 결합은 Tag 다의어 불성립",
    57: "스노클링 전망 속성 결합은 View 불성립",
    58: "칵테일 요약 결합은 Summary 불성립",
    59: "치약 타임라인 결합은 Timeline 불성립",
    60: "카약 티켓 결합은 Ticket 다의어 불성립",
    61: "바리스타 목록 결합은 List 불성립",
    62: "구강청격 테이블 결합은 Table 불성립",
    63: "폭포 슬롯 결합은 Slot 불성립",
    64: "펍 메모 결합은 Memo 불성립",
    65: "마우스가드 한도 결합은 Quota 불성립",
    66: "일몰 게시물 결합은 Bulletin 다의어 불성립",
    68: "스마일 요약 결합은 Recap 불성립",
    69: "수변 요금 속성 결합은 Fee 불성립",
    70: "스시 가격 속성 결합은 Price 불성립",
    71: "호흡 요금 속성 결합은 Fare 불성립",
    72: "보드워크 대출 결합은 Loan 불성립",
    73: "타코 판매 결합은 Sale 다의어 불성립",
    74: "코골이 청구 결합은 Charge 다의어 불성립",
    75: "해변 수당 결합은 Allowance 불성립",
    76: "면집 마진 속성 결합은 Margin 불성립",
    77: "교합 벌금 결합은 Fine 불성립",
    78: "전망 버전 속성 결합은 Version 불성립",
    79: "해산물 식별자 결합은 Identifier 불성립",
    80: "치과 분류 결합은 Category 불성립",
    81: "배낭여행 필드 결합은 Field 불성립",
    82: "교정의 서명 결합은 Signature 불성립",
    83: "패러세일링 잔액 결합은 Balance 불성립",
    84: "치위 기한 결합은 Due 불성립",
    85: "야생동물 할인 결합은 Discount 불성립",
    86: "치실 벌칙 결합은 Penalty 불성립",
    87: "라군 리딤 결합은 Redemption 불성립",
    88: "치석 그래프 결합은 Graph 불성립",
    89: "빙하 매뉴얼 결합은 여행 서비스와 결합 불명확",
    91: "화산 스케치 결합은 여행 서비스와 결합 불명확",
    92: "실런트 통지 결합은 Notification 불성립",
    93: "당일여행 횟수 결합은 여행 서비스와 결합 불명확",
    94: "치은염 위젯 결합은 Widget 불성립",
    95: "요트 공지 결합은 여행 서비스와 결합 불명확",
    96: "이갈이 생성기 결합은 Generator 추상 불성립",
    97: "산책로 견적기 결합은 Estimator 추상 불성립",
    98: "구취 타이머 결합은 Timer 추상 불성립",
    99: "우릴 보호자 결합은 Guardian 추상 불성립",
    100: "치주염 결과 속성 결합은 Result 불성립",
    101: "사막 순위 속성 결합은 Rank 불성립",
    102: "부정교합 비교 속성 결합은 Comparison 불성립",
    103: "와이너리 보증 속성 결합은 Guarantee 불성립",
    104: "치수과 사본 결합은 Copy 다의어 불성립",
    105: "치주 예측 속성 결합은 Forecast 불성립",
    107: "손해사정 소견 결합 불명확",
    109: "풀필먼트 선물 결합 불성립 - Gift",
    110: "어메니티 리트리트 결합 불성립",
    111: "등록금 토너먼트 결합은 Tuition 결합 불성립",
    115: "보험 특약 권고 결합 불명확",
    117: "하자보증 선물 결합 불성립 - Gift",
    118: "재고 보충 리트리트 결합 불성립",
    119: "셔틀 토너먼트 결합 불성립",
    123: "이벤트 녹화 일정표 결합 불명확",
    124: "외식 권고 결합은 Dine 단독 결합 불명확",
    126: "치아미백 선물 결합 불성립 - Gift",
    127: "기저귀 리트리트 결합 불성립",
    128: "옷장 정리 토너먼트 결합 불성립",
    130: "카페 탐색기 결합은 Locator 추상 불성립",
    131: "다이너 수준 속성 결합은 Level 불성립",
    132: "비스트로 청원 결합은 Petition 불성립",
    133: "피자집 분류 결합은 Category 불성립",
    134: "델리 렌더링 결합은 매장 운영과 결합 불명확",
    135: "디저트 판독 결합은 Reading 다의어 불성립",
    137: "브런치 거리 속성 결합은 Distance 불성립",
    138: "베이커리 센서 결합은 Sensor 불성립",
    139: "보험사 교육 결합은 Carrier 다의어 불명확",
    141: "단열 시공 일정표 결합 불명확",
    142: "과외 소견 결합 불명확",
    143: "포트홀 권고 결합 불명확",
    145: "복리후생 선물 결합 불성립 - Gift",
    146: "민원 리트리트 결합 불성립",
    147: "범퍼 토너먼트 결합 불성립",
    149: "베이글 중심 결합은 Core 다의어 불성립",
    150: "도넛 엔진 결합은 Engine 추상 불성립",
    151: "에스프레소 명단 결합은 Roster 불성립",
    152: "라떼 노트 결합은 Note 불성립",
    153: "칫솔 프로필 결합은 Profile 다의어 불성립",
    154: "스노클링 이력 속성 결합은 History 불성립",
    155: "칵테일 타임라인 결합은 Timeline 불성립",
    156: "치약 리마인더 결합은 Reminder 불성립",
    158: "바리스타 테이블 결합은 Table 불성립",
    159: "구강청격 전표 결합은 Slip 다의어 불성립",
    160: "폭포 패스 결합은 Pass 다의어 불성립",
    161: "펍 한도 결합은 Quota 불성립",
    162: "마우스가드 탭 결합은 Tab 다의어 불성립",
    163: "일몰 요약 결합은 Brief 다의어 불성립",
    164: "스테이크하우스 요약 결합은 Recap 불성립",
    165: "스마일 항목 결합은 Entry 다의어 불성립",
    166: "수변 품목 결합은 Item 다의어 불성립",
    167: "스시 요금 속성 결합은 Fare 불성립",
    168: "호흡 세금 결합은 Tax 불성립",
    169: "보드워크 합계 결합은 Sum 불성립",
    170: "타코 청구 결합은 Charge 다의어 불성립",
    171: "코골이 의무 결합은 Duty 불성립",
    172: "해변 관세 결합은 Tariff 불성립",
    173: "면집 벌금 결합은 Fine 불성립",
    174: "교합 번호 속성 결합은 Number 불성립",
    175: "전망 링크 결합은 Link 불성립",
    176: "해산물 분류 결합은 Category 불성립",
    177: "치과 속성 결합은 Attribute 불성립",
    178: "배낭여행 형식 결합은 Format 불성립",
    179: "교정의 마커 결합은 Marker 불성립",
    180: "패러세일링 이자 결합은 Interest 불성립",
    181: "치위 보조금 결합은 Subsidy 불성립",
    182: "야생동물 연체 결합은 Arrears 불성립",
    183: "치실 가산율 결합은 Markup 불성립",
    184: "라군 연장 결합은 Extension 불성립",
    185: "치석 라벨 결합은 Label 불성립",
    186: "빙하 워크시트 결합은 여행 서비스와 결합 불명확",
    187: "불소 배치도 결합은 Layout 불성립",
    188: "화산 개요 결합은 여행 서비스와 결합 불명확",
    189: "실런트 키트 결합은 Kit 불성립",
    190: "당일여행 메시지 결합은 여행 서비스와 결합 불명확",
    191: "치은염 저장소 결합은 Repository 불성립",
    192: "요트 계산기 결합은 여행 서비스와 결합 불명확",
    193: "이갈이 기록기 결합은 Recorder 추상 불성립",
    194: "산책로 점검기 결합은 Checker 추상 불성립",
    196: "우릴 조력자 결합은 Helper 추상 불성립",
    197: "치주염 연승 속성 결합은 Streak 불성립",
    198: "사막 추이 속성 결합은 Trend 불성립",
    199: "부정교합 제안 결합은 Proposal 불성립",
    200: "와이너리 기록 속성 결합은 Record 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 33, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 167, len(REJECT_REASON)
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
