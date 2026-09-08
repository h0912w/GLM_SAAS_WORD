import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk23_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk23_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "음악이론 오답 탐지기로 실재 도구 (Detector 라인)"),
    7: (0.6, "미디어 기능(피처) 평가로 명확 - 미디어 실무 (Evaluation 라인)"),
    8: (0.6, "적성 확인 설문으로 명확"),
    9: (0.6, "식단 요건 관리로 명확 (Requirement 라인)"),
    24: (0.6, "멜로디 작업 스케줄러로 명확 (Scheduler 라인)"),
    26: (0.6, "비트 연습 캘린더로 명확 (Calendar 라인)"),
    27: (0.6, "피치 연습 사무 관리로 명확 (Office 라인)"),
    31: (0.6, "기타 연습 리마인더로 명확 (Reminder 라인)"),
    33: (0.6, "드럼 공연 무대 준비 관리로 명확 (Stage 물리공간 라인)"),
    34: (0.6, "보컬 연습 일지 관리로 명확 (Diary 라인)"),
    37: (0.6, "용어 요건 관리로 명확 (Requirement 라인)"),
    42: (0.6, "플루트 기록 등록부 관리로 명확 (Registry 라인)"),
    45: (0.6, "트럼펫 레퍼런스 관리로 명확 (Reference 라인)"),
    47: (0.6, "발달 이정표 확인 설문으로 명확"),
    52: (0.6, "검인 사건 명부 관리로 명확 (Roster 라인, Probate 기록물형)"),
    53: (0.6, "하프 레슨 바우처 관리로 명확 (Voucher 라인)"),
    59: (0.6, "아동 공예 활동 평가로 명확 - 육아 실무 (Evaluation 라인)"),
    60: (0.6, "식기세척기 확인 설문으로 명확"),
    63: (0.6, "제습기 요건 관리로 명확 (Requirement 라인)"),
    71: (0.6, "리사이탈 확정 관리로 명확 (Confirmation 라인)"),
    74: (0.6, "이론 연습 타이머로 실재 도구 (Timer 라인)"),
    75: (0.6, "코드 연습 템플릿 관리로 명확 (Template 라인)"),
    79: (0.6, "기능 확인 설문으로 명확"),
    95: (0.6, "멜로디 연습 모니터링 관리로 명확 (Monitor 라인)"),
    96: (0.6, "리듬 연습 플레이북 관리로 명확 (Playbook 라인)"),
    97: (0.6, "비트 기록 디렉터리 관리로 명확 (Directory 라인)"),
    99: (0.6, "화물 취급 위험 관리로 명확 - 낙하·파손 위험 실존 (Hazard 물리위험 라인)"),
    105: (0.6, "보컬 레슨 환불 관리로 명확 (Refund 라인)"),
    107: (0.6, "마스터키 시공 요건 관리로 명확 (Requirement 라인)"),
    112: (0.6, "플루트 레슨 캘린더로 명확 (Calendar 라인)"),
    122: (0.6, "검인 기한 알림 관리로 명확 (Alert 라인, Probate 기한형)"),
    123: (0.6, "하프 레슨 배지 관리로 명확 (Badge 라인)"),
    126: (0.6, "트롬본 공연 마감 관리로 명확 (Deadline 라인)"),
    127: (0.6, "타액 레슨 결제 관리로 명확 (Payment 라인)"),
    129: (0.6, "잇몸·치은 평가로 명확 - 치과 실무 (Evaluation 라인)"),
    130: (0.6, "공예 확인 설문으로 명확"),
    133: (0.6, "흡입기 요건 관리로 명확 (Requirement 라인)"),
    140: (0.6, "연습 요약 관리로 명확 (Summary 라인)"),
    144: (0.6, "이론 워크숍 관리로 명확 (Workshop 라인)"),
    145: (0.6, "코드 가이드 관리로 명확 (Guide 라인)"),
    164: (0.6, "유산 설계 플래너로 실존 서비스 (Planner 라인)"),
    166: (0.6, "리듬 연습 일지 관리로 명확 (Journal 라인)"),
    168: (0.6, "피치 녹음 부스 예약 관리로 명확 (Booth 라인)"),
    173: (0.6, "드럼 연속 연습 기록 관리로 명확 (Streak 라인)"),
    174: (0.6, "보컬 레슨 비용 관리로 명확 (Expense 라인)"),
    175: (0.6, "약제 조제 평가로 명확 - 약국 실무 (Evaluation 라인)"),
    176: (0.6, "여과 요건 관리로 명확 (Requirement 라인)"),
    182: (0.6, "플루트 기록 디렉터리 관리로 명확 (Directory 라인)"),
    185: (0.6, "트럼펫 공연 마감 관리로 명확 (Deadline 라인)"),
    192: (0.6, "검인 절차 차트 관리로 명확 (Chart 라인, Probate 기록물형)"),
    195: (0.6, "비올라 레슨 알림 관리로 명확 (Notification 라인)"),
    199: (0.6, "반려동물 벼룩 진단 평가로 명확 - 수의 실무 (Evaluation 라인)"),
    200: (0.6, "잇몸 확인 설문으로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "조율 체험 결합은 Trial 기각 라인",
    10: "교정 감가상각 결합 불성립",
    3: "코드 사용 승인 결합은 불성립",
    4: "템포에 예약금 결합 불성립",
    5: "레퍼토리 무게 결합은 Weight 속성어 불성립",
    6: "합주 상태 결합은 Condition 속성어 불성립",
    11: "유모차 사직 결합은 Resignation 불성립",
    12: "스파에 위험 결합은 서비스 대상 불성립",
    13: "연석에 튜너 결합 불성립",
    14: "반주자 흐름 결합은 Flow 불성립",
    15: "메트로놈 시계로 오독하는 Watch 결합은 불성립",
    16: "증서 파도 결합은 Wave 추상 불성립",
    17: "곡집 거점 결합은 Base 불성립",
    18: "교법 스테이션 결합은 Station 불성립",
    19: "캠프 패널 결합은 Panel 불성립",
    20: "합창 체인 결합은 Chain 추상 불성립",
    21: "퇴직 관문 결합은 Gate 불성립",
    22: "오케스트라 관리자 결합은 Keeper 불명확 기각 라인",
    23: "유산 엔진 결합은 Engine 추상 불성립",
    25: "리듬 운영 결합은 Ops 불명확",
    28: "화물 사직 결합은 Resignation 불성립",
    29: "정책에 보증인 결합 불성립",
    30: "피아노 관리자 결합은 Manager 불성립",
    32: "바이올린 규칙 결합은 Rule 불성립",
    35: "여과 활용률 결합 불성립 - Utilization",
    36: "마스터키 혜택 결합은 Benefit 추상 불명확",
    38: "갤러리 사직 결합은 Resignation 불성립",
    39: "꽃집에 위험 결합 불성립",
    40: "라이너에 튜너 결합 불성립",
    41: "우쿨렐레 책상 결합은 Desk 불성립",
    43: "첼로 샘플 결합은 Sample 다의어 불명확",
    44: "색소폰 저울·잔액 결합은 Balance 다의어 불명확",
    46: "클라리넷 거리 결합은 Distance 속성어 불성립",
    48: "수선 사직 결합은 Resignation 불성립",
    49: "추모식에 위험 결합 불성립",
    50: "베이스 범위 결합은 Scope 불성립",
    51: "오르간 구역 결합은 Bay 불성립",
    54: "오보에 링크 결합은 Link 불성립",
    55: "비올라 개요 결합은 Outline 불성립",
    56: "트롬본 예측 결합은 Forecast 불성립",
    57: "타액 수정 결합은 Revision 기각 라인",
    58: "만돌린 전압 결합은 Voltage 속성어 불성립",
    61: "블로우아웃 활용률 결합 불성립 - Utilization",
    62: "흡입기 혜택 결합은 Benefit 추상 불명확",
    64: "자물쇠 홈 감가상각 결합 불성립",
    65: "구문 사직 결합은 Resignation 불성립",
    66: "케이크에 튜너 결합 불성립",
    67: "아코디언 릴레이 결합은 Relay 불성립",
    68: "하모니카 저울 결합은 Scale 다의어 불명확",
    69: "레슨 게시물 결합은 Post 다의어 불명확",
    70: "연습 초안 결합은 Draft 다의어 불명확",
    72: "오디션 규칙 결합은 Rule 불성립",
    73: "조율 그래프 결합은 Graph 불성립",
    76: "템포에 인증 결합 불성립",
    77: "레퍼토리 거리 결합은 Distance 속성어 불성립",
    78: "합주 습도 결합은 Humidity 속성어 불성립",
    80: "적성 활용률 결합 불성립 - Utilization",
    81: "식이 감가상각 결합 불성립",
    82: "교정 사직 결합은 Resignation 불성립",
    83: "유모차에 위험 결합은 서비스 대상 불성립",
    84: "스파에 보증인 결합 불성립",
    85: "반주자 허브 결합은 Hub 추상 불성립",
    86: "메트로놈 범위 결합은 Scope 불성립",
    87: "증서 경로 결합은 Path 추상 불성립",
    88: "곡집 핵심 결합은 Core 불성립",
    89: "교법 터미널 결합은 Terminal 불성립",
    90: "캠프 저울 결합은 Scale 다의어 불명확",
    91: "합창 링 결합은 Ring 불성립",
    92: "퇴직 연결점 결합은 Nexus 추상 불성립",
    93: "오케스트라 관리자 결합은 Manager 불성립",
    94: "유산 조수 결합은 Assistant 불명확 기각 라인",
    98: "피치 카운터 결합은 Counter 다의어 불명확",
    100: "정책에 튜너 결합 불성립",
    101: "피아노 엔진 결합은 Engine 추상 불성립",
    102: "기타 색인 결합은 Index 다의어 불명확",
    103: "바이올린 세부 결합은 Detail 속성어 불성립",
    104: "드럼 결과 결합은 Result 불명확",
    106: "여과 혜택 결합은 Benefit 추상 불명확",
    108: "용어 감가상각 결합 불성립",
    109: "갤러리에 위험 결합은 서비스 대상 불성립",
    110: "꽃집에 보증인 결합 불성립",
    111: "우쿨렐레 레이더 결합은 Radar 추상 불성립",
    113: "첼로 슬롯 결합은 Slot 불성립",
    114: "색소폰 이자·관심 결합은 Interest 다의어 불명확",
    115: "트럼펫 예측 결합은 Forecast 불성립",
    116: "클라리넷 범위 결합은 Range 속성어 불성립",
    117: "이정표 활용률 결합 불성립 - Utilization",
    118: "수선에 위험 결합 불성립",
    119: "추모식에 보증인 결합 불성립",
    120: "베이스 순환 결합은 Loop 불성립",
    121: "오르간 게시물 결합은 Post 다의어 불명확",
    124: "오보에 규칙 결합은 Rule 불성립",
    125: "비올라 렌더링 결합은 Rendering 불성립",
    128: "만돌린 와트 결합은 Wattage 속성어 불성립",
    131: "식기세척기 활용률 결합 불성립 - Utilization",
    132: "블로우아웃 혜택 결합은 Benefit 추상 불명확",
    134: "제습기 감가상각 결합 불성립",
    135: "자물쇠 홈 사직 결합은 Resignation 불성립",
    136: "구문에 위험 결합 불성립",
    137: "아코디언 금고 결합은 Vault 불성립",
    138: "하모니카 경로 결합은 Route 불성립",
    139: "레슨 항구 결합은 Harbor 불성립",
    141: "리사이탈 요약 재현 결합은 Recap 기각 라인",
    142: "오디션 세부 결합은 Detail 속성어 불성립",
    143: "조율 라벨 결합은 Label 불성립",
    146: "템포에 지명 결합 불성립",
    147: "레퍼토리 범위 결합은 Range 속성어 불성립",
    148: "합주 에피소드 결합은 Episode 불성립",
    149: "기능 활용률 결합 불성립 - Utilization",
    150: "적성 혜택 결합은 Benefit 추상 불명확",
    151: "식이 사직 결합은 Resignation 불성립",
    152: "교정에 위험 결합 불성립",
    153: "유모차에 보증인 결합 불성립",
    154: "스파에 튜너 결합 불성립",
    155: "반주자 책상 결합은 Desk 불성립",
    156: "메트로놈 순환 결합은 Loop 불성립",
    157: "증서 포인트 결합은 Point 불성립",
    158: "곡집 장부 결합은 Ledger가 Lesson 수강료 장부만 승인",
    159: "교법 센터 결합은 Center 불성립",
    160: "캠프 경로 결합은 Route 불성립",
    161: "합창 관문 결합은 Gate 불성립",
    162: "퇴직 대성지도 결합은 Atlas 추상 불성립",
    163: "오케스트라 엔진 결합은 Engine 추상 불성립",
    165: "멜로디 동반자 결합은 Companion 불명확 기각 라인",
    167: "비트 검색기 결합은 Locator/Finder 불성립",
    169: "화물에 보증인 결합 불성립",
    170: "피아노 조수 결합은 Assistant 불명확 기각 라인",
    171: "기타 티켓 결합은 Ticket 불명확",
    172: "바이올린 식별자 결합은 Identifier 불성립",
    177: "마스터키 감가상각 결합 불성립",
    178: "용어 사직 결합은 Resignation 불성립",
    179: "갤러리에 보증인 결합 불성립",
    180: "꽃집에 튜너 결합 불성립",
    181: "우쿨렐레 릴레이 결합은 Relay 불성립",
    183: "첼로 통과 결합은 Pass 기각 라인",
    184: "색소폰 자산 결합은 Asset 불성립",
    186: "클라리넷 한도 결합은 Limit 속성어 불성립",
    187: "이정표 혜택 결합은 Benefit 추상 불명확",
    188: "수선에 보증인 결합 불성립",
    189: "추모식에 튜너 결합 불성립",
    190: "베이스 격자 결합은 Grid 불성립",
    191: "오르간 항구 결합은 Harbor 불성립",
    193: "하프 보관 즉시 결제 증서 결합은 Stub 불성립",
    194: "오보에 세부 결합은 Detail 속성어 불성립",
    196: "트롬본 지속시간 결합은 Duration 불성립",
    197: "타액 검증 결합은 Verification 기각 라인",
    198: "만돌린 밝기 결합은 Brightness 불성립",
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
