import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk1_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk1_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    8: (0.6, "광산 교대근무 실무 교육 콘텐츠로 성립 (Tutorial 라인)"),
    9: (0.6, "필터 관리 핸드북으로 실재 (Handbook 라인)"),
    12: (0.6, "보관업체 추천 서비스로 실재 (Recommendation 라인)"),
    13: (0.6, "사진 전시 세미나로 실재 (Seminar 라인)"),
    14: (0.6, "꽃배달 선물 서비스로 성립 (Gift 라인)"),
    17: (0.6, "코팅 서비스 홍보 전단으로 실재 (Flyer 라인)"),
    18: (0.6, "비행 일지 작성 교육으로 실재 (Tutorial 라인)"),
    19: (0.6, "폐사 처리 핸드북으로 실재 (Handbook 라인)"),
    29: (0.6, "보험 잔존물 처리 실무 교육으로 성립 (Tutorial 라인)"),
    30: (0.6, "연금 핸드북으로 실재 (Handbook 라인)"),
    31: (0.6, "사이딩 시공 일정표로 성립 (Timetable 라인)"),
    32: (0.6, "논문 심사 의견서로 성립 (Opinion 라인)"),
    34: (0.6, "헤드라인 작성 세미나로 실재 (Seminar 라인)"),
    38: (0.6, "차량 검사 안내 전단으로 실재 (Flyer 라인)"),
    39: (0.6, "식당 방문·식단 추적 도구로 성립 (Tracker 라인)"),
    41: (0.6, "축제 피자 부스 운영으로 실재 (Booth 공간)"),
    46: (0.6, "제빵 워크숍으로 실재 (Workshop 라인)"),
    47: (0.6, "페이스트리 평점 서비스로 성립 (Rating 라인)"),
    51: (0.6, "피부양자 등록 실무 교육으로 성립 (Tutorial 라인)"),
    52: (0.6, "캐비닛 시공 핸드북으로 실재 (Handbook 라인)"),
    54: (0.6, "커피 평론 콘텐츠로 성립 (Opinion 라인)"),
    55: (0.6, "반려동물 행동 관리 추천으로 성립 (Recommendation 라인)"),
    56: (0.6, "구강관리 교육 세미나로 실재 (Seminar 라인)"),
    59: (0.6, "스노클링 대회 개최로 성립 (Tournament 라인)"),
    66: (0.6, "폭포 위치 지도로 실재 (Map 라인)"),
    77: (0.6, "코골이 모니터링 기기·앱으로 실재 (Monitor 라인)"),
    79: (0.6, "면요리집 등록 목록으로 성립 (Registry 라인)"),
    80: (0.6, "교정 착용 일정 캘린더로 성립 (Calendar 라인)"),
    85: (0.6, "교정 진단 차트로 성립 (Chart 라인)"),
    88: (0.6, "야생동물 관찰 보고서로 실재 (Report 라인)"),
    92: (0.6, "빙하 상태 정보로 실재 (Status 라인)"),
    96: (0.6, "당일치기 일정 타임라인으로 실재 (Timeline 라인)"),
    102: (0.6, "우림 투어 바우처로 실재 (Voucher 라인)"),
    109: (0.6, "항공 연료 계산 교육으로 실재 (Tutorial 라인)"),
    110: (0.6, "교대근무 핸드북으로 실재 (Handbook 라인)"),
    111: (0.6, "필터 교체 일정표로 성립 (Timetable 라인)"),
    119: (0.6, "항만 운영 교육 콘텐츠로 실재 (Tutorial 라인)"),
    120: (0.6, "로그북 실무 핸드북으로 실재 (Handbook 라인)"),
    123: (0.6, "스마트락 키패드 추천 서비스로 실재 (Recommendation 라인)"),
    124: (0.6, "이중언어 교육 세미나로 실재 (Seminar 라인)"),
    130: (0.6, "계약 변경 실무 교육으로 성립 (Tutorial 라인)"),
    131: (0.6, "손해 처리 핸드북으로 실재 (Handbook 라인)"),
    132: (0.6, "연금 납부·수령 일정표로 성립 (Timetable 라인)"),
    135: (0.6, "회의 실무 세미나로 성립 (Seminar 라인)"),
    139: (0.6, "이벤트 굿즈 홍보 전단으로 성립 (Flyer 라인)"),
    144: (0.6, "디저트 주문 확정 통지로 성립 (Confirmation 라인)"),
    146: (0.6, "브런치 운영 매뉴얼로 성립 (Manual 라인)"),
    149: (0.6, "베이글 가게 결제 처리로 성립 (Payment 라인)"),
    152: (0.6, "보험 소송 절차 교육으로 성립 (Tutorial 라인)"),
    153: (0.6, "피부양자 등록 실무 안내로 성립 (Handbook 라인)"),
    154: (0.6, "캐비닛 시공 일정표로 성립 (Timetable 라인)"),
    156: (0.6, "커피 추천 서비스로 실재 (Recommendation 라인)"),
    157: (0.6, "행동 교정 세미나로 실재 (Seminar 라인)"),
    158: (0.6, "칫솔 선물 세트로 성립 (Gift 라인)"),
    161: (0.6, "스노클링 투어 전단으로 실재 (Flyer 라인)"),
    180: (0.6, "면요리 행사 캘린더로 성립 (Calendar 라인)"),
    189: (0.6, "야생동물 관찰 로그로 실재 (Log 라인)"),
    195: (0.6, "화산 활동 갱신 정보로 실재 (Update 라인)"),
    196: (0.6, "실런트 시술 요약으로 성립 (Summary 라인)"),
    197: (0.6, "당일치기 일정 알림으로 성립 (Reminder 라인)"),
    198: (0.6, "치은염 치료 견적으로 실재 (Estimate 라인)"),
    199: (0.6, "요트 렌탈 청구서로 성립 (Bill 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "우림 통행권 결합은 Pass 다의어 불명확",
    2: "치주염 전표 결합은 Stub 다의어 불성립",
    3: "사막 메모 결합 불성립",
    4: "부정교합 탭 결합은 Tab 다의어 불성립",
    5: "와이너리 요약 결합은 Brief 다의어 불성립",
    6: "치수과 권고 결합은 Advisory 불성립",
    7: "치주과 정리 결합은 Recap 다의어 불성립",
    10: "마스터키 시간표 결합 불성립",
    11: "용어 의견 결합 불성립",
    15: "갱신 리트리트 결합 불성립",
    16: "라이너 토너먼트 결합 불성립",
    20: "코일 시간표 결합 불성립",
    21: "키패드 의견 결합 불성립",
    22: "이중언어 추천 결합 불성립",
    23: "마일리지 세미나 결합 불성립",
    24: "보정 선물 결합 불성립 - Gift",
    25: "축사 리트리트 결합 불성립",
    26: "보증금 토너먼트 결합 불성립",
    27: "탁도 전단 결합 불성립",
    28: "카페 호환성 결합은 Compatibility 속성어 불성립",
    33: "회의 추천 결합 불성립",
    35: "우선순위 선물 결합 불성립 - Gift",
    36: "헤드헌터 리트리트 결합 불성립",
    37: "스웨그 토너먼트 결합 불성립",
    40: "비스트로 존 결합은 Zone 불성립",
    42: "데리 업데이트 결합 불성립",
    43: "디저트 청원 결합은 Petition 불성립",
    44: "포장 규칙 결합은 Rule 불성립",
    45: "브런치 라벨 결합은 Label 다의어 불명확",
    48: "베이글 개정 결합은 Revision 다의어 불성립",
    49: "도넛 시계 결합은 Clock 다의어 불성립",
    50: "에스프레소 수신 결합은 Reception 다의어 불성립",
    53: "철회 시간표 결합은 Withdrawal 다의어 불명확",
    57: "보모 선물 결합 불성립 - Gift",
    58: "보도 리트리트 결합 불성립",
    60: "메트로놈 전단 결합 불성립",
    61: "칵테일 금고 결합은 Vault 추상 불성립",
    62: "치약 나침반 결합은 Compass 추상 불성립",
    63: "카약 폭포 결합은 Cascade 추상 불성립",
    64: "바리스타 격자 결합은 Grid 추상 불성립",
    65: "구강청격 파도 결합은 Wave 추상 불성립",
    67: "펍 갑판 결합은 Deck 불성립",
    68: "마우스가드 스튜디오 결합 불명확",
    69: "선셋 거점 결합은 Station 불성립",
    70: "스테이크하우스 콘솔 결합은 Console 불성립",
    71: "스마일 패널 결합은 Panel 불성립",
    72: "수변 항로 결합은 Route 불명확",
    73: "스시 관문 결합은 Gate 불성립",
    74: "구채 연결점 결합은 Nexus 추상 불성립",
    75: "복도 관리인 결합은 Keeper 불명확",
    76: "타코 일정 결합 불성립",
    78: "해변 등록 결합 불명확",
    81: "전망 탐색기 결합은 Locator 불명확",
    82: "해산물 키오스크 결합은 Kiosk 불성립",
    83: "치과 키오스크 결합은 Kiosk 불성립",
    84: "배낭여행 게시 결합은 Post 다의어 불성립",
    86: "패러세일링 여권 결합은 Passport 불성립",
    87: "치위 창 결합은 Window 다의어 불성립",
    89: "치실 카드 결합은 Card 다의어 불성립",
    90: "라군 점검 결합 불명확",
    91: "치석 태그 결합 불성립",
    93: "불소 서류 결합은 File 다의어 불명확",
    94: "화산 요율 속성 결합은 Rate 불성립",
    95: "실런트 초안 결합은 Draft 다의어 불성립",
    97: "치은염 티켓 결합 불성립",
    98: "요트 주문 결합은 Order 다의어 불성립",
    99: "이갈이 코드 결합 불성립",
    100: "산책로 표 결합은 Table 다의어 불성립",
    101: "구취 슬롯 결합은 Slot 다의어 불성립",
    103: "치주염 정산 결합은 Statement 불성립",
    104: "사막 한도 결합은 Quota 속성어 불성립",
    105: "부정교합 회람 결합은 Bulletin 다의어 불성립",
    106: "와이너리 회람 결합은 Circular 다의어 불성립",
    107: "치수과 청원 결합은 Petition 불성립",
    108: "치주과 항목 결합은 Entry 다의어 불성립",
    112: "마스터키 의견 결합 불성립",
    113: "용어 추천 결합 불성립",
    114: "창고 세미나 결합 불성립",
    115: "갤러리 선물 결합 불명확",
    116: "플로리스트 리트리트 결합 불성립",
    117: "갱신 토너먼트 결합 불성립",
    118: "라이너 전단 결합 불성립",
    121: "폐사 시간표 결합 불성립",
    122: "코일 의견 결합 불성립",
    125: "마일리지 선물 결합 불성립 - Gift",
    126: "보정 리트리트 결합 불성립",
    127: "축사 토너먼트 결합 불성립",
    128: "보증금 전단 결합 불성립",
    129: "카페 수용력 결합은 Capacity 불성립",
    133: "사이딩 의견 결합 불성립",
    134: "논문 추천 결합 불성립",
    136: "헤드라인 선물 결합 불성립 - Gift",
    137: "우선순위 리트리트 결합 불성립",
    138: "헤드헌터 토너먼트 결합 불성립",
    140: "다이너 흐름 결합은 Flow 추상 불성립",
    141: "비스트로 포털 결합은 Portal 불명확",
    142: "피자집 키오스크 결합은 Kiosk 불성립",
    143: "데리 피드 결합은 Feed 추상 불성립",
    145: "포장 세부 결합은 Detail 속성어 불성립",
    147: "베이커리 감시자 결합은 Guardian 불명확",
    148: "페이스트리 계약 결합은 Agreement 불성립",
    150: "도넛 시간 속성 결합은 Time 불성립",
    151: "에스프레소 후속 결합은 Followup 불성립",
    155: "철회 의견 결합은 Withdrawal 다의어 불성립",
    159: "보모 리트리트 결합 불성립",
    160: "보도 토너먼트 결합 불성립",
    162: "칵테일 나침반 결합은 Compass 추상 불성립",
    163: "치약 등대 결합은 Beacon 추상 불성립",
    164: "카약 다리 결합은 Bridge 다의어 불성립",
    165: "바리스타 파도 결합은 Wave 추상 불성립",
    166: "구강청격 경로 결합은 Path 불성립",
    167: "폭포 틀 결합은 Frame 추상 불성립",
    168: "펍 스튜디오 결합 불명확",
    169: "마우스가드 실험실 결합은 Lab 불성립",
    170: "선셋 터미널 결합은 Terminal 불성립",
    171: "스테이크하우스 패널 결합은 Panel 불성립",
    172: "스마일 저울 결합은 Scale 다의어 불성립",
    173: "수변 레일 결합은 Rail 다의어 불성립",
    174: "스시 연결점 결합은 Nexus 추상 불성립",
    175: "구채 지도집 결합은 Atlas 추상 불성립",
    176: "복도 관리자 결합은 Manager 불명확",
    177: "타코 감시 결합 불성립",
    178: "코골이 동반자 결합은 Companion 불명확",
    179: "해변 운영 결합은 Ops 불성립",
    181: "교합 디렉터리 결합 불성립",
    182: "전망 검색기 결합은 Finder 불명확",
    183: "해산물 키오스크 결합은 Kiosk 불성립",
    184: "치과 만 결합은 Bay 불성립",
    185: "배낭여행 항구 결합은 Harbor 불성립",
    186: "교정의 상자 결합은 Bin 불성립",
    187: "패러세일링 로비 결합은 Lobby 불성립",
    188: "치위 명부 결합은 Roll 불성립",
    190: "치실 시트 결합은 Sheet 다의어 불성립",
    191: "라군 점수 결합은 Score 불성립",
    192: "치석 프로필 결합 불성립",
    193: "빙하 뷰 결합은 View 추상 불성립",
    194: "불소 수준 속성 결합은 Level 불성립",
    200: "이갈이 목록 결합 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 62, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 138, len(REJECT_REASON)
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
