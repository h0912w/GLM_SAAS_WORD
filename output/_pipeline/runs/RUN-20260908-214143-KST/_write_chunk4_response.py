import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk3_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk3_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "당일여행 상품 티켓으로 실재 (Ticket 구체 서비스)"),
    11: (0.6, "와이너리 투어 예약 확정으로 성립 (Confirmation 라인)"),
    14: (0.6, "미용실 수수료 정산 교육으로 성립 (Tutorial 라인)"),
    15: (0.6, "약 조제 핸드북으로 실재 (Handbook 라인)"),
    16: (0.6, "전세 선박 일정표로 성립 (Timetable 라인)"),
    19: (0.6, "필터 세미나로 실재 (Seminar 라인)"),
    23: (0.6, "전시 홍보 전단으로 실재 (Flyer 라인)"),
    24: (0.6, "추모 절차 실무 교육으로 실재 (Tutorial 라인)"),
    26: (0.6, "리콜 처리 일정표로 성립 (Timetable 라인)"),
    29: (0.6, "폐사 실무 세미나로 실재 (Seminar 라인)"),
    32: (0.6, "번역·통역 대회로 실재 (Tournament 라인)"),
    35: (0.6, "알레르기 관리 튜토리얼로 실재 (Tutorial 라인)"),
    36: (0.6, "송금 핸드북으로 실재 (Handbook 라인)"),
    37: (0.6, "섀시 반출입 일정표로 성립 (Timetable 라인)"),
    39: (0.6, "잔존물 처리 추천으로 성립 (Recommendation 라인)"),
    40: (0.6, "연금 세미나로 실재 (Seminar 라인)"),
    42: (0.6, "논문 집필 리트리트로 실재 (Retreat 라인)"),
    49: (0.6, "디저트 주문 수수료 안내로 성립 (Fee 라인)"),
    56: (0.7, "커피 감평 실무 평가로 실재 (Evaluation 도메인 실무)"),
    57: (0.6, "채무자 관리 교육으로 실재 (Tutorial 라인)"),
    58: (0.6, "플랫베드 핸드북으로 실재 (Handbook 라인)"),
    60: (0.6, "소송 소견서로 실재 (Opinion 라인)"),
    62: (0.6, "캐비닛 세미나로 실재 (Seminar 라인)"),
    66: (0.6, "칫솔 홍보 전단으로 실재 (Flyer 라인)"),
    82: (0.6, "산책 코스 계획 도구로 성립 (Planner 라인)"),
    84: (0.6, "코골이 관리 플레이북으로 성립 (Playbook 라인)"),
    88: (0.6, "전망대 포토부스로 실재 (Booth 공간)"),
    90: (0.6, "치과의 당직 명부로 성립 (Roster 라인)"),
    96: (0.6, "치실 기록 노트로 성립 (Note 라인)"),
    98: (0.6, "치석 이력 관리로 성립 (History 라인)"),
    101: (0.6, "화산 활동 요약으로 성립 (Summary 라인)"),
    103: (0.6, "당일여행 비용 견적으로 성립 (Estimate 라인)"),
    104: (0.6, "치은염 치료 영수증으로 성립 (Receipt 라인)"),
    105: (0.6, "요트 대여 목록으로 성립 (List 라인)"),
    114: (0.6, "치수 치료 수수료 안내로 성립 (Fee 라인)"),
    115: (0.6, "치주 치료 계획으로 실재 (Plan 라인)"),
    116: (0.6, "묘지 절차 실무 교육으로 성립 (Tutorial 라인)"),
    117: (0.6, "수수료 실무 핸드북으로 성립 (Handbook 라인)"),
    121: (0.6, "교대근무 세미나로 성립 (Seminar 라인)"),
    125: (0.6, "창고 보관 홍보 전단으로 실재 (Flyer 라인)"),
    126: (0.6, "의류 수선 실무 교육으로 실재 (Tutorial 라인)"),
    127: (0.6, "추모 핸드북으로 실재 (Handbook 라인)"),
    131: (0.6, "로그북 세미나로 실재 (Seminar 라인)"),
    135: (0.6, "이중언어 서비스 전단으로 실재 (Flyer 라인)"),
    137: (0.6, "아코디언 레슨 튜토리얼로 실재 (Tutorial 라인)"),
    138: (0.6, "알레르기 핸드북으로 실재 (Handbook 라인)"),
    139: (0.6, "정기송금 일정표로 성립 (Timetable 라인)"),
    142: (0.6, "잔존물 실무 세미나로 성립 (Seminar 라인)"),
    146: (0.6, "공청회 안내 전단으로 실재 (Flyer 라인)"),
    149: (0.6, "피자집 당직 명부로 성립 (Roster 라인)"),
    154: (0.6, "베이킹 연속 챌린지 기록으로 성립 (Streak 라인)"),
    159: (0.6, "질병 관리 튜토리얼로 실재 (Tutorial 라인)"),
    160: (0.6, "채무자 핸드북으로 실재 (Handbook 라인)"),
    161: (0.6, "플랫베드 운송 일정표로 성립 (Timetable 라인)"),
    162: (0.6, "동네 평가 콘텐츠로 성립 (Opinion 라인)"),
    164: (0.6, "피부양자 복지 설명회로 성립 (Seminar 라인)"),
    167: (0.6, "라테 아트 대회로 실재 (Tournament 라인)"),
    168: (0.6, "행동 교정 홍보 전단으로 실재 (Flyer 라인)"),
    169: (0.6, "칫솔 사용 추적 앱으로 실재 (Tracker 라인)"),
    180: (0.6, "스테이크하우스 푸드 트레일로 성립 (Trail 물리 코스)"),
    186: (0.6, "타코 창업 플레이북으로 성립 (Playbook 라인)"),
    187: (0.6, "코골이 기록 저널로 실재 (Journal 라인)"),
    188: (0.6, "해변 이벤트 캘린더로 성립 (Calendar 라인)"),
    193: (0.6, "치과 예약 알림으로 성립 (Alert 라인)"),
    198: (0.6, "야생동물 관찰 체크리스트로 성립 (Check 라인)"),
    200: (0.6, "라군 수질 상태 정보로 성립 (Status 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "치은염 청구서 결합 불성립",
    3: "요트 코드 결합 불성립",
    4: "이갈이 전표 결합은 Slip 다의어 불성립",
    5: "산책로 슬롯 결합은 Slot 다의어 불성립",
    6: "구취 배지 결합 불성립",
    7: "우릴 정산 결합은 Statement 불성립",
    8: "치주염 탭 결합은 Tab 다의어 불성립",
    9: "사막 요약 결합은 Brief 다의어 불성립",
    10: "부정교합 권고 결합은 Advisory 불성립",
    12: "치수과 항목 결합은 Entry 다의어 불성립",
    13: "치주과 단위 결합은 Unit 다의어 불성립",
    17: "연료 의견 결합 불성립",
    18: "교대 추천 결합 불성립",
    20: "마스터키 선물 결합 불성립 - Gift",
    21: "용어 리트리트 결합 불성립",
    22: "창고 토너먼트 결합 불성립",
    25: "체크아웃 핸드북 결합 불명확",
    27: "항만 의견 결합 불성립",
    28: "로그북 추천 결합 불성립",
    30: "코일 선물 결합 불성립 - Gift",
    31: "키패드 리트리트 결합 불성립",
    33: "마일리지 전단 결합 불성립",
    34: "카페 습도 속성 결합은 Humidity 불성립",
    38: "계약 변경 의견 결합 불성립",
    41: "사이딩 선물 결합 불성립 - Gift",
    43: "회의 토너먼트 결합 불성립",
    44: "헤드라인 전단 결합 불성립",
    45: "다이너 레이더 결합은 Radar 추상 불성립",
    46: "비스트로 저울 결합은 Scale 다의어 불성립",
    47: "피자집 항구 결합은 Harbor 불성립",
    48: "데리 타임라인 결합 불성립",
    50: "포장 속성 결합은 Attribute 불성립",
    51: "브런치 도면 결합은 Schematic 불성립",
    52: "베이커리 결과 결합은 Result 불성립",
    53: "페이스트리 케이스 결합은 Case 다의어 불성립",
    54: "베이글 예측기 결합은 Predictor 불성립",
    55: "도넛 높이 속성 결합은 Height 불성립",
    59: "동네 시간표 결합 불성립",
    61: "피부양자 추천 결합 불성립",
    63: "철회 선물 결합은 Withdrawal 다의어 불성립",
    64: "라테 리트리트 결합 불성립",
    65: "행동 토너먼트 결합 불성립",
    67: "스노클링 허브 결합은 Hub 불성립",
    68: "칵테일 폭포 결합은 Cascade 추상 불성립",
    69: "치약 다리 결합은 Bridge 불성립",
    70: "카약 스코프 결합은 Scope 불성립",
    71: "바리스타 지도 결합은 Map 불성립",
    72: "구강청격 틀 결합은 Frame 추상 불성립",
    73: "폭포 장부 결합은 Ledger 불성립",
    74: "펍 터미널 결합은 Terminal 불성립",
    75: "마우스가드 센터 결합은 Center 불성립",
    76: "선셋 포털 결합은 Portal 불명확",
    77: "스테이크하우스 레일 결합은 Rail 다의어 불성립",
    78: "스마일 트레일 결합 불성립",
    79: "수변 링 결합은 Ring 불성립",
    80: "스시 관리자 결합은 Manager 불명확",
    81: "구채 엔진 결합은 Engine 추상 불성립",
    83: "타코 운영 결합은 Ops 불성립",
    85: "해변 등록부 결합 불명확",
    86: "면집 검색기 결합은 Finder 불명확",
    87: "교합 사무실 결합 불성립",
    89: "해산물 항구 결합은 Harbor 불성립",
    91: "배낭여행 차트 결합 불명확",
    92: "교정의 전광판 결합은 Ticker 불성립",
    93: "패러세일링 창 결합은 Window 다의어 불성립",
    94: "치위 형식 결합은 Form 다의어 불성립",
    95: "야생동물 시트 결합은 Sheet 다의어 불성립",
    97: "라군 프로필 결합 불성립",
    99: "빙하 수준 속성 결합은 Level 불성립",
    100: "불소 피드 결합은 Feed 추상 불성립",
    102: "실런트 색인 결합은 Index 다의어 불성립",
    106: "이갈이 표본 결합은 Sample 다의어 불성립",
    107: "산책로 통행 결합은 Pass 다의어 불성립",
    108: "구취 전표 결합은 Stub 다의어 불성립",
    109: "우릴 메모 결합 불성립",
    110: "치주염 회람 결합은 Bulletin 다의어 불성립",
    111: "사막 회람 결합은 Circular 다의어 불성립",
    112: "부정교합 청원 결합은 Petition 불성립",
    113: "와이너리 정리 결합은 Recap 다의어 불성립",
    118: "조제 일정표 결합 불성립",
    119: "전세 의견 결합 불성립",
    120: "연료 추천 결합 불성립",
    122: "필터 선물 결합 불성립 - Gift",
    123: "마스터키 리트리트 결합 불성립",
    124: "용어 대회 결합 불성립",
    128: "체크아웃 시간표 결합 불명확",
    129: "리콜 의견 결합 불성립",
    130: "항만 추천 결합 불성립",
    132: "폐사 선물 결합 불성립 - Gift",
    133: "코일 리트리트 결합 불성립",
    134: "키패드 토너먼트 결합 불성립",
    136: "카페 에피소드 결합은 Episode 다의어 불성립",
    140: "섀시 의견 결합 불성립",
    141: "계약 변경 추천 결합 불성립",
    143: "연금 선물 결합 불성립 - Gift",
    144: "사이딩 리트리트 결합 불성립",
    145: "논문 토너먼트 결합 불성립",
    147: "다이너 릴레이 결합은 Relay 불성립",
    148: "비스트로 항로 결합은 Route 불성립",
    150: "데리 알림 결합 불성립",
    151: "디저트 항목 결합은 Item 다의어 불성립",
    152: "포장 분야 결합은 Field 다의어 불성립",
    153: "브런치 배치 결합은 Layout 불성립",
    155: "페이스트리 매칭 결합은 Match 불성립",
    156: "베이글 봉인 결합은 Seal 다의어 불성립",
    157: "도넛 폭 속성 결합은 Width 불성립",
    158: "에스프레소 설문 결합은 Questionnaire 불성립",
    163: "소송 추천 결합 불성립",
    165: "캐비닛 선물 결합 불성립 - Gift",
    166: "철회 리트리트 결합은 Withdrawal 다의어 불성립",
    170: "스노클링 책상 결합은 Desk 불성립",
    171: "칵테일 다리 결합은 Bridge 다의어 불성립",
    172: "치약 신호 결합은 Signal 추상 불성립",
    173: "카약 루프 결합은 Loop 추상 불성립",
    174: "바리스타 틀 결합은 Frame 추상 불성립",
    175: "구강청격 기지 결합은 Base 추상 불성립",
    176: "폭포 보드 결합은 Board 다의어 불성립",
    177: "펍 센터 결합은 Center 불성립",
    178: "마우스가드 존 결합은 Zone 불성립",
    179: "선셋 콘솔 결합은 Console 불성립",
    181: "스마일 사슬 결합은 Chain 다의어 불성립",
    182: "수변 관문 결합은 Gate 불성립",
    183: "스시 엔진 결합은 Engine 추상 불성립",
    184: "구채 조수 결합은 Assistant 불명확",
    185: "복도 스케줄러 결합 불성립",
    189: "면집 사무실 결합 불성립",
    190: "교합 계수기 결합은 Counter 다의어 불성립",
    191: "전망 키오스크 결합은 Kiosk 불성립",
    192: "해산물 명부 결합 불성립",
    194: "배낭여행 상자 결합은 Bin 불성립",
    195: "교정의 줄 결합은 Line 다의어 불성립",
    196: "패러세일링 명부 결합은 Roll 불성립",
    197: "치위 카드 결합은 Card 다의어 불성립",
    199: "치실 태그 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 66, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 134, len(REJECT_REASON)
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
