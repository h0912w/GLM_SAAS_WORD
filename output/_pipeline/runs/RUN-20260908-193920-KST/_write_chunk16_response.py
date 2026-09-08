import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk15_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk15_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "오보에 연습 계획 관리로 명확 (Plan 라인)"),
    7: (0.6, "만돌린 소식지 관리로 명확 (Newsletter 라인)"),
    9: (0.6, "연금 제도·수령 평가로 명확 - HR 실무 (Evaluation 라인)"),
    10: (0.6, "외장재 확인 설문으로 명확"),
    13: (0.6, "헤드라인 요건 관리로 명확"),
    21: (0.6, "리사이탈 청구서 관리로 명확 (Bill 라인)"),
    24: (0.6, "음악이론 다이어그램 관리로 명확 (Diagram 라인)"),
    30: (0.6, "반려동물 행동 평가로 명확 - 수의 실무 (Evaluation 라인)"),
    31: (0.6, "보모 확인 설문으로 명확"),
    33: (0.6, "운동 요건 관리로 명확"),
    42: (0.6, "합창 배치 지도 관리로 명확 (Map 라인)"),
    50: (0.6, "편집 품질 평가로 명확 - 미디어 실무 (Evaluation 라인)"),
    51: (0.6, "배포 요건 관리로 명확"),
    54: (0.6, "기타 연습 로그 관리로 명확 (Log 라인)"),
    59: (0.6, "채용 프로세스 평가로 명확 - HR 실무 (Evaluation 라인)"),
    62: (0.6, "코호트 요건 관리로 명확"),
    64: (0.6, "변전소 작업 안전 위험 관리로 명확 - 감전 위험 실존"),
    67: (0.6, "첼로 연습 이력 관리로 명확 (History 라인)"),
    71: (0.6, "수영장 탁도 검사 평가로 명확 - 수영장 관리 실무 (Evaluation 라인)"),
    72: (0.6, "폼 확인 설문으로 명확"),
    87: (0.6, "만돌린 악기 재고 관리로 명확 (Inventory 라인)"),
    89: (0.6, "잔존가치(salvage) 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    90: (0.6, "연금 확인 설문으로 명확"),
    93: (0.6, "회의 요건 관리로 명확"),
    101: (0.6, "리사이탈 영수증 관리로 명확 (Receipt 라인)"),
    104: (0.6, "음악이론 도식 관리로 명확 (Schematic 라인)"),
    110: (0.6, "행동 확인 설문으로 명확"),
    115: (0.6, "유조선 운송 사고 위험 관리로 명확 - 유출 위험 실존"),
    129: (0.6, "편집 확인 설문으로 명확"),
    132: (0.6, "피아노 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    135: (0.6, "드럼 연습 알림 관리로 명확 (Notification 라인)"),
    136: (0.6, "보컬 레슨 예약 관리로 명확 (Appointment 라인)"),
    138: (0.6, "자부담(deductible) 산정 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    139: (0.6, "채용 확인 설문으로 명확"),
    141: (0.6, "점유 요건 관리로 명확"),
    143: (0.6, "농약 살포 작업 안전 위험 관리로 명확 - 물리 위험 실존"),
    149: (0.6, "클라리넷 수강료 결제 관리로 명확 (Payment 라인)"),
    150: (0.6, "탁도 확인 설문으로 명확"),
    153: (0.6, "호스텔 요건 관리로 명확"),
    161: (0.6, "하프 연습 소식·갱신 관리로 명확 (Update 라인)"),
    165: (0.6, "타액 강사-학생 매칭 관리로 명확 (Match 라인)"),
    168: (0.6, "계약 변경(amendment) 검토 평가로 명확 - 부동산 실무 (Evaluation 라인)"),
    169: (0.6, "잔존물 확인 설문으로 명확"),
    172: (0.6, "논문 제출 요건 관리로 명확"),
    180: (0.6, "연습생 명단 관리로 명확 (Roll 라인)"),
    190: (0.6, "맞춤 가구(cabinetry) 시공 평가로 명확 - 건설 실무 (Evaluation 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "검인 조수 결합은 Assistant 불명확 기각 라인",
    2: "하프 수준 결합은 Level 속성어 불성립",
    4: "비올라 이자·관심 결합은 Interest 기각 라인",
    5: "트롬본 생성기 결합은 불성립",
    6: "타액 계좌·계정 결합은 Account 다의어 불명확",
    8: "아코디언 고장 분석 결합은 Breakdown 불성립",
    11: "논문 활용률 결합 불성립 - Utilization",
    12: "회의 혜택 결합은 Benefit 추상 불명확",
    14: "우선순위 감가상각 결합 불성립",
    15: "헤드헌터 사직 결합은 Resignation 불성립",
    16: "굿즈에 위험 결합 불성립",
    17: "진드기에 튜너 결합 불성립",
    18: "하모니카 루프 결합은 Loop 추상 불성립",
    19: "레슨 관리자 결합은 Manager 불성립",
    20: "연습 라인 결합은 Line 추상 불명확",
    22: "오디션 비용 결합은 Cost 속성어 불성립",
    23: "조율 속성 결합은 Attribute 불성립",
    25: "코드 보호자 결합은 Guardian 불명확 기각 라인",
    26: "템포 평점 결합은 불성립",
    27: "레퍼토리 정정 결합은 Correction 불성립",
    28: "합주 거리 결합은 Distance 속성어 불성립",
    29: "반주자 습도 결합은 Humidity 불성립",
    32: "메트로놈 혜택 결합은 Benefit 추상 불명확",
    34: "수취인 감가상각 결합 불성립",
    35: "탱커 사직 결합은 Resignation 불성립",
    36: "증서에 위험 결합 불성립",
    37: "계약자에 보증인 결합 불성립",
    38: "상판에 튜너 결합 불성립",
    39: "곡집 허브 결합은 Hub 추상 불성립",
    40: "교법 대장간 결합은 Forge 불성립",
    41: "캠프 루프 결합은 Loop 추상 불성립",
    43: "퇴직 베이스 결합은 Base 추상 불성립",
    44: "오케스트라 게시판 결합은 Board 다의어 불명확",
    45: "유산 스튜디오 결합은 불성립",
    46: "멜로디 터미널 결합은 Terminal 불성립",
    47: "리듬 콘솔 결합은 Console 도구형 불성립",
    48: "비트 궤도 결합은 Rail 불성립",
    49: "피치 관문 결합은 Gate 불성립",
    52: "등록에 위험 결합 불성립",
    53: "피아노 데크 결합은 Deck 불성립",
    55: "바이올린 가격 결합은 Price 속성어 불성립",
    56: "드럼 렌더링 결합은 Rendering 불성립",
    57: "보컬 바코드 결합은 불성립",
    58: "우쿨렐레 주기 결합은 Cycle 불성립",
    60: "카탈로그 활용률 결합 불성립 - Utilization",
    61: "점유 혜택 결합은 Benefit 추상 불명확",
    63: "농약 사직 결합은 Resignation 불성립",
    65: "기록물에 튜너 결합 불성립",
    66: "플루트 경로 결합은 Route 불성립",
    68: "색소폰 수당 결합은 Allowance 기각 라인",
    69: "트럼펫 생성기 결합은 불성립",
    70: "클라리넷 개정 결합은 Revision 불성립",
    73: "세탁기 활용률 결합 불성립 - Utilization",
    74: "호스텔 혜택 결합은 Benefit 추상 불명확",
    75: "베이스 요건 결합은 요건 대상 불성립",
    76: "분류(triage) 감가상각 결합 불성립",
    77: "배당 사직 결합은 Resignation 불성립",
    78: "패러리걸에 위험 결합 불성립",
    79: "택배에 보증인 결합 불성립",
    80: "오르간 관리자 결합은 Manager 불성립",
    81: "검인 플래너 결합은 Probate 도구형 기각 라인",
    82: "하프 요율 결합은 Rate 속성어 불성립",
    83: "오보에 비용 결합은 Cost 속성어 불성립",
    84: "비올라 자산 결합은 Asset 단독 불명확",
    85: "트롬본 녹음기 결합은 불성립",
    86: "타액 케이스·소송 결합은 Case 다의어 불명확",
    88: "아코디언 센서 결합은 Sensor 불성립",
    91: "외장재 활용률 결합 불성립 - Utilization",
    92: "논문 혜택 결합은 Benefit 추상 불명확",
    94: "헤드라인 감가상각 결합 불성립",
    95: "우선순위 사직 결합은 Resignation 불성립",
    96: "헤드헌터에 위험 결합 불성립",
    97: "굿즈에 보증인 결합 불성립",
    98: "하모니카 격자 결합은 Grid 추상 불성립",
    99: "레슨 엔진 결합은 Engine 추상 불성립",
    100: "연습 창·기간 결합은 Window 다의어 불명확",
    102: "오디션 가격 결합은 Price 속성어 불성립",
    103: "조율 분야 결합은 Field 다의어 불명확",
    105: "코드 조수 결합은 Helper 불명확 기각 라인",
    106: "템포 합의 결합은 불성립",
    107: "레퍼토리 개정 결합은 Revision 불성립",
    108: "합주 범위 결합은 Range 속성어 불성립",
    109: "반주자 에피소드 결합은 Episode 불성립",
    111: "보모 활용률 결합 불성립 - Utilization",
    112: "메트로놈 요건 결합은 불성립",
    113: "운동 감가상각 결합 불성립",
    114: "수취인 사직 결합은 Resignation 불성립",
    116: "증서에 보증인 결합 불성립",
    117: "계약자에 튜너 결합 불성립",
    118: "곡집 데스크 결합은 Desk 추상 불성립",
    119: "교법 연쇄 결합은 Cascade 추상 불성립",
    120: "캠프 격자 결합은 Grid 추상 불성립",
    121: "합창 틀 결합은 Frame 불성립",
    122: "퇴직 코어 결합은 Core 불성립",
    123: "오케스트라 데크 결합은 Deck 불성립",
    124: "유산 실험실 결합은 Lab 불성립",
    125: "멜로디 센터 결합은 Center 불성립",
    126: "리듬 패널 결합은 Panel 불성립",
    127: "비트 흔적 결합은 Trail 불성립",
    128: "피치 연결점 결합은 Nexus 추상 불성립",
    130: "배포 감가상각 결합 불성립",
    131: "등록에 보증인 결합 불성립",
    133: "기타 양식 결합은 Form 다의어 불명확",
    134: "바이올린 요금(교통) 결합은 Fare 기각 라인",
    137: "우쿨렐레 고장 분석 결합은 Breakdown 불성립",
    140: "카탈로그 혜택 결합은 Benefit 추상 불명확",
    142: "코호트 감가상각 결합 불성립",
    144: "변전소에 보증인 결합 불성립",
    145: "플루트 궤도 결합은 Rail 불성립",
    146: "첼로 파일 결합은 File 다의어 불명확",
    147: "색소폰 관세 결합은 Tariff 기각 라인",
    148: "트럼펫 녹음기 결합은 불성립",
    151: "폼 활용률 결합 불성립 - Utilization",
    152: "세탁기 혜택 결합은 Benefit 추상 불명확",
    154: "베이스 감가상각 결합 불성립",
    155: "분류(triage) 사직 결합은 Resignation 불성립",
    156: "배당에 위험 결합 불성립",
    157: "패러리걸에 보증인 결합 불성립",
    158: "택배에 튜너 결합 불성립",
    159: "오르간 엔진 결합은 Engine 추상 불성립",
    160: "검인 스케줄러 결합은 Probate 도구형 기각 라인",
    162: "오보에 가격 결합은 Price 속성어 불성립",
    163: "비올라 부과금 결합은 Levy 기각 라인",
    164: "트롬본 추정기 결합은 불성립",
    166: "만돌린 청구 결합은 Claim 다의어 불명확",
    167: "아코디언 접수 결합은 Reception 불성립",
    170: "연금 활용률 결합 불성립 - Utilization",
    171: "외장재 혜택 결합은 Benefit 추상 불명확",
    173: "회의 감가상각 결합 불성립",
    174: "헤드라인 사직 결합은 Resignation 불성립",
    175: "우선순위에 위험 결합 불성립",
    176: "헤드헌터에 보증인 결합 불성립",
    177: "굿즈에 튜너 결합 불성립",
    178: "하모니카 파도 결합은 Wave 추상 불성립",
    179: "레슨 조수 결합은 Assistant 불명확 기각 라인",
    181: "리사이탈 코드 결합은 Code 다의어 불명확",
    182: "오디션 요금(교통) 결합은 Fare 기각 라인",
    183: "조율 형식 결합은 Format 불성립",
    184: "이론 배치 결합은 Layout 불성립",
    185: "코드 무대 결합은 Stage 다의어 불명확",
    186: "템포 회신 결합은 Reply 불성립",
    187: "레퍼토리 결제 결합은 불성립",
    188: "합주 한도 결합은 Limit 속성어 불성립",
    189: "반주자 주기 결합은 Cycle 불성립",
    191: "행동 활용률 결합 불성립 - Utilization",
    192: "보모 혜택 결합은 Benefit 추상 불명확",
    193: "메트로놈 감가상각 결합 불성립",
    194: "운동 사직 결합은 Resignation 불성립",
    195: "수취인에 위험 결합 불성립",
    196: "탱커에 보증인 결합 불성립",
    197: "증서에 튜너 결합 불성립",
    198: "곡집 레이더 결합은 Radar 추상 불성립",
    199: "교법 브리지 결합은 Bridge 기각 라인",
    200: "캠프 파도 결합은 Wave 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 46, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 154, len(REJECT_REASON)
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
