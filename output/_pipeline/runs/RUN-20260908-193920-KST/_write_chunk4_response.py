import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk3_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk3_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "치통 자가 문진 설문으로 명확"),
    4: (0.6, "보행기 구비·사용 요건 관리로 명확"),
    12: (0.6, "하프 연습 부스 예약·관리로 명확"),
    13: (0.6, "오보에 수리·레슨 견적 관리로 명확 (Quote·Estimate 라인 준용)"),
    18: (0.6, "아코디언 신규 레슨 온보딩 관리로 명확 (Onboarding 라인)"),
    19: (0.6, "하모니카 수강 접수 관리로 명확 (Reception 라인)"),
    20: (0.6, "부동산 계약 부속 조항(addendum) 평가로 명확 - 부동산 실무 (Evaluation 라인)"),
    21: (0.6, "보험 합의(settlement) 인테이크 설문으로 명확"),
    24: (0.6, "논문 제출 요건 관리로 명확"),
    32: (0.6, "조율 서비스 요금 관리로 명확"),
    35: (0.6, "연주 템포 기록 관리로 명확 (Recorder 라인)"),
    37: (0.6, "합주 리허설 피드백 수집 관리로 명확"),
    38: (0.6, "반주자 네트워크 뉴스레터 발송 관리로 명확"),
    43: (0.6, "캠프 등록 접수 관리로 명확 (Reception 라인)"),
    44: (0.6, "옥상 시설·안전 평가로 명확 - 점검 실무 (Evaluation 라인)"),
    45: (0.6, "합창단 단원 인테이크 설문으로 명확"),
    47: (0.6, "퇴직 연금 수혜(benefit) 관리로 명확 - 복지 실무 용어"),
    57: (0.6, "촬영 결과물 평가로 명확 (Evaluation 라인)"),
    58: (0.6, "결혼식 의식 구성 선호 설문으로 명확"),
    61: (0.6, "세차 시공 요건 관리로 명확"),
    66: (0.6, "기타 연습 진도 모니터링으로 명확 (Tracker 라인 준용)"),
    67: (0.6, "바이올린 레슨비 청구서 관리로 명확"),
    75: (0.6, "HVAC 출동 작업 안전 위험(추락·감전) 관리로 명확 - 물리 위험 실존"),
    78: (0.6, "첼로 학원 운영 사무 관리로 명확 (Harp Office 준용)"),
    81: (0.6, "클라리넷 연주 실력 진단으로 명확 (Evaluation 라인 준용)"),
    83: (0.6, "셰프 성과·요리 평가로 명확 (Evaluation 라인)"),
    84: (0.6, "애견 호텔 체크인 문진 설문으로 명확"),
    87: (0.6, "영유아 등록 요건 관리로 명확"),
    99: (0.6, "연습 시간 측정 타이머로 명확 - 실재 도구"),
    101: (0.6, "아코디언 수강 출결 체크인 관리로 명확"),
    102: (0.6, "하모니카 레슨 후속 관리로 명확 (Followup 라인)"),
    103: (0.6, "화물 적하(payload) 상태 평가로 명확 - 물류 실무 (Evaluation 라인)"),
    104: (0.6, "계약 부속 조항 확인 설문으로 명확"),
    107: (0.6, "배수로 시공 요건 관리로 명확"),
    118: (0.6, "오디오 BPM 자동 추정 도구로 명확 - 실재 도구 (Tempo 계열 준용)"),
    119: (0.6, "연주 곡 숙달도 진단으로 명확 (Diagnostic 라인)"),
    120: (0.6, "합주단 공연비 송장 관리로 명확"),
    126: (0.6, "캠프 사후 후속 관리로 명확 (Followup 라인)"),
    128: (0.6, "옥상 점검 인테이크 설문으로 명확"),
    131: (0.6, "퇴직연금 가입 요건 관리로 명확"),
    140: (0.6, "이사 서비스·견적 평가로 명확 (Evaluation 라인)"),
    141: (0.6, "촬영 요구 확인 인테이크 설문으로 명확"),
    144: (0.6, "잔류 염소 수질 기준 요건 관리로 명확"),
    150: (0.6, "바이올린 레슨비 영수증 관리로 명확"),
    153: (0.6, "우쿨렐레 신규 레슨 온보딩 관리로 명확 (Onboarding 라인)"),
    156: (0.6, "약제 등재(formulary) 요건 관리로 명확 - 약제 실무"),
    163: (0.6, "클라리넷 연습 진도 관리로 명확"),
    165: (0.6, "배출가스 검사 평가로 명확 - 자동차 실무 (Evaluation 라인)"),
    166: (0.6, "고객 식단 선호 설문으로 명확"),
    169: (0.6, "러닝머신 설치·안전 요건 관리로 명확"),
    178: (0.6, "오보에 레슨비 청구서 관리로 명확 (Violin Bill 준용)"),
    181: (0.6, "타악 워크숍 운영 관리로 명확 (Workshop 라인)"),
    184: (0.6, "하모니카 수강 신청 승인 관리로 명확 (Approval 라인)"),
    185: (0.6, "거래(trading) 성과·전략 평가로 명확 - 금융 실무 (Evaluation 라인)"),

    186: (0.6, "화물 적하 정보 확인 설문으로 명확"),
    189: (0.6, "베스팅 조건(vesting requirement) 관리로 명확 - HR 실무"),
    195: (0.6, "연습 계획 플래너로 명확 (Guitar Planner 준용)"),
    196: (0.6, "연주회 출연자 명단 관리로 명확 (Roster 라인 준용)"),
    197: (0.6, "오디션 접수 확인서 관리로 명확 (Receipt 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "러닝머신 활용률 결합 불성립 - Utilization",
    3: "영유아 혜택 결합은 Benefit 추상 불명확",
    5: "방역에 감가상각 결합 불성립",
    6: "멀칭 사직 결합은 Resignation 불성립",
    7: "가구 청소 문맥에 위험 등록 불성립",
    8: "얼룩에 보증인 결합 불성립",
    9: "화장 대상에 튜너 결합 불성립",
    10: "오르간 격자 결합은 Grid 추상 불성립",
    11: "검인 포인트 결합은 Probate 도구형 기각 라인",
    14: "비올라 대출 결합은 Loan 금융 다의어 불명확 - 악기 대여는 Rental",
    15: "트롬본 보조금 결합은 Subsidy 불성립",
    16: "타악 감지기 결합은 Detector 불성립",
    17: "만돌린 조회 결합은 Lookup 불성립",
    22: "베스팅 활용률 결합 불성립 - Utilization",
    23: "배수로 혜택 결합은 Benefit 추상 불명확",
    25: "바이라인 사직 결합은 Resignation 불성립",
    26: "심각도에 위험 결합 불성립 - 추상 대상",
    27: "애프터파티에 튜너 결합 불성립",
    28: "레슨 파도 결합은 Wave 추상 불성립",
    29: "연습 엔진 결합은 Engine 추상 불성립",
    30: "리사이탈 라인 결합은 Line 추상 불명확",
    31: "오디션 주문·순서 결합은 Order 다의어 불명확",
    33: "이론 규칙 결합은 Rule 불성립",
    34: "코드 익스텐션 결합은 Extension 다의어 불명확 - 브라우저 확장 연상",
    36: "레퍼토리 음량·권 결합은 Volume 다의어 불명확",
    39: "메트로놈 시계 결합은 Clock 불성립",
    40: "증서 높이 결합은 Height 속성어 불성립",
    41: "곡집 전압 결합은 Voltage 불성립",
    42: "교법 상태·조건 결합은 Condition 다의어 불명확",
    46: "호흡 활용률 결합 불성립 - Utilization",
    48: "우산보험 상품에 요건 결합 불성립 - 관리 대상 불명확",
    49: "오케스트라 사직 결합은 Resignation 불성립",
    50: "명상에 위험 결합 불성립",
    51: "유산 재산에 보증인 결합 불성립",
    52: "신고서에 튜너 결합 불성립",
    53: "멜로디 흐름 결합은 Flow 추상 불성립",
    54: "리듬 릴레이 결합은 Relay 불성립",
    55: "비트 대장간 결합은 Forge 불성립",
    56: "피치 감시 결합은 Watch 도구형 기각 라인",
    59: "위반 활용률 결합 불성립 - Utilization",
    60: "잔류 염소 혜택 결합은 Benefit 추상 불명확",
    62: "수전 감가상각 결합 불성립 - 소모품",
    63: "호텔 사직 결합은 Resignation 불성립",
    64: "피아노에 위험 등록 불성립",
    65: "송장에 튜너 결합 불성립",
    68: "드럼 분야·현장 결합은 Field 다의어 불명확",
    69: "보컬 비교 결합은 비교 대상 불명확",
    70: "우쿨렐레 클레임 결합은 Claim 불성립",
    71: "랙 평가 결합은 평가 대상 불성립",
    72: "대기자 활용률 결합 불성립 - Utilization",
    73: "약제집 혜택 결합은 Benefit 추상 불명확",
    74: "전세에 감가상각 결합 불성립",
    76: "금고에 보증인 결합 불성립",
    77: "플루트 비컨 결합은 Beacon 추상 불성립",
    79: "색소폰 스텁 결합은 Stub 불성립",
    80: "트럼펫 보조금 결합은 Subsidy 불성립",
    82: "베이스 시간 결합은 Time 속성어 불성립",
    85: "치통 활용률 결합 불성립 - Utilization",
    86: "러닝머신 혜택 결합은 Benefit 추상 불명확",
    88: "보행기 감가상각 결합 불성립",
    89: "방역 사직 결합은 Resignation 불성립",
    90: "멀칭에 위험 결합 불성립",
    91: "가구에 보증인 결합 불성립",
    92: "얼룩에 튜너 결합 불성립",
    93: "오르간 파도 결합은 Wave 추상 불성립",
    94: "검인 지도 결합은 Probate 도구형 기각 라인",
    95: "하프 키오스크 결합은 Kiosk 불성립",
    96: "오보에 주문·순서 결합은 Order 다의어 불명확",
    97: "비올라 합계 결합은 Sum 불성립",
    98: "트롬본 할인 결합은 Discount 불성립",
    100: "만돌린 핑 결합은 Ping 불성립",
    105: "보험 합의 활용률 결합 불성립 - Utilization",
    106: "베스팅 수혜 결합은 Benefit 추상 불명확",
    108: "논문에 감가상각 결합 불성립",
    109: "바이라인에 위험 결합 불성립",
    110: "심각도에 보증인 결합 불성립",
    111: "레슨 경로 결합은 Path 추상 불성립",
    112: "연습 도우미 결합은 Assistant 은유 불명확 - Helper 라인 준용",
    113: "리사이탈 창·기간 결합은 Window 다의어 불명확",
    114: "오디션에 청구서 결합 불성립",
    115: "튜닝 항목 결합은 Item 불명확",
    116: "이론 세부 결합은 Detail 속성어 불성립",
    117: "코드 시험·재판 결합은 Trial 다의어 불명확",
    121: "반주자에 재고 결합 불성립 - 인적 대상",
    122: "메트로놈 시간 결합은 Time 속성어 불성립",
    123: "증서 폭 결합은 Width 속성어 불성립",
    124: "곡집 와트 결합은 Wattage 불성립",
    125: "교법 습도 결합은 대상 불성립 - Humidity는 악기 보관 라인",
    127: "유예(grace) 평가 결합은 Grace 다의어 불명확",
    129: "합창 활용률 결합 불성립 - Utilization",
    130: "호흡 혜택 결합은 Benefit 추상 불명확",
    132: "우산보험에 감가상각 결합 불성립",
    133: "오케스트라에 위험 등록 불성립 - 단체 대상",
    134: "명상에 보증인 결합 불성립",
    135: "유산 재산에 튜너 결합 불성립",
    136: "멜로디 허브 결합은 Hub 추상 불성립",
    137: "리듬 금고 결합은 Vault 추상 불성립",
    138: "비트 연쇄 결합은 Cascade 추상 불성립",
    139: "피치 범위 결합은 Scope 불명확",
    142: "의식 활용률 결합 불성립 - Utilization",
    143: "위반 혜택 결합은 Benefit 추상 불명확",
    145: "세차에 감가상각 결합 불성립",
    146: "수전 사직 결합은 Resignation 불성립",
    147: "호텔에 위험 등록 불성립 - 위험 주체 불명확",
    148: "피아노에 보증인 결합 불성립",
    149: "기타 동반자 결합은 Companion 불명확 은유",
    151: "드럼 형식 결합은 Format 불성립",
    152: "보컬 제안서 결합은 Proposal 불성립",
    154: "랙 설문 결합 불성립 - 응답 대상 불성립",
    155: "대기자 혜택 결합은 Benefit 추상 불명확",
    157: "출동에 보증인 결합 불성립",
    158: "금고에 튜너 결합 불성립",
    159: "플루트 대장간 결합은 Forge 불성립",
    160: "첼로 카운터 결합은 Counter 불성립",
    161: "색소폰 명세서·진술 결합은 Statement 다의어 불명확",
    162: "트럼펫 할인 결합은 Discount 불성립",
    164: "베이스 속도 결합은 Speed 속성어 불성립",
    167: "애견 호텔 활용률 결합 불성립 - Utilization",
    168: "치통 혜택 결합은 Benefit 추상 불명확",
    170: "영유아에 감가상각 결합 불성립",
    171: "보행기 사직 결합은 Resignation 불성립",
    172: "방역에 위험 등록 불성립 - 위험 주체 불명확",
    173: "멀칭에 보증인 결합 불성립",
    174: "가구에 튜너 결합 불성립",
    175: "오르간 경로 결합은 Path 추상 불성립",
    176: "검인 틀 결합은 Probate 추상 기각 라인",
    177: "하프 만·구획 결합은 Bay 불성립",
    179: "비올라 부채 결합은 Debt 불성립",
    180: "트롬본 체납 결합은 Arrears 기각 라인",
    182: "만돌린 모델 결합은 Model 속성·다의어 불명확",
    183: "아코디언 크기 결합은 Size 속성어 불성립",
    187: "부속 조항 활용률 결합 불성립 - Utilization",
    188: "보험 합의 혜택 결합은 Benefit 추상 불명확",
    190: "배수로에 감가상각 결합 불성립",
    191: "논문 사직 결합은 Resignation 불성립",
    192: "바이라인에 보증인 결합 불성립",
    193: "심각도에 튜너 결합 불성립",
    194: "레슨 포인트 결합은 Point 불명확",
    198: "튜닝 단위 결합은 Unit 불명확",
    199: "이론 식별자 결합은 Identifier 불성립",
    200: "코드 그래프 결합은 Graph 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 59, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 141, len(REJECT_REASON)
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
