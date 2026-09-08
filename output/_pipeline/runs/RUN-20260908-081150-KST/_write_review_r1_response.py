import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "팰콘 장부는 맹금류 이름 도메인 결합 성립 - 카나리아"),
    2: (0.6, "양자 공증은 기술 수식어+실제 서비스 결합 성립 - 카나리아"),
    6: (0.6, "장부 파수 도구는 Sentinel 독립 감시 은유 성립 - 카나리아"),
    7: (0.6, "장부 파수꾼은 Watchman 독립 감시 은유 성립 - 카나리아"),
    8: (0.6, "피아노 음역 레지스터 관리는 실제 음악 용어 - register 실제 음악 의미"),
    11: (0.6, "드럼 악기 보증 관리는 실제 악기 판매 운영 항목 - Guarantee 라인(Roofing Guarantee 정합)"),
    13: (0.6, "유지보수 상태 평가는 실제 조경 운영 항목 - Evaluation 신규 기능어 실재 결합"),
    14: (0.6, "점검용 설문 양식은 실제 청소 운영 문서 - Questionnaire 신규 기능어 실재 결합"),
    20: (0.6, "연료 위험 관리는 실제 항공 안전 운영 항목 - Hazard 신규 기능어 실재 결합"),
    29: (0.6, "콜백 처리 평가는 실제 고객지원 운영 항목 - Evaluation 라인(Maintenance Evaluation 정합)"),
    30: (0.6, "추천 후보 설문은 실제 채용 운영 문서 - Questionnaire 라인(Inspection Questionnaire 정합)"),
    33: (0.6, "프랜차이즈 가맹 요건 관리는 실제 외식 운영 항목 - Requirement 신규 기능어 실재 결합"),
    48: (0.6, "자막 품질 평가는 실제 미디어 운영 항목 - Evaluation 라인(Callback Evaluation 정합)"),
    50: (0.6, "리크루터 가동률 관리는 실제 채용 운영 지표 - Utilization 신규 기능어 실재 결합"),
    52: (0.6, "차량 점검 요건 관리는 실제 자동차 운영 항목 - Requirement 라인(Franchise Requirement 정합)"),
    55: (0.6, "공작 활동 위험 관리는 실제 육아 안전 운영 항목 - Hazard 라인(Fuel Hazard 정합)"),
    70: (0.6, "채권자 신용 평가는 실제 금융 심사 운영 항목 - Evaluation 라인 실재 결합"),
    74: (0.6, "교육 이수 요건 관리는 실제 인사 운영 항목 - Requirement 라인 실재 결합"),
    86: (0.6, "성가대 운영 도우미는 실제 음악 단체 관리 항목 - Assistant 라인(Stock Assistant 정합)"),
    88: (0.6, "오케스트라 단원 명부는 실제 음악 단체 운영 문서 - Register 라인(Immunization Register 정합)"),
    89: (0.6, "상속 재산 정리 플레이북은 실제 금융·법률 문서 - Playbook 라인(Estate Playbook 법률 문맥 성립)"),
    97: (0.6, "드럼 연습 기록 관리는 실제 음악 학습 운영 항목 - Record 라인(Roofing Record 정합)"),
    99: (0.6, "방역 약품 평가는 실제 방역 운영 항목 - Evaluation 라인 실재 결합"),
    100: (0.6, "유지보수 만족도 설문은 실제 조경 운영 문서 - Questionnaire 라인 실재 결합"),
    103: (0.6, "묘지 이용 요건 관리는 실제 장례 운영 항목 - Requirement 라인 실재 결합"),
    106: (0.6, "용선 계약 위험 조항은 실제 해운 운영 항목 - Hazard 라인 실재(charterparty hazard)"),
    115: (0.6, "런북 품질 평가는 실제 IT 운영 항목 - Evaluation 라인 실재 결합"),
    116: (0.6, "콜백 만족도 설문은 실제 고객지원 운영 문서 - Questionnaire 라인 실재 결합"),
    119: (0.6, "차량 감정 요건 관리는 실제 자동차 운영 항목 - Requirement 라인 실재 결합"),
    122: (0.6, "X선 방사선 위험 관리는 실제 치과 안전 운영 항목 - Hazard 라인 실재 결합"),
    131: (0.6, "트롬본 선택 가이드는 실제 악기 안내 문서 - Guide 라인(Roofing Guide 정합)"),
    133: (0.6, "만돌린 보관 습도 관리는 실제 목제 악기 관리 항목 - Humidity 라인 실재(목악기 습도 관리)"),
    134: (0.6, "예산 평가는 실제 행정 운영 항목 - Evaluation 라인 실재 결합"),
    156: (0.6, "부상 평가는 실제 의료 운영 항목 - Evaluation 라인 실재 결합"),
    158: (0.6, "냉장 컨테이너 가동률은 실제 물류 운영 지표 - Utilization 라인 실재 결합"),
    159: (0.6, "리모델링 세제 혜택 관리는 실제 부동산 운영 항목 - Benefit 라인 실재 결합"),
    160: (0.6, "보상 조정 요건 관리는 실제 보험 운영 항목 - Requirement 라인 실재 결합"),
    172: (0.6, "성가대 일정 플래너는 실제 음악 단체 도구 - Planner 라인(Trading Planner 정합)"),
    173: (0.6, "은퇴 자금 감시 도구는 실제 금융 도구 - Monitor 금융 라인(Stock Monitor 정합)"),
    177: (0.6, "리듬 박자 카운터는 실제 음악 연습 도구 - Counter 라인 실재 결합"),
    185: (0.6, "보호 가족 만족 평가는 실제 시니어 케어 운영 항목 - Evaluation 라인 실재 결합"),
    192: (0.6, "약품 조제 위험 관리는 실제 약국 안전 운영 항목 - Hazard 라인 실재 결합"),
    193: (0.6, "용선 계약 보증인 관리는 실제 해운 운영 항목 - Guarantor 신규 기능어 실재(charterparty guarantor)"),
    199: (0.6, "트럼펫 선택 가이드는 실제 악기 안내 문서 - Guide 라인(Trombone Guide 정합)"),
}

DUP_REJECT = {}

REJECT_REASON = {
    3: "Slack은 협업 도구 유명 상표 - Messenger 결합 상표 유사",
    4: "Photoshop은 이미지 편집 유명 상표 - Canvas 결합 상표 유사",
    5: "Thing은 무의미 일반어로 명확성 불성립 - 카나리아",
    9: "기타 코드 표기 결합은 Code 대상 불분명(Chord와 혼동)",
    10: "바이올린 일련번호 결합은 Serial 속성 항목 불성립",
    12: "보컬 체크인 결합은 Checkin 결합 대상 불분명",
    15: "가격 책정 가동률 결합은 Pricing 속성 도메인 불성립",
    16: "묘지 수당 결합은 Benefit 결합 대상 불분명(Funeral Benefit과 달리 묘지 결합 불성립)",
    17: "커미션 요건 결합은 Commission 기각 도메인 불성립",
    18: "조제 설비 감가상각 결합은 Depreciation 결합 대상 불분명(자산 도메인 아님)",
    19: "용선 사직 결합은 Resignation 결합 불성립(계약 해지와 무관)",
    21: "교대 보증인 결합은 Guarantor 결합 대상 불분명",
    22: "필터 튜너 결합은 Tuner 조율 대상 불분명(악기·신호 조율과 무관)",
    23: "우쿨렐레 폭포 결합은 Cascade 앵커 불성립",
    24: "플루트 부스 결합은 Booth 연습실 읽기 불성립(Booth/Kiosk 기각 계열)",
    25: "첼로 메모 결합은 Memo 결합 대상 불분명(악기 도메인 메모 실무 없음)",
    26: "색소폰 연체료 결합은 Arrears 금융 라인 불성립",
    27: "트럼펫 인증 결합은 Authorization 결합 대상 불분명",
    28: "클라리넷 깊이 결합은 Depth 물리 사양 명사 불성립",
    31: "피드백 활용 결합은 Utilization 가동률 의미 불일치",
    32: "감정 혜택 결합은 Benefit 결합 대상 불분명",
    34: "퇴원 감가상각 결합은 Depreciation 결합 불성립",
    35: "X레이 사직 결합은 Resignation 결합 불성립",
    36: "운동 세션 위험 결합은 Hazard 결합 대상 약함(Fuel Hazard 연료 위험과 달리 불성립)",
    37: "이정표 보증인 결합은 Guarantor 결합 불성립",
    38: "웰니스 조율기 결합은 Tuner 결합 대상 불분명",
    39: "베이스 골조 결합은 Frame 불성립",
    40: "오르간 여권 결합은 Passport 결합 불성립",
    41: "검인 라인 결합은 Line 불성립",
    42: "하프 게시판 결합은 Bulletin 앵커 불성립",
    43: "오보에 양식 결합은 Format 결합 불성립",
    44: "비올라 위젯 결합은 Widget 기술 일반어 불성립",
    45: "트롬본 템플릿 결합은 Template 결합 대상 불분명",
    46: "타악기 레시피 결합은 Recipe 앵커 불성립",
    47: "만돌린 상태 결합은 Condition 속성 follower 불성립(설비 운영 문맥 아님)",
    49: "감정 분석 설문 결합은 Sentiment 기각 도메인 불성립",
    51: "랜야드 수당 결합은 Benefit 결합 불성립",
    53: "벼룩 감가상각 결합은 Depreciation 결합 불성립",
    54: "잇몸 사직 결합은 Resignation 결합 불성립",
    56: "식기세척기 보증인 결합은 Guarantor 결합 불성립",
    57: "블로아웃 조율기 결합은 Tuner 결합 불성립",
    58: "아코디언 신호 결합은 Signal 결합 불성립",
    59: "하모니카 결절점 결합은 Nexus 불성립",
    60: "레슨 로비 결합은 Lobby 결합 불성립",
    61: "연습 주문 결합은 Order 발주 의미 불일치",
    62: "발표회 비용 결합은 Cost 속성 항목 불성립",
    63: "오디션 일련번호 결합은 Serial 속성 불성립",
    64: "조율 스케치 결합은 Sketch 결합 불성립",
    65: "이론 순위 결합은 Rank 속성 불성립",
    66: "코드 짝 결합은 Match 앵커 불성립(Roofing Match 준용)",
    67: "템포 예측기 결합은 Predictor 결합 대상 불분명",
    68: "레퍼토리 깊이 결합은 Depth 물리 불성립",
    69: "합주단 승인 결합은 승인 대상 불분명",
    71: "냉장 컨테이너 설문 결합은 Questionnaire 결합 대상 불분명",
    72: "리노베이션 가동률 결합은 Utilization 결합 대상 불분명",
    73: "보상 조정 수당 결합은 Benefit 결합 대상 불분명",
    75: "파티오 감가상각 결합은 Depreciation 결합 대상 불분명",
    76: "전학 사직 결합은 Resignation 결합 불성립",
    77: "선거구 위험 결합은 Hazard 결합 대상 불분명",
    78: "기능 보증인 결합은 Guarantor 결합 불성립",
    79: "적성 조율기 결합은 Tuner 결합 불성립",
    80: "반주자 제련소 결합은 Forge 앵커 불성립",
    81: "메트로놈 골조 결합은 Frame 물건 불성립",
    82: "증서 게시판 결합은 Board 불성립",
    83: "곡집 터미널 결합은 Terminal 금융 도구 라인 불성립",
    84: "교본 경로 결합은 Route 불성립",
    85: "캠프 결절점 결합은 Nexus 불성립",
    87: "은퇴 일정 관리기 결합은 Scheduler 결합 대상 불분명",
    90: "멜로디 캘린더 결합은 Calendar 결합 대상 불분명",
    91: "리듬 사무실 결합은 Office 결합 불성립",
    92: "비트 보관베이 결합은 Bay 기각 계열 불성립",
    93: "음정 경보 결합은 Alert 시세·안전 라인 불일치(튜닝 앱 기능 표현 불명확)",
    94: "피아노 운영팀 결합은 Ops 결합 불성립",
    95: "기타 목록 결합은 List 결합 대상 불분명",
    96: "바이올린 토큰 결합은 Token 기술 일반어 불성립",
    98: "보컬 크기 결합은 Size 물리 사양 불성립",
    101: "점검 가동률 결합은 Utilization 결합 대상 불분명",
    102: "가격 책정 수당 결합은 Pricing 기각 도메인 불성립",
    104: "커미션 감가상각 결합은 Depreciation 결합 불성립",
    105: "조제 사직 결합은 Resignation 결합 불성립",
    107: "연료 보증인 결합은 Guarantor 결합 불성립",
    108: "교대 조율기 결합은 Tuner 결합 불성립",
    109: "우쿨렐레 브리지 결합은 Bridge 부품 물건 불성립",
    110: "플루트 키오스크 결합은 Kiosk 기각 계열 불성립",
    111: "첼로 배정량 결합은 Quota 결합 불성립",
    112: "색소폰 선급금 결합은 Advance 속성 불성립",
    113: "트럼펫 템플릿 결합은 Template 결합 대상 불분명",
    114: "클라리넷 높이 결합은 Height 물리 사양 불성립",
    117: "추천 활용률 결합은 Utilization 결합 대상 불분명",
    118: "피드백 수당 결합은 Benefit 결합 불성립",
    120: "프랜차이즈 감가상각 결합은 Depreciation 결합 대상 불분명",
    121: "퇴원 사직 결합은 Resignation 결합 불성립",
    123: "세션 보증인 결합은 Guarantor 결합 불성립",
    124: "이정표 조율기 결합은 Tuner 결합 불성립",
    125: "베이스 기반 결합은 Base 불성립",
    126: "오르간 로비 결합은 Lobby 결합 불성립",
    127: "검인 창 결합은 Window 결합 불성립",
    128: "하프 요약보고 결합은 Brief 앵커 불성립",
    129: "오보에 일련번호 결합은 Serial 속성 불성립",
    130: "비올라 저장소 결합은 Repository 기술 일반어 불성립",
    132: "타악기 영상 결합은 Video 불성립",
    135: "자막 설문 결합은 Questionnaire 결합 대상 불분명",
    136: "감정 분석 가동률 결합은 Sentiment 기각 도메인 불성립",
    137: "리크루터 수당 결합은 Benefit 결합 대상 불분명",
    138: "랜야드 요건 결합은 Requirement 결합 불성립",
    139: "점검 감가상각 결합은 Depreciation 결합 불성립",
    140: "벼룩 사직 결합은 Resignation 결합 불성립",
    141: "잇몸 위험 결합은 Hazard 결합 대상 불분명",
    142: "공작 보증인 결합은 Guarantor 결합 불성립",
    143: "식기세척기 조율기 결합은 Tuner 결합 불성립",
    144: "아코디언 감시 결합은 Watch 금융 감시 라인 불성립",
    145: "하모니카 지도집 결합은 Atlas 불성립",
    146: "레슨 티커 결합은 Ticker 금융 시세 라인 불성립",
    147: "연습 청구서 결합은 Bill 결합 대상 불분명",
    148: "발표회 가격 결합은 Price 속성 불성립",
    149: "오디션 토큰 결합은 Token 기술 일반어 불성립",
    150: "조율 개요 결합은 Outline 결합 불성립",
    151: "이론 추이 결합은 Trend 속성 불성립",
    152: "코드 검증 결합은 Validation 결합 대상 불분명",
    153: "템포 날인 결합은 Seal 결합 불성립",
    154: "레퍼토리 높이 결합은 Height 물리 불성립",
    155: "합주단 행렬 결합은 Matrix 기각 follower 불성립",
    157: "채권자 설문 결합은 Questionnaire 결합 대상 불분명",
    159.5: "",
    161: "교육 감가상각 결합은 Depreciation 결합 불성립",
    162: "파티오 사직 결합은 Resignation 결합 불성립",
    163: "전학 위험 결합은 Hazard 결합 불성립",
    164: "선거구 보증인 결합은 Guarantor 결합 불성립",
    165: "기능 조율기 결합은 Tuner 결합 불성립",
    166: "반주자 폭포 결합은 Cascade 앵커 불성립",
    167: "메트로놈 기반 결합은 Base 불성립",
    168: "증서 데크 결합은 Deck 불성립",
    169: "곡집 센터 결합은 Center 결합 불성립",
    170: "교본 레일 결합은 Rail 물리 부재 불성립",
    171: "캠프 지도집 결합은 Atlas 불성립",
    174: "오케스트라 운영팀 결합은 Ops 결합 불성립",
    175: "상속 일지 결합은 Journal 불성립(Estate Log/Record와 별개 미성립)",
    176: "멜로디 디렉터리 결합은 Directory 결합 대상 불분명",
    178: "비트 게시물 결합은 Post 기각 계열 불성립",
    179: "음정 차트 결합은 Chart 시세 라인 불일치(음악 차트 읽기 모호)",
    180: "피아노 플레이북 결합은 Playbook 교육 문맥 불성립(법률·금융 계약 문맥 한정)",
    181: "기타 코드표 결합은 Table 단독 읽기 모호(Table 라인 불성립)",
    182: "바이올린 서명 결합은 Signature 서비스 서명 라인 불일치",
    183: "드럼 사본 결합은 Copy 앵커 미확정 불성립",
    184: "보컬 길이 결합은 Length 물리 사양 불성립",
    186: "약품 설문 결합은 Questionnaire 결합 대상 불분명",
    187: "유지보수 가동률 결합은 Utilization 표준 지표 불성립",
    188: "점검 수당 결합은 Benefit 결합 불성립",
    189: "가격 책정 요건 결합은 Pricing 기각 도메인 불성립",
    190: "묘지 감가상각 결합은 Depreciation 결합 불성립",
    191: "커미션 사직 결합은 Resignation 결합 불성립",
    194: "연료 조율기 결합은 Tuner 결합 불성립",
    195: "우쿨렐레 신호 결합은 Signal 결합 불성립",
    196: "플루트 보관베이 결합은 Bay 기각 계열 불성립",
    197: "첼로 타브 결합은 Tab 악보 관행 불성립(기타·베스 한정)",
    198: "색소폰 벌금 결합은 Penalty 결합 불성립",
    200: "클라리넷 폭 결합은 Width 물리 사양 불성립",
}

del REJECT_REASON[159.5]

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 44, len(APPROVE)
assert len(DUP_REJECT) == 0
assert len(REJECT_REASON) == 156, len(REJECT_REASON)
covered = set(APPROVE) | set(DUP_REJECT) | set(REJECT_REASON)
missing = sorted(set(range(1, n + 1)) - covered)
extra = sorted(covered - set(range(1, n + 1)))
assert covered == set(range(1, n + 1)), f"missing={missing} extra={extra}"
overlap = (set(APPROVE) & set(DUP_REJECT)) | (set(APPROVE) & set(REJECT_REASON)) | (set(DUP_REJECT) & set(REJECT_REASON))
assert not overlap, f"overlapping indices: {sorted(overlap)}"

decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in APPROVE:
        conf, reason = APPROVE[i]
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": conf, "reason": reason})
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
print(f"approve={approved} reject={len(decisions)-approved} (dup={len(DUP_REJECT)})")
