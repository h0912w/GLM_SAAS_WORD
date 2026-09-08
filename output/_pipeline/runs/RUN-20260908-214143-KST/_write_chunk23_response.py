import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk22_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk22_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "뷰티 세미나 안내 전단으로 실재 (Flyer 라인)"),
    5: (0.6, "스노클링 트레일로 실재 (Trail 물리 코스)"),
    14: (0.6, "일몰 시간 알림으로 성립 (Alert 라인)"),
    19: (0.6, "호흡 검사로 성립 (Check 검사 독해)"),
    27: (0.6, "해산물 도매 청구서로 성립 (Bill 실물 청구)"),
    28: (0.6, "치과 진료 영수증으로 성립 (Receipt 라인)"),
    31: (0.6, "패러세일링 투어 바우처로 성립 (Voucher 라인)"),
    54: (0.6, "보컬 교육 튜토리얼로 실재 (Tutorial 라인)"),
    63: (0.6, "클라리넷 핸드북으로 실재 (Handbook 라인)"),
    70: (0.6, "유치권 세미나 전단으로 실재 (Flyer 라인)"),
    71: (0.7, "수영장 개시 절차 교육으로 실재 (도메인 실무 개념)"),
    76: (0.6, "접종 세미나로 실재 (Seminar 라인)"),
    80: (0.6, "배상 세미나 전단으로 실재 (Flyer 라인)"),
    84: (0.6, "피자집 영수증으로 성립 (Receipt 라인)"),
    89: (0.6, "베이커리 케이터링 견적으로 성립 (Quote 견적)"),
    92: (0.7, "루브릭 작성 교육으로 실재 (도메인 실무 개념)"),
    93: (0.6, "국민투표 핸드북으로 실재 (Handbook 라인)"),
    97: (0.6, "정비 교육 세미나로 실재 (Seminar 라인)"),
    114: (0.6, "일몰 시간 차트로 성립 (Chart 실재 기록)"),
    126: (0.6, "전망대 입장 티켓으로 성립 (Ticket 라인)"),
    127: (0.6, "해산물 영수증으로 성립 (Receipt 라인)"),
    135: (0.6, "라군 투어 예약 확정서로 성립 (Confirmation 라인)"),
    155: (0.6, "보컬 핸드북으로 실재 (Handbook 라인)"),
    162: (0.6, "뚫어락 사용법 교육으로 실재 (Tutorial 라인)"),
    163: (0.6, "관광 가이드북으로 실재 (Handbook 라인)"),
    167: (0.6, "법령 해설 세미나로 실재 (Seminar 라인)"),
    171: (0.6, "조경 관리 교육으로 실재 (Tutorial 라인)"),
    172: (0.6, "수영장 개시 핸드북으로 실재 (Handbook 라인)"),
    180: (0.6, "조건부 계약 세미나 전단으로 실재 (Flyer 라인)"),
    192: (0.6, "데크 시공 교육으로 실재 (Tutorial 라인)"),
    193: (0.6, "루브릭 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "에스프레소 파도 결합은 Wave 불성립",
    3: "라떼 콘솔 결합은 Console 불성립",
    4: "칫솔 저울 결합은 Scale 다의어 불성립",
    6: "칵테일 엔진 결합은 Engine 추상 불성립",
    7: "치약 보조원 결합은 Assistant 불성립",
    8: "카약 감시자 결합은 Monitor 불성립",
    9: "바리스타 등록부 결합은 Registry 불성립",
    10: "구강청격 캘린더 결합 불성립",
    11: "폭포 탐색기 결합은 Finder 불성립",
    12: "펍 게시 결합은 Post 다의어 불성립",
    13: "마우스가드 항구 결합은 Harbor 불성립",
    15: "스테이크하우스 전광판 결합은 Ticker 불성립",
    16: "스마일 라인 결합은 Line 다의어 불성립",
    17: "수변 굴림 결합은 Roll 불성립",
    18: "스시 시트 결합은 Sheet 다의어 불성립",
    20: "보드워크 메모 결합은 Note 다의어 불성립",
    21: "타코 역사 결합 불성립",
    22: "코골이 파일 결합은 File 불성립",
    23: "해변 요율 속성 결합은 Rate 불성립",
    24: "면집 요약 결합은 Summary 불성립",
    25: "교합 타임라인 결합 불성립",
    26: "전망 색인 결합은 Index 다의어 불성립",
    29: "배낭여행 목록 결합 불명확",
    30: "교정의 슬롯 결합은 Slot 다의어 불성립",
    32: "치위 메모 결합은 Memo 다의어 불성립",
    33: "야생동물 탭 결합은 Tab 불성립",
    34: "치실 회람 결합은 Circular 다의어 불성립",
    35: "라군 청원 결합은 Petition 불성립",
    36: "치석 항목 결합은 Entry 다의어 불성립",
    37: "빙하 품목 결합은 Item 다의어 불성립",
    38: "불소 비용 속성 결합은 Cost 불성립",
    39: "화산 운임 속성 결합은 Fare 불성립",
    40: "실런트 합계 결합은 Sum 불성립",
    41: "당일여행 기금 결합은 Fund 불성립",
    42: "치은염 청구 결합은 Charge 다의어 불성립",
    43: "요트 수당 결합은 Allowance 불성립",
    44: "이갈이 지분 결합은 Stake 불성립",
    45: "산책로 벌금 결합은 Fine 불성립",
    46: "구취 링크 결합은 Link 불성립",
    47: "우릴 세부 결합은 Detail 불성립",
    48: "치주염 속성 결합은 Attribute 불성립",
    49: "사막 형식 결합은 Format 불성립",
    50: "부정교합 토큰 결합은 Token 불성립",
    51: "와이너리 표식 결합은 Marker 불성립",
    52: "치수과 이자 결합은 Interest 불성립",
    53: "치주과 기한 결합은 Due 불성립",
    55: "결제 일정표 결합 불명확",
    56: "계약 수정 소견 결합 불명확",
    57: "팔레트 권고 결합 불명확",
    58: "보험 보장 선물 결합 불성립 - Gift",
    59: "연차 리트리트 결합 불성립",
    60: "건설 변경 토너먼트 결합은 Change 다의어 불성립",
    61: "공급업체 전단 결합 불명확",
    62: "관광 튜토리얼 결합 불명확",
    64: "환자 동의 일정표 결합 불명확",
    65: "에스크로 소견 결합 불명확",
    66: "법령 권고 결합 불명확",
    67: "백오더 세미나 결합 불명확",
    68: "보험 바인더 리트리트 결합은 Binder 다의어 불성립",
    69: "인사 고과 토너먼트 결합은 Review 다의어 불성립",
    72: "버킷 핸드북 결합 불성립",
    73: "연수기 일정표 결합 불명확",
    74: "여행자 소견 결합 불명확",
    75: "만돌린 권고 결합 불명확",
    77: "송금 선물 결합 불성립 - Gift",
    78: "트레일러 리트리트 결합 불성립",
    79: "조건부 계약 토너먼트 결합 불성립",
    81: "카페 대장간 결합은 Forge 불성립",
    82: "다이너 문 결합은 Gate 불성립",
    83: "비스트로 로비 결합은 Lobby 불성립",
    85: "데리 대출 결합은 Loan 불성립",
    86: "디저트 자산 결합은 Asset 불성립",
    87: "포장 공지 결합 불성립",
    88: "브런치 기간 속성 결합은 Duration 불성립",
    90: "제과 길이 속성 결합은 Length 불성립",
    91: "베이글 에피소드 결합 불성립",
    94: "스토리 일정표 결합 불명확",
    95: "인턴십 소견 결합 불명확",
    96: "출석 권고 결합 불명확",
    98: "도넛 선물 결합 불성립 - Gift",
    99: "안락사 리트리트 결합 불성립",
    100: "임플란트 토너먼트 결합 불성립",
    101: "자장가 전단 결합 불명확",
    102: "에스프레소 길 결합은 Path 불성립",
    103: "라떼 패널 결합은 Panel 불성립",
    104: "칫솔 경로 결합은 Route 불성립",
    105: "스노클링 사슬 결합은 Chain 불성립",
    106: "칵테일 보조원 결합은 Assistant 불성립",
    107: "치약 플래너 결합은 Planner 불성립",
    108: "카약 동반자 결합은 Companion 불성립",
    109: "바리스타 캘린더 결합 불성립",
    110: "구강청격 디렉터리 결합 불성립",
    111: "폭포 사무실 결합은 Office 불성립",
    112: "펍 항구 결합은 Harbor 불성립",
    113: "마우스가드 명단 결합은 Roster 불성립",
    115: "스테이크하우스 라인 결합은 Line 다의어 불성립",
    116: "스마일 창 결합은 Window 불성립",
    117: "수변 리포트 결합 불성립",
    118: "스시 점검 결합 불성립",
    119: "호흡 점수 결합은 Score 불성립",
    120: "보드워크 태그 결합은 Tag 다의어 불성립",
    121: "타코 파일 결합은 File 불성립",
    122: "코골이 수준 속성 결합은 Level 불성립",
    123: "해변 갱신 결합은 Update 불성립",
    124: "면집 타임라인 결합 불성립",
    125: "교합 알림 결합은 Reminder 불성립",
    128: "치과 코드 결합은 Code 불성립",
    129: "배낭여행 표 결합은 Table 다의어 불성립",
    130: "교정의 통행 결합은 Pass 다의어 불성립",
    131: "패러세일링 배지 결합은 Badge 불성립",
    132: "치위 한도 결합은 Quota 속성어 불성립",
    133: "야생동물 회람 결합은 Bulletin 다의어 불성립",
    134: "치실 권고 결합은 Advisory 불성립",
    136: "치석 요금 결합은 Fee 불성립",
    137: "빙하 단위 결합은 Unit 다의어 불성립",
    138: "불소 가격 속성 결합은 Price 불성립",
    139: "화산 세금 결합은 Tax 불성립",
    140: "실런트 부채 결합은 Debt 불성립",
    141: "당일여행 현금 결합은 Cash 불성립",
    142: "치은염 의무 결합은 Duty 불성립",
    143: "요트 관세 결합은 Tariff 불성립",
    144: "이갈이 마진 속성 결합은 Margin 불성립",
    145: "산책로 번호 속성 결합은 Number 불성립",
    146: "구취 규칙 결합은 Rule 불성립",
    147: "우릴 식별자 결합은 Identifier 불성립",
    148: "치주염 분야 결합은 Field 불성립",
    149: "사막 일련번호 결합은 Serial 불성립",
    150: "부정교합 서명 결합은 Signature 불성립",
    151: "와이너리 잔액 결합은 Balance 불성립",
    152: "치수과 자산 결합은 Asset 불성립",
    153: "치주과 보조금 결합은 Subsidy 불성립",
    154: "여행 튜토리얼 결합 불명확",
    156: "결제 소견 결합 불명확",
    157: "계약 수정 권고 결합 불명확",
    158: "팔레트 세미나 결합 불명확",
    159: "보험 보장 리트리트 결합 불성립",
    160: "연차 토너먼트 결합 불성립",
    161: "건설 변경 전단 결합은 Change 다의어 불성립",
    164: "클라리넷 일정표 결합 불명확",
    165: "환자 동의 소견 결합 불명확",
    166: "에스크로 권고 결합 불명확",
    168: "백오더 선물 결합 불성립 - Gift",
    169: "보험 바인더 토너먼트 결합은 Binder 다의어 불성립",
    170: "인사 고과 전단 결합은 Review 다의어 불성립",
    173: "버킷 일정표 결합 불성립",
    174: "연수기 소견 결합 불명확",
    175: "여행자 권고 결합 불명확",
    176: "만돌린 세미나 결합 불명확",
    177: "접종 선물 결합 불성립 - Gift",
    178: "송금 리트리트 결합 불성립",
    179: "트레일러 토너먼트 결합 불성립",
    181: "카페 폭포 결합은 Cascade 불성립",
    182: "다이너 연결점 결합은 Nexus 불성립",
    183: "비스트로 전광판 결합은 Ticker 불성립",
    184: "피자집 코드 결합은 Code 불성립",
    185: "데리 합계 결합은 Sum 불성립",
    186: "디저트 과세 결합은 Levy 불성립",
    187: "포장 계산기 결합 불명확",
    188: "브런치 부피 속성 결합은 Volume 불성립",
    189: "베이커리 보증 결합은 Warranty 불성립",
    190: "제과 무게 속성 결합은 Weight 불성립",
    191: "베이글 주기 결합은 Cycle 불성립",
    194: "국민투표 일정표 결합 불명확",
    195: "스토리 소견 결합 불명확",
    196: "인턴십 권고 결합 불명확",
    197: "출석 세미나 결합 불명확",
    198: "변속기 선물 결합 불성립 - Gift",
    199: "도넛 리트리트 결합 불성립",
    200: "안락사 토너먼트 결합 불성립",
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
