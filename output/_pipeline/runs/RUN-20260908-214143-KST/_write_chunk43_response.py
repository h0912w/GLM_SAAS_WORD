import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk42_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk42_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    12: (0.6, "보드워크 투어 확인서로 성립 (Confirmation 라인 준용)"),
    14: (0.6, "코골이 치료 플랜으로 실재 (Plan 라인 준용)"),
    34: (0.6, "치은염 도해 학습자료로 실재 (dental 도해 계열)"),
    46: (0.6, "모금 전략 핸드북으로 실재 (Handbook 라인)"),
    50: (0.6, "배차 실무 세미나로 실재 (Seminar 라인)"),
    54: (0.7, "윤작 계획 교육으로 실재 (농업 실무 개념)"),
    57: (0.6, "구독 발행 실무 세미나로 실재 (Seminar 라인)"),
    61: (0.7, "구역 온도 관리 교육으로 실재 (HVAC 실무 개념)"),
    62: (0.6, "잠금 장치 설치 핸드북으로 실재 (Handbook 라인)"),
    65: (0.6, "결혼 서약 준비 세미나로 실재 (Seminar 라인)"),
    68: (0.6, "배관 서비스 전단으로 실재 (Flyer 라인)"),
    71: (0.6, "비스트로 이용권으로 성립 (Voucher 라인 준용)"),
    79: (0.7, "치과 마취 프로토콜 교육으로 실재 (도메인 실무 개념)"),
    80: (0.6, "현장학습 준비 핸드북으로 실재 (Handbook 라인)"),
    87: (0.6, "상처 드레싱 교육 안내 전단으로 실재 (Flyer 라인)"),
    130: (0.6, "치은염 도식 학습자료로 실재 (dental 도해 계열)"),
    139: (0.6, "와이너리 테스팅 워크숍으로 실재 (Workshop 라인)"),
    142: (0.7, "작물 재배 교육으로 실재 (농업 실무 개념)"),
    146: (0.6, "원고 준비 실무 세미나로 실재 (Seminar 라인)"),
    150: (0.7, "계측기 교정 교육으로 실재 (제조 실무 개념)"),
    151: (0.6, "윤작 계획 핸드북으로 실재 (Handbook 라인)"),
    153: (0.6, "콘텐츠 마케팅 세미나로 실재 (Seminar 라인)"),
    156: (0.6, "보안 패치 서비스 전단으로 실재 (Flyer 라인)"),
    157: (0.6, "시럽 투여 복약 교육으로 실재 (약국 실무 개념)"),
    158: (0.6, "구역 온도 관리 핸드북으로 실재 (Handbook 라인)"),
    164: (0.6, "하부 세척 서비스 전단으로 실재 (Flyer 라인)"),
    175: (0.6, "치과 마취 프로토콜 핸드북으로 실재 (Handbook 라인)"),
    178: (0.6, "열전대 점검 세미나로 실재 (Seminar 라인)"),
    182: (0.6, "음악 교육 안내 전단으로 실재 (Flyer 라인)"),
    194: (0.6, "폭포 투어 견적으로 성립 (Estimate 라인 준용)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "바리스타 초안 결합은 Draft 다의어 불성립",
    2: "구강청격 요약 결합은 Summary 불성립",
    3: "폭포 색인 결합은 Index 불성립",
    4: "펍 코드 결합은 Code 불성립",
    5: "마우스가드 목록 결합은 List 불성립",
    6: "일몰 전표 결합은 Slip 다의어 불성립",
    7: "스테이크하우스 배지 결합은 Badge 다의어 불성립",
    8: "스마일 잔표 결합은 Stub 불성립",
    9: "수변 메모 결합은 Memo 불성립",
    10: "스시 회람 결합은 Circular 다의어 불성립",
    11: "호흡 자문 결합은 Advisory 추상 불성립",
    13: "타코 단위 결합은 Unit 다의어 불성립",
    15: "해변 가격 속성 결합은 Price 불성립",
    16: "면집 합계 결합은 Sum 불성립",
    17: "교합 채무 결합은 Debt 불성립",
    18: "전망 현금 결합은 Cash 불성립",
    19: "해산물 수당 결합은 Allowance 불성립",
    20: "치과 관세 결합은 Tariff 불성립",
    21: "배낭여행 지분 결합은 Stake 불성립",
    22: "교정의 버전 속성 결합은 Version 불성립",
    23: "패러세일링 규칙 결합은 Rule 불성립",
    24: "치위 속성 결합은 Attribute 불성립",
    25: "야생동물 형식 결합은 Format 불성립",
    26: "치실 서명 결합은 Signature 불성립",
    27: "라군 잔액 결합은 Balance 불성립",
    28: "치석 부과금 결합은 Levy 불성립",
    29: "빙하 보조금 결합은 Subsidy 불성립",
    30: "불소 선수금 결합은 Advance 불성립",
    31: "화산 가산율 결합은 Markup 불성립",
    32: "실런트 체험 결합은 Trial 불성립",
    33: "당일여행 라벨 결합은 Label 불성립",
    35: "요트 배치도 결합은 여행 서비스와 결합 불명확",
    36: "이갈이 렌더링 결합은 Rendering 불성립",
    37: "산책로 키트 결합은 Kit 불성립",
    38: "구취 합계 결합은 Total 불성립",
    39: "우릴 저장소 결합은 Repository 불성립",
    40: "치주염 변환기 결합은 Converter 추상 불성립",
    41: "사막 기록기 결합은 Recorder 추상 불성립",
    42: "부정교합 점검기 결합은 Checker 추상 불성립",
    43: "와이너리 타이머 결합은 Timer 추상 불성립",
    44: "치수과 보호자 결합은 Guardian 추상 불성립",
    45: "치주 결과 속성 결합은 Result 불성립",
    47: "주민 대응 일정표 결합 불명확",
    48: "브랜드 소견 결합 불명확",
    49: "원고 권고 결합 불명확",
    51: "위협 분석 리트리트 결합 불성립",
    52: "프로비저닝 토너먼트 결합 불성립",
    53: "대기열 전단 결합은 Queue 추상 불명확",
    55: "후원자 관리 일정표 결합 불명확",
    56: "콘텐츠 권고 결합 불명확",
    58: "통신 개통 리트리트 결합 불성립",
    59: "보안 패치 토너먼트 결합 불성립",
    60: "설정 전단 결합은 Configuration 추상 불명확",
    63: "통번역 일정표 결합 불명확",
    64: "이사 파손 소견 결합 불명확",
    66: "수영장 동절기 관리 리트리트 결합 불성립",
    67: "차량 하부 토너먼트 결합 불성립",
    69: "카페 플래너 결합은 Planner 추상 불성립",
    70: "다이너 카드 결합은 Card 다의어 불성립",
    72: "피자집 관세 결합은 Tariff 불성립",
    73: "데리 연장 결합은 Extension 불성립",
    74: "디저트 조력자 결합은 Helper 추상 불성립",
    75: "포장 조회 결합은 Lookup 불성립",
    76: "브런치 다이어리 결합은 Diary 불성립",
    77: "베이커리 와트 속성 결합은 Wattage 불성립",
    78: "제과 보증인 결합은 Guarantor 불성립",
    81: "네일 폴리시 일정표 결합 불명확",
    82: "열전대 권고 결합 불명확",
    83: "비상 장치 세미나 결합은 Panic 다의어 불명확",
    84: "수영장 선물 결합 불성립 - Gift",
    85: "서핑 리트리트 결합 불성립",
    86: "템포 토너먼트 결합 불성립",
    88: "베이글 신호 결합은 Signal 불성립",
    89: "도넛 저울 결합은 Scale 다의어 불성립",
    90: "에스프레소 달력 결합은 Calendar 불성립",
    91: "라떼 전광판 결합은 Ticker 불성립",
    92: "칫솔 창문 결합은 Window 불성립",
    93: "스노클링 로그 결합은 Log 불성립",
    94: "칵테일 프로필 결합은 Profile 다의어 불성립",
    95: "치약 상태 속성 결합은 Status 불성립",
    96: "카약 파일 결합은 File 불성립",
    97: "바리스타 요약 결합은 Summary 불성립",
    98: "구강청격 타임라인 결합은 Timeline 불성립",
    99: "폭포 티켓 결합은 Ticket 다의어 불성립",
    100: "펍 목록 결합은 List 불성립",
    101: "마우스가드 테이블 결합은 Table 불성립",
    102: "일몰 샘플 결합은 Sample 다의어 불성립",
    103: "스테이크하우스 잔표 결합은 Stub 불성립",
    104: "스마일 명세서 결합은 Statement 불성립",
    105: "수변 한도 결합은 Quota 불성립",
    106: "스시 자문 결합은 Advisory 추상 불성립",
    107: "호흡 청원 결합은 Petition 불성립",
    108: "보드워크 요약 결합은 Recap 불성립",
    109: "타코 플랜 결합은 Noodle Plan 기각 라인 준용 불명확",
    110: "코골이 비용 속성 결합은 Cost 불성립",
    111: "해변 요금 속성 결합은 Fare 불성립",
    112: "면집 채무 결합은 Debt 불성립",
    113: "교합 기금 결합은 Fund 불성립",
    114: "전망 판매 결합은 Sale 다의어 불성립",
    115: "해산물 관세 결합은 Tariff 불성립",
    116: "치과 가치 속성 결합은 Value 불성립",
    117: "배낭여행 마진 속성 결합은 Margin 불성립",
    118: "교정의 링크 결합은 Link 불성립",
    119: "패러세일링 세부 결합은 Detail 불성립",
    120: "치위 필드 결합은 Field 불성립",
    121: "야생동물 일련번호 결합은 Serial 불성립",
    122: "치실 마커 결합은 Marker 불성립",
    123: "라군 이자 결합은 Interest 불성립",
    124: "치석 기한 결합은 Due 불성립",
    125: "빙하 할인 결합은 Discount 불성립",
    126: "불소 벌칙 결합은 Penalty 불성립",
    127: "화산 리딤 결합은 Redemption 불성립",
    128: "실런트 그래프 결합은 Graph 불성립",
    129: "당일여행 매뉴얼 결합은 여행 서비스와 결합 불명확",
    131: "요트 스케치 결합은 여행 서비스와 결합 불명확",
    132: "이갈이 통지 결합은 Notification 불성립",
    133: "산책로 횟수 결합은 Count 불성립",
    134: "구취 위젯 결합은 Widget 불성립",
    135: "우릴 공지 결합은 Announcement 불성립",
    136: "치주염 생성기 결합은 Generator 추상 불성립",
    137: "사막 견적기 결합은 Estimator 추상 불성립",
    138: "부정교합 탐지기 결합은 Detector 추상 불성립",
    140: "치수과 조력자 결합은 Helper 추상 불성립",
    141: "치주 연승 속성 결합은 Streak 불성립",
    143: "모금 일정표 결합 불명확",
    144: "주민 대응 소견 결합 불명확",
    145: "브랜드 권고 결합 불명확",
    147: "배차 선물 결합 불성립 - Gift",
    148: "위협 분석 토너먼트 결합 불성립",
    149: "프로비저닝 전단 결합 불명확",
    152: "후원자 관리 소견 결합 불명확",
    154: "구독 발행 선물 결합 불성립 - Gift",
    155: "통신 개통 토너먼트 결합 불성립",
    159: "잠금 장치 일정표 결합 불명확",
    160: "통번역 소견 결합 불명확",
    161: "이사 파손 권고 결합 불명확",
    162: "결혼 서약 선물 결합 불성립 - Gift",
    163: "수영장 동절기 관리 토너먼트 결합 불성립",
    165: "카페 스케줄러 결합은 Scheduler 추상 불성립",
    166: "다이너 시트 결합은 Sheet 다의어 불성립",
    167: "비스트로 배지 결합은 Badge 다의어 불성립",
    168: "피자집 가치 속성 결합은 Value 불성립",
    169: "데리 체험 결합은 Trial 불성립",
    170: "디저트 단계 결합은 Stage 다의어 불성립",
    171: "포장 핑 결합은 Ping 불성립",
    172: "브런치 환불 결합은 Refund 불성립",
    173: "베이커리 밝기 속성 결합은 Brightness 불성립",
    174: "제과 조율기 결합은 Tuner 추상 불성립",
    176: "현장학습 일정표 결합 불명확",
    177: "네일 폴리시 소견 결합 불명확",
    179: "비상 장치 선물 결합은 Panic 다의어 불성립",
    180: "수영장 리트리트 결합 불성립",
    181: "서핑 토너먼트 결합 불성립",
    183: "베이글 시계 결합은 Watch 다의어 불성립",
    184: "도넛 경로 결합은 Route 불성립",
    185: "에스프레소 디렉터리 결합은 Directory 불성립",
    186: "라떼 선 결합은 Line 다의어 불성립",
    187: "칫솔 롤 결합은 Roll 다의어 불성립",
    188: "스노클링 양식 결합은 Form 다의어 불성립",
    189: "칵테일 상태 속성 결합은 Status 불성립",
    190: "치약 전망 속성 결합은 View 불성립",
    191: "카약 수준 속성 결합은 Level 불성립",
    192: "바리스타 타임라인 결합은 Timeline 불성립",
    193: "구강청격 리마인더 결합은 Reminder 불성립",
    195: "펍 테이블 결합은 Table 불성립",
    196: "마우스가드 전표 결합은 Slip 다의어 불성립",
    197: "일몰 슬롯 결합은 Slot 불성립",
    198: "스테이크하우스 명세서 결합은 Statement 불성립",
    199: "스마일 메모 결합은 Memo 불성립",
    200: "수변 탭 결합은 Tab 다의어 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 30, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 170, len(REJECT_REASON)
covered = set(APPROVE) | set(TRADEMARK_REJECT) | set(DUP_REJECT) | set(REJECT_REASON)
missing = sorted(set(range(1, n + 1)) - covered)
extra = sorted(covered - set(range(1, n + 1)))
assert covered == set(range(1, n + 1)), f"missing={missing} extra={extra}"
overlap = (set(APPROVE) & set(TRADEMARK_REJECT)) | (set(APPROVE) & set(DUP_REJECT)) | (set(APPROVE) & set(REJECT_REASON)) | (set(TRADEMARK_REJECT) & set(DUP_REJECT)) | (set(TRADEMARK_REJECT) & set(REJECT_REASON)) | (set(DUP_REJECT) & set(REJECT_REASON))
assert not overlap, f"overlap={sorted(overlap)}"

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
