import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk41_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk41_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    10: (0.6, "펍 청구서로 성립 (Bill 라인 준용)"),
    11: (0.6, "마우스가드 영수증으로 성립 (Receipt 라인 준용)"),
    14: (0.6, "치아미백 이용권으로 성립 (Voucher 라인 준용)"),
    21: (0.6, "해변 여행 플랜으로 성립 (Plan 라인 준용)"),
    40: (0.6, "치은염 관리 매뉴얼로 실재 (dental 도해 계열)"),
    42: (0.6, "이갈이 스케치 학습자료로 실재 (dental 도해 계열)"),
    52: (0.6, "주민 대응 교육으로 실재 (정부 실무 개념)"),
    53: (0.6, "브랜드 구축 핸드북으로 실재 (Handbook 라인)"),
    56: (0.6, "위협 인텔리전스 세미나로 실재 (Seminar 라인)"),
    61: (0.6, "후원자 관리 교육으로 실재 (비영리 실무 개념)"),
    64: (0.6, "통신 개통 실무 세미나로 실재 (Seminar 라인)"),
    68: (0.6, "통번역 실무 교육으로 실재 (통역사 의미 명확)"),
    69: (0.6, "이사 파손 대응 핸드북으로 실재 (Handbook 라인)"),
    71: (0.6, "수영장 동절기 관리 세미나로 실재 (Seminar 라인)"),
    75: (0.6, "타악기 레슨 홍보 전단으로 실재 (Flyer 라인)"),
    81: (0.6, "디저트 실습 워크숍으로 실재 (Workshop 라인)"),
    83: (0.6, "브런치 레시피 콘텐츠로 실재 (음식업 실무 콘텐츠)"),
    86: (0.6, "네일 폴리시 교육으로 실재 (salon 맥락 의미 명확)"),
    90: (0.6, "서핑 강습 세미나로 실재 (Seminar 라인)"),
    94: (0.6, "화물 통합 서비스 전단으로 실재 (Flyer 라인)"),
    107: (0.6, "펍 영수증으로 성립 (Receipt 라인 준용)"),
    110: (0.6, "스테이크하우스 이용권으로 성립 (Voucher 라인 준용)"),
    137: (0.6, "치은염 관리 워크시트로 실재 (dental 도해 계열)"),
    147: (0.6, "치수과 실습 워크숍으로 실재 (Workshop 라인)"),
    149: (0.7, "모금 전략 교육으로 실재 (도메인 실무 개념)"),
    150: (0.6, "주민 대응 핸드북으로 실재 (Handbook 라인)"),
    157: (0.6, "채용 소싱 서비스 전단으로 실재 (Flyer 라인)"),
    158: (0.6, "후원자 관리 핸드북으로 실재 (Handbook 라인)"),
    165: (0.6, "잠금 장치 설치 교육으로 실재 (locksmith 맥락 명확)"),
    166: (0.6, "통번역 실무 핸드북으로 실재 (Handbook 라인)"),
    183: (0.6, "현장학습 준비 교육 자료로 실재 (육아 실무 개념)"),
    184: (0.6, "네일 폴리시 핸드북으로 실재 (Handbook 라인)"),
    187: (0.6, "수영장 관리 세미나로 실재 (Seminar 라인)"),
    191: (0.6, "파산 상담 서비스 전단으로 실재 (Flyer 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "라떼 창고 결합은 Bin 다의어 불성립",
    2: "칫솔 로비 결합은 Lobby 불성립",
    3: "스노클링 창문 결합은 Window 불성립",
    4: "칵테일 점수 결합은 Score 불성립",
    5: "치약 노트 결합은 Note 불성립",
    6: "카약 상태 속성 결합은 Status 불성립",
    7: "바리스타 갱신 결합은 Update 불성립",
    8: "구강청격 피드 결합은 Feed 불성립",
    9: "폭포 타임라인 결합은 Timeline 불성립",
    12: "일몰 목록 결합은 List 불성립",
    13: "스테이크하우스 패스 결합은 Pass 다의어 불성립",
    15: "수변 잔표 결합은 Stub 불성립",
    16: "스시 게시물 결합은 Bulletin 다의어 불성립",
    17: "호흡 요약 결합은 Brief 다의어 불성립",
    18: "보드워크 자문 결합은 Advisory 추상 불성립",
    19: "타코 요금 속성 결합은 Fee 불성립",
    20: "코골이 품목 결합은 Item 다의어 불성립",
    22: "면집 세금 결합은 Tax 불성립",
    23: "교합 대출 결합은 Loan 불성립",
    24: "전망 채무 결합은 Debt 불성립",
    25: "해산물 청구 결합은 Charge 다의어 불성립",
    26: "치과 의무 결합은 Duty 불성립",
    27: "배낭여행 관세 결합은 Tariff 불성립",
    28: "교정의 벌금 결합은 Fine 불성립",
    29: "패러세일링 버전 속성 결합은 Version 불성립",
    30: "치위 식별자 결합은 Identifier 불성립",
    31: "야생동물 속성 결합은 Attribute 불성립",
    32: "치실 일련번호 결합은 Serial 불성립",
    33: "라군 서명 결합은 Signature 불성립",
    34: "치석 이자 결합은 Interest 불성립",
    35: "빙하 부과금 결합은 Levy 불성립",
    36: "불소 할인 결합은 Discount 불성립",
    37: "화산 선수금 결합은 Advance 불성립",
    38: "실런트 리딤 결합은 Redemption 불성립",
    39: "당일여행 체험 결합은 Trial 불성립",
    41: "요트 도해 결합은 여행 서비스와 결합 불명확",
    43: "산책로 렌더링 결합은 Rendering 불성립",
    44: "구취 횟수 결합은 Count 불성립",
    45: "우릴 합계 결합은 Total 불성립",
    46: "치주염 공지 결합은 Announcement 불성립",
    47: "사막 변환기 결합은 Converter 추상 불성립",
    48: "부정교합 기록기 결합은 Recorder 추상 불성립",
    49: "와이너리 점검기 결합은 Checker 추상 불성립",
    50: "치수과 타이머 결합은 Timer 추상 불성립",
    51: "치주 조력자 결합은 Helper 추상 불성립",
    54: "원고 일정표 결합 불명확",
    55: "배차 소견 결합 불명확",
    57: "프로비저닝 선물 결합 불성립 - Gift",
    58: "대기열 리트리트 결합은 Queue 추상 불성립",
    59: "인재 소싱 토너먼트 결합 불성립",
    60: "명찰 전단 결합은 Badge 다의어 불성립",
    62: "콘텐츠 일정표 결합 불명확",
    63: "구독 발행 소견 결합 불명확",
    65: "보안 패치 선물 결합 불성립 - Gift",
    66: "설정 리트리트 결합은 Configuration 추상 불성립",
    67: "채팅 토너먼트 결합은 Chat 추상 불성립",
    70: "결혼 서약 소견 결합 불명확",
    72: "차량 하부 선물 결합 불성립 - Gift",
    73: "배수관 리트리트 결합 불성립",
    74: "관광객 토너먼트 결합은 Tourist 불성립",
    76: "카페 엔진 결합은 Engine 추상 불성립",
    77: "다이너 로그 결합은 Log 불성립",
    78: "비스트로 슬롯 결합은 Slot 불성립",
    79: "피자집 의무 결합은 Duty 불성립",
    80: "데리 가산율 결합은 Markup 불성립",
    82: "포장 매치 결합은 Match 다의어 불성립",
    84: "베이커리 부하 결합은 Load 불성립",
    85: "제과 사직 결합은 Resignation 불성립",
    87: "열전대 일정표 결합 불명확",
    88: "비상 대응 소견 결합은 Panic 다의어 불명확",
    89: "수영장 관리 권고 결합 불명확",
    91: "템포 선물 결합 불성립 - Gift",
    92: "상처 드레싱 리트리트 결합 불성립",
    93: "파산 토너먼트 결합 불성립",
    95: "베이글 폭포 결합은 Cascade 추상 불성립",
    96: "도넛 콘솔 결합은 Console 추상 불성립",
    97: "에스프레소 저널 결합은 Journal 다의어 불성립",
    98: "라떼 여권 결합은 Passport 다의어 불성립",
    99: "칫솔 전광판 결합은 Ticker 불성립",
    100: "스노클링 롤 결합은 Roll 다의어 불성립",
    101: "칵테일 노트 결합은 Note 불성립",
    102: "치약 태그 결합은 Tag 다의어 불성립",
    103: "카약 전망 속성 결합은 View 불성립",
    104: "바리스타 피드 결합은 Feed 불성립",
    105: "구강청격 초안 결합은 Draft 다의어 불성립",
    106: "폭표 리마인더 결합은 Reminder 불성립",
    108: "마우스가드 코드 결합은 Code 불성립",
    109: "일몰 테이블 결합은 Table 불성립",
    111: "스마일 배지 결합은 Badge 다의어 불성립",
    112: "수변 명세서 결합은 Statement 불성립",
    113: "스시 요약 결합은 Brief 다의어 불성립",
    114: "호흡 회람 결합은 Circular 다의어 불성립",
    115: "보드워크 청원 결합은 Petition 불성립",
    116: "타코 항목 결합은 Entry 다의어 불성립",
    117: "코골이 단위 결합은 Unit 다의어 불성립",
    118: "해변 비용 속성 결합은 Cost 불성립",
    119: "면집 대출 결합은 Loan 불성립",
    120: "교합 합계 결합은 Sum 불성립",
    121: "전망 기금 결합은 Fund 불성립",
    122: "해산물 의무 결합은 Duty 불성립",
    123: "치과 수당 결합은 Allowance 불성립",
    124: "배낭여행 가치 속성 결합은 Value 불성립",
    125: "교정의 번호 속성 결합은 Number 불성립",
    126: "패러세일링 링크 결합은 Link 불성립",
    127: "치위 분류 결합은 Category 불성립",
    128: "야생동물 필드 결합은 Field 불성립",
    129: "치실 토큰 결합은 Token 불성립",
    130: "라군 마커 결합은 Marker 불성립",
    131: "치석 자산 결합은 Asset 불성립",
    132: "빙하 기한 결합은 Due 불성립",
    133: "불소 연체 결합은 Arrears 불성립",
    134: "화산 벌칙 결합은 Penalty 불성립",
    135: "실런트 연장 결합은 Extension 불성립",
    136: "당일여행 그래프 결합은 Graph 불성립",
    138: "요트 도식 결합은 여행 서비스와 결합 불명확",
    139: "이갈이 개요 결합은 Outline 불성립",
    140: "산책로 통지 결합은 Notification 불성립",
    141: "구취 메시지 결합은 Message 불성립",
    142: "우릴 위젯 결합은 Widget 불성립",
    143: "치주염 계산기 결합은 Calculator 추상 불성립",
    144: "사막 생성기 결합은 Generator 추상 불성립",
    145: "부정교합 견적기 결합은 Estimator 추상 불성립",
    146: "와이너리 탐지기 결합은 Detector 추상 불성립",
    148: "치주 단계 결합은 Stage 다의어 불성립",
    151: "브랜드 일정표 결합 불명확",
    152: "원고 소견 결합 불명확",
    153: "배차 권고 결합 불명확",
    154: "위협 분석 선물 결합 불성립 - Gift",
    155: "프로비저닝 리트리트 결합 불성립",
    156: "대기열 토너먼트 결합은 Queue 추상 불성립",
    159: "콘텐츠 소견 결합 불명확",
    160: "구독 발행 권고 결합 불명확",
    161: "통신 개통 선물 결합 불성립 - Gift",
    162: "보안 패치 리트리트 결합 불성립",
    163: "설정 토너먼트 결합은 Configuration 추상 불성립",
    164: "채팅 전단 결합은 Chat 추상 불명확",
    167: "이사 파손 일정표 결합 불명확",
    168: "결혼 서약 권고 결합 불명확",
    169: "수영장 동절기 관리 선물 결합 불성립 - Gift",
    170: "차량 하부 리트리트 결합 불성립",
    171: "배수관 토너먼트 결합 불성립",
    172: "관광객 전단 결합은 Tourist 불성립",
    173: "카페 조수 결합은 Assistant 추상 불성립",
    174: "다이너 양식 결합은 Form 다의어 불성립",
    175: "비스트로 패스 결합은 Pass 다의어 불성립",
    176: "피자집 수당 결합은 Allowance 불성립",
    177: "데리 리딤 결합은 Redemption 불성립",
    178: "디저트 보호자 결합은 Guardian 추상 불성립",
    179: "포장 검증 결합은 Validation 불성립",
    180: "브런치 영상 결합은 Video 불성립",
    181: "베이커리 전압 속성 결합은 Voltage 불성립",
    182: "제과 위험 속성 결합은 Hazard 불성립",
    185: "열전대 소견 결합 불명확",
    186: "비상 대응 권고 결합은 Panic 다의어 불명확",
    188: "서핑 선물 결합 불성립 - Gift",
    189: "템포 리트리트 결합 불성립",
    190: "상처 드레싱 토너먼트 결합 불성립",
    192: "베이글 다리 결합은 Bridge 다의어 불성립",
    193: "도넛 패널 결합은 Panel 불성립",
    194: "에스프레소 등록부 결합은 Registry 불성립",
    195: "라떼 로비 결합은 Lobby 불성립",
    196: "칫솔 선 결합은 Line 다의어 불성립",
    197: "스노클링 보고서 결합은 Report 불성립",
    198: "칵테일 태그 결합은 Tag 다의어 불성립",
    199: "치약 프로필 결합은 Profile 다의어 불성립",
    200: "카약 이력 속성 결합은 History 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 34, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 166, len(REJECT_REASON)
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
