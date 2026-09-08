import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk6_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk6_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "오보에 수강료 전표 관리로 명확 (Slip 라인)"),
    4: (0.6, "타악 연속 연습 기록 관리로 명확 (Vocal Streak 준용)"),
    5: (0.6, "만돌린 레슨 예약 관리로 명확 (Appointment 라인)"),
    7: (0.6, "세차천(마이크로파이버) 품질 평가로 명확 - 장비 실무 (Evaluation 라인)"),
    8: (0.6, "역류 검사 확인 설문으로 명확"),
    11: (0.6, "복약 요건 관리로 명확"),
    17: (0.6, "수강료 장부 관리로 명확 (Ledger 라인)"),
    23: (0.6, "코드 지판 도식 관리로 명확 (Diagram 라인 준용)"),
    25: (0.6, "연주 곡 사용 계약 관리로 명확 (Agreement 라인 준용)"),
    26: (0.6, "합주 단원 지명·추천 관리로 명확"),
    32: (0.6, "보험 공제(coinsurance) 평가로 명확 - 보험 실무 (Evaluation 라인)"),
    33: (0.6, "목공 인테이크 설문으로 명확"),
    42: (0.6, "은퇴 준비 현황 추적으로 명확 (Tracker 라인)"),
    48: (0.6, "음정·음역 지도 관리로 명확 (Map 라인)"),
    49: (0.6, "선박 검사 평가로 명확 - 해운 실무 (Evaluation 라인)"),
    50: (0.6, "비행 인테이크 설문으로 명확"),
    51: (0.6, "열쇠 규격 요건 관리로 명확"),
    58: (0.6, "기타 레슨 캘린더 관리로 명확 (Calendar 라인)"),
    59: (0.6, "바이올린 레슨 슬롯 관리로 명확 (Slot 라인)"),
    63: (0.6, "치과 차트(진료기록) 평가로 명확 - 치과 실무 (Evaluation 라인)"),
    69: (0.6, "첼로 단원 명단 관리로 명확 (Roster 라인)"),
    74: (0.6, "라우터 성능 평가로 명확 - 통신 실무 (Evaluation 라인)"),
    75: (0.6, "비밀번호 보안 습관 설문으로 명확"),
    78: (0.6, "지원 자격 요건 관리로 명확"),
    90: (0.6, "타악 실력 등급 관리로 명확 (Rank 라인)"),
    91: (0.6, "만돌린 레슨 피드백 관리로 명확"),
    93: (0.6, "수영장 밸브 점검 평가로 명확 - 시설 실무 (Evaluation 라인)"),
    94: (0.6, "세차 장비 확인 설문으로 명확"),
    100: (0.6, "적하물 손상 위험 관리로 명확 - 물리 위험 실존 (Shipment Hazard 준용)"),
    103: (0.6, "학원 공지 게시판 관리로 명확"),
    104: (0.6, "연습 플레이북 관리로 명확 (Playbook 라인)"),
    106: (0.6, "오디션 슬롯 관리로 명확 (Slot 라인)"),
    118: (0.6, "신탁(trust) 평가로 명확 - 금융 실무 (Evaluation 라인)"),
    119: (0.6, "공제 확인 설문으로 명확"),
    122: (0.6, "캠프 참가 요건 관리로 명확"),
    135: (0.6, "선박 인테이크 설문으로 명확"),
    139: (0.6, "이사 짐 파손 위험 관리로 명확 - 물리 위험 실존 (Shipment Hazard 준용)"),
    143: (0.6, "기타 강사 디렉터리 관리로 명확 (Directory 라인)"),
    146: (0.6, "보컬 오디션·과제 마감 관리로 명확 (Deadline 라인)"),
    148: (0.6, "견종 특성 평가로 명확 - 수의 실무 (Evaluation 라인)"),
    149: (0.6, "치과 차트 확인 설문으로 명확"),
    154: (0.6, "첼로 레슨·조율 알림 관리로 명확 (Alert 라인)"),
    157: (0.6, "클라리넷 수강 계정 관리로 명확 (Account 라인)"),
    159: (0.6, "카풀 운영·매칭 평가로 명확 - 교통 실무 (Evaluation 라인)"),
    160: (0.6, "라우터 요구 확인 설문으로 명확"),
    163: (0.6, "문의 접수 요건 관리로 명확"),
    172: (0.6, "오보에 레슨 슬롯 관리로 명확 (Slot 라인)"),
    176: (0.6, "만돌린 레슨비 송장 관리로 명확 (Invoice 라인)"),
    178: (0.6, "지붕 상태·누수 평가로 명확 - 시설 실무 (Evaluation 라인)"),
    179: (0.6, "밸브 점검 확인 설문으로 명확"),
    182: (0.6, "사파리 투어 참가 요건 관리로 명확"),
    189: (0.6, "연습 일지 관리로 명확 (Journal 라인)"),
    190: (0.6, "연주회 심사 채점 관리로 명확 (Score 라인)"),
    194: (0.6, "코드 진행 초안 관리로 명확 - 작곡 실무"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "비올라 의무·관세 결합은 Duty 다의어 불명확",
    3: "트롬본 확장 결합은 Extension 다의어 불명확",
    6: "아코디언 한도 결합은 Limit 속성어 불성립",
    9: "사파리 활용률 결합 불성립 - Utilization",
    10: "하모니카 혜택 결합은 Benefit 추상 불명확",
    12: "거래에 감가상각 결합 불성립",
    13: "화물 사직 결합은 Resignation 불성립",
    14: "부속 조항에 위험 결합 불성립",
    15: "보험 합의에 보증인 결합 불성립",
    16: "베스팅에 튜너 결합 불성립",
    18: "연습 운영 옵스 결합은 Ops 불성립",
    19: "리사이탈 시트 결합은 Sheet 다의어 불명확",
    20: "오디션 샘플 결합은 Sample 기각 라인",
    21: "조율 세금 결합은 Tax 불성립",
    22: "이론 일련번호 결합은 Serial 불성립",
    24: "템포 도우미 결합은 Helper 불명확 은유",
    27: "반주자 무게 결합은 Weight 속성어 불성립",
    28: "메트로놈 압력 결합은 Pressure 속성어 불성립",
    29: "증서 밝기 결합은 Brightness 속성어 불성립",
    30: "곡집 상태·조건 결합은 Condition 다의어 불명확",
    31: "교법에 후속 결합 불성립",
    34: "피트니스 활용률 결합 불성립 - Utilization",
    35: "캠프 혜택 결합은 Benefit 추상 불명확",
    36: "자세에 요건 결합 불성립",
    37: "자산에 감가상각 결합 불성립",
    38: "유예(grace) 사직 결합은 Resignation 불성립",
    39: "옥상에 위험 결합 불성립",
    40: "합창에 보증인 결합 불성립",
    41: "호흡에 튜너 결합 불성립",
    43: "오케스트라 데스크 결합은 Desk 추상 불성립",
    44: "유산 릴레이 결합은 Relay 불성립",
    45: "멜로디 비컨 결합은 Beacon 추상 불성립",
    46: "리듬 신호 결합은 Signal 추상 불성립",
    47: "비트 격자 결합은 Grid 추상 불성립",
    52: "용어집에 감가상각 결합 불성립",
    53: "이사 사직 결합은 Resignation 불성립",
    54: "촬영에 위험 결합 불성립",
    55: "의식에 보증인 결합 불성립",
    56: "위반에 튜너 결합 불성립",
    57: "피아노 레이더 결합은 Radar 추상 불성립",
    60: "드럼 이자 결합은 Interest 기각 라인",
    61: "보컬 예측 결합은 Forecast 불성립",
    62: "우쿨렐레 범위 결합은 Range 속성어 불성립",
    64: "활력징후 혜택 결합은 Benefit 추상 불명확",
    65: "반복(recurring) 요건 결합은 Recurring 속성어 불명확",
    66: "랙에 위험 결합 불성립",
    67: "대기자에 튜너 결합 불성립",
    68: "플루트 루프 결합은 Loop 추상 불성립",
    70: "색소폰 회람 결합은 Circular 불명확",
    71: "트럼펫 확장 결합은 Extension 다의어 불명확",
    72: "클라리넷 회신 결합은 Reply 불성립",
    73: "베이스 하중 결합은 Load 속성어 불성립",
    76: "클라우드 활용률 결합 불성립 - Utilization",
    77: "문의 혜택 결합은 Benefit 추상 불명확",
    79: "연사에 감가상각 결합 불성립",
    80: "배출가스 사직 결합은 Resignation 불성립",
    81: "셰프에 위험 결합 불성립",
    82: "애견 호텔에 보증인 결합 불성립",
    83: "치통에 튜너 결합 불성립",
    84: "오르간에 장부 결합 불성립",
    85: "검인 스튜디오 결합은 Probate 추상 기각 라인",
    86: "하프 빈 결합은 Bin 기각 라인",
    87: "오보에 샘플 결합은 Sample 기각 라인",
    88: "비올라 수당 결합은 Allowance 불성립",
    89: "트롬본 시험·재판 결합은 Trial 다의어 불명확",
    92: "아코디언 유형 결합은 Type 속성어 불성립",
    95: "역류 활용률 결합 불성립 - Utilization",
    96: "사파리 혜택 결합은 Benefit 추상 불명확",
    97: "하모니카에 요건 결합 불성립",
    98: "용량에 감가상각 결합 불성립",
    99: "거래 사직 결합은 Resignation 불성립",
    101: "부속 조항에 보증인 결합 불성립",
    102: "보험 합의에 튜너 결합 불성립",
    105: "리사이탈 체크 결합은 Check 불명확",
    107: "조율 대출 결합은 Loan 금융 다의어 불명확",
    108: "이론 토큰 결합은 Token 기각 라인",
    109: "코드 레이아웃 결합은 Layout 불성립",
    110: "템포 무대·단계 결합은 Stage 다의어 불명확",
    111: "레퍼토리 회신 결합은 Reply 불성립",
    112: "합주 정정 결합은 Correction 불성립",
    113: "반주자 거리 결합은 Distance 속성어 불성립",
    114: "메트로놈 하중 결합은 Load 속성어 불성립",
    115: "증서 빈도 결합은 Frequency 속성어 불성립",
    116: "곡집에 습도 결합 불성립 - Humidity는 실악기 보관 라인",
    117: "교법에 승인 결합 불성립",
    120: "목공 활용률 결합 불성립 - Utilization",
    121: "피트니스 혜택 결합은 Benefit 추상 불명확",
    123: "자세에 감가상각 결합 불성립",
    124: "자산 사직 결합은 Resignation 불성립",
    125: "유예(grace)에 위험 결합 불성립",
    126: "옥상에 보증인 결합 불성립",
    127: "합창에 튜너 결합 불성립",
    128: "퇴직 흐름 결합은 Flow 추상 불성립",
    129: "오케스트라 레이더 결합은 Radar 추상 불성립",
    130: "유산 금고 결합은 Vault 추상 불성립",
    131: "멜로디 대장간 결합은 Forge 불성립",
    132: "리듬 감시 결합은 Watch 도구형 기각 라인",
    133: "비트 파도 결합은 Wave 추상 불성립",
    134: "피치 틀 결합은 Frame 불성립",
    136: "비행 활용률 결합 불성립 - Utilization",
    137: "키웨이에 감가상각 결합 불성립",
    138: "용어집 사직 결합은 Resignation 불성립",
    140: "촬영에 보증인 결합 불성립",
    141: "의식에 튜너 결합 불성립",
    142: "피아노 릴레이 결합은 Relay 불성립",
    144: "바이올린 패스 결합은 합격·통행 다의어 불명확",
    145: "드럼 자산 결합은 Asset 단독 불명확 - 회계 실무 용어 아님",
    147: "우쿨렐레 한도 결합은 Limit 속성어 불성립",
    150: "활력징후에 요건 결합 불성립",
    151: "반복(recurring)에 감가상각 결합 불성립",
    152: "랙에 보증인 결합 불성립",
    153: "플루트 격자 결합은 Grid 추상 불성립",
    155: "색소폰 자문 결합은 Advisory 불성립",
    156: "트럼펫 시험·재판 결합은 Trial 다의어 불명확",
    158: "베이스 전압 결합은 Voltage 불성립",
    161: "비밀번호 활용률 결합 불성립 - Utilization",
    162: "클라우드 혜택 결합은 Benefit 추상 불명확",
    164: "이력서에 감가상각 결합 불성립",
    165: "연사 사직 결합은 Resignation 불성립",
    166: "배출가스에 위험 결합 불성립",
    167: "셰프에 보증인 결합 불성립",
    168: "애견 호텔에 튜너 결합 불성립",
    169: "오르간 게시판 결합은 Board 다의어 불명확",
    170: "검인 실험실 결합은 Probate 추상 기각 라인",
    171: "하프 여권 결합은 Passport 기각 라인",
    173: "비올라 관세·요율 결합은 Tariff 불성립",
    174: "트롬본 그래프 결합은 Graph 불명확",
    175: "타악 추세 결합은 Trend 불성립",
    177: "아코디언 시계 결합은 Clock 불성립",
    180: "세차천 활용률 결합 불성립 - Utilization",
    181: "역류 혜택 결합은 Benefit 추상 불명확",
    183: "하모니카에 감가상각 결합 불성립",
    184: "용량 사직 결합은 Resignation 불성립",
    185: "거래에 위험 결합 불성립",
    186: "화물에 보증인 결합 불성립",
    187: "부속 조항에 튜너 결합 불성립",
    188: "레슨 데크 결합은 Deck 불성립",
    191: "오디션 패스 결합은 합격·통행 다의어 불명확",
    192: "조율 합계 결합은 Sum 불성립",
    193: "이론 서명 결합은 Signature 다의어 불명확",
    195: "템포 결과 결합은 Result 불성립",
    196: "곡목에 계정 결합 불성립",
    197: "합주 수정 결합은 Revision 불성립",
    198: "반주자 범위 결합은 Range 속성어 불성립",
    199: "메트로놈 전압 결합은 Voltage 불성립",
    200: "증서 호환성 결합은 Compatibility 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 54, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 146, len(REJECT_REASON)
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
