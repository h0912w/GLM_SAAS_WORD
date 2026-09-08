import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk16_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk16_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "합주 핸드북으로 실재 (Handbook 라인)"),
    5: (0.6, "리모델링 세미나로 실재 (Seminar 라인)"),
    9: (0.6, "편입 설명회 전단으로 실재 (Flyer 라인)"),
    16: (0.6, "카약 트레일로 실재 (Trail 물리 코스)"),
    22: (0.6, "일몰 시간 캘린더로 성립 (Calendar 라인)"),
    30: (0.6, "코골이 기록으로 성립 (Log 실재 기록)"),
    39: (0.6, "패러세일링 투어 입장권으로 성립 (Ticket 라인)"),
    40: (0.6, "스케일링 영수증으로 성립 (Receipt 라인)"),
    48: (0.6, "실런트 시술 예약 확정서로 성립 (Confirmation 라인)"),
    62: (0.6, "토양 핸드북으로 실재 (Handbook 라인)"),
    65: (0.6, "크리에이티브 세미나로 실재 (Seminar 라인)"),
    69: (0.6, "보안 감사 세미나 전단으로 실재 (Flyer 라인)"),
    74: (0.6, "선거 교육 세미나로 실재 (Seminar 라인)"),
    78: (0.6, "네트워크 세미나 전단으로 실재 (Flyer 라인)"),
    80: (0.6, "예산 핸드북으로 실재 (Handbook 라인)"),
    88: (0.6, "잇몸 관리 안내 전단으로 실재 (Flyer 라인)"),
    97: (0.6, "제과 리뷰로 성립 (Review 음식 리뷰 독해)"),
    100: (0.6, "놀이터 안전 관리 교육으로 실재 (Tutorial 라인)"),
    101: (0.6, "카지노 게임 가이드로 실재 (Handbook 라인)"),
    109: (0.6, "패티오 시공 안내 전단으로 실재 (Flyer 라인)"),
    122: (0.6, "일몰 명소 목록으로 성립 (Directory 라인)"),
    123: (0.6, "스테이크하우스 부스석으로 실재 (Booth 실물 공간)"),
    139: (0.6, "패러세일링 투어 견적으로 성립 (Estimate 견적)"),
    143: (0.6, "라군 투어 바우처로 성립 (Voucher 라인)"),
    150: (0.6, "치은염 치료 계획으로 성립 (Plan 라인)"),
    162: (0.6, "채점 교육으로 실재 (Tutorial 라인)"),
    169: (0.6, "로밍 요금제 안내 전단으로 실재 (Flyer 라인)"),
    170: (0.6, "동문 네트워크 가이드로 실재 (Handbook 라인)"),
    178: (0.6, "도장 시공 교육으로 실재 (Tutorial 라인)"),
    183: (0.6, "채용 실무 세미나로 실재 (Seminar 라인)"),
    187: (0.6, "진드기 예방 안내 전단으로 실재 (Flyer 라인)"),
    191: (0.6, "케이터링 주문 확정서로 성립 (Confirmation 라인)"),
    194: (0.6, "브런치집 랭킹으로 성립 (Rank 랭킹 독해)"),
    196: (0.6, "제과 레시피로 실재 (Recipe 라인)"),
    199: (0.6, "대체약 교육으로 실재 (Tutorial 라인)"),
    200: (0.6, "놀이터 관리 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "부상 일정표 결합 불명확",
    3: "채권자 소견 결합 불명확",
    4: "냉장 컨테이너 권고 결합 불명확",
    6: "보험 조정 선물 결합 불성립 - Gift",
    7: "교육 리트리트 결합 불성립",
    8: "패티오 토너먼트 결합 불성립",
    10: "에스프레소 릴레이 결합은 Relay 불성립",
    11: "라떼 기반 결합은 Base 추상 불성립",
    12: "칫솔 장부 결합은 Ledger 불성립",
    13: "스노클링 스튜디오 결합 불명확",
    14: "칵테일 패널 결합은 Panel 불성립",
    15: "치약 저울 결합은 Scale 다의어 불성립",
    17: "바리스타 관리인 결합은 Keeper 불성립",
    18: "구강청격 관리자 결합은 Manager 불성립",
    19: "폭포 플래너 결합 불성립",
    20: "펍 플레이북 결합 불성립",
    21: "마우스가드 일지 결합 불성립",
    23: "스테이크하우스 계수기 결합은 Counter 다의어 불성립",
    24: "스마일 부스 결합 불명확",
    25: "수변 만 결합은 Bay 불성립",
    26: "스시 차트 결합 불성립",
    27: "호흡 수거함 결합은 Bin 불성립",
    28: "보드워크 로비 결합은 Lobby 불성립",
    29: "타코 리포트 결합 불성립",
    31: "해변 카드 결합은 Card 다의어 불성립",
    32: "면집 메모 결합은 Note 다의어 불성립",
    33: "교합 태그 결합은 Tag 다의어 불성립",
    34: "전망 상태 결합은 Status 불성립",
    35: "해산물 수준 속성 결합은 Level 불성립",
    36: "치과 요율 속성 결합은 Rate 불성립",
    37: "배낭여행 피드 결합은 Feed 추상 불성립",
    38: "교정의 알림 결합 불성립",
    41: "야생동물 목록 결합 불명확",
    42: "치실 샘플 결합은 Sample 다의어 불성립",
    43: "라군 통행 결합은 Pass 다의어 불성립",
    44: "치석 전표 결합은 Stub 불성립",
    45: "빙하 메모 결합은 Memo 다의어 불성립",
    46: "불소 회람 결합은 Bulletin 다의어 불성립",
    47: "화산 회람 결합은 Circular 다의어 불성립",
    49: "당일여행 항목 결합은 Entry 다의어 불성립",
    50: "치은염 단위 결합은 Unit 다의어 불성립",
    51: "요트 비용 속성 결합은 Cost 불성립",
    52: "이갈이 세금 결합은 Tax 불성립",
    53: "산책로 합계 결합은 Sum 다의어 불성립",
    54: "구취 현금 결합 불성립",
    55: "우릴 청구 결합은 Charge 다의어 불성립",
    56: "치주염 관세 결합은 Tariff 불성립",
    57: "사막 지분 결합은 Stake 불성립",
    58: "부정교합 벌금 결합은 Fine 불성립",
    59: "와이너리 버전 결합은 Version 불성립",
    60: "치수과 규칙 결합은 Rule 불성립",
    61: "치주과 분류 결합은 Category 불성립",
    63: "약정 의견 결합 불명확",
    64: "공청회 권고 결합은 Hearing 다의어 불명확",
    66: "아카이브 선물 결합 불성립 - Gift",
    67: "운전 리트리트 결합 불성립",
    68: "로밍 토너먼트 결합 불성립",
    70: "동문 튜토리얼 결합 불명확",
    71: "처리량 핸드북 결합은 Throughput 속성어 불성립",
    72: "사일로 일정표 결합 불명확",
    73: "장부 권고 결합 불명확",
    75: "배치 선물 결합 불성립 - Gift",
    76: "피드 리트리트 결합 불성립",
    77: "허가 토너먼트 결합 불성립",
    79: "선수과목 튜토리얼 결합 불명확",
    81: "캡션 일정표 결합 불명확",
    82: "감정 분석 소견 결합 불명확",
    83: "리크루터 권고 결합 불명확",
    84: "랜야드 세미나 결합 불명확",
    85: "점검 선물 결합 불성립 - Gift",
    86: "카페 리트리트 결합 불성립",
    87: "진드기 토너먼트 결합 불성립",
    89: "다이너 터미널 결합은 Terminal 불성립",
    90: "비스트로 사무실 결합 불성립",
    91: "피자집 요율 속성 결합은 Rate 불성립",
    92: "데리 청원 결합은 Petition 불성립",
    93: "디저트 세부 결합은 Detail 불성립",
    94: "포장 도면 결합은 Schematic 불성립",
    95: "브런치 연승 결합은 Streak 불성립",
    96: "베이커리 검증 결합은 Validation 불성립",
    98: "베이글 온도 속성 결합은 Temperature 불성립",
    99: "도넛 요건 결합은 Requirement 불성립",
    102: "합주 일정표 결합 불명확",
    103: "부상 소견 결합 불명확",
    104: "채권자 권고 결합 불명확",
    105: "냉장 컨테이너 세미나 결합 불명확",
    106: "리모델링 선물 결합 불성립 - Gift",
    107: "보험 조정 리트리트 결합 불성립",
    108: "교육 토너먼트 결합 불성립",
    110: "에스프레소 금고 결합은 Vault 불성립",
    111: "라떼 핵심 결합은 Core 추상 불성립",
    112: "칫솔 게시판 결합은 Board 다의어 불성립",
    113: "스노클링 실험실 결합은 Lab 불성립",
    114: "칵테일 저울 결합은 Scale 다의어 불성립",
    115: "치약 경로 결합은 Route 불성립",
    116: "카약 사슬 결합은 Chain 불성립",
    117: "바리스타 관리자 결합은 Manager 불성립",
    118: "구강청격 엔진 결합은 Engine 추상 불성립",
    119: "폭포 스케줄러 결합 불성립",
    120: "펍 일지 결합 불성립",
    121: "마우스가드 등록부 결합 불성립",
    124: "스마일 키오스크 결합 불명확",
    125: "수변 게시 결합은 Post 다의어 불성립",
    126: "스시 수거함 결합은 Bin 불성립",
    127: "호흡 여권 결합은 Passport 다의어 불성립",
    128: "보드워크 전광판 결합은 Ticker 불성립",
    129: "타코 기록 결합 불성립",
    130: "코골이 서식 결합은 Form 다의어 불성립",
    131: "해변 시트 결합은 Sheet 다의어 불성립",
    132: "면집 태그 결합은 Tag 다의어 불성립",
    133: "교합 프로필 결합 불성립",
    134: "전망 뷰 결합은 View 추상 불성립",
    135: "해산물 요율 속성 결합은 Rate 불성립",
    136: "치과 갱신 결합 불성립",
    137: "배낭여행 초안 결합은 Draft 다의어 불성립",
    138: "교정의 색인 결합은 Index 다의어 불성립",
    140: "치위 코드 결합은 Code 불성립",
    141: "야생동물 표 결합은 Table 다의어 불성립",
    142: "치실 슬롯 결합은 Slot 다의어 불성립",
    144: "치석 정산 결합은 Statement 불성립",
    145: "빙하 한도 결합은 Quota 속성어 불성립",
    146: "불소 요약 결합은 Brief 다의어 불성립",
    147: "화산 권고 결합은 Advisory 불성립",
    148: "실런트 정리 결합은 Recap 다의어 불성립",
    149: "당일여행 요금 결합은 Fee 불성립",
    151: "요트 가격 속성 결합은 Price 불성립",
    152: "이갈이 대출 결합 불성립",
    153: "산책로 부채 결합 불성립",
    154: "구취 판매 결합은 Sale 다의어 불성립",
    155: "우릴 의무 결합 불성립",
    156: "치주염 가치 결합은 Value 불성립",
    157: "사막 마진 속성 결합은 Margin 불성립",
    158: "부정교합 번호 속성 결합은 Number 불성립",
    159: "와이너리 링크 결합은 Link 불성립",
    160: "치수과 세부 결합은 Detail 불성립",
    161: "치주과 속성 결합은 Attribute 불성립",
    163: "토양 일정표 결합 불명확",
    164: "약정 권고 결합 불명확",
    165: "공청회 세미나 결합은 Hearing 다의어 불명확",
    166: "소재 선물 결합 불성립 - Gift",
    167: "아카이브 리트리트 결합 불성립",
    168: "운전 토너먼트 결합 불성립",
    171: "처리량 일정표 결합은 Throughput 속성어 불성립",
    172: "사일로 소견 결합 불명확",
    173: "장부 세미나 결합 불명확",
    174: "투표 선물 결합 불성립 - Gift",
    175: "배치 리트리트 결합 불성립",
    176: "피드 토너먼트 결합 불성립",
    177: "허가 전단 결합 불명확",
    179: "선수과목 핸드북 결합 불명확",
    180: "예산 일정표 결합 불명확",
    181: "캡션 소견 결합 불명확",
    182: "감정 분석 권고 결합 불명확",
    184: "랜야드 선물 결합 불성립 - Gift",
    185: "점검 리트리트 결합 불성립",
    186: "카페 토너먼트 결합 불성립",
    188: "다이너 센터 결합은 Center 불성립",
    189: "비스트로 계수기 결합은 Counter 다의어 불성립",
    190: "피자집 갱신 결합 불성립",
    192: "디저트 식별자 결합은 Identifier 불성립",
    193: "포장 배치 결합은 Layout 불성립",
    195: "베이커리 조회 결합은 Lookup 불성립",
    197: "베이글 압력 속성 결합은 Pressure 불성립",
    198: "도넛 감가상각 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 36, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 164, len(REJECT_REASON)
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
