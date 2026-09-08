import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk49_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk49_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "트럼펫 강습 핸드북으로 실재 (Handbook 라인)"),
    6: (0.6, "하자보증 서비스 전단으로 실재 (Flyer 라인)"),
    11: (0.6, "이벤트 녹화 세미나로 실재 (Seminar 라인)"),
    14: (0.6, "치아미백 서비스 전단으로 실재 (Flyer 라인)"),
    24: (0.7, "경매 투자 교육으로 실재 (금융 실무 개념)"),
    25: (0.6, "드리야지 운송 핸드북으로 실재 (Handbook 라인)"),
    29: (0.6, "단열 시공 세미나로 실재 (Seminar 라인)"),
    33: (0.6, "복리후생 안내 전단으로 실재 (Flyer 라인)"),
    43: (0.6, "카약 투어 영수증으로 성립 (Receipt 라인 준용)"),
    71: (0.6, "치석 도식 학습자료로 실재 (dental 도해 계열)"),
    80: (0.6, "역사 산책 워크숍으로 실재 (Workshop 라인)"),
    90: (0.6, "드럼 강습 핸드북으로 실재 (Handbook 라인)"),
    92: (0.6, "창고 운영 세미나로 실재 (Seminar 라인)"),
    94: (0.6, "입찰 안내 전단으로 실재 (Flyer 라인)"),
    95: (0.7, "렌치 사용법 강좌로 실재 (배관 실무 개념)"),
    96: (0.6, "관광 명소 안내 핸드북으로 실재 (Handbook 라인)"),
    99: (0.6, "증거개시 절차 세미나로 실재 (Seminar 라인)"),
    102: (0.7, "지붕 시공 교육으로 실재 (건설 실무 개념)"),
    106: (0.6, "자기소개서 작성 세미나로 실재 (Seminar 라인)"),
    120: (0.6, "경매 투자 핸드북으로 실재 (Handbook 라인)"),
    124: (0.6, "노사 관계 세미나로 실재 (Seminar 라인)"),
    128: (0.6, "뉴스레터 구독 유치 전단으로 실재 (Flyer 라인)"),
    136: (0.6, "이벤트 바 케이터링 견적으로 성립 (Estimate 라인 준용)"),
    144: (0.6, "선셋 투어 예약 확인서로 성립 (Confirmation 라인 준용)"),
    146: (0.6, "미소 교정 플랜으로 성립 (Plan 라인 준용)"),
    166: (0.6, "치석 도식 학습자료로 실재 (dental 도해 계열)"),
    184: (0.7, "누수 수리 교육으로 실재 (배관 실무 개념)"),
    190: (0.7, "스크래치 복원 교육으로 실재 (디테일링 실무 개념)"),
    191: (0.6, "렌치 사용법 핸드북으로 실재 (Handbook 라인)"),
    194: (0.6, "챠지백 대응 세미나로 실재 (Seminar 라인)"),
    196: (0.6, "보험 특약 안내 전단으로 실재 (Flyer 라인)"),
    197: (0.7, "원천징수 교육으로 실재 (급여 실무 개념)"),
    198: (0.6, "지붕 시공 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "챠지백 소견 결합 불명확",
    3: "증거개시 권고 결합 불명확",
    4: "보험 특약 리트리트 결합 불성립",
    5: "채용 후보자 토너먼트 결합 불성립",
    7: "미성년자/부전공 다의어 결합은 Minor 불명확",
    8: "동영상 일정표 결합 불명확",
    9: "설문 소견 결합 불명확",
    10: "자기소개서 권고 결합 불명확",
    12: "외식 리트리트 결합은 Dine 단독 결합 불명확",
    13: "중성화 토너먼트 결합 불성립",
    15: "카페 카운터 결합은 Counter 다의어 불성립",
    16: "다이너 피드 결합은 Feed 다의어 불성립",
    17: "비스트로 항목 결합은 Entry 다의어 불성립",
    18: "피자집 형식 결합은 Format 불성립",
    19: "델리 횟수 결합은 Count 불성립",
    20: "디저트 기한 속성 결합은 Deadline 불성립",
    21: "포장 자격증 결합은 Certification 불성립",
    22: "브런치 유형 속성 결합은 Type 불성립",
    23: "베이커리 승인 결합은 Approval 불성립",
    26: "부동산 중개 일정표 결합 불명확",
    27: "보험사 소견 결합은 Carrier 다의어 불명확",
    28: "노사 관계 권고 결합 불명확",
    30: "과외 선물 결합 불성립 - Gift",
    31: "포트홀 리트리트 결합 불성립",
    32: "뉴스레터 토너먼트 결합 불성립",
    34: "제과 허브 결합은 Hub 추상 불성립",
    35: "베이글 갑판 결합은 Deck 불성립",
    36: "도넛 스케줄러 결합은 Scheduler 추상 불성립",
    37: "에스프레소 통 결합은 Bin 불성립",
    38: "라떼 상태 속성 결합은 Status 불성립",
    39: "칫솔 이력 속성 결합은 History 불성립",
    40: "스노클링 요율 속성 결합은 Rate 불성립",
    41: "칵테일 티켓 결합은 Ticket 다의어 불성립",
    42: "치약 견적 결합은 치과 서비스와 결합 불성립",
    44: "바리스타 슬롯 결합은 Slot 불성립",
    45: "구강청격 패스 결합은 Pass 다의어 불성립",
    46: "폭표 스텁 결합은 Stub 불성립",
    47: "펍 요약 결합은 Brief 다의어 불성립",
    48: "마우스가드 회람 결합은 Circular 다의어 불성립",
    49: "일몰 청원 결합은 Petition 불성립",
    50: "스테이크하우스 품목 결합은 Item 다의어 불성립",
    51: "스마일 유닛 결합은 Unit 다의어 불성립",
    52: "수변 비용 속성 결합은 Cost 불성립",
    53: "스시 합계 결합은 Sum 불성립",
    54: "호흡 부채 결합은 Debt 불성립",
    55: "보드워크 현금 결합은 Cash 불성립",
    56: "타코 관세 결합은 Tariff 불성립",
    57: "코골이 가치 속성 결합은 Value 불성립",
    58: "해변 마진 속성 결합은 Margin 불성립",
    59: "면집 링크 결합은 Link 불성립",
    60: "교합 규칙 결합은 Rule 불성립",
    61: "전망 식별자 결합은 Identifier 불성립",
    62: "해산물 형식 결합은 Format 불성립",
    63: "치과 일련번호 결합은 Serial 불성립",
    64: "배낭여행 서명 결합은 Signature 불성립",
    65: "교정의 자산 결합은 Asset 불성립",
    66: "패러세일링 기한 결합은 Due 불성립",
    67: "치위 선금 결합은 Advance 다의어 불성립",
    68: "야생동물 가산율 결합은 Markup 불성립",
    69: "치실 재판 결합은 Trial 다의어 불성립",
    70: "라군 라벨 결합은 Label 불성립",
    72: "빙하 배치도 결합은 여행 서비스와 결합 불명확",
    73: "불소 렌더링 결합은 Rendering 불성립",
    74: "화산 키트 결합은 여행 서비스와 결합 불명확",
    75: "실런트 합계 결합은 Total 불성립",
    76: "당일여행 저장소 결합은 Repository 불성립",
    77: "치은염 변환기 결합은 Converter 추상 불성립",
    78: "요트 기록기 결합은 여행 서비스와 결합 불명확",
    79: "이갈이 탐지기 결합은 Detector 추상 불성립",
    81: "구취 무대 결합은 Stage 다의어 불성립",
    82: "우릴 연승 속성 결합은 Streak 불성립",
    83: "치주염 비교 속성 결합은 Comparison 불성립",
    84: "사막 보증 속성 결합은 Guarantee 불성립",
    85: "부정교합 사본 결합은 Copy 다의어 불성립",
    86: "와이너리 참고자료 결합은 Reference 불성립",
    87: "치수과 기한 속성 결합은 Deadline 불성립",
    88: "치주 진단 속성 결합은 Diagnostic 불성립",
    89: "투어 교육 결합은 Tour 단독 다의어 불명확",
    91: "의료 제공자 일정표 결합 불명확",
    93: "손해사정 리트리트 결합 불성립",
    97: "트럼펫 일정표 결합 불명확",
    98: "챠지백 권고 결합 불명확",
    100: "보험 특약 토너먼트 결합 불성립",
    101: "채용 후보자 전단 결합 불명확",
    103: "미성년자/부전공 다의어 결합은 Minor 불명확",
    104: "동영상 소견 결합 불명확",
    105: "설문 권고 결합 불명확",
    107: "이벤트 녹화 선물 결합 불성립 - Gift",
    108: "외식 토너먼트 결합은 Dine 단독 결합 불명확",
    109: "중성화 전단 결합 불명확",
    110: "카페 부스 결합은 Booth 불성립",
    111: "다이너 초안 결합은 Draft 다의어 불성립",
    112: "비스트로 요금 속성 결합은 Fee 불성립",
    113: "피자집 일련번호 결합은 Serial 불성립",
    114: "델리 메시지 결합은 Message 불성립",
    115: "디저트 기간 속성 결합은 Duration 불성립",
    116: "포장 추천 결합은 Nomination 불성립",
    117: "브런치 시계 결합은 Clock 불성립",
    118: "베이커리 행렬 결합은 Matrix 불성립",
    119: "검사/시험 다의어 결합은 Test 불명확",
    121: "드리야지 일정표 결합 불명확",
    122: "부동산 중개 소견 결합 불명확",
    123: "보험사 권고 결합은 Carrier 다의어 불명확",
    125: "단열 시공 선물 결합 불성립 - Gift",
    126: "과외 리트리트 결합 불성립",
    127: "포트홀 토너먼트 결합 불성립",
    129: "제과 책상 결합은 Desk 불성립",
    130: "베이글 스튜디오 결합은 Studio 불성립",
    131: "도넛 모니터 결합은 Monitor 추상 불성립",
    132: "에스프레소 여권 결합은 Passport 불성립",
    133: "라떼 전망 속성 결합은 View 불성립",
    134: "칫솔 파일 결합은 File 불성립",
    135: "스노클링 업데이트 결합은 Update 다의어 불성립",
    137: "치약 주문 결합은 Order 다의어 불성립",
    138: "카약 코드 결합은 Code 불성립",
    139: "바리스타 패스 결합은 Pass 다의어 불성립",
    140: "구강청격 바우처 결합은 제품 결합 불성립",
    141: "폭포 진술서 결합은 Statement 불성립",
    142: "펍 회람 결합은 Circular 다의어 불성립",
    143: "마우스가드 자문 결합은 Advisory 추상 불성립",
    145: "스테이크하우스 유닛 결합은 Unit 다의어 불성립",
    147: "수변 가격 속성 결합은 Price 불성립",
    148: "스시 부채 결합은 Debt 불성립",
    149: "호흡 기금 결합은 Fund 불성립",
    150: "보드워크 판매 결합은 Sale 다의어 불성립",
    151: "타코 가치 속성 결합은 Value 불성립",
    152: "코골이 지분 결합은 Stake 불성립",
    153: "해변 벌금 결합은 Fine 불성립",
    154: "면집 규칙 결합은 Rule 불성립",
    155: "교합 상세 결합은 Detail 불성립",
    156: "전망 분류 결합은 Category 불성립",
    157: "해산물 일련번호 결합은 Serial 불성립",
    158: "치과 토큰 결합은 Token 불성립",
    159: "배낭여행 마커 결합은 Marker 불성립",
    160: "교정의 부과금 결합은 Levy 불성립",
    161: "패러세일링 보조금 결합은 Subsidy 불성립",
    162: "치위 벌칙 결합은 Penalty 불성립",
    163: "야생동물 리딤 결합은 Redemption 불성립",
    164: "치실 그래프 결합은 Graph 불성립",
    165: "라군 매뉴얼 결합은 여행 서비스와 결합 불명확",
    167: "빙하 스케치 결합은 여행 서비스와 결합 불명확",
    168: "불소 통지 결합은 Notification 불성립",
    169: "화산 횟수 결합은 여행 서비스와 결합 불명확",
    170: "실런트 위젯 결합은 Widget 불성립",
    171: "당일여행 공지 결합은 여행 서비스와 결합 불명확",
    172: "치은염 생성기 결합은 Generator 추상 불성립",
    173: "요트 견적기 결합은 여행 서비스와 결합 불명확",
    174: "이갈이 타이머 결합은 Timer 추상 불성립",
    175: "산책로 보호자 결합은 Guardian 추상 불성립",
    176: "구취 결과 속성 결합은 Result 불성립",
    177: "우릴 순위 속성 결합은 Rank 불성립",
    178: "치주염 제안 결합은 Proposal 불성립",
    179: "사막 기록 속성 결합은 Record 불성립",
    180: "부정교합 판독 결합은 Reading 다의어 불성립",
    181: "와이너리 예측 속성 결합은 Forecast 불성립",
    182: "치수과 기간 속성 결합은 Duration 불성립",
    183: "치주 진행 속성 결합은 Progress 불성립",
    185: "투어 핸드북 결합은 Tour 단독 다의어 불명확",
    186: "드럼 일정표 결합 불명확",
    187: "의료 제공자 소견 결합 불명확",
    188: "창고 선물 결합 불성립 - Gift",
    189: "손해사정 토너먼트 결합 불성립",
    192: "관광 명소 일정표 결합 불명확",
    193: "트럼펫 소견 결합 불명확",
    195: "증거개시 선물 결합 불성립 - Gift",
    199: "미성년자/부전공 일정표 결합은 Minor 불명확",
    200: "동영상 권고 결합 불명확",
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
