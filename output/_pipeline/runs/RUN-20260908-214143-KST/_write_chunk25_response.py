import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk24_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk24_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "도넛 가게 안내 전단으로 실재 (Flyer 라인)"),
    27: (0.6, "해산물 식당 식탁으로 실재 (Table 실물 식탁)"),
    36: (0.6, "치석 관리 계획으로 성립 (Plan 라인)"),
    54: (0.7, "수영장 조류 제거 교육으로 실재 (도메인 실무 개념)"),
    55: (0.6, "차량 시트 관리 핸드북으로 실재 (Handbook 라인)"),
    72: (0.7, "이사 비용 정산 절차 교육으로 실재 (도메인 실무 개념)"),
    73: (0.6, "사진 라이선싱 핸드북으로 실재 (Handbook 라인)"),
    81: (0.6, "접종 안내 전단으로 실재 (Flyer 라인)"),
    93: (0.7, "유사 매물 비교 분석 교육으로 실재 (도메인 실무 개념)"),
    94: (0.6, "보험금 수령 핸드북으로 실재 (Handbook 라인)"),
    98: (0.6, "국민투표 해설 세미나로 실재 (Seminar 라인)"),
    102: (0.6, "정비 교육 전단으로 실재 (Flyer 라인)"),
    126: (0.6, "면요리 케이터링 견적으로 성립 (Estimate 견적)"),
    156: (0.7, "퇴거 절차 교육으로 실재 (도메인 실무 개념)"),
    157: (0.6, "수영장 조류 제거 핸드북으로 실재 (Handbook 라인)"),
    174: (0.6, "법령 세미나 전단으로 실재 (Flyer 라인)"),
    175: (0.7, "어휘 학습 교육으로 실재 (도메인 실무 개념)"),
    176: (0.6, "이사 비용 정산 핸드북으로 실재 (Handbook 라인)"),
    197: (0.6, "유사 매물 비교 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "에스프레소 틀 결합은 Frame 불성립",
    3: "라떼 레일 결합은 Rail 불성립",
    4: "칫솔 사슬 결합은 Chain 불성립",
    5: "스노클링 연결점 결합은 Nexus 불성립",
    6: "칵테일 감시자 결합은 Monitor 불성립",
    7: "치약 동반자 결합은 Companion 불성립",
    8: "카약 플레이북 결합은 Playbook 불성립",
    9: "바리스타 탐색기 결합은 Finder 불성립",
    10: "구강청격 사무실 결합은 Office 불성립",
    11: "폭포 키오스크 결합은 Kiosk 불성립",
    12: "펍 차트 결합은 Chart 불성립",
    13: "마우스가드 수거함 결합은 Bin 불성립",
    14: "일몰 로비 결합은 Lobby 불성립",
    15: "스테이크하우스 리포트 결합 불성립",
    16: "스마일 기록 결합은 Log 불성립",
    17: "수변 카드 결합은 Card 다의어 불성립",
    18: "스시 태그 결합은 Tag 다의어 불성립",
    19: "호흡 프로필 결합 불성립",
    20: "보드워크 뷰 결합은 View 추상 불성립",
    21: "타코 갱신 결합은 Update 불성립",
    22: "코골이 피드 결합은 Feed 추상 불성립",
    23: "해변 요약 결합은 Summary 불성립",
    24: "면집 티켓 결합 불성립",
    25: "교합 견적 결합 불성립",
    26: "전망 청구서 결합 불성립",
    28: "치과 전표 결합은 Slip 다의어 불성립",
    29: "배낭여행 슬롯 결합은 Slot 다의어 불성립",
    30: "교정의 전표 결합은 Stub 다의어 불성립",
    31: "패러세일링 메모 결합은 Memo 다의어 불성립",
    32: "치위 브리핑 결합은 Brief 다의어 불성립",
    33: "야생동물 권고 결합은 Advisory 불성립",
    34: "치실 정리 결합은 Recap 다의어 불성립",
    35: "라군 요금 속성 결합은 Fee 불성립",
    37: "빙하 가격 속성 결합은 Price 불성립",
    38: "불소 대출 결합은 Loan 불성립",
    39: "화산 부채 결합은 Debt 불성립",
    40: "실런트 판매 결합은 Sale 다의어 불성립",
    41: "당일여행 의무 결합은 Duty 불성립",
    42: "치은염 가치 속성 결합은 Value 불성립",
    43: "요트 마진 속성 결합은 Margin 불성립",
    44: "이갈이 버전 결합은 Version 불성립",
    45: "산책로 규칙 결합은 Rule 불성립",
    46: "구취 분류 결합은 Category 불성립",
    47: "우릴 분야 결합은 Field 불성립",
    48: "치주염 토큰 결합은 Token 불성립",
    49: "사막 표식 결합은 Marker 불성립",
    50: "부정교합 이자 결합은 Interest 불성립",
    51: "와이너리 과세 결합은 Levy 불성립",
    52: "치수과 보조금 결합은 Subsidy 불성립",
    53: "치주과 선수금 결합은 Advance 불성립",
    56: "싱크대 일정표 결합 불명확",
    57: "여행 소견 결합 불명확",
    58: "보컬 권고 결합 불명확",
    59: "결제 선물 결합 불성립 - Gift",
    60: "계약 수정 리트리트 결합 불성립",
    61: "팔레트 토너먼트 결합 불성립",
    62: "입주자 튜토리얼 결합 불명확",
    63: "기술자 핸드북 결합은 Technician 불명확",
    64: "린스 일정표 결합 불명확",
    65: "뚫어락 소견 결합 불명확",
    66: "관광 권고 결합 불명확",
    67: "클라리넷 세미나 결합 불명확",
    68: "동의서 선물 결합 불성립 - Gift",
    69: "에스크로 리트리트 결합 불성립",
    70: "법령 토너먼트 결합 불성립",
    71: "백오더 전단 결합 불명확",
    74: "등록관 일정표 결합은 Registrar 다의어 불명확",
    75: "조경 소견 결합 불명확",
    76: "수영장 개시 권고 결합 불명확",
    77: "버킷 세미나 결합 불명확",
    78: "연수기 선물 결합 불성립 - Gift",
    79: "여행자 리트리트 결합 불성립",
    80: "만돌린 토너먼트 결합 불성립",
    82: "카페 시계 결합은 Watch 다의어 불성립",
    83: "다이너 관리자 결합은 Manager 불성립",
    84: "비스트로 굴림 결합은 Roll 불성립",
    85: "피자집 전표 결합은 Slip 다의어 불성립",
    86: "데리 현금 결합은 Cash 불성립",
    87: "디저트 할인 결합은 Discount 불성립",
    88: "포장 기록기 결합은 Recorder 불성립",
    89: "브런치 승인 결합은 Authorization 불성립",
    90: "베이커리 후보 지명 결합은 Nomination 불성립",
    91: "제과 한도 속성 결합은 Limit 불성립",
    92: "베이글 리셉션 결합 불명확",
    95: "수습 일정표 결합 불명확",
    96: "데크 소견 결합 불명확",
    97: "루브릭 권고 결합 불명확",
    99: "스토리 선물 결합 불성립 - Gift",
    100: "인턴십 리트리트 결합 불성립",
    101: "출석 토너먼트 결합 불성립",
    103: "도넛 추적자 결합은 Tracker 불성립",
    104: "에스프레소 기반 결합은 Base 추상 불성립",
    105: "라떼 트레일 결합은 Trail 불성립",
    106: "칫솔 링 결합은 Ring 불성립",
    107: "스노클링 지도집 결합은 Atlas 불성립",
    108: "칵테일 동반자 결합은 Companion 불성립",
    109: "치약 등기부 결합은 Register 다의어 불성립",
    110: "카약 저널 결합은 Journal 다의어 불성립",
    111: "바리스타 사무실 결합은 Office 불성립",
    112: "구강청격 계수기 결합은 Counter 다의어 불성립",
    113: "폭포 만 결합은 Bay 불성립",
    114: "펍 수거함 결합은 Bin 불성립",
    115: "마우스가드 여권 결합은 Passport 다의어 불성립",
    116: "일몰 전광판 결합은 Ticker 불성립",
    117: "스테이크하우스 기록 결합은 Log 위치 추상 불성립",
    118: "스마일 서식 결합은 Form 다의어 불성립",
    119: "수변 시트 결합은 Sheet 다의어 불성립",
    120: "스시 프로필 결합 불성립",
    121: "호흡 상태 결합은 Status 불성립",
    122: "보드워크 역사 결합 불성립",
    123: "타코 피드 결합은 Feed 추상 불성립",
    124: "코골이 초안 결합은 Draft 다의어 불성립",
    125: "해변 타임라인 결합 불성립",
    127: "교합 주문 결합은 Order 다의어 불성립",
    128: "전망 영수증 결합 불성립",
    129: "해산물 전표 결합은 Slip 다의어 불성립",
    130: "치과 샘플 결합은 Sample 다의어 불성립",
    131: "배낭여행 통행 결합은 Pass 다의어 불성립",
    132: "교정의 정산 결합은 Statement 다의어 불성립",
    133: "패러세일링 한도 결합은 Quota 속성어 불성립",
    134: "치위 회람 결합은 Circular 다의어 불성립",
    135: "야생동물 청원 결합은 Petition 불성립",
    136: "치실 항목 결합은 Entry 다의어 불성립",
    137: "라군 품목 결합은 Item 다의어 불성립",
    138: "치석 비용 속성 결합은 Cost 불성립",
    139: "빙하 운임 속성 결합은 Fare 불성립",
    140: "불소 합계 결합은 Sum 불성립",
    141: "화산 기금 결합은 Fund 불성립",
    142: "실런트 청구 결합은 Charge 다의어 불성립",
    143: "당일여행 수당 결합은 Allowance 불성립",
    144: "치은염 지분 결합은 Stake 불성립",
    145: "요트 벌금 결합은 Fine 불성립",
    146: "이갈이 링크 결합은 Link 불성립",
    147: "산책로 세부 결합은 Detail 불성립",
    148: "구취 속성 결합은 Attribute 불성립",
    149: "우릴 형식 결합은 Format 불성립",
    150: "치주염 서명 결합은 Signature 불성립",
    151: "사막 잔액 결합은 Balance 불성립",
    152: "부정교합 자산 결합은 Asset 불성립",
    153: "와이너리 기한 결합은 Due 불성립",
    154: "치수과 할인 결합은 Discount 불성립",
    155: "치주과 벌칙 결합은 Penalty 불성립",
    158: "차량 시트 일정표 결합 불명확",
    159: "싱크대 소견 결합 불명확",
    160: "여행 권고 결합 불명확",
    161: "보컬 세미나 결합 불명확",
    162: "결제 리트리트 결합 불성립",
    163: "계약 수정 토너먼트 결합 불성립",
    164: "팔레트 전단 결합 불명확",
    165: "하객 선물 튜토리얼 결합은 Favor 다의어 불명확",
    166: "입주자 핸드북 결합 불명확",
    167: "기술자 일정표 결합 불명확",
    168: "린스 소견 결합 불명확",
    169: "뚫어락 권고 결합 불명확",
    170: "관광 세미나 결합 불명확",
    171: "클라리넷 선물 결합 불성립 - Gift",
    172: "동의서 리트리트 결합 불성립",
    173: "에스크로 토너먼트 결합 불성립",
    177: "사진 라이선스 일정표 결합 불명확",
    178: "등록관 소견 결합은 Registrar 다의어 불명확",
    179: "조경 권고 결합 불명확",
    180: "수영장 개시 세미나 결합 불명확",
    181: "버킷 선물 결합 불성립 - Gift",
    182: "연수기 리트리트 결합 불성립",
    183: "여행자 토너먼트 결합 불성립",
    184: "만돌린 전단 결합 불명확",
    185: "카페 범위 결합은 Scope 추상 불성립",
    186: "다이너 엔진 결합은 Engine 추상 불성립",
    187: "비스트로 리포트 결합 불성립",
    188: "피자집 샘플 결합은 Sample 다의어 불성립",
    189: "데리 판매 결합은 Sale 다의어 불성립",
    190: "디저트 연체 결합은 Arrears 불성립",
    191: "포장 추정기 결합은 Estimator 불성립",
    192: "브런치 템플릿 결합 불명확",
    193: "베이커리 정정 결합은 Correction 불성립",
    194: "제과 유형 속성 결합은 Type 불성립",
    195: "베이글 후속 결합은 Followup 불성립",
    196: "벌크 운송 교육 결합 불명확",
    198: "보험금 일정표 결합 불명확",
    199: "수습 소견 결합 불명확",
    200: "데크 권고 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 19, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 181, len(REJECT_REASON)
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
