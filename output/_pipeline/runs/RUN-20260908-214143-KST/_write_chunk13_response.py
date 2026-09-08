import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk12_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk12_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    8: (0.6, "수변 행사 캘린더로 성립 (Calendar 라인)"),
    26: (0.6, "라군 투어 청구서로 성립 (Bill 라인)"),
    45: (0.6, "해외 로밍 설정 교육으로 실재 (Tutorial 라인)"),
    46: (0.6, "보안 감사 핸드북으로 실재 (Handbook 라인)"),
    54: (0.6, "운수 허가 신청 교육으로 실재 (Tutorial 라인)"),
    55: (0.6, "네트워크 핸드북으로 실재 (Handbook 라인)"),
    59: (0.6, "채용 리퍼럴 세미나로 실재 (Seminar 라인)"),
    65: (0.6, "반려동물 진드기 관리 교육으로 실재 (Tutorial 라인)"),
    66: (0.6, "잇몸 케어 핸드북으로 실재 (Handbook 라인)"),
    70: (0.6, "흡입기 사용법 세미나로 실재 (Seminar 라인)"),
    86: (0.6, "HR 교육 콘텐츠로 실재 (Tutorial 라인)"),
    87: (0.6, "패티오 시공 핸드북으로 실재 (Handbook 라인)"),
    91: (0.6, "적성 검사 세미나로 실재 (Seminar 라인)"),
    95: (0.6, "반려동물 식이 안내 전단으로 실재 (Flyer 라인)"),
    98: (0.6, "스노클링 스팟 지도로 실재 (Map 물리 지도)"),
    110: (0.6, "수변 명소 디렉터리로 성립 (Directory 라인)"),
    111: (0.6, "스시 페스티벌 부스로 실재 (Booth 실물 공간)"),
    128: (0.6, "라군 투어 영수증으로 성립 (Receipt 라인)"),
    131: (0.6, "불소 도포 바우처로 성립 (Voucher 라인)"),
    136: (0.6, "요트 대여 예약 확정서로 성립 (Confirmation 라인)"),
    147: (0.6, "운전 교육으로 실재 (Tutorial 라인)"),
    148: (0.6, "로밍 핸드북으로 실재 (Handbook 라인)"),
    152: (0.6, "추천서 작성 세미나로 실재 (Seminar 라인)"),
    158: (0.6, "허가 절차 핸드북으로 실재 (Handbook 라인)"),
    166: (0.6, "프랜차이즈 모집 전단으로 실재 (Flyer 라인)"),
    167: (0.6, "카페 창업 교육으로 실재 (Tutorial 라인)"),
    168: (0.6, "진드기 예방 핸드북으로 실재 (Handbook 라인)"),
    171: (0.6, "식기세척기 추천 가이드로 실재 (Recommendation 라인)"),
    172: (0.6, "미용 기술 세미나로 실재 (Seminar 라인)"),
    176: (0.6, "문법 강좌 안내 전단으로 실재 (Flyer 라인)"),
    184: (0.6, "베이커리 안내서로 실재 (Guide 라인)"),
    188: (0.6, "보험 청구 조정 교육으로 실재 (Tutorial 라인)"),
    189: (0.6, "교육 핸드북으로 실재 (Handbook 라인)"),
    193: (0.6, "기획 기사 세미나로 실재 (Seminar 라인)"),
    197: (0.6, "에스프레소 강좌 전단으로 실재 (Flyer 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "구강청격 레일 결합은 Rail 다의어 불성립",
    2: "폭포 고리 결합은 Ring 불성립",
    3: "펍 엔진 결합은 Engine 추상 불성립",
    4: "마우스가드 조수 결합은 Assistant 불명확",
    5: "선셋 스케줄러 결합 불성립",
    6: "스테이크하우스 플레이북 결합 불성립",
    7: "스마일 일지 결합 불명확",
    9: "스시 계수기 결합은 Counter 다의어 불성립",
    10: "호흡 부스 결합 불명확",
    11: "보드워크 만 결합은 Bay 불성립",
    12: "타코 차트 결합 불명확",
    13: "코골이 수거함 결합은 Bin 불성립",
    14: "해변 로비 결합은 Lobby 불성립",
    15: "면집 순서 결합은 Roll 다의어 불성립",
    16: "교합 리포트 결합 불성립",
    17: "전망 서식 결합은 Form 다의어 불성립",
    18: "해산물 점수 결합은 Score 불성립",
    19: "치과 메모 결합은 Note 다의어 불성립",
    20: "배낭여행 프로필 결합 불성립",
    21: "교정의 파일 결합은 File 다의어 불성립",
    22: "패러세일링 요율 속성 결합은 Rate 불성립",
    23: "치위 요약 결합 불성립",
    24: "야생동물 알림 결합 불성립",
    25: "치실 견적 결합 불성립",
    27: "치석 목록 결합 불명확",
    28: "빙하 전표 결합은 Slip 다의어 불성립",
    29: "불소 통행 결합은 Pass 다의어 불성립",
    30: "화산 배지 결합 불성립",
    31: "실런트 메모 결합은 Memo 다의어 불성립",
    32: "당일여행 탭 결합은 Tab 다의어 불성립",
    33: "치은염 회람 결합은 Circular 다의어 불성립",
    34: "요트 청원 결합은 Petition 불성립",
    35: "이갈이 항목 결합은 Entry 다의어 불성립",
    36: "산책로 항목 결합은 Item 다의어 불성립",
    37: "구취 비용 속성 결합은 Cost 불성립",
    38: "우릴 요금 결합은 Fare 다의어 불성립",
    39: "치주염 합계 결합은 Sum 다의어 불성립",
    40: "사막 기금 결합 불성립",
    41: "부정교합 판매 결합은 Sale 다의어 불성립",
    42: "와이너리 의무 결합 불성립",
    43: "치수과 관세 결합은 Tariff 불성립",
    44: "치주과 마진 속성 결합은 Margin 불성립",
    47: "파이프라인 일정표 결합 불명확",
    48: "환불 소견 결합 불명확",
    49: "추천서 권고 결합 불명확",
    50: "안건 세미나 결합 불명확",
    51: "금융 선물 결합 불성립 - Gift",
    52: "규정 리트리트 결합 불성립",
    53: "예약 토너먼트 결합 불성립",
    56: "경계 일정표 결합 불명확",
    57: "런북 소견 결합 불명확",
    58: "콜백 권고 결합 불명확",
    60: "피드백 선물 결합 불성립 - Gift",
    61: "감정 리트리트 결합 불성립",
    62: "프랜차이즈 토너먼트 결합 불성립",
    63: "퇴원 전단 결합 불명확",
    64: "카페 조율기 결합은 Tuner 불성립",
    67: "공예 일정표 결합 불명확",
    68: "식기세척기 소견 결합 불명확",
    69: "블로우 추천 결합 불명확",
    71: "제습기 선물 결합 불성립 - Gift",
    72: "마감로크 리트리트 결합 불성립",
    73: "문법 토너먼트 결합 불성립",
    74: "엘리베이터 전단 결합 불명확",
    75: "다이너 기반 결합은 Base 추상 불성립",
    76: "비스트로 운영 결합은 Ops 불성립",
    77: "피자집 메모 결합은 Note 다의어 불성립",
    78: "데리 정산 결합은 Statement 불성립",
    79: "디저트 가치 결합은 Value 불성립",
    80: "포장 사용 결합은 Redemption 불성립",
    81: "브런치 검증기 결합은 Checker 불성립",
    82: "베이커리 템플릿 결합 불명확",
    83: "제과 추천 결합은 Nomination 불성립",
    84: "베이글 한도 속성 결합은 Limit 불성립",
    85: "도넛 접수 결합은 Reception 다의어 불성립",
    88: "편입 일정표 결합 불명확",
    89: "구 소견 결합 불명확 - Ward",
    90: "기사 권고 결합 불명확",
    92: "네트워킹 선물 결합 불성립 - Gift",
    93: "라디에이터 리트리트 결합 불성립",
    94: "에스프레소 토너먼트 결합 불성립",
    96: "라떼 고리 결합은 Loop 추상 불성립",
    97: "칫솔 파도 결합은 Wave 추상 불성립",
    99: "칵테일 실험실 결합은 Lab 불성립",
    100: "치약 역 결합은 Station 다의어 불성립",
    101: "카약 구역 결합은 Zone 불성립",
    102: "바리스타 레일 결합은 Rail 다의어 불성립",
    103: "구강청격 산책로 결합은 Trail 불성립",
    104: "폭포 문 결합은 Gate 불성립",
    105: "펍 조수 결합은 Assistant 불명확",
    106: "마우스가드 플래너 결합 불성립",
    107: "선셋 모니터 결합 불성립",
    108: "스테이크하우스 일지 결합 불명확",
    109: "스마일 등록부 결합 불성립",
    112: "호흡 키오스크 결합 불명확",
    113: "보드워크 게시 결합은 Post 다의어 불성립",
    114: "타코 수거함 결합은 Bin 불성립",
    115: "코골이 여권 결합은 Passport 다의어 불성립",
    116: "해변 전광판 결합은 Ticker 불성립",
    117: "면집 리포트 결합 불성립",
    118: "교합 기록 결합 불성립",
    119: "전망 카드 결합은 Card 다의어 불성립",
    120: "해산물 메모 결합은 Note 다의어 불성립",
    121: "치과 태그 결합은 Tag 다의어 불성립",
    122: "배낭여행 상태 결합은 Status 불성립",
    123: "교정의 수준 속성 결합은 Level 불성립",
    124: "패러세일링 갱신 결합 불성립",
    125: "치위 타임라인 결합 불성립",
    126: "야생동물 색인 결합은 Index 다의어 불성립",
    127: "치실 주문 결합은 Order 다의어 불성립",
    129: "치석 표 결합은 Table 다의어 불성립",
    130: "빙하 샘플 결합은 Sample 다의어 불성립",
    132: "화산 전표 결합은 Stub 불성립",
    133: "실런트 한도 결합은 Quota 속성어 불성립",
    134: "당일여행 회람 결합은 Bulletin 다의어 불성립",
    135: "치은염 권고 결합은 Advisory 불성립",
    137: "이갈이 요금 결합은 Fee 불성립",
    138: "산책로 단위 결합은 Unit 다의어 불성립",
    139: "구취 가격 속성 결합은 Price 불성립",
    140: "우릴 세금 결합은 Tax 불성립",
    141: "치주염 부채 결합 불성립",
    142: "사막 현금 결합 불성립",
    143: "부정교합 청구 결합은 Charge 다의어 불성립",
    144: "와이너리 수당 결합 불성립",
    145: "치수과 가치 결합은 Value 불성립",
    146: "치주과 벌금 결합은 Fine 불성립",
    149: "감사 일정표 결합 불명확",
    150: "파이프라인 소견 결합 불명확",
    151: "환불 권고 결합 불명확",
    153: "안건 선물 결합 불성립 - Gift",
    154: "금융 리트리트 결합 불성립",
    155: "규정 토너먼트 결합 불성립",
    156: "예약 전단 결합 불명확",
    157: "피드 튜토리얼 결합 불명확",
    159: "네트워크 일정표 결합 불명확",
    160: "경계 소견 결합 불명확",
    161: "런북 권고 결합 불명확",
    162: "콜백 세미나 결합 불명확",
    163: "리퍼럴 선물 결합 불성립 - Gift",
    164: "피드백 리트리트 결합 불성립",
    165: "감정 토너먼트 결합 불성립",
    169: "잇몸 일정표 결합 불명확",
    170: "공예 의견 결합 불명확",
    173: "흡입기 선물 결합 불성립 - Gift",
    174: "제습기 리트리트 결합 불성립",
    175: "마감로크 토너먼트 결합 불성립",
    177: "다이너 핵심 결합은 Core 추상 불성립",
    178: "비스트로 플레이북 결합 불성립",
    179: "피자집 태그 결합은 Tag 다의어 불성립",
    180: "데리 메모 결합은 Memo 다의어 불성립",
    181: "디저트 지분 결합은 Stake 불성립",
    182: "포장 연장 결합은 Extension 불성립",
    183: "브런치 감지기 결합은 Detector 불성립",
    185: "제과 교정 결합은 Correction 불성립",
    186: "베이글 유형 속성 결합은 Type 불성립",
    187: "도넛 후속 결합은 Followup 불성립",
    190: "패티오 일정표 결합 불명확",
    191: "편입 의견 결합 불명확",
    192: "구 권고 결합 불명확 - Ward",
    194: "적성 선물 결합 불성립 - Gift",
    195: "네트워킹 리트리트 결합 불성립",
    196: "라디에이터 토너먼트 결합 불성립",
    198: "라떼 격자 결합은 Grid 추상 불성립",
    199: "칫솔 경로 결합은 Path 불성립",
    200: "스노클링 액자 결합은 Frame 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 35, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 165, len(REJECT_REASON)
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
