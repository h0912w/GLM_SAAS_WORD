import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk43_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk43_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    37: (0.7, "설비 정지 대응 교육으로 실재 (제조 실무 개념)"),
    38: (0.6, "작물 재배 핸드북으로 실재 (Handbook 라인)"),
    41: (0.6, "브랜딩 세미나로 실재 (Seminar 라인)"),
    44: (0.6, "위협 인텔 서비스 전단으로 실재 (Flyer 라인)"),
    45: (0.7, "수업 운영 교육으로 실재 (교육 실무 개념)"),
    46: (0.6, "계측기 교정 핸드북으로 실재 (Handbook 라인)"),
    51: (0.6, "개통 서비스 전단으로 실재 (Flyer 라인)"),
    52: (0.7, "왁싱 기술 교육으로 실재 (salon 실무 개념)"),
    53: (0.6, "시럽 투여 복약 핸드북으로 실재 (Handbook 라인)"),
    57: (0.6, "이사 파손 대응 세미나로 실재 (Seminar 라인)"),
    59: (0.6, "수영장 동절기 관리 전단으로 실재 (Flyer 라인)"),
    69: (0.7, "제과 기술 교육으로 실재 (제빵학원 실무 개념)"),
    76: (0.6, "서핑 레슨 전단으로 실재 (Flyer 라인)"),
    95: (0.6, "스시 예약 확인서로 성립 (Confirmation 라인 준용)"),
    117: (0.6, "실런트 시술 매뉴얼로 실재 (dental 도해 계열)"),
    119: (0.6, "치은염 스케치 학습자료로 실재 (dental 도해 계열)"),
    127: (0.6, "부정교합 실습 워크숍으로 실재 (Workshop 라인)"),
    132: (0.6, "설비 정지 대응 핸드북으로 실재 (Handbook 라인)"),
    135: (0.6, "주민 대응 세미나로 실재 (Seminar 라인)"),
    139: (0.6, "셔틀 운영 교육으로 실재 (호텔 실무 개념)"),
    140: (0.6, "수업 운영 핸드북으로 실재 (Handbook 라인)"),
    143: (0.6, "후원자 관리 세미나로 실재 (Seminar 라인)"),
    146: (0.6, "옷장 정리 교육으로 실재 (홈오거나이징 실무 개념)"),
    147: (0.6, "왁싱 기술 핸드북으로 실재 (Handbook 라인)"),
    151: (0.6, "통번역 세미나로 실재 (Seminar 라인)"),
    163: (0.6, "범퍼 수리 교육으로 실재 (바디샵 실무 개념)"),
    164: (0.6, "제과 기술 핸드북으로 실재 (Handbook 라인)"),
    167: (0.6, "네일 실무 세미나로 실재 (Seminar 라인)"),
    170: (0.6, "수영장 관리 서비스 전단으로 실재 (Flyer 라인)"),
    182: (0.6, "폭포 투어 청구서로 성립 (Bill 라인 준용)"),
    185: (0.6, "일몰 투어 이용권으로 성립 (Voucher 라인 준용)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "스시 청원 결합은 Petition 불성립",
    2: "구강 관리 확인서 결합은 Breath 결합 불명확",
    3: "보드워크 항목 결합은 Entry 다의어 불성립",
    4: "타코 비용 속성 결합은 Cost 불성립",
    5: "코골이 가격 속성 결합은 Price 불성립",
    6: "해변 세금 결합은 Tax 불성립",
    7: "면집 기금 결합은 Fund 불성립",
    8: "교합 현금 결합은 Cash 불성립",
    9: "전망 청구 결합은 Charge 다의어 불성립",
    10: "해산물 가치 속성 결합은 Value 불성립",
    11: "치과 지분 결합은 Stake 불성립",
    12: "배낭여행 벌금 결합은 Fine 불성립",
    13: "교정의 규칙 결합은 Rule 불성립",
    14: "패러세일링 식별자 결합은 Identifier 불성립",
    15: "치위 형식 결합은 Format 불성립",
    16: "야생동물 토큰 결합은 Token 불성립",
    17: "치실 잔액 결합은 Balance 불성립",
    18: "라군 자산 결합은 Asset 불성립",
    19: "치석 보조금 결합은 Subsidy 불성립",
    20: "빙하 연체 결합은 Arrears 불성립",
    21: "불소 가산율 결합은 Markup 불성립",
    22: "화산 연장 결합은 Extension 불성립",
    23: "실런트 라벨 결합은 Label 불성립",
    24: "당일여행 워크시트 결합은 여행 서비스와 결합 불명확",
    25: "치은염 배치도 결합은 Layout 불성립",
    26: "요트 개요 결합은 여행 서비스와 결합 불명확",
    27: "이갈이 키트 결합은 Kit 불성립",
    28: "산책로 메시지 결합은 Message 불성립",
    29: "구취 저장소 결합은 Repository 불성립",
    30: "우릴 계산기 결합은 Calculator 추상 불성립",
    31: "치주염 기록기 결합은 Recorder 추상 불성립",
    32: "사막 점검기 결합은 Checker 추상 불성립",
    33: "부정교합 타이머 결합은 Timer 추상 불성립",
    34: "와이너리 보호자 결합은 Guardian 추상 불성립",
    35: "치수과 단계 결합은 Stage 다의어 불성립",
    36: "치주 순위 속성 결합은 Rank 불성립",
    39: "모금 소견 결합 불명확",
    40: "주민 대응 권고 결합 불명확",
    42: "원고 선물 결합 불성립 - Gift",
    43: "배차 리트리트 결합 불성립",
    47: "윤작 일정표 결합 불명확",
    48: "후원자 관리 권고 결합 불명확",
    49: "콘텐츠 선물 결합 불성립 - Gift",
    50: "구독 발행 리트리트 결합 불성립",
    54: "구역 온도 관리 일정표 결합 불명확",
    55: "잠금 장치 소견 결합 불명확",
    56: "통번역 권고 결합 불명확",
    58: "결혼 서약 리트리트 결합 불성립",
    60: "카페 모니터 결합은 Monitor 다의어 불성립",
    61: "다이너 점검 결합은 Check 불성립",
    62: "비스트로 잔표 결합은 Stub 불성립",
    63: "피자집 지분 결합은 Stake 불성립",
    64: "데리 그래프 결합은 Graph 불성립",
    65: "디저트 결과 속성 결합은 Result 불성립",
    66: "포장 모형 결합은 Model 불성립",
    67: "브런치 경비 속성 결합은 Expense 불성립",
    68: "베이커리 빈도 속성 결합은 Frequency 불성립",
    70: "치과 마취 일정표 결합 불명확",
    71: "현장학습 소견 결합 불명확",
    72: "네일 폴리시 권고 결합 불명확",
    73: "열전대 선물 결합 불성립 - Gift",
    74: "비상 장치 리트리트 결합은 Panic 다의어 불성립",
    75: "수영장 토너먼트 결합 불성립",
    77: "베이글 범위 속성 결합은 Scope 불성립",
    78: "도넛 레일 결합은 Rail 불성립",
    79: "에스프레소 탐색기 결합은 Locator 추상 불성립",
    80: "라떼 창문 결합은 Window 불성립",
    81: "칫솔 보고서 결합은 Report 불성립",
    82: "스노클링 카드 결합은 Card 다의어 불성립",
    83: "칵테일 전망 속성 결합은 View 불성립",
    84: "치약 이력 속성 결합은 History 불성립",
    85: "카약 요율 속성 결합은 Rate 불성립",
    86: "바리스타 리마인더 결합은 Reminder 불성립",
    87: "구강청격 색인 결합은 Index 불성립",
    88: "폭포 주문 결합은 Order 다의어 불성립",
    89: "펍 전표 결합은 Slip 다의어 불성립",
    90: "마우스가드 샘플 결합은 Sample 다의어 불성립",
    91: "일몰 패스 결합은 Pass 다의어 불성립",
    92: "스테이크하우스 메모 결합은 Memo 불성립",
    93: "스마일 한도 결합은 Quota 불성립",
    94: "수변 게시물 결합은 Bulletin 다의어 불성립",
    96: "호흡 요약 결합은 Recap 불성립",
    97: "보드워크 요금 속성 결합은 Fee 불성립",
    98: "타코 가격 속성 결합은 Price 불성립",
    99: "코골이 요금 속성 결합은 Fare 불성립",
    100: "해변 대출 결합은 Loan 불성립",
    101: "면집 현금 결합은 Cash 불성립",
    102: "교합 판매 결합은 Sale 다의어 불성립",
    103: "전망 의무 결합은 Duty 불성립",
    104: "해산물 지분 결합은 Stake 불성립",
    105: "치과 마진 속성 결합은 Margin 불성립",
    106: "배낭여행 번호 속성 결합은 Number 불성립",
    107: "교정의 세부 결합은 Detail 불성립",
    108: "패러세일링 분류 결합은 Category 불성립",
    109: "치위 일련번호 결합은 Serial 불성립",
    110: "야생동물 서명 결합은 Signature 불성립",
    111: "치실 이자 결합은 Interest 불성립",
    112: "라군 부과금 결합은 Levy 불성립",
    113: "치석 할인 결합은 Discount 불성립",
    114: "빙하 선수금 결합은 Advance 불성립",
    115: "불소 리딤 결합은 Redemption 불성립",
    116: "화산 체험 결합은 Trial 불성립",
    118: "당일여행 도해 결합은 여행 서비스와 결합 불명확",
    120: "요트 렌더링 결합은 여행 서비스와 결합 불명확",
    121: "이갈이 횟수 결합은 Count 불성립",
    122: "산책로 합계 결합은 Total 불성립",
    123: "구취 공지 결합은 Announcement 불성립",
    124: "우릴 변환기 결합은 Converter 추상 불성립",
    125: "치주염 견적기 결합은 Estimator 추상 불성립",
    126: "사막 탐지기 결합은 Detector 추상 불성립",
    128: "와이너리 조력자 결합은 Helper 추상 불성립",
    129: "치수과 결과 속성 결합은 Result 불성립",
    130: "치주 추이 속성 결합은 Trend 불성립",
    131: "등록금 교육 결합은 Tuition 결합 불명확",
    133: "작물 일정표 결합 불명확",
    134: "모금 권고 결합 불명확",
    136: "브랜드 선물 결합 불성립 - Gift",
    137: "원고 리트리트 결합 불성립",
    138: "배차 토너먼트 결합 불성립",
    141: "계측기 교정 일정표 결합 불명확",
    142: "윤작 소견 결합 불명확",
    144: "콘텐츠 리트리트 결합 불성립",
    145: "구독 발행 토너먼트 결합 불성립",
    148: "시럽 일정표 결합 불명확",
    149: "구역 온도 관리 소견 결합 불명확",
    150: "잠금 장치 권고 결합 불명확",
    152: "이사 파손 선물 결합 불성립 - Gift",
    153: "결혼 서약 토너먼트 결합 불성립",
    154: "카페 동반자 결합은 Companion 추상 불성립",
    155: "다이너 점수 결합은 Score 불성립",
    156: "비스트로 명세서 결합은 Statement 불성립",
    157: "피자집 마진 속성 결합은 Margin 불성립",
    158: "데리 라벨 결합은 Label 불성립",
    159: "디저트 연승 속성 결합은 Streak 불성립",
    160: "포장 가용성 속성 결합은 Availability 불성립",
    161: "브런치 뉴스레터 결합은 Newsletter 불성립",
    162: "베이커리 호환성 속성 결합은 Compatibility 불성립",
    165: "치과 마취 소견 결합 불명확",
    166: "현장학습 권고 결합 불명확",
    168: "열전대 리트리트 결합 불성립",
    169: "비상 장치 토너먼트 결합은 Panic 다의어 불성립",
    171: "베이글 순환 결합은 Loop 불성립",
    172: "도넛 산책로 결합은 Trail 다의어 불성립",
    173: "에스프레소 검색기 결합은 Finder 추상 불성립",
    174: "라떼 롤 결합은 Roll 다의어 불성립",
    175: "칫솔 로그 결합은 Log 불성립",
    176: "스노클링 시트 결합은 Sheet 다의어 불성립",
    177: "칵테일 이력 속성 결합은 History 불성립",
    178: "치약 파일 결합은 File 불성립",
    179: "카약 갱신 결합은 Update 불성립",
    180: "바리스타 색인 결합은 Index 불성립",
    181: "구강청격 티켓 결합은 Ticket 다의어 불성립",
    183: "펍 샘플 결합은 Sample 다의어 불성립",
    184: "마우스가드 슬롯 결합은 Slot 불성립",
    186: "스테이크하우스 한도 결합은 Quota 불성립",
    187: "스마일 탭 결합은 Tab 다의어 불성립",
    188: "수변 요약 결합은 Brief 다의어 불성립",
    189: "스시 요약 결합은 Recap 불성립",
    190: "호흡 항목 결합은 Entry 다의어 불성립",
    191: "보드워크 품목 결합은 Item 다의어 불성립",
    192: "타코 요금 속성 결합은 Fare 불성립",
    193: "코골이 세금 결합은 Tax 불성립",
    194: "해변 합계 결합은 Sum 불성립",
    195: "면집 판매 결합은 Sale 다의어 불성립",
    196: "교합 청구 결합은 Charge 다의어 불성립",
    197: "전망 수당 결합은 Allowance 불성립",
    198: "해산물 마진 속성 결합은 Margin 불성립",
    199: "치과 벌금 결합은 Fine 불성립",
    200: "배낭여행 버전 속성 결합은 Version 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 31, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 169, len(REJECT_REASON)
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
