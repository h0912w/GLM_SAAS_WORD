import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk27_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk27_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    9: (0.6, "스키 기초 교육으로 실재 (Tutorial 라인)"),
    10: (0.6, "연주 곡목 핸드북으로 실재 (Handbook 라인)"),
    14: (0.6, "유사 매물 분석 세미나로 실재 (Seminar 라인)"),
    18: (0.6, "채점 세미나 전단으로 실재 (Flyer 라인)"),
    20: (0.6, "커피 클래스 스튜디오로 실재 (Studio 클래스 공간)"),
    72: (0.7, "도어 실린더 교체 교육으로 실재 (도메인 실무 개념)"),
    73: (0.6, "번역 교정 핸드북으로 실재 (Handbook 라인)"),
    77: (0.6, "퇴거 절차 세미나로 실재 (Seminar 라인)"),
    82: (0.7, "송풍기 유지보수 교육으로 실재 (도메인 실무 개념)"),
    83: (0.6, "자물쇠 사용 핸드북으로 실재 (Handbook 라인)"),
    92: (0.7, "소파 클리닝 교육으로 실재 (도메인 실무 개념)"),
    93: (0.6, "헤어 컬러링 핸드북으로 실재 (Handbook 라인)"),
    114: (0.6, "스키 기초 핸드북으로 실재 (Handbook 라인)"),
    128: (0.6, "칵테일 클래스 일정 캘린더로 성립 (Calendar 라인)"),
    176: (0.7, "압축기 유지보수 교육으로 실재 (도메인 실무 개념)"),
    177: (0.6, "도어 실린더 핸드북으로 실재 (Handbook 라인)"),
    187: (0.6, "송풍기 유지보수 핸드북으로 실재 (Handbook 라인)"),
    191: (0.6, "사진 조명 세미나로 실재 (Seminar 라인)"),
    196: (0.7, "아동 책읽기 교육으로 실재 (도메인 실무 개념)"),
    197: (0.6, "소파 클리닝 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "피자집 배지 결합은 Badge 불성립",
    2: "데리 관세 결합은 Tariff 불성립",
    3: "디저트 상환 결합은 Redemption 불성립",
    4: "포장 워크숍 결합 불명확",
    5: "브런치 회신 결합은 Reply 불성립",
    6: "베이커리 시뮬레이터 결합은 Simulator 불성립",
    7: "제과 깊이 속성 결합은 Depth 불성립",
    8: "베이글 설문지 결합은 Questionnaire 불성립",
    11: "병원 일정표 결합 불명확",
    12: "상속 소견 결합 불명확",
    13: "벌크 권고 결합 불명확",
    15: "보험금 선물 결합 불성립 - Gift",
    16: "수습 리트리트 결합 불성립",
    17: "데크 토너먼트 결합 불성립",
    19: "도넛 릴레이 결합은 Relay 불성립",
    21: "라떼 지도집 결합은 Atlas 불성립",
    22: "칫솔 관리자 결합은 Manager 불성립",
    23: "스노클링 플래너 결합은 Planner 불성립",
    24: "칵테일 등록부 결합은 Registry 불성립",
    25: "치약 캘린더 결합 불성립",
    26: "카약 탐색기 결합은 Finder 불성립",
    27: "바리스타 게시 결합은 Post 다의어 불성립",
    28: "구강청격 항구 결합은 Harbor 불성립",
    29: "폭포 차트 결합은 Chart 불성립",
    30: "펍 창 결합은 Window 불성립",
    31: "마우스가드 굴림 결합은 Roll 불성립",
    32: "일몰 기록 결합은 Log 불성립",
    33: "스테이크하우스 점수 결합은 Score 불성립",
    34: "스마일 메모 결합은 Note 다의어 불성립",
    35: "수변 프로필 결합 불성립",
    36: "스시 수준 속성 결합은 Level 불성립",
    37: "호흡 요율 속성 결합은 Rate 불성립",
    38: "보드워크 피드 결합은 Feed 추상 불성립",
    39: "타코 색인 결합은 Index 다의어 불성립",
    40: "코골이 티켓 결합 불성립",
    41: "해변 주문 결합은 Order 다의어 불성립",
    42: "면집 목록 결합은 List 다의어 불성립",
    43: "교합 표 결합은 Table 다의어 불성립",
    44: "전망 샘플 결합은 Sample 다의어 불성립",
    45: "해산물 배지 결합은 Badge 불성립",
    46: "치과 전표 결합은 Stub 다의어 불성립",
    47: "배낭여행 메모 결합은 Memo 다의어 불성립",
    48: "교정의 브리핑 결합은 Brief 다의어 불성립",
    49: "패러세일링 권고 결합은 Advisory 불성립",
    50: "치위 항목 결합은 Entry 다의어 불성립",
    51: "야생동물 품목 결합은 Item 다의어 불성립",
    52: "치실 비용 속성 결합은 Cost 불성립",
    53: "라군 운임 속성 결합은 Fare 불성립",
    54: "치석 합계 결합은 Sum 불성립",
    55: "빙하 기금 결합은 Fund 불성립",
    56: "불소 청구 결합은 Charge 다의어 불성립",
    57: "화산 수당 결합은 Allowance 불성립",
    58: "실런트 지분 결합은 Stake 불성립",
    59: "당일여행 벌금 결합은 Fine 불성립",
    60: "치은염 링크 결합은 Link 불성립",
    61: "요트 세부 결합은 Detail 불성립",
    62: "이갈이 속성 결합은 Attribute 불성립",
    63: "산책로 형식 결합은 Format 불성립",
    64: "구취 서명 결합은 Signature 불성립",
    65: "우릴 잔액 결합은 Balance 불성립",
    66: "치주염 과세 결합은 Levy 불성립",
    67: "사막 보조금 결합은 Subsidy 불성립",
    68: "부정교합 연체 결합은 Arrears 불성립",
    69: "와이너리 벌칙 결합은 Penalty 불성립",
    70: "치수과 상환 결합은 Redemption 불성립",
    71: "치주과 그래프 결합은 Graph 불성립",
    74: "짐 풀기 일정표 결합 불명확",
    75: "인화 교정쇄 소견 결합 불성립",
    76: "초대장 권고 결합 불명확",
    78: "수영장 조류 선물 결합 불성립 - Gift",
    79: "차량 시트 리트리트 결합 불성립",
    80: "싱크대 토너먼트 결합 불성립",
    81: "여행 전단 결합 불명확",
    84: "통역 일정표 결합 불명확",
    85: "이사 경로 소견 결합은 Route 추상 불성립",
    86: "사진 조명 권고 결합 불명확",
    87: "하객 선물 세미나 결합은 Favor 다의어 불명확",
    88: "입주자 선물 결합 불성립 - Gift",
    89: "기술자 리트리트 결합 불성립",
    90: "린스 토너먼트 결합 불성립",
    91: "뚫어락 전단 결합 불명확",
    94: "연고 일정표 결합 불명확",
    95: "가습기 소견 결합 불명확",
    96: "다이얼 조합 권고 결합 불명확",
    97: "어휘 세미나 결합 불명확",
    98: "이사 정산 선물 결합 불성립 - Gift",
    99: "사진 라이선스 리트리트 결합 불성립",
    100: "등록관 토너먼트 결합 불성립",
    101: "조경 전단 결합 불명확",
    102: "카페 지점 결합은 Point 다의어 불성립",
    103: "다이너 동반자 결합은 Companion 불성립",
    104: "비스트로 점검 결합은 Check 불성립",
    105: "피자집 전표 결합은 Stub 다의어 불성립",
    106: "데리 가치 속성 결합은 Value 불성립",
    107: "디저트 연장 결합은 Extension 불성립",
    108: "포장 수호자 결합은 Guardian 불성립",
    109: "브런치 계정 결합은 Account 불성립",
    110: "베이커리 예측기 결합은 Predictor 불성립",
    111: "제과 높이 속성 결합은 Height 불성립",
    112: "베이글 활용 결합은 Utilization 불성립",
    113: "클럽하우스 교육 결합 불명확",
    115: "연주 곡목 일정표 결합 불명확",
    116: "병원 소견 결합 불명확",
    117: "상속 권고 결합 불명확",
    118: "벌크 세미나 결합 불명확",
    119: "유사 매물 선물 결합 불성립 - Gift",
    120: "보험금 리트리트 결합 불성립",
    121: "수습 토너먼트 결합 불성립",
    122: "데크 전단 결합 불명확",
    123: "도넛 금고 결합은 Vault 불성립",
    124: "에스프레소 실험실 결합은 Lab 다의어 불성립",
    125: "라떼 관리인 결합은 Keeper 불성립",
    126: "칫솔 엔진 결합은 Engine 추상 불성립",
    127: "스노클링 스케줄러 결합은 Scheduler 불성립",
    129: "치약 디렉터리 결합 불성립",
    130: "카약 사무실 결합은 Office 불성립",
    131: "바리스타 항구 결합은 Harbor 불성립",
    132: "구강청격 명단 결합은 Roster 불성립",
    133: "폭표 수거함 결합은 Bin 불성립",
    134: "펍 굴림 결합은 Roll 불성립",
    135: "마우스가드 리포트 결합 불성립",
    136: "일몰 서식 결합은 Form 다의어 불성립",
    137: "스테이크하우스 메모 결합은 Note 다의어 불성립",
    138: "스마일 태그 결합은 Tag 다의어 불성립",
    139: "수변 상태 결합은 Status 불성립",
    140: "스시 요율 속성 결합은 Rate 불성립",
    141: "호흡 갱신 결합은 Update 불성립",
    142: "보드워크 초안 결합은 Draft 다의어 불성립",
    143: "타코 티켓 결합 불성립",
    144: "코골이 견적 결합 불성립",
    145: "해변 청구서 결합 불성립",
    146: "면집 표 결합은 Table 음식 결합 불성립",
    147: "교합 전표 결합은 Slip 다의어 불성립",
    148: "전망 슬롯 결합은 Slot 다의어 불성립",
    149: "해산물 전표 결합은 Stub 다의어 불성립",
    150: "치과 정산 결합은 Statement 다의어 불성립",
    151: "배낭여행 한도 결합은 Quota 속성어 불성립",
    152: "교정의 회람 결합은 Circular 다의어 불성립",
    153: "패러세일링 청원 결합은 Petition 불성립",
    154: "치위 요금 속성 결합은 Fee 불성립",
    155: "야생동물 단위 결합은 Unit 다의어 불성립",
    156: "치실 가격 속성 결합은 Price 불성립",
    157: "라군 세금 결합은 Tax 불성립",
    158: "치석 부채 결합은 Debt 불성립",
    159: "빙하 현금 결합은 Cash 불성립",
    160: "불소 의무 결합은 Duty 불성립",
    161: "화산 관세 결합은 Tariff 불성립",
    162: "실런트 마진 속성 결합은 Margin 불성립",
    163: "당일여행 번호 속성 결합은 Number 불성립",
    164: "치은염 규칙 결합은 Rule 불성립",
    165: "요트 식별자 결합은 Identifier 불성립",
    166: "이갈이 분야 결합은 Field 불성립",
    167: "산책로 일련번호 결합은 Serial 불성립",
    168: "구취 표식 결합은 Marker 불성립",
    169: "우릴 이자 결합은 Interest 불성립",
    170: "치주염 기한 결합은 Due 불성립",
    171: "사막 할인 결합은 Discount 불성립",
    172: "부정교합 선수금 결합은 Advance 불성립",
    173: "와이너리 가산율 결합은 Markup 불성립",
    174: "치수과 연장 결합은 Extension 불성립",
    175: "치주과 라벨 결합은 Label 불성립",
    178: "번역 교정 일정표 결합 불명확",
    179: "짐 풀기 소견 결합 불명확",
    180: "인화 교정쇄 권고 결합 불성립",
    181: "초대장 세미나 결합 불명확",
    182: "퇴거 선물 결합 불성립 - Gift",
    183: "수영장 조류 리트리트 결합 불성립",
    184: "차량 시트 토너먼트 결합 불성립",
    185: "싱크대 전단 결합 불명확",
    186: "매장량 교육 결합은 Reserve 다의어 불명확",
    188: "자물쇠 일정표 결합 불명확",
    189: "통역 소견 결합 불명확",
    190: "이사 경로 권고 결합은 Route 추상 불성립",
    192: "하객 선물 선물 결합 불성립 - Gift",
    193: "입주자 리트리트 결합 불성립",
    194: "기술자 토너먼트 결합 불성립",
    195: "린스 전단 결합 불명확",
    198: "컬러링 일정표 결합 불명확",
    199: "연고 소견 결합 불명확",
    200: "가습기 권고 결합 불명확",
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
