import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk25_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk25_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "트롬본 진도 관리로 명확 (Progress 라인)"),
    6: (0.6, "채용 평가로 명확 - 채용 실무 (Evaluation 라인)"),
    7: (0.6, "랜야드 확인 설문으로 명확"),
    9: (0.6, "잇몸 관리 요건 관리로 명확 (Requirement 라인)"),
    21: (0.6, "조율 절차 도식 관리로 명확 (Schematic 라인)"),
    27: (0.6, "리모델링 상태 평가로 명확 - 부동산 실무 (Evaluation 라인)"),
    28: (0.6, "보상 조정 확인 설문으로 명확"),
    41: (0.6, "오케스트라 일정 모니터링 관리로 명확 (Monitor 라인)"),
    42: (0.6, "유산 사건 대장 관리로 명확 (Register 라인)"),
    43: (0.6, "멜로디 연습 일지 관리로 명확 (Journal 라인)"),
    45: (0.6, "비트 녹음 부스 예약 관리로 명확 (Booth 라인)"),
    48: (0.6, "기타 레슨 영수증 관리로 명확 (Receipt 라인)"),
    51: (0.6, "보컬 레슨 온보딩 관리로 명확 (Onboarding 라인)"),
    52: (0.6, "요금 확인 설문으로 명확"),
    55: (0.6, "조제 요건 관리로 명확 (Requirement 라인)"),
    60: (0.6, "첼로 정산 명세 관리로 명확 (Statement 라인)"),
    62: (0.6, "트럼펫 진도 관리로 명확 (Progress 라인)"),
    74: (0.6, "고객 감성 평가로 명확 - 고객지원 실무 (Evaluation 라인)"),
    75: (0.6, "채용 확인 설문으로 명확"),
    77: (0.6, "벼룩 관리 요건 관리로 명확 (Requirement 라인)"),
    86: (0.6, "연습 비용 견적 관리로 명확 (Estimate 라인)"),
    87: (0.6, "리사이탈 계획 관리로 명확 (Plan 라인)"),
    90: (0.6, "이론 연속 학습 기록 관리로 명확 (Streak 라인)"),
    94: (0.6, "합주 팔로업 관리로 명확 (Followup 라인)"),
    95: (0.6, "냉장 컨테이너 상태 평가로 명확 - 물류 실무 (Evaluation 라인)"),
    96: (0.6, "리모델링 확인 설문으로 명확"),
    99: (0.6, "파티오 요건 관리로 명확 (Requirement 라인)"),
    109: (0.6, "퇴직 설계 플래너로 실존 서비스 (Planner 라인)"),
    112: (0.6, "멜로디 기록 등록부 관리로 명확 (Registry 라인)"),
    115: (0.6, "피치 출석 명부 관리로 명확 (Roster 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "오보에 속성 결합은 Attribute 속성어 불성립",
    2: "비올라 메시지 결합은 Message 불성립",
    4: "타액 인장 결합은 Seal 불성립",
    5: "만돌린 용량 결합은 Capacity 속성어 불성립",
    8: "벼룩 혜택 결합은 Benefit 추상 불명확",
    10: "공예 감가상각 결합 불성립",
    11: "식기세척기 사직 결합은 Resignation 불성립",
    12: "블로우아웃에 위험 결합 불성립",
    13: "흡입기에 보증인 결합 불성립",
    14: "제습기에 튜너 결합 불성립",
    15: "아코디언 연쇄 결합은 Cascade 추상 불성립",
    16: "하모니카 링 결합은 Ring 불성립",
    17: "레슨 상자 결합은 Bin 불성립",
    18: "연습 티켓 결합은 Ticket 불명확",
    19: "리사이탈 단위 결합은 Unit 속성어 불성립",
    20: "오디션 분야 결합은 Field 불성립",
    22: "이론 결과 결합은 Result 불명확",
    23: "코드 계정 결합은 불성립",
    24: "템포 검증 결합은 Verification 기각 라인",
    25: "레퍼토리 시간 결합은 Time 속성어 불성립",
    26: "합주 접수 결합은 Reception 다의어 불명확",
    29: "교육 활용률 결합 불성립 - Utilization",
    30: "파티오 혜택 결합은 Benefit 추상 불명확",
    31: "기능 사직 결합은 Resignation 불성립",
    32: "적성에 위험 결합 불성립",
    33: "반주자 나침반 결합은 Compass 추상 불성립",
    34: "메트로놈 포인트 결합은 Point 불성립",
    35: "증서 핵심 결합은 Core 불성립",
    36: "곡집 실험실 결합은 Lab 불성립",
    37: "교법 패널 결합은 Panel 불성립",
    38: "캠프 링 결합은 Ring 불성립",
    39: "합창 관리자 결합은 Manager 불성립",
    40: "퇴직 조수 결합은 Assistant 불명확 기각 라인",
    44: "리듬 검색기 결합은 Locator/Finder 불성립",
    46: "피치 항구 결합은 Harbor 불성립",
    47: "피아노 동반자 결합은 Companion 불명확 기각 라인",
    49: "바이올린 형식 결합은 Format 불성립",
    50: "드럼 제안 결합은 Proposal 불명확",
    53: "묘지 활용률 결합 불성립 - Utilization",
    54: "수수료 혜택 결합은 Benefit 추상 불명확",
    56: "여과에 보증인 결합 불성립",
    57: "마스터키에 튜너 결합 불성립",
    58: "우쿨렐레 대장간 결합은 Forge 불성립",
    59: "플루트 카운터 결합은 Counter 다의어 불명확",
    61: "색소폰 할인 결합은 Discount 기각 라인",
    63: "클라리넷 속도 결합은 Speed 속성어 불성립",
    64: "이정표에 위험 결합 불성립",
    65: "베이스에 지도 결합은 불성립 (Method Map 기각 선례 준용)",
    66: "오르간 상자 결합은 Bin 불성립",
    67: "검인 전광판 결합은 Ticker 불성립",
    68: "하프 타브악보로 오독하는 Tab 결합은 불명확",
    69: "오보에 분야 결합은 Field 불성립",
    70: "비올라 합계 결합은 Total 기각 라인",
    71: "트롬본 사용 승인 결합은 불성립",
    72: "타액 리뷰 결합은 후기/검토 다의어 불명확",
    73: "만돌린 사용량 결합은 Usage 속성어 불성립",
    76: "랜야드 활용률 결합 불성립 - Utilization",
    78: "잇몸 감가상각 결합 불성립",
    79: "공예 사직 결합은 Resignation 불성립",
    80: "식기세척기에 위험 결합 불성립",
    81: "블로우아웃에 보증인 결합 불성립",
    82: "흡입기에 튜너 결합 불성립",
    83: "아코디언 브리지 결합은 Bridge 추상 불성립",
    84: "하모니카 관문 결합은 Gate 불성립",
    85: "레슨 여권 결합은 Passport 불성립",
    88: "오디션 형식 결합은 Format 불성립",
    89: "조율 배치도 결합은 Layout 불성립",
    91: "코드 사례 결합은 Case 다의어 불명확",
    92: "템포 시뮬레이터 결합은 불성립",
    93: "레퍼토리 속도 결합은 Speed 속성어 불성립",
    97: "보상 조정 활용률 결합 불성립 - Utilization",
    98: "교육 혜택 결합은 Benefit 추상 불명확",
    100: "기능에 위험 결합 불성립",
    101: "적성에 보증인 결합 불성립",
    102: "반주자 등대 결합은 Beacon 추상 불성립",
    103: "메트로놈에 지도 결합은 불성립",
    104: "증서 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    105: "곡집 스테이션 결합은 Station 불성립",
    106: "교법 저울 결합은 Scale 다의어 불명확",
    107: "캠프 관문 결합은 Gate 불성립",
    108: "합창 엔진 결합은 Engine 추상 불성립",
    110: "오케스트라 동반자 결합은 Companion 불명확 기각 라인",
    111: "유산 운영 결합은 Ops 불명확",
    113: "리듬 검색기 결합은 Finder 불성립",
    114: "비트 키오스크 결합은 Kiosk 불성립",
}

n = len(req["items"])
assert n == 115, n
assert len(APPROVE) == 30, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 85, len(REJECT_REASON)
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
