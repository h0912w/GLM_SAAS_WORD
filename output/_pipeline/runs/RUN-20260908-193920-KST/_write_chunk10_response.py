import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk9_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk9_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    6: (0.6, "하모니카 연습 진도 트래커로 명확 (Tracker 라인)"),
    10: (0.6, "오디션 메모 관리로 명확 (Memo 라인)"),
    20: (0.6, "곡집 후속 조치 관리로 명확"),
    21: (0.6, "석조 시공 확인 설문으로 명확"),
    24: (0.6, "레슨 방식 요건 관리로 명확"),
    30: (0.6, "캠프 참가 트래커로 명확 (Tracker 라인)"),
    38: (0.6, "음정 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    40: (0.6, "장례 구성 요건 관리로 명확"),
    41: (0.6, "선박 운항 안전 위험 관리로 명확 - 해운 안전 실무 (물리 위험 라인)"),
    47: (0.6, "보컬 연습 템플릿 관리로 명확 (Worksheet 라인 준용)"),
    49: (0.6, "배포 롤백 평가로 명확 - DevOps 실무 (Evaluation 라인)"),
    57: (0.6, "트럼펫 운주 도식 관리로 명확 (Schematic 라인)"),
    60: (0.6, "숙제 평가로 명확 - 교육 실무 (Evaluation 라인)"),
    61: (0.6, "용접 확인 설문으로 명확"),
    64: (0.6, "투표 절차 요건 관리로 명확"),
    72: (0.6, "하프 연습 리포트 관리로 명확 (Report 라인)"),
    73: (0.6, "오보에 레슨 메모 관리로 명확 (Memo 라인)"),
    77: (0.6, "만돌린 출연 추천 관리로 명확 (Nomination 라인)"),
    79: (0.6, "HVAC 점화 장치 점검 평가로 명확 (Evaluation 라인)"),
    83: (0.6, "촬영지 요건 관리로 명확"),
    91: (0.6, "연습실 운영 사무 관리로 명확 (Office 라인)"),
    92: (0.6, "리사이탈 이력 기록 관리로 명확 (Record·Log 라인 준용)"),
    99: (0.6, "합주 연습 리뷰 관리로 명확 (Review 라인)"),
    103: (0.6, "곡 채택 승인 관리로 명확 (Approval 라인)"),
    104: (0.6, "파산 진행 평가로 명확 - 금융·법무 실무 (Evaluation 라인)"),
    107: (0.6, "보관 조건 요건 관리로 명확"),
    119: (0.6, "리듬 패턴 지도 관리로 명확 (Map 라인)"),
    122: (0.6, "세탁 주문 요건 관리로 명확"),
    130: (0.6, "보컬 연습 가이드 관리로 명확 (Guide 라인)"),
    132: (0.6, "롤백 확인 설문으로 명확"),
    134: (0.6, "티켓 발권 요건 관리로 명확"),
    141: (0.6, "클라리넷 수업 가능 시간 관리로 명확 (Availability 라인)"),
    143: (0.6, "발렛 주차 서비스 평가로 명확 - 호텔 실무 (Evaluation 라인)"),
    144: (0.6, "숙제 확인 설문으로 명확"),
    147: (0.6, "기부 자격·요건 관리로 명확"),
    155: (0.6, "하프 연습 로그 관리로 명확 (Log 라인)"),
    158: (0.6, "트롬본 악곡 스케치 관리로 명확 (Sketch 라인)"),
    159: (0.6, "타악 연주 참조 자료 관리로 명확 (Reference 라인)"),
    162: (0.6, "투약(주사) 평가로 명확 - 약국 실무 (Evaluation 라인)"),
    163: (0.6, "점화 장치 확인 설문으로 명확"),
    166: (0.6, "계단 운반 조건 요건 관리로 명확"),
    169: (0.6, "지붕 작업 안전 위험 관리로 명확 - 추락 위험 실존 (물리 위험 라인)"),
    173: (0.6, "수강 예약 포털 관리로 명확 - 구체 서비스 지시 (Portal 실측 승자 패턴)"),
    180: (0.6, "템포 기록 관리로 명확 (Record 라인)"),
    187: (0.6, "스트레칭 평가로 명확 - 건강 서비스 실무 (Evaluation 라인)"),
    188: (0.6, "파산 확인 설문으로 명확"),
    190: (0.6, "집안일 수행 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "지붕에 감가상각 결합 불성립",
    2: "밸브 사직 결합은 Resignation 불성립",
    3: "세차천에 위험 결합 불성립",
    4: "역류에 보증인 결합 불성립",
    5: "사파리에 튜너 결합 불성립",
    7: "레슨 센터 결합은 Center 불성립",
    8: "연습 검색기 결합은 Finder 불성립 - 검색 대상 불명확",
    9: "리사이탈 뷰 결합은 View 불성립",
    11: "조율 청구 결합은 Charge 다의어 불명확",
    12: "이론 부과금 결합은 Levy 기각 라인",
    13: "코드 개수 결합은 Count 불성립",
    14: "템포 제안 결합은 Proposal 불성립",
    15: "레퍼토리 핑 결합은 Ping 불성립",
    16: "합주 인장·봉인 결합은 Seal 불성립",
    17: "반주자 속도 결합은 Speed 속성어 불성립",
    18: "메트로놈 용량 결합은 Capacity 속성어 불성립",
    19: "증서 에피소드 결합은 Episode 불성립",
    22: "집안일 활용률 결합 불성립 - Utilization",
    23: "보관 혜택 결합은 Benefit 추상 불명확",
    25: "수분 감가상각 결합 불성립",
    26: "신탁 사직 결합은 Resignation 불성립",
    27: "공제에 위험 결합 불성립",
    28: "목공에 보증인 결합 불성립",
    29: "피트니스에 튜너 결합 불성립",
    31: "합창 릴레이 결합은 Relay 불성립",
    32: "퇴직 컴퍼스 결합은 Compass 추상 불성립",
    33: "오케스트라 연쇄 결합은 Cascade 추상 불성립",
    34: "유산 신호 결합은 Signal 불성립",
    35: "멜로디 루프 결합은 Loop 추상 불성립",
    36: "리듬 포인트 결합은 Point 불성립",
    37: "비트 코어 결합은 Core 불성립",
    39: "세탁 주문 혜택 결합은 Benefit 추상 불명확",
    42: "비행에 보증인 결합 불성립",
    43: "피아노 브리지 결합은 Bridge 기각 라인",
    44: "기타 키오스크 결합은 Kiosk 불성립",
    45: "바이올린 할당량 결합은 Quota 불성립",
    46: "드럼 선불·전진 결합은 Advance 다의어 불명확",
    48: "우쿨렐레 높이 결합은 Height 속성어 불성립",
    50: "스크리닝 활용률 결합 불성립 - Utilization",
    51: "티켓팅 혜택 결합은 Benefit 추상 불명확",
    52: "견종 사직 결합은 Resignation 불성립",
    53: "치과 차트에 위험 결합 불성립",
    54: "플루트 베이스 결합은 Base 추상 불성립",
    55: "첼로 라인 결합은 Line 추상 불명확",
    56: "색소폰 항목 결합은 Item 다의어 불명확",
    58: "클라리넷 모델 결합은 Model 속성어·다의어 불명확",
    59: "베이스 사용률 결합은 Usage 불성립",
    62: "트랙터 활용률 결합 불성립 - Utilization",
    63: "기부 혜택 결합은 Benefit 추상 불명확",
    65: "독자에 감가상각 결합 불성립",
    66: "카풀 사직 결합은 Resignation 불성립",
    67: "라우터에 위험 결합 불성립",
    68: "비밀번호에 보증인 결합 불성립",
    69: "클라우드에 튜너 결합 불성립",
    70: "오르간 센터 결합은 Center 불성립",
    71: "검인 콘솔 결합은 Probate 도구형 기각 라인",
    74: "비올라 버전 결합은 Version 속성어 불성립",
    75: "트롬본 배치 결합은 Layout 불성립",
    76: "타악 판독·독서 결합은 Reading 다의어 불명확",
    78: "아코디언 온도 결합은 Temperature 속성어 불성립",
    80: "림 확인 설문은 대상 불성립",
    81: "관용구 활용률 결합 불성립 - Utilization",
    82: "계단 혜택 결합은 Benefit 추상 불명확",
    84: "장식에 감가상각 결합 불성립",
    85: "지붕 사직 결합은 Resignation 불성립",
    86: "밸브 위험 결합은 위험 관리 대상 불성립 - 부속 장치",
    87: "세차천에 보증인 결합 불성립",
    88: "역류에 튜너 결합 불성립",
    89: "하모니카 흐름 결합은 Flow 추상 불성립",
    90: "레슨 구역 결합은 Zone 불성립",
    93: "오디션 할당량 결합은 Quota 불성립",
    94: "조율 의무·관세 결합은 Duty 다의어 불명확",
    95: "이론 기한 결합은 Due 단독 불성립",
    96: "코드 메시지 결합은 Message 불성립",
    97: "템포 보증 결합은 Guarantee 불성립",
    98: "레퍼토리 모델 결합은 Model 불성립",
    100: "반주자 깊이 결합은 Depth 속성어 불성립",
    101: "메트로놈 사용률 결합은 Usage 불성립",
    102: "증서 주기 결합은 Cycle 불성립",
    105: "석조 활용률 결합 불성립 - Utilization",
    106: "집안일 혜택 결합은 Benefit 추상 불명확",
    108: "교법에 감가상각 결합 불성립",
    109: "수분 사직 결합은 Resignation 불성립",
    110: "신탁에 위험 결합 불성립",
    111: "공제에 보증인 결합 불성립",
    112: "목공에 튜너 결합 불성립",
    113: "캠프 흐름 결합은 Flow 추상 불성립",
    114: "합창 금고 결합은 Vault 추상 불성립",
    115: "퇴직 비컨 결합은 Beacon 추상 불성립",
    116: "오케스트라 브리지 결합은 Bridge 기각 라인",
    117: "유산 감시 결합은 Watch 도구형 기각 라인",
    118: "멜로디 격자 결합은 Grid 추상 불성립",
    120: "비트 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    121: "피치 실험실 결합은 Lab 불성립",
    123: "장례 구성 감가상각 결합 불성립",
    124: "선박에 보증인 결합 불성립",
    125: "비행에 튜너 결합 불성립",
    126: "피아노 신호 결합은 Signal 불성립",
    127: "기타 베이·만 결합은 Bay 불성립",
    128: "바이올린 타브 결합은 Tab 불성립 - 타브 악보는 기타 계열 용어",
    129: "드럼 벌금 결합은 Penalty 기각 라인",
    131: "우쿨렐레 폭 결합은 Width 속성어 불성립",
    133: "스크리닝 혜택 결합은 Benefit 추상 불명확",
    135: "견종에 위험 결합 불성립",
    136: "치과 차트에 보증인 결합 불성립",
    137: "플루트 코어 결합은 Core 불성립",
    138: "첼로 창·기간 결합은 Window 다의어 불명확",
    139: "색소폰 단위 결합은 Unit 불성립",
    140: "트럼펫 배치 결합은 Layout 불성립",
    142: "베이스 상태·조건 결합은 Condition 다의어 불명확",
    145: "용접 활용률 결합 불성립 - Utilization",
    146: "트랙터 혜택 결합은 Benefit 추상 불명확",
    148: "투표에 감가상각 결합 불성립",
    149: "독자 사직 결합은 Resignation 불성립",
    150: "카풀에 위험 결합 불성립",
    151: "라우터에 보증인 결합 불성립",
    152: "비밀번호에 튜너 결합 불성립",
    153: "오르간 구역 결합은 Zone 불성립",
    154: "검인 패널 결합은 Panel 불성립",
    156: "오보에 할당량 결합은 Quota 불성립",
    157: "비올라 링크 결합은 Link 불성립",
    160: "만돌린 정정 결합은 Correction 불성립",
    161: "아코디언 압력 결합은 Pressure 속성어 불성립",
    164: "림 활용률 결합은 대상 불성립",
    165: "관용구 혜택 결합은 Benefit 추상 불명확",
    167: "촬영지에 감가상각 결합 불성립",
    168: "장식 사직 결합은 Resignation 불성립",
    170: "밸브에 보증인 결합 불성립",
    171: "세차천에 튜너 결합 불성립",
    172: "하모니카 허브 결합은 Hub 추상 불성립",
    174: "연습 카운터 결합은 Counter 불성립",
    175: "리사이탈 파일 결합은 File 다의어 불명확",
    176: "오디션 탭 결합은 Tab 불성립",
    177: "조율 수당 결합은 Allowance 기각 라인",
    178: "이론 보조금 결합은 Subsidy 기각 라인",
    179: "코드 합계 결합은 Total 불성립",
    181: "레퍼토리 가용성 결합은 대상 불성립",
    182: "합주 조리법 결합은 Recipe 불성립",
    183: "반주자 높이 결합은 Height 속성어 불성립",
    184: "메트로놈 상태·조건 결합은 Condition 다의어 불명확",
    185: "증서 내역 분석 결합은 Breakdown 불성립",
    186: "곡집 매트릭스 결합은 Matrix 추상 불성립",
    189: "석조 혜택 결합은 Benefit 추상 불명확",
    191: "보관에 감가상각 결합 불성립",
    192: "교법 사직 결합은 Resignation 불성립",
    193: "수분에 위험 결합 불성립",
    194: "신탁에 보증인 결합 불성립 - Guarantor는 Tenant만 성립",
    195: "공제에 튜너 결합 불성립",
    196: "캠프 허브 결합은 Hub 추상 불성립",
    197: "합창 컴퍼스 결합은 Compass 추상 불성립",
    198: "퇴직 대장간 결합은 Forge 불성립",
    199: "오케스트라 신호 결합은 Signal 불성립",
    200: "유산 범위 결합은 Scope 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 47, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 153, len(REJECT_REASON)
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
