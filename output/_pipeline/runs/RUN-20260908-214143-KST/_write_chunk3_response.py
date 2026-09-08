import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk2_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk2_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    8: (0.6, "치수과 예약 확정 통지로 성립 (Confirmation 라인)"),
    9: (0.6, "치주 치료 수수료 안내로 성립 (Fee 라인)"),
    10: (0.6, "전세 선박 실무 교육으로 실재 (Tutorial 라인)"),
    11: (0.6, "항공 연료 핸드북으로 실재 (Handbook 라인)"),
    12: (0.6, "교대근무 시간표로 실재 (Timetable 라인)"),
    14: (0.6, "잠금 시스템 추천 서비스로 성립 (Recommendation 라인)"),
    15: (0.6, "번역 용어 세미나로 실재 (Seminar 라인)"),
    19: (0.6, "임대차 갱신 안내 전단으로 성립 (Flyer 라인)"),
    20: (0.6, "약국 리콜 절차 교육으로 실재 (Tutorial 라인)"),
    21: (0.6, "항만 핸드북으로 실재 (Handbook 라인)"),
    24: (0.6, "코일 교체 추천으로 성립 (Recommendation 라인)"),
    25: (0.6, "도어락 키패드 세미나로 실재 (Seminar 라인)"),
    28: (0.6, "사진 보정 콘테스트로 실재 (Tournament 라인)"),
    29: (0.6, "축사 서비스 홍보 전단으로 성립 (Flyer 라인)"),
    31: (0.6, "섀시 실무 교육으로 실재 (Tutorial 라인)"),
    32: (0.6, "계약 변경 핸드북으로 실재 (Handbook 라인)"),
    33: (0.6, "잔존물 처리 일정표로 성립 (Timetable 라인)"),
    34: (0.6, "연금 전문가 의견 칼럼으로 성립 (Opinion 라인)"),
    35: (0.6, "사이딩 자재 추천으로 성립 (Recommendation 라인)"),
    36: (0.6, "논문 세미나로 실재 (Seminar 라인)"),
    40: (0.6, "헤드헌팅 홍보 전단으로 실재 (Flyer 라인)"),
    47: (0.6, "브런치 계획 워크시트로 성립 (Worksheet 라인)"),
    53: (0.6, "이사 지역 안내 튜토리얼로 성립 (Tutorial 라인)"),
    54: (0.6, "소송 핸드북으로 실재 (Handbook 라인)"),
    56: (0.6, "캐비닛 디자인 컨설팅 소견으로 성립 (Opinion 라인)"),
    58: (0.6, "라테 아트 세미나로 실재 (Seminar 라인)"),
    62: (0.6, "보도 시공 서비스 전단으로 성립 (Flyer 라인)"),
    63: (0.6, "스노클링 기록 추적 앱으로 성립 (Tracker 라인)"),
    75: (0.6, "수변 산책 트레일 안내로 실재 (Trail 물리 경로)"),
    81: (0.6, "해변 사업 운영 플레이북으로 성립 (Playbook 라인)"),
    82: (0.6, "면집 디렉터리로 실재 (Directory 라인)"),
    84: (0.6, "전망 사무공간 임대로 실재 (Office 라인)"),
    90: (0.6, "치위 진료 보고서로 실재 (Report 라인)"),
    92: (0.6, "치실 사용 점검으로 성립 (Check 라인)"),
    93: (0.6, "라군 관찰 노트로 성립 (Note 라인)"),
    94: (0.6, "치석 관리 상태로 성립 (Status 라인)"),
    95: (0.6, "빙하 이력 정보로 실재 (History 라인)"),
    98: (0.6, "실런트 시술 타임라인으로 성립 (Timeline 라인)"),
    101: (0.6, "요트 렌탈 영수증으로 성립 (Receipt 라인)"),
    104: (0.6, "구취 치료 바우처로 성립 (Voucher 라인)"),
    112: (0.6, "약 조제 실무 교육으로 실재 (Tutorial 라인)"),
    113: (0.6, "전세 선박 핸드북으로 실재 (Handbook 라인)"),
    114: (0.6, "급유 일정표로 성립 (Timetable 라인)"),
    116: (0.6, "필터 추천 서비스로 실재 (Recommendation 라인)"),
    117: (0.6, "마스터키 세미나로 실재 (Seminar 라인)"),
    120: (0.6, "사진전 콘테스트로 실재 (Tournament 라인)"),
    121: (0.6, "꽃집 홍보 전단으로 실재 (Flyer 라인)"),
    123: (0.6, "리콜 핸드북으로 실재 (Handbook 라인)"),
    124: (0.6, "항만 배 시간표로 실재 (Timetable 라인)"),
    127: (0.6, "코일 실무 세미나로 실재 (Seminar 라인)"),
    131: (0.6, "보정 서비스 전단으로 실재 (Flyer 라인)"),
    133: (0.6, "송금 실무 교육으로 실재 (Tutorial 라인)"),
    134: (0.6, "섀시 핸드북으로 실재 (Handbook 라인)"),
    135: (0.6, "계약 변경 일정표로 성립 (Timetable 라인)"),
    136: (0.6, "잔존물 감정 소견으로 성립 (Opinion 라인)"),
    137: (0.6, "연금 상품 추천으로 성립 (Recommendation 라인)"),
    138: (0.6, "사이딩 세미나로 실재 (Seminar 라인)"),
    155: (0.6, "플랫베드 운송 실무 교육으로 실재 (Tutorial 라인)"),
    156: (0.6, "동네 안내 핸드북으로 실재 (Handbook 라인)"),
    157: (0.6, "소송 일정표로 실재 (Timetable 라인)"),
    159: (0.6, "캐비닛 추천 서비스로 실재 (Recommendation 라인)"),
    161: (0.6, "커피 선물 세트로 성립 (Gift 라인)"),
    164: (0.6, "보모 모집 전단으로 실재 (Flyer 라인)"),
    183: (0.6, "해변 여행 저널로 실재 (Journal 라인)"),
    189: (0.6, "배낭여행 특가 알림으로 성립 (Alert 라인)"),
    192: (0.6, "치위 작업 로그로 성립 (Log 라인)"),
    198: (0.6, "불소 도포 갱신 안내로 성립 (Update 라인)"),
    200: (0.6, "실런트 재시술 알림으로 성립 (Reminder 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "산책로 전표 결합은 Slip 다의어 불성립",
    2: "구취 통행 결합은 Pass 다의어 불성립",
    3: "우릴 배지 결합 불성립",
    4: "치주염 메모 결합 불성립",
    5: "사막 탭 결합은 Tab 다의어 불성립",
    6: "부정교합 요약 결합은 Brief 다의어 불성립",
    7: "와이너리 권고 결합은 Advisory 불성립",
    13: "필터 의견 결합 불성립",
    16: "창고 선물 결합 불성립 - Gift",
    17: "갤러리 리트리트 결합 불성립",
    18: "플로리스트 토너먼트 결합 불성립",
    22: "로그북 시간표 결합 불성립",
    23: "폐사 의견 결합 불성립",
    26: "이중언어 선물 결합 불성립 - Gift",
    27: "마일리지 리트리트 결합 불성립",
    30: "카페 사용량 속성 결합은 Usage 불성립",
    37: "회의 선물 결합 불성립 - Gift",
    38: "헤드라인 리트리트 결합 불성립",
    39: "우선순위 토너먼트 결합 불성립",
    41: "다이너 허브 결합은 Hub 불성립",
    42: "비스트로 콘솔 결합은 Console 불성립",
    43: "피자집 만 결합은 Bay 불성립",
    44: "데리 초안 결합은 Draft 다의어 불성립",
    45: "디저트 정리 결합은 Recap 다의어 불성립",
    46: "포장 식별자 결합은 Identifier 불성립",
    48: "베이커리 도우미 결합은 Helper 불명확",
    49: "페이스트리 회신 결합은 Reply 불성립",
    50: "베이글 검증 결합은 Verification 다의어 불성립",
    51: "도넛 속도 속성 결합은 Speed 불성립",
    52: "에스프레소 승인 결합은 Approval 다의어 불성립",
    55: "피부양자 시간표 결합 불성립",
    57: "철회 추천 결합은 Withdrawal 다의어 불성립",
    59: "행동 선물 결합 불성립 - Gift",
    60: "칫솔 리트리트 결합 불성립",
    61: "보모 토너먼트 결합 불성립",
    64: "칵테일 등대 결합은 Beacon 추상 불성립",
    65: "치약 대장간 결합은 Forge 추상 불성립",
    66: "카약 신호 결합은 Signal 추상 불성립",
    67: "바리스타 경로 결합은 Path 불성립",
    68: "구강청격 지점 결합은 Point 불성립",
    69: "폭포 기지 결합은 Base 추상 불성립",
    70: "펍 실험실 결합은 Lab 불성립",
    71: "마우스가드 거점 결합은 Station 불성립",
    72: "선셋 센터 결합은 Center 불성립",
    73: "스테이크하우스 저울 결합은 Scale 다의어 불성립",
    74: "스마일 항로 결합은 Route 불성립",
    76: "스시 지도집 결합은 Atlas 추상 불성립",
    77: "구채 관리인 결합은 Keeper 불명확",
    78: "복도 엔진 결합은 Engine 추상 불성립",
    79: "타코 동반자 결합은 Companion 불명확",
    80: "코골이 등록 결합 불명확",
    83: "교합 탐색기 결합은 Locator 불명확",
    85: "해산물 만 결합은 Bay 불성립",
    86: "치과 게시 결합은 Post 다의어 불성립",
    87: "배낭여행 명부 결합 불성립",
    88: "교정의 여권 결합은 Passport 불성립",
    89: "패러세일링 전광판 결합은 Ticker 불성립",
    91: "야생동물 형식 결합은 Form 다의어 불명확",
    96: "불소 요율 속성 결합은 Rate 불성립",
    97: "화산 피드 결합은 Feed 추상 불성립",
    99: "당일치기 색인 결합은 Index 다의어 불성립",
    100: "치은염 주문 결합은 Order 다의어 불성립",
    102: "이갈이 표 결합은 Table 다의어 불성립",
    103: "산책로 표본 결합은 Sample 다의어 불성립",
    105: "우릴 전표 결합은 Stub 다의어 불성립",
    106: "치주염 한도 결합은 Quota 속성어 불성립",
    107: "사막 회람 결합은 Bulletin 다의어 불성립",
    108: "부정교합 회람 결합은 Circular 다의어 불성립",
    109: "와이너리 청원 결합은 Petition 불성립",
    110: "치수과 정리 결합은 Recap 다의어 불성립",
    111: "치주과 항목 결합은 Item 다의어 불성립",
    115: "교대 의견 결합 불성립",
    118: "용어 선물 결합 불성립 - Gift",
    119: "창고 리트리트 결합 불성립",
    122: "체크아웃 교육 결합 불명확",
    125: "로그북 의견 결합 불성립",
    126: "폐사 추천 결합 불성립",
    128: "키패드 선물 결합 불성립 - Gift",
    129: "이중언어 리트리트 결합 불성립",
    130: "마일리지 토너먼트 결합 불성립",
    132: "카페 상태 속성 결합은 Condition 불성립",
    139: "논문 선물 결합 불성립 - Gift",
    140: "회의 리트리트 결합 불성립",
    141: "헤드라인 토너먼트 결합 불성립",
    142: "우선순위 전단 결합 불성립",
    143: "다이너 책상 결합은 Desk 불성립",
    144: "비스트로 패널 결합은 Panel 불성립",
    145: "피자집 게시 결합은 Post 다의어 불성립",
    146: "데리 요약 결합 불성립",
    147: "디저트 항목 결합은 Entry 다의어 불성립",
    148: "포장 분류 속성 결합은 Category 불성립",
    149: "브런치 도식 결합은 Diagram 불성립",
    150: "베이커리 무대 결합은 Stage 불성립",
    151: "페이스트리 계좌 결합은 Account 다의어 불명확",
    152: "베이글 시뮬레이터 결합 불성립",
    153: "도넛 깊이 속성 결합은 Depth 불성립",
    154: "에스프레소 행렬 결합은 Matrix 불성립",
    158: "피부양자 의견 결합 불성립",
    160: "철회 세미나 결합은 Withdrawal 다의어 불성립",
    162: "행동 리트리트 결합 불성립",
    163: "칫솔 토너먼트 결합 불성립",
    165: "스노클링 흐름 결합은 Flow 추상 불성립",
    166: "칵테일 대장간 결합은 Forge 추상 불성립",
    167: "치약 폭포 결합은 Cascade 추상 불성립",
    168: "카약 시계 결합은 Watch 다의어 불성립",
    169: "바리스타 지점 결합은 Point 불성립",
    170: "구강청격 지도 결합은 Map 불성립",
    171: "폭포 핵심 결합은 Core 추상 불성립",
    172: "펍 거점 결합은 Station 불성립",
    173: "마우스가드 터미널 결합은 Terminal 불성립",
    174: "선셋 존 결합은 Zone 불성립",
    175: "스테이크하우스 항로 결합은 Route 불성립",
    176: "스마일 레일 결합은 Rail 다의어 불성립",
    177: "수변 사슬 결합은 Chain 다의어 불성립",
    178: "스시 관리인 결합은 Keeper 불명확",
    179: "구채 관리자 결합은 Manager 불명확",
    180: "복도 조수 결합은 Assistant 불명확",
    181: "타코 등록 결합 불성립",
    182: "코골이 운영 결합은 Ops 불성립",
    184: "면집 탐색기 결합은 Locator 불명확",
    185: "교합 검색기 결합은 Finder 불명확",
    186: "전망 계수기 결합은 Counter 다의어 불성립",
    187: "해산물 게시 결합은 Post 다의어 불성립",
    188: "치과 항구 결합은 Harbor 불성립",
    190: "교정의 로비 결합은 Lobby 불성립",
    191: "패러세일링 줄 결합은 Line 다의어 불성립",
    193: "야생동물 카드 결합은 Card 다의어 불성립",
    194: "치실 점수 결합 불성립",
    195: "라군 태그 결합 불성립",
    196: "치석 뷰 결합은 View 추상 불성립",
    197: "빙하 서류 결합은 File 다의어 불명확",
    199: "화산 초안 결합은 Draft 다의어 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 68, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 132, len(REJECT_REASON)
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
