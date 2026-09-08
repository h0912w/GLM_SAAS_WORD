import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk23_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk23_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "임플란트 안내 전단으로 실재 (Flyer 라인)"),
    37: (0.6, "빙하 투어 계획으로 성립 (Plan 라인)"),
    54: (0.6, "싱크대 설치 교육으로 실재 (Tutorial 라인)"),
    58: (0.6, "계약 수정 실무 세미나로 실재 (Seminar 라인)"),
    61: (0.6, "연차 제도 안내 전단으로 실재 (Flyer 라인)"),
    63: (0.6, "뚫어락 사용법 핸드북으로 실재 (Handbook 라인)"),
    67: (0.6, "에스크로 실무 세미나로 실재 (Seminar 라인)"),
    72: (0.6, "조경 관리 핸드북으로 실재 (Handbook 라인)"),
    92: (0.7, "수습 절차 교육으로 실재 (도메인 실무 개념)"),
    93: (0.6, "데크 시공 핸드북으로 실재 (Handbook 라인)"),
    97: (0.6, "인턴십 프로그램 세미나로 실재 (Seminar 라인)"),
    154: (0.7, "차량 시트 관리 교육으로 실재 (도메인 실무 개념)"),
    155: (0.6, "싱크대 설치 핸드북으로 실재 (Handbook 라인)"),
    171: (0.7, "사진 라이선싱 교육으로 실재 (도메인 실무 개념)"),
    184: (0.6, "피자집 식탁으로 실재 (Table 실물 식탁)"),
    192: (0.7, "보험금 수령 절차 교육으로 실재 (도메인 실무 개념)"),
    193: (0.6, "수습 절차 핸드북으로 실재 (Handbook 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "에스프레소 지점 결합은 Point 다의어 불성립",
    3: "라떼 저울 결합은 Scale 다의어 불성립",
    4: "칫솔 레일 결합은 Rail 불성립",
    5: "스노클링 링 결합은 Ring 불성립",
    6: "칵테일 플래너 결합은 Planner 불성립",
    7: "치약 스케줄러 결합은 Scheduler 불성립",
    8: "카약 등록부 결합은 Register 다의어 불성립",
    9: "바리스타 디렉터리 결합 불성립",
    10: "구강청격 탐색기 결합은 Locator 불성립",
    11: "폭포 계수기 결합은 Counter 다의어 불성립",
    12: "펍 명단 결합은 Roster 불성립",
    13: "마우스가드 경보 결합 불성립",
    14: "일몰 수거함 결합은 Bin 불성립",
    15: "스테이크하우스 창 결합은 Window 불성립",
    16: "스마일 굴림 결합은 Roll 불성립",
    17: "수변 기록 결합은 Log 위치 추상 불성립",
    18: "스시 점수 결합은 Score 불성립",
    19: "호흡 메모 결합은 Note 다의어 불성립",
    20: "보드워크 프로필 결합 불성립",
    21: "타코 수준 속성 결합은 Level 불성립",
    22: "코골이 요율 속성 결합은 Rate 불성립",
    23: "해변 피드 결합은 Feed 추상 불성립",
    24: "면집 알림 결합은 Reminder 불성립",
    25: "교합 색인 결합은 Index 다의어 불성립",
    26: "전망 견적 결합 불성립",
    27: "해산물 코드 결합은 Code 불성립",
    28: "치과 목록 결합은 List 다의어 불성립",
    29: "배낭여행 전표 결합은 Slip 다의어 불성립",
    30: "교정의 바우처 결합 불명확",
    31: "패러세일링 전표 결합은 Stub 다의어 불성립",
    32: "치위 탭 결합은 Tab 다의어 불성립",
    33: "야생동물 브리핑 결합은 Brief 다의어 불성립",
    34: "치실 청원 결합은 Petition 불성립",
    35: "라군 정리 결합은 Recap 다의어 불성립",
    36: "치석 품목 결합은 Item 다의어 불성립",
    38: "불소 운임 속성 결합은 Fare 불성립",
    39: "화산 대출 결합은 Loan 불성립",
    40: "실런트 기금 결합은 Fund 불성립",
    41: "당일여행 판매 결합은 Sale 다의어 불성립",
    42: "치은염 수당 결합은 Allowance 불성립",
    43: "요트 가치 속성 결합은 Value 불성립",
    44: "이갈이 벌금 결합은 Fine 불성립",
    45: "산책로 버전 결합은 Version 불성립",
    46: "구취 세부 결합은 Detail 불성립",
    47: "우릴 분류 결합은 Category 불성립",
    48: "치주염 형식 결합은 Format 불성립",
    49: "사막 토큰 결합은 Token 불성립",
    50: "부정교합 표식 결합은 Marker 불성립",
    51: "와이너리 이자 결합은 Interest 불성립",
    52: "치수과 과세 결합은 Levy 불성립",
    53: "치주과 할인 결합은 Discount 불성립",
    55: "여행 핸드북 결합 불명확",
    56: "보컬 일정표 결합 불명확",
    57: "결제 권고 결합 불명확",
    59: "팔레트 선물 결합 불성립 - Gift",
    60: "보험 보장 토너먼트 결합 불성립",
    62: "린스 튜토리얼 결합 불명확",
    64: "관광 일정표 결합 불명확",
    65: "클라리넷 소견 결합 불명확",
    66: "환자 동의 권고 결합 불명확",
    68: "법령 선물 결합 불성립 - Gift",
    69: "백오더 리트리트 결합 불성립",
    70: "보험 바인더 전단 결합은 Binder 다의어 불성립",
    71: "등록관 튜토리얼 결합은 Registrar 다의어 불명확",
    73: "수영장 개시 일정표 결합 불명확",
    74: "버킷 소견 결합 불명확",
    75: "연수기 권고 결합 불명확",
    76: "여행자 세미나 결합 불명확",
    77: "만돌린 선물 결합 불성립 - Gift",
    78: "접종 리트리트 결합 불성립",
    79: "송금 토너먼트 결합 불성립",
    80: "트레일러 전단 결합 불명확",
    81: "카페 다리 결합은 Bridge 불성립",
    82: "다이너 지도집 결합은 Atlas 불성립",
    83: "비스트로 라인 결합은 Line 다의어 불성립",
    84: "피자집 목록 결합은 List 다의어 불성립",
    85: "데리 부채 결합은 Debt 불성립",
    86: "디저트 기한 결합은 Due 불성립",
    87: "포장 변환기 결합은 Converter 불성립",
    88: "브런치 진단 결합은 Diagnostic 불성립",
    89: "베이커리 보증금 결합은 Deposit 다의어 불성립",
    90: "제과 거리 속성 결합은 Distance 불성립",
    91: "베이글 고장 결합은 Breakdown 다의어 불성립",
    94: "루브릭 일정표 결합 불명확",
    95: "국민투표 소견 결합 불명확",
    96: "스토리 권고 결합 불명확",
    98: "출석 선물 결합 불성립 - Gift",
    99: "변속기 리트리트 결합 불성립",
    100: "도넛 토너먼트 결합 불성립",
    101: "안락사 전단 결합 불성립",
    102: "에스프레소 지도 결합은 Map 불성립",
    103: "라떼 경로 결합은 Route 추상 불성립",
    104: "칫솔 트레일 결합은 Trail 불성립",
    105: "스노클링 문 결합은 Gate 불성립",
    106: "칵테일 스케줄러 결합은 Scheduler 불성립",
    107: "치약 감시자 결합은 Monitor 불성립",
    108: "카약 작전 결합은 Ops 불성립",
    109: "바리스타 탐색기 결합은 Locator 불성립",
    110: "구강청격 탐색기 결합은 Finder 불성립",
    111: "폭포 부스 결합은 Booth 불성립",
    112: "펍 경보 결합은 Alert 불성립",
    113: "마우스가드 차트 결합은 Chart 불성립",
    114: "일몰 여권 결합은 Passport 다의어 불성립",
    115: "스테이크하우스 굴림 결합은 Roll 불성립",
    116: "스마일 리포트 결합 불성립",
    117: "수변 서식 결합은 Form 다의어 불성립",
    118: "스시 메모 결합은 Note 다의어 불성립",
    119: "호흡 태그 결합은 Tag 다의어 불성립",
    120: "보드워크 상태 결합은 Status 불성립",
    121: "타코 요율 속성 결합은 Rate 불성립",
    122: "코골이 갱신 결합은 Update 불성립",
    123: "해변 초안 결합은 Draft 다의어 불성립",
    124: "면집 색인 결합은 Index 다의어 불성립",
    125: "교합 티켓 결합 불성립",
    126: "전망 주문 결합은 Order 다의어 불성립",
    127: "해산물 목록 결합은 List 다의어 불성립",
    128: "치과 표 결합은 Table 다의어 불성립",
    129: "배낭여행 샘플 결합은 Sample 다의어 불성립",
    130: "교정의 배지 결합은 Badge 불성립",
    131: "패러세일링 정산 결합은 Statement 다의어 불성립",
    132: "치위 회람 결합은 Bulletin 다의어 불성립",
    133: "야생동물 회람 결합은 Circular 다의어 불성립",
    134: "치실 확인서 결합 불성립",
    135: "라군 항목 결합은 Entry 다의어 불성립",
    136: "치석 단위 결합은 Unit 다의어 불성립",
    137: "빙하 비용 속성 결합은 Cost 불성립",
    138: "불소 세금 결합은 Tax 불성립",
    139: "화산 합계 결합은 Sum 불성립",
    140: "실런트 현금 결합은 Cash 불성립",
    141: "당일여행 청구 결합은 Charge 다의어 불성립",
    142: "치은염 관세 결합은 Tariff 불성립",
    143: "요트 지분 결합은 Stake 불성립",
    144: "이갈이 번호 속성 결합은 Number 불성립",
    145: "산책로 링크 결합은 Link 불성립",
    146: "구취 식별자 결합은 Identifier 불성립",
    147: "우릴 속성 결합은 Attribute 불성립",
    148: "치주염 일련번호 결합은 Serial 불성립",
    149: "사막 서명 결합은 Signature 불성립",
    150: "부정교합 잔액 결합은 Balance 불성립",
    151: "와이너리 자산 결합은 Asset 불성립",
    152: "치수과 기한 결합은 Due 불성립",
    153: "치주과 연체 결합은 Arrears 불성립",
    156: "여행 일정표 결합 불명확",
    157: "보컬 소견 결합 불명확",
    158: "결제 세미나 결합 불명확",
    159: "계약 수정 선물 결합 불성립 - Gift",
    160: "팔레트 리트리트 결합 불성립",
    161: "보험 보장 전단 결합 불명확",
    162: "기술자 교육 결합은 Technician 불명확",
    163: "린스 핸드북 결합 불명확",
    164: "뚫어락 일정표 결합 불명확",
    165: "관광 소견 결합 불명확",
    166: "클라리넷 권고 결합 불명확",
    167: "동의서 세미나 결합 불명확",
    168: "에스크로 선물 결합 불성립 - Gift",
    169: "법령 리트리트 결합 불성립",
    170: "백오더 토너먼트 결합 불성립",
    172: "등록관 핸드북 결합은 Registrar 다의어 불명확",
    173: "조경 일정표 결합 불명확",
    174: "수영장 개시 소견 결합 불명확",
    175: "버킷 권고 결합 불명확",
    176: "연수기 세미나 결합 불명확",
    177: "여행자 선물 결합 불성립 - Gift",
    178: "만돌린 리트리트 결합 불성립",
    179: "접종 토너먼트 결합 불성립",
    180: "송금 전단 결합 불명확",
    181: "카페 신호 결합은 Signal 추상 불성립",
    182: "다이너 관리인 결합은 Keeper 불성립",
    183: "비스트로 창 결합은 Window 불성립",
    185: "데리 기금 결합은 Fund 불성립",
    186: "디저트 보조금 결합은 Subsidy 불성립",
    187: "포장 생성기 결합은 Generator 불성립",
    188: "브런치 진행 결합은 Progress 불성립",
    189: "베이커리 인증 결합 불명확",
    190: "제과 범위 결합은 Range 다의어 불성립",
    191: "베이글 센서 결합은 Sensor 불성립",
    194: "데크 일정표 결합 불명확",
    195: "루브릭 소견 결합 불명확",
    196: "국민투표 권고 결합 불명확",
    197: "스토리 세미나 결합 불명확",
    198: "인턴십 선물 결합 불성립 - Gift",
    199: "출석 리트리트 결합 불성립",
    200: "변속기 토너먼트 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 17, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 183, len(REJECT_REASON)
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
