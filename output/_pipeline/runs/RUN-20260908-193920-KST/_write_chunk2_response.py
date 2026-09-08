import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk1_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk1_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    1: (0.6, "하프 레슨 강사·업체 디렉터리 관리로 명확"),
    3: (0.6, "비올라 학습 플랜 관리로 명확"),
    7: (0.6, "아코디언 수강료 환불 처리 관리로 명확 (학원 운영)"),
    8: (0.6, "하모니카 목재 보관 습도 관리로 명확 (악기 보관 실무)"),
    9: (0.6, "기고자 인테이크 설문으로 명확"),
    11: (0.6, "애프터파티 요건(인원·장비) 관리로 명확"),
    19: (0.6, "오디션 진행 타임라인 관리로 명확"),
    20: (0.6, "조율 관련 자문 서비스로 명확"),
    25: (0.6, "앙상블 단원 가용 시간 관리로 명확"),
    32: (0.6, "합창단 입단·문의 접수 관리로 명확"),
    33: (0.6, "퇴직플랜 승인 처리 관리로 명확"),
    34: (0.6, "오케스트라 단원·청중 설문으로 명확"),
    37: (0.6, "보험 신고서 제출 요건 관리로 명확"),
    38: (0.6, "임대 자산 감가상각 관리로 명확 - 임대인 실제 회계 업무"),
    41: (0.6, "리듬 훈련 진도 추적으로 명확 (학원 운영)"),
    44: (0.6, "수전 상태·설치 평가로 명확 (Evaluation 라인)"),
    45: (0.6, "호텔 투숙 만족 설문으로 명확"),
    47: (0.6, "송장 발행 요건·필수항목 관리로 명확"),
    50: (0.6, "임차 위험 요인(미납·파손) 관리로 명확 - 임대 운영 위험 실존"),
    53: (0.6, "기타 레슨 운영 관리(회원·일정)로 명확"),
    54: (0.6, "바이올린 연습·레슨 알림으로 명확"),
    57: (0.6, "우쿨렐레 연습 일지 관리로 명확 (Diary 라인)"),
    58: (0.6, "전세기 운항·안전 평가로 명확 (Evaluation 라인)"),
    65: (0.6, "첼로 수강 등록부 관리로 명확"),
    68: (0.6, "클라리넷 운지법·연습 참고 자료 관리로 명확"),
    70: (0.6, "보행기 상태·적합성 평가로 명확 (Evaluation 라인)"),
    71: (0.6, "방역 대상지·만족도 설문으로 명확"),
    83: (0.6, "오보에 학습 진도 타임라인 관리로 명확"),
    86: (0.6, "타악 리듬 패턴 생성기로 명확 - 실재 음악 제작·연습 도구"),
    87: (0.6, "만돌린 수강생 계정 관리로 명확 (학원 운영)"),
    90: (0.6, "논문 심사·평가로 명확 (Evaluation 라인)"),
    101: (0.6, "오디션 일정·결과 알림으로 명확"),
    106: (0.6, "레퍼토리 곡목 참고 자료 관리로 명확"),
    107: (0.6, "앙상블 참가 자격·요건 관리로 명확"),
    108: (0.6, "반주 연습·시범 영상 관리로 명확"),
    114: (0.6, "합창단 오디션 후 후속 연락 관리로 명확"),
    116: (0.6, "우산보험(실손 담보) 담보 평가로 명확 (Evaluation 라인)"),
    119: (0.6, "상속·자산 절차 요건 관리로 명확"),
    127: (0.6, "세차 품질 평가로 명확 (Evaluation 라인)"),
    128: (0.6, "수전 수리 견적 인테이크 설문으로 명확"),
    133: (0.6, "배송 화물 위험 요인 관리로 명확 - 운송 위험 실존"),
    134: (0.6, "임차 보증인 심사·서류 관리로 명확 - 임대 보증 실무 (nonsense Guarantor 결합과 구분)"),
    140: (0.6, "우쿨렐레 수강료 환불 처리 관리로 명확"),
    141: (0.6, "전세기 차량 문의 인테이크 설문으로 명확"),
    143: (0.6, "금고 설치·보안 등급 요건 관리로 명확"),
    147: (0.6, "첼로 레슨 일정 관리로 명확 (학원 운영)"),
    148: (0.6, "색소폰 레슨 시간대 슬롯 관리로 명확 (예약 운영)"),
    152: (0.6, "영유아 발달 평가로 명확 (Evaluation 라인)"),
    153: (0.6, "보행기 지원 인테이크 설문으로 명확"),
    156: (0.6, "가구 소재별 세척 요건 관리로 명확"),
    165: (0.6, "오보에 연습·레슨 알림으로 명확"),
    168: (0.6, "타악 연습·연주 녹음 관리로 명확 - 녹음기 reading (타악은 리코더 악기 아님)"),
    170: (0.6, "학원 소식 뉴스레터 발송 관리로 명확"),
    172: (0.6, "배수로·홈 통로 상태 평가로 명확 (Evaluation 라인)"),
    173: (0.6, "논문 조사용 설문 도구로 명확"),
    175: (0.6, "지원 티켓 심각도 분류 기준 요건 관리로 명확"),
    177: (0.6, "타이어 마모·파손 위험 관리로 명확 - 차량 안전 위험 실존"),
    184: (0.6, "조율 예약 확인·확정 관리로 명확"),
    187: (0.6, "템포(BPM) 계산기로 명확 - 실재 음악 도구 (대상 모호 계산기 결합과 구분)"),
    190: (0.6, "반주 연습 일지 관리로 명확 (Diary 라인)"),
    196: (0.6, "합창단 입단·참가 승인 관리로 명확"),
    197: (0.6, "퇴직플랜·은퇴 자산 평가로 명확 (Evaluation 라인)"),
    198: (0.6, "우산보험 문의 인테이크 설문으로 명확"),
    200: (0.6, "명상 코스 참가 요건 관리로 명확"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    2: "오보에 요약 결합은 요약 대상 불성립",
    4: "트롬본 균형·잔고 결합은 Balance 불성립",
    5: "타악 변환기 결합은 Converter 불성립",
    6: "만돌린 회신 결합은 Reply 불성립",
    10: "심각도 활용률 결합 불성립 - Utilization",
    12: "타이어에 감가상각 결합 불성립",
    13: "Litter 다의어 도메인 기각 라인 + Resignation 불성립",
    14: "법랑질 신체 조직에 위험 등록 서비스 불성립 - 시설·설비 위험과 구분",
    15: "Outdoor 형용사 단독 도메인 기각 라인 + Guarantor 불성립",
    16: "레슨 신호 결합은 Signal 추상 불성립",
    17: "연습 게이트 결합은 Gate 불성립",
    18: "리사이탈 차트 결합은 Chart 불성립",
    21: "이론 마진 결합은 Margin 불성립",
    22: "코드 연체 결합은 Arrears 불성립",
    23: "템포 저장소 결합은 저장 대상 불성립",
    24: "레퍼토리 읽기 결합 불성립 - 독보 대상은 악보이지 곡목이 아님",
    26: "반주자 레시피 결합 불성립",
    27: "메트로놈 무게 결합은 Weight 속성어 불성립",
    28: "증서 유형 결합은 Type 속성어 불성립",
    29: "곡집 높이 결합은 Height 속성어 불성립",
    30: "교법 밝기 결합은 Brightness 불성립",
    31: "캠프 습도 결합은 대상 불성립으로 불명확",
    35: "명상 활용률 결합 불성립 - Utilization",
    36: "자산 혜택 결합은 Benefit 추상 불명확",
    39: "멜로디 사직 결합은 Resignation 불성립",
    40: "수면 건강 대상에 위험 등록 서비스 불성립",
    42: "비트 레이더 결합은 Radar 추상 불성립",
    43: "피치 비컨 결합은 Beacon 추상 불성립",
    46: "피아노 활용률 결합 불성립 - Utilization",
    48: "사건서류에 감가상각 결합 불성립",
    49: "배송 사직 결합은 Resignation 불성립",
    51: "보험료에 보증인 결합 불성립",
    52: "근태에 튜너 결합 불성립",
    55: "드럼 규칙 결합은 Rule 불성립",
    56: "보컬 스테이지 결합은 무대·단계 다의어 불명확",
    59: "출동 활용률 결합 불성립 - Utilization",
    60: "금고 혜택 결합은 Benefit 추상 불명확",
    61: "배경망 사직 결합은 Resignation 불성립",
    62: "작가 인적 대상에 위험 등록 서비스 불성립",
    63: "히터에 튜너 결합 불성립",
    64: "플루트 데스크 결합은 Desk 추상 불성립",
    66: "색소폰 샘플 결합은 음원·견본 다의어 불명확",
    67: "트럼펫 균형·잔고 결합은 Balance 불성립",
    69: "베이스 거리 결합은 Distance 속성어 불성립",
    72: "멀칭 활용률 결합 불성립 - Utilization",
    73: "가구 혜택 결합은 Benefit 추상 불명확",
    74: "얼룩에 요건 결합 불성립",
    75: "화장에 감가상각 결합 불성립",
    76: "커트 사직 결합은 Resignation 불성립",
    77: "약사 인적 대상에 위험 등록 서비스 불성립",
    78: "마리나에 보증인 결합 불성립",
    79: "활주로에 튜너 결합 불성립",
    80: "오르간 신호 결합은 Signal 추상 불성립",
    81: "검인 루프 결합은 Loop 추상 불성립 - 도구형 Probate 기각 라인",
    82: "하프 로케이터 결합은 검색 대상 불명확",
    84: "비올라 비용 결합은 대상 불충분으로 불명확",
    85: "트롬본 이자·관심 결합은 Interest 불성립",
    88: "아코디언 경비 결합은 대상 불충분으로 불명확",
    89: "하모니카 에피소드 결합은 회차 콘텐츠 서비스 불충분으로 불명확",
    91: "바이라인 활용률 결합 불성립 - Utilization",
    92: "심각도 혜택 결합은 Benefit 추상 불명확",
    93: "애프터파티에 감가상각 결합 불성립",
    94: "타이어 사직 결합은 Resignation 불성립",
    95: "Litter 다의어 도메인 기각 라인 + 위험 결합 불성립",
    96: "법랑질에 보증인 결합 불성립",
    97: "Outdoor 형용사 단독 도메인 기각 라인 + Tuner 불성립",
    98: "레슨 감시 결합은 Watch 도구형 불성립 - Probate Watch 준용",
    99: "연습 넥서스 결합은 Nexus 추상 불성립 - Guitar Nexus 준용",
    100: "리사이탈 빈 결합은 Bin 불성립",
    102: "튜닝 청원 결합은 Petition 불성립",
    103: "이론 벌금 결합은 Fine 다의어 불성립",
    104: "코드 선수금·전진 결합은 Advance 불성립",
    105: "템포 공지 결합은 공지 대상 불성립",
    109: "메트로놈 거리 결합은 Distance 속성어 불성립",
    110: "증서 시계 결합은 Clock 불성립",
    111: "곡집 폭 결합은 Width 속성어 불성립",
    112: "교법 빈도 결합은 Frequency 불명확",
    113: "캠프 에피소드 결합은 불명확 - Episode 라인",
    115: "퇴직 행렬 결합은 Matrix 추상 불성립",
    117: "오케스트라 활용률 결합 불성립 - Utilization",
    118: "명상 혜택 결합은 Benefit 추상 불명확",
    120: "신고서에 감가상각 결합 불성립",
    121: "임대인 사직 결합은 Resignation 불성립",
    122: "멜로디에 위험 결합 불성립",
    123: "수면에 보증인 결합 불성립",
    124: "리듬 흐름 결합은 Flow 추상 불성립",
    125: "비트 릴레이 결합은 Relay 불성립",
    126: "피치 대장간 결합은 Forge 불성립",
    129: "호텔 활용률 결합 불성립 - Utilization",
    130: "피아노 혜택 결합은 Benefit 추상 불명확",
    131: "송장에 감가상각 결합 불성립",
    132: "사건서류 사직 결합은 Resignation 불성립",
    135: "보험료에 튜너 결합 불성립",
    136: "기타 엔진 결합은 Engine 추상 불성립",
    137: "바이올린 지수·색인 결합은 Index 불명확",
    138: "드럼 세부 결합은 Detail 불성립",
    139: "보컬 결과 결합은 결과 대상 불명확",
    142: "출동 혜택 결합은 Benefit 추상 불명확",
    144: "촬영 배경 물건에 위험 등록 불성립",
    145: "작가에 보증인 결합 불성립",
    146: "플루트 레이더 결합은 Radar 추상 불성립",
    149: "트럼펫 이자·관심 결합은 Interest 불성립",
    150: "클라리넷 예측 결합은 Forecast 불성립",
    151: "베이스 범위 결합은 Range 속성어 불성립",
    154: "방역 활용률 결합 불성립 - Utilization",
    155: "멀칭 혜택 결합은 Benefit 추상 불명확",
    157: "얼룩에 감가상각 결합 불성립",
    158: "화장 사직 결합은 Resignation 불성립",
    159: "커트에 위험 결합 불성립",
    160: "약사에 보증인 결합 불성립",
    161: "마리나에 튜너 결합 불성립",
    162: "오르간 감시 결합은 Watch 도구형 불성립",
    163: "검인 격자 결합은 Grid 추상 불성립",
    164: "하프 파인더 결합은 검색 대상 불명확",
    166: "비올라 가격 결합은 Price 속성어 불성립 - 견적은 Quote 라인",
    167: "트롬본 자산 결합 불성립",
    169: "만돌린 케이스 결합은 악기 가방 물건 자체 대상 불성립",
    171: "하모니카 주기 결합은 Cycle 불명확",
    174: "바이라인 혜택 결합은 Benefit 추상 불명확",
    176: "애프터파티 사직 결합은 Resignation 불성립",
    178: "Litter 다의어 도메인 기각 라인 + Guarantor 불성립",
    179: "법랑질에 튜너 결합 불성립",
    180: "레슨 범위 결합은 Scope 불명확 - Probate Scope 준용",
    181: "연습 도감 결합은 Atlas 불명확 - Guitar Atlas 준용",
    182: "리사이탈 여권 결합은 Passport 은유 불성립",
    183: "오디션 지수·색인 결합은 Index 불명확",
    185: "이론 번호 결합은 Number 속성어 불성립 - Drum Number 준용",
    186: "코드 페널티 결합은 Penalty 불성립",
    188: "레퍼토리 예측 결합은 Forecast 불성립",
    189: "앙상블 방송 결합은 대상·방식 불명확",
    191: "메트로놈 범위 결합은 Range 속성어 불성립",
    192: "증서 시간 결합은 Time 속성어 불성립",
    193: "곡집 온도 결합은 Temperature 불성립",
    194: "교법 호환성 결합은 Compatibility 불성립",
    195: "캠프 주기 결합은 Cycle 불명확",
    199: "오케스트라 혜택 결합은 Benefit 추상 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 64, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 136, len(REJECT_REASON)
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
