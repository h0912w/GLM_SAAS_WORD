import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "골든셋 승인 기준선 - Ledger 회계 서비스에 Falcon 브랜드 은유 결합, 명확·비중복·상표 무관"),
    2: (0.6, "골든셋 승인 기준선 - Notary 공증 서비스에 Quantum 브랜드 은유 결합, 명확·비중복·상표 무관"),
    6: (0.6, "골든셋 대조쌍 승인 기준선 - Ledger 회계 감시·모니터링 SaaS로 명확"),
    8: (0.6, "보컬 워크숍 운영·신청 관리 서비스로 명확"),
    9: (0.6, "우쿨렐레 연주·수업 리뷰 피드백 관리로 명확"),
    10: (0.6, "금고 보안 상태 평가 서비스로 명확 (Evaluation 라인)"),
    12: (0.6, "웨딩 작가 섭외 요건·요구사항 관리로 명확"),
    17: (0.6, "플루트 연습 진도 추적으로 명확 (학원 운영 라인)"),
    19: (0.6, "색소폰 곡목·연습 목록 관리로 명확 (학원 운영 라인)"),
    21: (0.6, "클라리넷 연습·성적 기록 관리로 명확"),
    23: (0.6, "가구 세척 전후 상태 평가로 명확 (Evaluation 라인)"),
    24: (0.6, "세탁 접수 얼룩 정보 인테이크 설문으로 명확"),
    27: (0.6, "약사 자격·복약 요건 관리로 명확"),
    28: (0.6, "마리나 시설 자산 감가상각 관리로 명확"),
    30: (0.6, "채석장 안전 위험 등록·점검 관리로 명확 (Blueprint Hazard 도면 불성립과 구분)"),
    35: (0.6, "하프 수강 등록부 관리로 명확"),
    40: (0.6, "만돌린 연주 평점·등급 관리로 명확 (Score·Level 라인 준용)"),
    41: (0.6, "아코디언 레슨·연주 영상 관리로 명확"),
    43: (0.6, "지원 티켓 심각도 평가로 명확 - CS 표준 용어 (Evaluation 라인)"),
    53: (0.6, "리사이탈 출연·참가 명단 관리로 명확"),
    59: (0.6, "레퍼토리 곡목 기록 관리로 명확"),
    70: (0.6, "명상 프로그램 효과 평가로 명확 (Evaluation 라인)"),
    71: (0.6, "자산·상속 상담 인테이크 설문으로 명확"),
    80: (0.6, "피아노 수준·연주 평가로 명확 (Evaluation 라인)"),
    83: (0.6, "배송 요건(기한·온도 등) 관리로 명확"),
    94: (0.6, "HVAC 출동 서비스 기록·품질 평가로 명확 (Evaluation 라인)"),
    96: (0.6, "촬영 배경 요건·요구사항 접수 관리로 명확"),
    98: (0.6, "풀 히터 안전 위험 점검 관리로 명확 (설비 물리 대상 - Blueprint와 구분)"),
    102: (0.6, "첼로 학습·운영 매뉴얼(플레이북) 관리로 명확"),
    107: (0.6, "조경 멀칭 시공 상태 평가로 명확 (Evaluation 라인)"),
    108: (0.6, "가구 세척 견적 인테이크 설문으로 명확"),
    111: (0.6, "커트 스타일 요구사항 접수 관리로 명확"),
    114: (0.6, "활주로 위험(FOD 등) 등록·점검 관리로 명확"),
    119: (0.6, "하프 레슨 일정 관리로 명확 (학원 운영 라인)"),
    124: (0.6, "만돌린 수강 계약서 관리로 명확"),
    125: (0.6, "아코디언 연습 일지 관리로 명확"),
    126: (0.6, "하모니카 악기 상태 점검 관리로 명확 (Heater 상태 라인 준용)"),
    127: (0.6, "기고 바이라인·기여 평가로 명확 (Evaluation 라인)"),
    128: (0.6, "문의 심각도 파악 인테이크 설문으로 명확"),
    130: (0.6, "타이어 규격·마모 기준 요건 관리로 명확"),
    137: (0.6, "리사이탈 일정·안내 알림 서비스로 명확"),
    138: (0.6, "오디션 심사 결과 요약 보고로 명확"),
    145: (0.6, "반주자 품질 평가·리뷰로 명확"),
    152: (0.6, "퇴직플랜 사후 상담·후속 관리로 명확"),
    153: (0.6, "오케스트라 합주·연주 평가로 명확 (Evaluation 라인)"),
    154: (0.6, "명상 프로그램 사전 설문으로 명확"),
    157: (0.6, "임대인 자격·임대 심사 요건 관리로 명확"),
    163: (0.6, "호텔 품질 평가로 명확 (Evaluation 라인)"),
    164: (0.6, "피아노 레슨 인테이크 설문으로 명확"),
    166: (0.6, "사건 기일·제출 요건 관리로 명확"),
    173: (0.6, "바이올린 학습 진도 타임라인 관리로 명확"),
    176: (0.6, "우쿨렐레 레슨 영상 관리로 명확"),
    177: (0.6, "HVAC 출동 후 고객 만족 설문으로 명확"),
    184: (0.6, "첼로 연습 일지 관리로 명확 (Journal)"),
    187: (0.6, "클라리넷 악보 읽기(시연) 훈련·평가로 명확"),
    189: (0.6, "모기 방역 상태 평가로 명확 (Evaluation 라인)"),
    190: (0.6, "조경 멀칭 견적 인테이크 설문으로 명확"),
    193: (0.6, "화장 허가·절차 요건 안내 관리로 명확"),
    196: (0.6, "마리나 시설 안전 위험 점검 관리로 명확"),
}

TRADEMARK_REJECT = {
    3: "유명 SaaS 브랜드 Slack과 유사 - 상표 기준선",
    4: "유명 소프트웨어 브랜드 Photoshop과 유사 - 상표 기준선",
}

DUP_REJECT = {
    7: "Ledger Sentinel과 감시자 동일 개념 의미 중복 - 대조쌍 거절 기준선",
}

REJECT_REASON = {
    5: "Thing 추상 결합 - 어떤 SaaS인지 추측 불가 (골든셋 거절 기준선)",
    11: "배경망 혜택 결합은 Benefit 추상 불명확 - 서비스 추측 불가",
    13: "히터 사직 결합은 Resignation 불성립",
    14: "세라믹 코팅 대상에는 위험 등록 서비스가 성립하지 않음 - Blueprint Hazard 준용",
    15: "배관 막힘에 보증인 결합 불성립 (Guarantor 라인)",
    16: "Luggage 수하물 물건 자체 도메인 기각 라인 + Tuner 불성립",
    18: "첼로 옵스 결합은 Ops 추상 축약 불명확",
    20: "트럼펫 토큰 결합은 Token 추상 불성립",
    22: "베이스 크기 결합은 Size 속성어 불성립",
    25: "화장 건수에 활용률 결합 불성립 - Utilization 지표어 추상",
    26: "커트 혜택 결합은 Benefit 추상 불명확",
    29: "활주로 사직 결합은 Resignation 불성립",
    31: "응축기에 보증인 결합 불성립",
    32: "생체인식에 튜너 결합 불성립",
    33: "오르간 대장간 결합은 Forge 불성립",
    34: "검인 신호 결합은 Signal 추상 불성립",
    36: "오보에 피드 결합은 Feed 추상 불성립",
    37: "비올라 품목 결합은 Item 속성어 불성립",
    38: "트롬본 서명 결합 불성립 - 악기에 전자서명 기능 불성립",
    39: "타악 공지 결합은 공지 대상 불성립으로 불명확",
    42: "하모니카 사용량 결합 불성립 - Usage 지표어",
    44: "애프터파티 활용률 결합 불성립 - Utilization",
    45: "타이어 혜택 결합은 Benefit 추상 불명확",
    46: "Litter 배변·깔짚·새끼 다의어 도메인 기각 라인",
    47: "법랑질에 감가상각 회계 결합 불성립",
    48: "Outdoor 형용사 단독 도메인 기각 라인 + Resignation 불성립",
    49: "비타민에 보증인 결합 불성립",
    50: "굴뚝에 튜너 결합 불성립",
    51: "레슨 연쇄 결합은 Cascade 추상 불성립",
    52: "연습 체인 결합은 Chain 추상 불성립",
    54: "오디션 초안 결합은 Draft 문서 불성립 (Violin Draft 준용)",
    55: "튜닝 브리핑 결합 불성립",
    56: "이론 가치 결합은 Value 속성어 불성립",
    57: "코드 보조금 결합은 Subsidy 불성립",
    58: "템포 총액 결합은 Total 속성어 불성립",
    60: "앙상블 핑 결합은 Ping 추상 불성립",
    61: "반주자 봉인 결합은 Seal 불성립",
    62: "메트로놈 크기 결합은 Size 속성어 불성립",
    63: "증서 범위 결합은 Range 불성립",
    64: "곡집 속도 결합은 Speed 속성어 불성립",
    65: "교법 전압 결합은 Voltage 불성립",
    66: "캠프 사용량 결합 불성립 - Usage 지표어",
    67: "합창 고장·분석 결합은 Breakdown 불명확",
    68: "재무 은퇴에 리셉션 행사 결합 불성립",
    69: "오케스트라 행렬 결합은 Matrix 추상 불성립",
    72: "신고서에 활용률 결합 불성립 - Utilization",
    73: "임대인 혜택 결합은 Benefit 추상 불명확",
    74: "멜로디에 요건 결합 불성립",
    75: "수면에 감가상각 결합 불성립 - sleep deprivation과 혼동",
    76: "리듬에 보증인 결합 불성립",
    77: "Jogging 활동 자체 도메인 기각 라인 + Tuner 불성립",
    78: "비트 허브 결합은 Hub 추상 불성립",
    79: "피치 금고 결합은 Vault 추상 불성립",
    81: "송장 활용률 결합 불성립 - Utilization",
    82: "사건서류 혜택 결합은 Benefit 추상 불명확",
    84: "임차인에 감가상각 결합 불성립",
    85: "보험료 사직 결합은 Resignation 불성립",
    86: "근태에 위험 결합 불성립 - Blueprint Hazard 준용",
    87: "도면에 보증인 결합 불성립",
    88: "상품옵션에 튜너 결합 불성립",
    89: "기타 도감 결합은 Atlas 기능 불명확",
    90: "바이올린 요약 결합은 요약 대상 불성립",
    91: "드럼 버전 결합은 Version 속성어 불성립",
    92: "보컬 지킴이 결합은 Guardian 불명확 은유 (Sentinel 표준 어휘와 구분)",
    93: "우쿨렐레 레시피 결합 불성립",
    95: "금고 설문 결합 불성립 - 인테이크 대상 불성립",
    97: "작가에게 감가상각 결합 불성립",
    99: "세라믹에 보증인 결합 불성립",
    100: "배관에 튜너 결합 불성립",
    101: "플루트 흐름 결합은 Flow 추상 불성립",
    103: "색소폰 표 결합은 Table 불성립",
    104: "트럼펫 서명 결합 불성립 - 악기에 서명 기능 불성립",
    105: "클라리넷 사본 결합은 Copy 속성어 불성립",
    106: "베이스 길이 결합은 Length 속성어 불성립",
    109: "얼룩 활용률 결합 불성립 - Utilization",
    110: "화장 혜택 결합은 Benefit 추상 불명확",
    112: "약사에게 감가상각 결합 불성립",
    113: "마리나 사직 결합은 Resignation 불성립",
    115: "채석에 보증인 결합 불성립",
    116: "응축기에 튜너 결합 불성립",
    117: "오르간 연쇄 결합은 Cascade 추상 불성립",
    118: "검인 감시 결합은 Watch 불성립 - 도구형 Probate 기각 라인",
    120: "오보에 초안 결합은 Draft 문서 불성립",
    121: "비올라 유닛 결합은 Unit 속성어 불성립",
    122: "트롬본 마커 결합 불성립",
    123: "타악 계산기 결합 불성립",
    129: "애프터파티 혜택 결합은 Benefit 추상 불명확",
    131: "Litter 다의어 도메인 기각 라인 + 감가상각 불성립",
    132: "법랑질 사직 결합은 Resignation 불성립",
    133: "Outdoor 형용사 단독 도메인 기각 라인 + 위험 결합 불성립",
    134: "비타민에 튜너 결합 불성립",
    135: "레슨 브리지 결합은 Bridge 기각 라인",
    136: "연습 링 결합은 Ring 불성립",
    139: "튜닝 회람 결합은 Circular 불성립",
    140: "이론 지분 결합은 Stake 불성립",
    141: "코드 할인 결합 불성립",
    142: "템포 위젯 결합은 Widget 추상 불성립",
    143: "레퍼토리 사본 결합은 Copy 불성립",
    144: "앙상블 모델 결합은 ML 용어와 충돌해 불명확",
    146: "메트로놈 길이 결합은 Length 속성어 불성립",
    147: "증서 한도 결합은 Limit 불성립",
    148: "곡집 깊이 결합은 Depth 속성어 불성립",
    149: "교법 와트 결합은 Wattage 불성립",
    150: "캠프 상태 결합은 대상 불성립으로 불명확",
    151: "합창 센서 결합은 Sensor 불성립",
    155: "자산 활용률 결합 불성립 - Utilization",
    156: "신고서 혜택 결합은 Benefit 추상 불명확",
    158: "멜로디에 감가상각 결합 불성립",
    159: "수면 사직 결합은 Resignation 불성립",
    160: "리듬에 튜너 결합 불성립",
    161: "비트 데스크 결합은 Desk 추상 불성립",
    162: "피치 나침반 결합은 Compass 불명확 은유",
    165: "송장 혜택 결합은 Benefit 추상 불명확",
    167: "배송에 감가상각 결합 불성립",
    168: "임차 해지는 Resignation 불성립 - Lease 종료 어휘와 불일치",
    169: "보험료 위험 결합은 불명확",
    170: "근태에 보증인 결합 불성립",
    171: "도면에 튜너 결합 불성립",
    172: "기타 관리인 결합은 Keeper 불명확 은유",
    174: "드럼 링크 결합은 Link 추상 불성립",
    175: "보컬 도우미 결합은 Helper 불명확",
    178: "금고 활용률 결합 불성립 - Utilization",
    179: "배경망에 감가상각 결합 불성립",
    180: "작가 사직 결합은 Resignation 불성립",
    181: "히터에 보증인 결합 불성립",
    182: "세라믹에 튜너 결합 불성립",
    183: "플루트 허브 결합은 Hub 추상 불성립",
    185: "색소폰 전표 결합은 Slip 불성립",
    186: "트럼펫 마커 결합 불성립",
    188: "베이스 무게 결합은 Weight 속성어 불성립",
    191: "가구 활용률 결합 불성립 - Utilization",
    192: "얼룩 혜택 결합은 Benefit 추상 불명확",
    194: "커트에 감가상각 결합 불성립",
    195: "약사 사직 결합은 Resignation 불성립",
    197: "활주로에 보증인 결합 불성립",
    198: "채석에 튜너 결합 불성립",
    199: "오르간 브리지 결합은 Bridge 기각 라인",
    200: "검인 범위 결합은 Scope 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 59, len(APPROVE)
assert len(TRADEMARK_REJECT) == 2, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 1, len(DUP_REJECT)
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
print(f"approve={approved} reject={len(decisions)-approved} (tm={len(TRADEMARK_REJECT)} dup={len(DUP_REJECT)})")
