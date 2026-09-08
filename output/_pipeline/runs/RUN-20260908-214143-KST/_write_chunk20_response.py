import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk19_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk19_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "놀이터 안전 세미나로 실재 (Seminar 라인)"),
    36: (0.6, "교정 치료 영수증으로 성립 (Receipt 라인)"),
    39: (0.6, "야생동물 투어 바우처로 성립 (Voucher 라인)"),
    46: (0.6, "실런트 치료 계획으로 성립 (Plan 라인)"),
    60: (0.7, "보험 보장 내용 교육으로 실재 (도메인 실무 개념)"),
    61: (0.6, "연차 핸드북으로 실재 (Handbook 라인)"),
    65: (0.6, "채점 연수 세미나로 실재 (Seminar 라인)"),
    75: (0.6, "송금 절차 교육으로 실재 (Tutorial 라인)"),
    76: (0.6, "트레일러 핸드북으로 실재 (Handbook 라인)"),
    80: (0.6, "도장 기술 세미나로 실재 (Seminar 라인)"),
    91: (0.6, "포장 키트로 실재 (Kit 실물 세트)"),
    94: (0.6, "제과 구독 뉴스레터로 실재 (Newsletter 라인)"),
    96: (0.6, "도넛 만들기 튜토리얼로 실재 (Tutorial 라인)"),
    101: (0.6, "대체약 세미나로 실재 (Seminar 라인)"),
    158: (0.6, "보험 보장 핸드북으로 실재 (Handbook 라인)"),
    162: (0.6, "컨시어지 서비스 세미나로 실재 (Seminar 라인)"),
    165: (0.7, "백오더 실무 교육으로 실재 (도메인 실무 개념)"),
    173: (0.6, "접종 안내 교육으로 실재 (Tutorial 라인)"),
    174: (0.6, "송금 핸드북으로 실재 (Handbook 라인)"),
    178: (0.6, "퇴직 설명 세미나로 실재 (Seminar 라인)"),
    192: (0.6, "제과 재고 관리로 성립 (Inventory 재고 독해)"),
    194: (0.6, "변속기 정비 교육으로 실재 (Tutorial 라인)"),
    195: (0.6, "도넛 핸드북으로 실재 (Handbook 라인)"),
    199: (0.6, "스타일링 세미나로 실재 (Seminar 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "스타일 소견 결합 불명확",
    2: "대체약 권고 결합 불명확",
    4: "카지노 선물 결합 불성립 - Gift",
    5: "합주 리트리트 결합 불성립",
    6: "부상 토너먼트 결합 불성립",
    7: "채권자 전단 결합 불명확",
    8: "에스프레소 다리 결합은 Bridge 불성립",
    9: "라떼 실험실 결합은 Lab 불성립",
    10: "칫솔 터미널 결합은 Terminal 불성립",
    11: "스노클링 포털 결합은 Portal 불성립",
    12: "칵테일 고리 결합은 Ring 불성립",
    13: "치약 문 결합은 Gate 불성립",
    14: "카약 관리인 결합은 Keeper 불성립",
    15: "바리스타 감시자 결합은 Monitor 불성립",
    16: "구강청격 동반자 결합은 Companion 불성립",
    17: "폭표 플레이북 결합은 Playbook 불성립",
    18: "펍 탐색기 결합은 Finder 불성립",
    19: "마우스가드 사무실 결합은 Office 불성립",
    20: "일몰 부스 결합 불명확",
    21: "스테이크하우스 명단 결합은 Roster 불성립",
    22: "스마일 경보 결합 불명확",
    23: "수변 수거함 결합은 Bin 불성립",
    24: "스시 창 결합은 Window 불성립",
    25: "호흡 굴림 결합은 Roll 불성립",
    26: "보드워크 기록 결합은 Log 불성립",
    27: "타코 점수 결합은 Score 불성립",
    28: "코골이 메모 결합은 Note 다의어 불성립",
    29: "해변 프로필 결합 불성립",
    30: "면집 파일 결합은 File 불성립",
    31: "교합 수준 속성 결합은 Level 불성립",
    32: "전망 갱신 결합은 Update 불성립",
    33: "해산물 타임라인 결합 불성립",
    34: "치과 알림 결합은 Reminder 불성립",
    35: "배낭여행 티켓 결합 불명확",
    37: "패러세일링 목록 결합 불명확",
    38: "치위 슬롯 결합은 Slot 다의어 불성립",
    40: "치실 정산 결합은 Statement 불성립",
    41: "라군 한도 결합은 Quota 속성어 불성립",
    42: "치석 요약 결합은 Brief 다의어 불성립",
    43: "빙하 권고 결합은 Advisory 불성립",
    44: "불소 정리 결합은 Recap 다의어 불성립",
    45: "화산 요금 결합은 Fee 불성립",
    47: "당일여행 가격 속성 결합은 Price 불성립",
    48: "치은염 대출 결합은 Loan 불성립",
    49: "요트 부채 결합은 Debt 불성립",
    50: "이갈이 판매 결합은 Sale 다의어 불성립",
    51: "산책로 의무 결합은 Duty 불성립",
    52: "구취 가치 결합은 Value 불성립",
    53: "우릴 마진 속성 결합은 Margin 불성립",
    54: "치주염 버전 결합은 Version 불성립",
    55: "사막 규칙 결합은 Rule 불성립",
    56: "부정교합 식별자 결합은 Identifier 불성립",
    57: "와이너리 속성 결합은 Attribute 불성립",
    58: "치수과 형식 결합은 Format 불성립",
    59: "치주과 서명 결합은 Signature 불성립",
    62: "건설 변경 일정표 결합은 Change 다의어 불성립",
    63: "공급업체 소견 결합 불명확",
    64: "컨시어지 권고 결합 불명확",
    66: "토양 리트리트 결합 불성립",
    67: "약정 전단 결합 불명확",
    68: "보험 바인더 핸드북 결합은 Binder 다의어 불성립",
    69: "인사 고과 일정표 결합은 Review 다의어 불성립",
    70: "유치권 소견 결합 불명확",
    71: "번들 권고 결합 불명확",
    72: "동문 선물 결합 불성립 - Gift",
    73: "처리량 리트리트 결합 불성립",
    74: "사일로 토너먼트 결합 불성립",
    77: "조건부 계약 일정표 결합 불명확",
    78: "보험 배상 소견 결합 불명확",
    79: "퇴직 권고 결합 불명확",
    81: "선수과목 선물 결합 불성립 - Gift",
    82: "예산 리트리트 결합 불성립",
    83: "캡션 토너먼트 결합 불성립",
    84: "감정 분석 전단 결합 불명확",
    85: "카페 책상 결합은 Desk 불성립",
    86: "다이너 저울 결합은 Scale 다의어 불성립",
    87: "비스트로 항구 결합은 Harbor 불성립",
    88: "피자집 알림 결합은 Reminder 불성립",
    89: "데리 단위 결합은 Unit 다의어 불성립",
    90: "디저트 일련번호 결합은 Serial 불성립",
    92: "브런치 기록 결합은 Record 불성립",
    93: "베이커리 방송 결합은 Broadcast 불성립",
    95: "베이글 빈도 속성 결합은 Frequency 불성립",
    97: "안락사 핸드북 결합 불명확",
    98: "임플란트 일정표 결합 불명확",
    99: "자장가 소견 결합 불명확",
    100: "스타일 권고 결합 불명확",
    102: "놀이터 선물 결합 불성립 - Gift",
    103: "카지노 리트리트 결합 불성립",
    104: "합주 토너먼트 결합 불성립",
    105: "부상 전단 결합 불명확",
    106: "에스프레소 신호 결합은 Signal 불성립",
    107: "라떼 기지 결합은 Station 불성립",
    108: "칫솔 센터 결합 불명확",
    109: "스노클링 콘솔 결합은 Console 불성립",
    110: "칵테일 문 결합은 Gate 불성립",
    111: "치약 연결점 결합은 Nexus 불성립",
    112: "카약 관리자 결합은 Manager 불성립",
    113: "바리스타 동반자 결합은 Companion 불성립",
    114: "구강청격 등기부 결합은 Register 다의어 불성립",
    115: "폭포 일지 결합 불성립",
    116: "펍 사무실 결합은 Office 불성립",
    117: "마우스가드 계수기 결합은 Counter 다의어 불성립",
    118: "일몰 키오스크 결합 불명확",
    119: "스테이크하우스 경보 결합 불명확",
    120: "스마일 차트 결합 불명확",
    121: "수변 여권 결합은 Passport 다의어 불성립",
    122: "스시 롤 결합은 음식명으로 서비스 불성립",
    123: "호흡 리포트 결합 불성립",
    124: "보드워크 서식 결합은 Form 다의어 불성립",
    125: "타코 메모 결합은 Note 다의어 불성립",
    126: "코골이 태그 결합은 Tag 다의어 불성립",
    127: "해변 상태 결합은 Status 불성립",
    128: "면집 수준 속성 결합은 Level 불성립",
    129: "교합 요율 속성 결합은 Rate 불성립",
    130: "전망 피드 결합은 Feed 추상 불성립",
    131: "해산물 알림 결합은 Reminder 불성립",
    132: "치과 색인 결합은 Index 다의어 불성립",
    133: "배낭여행 견적 결합 불명확",
    134: "교정의 코드 결합은 Code 불성립",
    135: "패러세일링 표 결합은 Table 다의어 불성립",
    136: "치위 통행 결합은 Pass 다의어 불성립",
    137: "야생동물 배지 결합은 Badge 불성립",
    138: "치실 메모 결합은 Memo 다의어 불성립",
    139: "라군 탭 결합은 Tab 불성립",
    140: "치석 회람 결합은 Circular 다의어 불성립",
    141: "빙하 청원 결합은 Petition 불성립",
    142: "불소 항목 결합은 Entry 다의어 불성립",
    143: "화산 품목 결합은 Item 다의어 불성립",
    144: "실런트 비용 속성 결합은 Cost 불성립",
    145: "당일여행 운임 속성 결합은 Fare 불성립",
    146: "치은염 합계 결합은 Sum 불성립",
    147: "요트 기금 결합은 Fund 불성립",
    148: "이갈이 청구 결합은 Charge 다의어 불성립",
    149: "산책로 수당 결합은 Allowance 불성립",
    150: "구취 지분 결합은 Stake 불성립",
    151: "우릴 벌금 결합은 Fine 불성립",
    152: "치주염 링크 결합은 Link 불성립",
    153: "사막 세부 결합은 Detail 불성립",
    154: "부정교합 분류 결합은 Category 불성립",
    155: "와이너리 분야 결합은 Field 불성립",
    156: "치수과 일련번호 결합은 Serial 불성립",
    157: "치주과 표식 결합은 Marker 불성립",
    159: "연차 일정표 결합 불명확",
    160: "건설 변경 소견 결합은 Change 다의어 불성립",
    161: "공급업체 권고 결합 불명확",
    163: "채점 선물 결합 불성립 - Gift",
    164: "토양 토너먼트 결합 불성립",
    166: "보험 바인더 일정표 결합은 Binder 다의어 불성립",
    167: "인사 고과 소견 결합은 Review 다의어 불성립",
    168: "유치권 권고 결합 불명확",
    169: "번들 세미나 결합 불명확",
    170: "동문 리트리트 결합 불성립",
    171: "처리량 토너먼트 결합 불성립",
    172: "사일로 전단 결합 불명확",
    175: "트레일러 일정표 결합 불명확",
    176: "조건부 계약 소견 결합 불명확",
    177: "보험 배상 권고 결합 불명확",
    179: "도장 선물 결합 불성립 - Gift",
    180: "선수과목 리트리트 결합 불성립",
    181: "예산 토너먼트 결합 불성립",
    182: "캡션 전단 결합 불명확",
    183: "카페 레이더 결합은 Radar 불성립",
    184: "다이너 경로 결합은 Route 불성립",
    185: "비스트로 명단 결합은 Roster 불성립",
    186: "피자집 색인 결합은 Index 다의어 불성립",
    187: "데리 계획 결합 불명확",
    188: "디저트 토큰 결합은 Token 불성립",
    189: "포장 계수 결합은 Count 불성립",
    190: "브런치 사본 결합은 Copy 다의어 불성립",
    191: "베이커리 바코드 결합 불명확",
    193: "베이글 호환성 결합 불성립",
    196: "안락사 일정표 결합 불성립",
    197: "임플란트 소견 결합 불명확",
    198: "자장가 권고 결합 불명확",
    200: "대체약 선물 결합 불성립 - Gift",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 24, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 176, len(REJECT_REASON)
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
