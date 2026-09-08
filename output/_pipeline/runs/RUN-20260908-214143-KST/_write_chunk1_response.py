import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.7, "장부 관리 결합으로 명확 (카나리아)"),
    2: (0.7, "공증 서비스 결합으로 명확 (카나리아)"),
    8: (0.6, "마스터키 사용법 학습 콘텐츠로 실재 (Tutorial 라인)"),
    9: (0.6, "통역 실무 용어 핸드북으로 실재 (Handbook 라인)"),
    10: (0.6, "보관 입출고 시간표로 성립 (Timetable 라인)"),
    11: (0.6, "사진 갤러리 비평 의견 콘텐츠로 성립 (Opinion 라인)"),
    12: (0.6, "플로리스트 추천 서비스로 실재 (Recommendation 라인)"),
    13: (0.6, "임대차 갱신 안내 세미나로 실재 (Seminar 라인)"),
    17: (0.6, "여행 상품 홍보 전단으로 실재 (Flyer 라인)"),
    18: (0.6, "냉각 코일 관리 학습 콘텐츠로 실재 (Tutorial 라인)"),
    19: (0.6, "도어락 키패드 실무 핸드북으로 실재 (Handbook 라인)"),
    20: (0.6, "이중언어 서비스 시간표로 성립 (Timetable 라인)"),
    22: (0.6, "사진 보정 추천 서비스로 실재 (Recommendation 라인)"),
    23: (0.6, "결혼식 축사 준비 세미나로 실재 (Seminar 라인)"),
    29: (0.6, "사이딩 시공 학습 콘텐츠로 실재 (Tutorial 라인)"),
    30: (0.6, "논문 작성 핸드북으로 실재 (Handbook 라인)"),
    31: (0.6, "의회 회의 일정표로 실재 (Timetable 라인)"),
    32: (0.6, "헤드라인 평론 콘텐츠로 성립 (Opinion 라인)"),
    33: (0.6, "티켓 우선순위 추천 도구로 성립 (Recommendation 라인)"),
    34: (0.6, "헤드헌팅 취업 세미나로 실재 (Seminar 라인)"),
    35: (0.6, "이벤트 굿즈 선물 세트로 성립 (Gift 라인)"),
    38: (0.6, "진드기 예방 안내 전단으로 실재 (Flyer 라인)"),
    46: (0.6, "제과 도안 템플릿으로 실재 (Template 라인)"),
    51: (0.6, "라테 레시피 핸드북으로 실재 (Handbook 라인)"),
    52: (0.6, "반려동물 훈련 일정표로 성립 (Timetable 라인)"),
    53: (0.6, "칫솔 평가 의견 콘텐츠로 실재 (Opinion 라인)"),
    54: (0.6, "보모 추천 서비스로 실재 (Recommendation 라인)"),
    56: (0.6, "스노클링 체험 선물권으로 성립 (Gift 라인)"),
    58: (0.6, "운동 대회 개최 서비스로 실재 (Tournament 라인)"),
    65: (0.6, "폭포 산책로 안내로 실재 서비스 (Path 물리 경로)"),
    66: (0.6, "펍 매출 장부 관리로 실재 (Ledger 라인)"),
    76: (0.6, "코골이 관리 계획 도구로 성립 (Planner 라인)"),
    77: (0.6, "해안 상태 모니터링 서비스로 실재 (Monitor 라인)"),
    78: (0.6, "면류 창업 플레이북으로 성립 (Playbook 라인)"),
    79: (0.6, "교합 기록 일지로 성립 (Journal 라인)"),
    80: (0.6, "전망 이벤트 캘린더로 성립 (Calendar 라인)"),
    84: (0.6, "교정의 당직 명부로 성립 (Roster 라인)"),
    85: (0.6, "패러세일링 항로 차트로 성립 (Chart 라인)"),
    88: (0.6, "치실 사용 기록 로그로 실재 (Log 라인)"),
    90: (0.6, "치석 검진 점수로 성립 (Score 심사 채점)"),
    94: (0.6, "실런트 재도포 갱신 안내로 성립 (Update 라인)"),
    96: (0.6, "치은염 관리 알림으로 성립 (Reminder 라인)"),
    97: (0.6, "요트 투어 승선권 판매로 실재 (Ticket 구체 서비스)"),
    107: (0.6, "치주과 예약 확정 통지로 성립 (Confirmation 라인)"),
    108: (0.6, "필터 관리 학습 콘텐츠로 실재 (Tutorial 라인)"),
    109: (0.6, "마스터키 실무 핸드북으로 실재 (Handbook 라인)"),
    112: (0.6, "사진 갤러리 추천 서비스로 실재 (Recommendation 라인)"),
    113: (0.6, "꽃꽂이 세미나로 실재 (Seminar 라인)"),
    117: (0.6, "변기 수리 서비스 홍보 전단으로 실재 (Flyer 라인)"),
    118: (0.6, "폐사 처리 실무 학습 콘텐츠로 실재 (Tutorial 라인)"),
    119: (0.6, "코일 유지보수 핸드북으로 실재 (Handbook 라인)"),
    123: (0.6, "사진 보정 세미나로 실재 (Seminar 라인)"),
    127: (0.6, "폼 세차 서비스 홍보 전단으로 실재 (Flyer 라인)"),
    129: (0.6, "연금 이해 교육 콘텐츠로 실재 (Tutorial 라인)"),
    130: (0.6, "사이딩 시공 핸드북으로 실재 (Handbook 라인)"),
    131: (0.6, "논문 작성 일정표로 실재 (Timetable 라인)"),
    133: (0.6, "헤드라인 제안 추천으로 성립 (Recommendation 라인)"),
    134: (0.6, "티켓 우선순위 실무 세미나로 성립 (Seminar 라인)"),
    138: (0.6, "다이너 홍보 전단으로 실재 (Flyer 라인)"),
    145: (0.6, "베이킹 타이머 도구로 실재 (Timer 라인)"),
    146: (0.6, "페이스트리 제과 가이드로 실재 (Guide 라인)"),
    150: (0.6, "캐비닛 시공 학습 콘텐츠로 실재 (Tutorial 라인)"),
    153: (0.6, "반려동물 행동 상담 소견으로 성립 (Opinion 라인)"),
    154: (0.6, "칫솔 추천 서비스로 실재 (Recommendation 라인)"),
    155: (0.6, "육아 도우미 교육 세미나로 실재 (Seminar 라인)"),
    157: (0.6, "스노클링 휴양 패키지로 실재 (Retreat 라인)"),
    159: (0.6, "헬스 모집 홍보 전단으로 실재 (Flyer 라인)"),
    176: (0.6, "수면검사 예약 스케줄러로 성립 (Scheduler 라인)"),
    178: (0.6, "면요리 평론 저널로 실재 (Journal 라인)"),
    179: (0.6, "교합 기록 등록부로 성립 (Registry 라인)"),
    180: (0.6, "전망 명소 디렉터리로 실재 (Directory 라인)"),
    184: (0.6, "교정 재방문 알림으로 성립 (Alert 기한형)"),
    190: (0.6, "치석 관찰 기록 노트로 성립 (Note 라인)"),
    192: (0.6, "불소 도포 이력 관리로 성립 (History 라인)"),
    195: (0.6, "당일치기 일정 요약으로 성립 (Summary 라인)"),
    197: (0.6, "요트 렌탈 견적 서비스로 실재 (Estimate 라인)"),
    198: (0.6, "나이트가드 치료 영수증 관리로 성립 (Receipt 라인)"),
    199: (0.6, "산책 코스 목록으로 실재 (List 라인)"),
}

TRADEMARK_REJECT = {
    3: "Slack 협업 도구 상표 (Salesforce)",
    4: "Photoshop 어도비 상표",
}

DUP_REJECT = {}

REJECT_REASON = {
    5: "Thing 무의미 추상 결합 불성립 (카나리아)",
    6: "Sentinel 감시 역할 결합 불성립 (카나리아)",
    7: "Watchman 감시 역할 결합 불성립 (카나리아)",
    14: "풀 라이너 선물 결합 불성립 - Gift",
    15: "코팅 리트리트 결합 불성립 - Retreat",
    16: "변기 토너먼트 결합 불성립",
    21: "마일리지 의견 결합 불성립 - Opinion",
    24: "보증금 선물 결합 불성립 - Gift",
    25: "탁도 리트리트 결합 불성립",
    26: "폼 토너먼트 결합 불성립",
    27: "워셔 부품 전단 결합 불명확",
    28: "카페 밝기 속성 결합은 Brightness 불성립",
    36: "차량 검사 리트리트 결합 불성립",
    37: "다이너 토너먼트 결합 불성립",
    39: "비스트로 터미널 결합은 Terminal 불성립",
    40: "피자집 사무실 결합 불성립",
    41: "데리 수준 속성 결합은 Level 불성립",
    42: "디저트 회람 전단 결합은 Circular 다의어 불명확",
    43: "테이크아웃 버전 결합은 Version 속성어 불성립",
    44: "브런치 체험 결합은 Trial 다의어 불명확",
    45: "베이커리 탐지기 결합은 Detector 불성립",
    47: "베이글 후보 지명 결합은 Nomination 불성립",
    48: "도넛 한도 속성 결합은 Limit 불성립",
    49: "에스프레소 고장 결합은 Breakdown 다의어 불성립",
    50: "중도 철회 학습 결합은 Withdrawal 다의어 불명확",
    55: "보도 세미나 결합 불성립",
    57: "메트로놈 리트리트 결합 불성립",
    59: "수취인 전단 결합 불성립",
    60: "칵테일 나침반 결합은 Radar 추상 불성립",
    61: "치약 릴레이 결합은 Relay 불성립",
    62: "카약 등대 결합은 Beacon 추상 불성립",
    63: "바리스타 스코프 결합은 Scope 불성립",
    64: "구강청결 루프 결합은 Loop 추상 불성립",
    67: "마우스가드 보드 결합은 Board 다의어 불성립",
    68: "선셋 스튜디오 결합 불명확",
    69: "스테이크하우스 존 결합은 Zone 불성립",
    70: "스마일 포털 결합은 Portal 불명확",
    71: "수변 패널 결합은 Panel 불성립",
    72: "스시 사슬 오독 결합은 Chain 불명확",
    73: "구채 링 결합은 Ring 불성립",
    74: "복도 연결점 결합은 Nexus 추상 불성립",
    75: "타코 조수 결합은 Assistant 불명확",
    81: "해산물 사무실 결합 불성립",
    82: "치과 계수기 오독 결합은 Counter 다의어 불명확",
    83: "배낭여행 키오스크 결합은 Kiosk 불성립",
    86: "치위 전광판 결합은 Ticker 불성립",
    87: "야생동물 창 결합은 Window 다의어 불성립",
    89: "라군 카드 결합은 Card 다의어 불성립",
    91: "빙하 태깅 결합 불성립",
    92: "불소 뷰 결합은 View 추상 불성립",
    93: "화산 서류 결합은 File 다의어 불명확",
    95: "당일치기 초안 결합은 Draft 다의어 불명확",
    98: "이갈이 청구서 결합 불성립",
    99: "산책로 코드 결합 불성립",
    100: "구취 전표 결합은 Slip 다의어 불성립",
    101: "우림 슬롯 결합은 Slot 다의어 불성립",
    102: "치주염 배지 결합 불성립",
    103: "사막 정산 명세 결합은 Statement 불성립",
    104: "부정교합 한도 결합은 Quota 속성어 불성립",
    105: "와이너리 회람 결합은 Bulletin 다의어 불성립",
    106: "치수과 회람 결합은 Circular 다의어 불성립",
    110: "용어 시간표 결합 불성립",
    111: "창고 의견 결합 불성립",
    114: "갱신 선물 결합 불성립 - Gift",
    115: "라이너 리트리트 결합 불성립",
    116: "코팅 토너먼트 결합 불성립",
    120: "키패드 시간표 결합 불성립",
    121: "이중언어 의견 결합 불성립",
    122: "마일리지 추천 결합 불성립",
    124: "축사 선물 결합 불성립 - Gift",
    125: "보증금 리트리트 결합 불성립",
    126: "탁도 토너먼트 결합 불성립",
    128: "카페 이용 빈도 결합은 Frequency 속성어 불성립",
    132: "회의 의견 결합 불성립",
    135: "헤드헌터 선물 결합 불성립 - Gift",
    136: "스웨그 리트리트 결합 불성립",
    137: "차량 검사 토너먼트 결합 불성립",
    139: "비스트로 센터 결합은 Center 불성립",
    140: "피자집 카운터 결합은 Counter 다의어 불성립",
    141: "데리 요율 속성 결합은 Rate 불성립",
    142: "디저트 권고 결합은 Advisory 불성립",
    143: "테이크아웃 링크 결합은 Link 추상 불성립",
    144: "브런치 그래프 결합은 Graph 불성립",
    147: "베이글 교정 결합 불성립",
    148: "도넛 종류 분류 결합은 Type 속성어 불성립",
    149: "에스프레소 센서 결합은 Sensor 불성립",
    151: "철회 핸드북 결합은 Withdrawal 다의어 불명확",
    152: "라테 시간표 결합 불성립",
    156: "보도 선물 결합 불성립 - Gift",
    158: "메트로놈 토너먼트 결합 불성립",
    160: "칵테일 릴레이 결합은 Relay 불성립",
    161: "치약 금고 결합은 Vault 추상 불성립",
    162: "카약 대장간 결합은 Forge 추상 불성립",
    163: "바리스타 루프 결합은 Loop 추상 불성립",
    164: "구강청격 격자 결합은 Grid 추상 불성립",
    165: "폭포 지점 결합은 Point 불성립",
    166: "펍 보드 결합은 Board 다의어 불성립",
    167: "마우스가드 갑판 결합은 Deck 불성립",
    168: "선셋 실험실 결합은 Lab 불성립",
    169: "스테이크하우스 포털 결합은 Portal 불명확",
    170: "스마일 콘솔 결합은 Console 불성립",
    171: "수변 저울 결합은 Scale 다의어 불성립",
    172: "스시 링 결합은 Ring 불성립",
    173: "구채 관문 결합은 Gate 불성립",
    174: "복도 지도집 결합은 Atlas 추상 불성립",
    175: "타코 계획 결합 불성립",
    177: "해변 동반자 결합은 Companion 불명확",
    181: "해산물 계수기 결합은 Counter 다의어 불성립",
    182: "치과 부스 결합 불성립",
    183: "배낭여행 만 결합은 Bay 불성립",
    185: "패러세일링 상자 결합은 Bin 불성립",
    186: "치위 줄 결합은 Line 다의어 불성립",
    187: "야생동물 명부 결합은 Roll 불성립",
    188: "치실 형식 결합 불성립",
    189: "라군 시트 결합은 Sheet 다의어 불성립",
    191: "빙하 프로필 결합 불성립",
    193: "화산 수준 속성 결합은 Level 불성립",
    194: "실런트 피드 결합은 Feed 추상 불성립",
    196: "치은염 지수 결합은 Index 다의어 불성립",
    200: "구취 표본 결합은 Sample 다의어 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 78, len(APPROVE)
assert len(TRADEMARK_REJECT) == 2, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 120, len(REJECT_REASON)
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
