import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk20_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk20_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    21: (0.6, "호흡 기록으로 성립 (Log 실재 기록)"),
    39: (0.6, "빙하 투어 예약 확정서로 성립 (Confirmation 라인)"),
    56: (0.6, "팔레트 취급 교육으로 실재 (Tutorial 라인)"),
    64: (0.7, "법령 해설 교육으로 실재 (도메인 실무 개념)"),
    65: (0.6, "백오더 핸드북으로 실재 (Handbook 라인)"),
    68: (0.6, "건설 유치권 세미나로 실재 (Seminar 라인)"),
    72: (0.6, "만돌린 레슨 튜토리얼로 실재 (Tutorial 라인)"),
    73: (0.6, "접종 핸드북으로 실재 (Handbook 라인)"),
    77: (0.6, "보험 배상 실무 세미나로 실재 (Seminar 라인)"),
    93: (0.6, "출석 관리 교육으로 실재 (Tutorial 라인)"),
    94: (0.6, "변속기 핸드북으로 실재 (Handbook 라인)"),
    102: (0.6, "카지노 게임 강습 안내 전단으로 실재 (Flyer 라인)"),
    113: (0.6, "펍 부스석으로 실재 (Booth 실물 공간)"),
    129: (0.6, "치과 치료 견적으로 성립 (Estimate 견적)"),
    140: (0.6, "화산 투어 계획으로 성립 (Plan 라인)"),
    155: (0.7, "계약 수정 실무 교육으로 실재 (도메인 실무 개념)"),
    156: (0.6, "팔레트 핸드북으로 실재 (Handbook 라인)"),
    163: (0.7, "에스크로 절차 교육으로 실재 (도메인 실무 개념)"),
    164: (0.6, "법령 핸드북으로 실재 (Handbook 라인)"),
    172: (0.6, "만돌린 핸드북으로 실재 (Handbook 라인)"),
    176: (0.7, "조건부 계약 세미나로 실재 (도메인 실무 개념)"),
    182: (0.6, "다이너 투어 코스로 실재 (Trail 물리 코스)"),
    192: (0.6, "인턴십 절차 교육으로 실재 (Tutorial 라인)"),
    193: (0.6, "출석 핸드북으로 실재 (Handbook 라인)"),
    197: (0.6, "임플란트 세미나로 실재 (Seminar 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "놀이터 리트리트 결합 불성립",
    2: "카지노 토너먼트 결합 불성립",
    3: "합주 전단 결합 불명확",
    4: "에스프레소 시계 결합은 Watch 다의어 불성립",
    5: "라떼 터미널 결합은 Terminal 불성립",
    6: "칫솔 구역 결합은 Zone 불성립",
    7: "스노클링 패널 결합은 Panel 불성립",
    8: "칵테일 연결점 결합은 Nexus 불성립",
    9: "치약 지도집 결합은 Atlas 불성립",
    10: "카약 엔진 결합은 Engine 추상 불성립",
    11: "바리스타 등기부 결합은 Register 다의어 불성립",
    12: "구강청격 작전 결합은 Ops 불성립",
    13: "폭표 등록부 결합은 Registry 불성립",
    14: "펍 계수기 결합은 Counter 다의어 불성립",
    15: "마우스가드 부스 결합 불성립",
    16: "일몰 만 결합은 Bay 불성립",
    17: "스테이크하우스 차트 결합 불성립",
    18: "스마일 수거함 결합은 Bin 불성립",
    19: "수변 로비 결합은 Lobby 불성립",
    20: "스시 리포트 결합 불성립",
    22: "보드워크 카드 결합은 Card 다의어 불성립",
    23: "타코 태그 결합은 Tag 다의어 불성립",
    24: "코골이 프로필 결합 불성립",
    25: "해변 뷰 결합은 View 추상 불성립",
    26: "면집 요율 속성 결합은 Rate 불성립",
    27: "교합 갱신 결합은 Update 불성립",
    28: "전망 초안 결합은 Draft 다의어 불성립",
    29: "해산물 색인 결합은 Index 다의어 불성립",
    30: "치과 티켓 결합 불명확",
    31: "배낭여행 주문 결합은 Order 다의어 불성립",
    32: "교정의 목록 결합 불명확",
    33: "패러세일링 전표 결합은 Slip 다의어 불성립",
    34: "치위 바우처 결합 불명확",
    35: "야생동물 전표 결합은 Stub 불성립",
    36: "치실 한도 결합은 Quota 속성어 불성립",
    37: "라군 회람 결합은 Bulletin 다의어 불성립",
    38: "치석 권고 결합은 Advisory 불성립",
    40: "불소 요금 결합은 Fee 불성립",
    41: "화산 단위 결합은 Unit 다의어 불성립",
    42: "실런트 가격 속성 결합은 Price 불성립",
    43: "당일여행 세금 결합은 Tax 불성립",
    44: "치은염 부채 결합은 Debt 불성립",
    45: "요트 현금 결합은 Cash 불성립",
    46: "이갈이 의무 결합은 Duty 불성립",
    47: "산책로 관세 결합은 Tariff 불성립",
    48: "구취 마진 속성 결합은 Margin 불성립",
    49: "우릴 번호 속성 결합은 Number 불성립",
    50: "치주염 규칙 결합은 Rule 불성립",
    51: "사막 식별자 결합은 Identifier 불성립",
    52: "부정교합 속성 결합은 Attribute 불성립",
    53: "와이너리 형식 결합은 Format 불성립",
    54: "치수과 토큰 결합은 Token 불성립",
    55: "치주과 잔액 결합은 Balance 불성립",
    57: "보험 보장 일정표 결합 불명확",
    58: "연차 소견 결합 불명확",
    59: "건설 변경 권고 결합은 Change 다의어 불성립",
    60: "공급업체 세미나 결합 불명확",
    61: "컨시어지 선물 결합 불성립 - Gift",
    62: "채점 리트리트 결합 불성립",
    63: "토양 전단 결합 불명확",
    66: "보험 바인더 소견 결합은 Binder 다의어 불성립",
    67: "인사 고과 권고 결합은 Review 다의어 불성립",
    69: "번들 선물 결합 불성립 - Gift",
    70: "동문 토너먼트 결합 불성립",
    71: "처리량 전단 결합 불성립",
    74: "송금 일정표 결합 불명확",
    75: "트레일러 소견 결합 불명확",
    76: "조건부 계약 권고 결합 불명확",
    78: "퇴직 선물 결합 불성립 - Gift",
    79: "도장 리트리트 결합 불성립",
    80: "선수과목 토너먼트 결합 불성립",
    81: "예산 전단 결합 불명확",
    82: "카페 릴레이 결합은 Relay 불성립",
    83: "다이너 레일 결합은 Rail 불성립",
    84: "비스트로 경보 결합 불명확",
    85: "피자집 티켓 결합 불명확",
    86: "데리 비용 속성 결합은 Cost 불성립",
    87: "디저트 서명 결합은 Signature 불성립",
    88: "포장 메시지 결합 불성립",
    89: "브런치 낭독 결합은 Reading 불성립",
    90: "베이커리 예약 결합 불성립",
    91: "제과 청구 결합은 Claim 다의어 불성립",
    92: "베이글 용량 속성 결합은 Capacity 불성립",
    95: "도넛 일정표 결합 불명확",
    96: "안락사 소견 결합 불성립",
    97: "임플란트 권고 결합 불명확",
    98: "자장가 세미나 결합 불명확",
    99: "스타일 선물 결합 불성립 - Gift",
    100: "대체약 리트리트 결합 불성립",
    101: "놀이터 토너먼트 결합 불성립",
    103: "에스프레소 범위 결합은 Scope 불성립",
    104: "라떼 센터 결합 불명확",
    105: "칫솔 포털 결합은 Portal 불성립",
    106: "스노클링 저울 결합은 Scale 다의어 불성립",
    107: "칵테일 지도집 결합은 Atlas 불성립",
    108: "치약 관리인 결합은 Keeper 불성립",
    109: "카약 보조원 결합은 Assistant 불성립",
    110: "바리스타 작전 결합은 Ops 불성립",
    111: "구강청격 플레이북 결합은 Playbook 불성립",
    112: "폭포 캘린더 결합 불성립",
    114: "마우스가드 키오스크 결합 불성립",
    115: "일몰 게시 결합은 Post 다의어 불성립",
    116: "스테이크하우스 수거함 결합은 Bin 불성립",
    117: "스마일 여권 결합은 Passport 다의어 불성립",
    118: "수변 전광판 결합은 Ticker 불성립",
    119: "스시 기록 결합은 Log 불성립",
    120: "호흡 서식 결합은 Form 다의어 불성립",
    121: "보드워크 시트 결합은 Sheet 다의어 불성립",
    122: "타코 프로필 결합 불성립",
    123: "코골이 상태 결합은 Status 불성립",
    124: "해변 역사 결합 불성립",
    125: "면집 갱신 결합은 Update 불성립",
    126: "교합 피드 결합은 Feed 추상 불성립",
    127: "전망 요약 결합은 Summary 불성립",
    128: "해산물 티켓 결합 불명확",
    130: "배낭여행 청구서 결합 불명확",
    131: "교정의 표 결합은 Table 다의어 불성립",
    132: "패러세일링 샘플 결합은 Sample 다의어 불성립",
    133: "치위 배지 결합은 Badge 불성립",
    134: "야생동물 정산 결합은 Statement 불성립",
    135: "치실 탭 결합은 Tab 불성립",
    136: "라군 요약 결합은 Brief 다의어 불성립",
    137: "치석 청원 결합은 Petition 불성립",
    138: "빙하 정리 결합은 Recap 다의어 불성립",
    139: "불소 품목 결합은 Item 다의어 불성립",
    141: "실런트 운임 결합은 Fare 불성립",
    142: "당일여행 대출 결합은 Loan 불성립",
    143: "치은염 기금 결합은 Fund 불성립",
    144: "요트 판매 결합은 Sale 다의어 불성립",
    145: "이갈이 수당 결합은 Allowance 불성립",
    146: "산책로 가치 결합은 Value 불성립",
    147: "구취 벌금 결합은 Fine 불성립",
    148: "우릴 버전 결합은 Version 불성립",
    149: "치주염 세부 결합은 Detail 불성립",
    150: "사막 분류 결합은 Category 불성립",
    151: "부정교합 분야 결합은 Field 불성립",
    152: "와이너리 일련번호 결합은 Serial 불성립",
    153: "치수과 서명 결합은 Signature 불성립",
    154: "치주과 이자 결합은 Interest 불성립",
    157: "보험 보장 소견 결합 불명확",
    158: "연차 권고 결합 불명확",
    159: "건설 변경 세미나 결합은 Change 다의어 불성립",
    160: "공급업체 선물 결합 불성립 - Gift",
    161: "컨시어지 리트리트 결합 불성립",
    162: "채점 토너먼트 결합 불성립",
    165: "백오더 일정표 결합 불명확",
    166: "보험 바인더 권고 결합은 Binder 다의어 불성립",
    167: "인사 고과 세미나 결합은 Review 다의어 불성립",
    168: "유치권 선물 결합 불성립 - Gift",
    169: "번들 리트리트 결합 불성립",
    170: "동문 전단 결합 불명확",
    171: "여행자 튜토리얼 결합 불명확",
    173: "접종 일정표 결합 불명확",
    174: "송금 소견 결합 불명확",
    175: "트레일러 권고 결합 불명확",
    177: "보험 배상 선물 결합 불성립 - Gift",
    178: "퇴직 리트리트 결합 불성립",
    179: "도장 토너먼트 결합 불성립",
    180: "선수과목 전단 결합 불명확",
    181: "카페 금고 결합은 Vault 불성립",
    183: "비스트로 차트 결합 불성립",
    184: "피자집 견적 결합 불명확",
    185: "데리 가격 속성 결합은 Price 불성립",
    186: "디저트 표식 결합은 Marker 불성립",
    187: "포장 합계 결합은 Total 불성립",
    188: "브런치 참고 결합은 Reference 다의어 불성립",
    189: "베이커리 피드백 결합 불성립",
    190: "제과 온보딩 결합 불성립",
    191: "베이글 사용 결합은 Usage 불성립",
    194: "변속기 일정표 결합 불명확",
    195: "도넛 소견 결합 불명확",
    196: "안락사 권고 결합 불성립",
    198: "자장가 선물 결합 불성립 - Gift",
    199: "스타일 리트리트 결합 불성립",
    200: "대체약 토너먼트 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 25, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 175, len(REJECT_REASON)
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
