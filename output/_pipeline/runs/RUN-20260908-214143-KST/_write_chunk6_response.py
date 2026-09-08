import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk5_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk5_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "패러세일링 운항 기록으로 실재 (Log 라인)"),
    4: (0.6, "치위 검진 서비스로 성립 (Check 라인)"),
    5: (0.6, "야생동물 관찰 노트로 실재 (Note 라인)"),
    7: (0.6, "관광지 라군 역사 안내로 성립 (History 라인)"),
    10: (0.6, "불소 도포 일정 타임라인으로 성립 (Timeline 라인)"),
    13: (0.6, "당일여행 영수증으로 성립 (Receipt 라인)"),
    16: (0.6, "나이트가드 시술 바우처로 성립 (Voucher 라인)"),
    21: (0.6, "사막 투어 예약 확정으로 성립 (Confirmation 라인)"),
    24: (0.6, "신경치료 계획서로 성립 (Plan 라인)"),
    26: (0.6, "유지보수 실무 튜토리얼로 실재 (Tutorial 라인)"),
    27: (0.6, "검수 핸드북으로 실재 (Handbook 라인)"),
    31: (0.6, "조제 실무 세미나로 실재 (Seminar 라인)"),
    35: (0.6, "필터 홍보 전단으로 실재 (Flyer 라인)"),
    36: (0.6, "방제 일정 실무 튜토리얼로 실재 (Tutorial 라인)"),
    37: (0.6, "제설 핸드북으로 실재 (Handbook 라인)"),
    45: (0.6, "광미 처리 서비스 전단으로 성립 (Flyer 라인)"),
    47: (0.6, "세차 실무 튜토리얼로 실재 (Tutorial 라인)"),
    48: (0.6, "배수 트랩 핸드북으로 실재 (Handbook 라인)"),
    49: (0.6, "로드트립 일정표로 실재 (Timetable 라인)"),
    51: (0.6, "알레르기 관리 권고 콘텐츠로 성립 (Recommendation 라인)"),
    52: (0.6, "송금 실무 세미나로 실재 (Seminar 라인)"),
    56: (0.6, "연금 서비스 홍보 전단으로 실재 (Flyer 라인)"),
    60: (0.6, "케이터링 견적으로 성립 (Estimate 라인)"),
    64: (0.6, "베이커리 비교 콘텐츠로 성립 (Comparison 라인)"),
    66: (0.6, "베이글 제조 영상으로 실재 (Video 라인)"),
    69: (0.6, "커브 어필 실무 교육으로 실재 (Tutorial 라인)"),
    70: (0.6, "포도원 핸드북으로 실재 (Handbook 라인)"),
    71: (0.6, "반주 연습 일정표로 실재 (Timetable 라인)"),
    72: (0.6, "질병 진료 소견으로 성립 (Opinion 라인)"),
    74: (0.6, "플랫베드 실무 세미나로 성립 (Seminar 라인)"),
    78: (0.6, "캐비닛 홍보 전단으로 실재 (Flyer 라인)"),
    84: (0.6, "카약 코스로 실재 (Path 물리 코스)"),
    90: (0.6, "선셋 투어 코스로 실재 (Route 물리 코스)"),
    95: (0.6, "호흡 모니터로 실재 (Monitor 라인)"),
    97: (0.6, "타코 이벤트 캘린더로 성립 (Calendar 라인)"),
    106: (0.6, "교정 경과 보고서로 실재 (Report 라인)"),
    114: (0.6, "불소 도포 알림으로 성립 (Reminder 라인)"),
    115: (0.6, "화산 투어 입장권으로 실재 (Ticket 라인)"),
    116: (0.6, "실런트 시술 청구서로 성립 (Bill 라인)"),
    130: (0.6, "방제 약제 실무 튜토리얼로 실재 (Tutorial 라인)"),
    131: (0.6, "유지보수 핸드북으로 실재 (Handbook 라인)"),
    132: (0.6, "정기 검사 일정표로 성립 (Timetable 라인)"),
    134: (0.6, "장지 추천 서비스로 성립 (Recommendation 라인)"),
    139: (0.6, "근무 교대 공지 전단으로 성립 (Flyer 라인)"),
    140: (0.6, "시니어 웰니스 교육으로 실재 (Tutorial 라인)"),
    141: (0.6, "방제 일정 핸드북으로 실재 (Handbook 라인)"),
    142: (0.6, "제설 일정표로 실재 (Timetable 라인)"),
    145: (0.6, "사전 장례 설명회로 성립 (Seminar 라인)"),
    151: (0.6, "수영장 동계 마감 교육으로 실재 (Tutorial 라인)"),
    152: (0.6, "세차 핸드북으로 실재 (Handbook 라인)"),
    155: (0.6, "악기 추천 콘텐츠로 성립 (Recommendation 라인)"),
    156: (0.6, "알레르기 세미나로 실재 (Seminar 라인)"),
    167: (0.6, "브런치 예약 알림으로 성립 (Notification 라인)"),
    170: (0.6, "제빵 기록 저널로 성립 (Diary 라인)"),
    173: (0.6, "커브 어필 핸드북으로 실재 (Handbook 라인)"),
    174: (0.6, "와이너리 투어 시간표로 실재 (Timetable 라인)"),
    176: (0.6, "질병 관리 권고 콘텐츠로 성립 (Recommendation 라인)"),
    177: (0.6, "채무 관리 세미나로 성립 (Seminar 라인)"),
    181: (0.6, "피부양자 안내 전단으로 성립 (Flyer 라인)"),
    200: (0.6, "타코집 디렉터리로 성립 (Directory 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "배낭여행 로비 결합은 Lobby 불성립",
    2: "교정의 순서 결합은 Roll 다의어 불성립",
    6: "치실 상태 결합은 Status 불성립",
    8: "치석 요율 속성 결합은 Rate 불성립",
    9: "빙하 피드 결합은 Feed 추상 불성립",
    11: "화산 색인 결합은 Index 다의어 불성립",
    12: "실런트 주문 결합은 Order 다의어 불성립",
    14: "치은염 표 결합은 Table 다의어 불성립",
    15: "요트 샘플 결합은 Sample 다의어 불성립",
    17: "산책로 전표 결합은 Stub 불성립",
    18: "구취 한도 결합은 Quota 속성어 불성립",
    19: "우릴 회람 결합은 Bulletin 다의어 불성립",
    20: "치주염 권고 결합은 Advisory 불성립",
    22: "부정교합 항목 결합은 Entry 다의어 불성립",
    23: "와이너리 항목 결합은 Item 다의어 불성립",
    25: "치주과 요금 결합은 Fare 다의어 불성립",
    28: "가격 일정표 결합 불성립",
    29: "묘지 의견 결합 불성립",
    30: "수수료 추천 결합 불명확",
    32: "전세 선물 결합 불성립 - Gift",
    33: "연료 리트리트 결합 불성립",
    34: "교대 토너먼트 결합 불성립",
    38: "재고 일정표 결합 불성립",
    39: "수선 의견 결합 불명확",
    40: "추모 추천 결합 불성립",
    41: "체크아웃 세미나 결합 불명확",
    42: "리콜 선물 결합 불성립 - Gift",
    43: "항만 리트리트 결합 불성립",
    44: "로그북 토너먼트 결합 불성립",
    46: "카페 센서 결합은 Sensor 불성립",
    50: "아코디언 평론 결합 불명확",
    53: "섀시 선물 결합 불성립 - Gift",
    54: "계약 변경 리트리트 결합 불성립",
    55: "잔존물 토너먼트 결합 불성립",
    57: "다이너 등대 결합은 Beacon 추상 불성립",
    58: "비스트로 사슬 결합은 Chain 다의어 불성립",
    59: "피자집 상자 결합은 Bin 불성립",
    61: "디저트 비용 속성 결합은 Cost 불성립",
    62: "포장 토큰 결합은 Token 불성립",
    63: "브런치 렌더링 결합은 Rendering 불성립",
    65: "페이스트리 핑 결합은 Ping 추상 불성립",
    67: "도넛 하중 결합은 Load 불성립",
    68: "에스프레소 요구사항 결합 불성립",
    73: "채무자 추천 결합 불명확",
    75: "동네 선물 결합 불성립 - Gift",
    76: "소송 리트리트 결합 불성립",
    77: "피부양자 토너먼트 결합 불성립",
    79: "라떼 흐름 결합은 Flow 추상 불성립",
    80: "칫솔 책상 결합은 Desk 불성립",
    81: "스노클링 금고 결합은 Vault 추상 불성립",
    82: "칵테일 스코프 결합은 Scope 불성립",
    83: "치약 루프 결합은 Loop 추상 불성립",
    85: "바리스타 장부 결합은 Ledger 불성립",
    86: "구강청격 게시판 결합은 Board 다의어 불성립",
    87: "폭포 실험실 결합은 Lab 불성립",
    88: "펍 콘솔 결합은 Console 불성립",
    89: "마우스가드 패널 결합은 Panel 불성립",
    91: "스테이크하우스 관문 결합은 Gate 불성립",
    92: "스마일 연결점 결합은 Nexus 추상 불성립",
    93: "수변 관리인 결합은 Keeper 불명확",
    94: "스시 스케줄러 결합 불성립",
    96: "보드워크 등록부 결합 불성립",
    98: "코골이 디렉터리 결합 불명확",
    99: "해변 탐색기 결합은 Finder 불명확",
    100: "면집 키오스크 결합은 Kiosk 불성립",
    101: "교합 만 결합은 Bay 불성립",
    102: "전망 항구 결합은 Harbor 불성립",
    103: "해산물 상자 결합은 Bin 불성립",
    104: "치과 여권 결합은 Passport 불성립",
    105: "배낭여행 전광판 결합은 Ticker 불성립",
    107: "패러세일링 서식 결합은 Form 다의어 불성립",
    108: "치위 점수 결합은 Score 불성립",
    109: "야생동물 꼬리표 결합은 Tag 다의어 불성립",
    110: "치실 뷰 결합은 View 추상 불성립",
    111: "라군 서류 결합은 File 다의어 불성립",
    112: "치석 갱신 결합 불성립",
    113: "빙하 초안 결합은 Draft 다의어 불성립",
    117: "당일여행 코드 결합은 Code 불성립",
    118: "치은염 전표 결합은 Slip 다의어 불성립",
    119: "요트 슬롯 결합은 Slot 다의어 불성립",
    120: "이갈이 배지 결합 불성립",
    121: "산책로 정산 결합은 Statement 불성립",
    122: "구취 탭 결합은 Tab 다의어 불성립",
    123: "우릴 요약 결합은 Brief 다의어 불성립",
    124: "치주염 청원 결합은 Petition 불성립",
    125: "사막 정리 결합은 Recap 다의어 불성립",
    126: "부정교합 요금 결합은 Fee 불성립",
    127: "와이너리 단위 결합은 Unit 다의어 불성립",
    128: "치수과 비용 속성 결합은 Cost 불성립",
    129: "치주과 세금 결합은 Tax 불성립",
    133: "가격 의견 결합 불명확",
    135: "수수료 세미나 결합 불명확",
    136: "조제 선물 결합 불성립 - Gift",
    137: "전세 리트리트 결합 불성립",
    138: "연료 토너먼트 결합 불성립",
    143: "재고 의견 결합 불명확",
    144: "수선 추천 결합 불명확",
    146: "체크아웃 선물 결합 불성립 - Gift",
    147: "리콜 리트리트 결합 불성립",
    148: "항만 토너먼트 결합 불성립",
    149: "로그북 전단 결합 불명확",
    150: "카페 접수처 결합은 Reception 다의어 불성립",
    153: "배수 일정표 결합 불성립",
    154: "로드트립 평론 결합 불명확",
    157: "송금 선물 결합 불성립 - Gift",
    158: "섀시 리트리트 결합 불성립",
    159: "계약 변경 토너먼트 결합 불성립",
    160: "잔존물 전단 결합 불명확",
    161: "다이너 대장간 결합은 Forge 추상 불성립",
    162: "비스트로 링 결합은 Ring 불성립",
    163: "피자집 여권 결합은 Passport 불성립",
    164: "데리 주문 결합은 Order 다의어 불성립",
    165: "디저트 가격 속성 결합은 Price 불성립",
    166: "포장 서명 결합은 Signature 다의어 불성립",
    168: "베이커리 제안 결합은 Proposal 불명확",
    169: "페이스트리 모형 결합은 Model 다의어 불성립",
    171: "도넛 전압 속성 결합은 Voltage 불성립",
    172: "에스프레소 감가상각 결합 불성립",
    175: "반주 의견 결합 불명확",
    178: "플랫베드 선물 결합 불성립 - Gift",
    179: "동네 리트리트 결합 불성립",
    180: "소송 토너먼트 결합 불성립",
    182: "라떼 허브 결합은 Hub 불성립",
    183: "칫솔 레이더 결합은 Radar 추상 불성립",
    184: "스노클링 나침반 결합은 Compass 추상 불성립",
    185: "칵테일 루프 결합은 Loop 추상 불성립",
    186: "치약 격자 결합은 Grid 추상 불성립",
    187: "카약 지점 결합은 Point 불성립",
    188: "바리스타 게시판 결합은 Board 다의어 불성립",
    189: "구강청격 갑판 결합은 Deck 불성립",
    190: "폭포 역 결합은 Station 다의어 불성립",
    191: "펍 패널 결합은 Panel 불성립",
    192: "마우스가드 저울 결합은 Scale 다의어 불성립",
    193: "선셋 레일 결합은 Rail 다의어 불성립",
    194: "스테이크하우스 연결점 결합은 Nexus 추상 불성립",
    195: "스마일 지도집 결합은 Atlas 추상 불성립",
    196: "수변 관리자 결합은 Manager 불명확",
    197: "스시 모니터 결합 불명확",
    198: "호흡 동반자 결합은 Companion 불명확",
    199: "보드워크 운영 결합은 Ops 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 60, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 140, len(REJECT_REASON)
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
