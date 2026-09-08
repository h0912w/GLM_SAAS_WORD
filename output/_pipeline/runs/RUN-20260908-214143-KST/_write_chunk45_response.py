import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk44_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk44_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    11: (0.6, "실런트 관리 워크시트로 실재 (dental 도해 계열)"),
    25: (0.6, "어메니티 서비스 교육으로 실재 (호텔 실무 개념)"),
    29: (0.6, "모금 전략 세미나로 실재 (Seminar 라인)"),
    33: (0.6, "배차 서비스 전단으로 실재 (Flyer 라인)"),
    34: (0.7, "재고 보충 교육으로 실재 (소매 실무 개념)"),
    35: (0.6, "셔틀 운영 핸드북으로 실재 (Handbook 라인)"),
    41: (0.6, "구독 발행 서비스 전단으로 실재 (Flyer 라인)"),
    42: (0.7, "기저귀 사용 교육으로 실재 (육아 강좌 실무 개념)"),
    43: (0.6, "옷장 정리 핸드북으로 실재 (Handbook 라인)"),
    47: (0.6, "잠금 실무 세미나로 실재 (Seminar 라인)"),
    50: (0.6, "결혼 서약 준비 전단으로 실재 (Flyer 라인)"),
    55: (0.6, "델리 운영 매뉴얼로 실재 (음식업 실무 개념)"),
    60: (0.7, "민원 대응 교육으로 실재 (고객 대응 실무 개념)"),
    61: (0.6, "범퍼 수리 핸드북으로 실재 (Handbook 라인)"),
    64: (0.6, "현장학습 준비 세미나로 실재 (Seminar 라인)"),
    108: (0.6, "실런트 시술 도해 학습자료로 실재 (dental 도해 계열)"),
    117: (0.6, "사막 생태 체험 워크숍으로 실재 (Workshop 라인)"),
    122: (0.7, "풀필먼트 운영 교육으로 실재 (이커머스 실무 개념)"),
    123: (0.6, "어메니티 서비스 핸드북으로 실재 (Handbook 라인)"),
    130: (0.6, "원고 준비 세미나 안내 전단으로 실재 (Flyer 라인)"),
    131: (0.7, "하자보증 교육으로 실재 (건설 실무 개념)"),
    132: (0.6, "재고 보충 핸드북으로 실재 (Handbook 라인)"),
    136: (0.6, "윤작 계획 세미나로 실재 (Seminar 라인)"),
    138: (0.6, "콘텐츠 서비스 전단으로 실재 (Flyer 라인)"),
    139: (0.7, "치아미백 사용 교육으로 실재 (치과 실무 개념)"),
    140: (0.6, "기저귀 사용 핸드북으로 실재 (Handbook 라인)"),
    144: (0.6, "구역 온도 관리 세미나로 실재 (Seminar 라인)"),
    157: (0.7, "복리후생 제도 교육으로 실재 (HR 실무 개념)"),
    158: (0.6, "민원 대응 핸드북으로 실재 (Handbook 라인)"),
    161: (0.6, "치과 마취 세미나로 실재 (Seminar 라인)"),
    164: (0.6, "HVAC 부품 서비스 전단으로 실재 (Flyer 라인)"),
    178: (0.6, "마우스가드 이용권으로 성립 (Voucher 라인 준용)"),
    185: (0.6, "보드워크 여행 플랜으로 성립 (Plan 라인 준용)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "교정의 식별자 결합은 Identifier 불성립",
    2: "패러세일링 속성 결합은 Attribute 불성립",
    3: "치위 토큰 결합은 Token 불성립",
    4: "야생동물 마커 결합은 Marker 불성립",
    5: "치실 자산 결합은 Asset 불성립",
    6: "라군 기한 결합은 Due 불성립",
    7: "치석 연체 결합은 Arrears 불성립",
    8: "빙하 벌칙 결합은 Penalty 불성립",
    9: "불소 연장 결합은 Extension 불성립",
    10: "화산 그래프 결합은 Graph 불성립",
    12: "당일여행 도식 결합은 여행 서비스와 결합 불명확",
    13: "치은염 개요 결합은 Outline 불성립",
    14: "요트 통지 결합은 여행 서비스와 결합 불명확",
    15: "이갈이 메시지 결합은 Message 불성립",
    16: "산책로 위젯 결합은 Widget 불성립",
    17: "구취 계산기 결합은 Calculator 추상 불성립",
    18: "우릴 생성기 결합은 Generator 추상 불성립",
    19: "치주염 점검기 결합은 Checker 추상 불성립",
    20: "사막 타이머 결합은 Timer 추상 불성립",
    21: "부정교합 보호자 결합은 Guardian 추상 불성립",
    22: "와이너리 단계 결합은 Stage 다의어 불성립",
    23: "치수과 연승 속성 결합은 Streak 불성립",
    24: "치주 비교 속성 결합은 Comparison 불성립",
    26: "등록금 핸드북 결합은 Tuition 결합 불명확",
    27: "설비 정지 일정표 결합 불명확",
    28: "작물 소견 결합 불명확",
    30: "주민 대응 선물 결합 불성립 - Gift",
    31: "브랜드 리트리트 결합 불성립",
    32: "원고 토너먼트 결합 불성립",
    36: "수업 운영 일정표 결합 불명확",
    37: "계측기 교정 소견 결합 불명확",
    38: "윤작 권고 결합 불명확",
    39: "후원자 관리 선물 결합 불성립 - Gift",
    40: "콘텐츠 토너먼트 결합 불성립",
    44: "왁싱 일정표 결합 불명확",
    45: "시럽 소견 결합 불명확",
    46: "구역 온도 관리 권고 결합 불명확",
    48: "통번역 선물 결합 불성립 - Gift",
    49: "이사 파손 리트리트 결합 불성립",
    51: "카페 등록기 결합은 Register 불성립",
    52: "다이너 노트 결합은 Note 불성립",
    53: "비스트로 메모 결합은 Memo 불성립",
    54: "피자집 벌금 결합은 Fine 불성립",
    56: "디저트 순위 속성 결합은 Rank 불성립",
    57: "포장 자격 속성 결합은 Eligibility 불성립",
    58: "브런치 재고 속성 결합은 Inventory 불성립",
    59: "베이커리 용량 속성 결합은 Capacity 불성립",
    62: "제과 일정표 결합 불명확",
    63: "치과 마취 권고 결합 불명확",
    65: "네일 폴리시 선물 결합 불성립 - Gift",
    66: "열전대 토너먼트 결합 불성립",
    67: "비상 장치 전단 결합은 Panic 다의어 불명확",
    68: "베이글 격자 결합은 Grid 불성립",
    69: "도넛 체인 결합은 Chain 다의어 불성립",
    70: "에스프레소 사무실 결합은 Office 불성립",
    71: "라떼 보고서 결합은 Report 불성립",
    72: "칫솔 양식 결합은 Form 다의어 불성립",
    73: "스노클링 점검 결합은 Check 불성립",
    74: "칵테일 파일 결합은 File 불성립",
    75: "치약 수준 속성 결합은 Level 불성립",
    76: "카약 피드 결합은 Feed 불성립",
    77: "바리스타 티켓 결합은 Ticket 다의어 불성립",
    78: "구강청격 견적 결합은 제품 견적 결합 불명확",
    79: "폭포 영수증 결합은 Receipt 라인 여행 결합 불명확",
    80: "펍 슬롯 결합은 Slot 불성립",
    81: "마우스가드 패스 결합은 Pass 다의어 불성립",
    82: "일몰 배지 결합은 Badge 다의어 불성립",
    83: "스테이크하우스 탭 결합은 Tab 다의어 불성립",
    84: "스마일 게시물 결합은 Bulletin 다의어 불성립",
    85: "수변 회람 결합은 Circular 다의어 불성립",
    86: "스시 항목 결합은 Entry 다의어 불성립",
    87: "호흡 요금 속성 결합은 Fee 불성립",
    88: "보드워크 단위 결합은 Unit 다의어 불성립",
    89: "타코 세금 결합은 Tax 불성립",
    90: "코골이 대출 결합은 Loan 불성립",
    91: "해변 채무 결합은 Debt 불성립",
    92: "면집 청구 결합은 Charge 다의어 불성립",
    93: "교합 의무 결합은 Duty 불성립",
    94: "전망 관세 결합은 Tariff 불성립",
    95: "해산물 벌금 결합은 Fine 불성립",
    96: "치과 번호 속성 결합은 Number 불성립",
    97: "배낭여행 링크 결합은 Link 불성립",
    98: "교정의 분류 결합은 Category 불성립",
    99: "패러세일링 필드 결합은 Field 불성립",
    100: "치위 서명 결합은 Signature 불성립",
    101: "야생동물 잔액 결합은 Balance 불성립",
    102: "치실 부과금 결합은 Levy 불성립",
    103: "라군 보조금 결합은 Subsidy 불성립",
    104: "치석 선수금 결합은 Advance 불성립",
    105: "빙하 가산율 결합은 Markup 불성립",
    106: "불소 체험 결합은 Trial 불성립",
    107: "화산 라벨 결합은 Label 불성립",
    109: "당일여행 배치도 결합은 여행 서비스와 결합 불명확",
    110: "치은염 렌더링 결합은 Rendering 불성립",
    111: "요트 키트 결합은 여행 서비스와 결합 불명확",
    112: "이갈이 합계 결합은 Total 불성립",
    113: "산책로 저장소 결합은 Repository 불성립",
    114: "구취 변환기 결합은 Converter 추상 불성립",
    115: "우릴 기록기 결합은 Recorder 추상 불성립",
    116: "치주염 탐지기 결합은 Detector 추상 불성립",
    118: "부정교합 조력자 결합은 Helper 추상 불성립",
    119: "와이너리 결과 속성 결합은 Result 불성립",
    120: "치수과 순위 속성 결합은 Rank 불성립",
    121: "치주 제안 결합은 Proposal 불성립",
    124: "등록금 일정표 결합은 Tuition 결합 불명확",
    125: "설비 정지 소견 결합 불명확",
    126: "작물 권고 결합 불명확",
    127: "모금 선물 결합 불성립 - Gift",
    128: "주민 대응 리트리트 결합 불성립",
    129: "브랜드 토너먼트 결합 불성립",
    133: "셔틀 일정표 결합 불명확",
    134: "수업 운영 소견 결합 불명확",
    135: "계측기 교정 권고 결합 불명확",
    137: "후원자 관리 리트리트 결합 불성립",
    141: "옷장 정리 일정표 결합 불명확",
    142: "왁싱 소견 결합 불명확",
    143: "시럽 권고 결합 불명확",
    145: "잠금 장치 선물 결합 불성립 - Gift",
    146: "통번역 리트리트 결합 불성립",
    147: "이사 파손 토너먼트 결합 불성립",
    148: "카페 운영 결합은 Ops 추상 불성립",
    149: "다이너 태그 결합은 Tag 다의어 불성립",
    150: "비스트로 한도 결합은 Quota 불성립",
    151: "피자집 번호 속성 결합은 Number 불성립",
    152: "데리 워크시트 결합 불명확",
    153: "디저트 추이 속성 결합은 Trend 불성립",
    154: "포장 방송 결합은 Broadcast 불성립",
    155: "브런치 청구 결합은 Claim 다의어 불성립",
    156: "베이커리 사용량 속성 결합은 Usage 불성립",
    159: "범퍼 일정표 결합 불명확",
    160: "제과 소견 결합 불명확",
    162: "현장학습 선물 결합 불성립 - Gift",
    163: "네일 폴리시 리트리트 결합 불성립",
    165: "베이글 파도 결합은 Wave 불성립",
    166: "도넛 반지 결합은 Ring 다의어 불성립",
    167: "에스프레소 카운터 결합은 Counter 다의어 불성립",
    168: "라떼 로그 결합은 Log 불성립",
    169: "칫솔 카드 결합은 Card 다의어 불성립",
    170: "스노클링 점수 결합은 Score 불성립",
    171: "칵테일 수준 속성 결합은 Level 불성립",
    172: "치약 요율 속성 결합은 Rate 불성립",
    173: "카약 초안 결합은 Draft 다의어 불성립",
    174: "바리스타 견적 결합은 서비스 견적 결합 불명확",
    175: "구강청격 주문 결합은 Order 다의어 불성립",
    176: "폭포 코드 결합은 Code 불성립",
    177: "펍 패스 결합은 Pass 다의어 불성립",
    179: "일몰 잔표 결합은 Stub 불성립",
    180: "스테이크하우스 게시물 결합은 Bulletin 다의어 불성립",
    181: "스마일 요약 결합은 Brief 다의어 불성립",
    182: "수변 자문 결합은 Advisory 추상 불성립",
    183: "스시 요금 속성 결합은 Fee 불성립",
    184: "호흡 품목 결합은 Item 다의어 불성립",
    186: "타코 대출 결합은 Loan 불성립",
    187: "코골이 합계 결합은 Sum 불성립",
    188: "해변 기금 결합은 Fund 불성립",
    189: "면집 의무 결합은 Duty 불성립",
    190: "교합 수당 결합은 Allowance 불성립",
    191: "전망 가치 속성 결합은 Value 불성립",
    192: "해산물 번호 속성 결합은 Number 불성립",
    193: "치과 버전 속성 결합은 Version 불성립",
    194: "배낭여행 규칙 결합은 Rule 불성립",
    195: "교정의 속성 결합은 Attribute 불성립",
    196: "패러세일링 형식 결합은 Format 불성립",
    197: "치위 마커 결합은 Marker 불성립",
    198: "야생동물 이자 결합은 Interest 불성립",
    199: "치실 기한 결합은 Due 불성립",
    200: "라군 할인 결합은 Discount 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 33, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 167, len(REJECT_REASON)
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
