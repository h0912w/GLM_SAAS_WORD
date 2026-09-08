import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk12_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk12_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    16: (0.6, "바이올린 레슨 예약 확인 관리로 명확 (Confirmation 라인)"),
    18: (0.6, "보컬 강사-학생 매칭 관리로 명확 (Match 라인)"),
    20: (0.6, "기록물 확인 설문으로 명확"),
    29: (0.6, "클라리넷 청구서 관리로 명확 (Invoice·Bill 라인)"),
    31: (0.6, "택배 배송 평가로 명확 - 물류 실무 (Evaluation 라인)"),
    34: (0.6, "비계 시공 요건 관리로 명확"),
    42: (0.6, "하프 연습 노트 관리로 명확 (Note 라인)"),
    46: (0.6, "타악 연습 진도 관리로 명확 (Progress 라인)"),
    49: (0.6, "이벤트 굿즈(판촉물) 평가로 명확 - 행사 실무 (Evaluation 라인)"),
    52: (0.6, "장난감 요건 관리로 명확"),
    60: (0.6, "연습생 명단 관리로 명확 (Roster 라인)"),
    61: (0.6, "리사이탈 요약 보고 관리로 명확 (Report 라인 준용)"),
    62: (0.6, "오디션 확정 확인 관리로 명확 (Confirmation 라인)"),
    65: (0.6, "코드 생성기로 명확 - 실재 도구"),
    68: (0.6, "합주단 의상·자산 재고 관리로 명확 (Inventory 라인)"),
    71: (0.6, "부동산 증서 거래 평가로 명확 (Evaluation 라인)"),
    72: (0.6, "보험계약자 확인 설문으로 명확"),
    75: (0.6, "메일룸 운영 요건 관리로 명확"),
    85: (0.6, "매물 위치 지도 관리로 명확 (Map 라인)"),
    87: (0.6, "리듬 연습 스튜디오 관리로 명확 (Booth·Studio 라인)"),
    90: (0.6, "행사 등록 평가로 명확 - 행사 실무 (Evaluation 라인)"),
    91: (0.6, "환자 진료 요건 관리로 명확"),
    96: (0.6, "드럼 연주 매뉴얼 관리로 명확 (Manual 라인)"),
    99: (0.6, "변전소 점검 평가로 명확 - 전력 실무 (Evaluation 라인)"),
    102: (0.6, "방송 요건 관리로 명확"),
    105: (0.6, "첼로 연습 점검 관리로 명확 (Check 라인)"),
    108: (0.6, "클라리넷 수강 갱신 관리로 명확 (Renewal 라인)"),
    109: (0.6, "베이스 후속 조치 관리로 명확 (Followup 라인)"),
    110: (0.6, "패러리걸 업무 평가로 명확 - 법무 실무 (Evaluation 라인)"),
    111: (0.6, "택배 확인 설문으로 명확"),
    113: (0.6, "초과근무 요건 관리로 명확"),
    116: (0.6, "발렛 운행 차량 손상 위험 관리로 명확 - 물리 위험 실존"),
    122: (0.6, "오보에 예약 확인 관리로 명확 (Confirmation 라인)"),
    126: (0.6, "만돌린 연습 리뷰 관리로 명확 (Review 라인)"),
    128: (0.6, "헤드헌터 성과 평가로 명확 - 채용 실무 (Evaluation 라인)"),
    129: (0.6, "굿즈 확인 설문으로 명확"),
    139: (0.6, "연습 알림 관리로 명확 (Alert 라인)"),
    140: (0.6, "리사이탈 일정 타임라인 관리로 명확 (Calendar 라인 준용)"),
    144: (0.6, "코드 녹음·기록 도구로 명확 (Recorder 라인)"),
    150: (0.6, "유조선 운송 평가로 명확 - 물류 실무 (Evaluation 라인)"),
    151: (0.6, "증서 확인 설문으로 명확"),
    154: (0.6, "분유 요건 관리로 명확"),
    169: (0.6, "등록 확인 설문으로 명확"),
    172: (0.6, "건반 음역 지도 관리로 명확 (Map 라인)"),
    175: (0.6, "드럼 연습 워크시트 관리로 명확 (Worksheet 라인)"),
    178: (0.6, "농약 적합성 평가로 명확 - 농업 실무 (Evaluation 라인)"),
    179: (0.6, "변전소 확인 설문으로 명확"),
    181: (0.6, "참여 목표 요건 관리로 명확"),
    188: (0.6, "클라리넷 레슨 견적 관리로 명확 (Quote 라인)"),
    189: (0.6, "베이스 레슨 예약 승인 관리로 명확 (Approval 라인)"),
    190: (0.6, "배당 정책·수익 평가로 명확 - 금융 실무 (Evaluation 라인)"),
    191: (0.6, "패러리걸 확인 설문으로 명확"),
    193: (0.6, "연금 가입 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "집안일에 튜너 결합 불성립",
    2: "교법 흐름 결합은 Flow 추상 불성립",
    3: "캠프 컴퍼스 결합은 Compass 추상 불성립",
    4: "합창 신호 결합은 Signal 불성립",
    5: "퇴직 범위 결합은 Scope 불명확",
    6: "오케스트라 파도 결합은 Wave 추상 불성립",
    7: "유산 포인트 결합은 Point 불성립",
    8: "멜로디 베이스 결합은 Base 추상 불성립",
    9: "리듬 데크 결합은 Deck 불성립",
    10: "비트 터미널 결합은 Terminal 불성립",
    11: "피치 콘솔 결합은 Console 도구형 불성립",
    12: "환자 혜택 결합은 Benefit 추상 불명확",
    13: "등록 감가상각 결합 불성립",
    14: "피아노 경로 결합은 Path 추상 불성립",
    15: "기타 통 결합은 Bin 불성립",
    17: "드럼 라벨 결합은 Label 불성립",
    19: "우쿨렐레 밝기 결합은 Brightness 속성어 불성립",
    21: "참여 활용률 결합 불성립 - Utilization",
    22: "방송 혜택 결합은 Benefit 추상 불명확",
    23: "롤백에 위험 결합 불성립",
    24: "스크리닝에 튜너 결합 불성립",
    25: "플루트 역 결합은 Station 불성립",
    26: "첼로 시트 결합은 Sheet 다의어 불명확",
    27: "색소폰 대출 결합은 Loan 다의어 불명확",
    28: "트럼펫 개수 결합은 Count 불성립",
    30: "베이스 접수 결합은 Reception 불성립",
    32: "연금 활용률 결합 불성립 - Utilization",
    33: "초과근무 혜택 결합은 Benefit 추상 불명확",
    35: "바코드 감가상각 결합 불성립",
    36: "발렛 사직 결합은 Resignation 불성립",
    37: "숙제에 위험 결합 불성립",
    38: "용접에 보증인 결합 불성립",
    39: "트랙터에 튜너 결합 불성립",
    40: "오르간 궤도 결합은 Rail 불성립",
    41: "검인 반지 결합은 Ring 불성립",
    43: "오보에 탄원 결합은 Petition 불성립",
    44: "비올라 분야 결합은 Field 다의어 불명확",
    45: "트롬본 메시지 결합은 Message 불성립",
    47: "만돌린 인장 결합은 Seal 불성립",
    48: "아코디언 호환성 결합은 Compatibility 불성립",
    50: "진드기 활용률 결합 불성립 - Utilization",
    51: "어금니 혜택 결합은 Benefit 추상 불명확",
    53: "제품 감가상각 결합 불성립",
    54: "투약 사직 결합은 Resignation 불성립",
    55: "점화 장치 위험 결합은 부속 장치라 대상 불성립",
    56: "림에 보증인 결합 불성립",
    57: "관용구에 튜너 결합 불성립",
    58: "하모니카 비컨 결합은 Beacon 추상 불성립",
    59: "레슨 흔적 결합은 Trail 불성립",
    63: "조율 번호 결합은 Number 불성립",
    64: "이론 상환 결합은 Redemption 불성립",
    66: "템포 기간 결합은 Duration 속성어 불성립",
    67: "레퍼토리 청구서 결합은 불성립",
    69: "반주자 와트 결합은 Wattage 불성립",
    70: "메트로놈 접수 결합은 Reception 불성립",
    73: "상판 활용률 결합 불성립 - Utilization",
    74: "분유 혜택 결합은 Benefit 추상 불명확",
    76: "곡집 감가상각 결합 불성립",
    77: "스트레칭 사직 결합은 Resignation 불성립",
    78: "파산에 위험 결합 불성립",
    79: "석조에 튜너 결합 불성립",
    80: "교법 허브 결합은 Hub 추상 불성립",
    81: "캠프 비컨 결합은 Beacon 추상 불성립",
    82: "합창 감시 결합은 Watch 도구형 기각 라인",
    83: "퇴직 루프 결합은 Loop 추상 불성립",
    84: "오케스트라 경로 결합은 Path 추상 불성립",
    86: "멜로디 코어 결합은 Core 불성립",
    88: "비트 센터 결합은 Center 불성립",
    89: "피치 패널 결합은 Panel 불성립",
    92: "등록 사직 결합은 Resignation 불성립",
    93: "피아노 포인트 결합은 Point 불성립",
    94: "기타 여권 결합은 Passport 기각 라인",
    95: "바이올린 회고 결합은 Recap 불성립",
    97: "보컬 검증 결합은 Validation 불성립",
    98: "우쿨렐레 빈도 결합은 Frequency 속성어 불성립",
    100: "기록물 활용률 결합 불성립 - Utilization",
    101: "참여 혜택 결합은 Benefit 추상 불명확",
    103: "롤백에 보증인 결합 불성립",
    104: "플루트 터미널 결합은 Terminal 불성립",
    106: "색소폰 합계 결합은 Sum 불성립",
    107: "트럼펫 메시지 결합은 Message 불성립",
    112: "연금 혜택 결합은 Benefit 추상 불명확",
    114: "비계 감가상각 결합 불성립",
    115: "바코드 사직 결합 불성립",
    117: "숙제에 보증인 결합 불성립",
    118: "용접에 튜너 결합 불성립",
    119: "오르간 흔적 결합은 Trail 불성립",
    120: "검인 관문 결합은 Gate 불성립",
    121: "하프 태그 결합은 Tag 불성립",
    123: "비올라 형식 결합은 Format 불성립",
    124: "트롬본 합계 결합은 Total 불성립",
    125: "타액에 승인 결합 불성립 - 승인 대상 불성립",
    127: "아코디언 용량 결합은 Capacity 속성어 불성립",
    130: "진드기 혜택 결합은 Benefit 추상 불명확",
    131: "어금니 요건 결합은 요건 대상 불성립",
    132: "장난감 감가상각 결합 불성립",
    133: "제품 사직 결합은 Resignation 불성립",
    134: "투약에 위험 결합 불성립",
    135: "점화 장치에 보증인 결합 불성립",
    136: "림에 튜너 결합 불성립",
    137: "하모니카 대장간 결합은 Forge 불성립",
    138: "레슨 사슬 결합은 Chain 불성립",
    141: "오디션 회고 결합은 Recap 불성립",
    142: "조율 버전 결합은 Version 속성어 불성립",
    143: "이론 연장 결합은 Extension 불성립",
    145: "템포 음량 결합은 Volume 속성어 불성립",
    146: "레퍼토리 갱신 결합은 불성립",
    147: "합주 청구 결합은 Claim 다의어 불명확",
    148: "반주자 밝기 결합은 Brightness 속성어 불성립",
    149: "메트로놈 후속 결합은 불성립",
    152: "계약자 활용률 결합 불성립 - Utilization",
    153: "상판 혜택 결합은 Benefit 추상 불명확",
    155: "메일룸 감가상각 결합 불성립",
    156: "곡집 사직 결합은 Resignation 불성립",
    157: "스트레칭에 위험 결합 불성립",
    158: "파산에 보증인 결합 불성립",
    159: "교법 데스크 결합은 Desk 추상 불성립",
    160: "캠프 대장간 결합은 Forge 불성립",
    161: "합창 범위 결합은 Scope 불명확",
    162: "퇴직 격자 결합은 Grid 추상 불성립",
    163: "오케스트라 포인트 결합은 Point 불성립",
    164: "유산 틀 결합은 Frame 불성립",
    165: "멜로디 장부 결합은 Ledger 불성립 - Lesson 수강료 장부만 성립",
    166: "리듬 실험실 결합은 Lab 불성립",
    167: "비트 구역 결합은 Zone 불성립",
    168: "피치 규모·음계 결합은 Scale 다의어 불명확",
    170: "환자 감가상각 결합 불성립",
    171: "등록에 위험 결합 불성립",
    173: "기타 로비 결합은 Lobby 불성립",
    174: "바이올린 항목·입장 결합은 Entry 다의어 불명확",
    176: "보컬 조회 결합은 Lookup 불성립",
    177: "우쿨렐레 호환성 결합은 Compatibility 불성립",
    180: "기록물 혜택 결합은 Benefit 추상 불명확",
    182: "방송 감가상각 결합 불성립",
    183: "롤백에 튜너 결합 불성립",
    184: "플루트 센터 결합은 Center 불성립",
    185: "첼로 악보·채점 결합은 Score 다의어 - 악보로 오독 위험",
    186: "색소폰 부채 결합은 Debt 기각 라인",
    187: "트럼펫 합계 결합은 Total 불성립",
    192: "택배 활용률 결합 불성립 - Utilization",
    194: "초과근무 감가상각 결합 불성립",
    195: "비계 사직 결합은 Resignation 불성립",
    196: "바코드 위험 결합 불성립",
    197: "발렛에 보증인 결합 불성립",
    198: "숙제에 튜너 결합 불성립",
    199: "오르간 사슬 결합은 Chain 불성립",
    200: "검인 연결점 결합은 Nexus 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 53, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 147, len(REJECT_REASON)
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
