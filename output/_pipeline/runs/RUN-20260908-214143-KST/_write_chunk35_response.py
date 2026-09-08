import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk34_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk34_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    7: (0.7, "영양 교육으로 실재 (도메인 실무 개념)"),
    8: (0.6, "아기 낮잠 훈련 핸드북으로 실재 (Handbook 라인)"),
    17: (0.7, "급여 압류 처리 교육으로 실재 (도메인 실무 개념)"),
    18: (0.6, "바닥재 시공 핸드북으로 실재 (Handbook 라인)"),
    34: (0.6, "브런치집 청구서로 성립 (Invoice 라인)"),
    38: (0.6, "저자 집필 출간 핸드북으로 실재 (Handbook 라인)"),
    74: (0.6, "배낭여행 계획으로 성립 (Plan 라인)"),
    93: (0.6, "치주염 실무 워크시트로 실재 (Worksheet 라인)"),
    95: (0.6, "부정교합 스케치 자료로 실재 (Sketch 라인)"),
    108: (0.6, "영양 교육 핸드북으로 실재 (Handbook 라인)"),
    117: (0.7, "배상책임 보험 교육으로 실재 (도메인 실무 개념)"),
    118: (0.6, "급여 압류 처리 핸드북으로 실재 (Handbook 라인)"),
    137: (0.7, "멘토링 프로그램 교육으로 실재 (도메인 실무 개념)"),
    171: (0.6, "전망대 예약 확정서로 성립 (Confirmation 라인)"),
    193: (0.6, "치주염 도해 자료로 실재 (Diagram 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "용품 공급 권고 결합은 Supply 추상 불성립",
    2: "세탁 수거 배달 세미나 결합 불명확",
    3: "서비스 선물 결합은 Service 다의어 불성립",
    4: "제품 판매 리트리트 결합 불성립",
    5: "복약 순응도 토너먼트 결합 불성립",
    6: "선석 전단 결합 불명확",
    9: "요양 인력 배치 일정표 결합 불명확",
    10: "흰개미 방제 소견 결합 불명확",
    11: "잔디 깎기 권고 결합 불명확",
    12: "객실 턴오버 세미나 결합 불명확",
    13: "세탁 접수 선물 결합 불성립 - Gift",
    14: "장례 사전 계획 리트리트 결합 불성립",
    15: "일정 토너먼트 결합은 Schedule 추상 불성립",
    16: "처방 상담 전단 결합 불명확",
    19: "선택 과목 일정표 결합은 Elective 불명확",
    20: "거주민 소견 결합은 Resident 불성립",
    21: "사진 촬영 권고 결합 불명확",
    22: "평점 세미나 결합은 Rating 다의어 불명확",
    23: "면접관 선물 결합 불성립 - Gift",
    24: "와이파이 리트리트 결합 불성립",
    25: "차량 진단 토너먼트 결합 불성립",
    26: "서빙 전단 결합 불명확",
    27: "카페 구역 결합은 Zone 불성립",
    28: "다이너 키오스크 결합은 Kiosk 불성립",
    29: "비스트로 초안 결합은 Draft 다의어 불성립",
    30: "피자집 요금 속성 결합은 Fee 불성립",
    31: "데리 형식 결합은 Format 불성립",
    32: "디저트 키트 결합은 Kit 불성립",
    33: "포장 참고 결합은 Reference 불성립",
    35: "베이커리 크기 속성 결합은 Size 불성립",
    36: "제과 습도 속성 결합은 Humidity 불성립",
    37: "통행금지 교육 결합은 Curfew 불명확",
    39: "공지 소견 결합은 Notice 다의어 불성립",
    40: "배기 시스템 권고 결합 불명확",
    41: "베이글 세미나 결합 불명확",
    42: "수의 혈액 검사 선물 결합 불성립 - Gift",
    43: "틀니 리트리트 결합 불성립",
    44: "배변 훈련 토너먼트 결합 불성립",
    45: "헤어 커트 전단 결합 불명확",
    46: "도넛 지점 결합은 Point 불성립",
    47: "에스프레소 고리 결합은 Ring 불성립",
    48: "라떼 달력 결합 불성립",
    49: "칫솔 탐색기 결합은 Locator 불성립",
    50: "스노클링 계수기 결합은 Counter 다의어 불성립",
    51: "칵테일 차트 결합은 Chart 불성립",
    52: "치약 창고 결합은 Bin 다의어 불성립",
    53: "카약 전광판 결합은 Ticker 불성립",
    54: "바리스타 서식 결합은 Form 다의어 불성립",
    55: "구강청격 카드 결합은 Card 다의어 불성립",
    56: "폭포 점수 결합은 Score 불성립",
    57: "펍 역사 결합 불성립",
    58: "마우스가드 파일 결합은 File 다의어 불성립",
    59: "일몰 요율 속성 결합은 Rate 불성립",
    60: "스테이크하우스 타임라인 결합 불성립",
    61: "스마일 알림 결합은 Reminder 불성립",
    62: "수변 티켓 결합 불명확",
    63: "스시 코드 결합은 Code 불성립",
    64: "호흡 목록 결합은 List 불성립",
    65: "보드워크 전표 결합은 Slip 다의어 불성립",
    66: "타코 배지 결합은 Badge 다의어 불성립",
    67: "코골이 전표 결합은 Stub 다의어 불성립",
    68: "해변 메모 결합은 Memo 다의어 불성립",
    69: "면집 요약 결합은 Brief 다의어 불성립",
    70: "교합 회람 결합은 Circular 다의어 불성립",
    71: "전망 청원 결합은 Petition 불성립",
    72: "해산물 요금 속성 결합은 Fee 불성립",
    73: "치과 품목 결합은 Item 다의어 불성립",
    75: "교정의 세금 결합은 Tax 불성립",
    76: "패러세일링 합계 결합은 Sum 불성립",
    77: "치위 판매 결합은 Sale 다의어 불성립",
    78: "야생동물 의무 결합은 Duty 불성립",
    79: "치실 가치 속성 결합은 Value 불성립",
    80: "라군 마진 속성 결합은 Margin 불성립",
    81: "치석 버전 결합은 Version 불성립",
    82: "빙하 규칙 결합은 Rule 불성립",
    83: "불소 분류 결합은 Category 불성립",
    84: "화산 필드 결합은 Field 불성립",
    85: "실런트 토큰 결합은 Token 불성립",
    86: "당일여행 마커 결합은 Marker 불성립",
    87: "치은염 자산 결합은 Asset 불성립",
    88: "요트 기한 결합은 Due 불성립",
    89: "이갈이 연체 결합은 Arrears 불성립",
    90: "산책로 벌칙 결합은 Penalty 불성립",
    91: "구취 연장 결합은 Extension 불성립",
    92: "우릴 그래프 결합은 Graph 불성립",
    94: "사막 도해 결합 불명확",
    96: "와이너리 렌더링 결합은 Rendering 불성립",
    97: "치수과 키트 결합은 Kit 불성립",
    98: "치주 총액 결합은 Total 불성립",
    99: "결제 핸드북 결합은 Billing 추상 불성립",
    100: "돌봄 일정표 결합은 Care 추상 불성립",
    101: "방제 계약 소견 결합 불명확",
    102: "관수 시스템 권고 결합 불명확",
    103: "용품 공급 세미나 결합은 Supply 추상 불성립",
    104: "세탁 수거 배달 선물 결합 불성립 - Gift",
    105: "서비스 리트리트 결합은 Service 다의어 불성립",
    106: "제품 판매 토너먼트 결합 불성립",
    107: "복약 순응도 전단 결합 불명확",
    109: "아기 낮잠 훈련 일정표 결합 불명확",
    110: "요양 인력 배치 소견 결합 불명확",
    111: "흰개미 방제 권고 결합 불명확",
    112: "잔디 깎기 세미나 결합 불명확",
    113: "객실 턴오버 선물 결합 불성립 - Gift",
    114: "세탁 접수 리트리트 결합 불성립",
    115: "장례 사전 계획 토너먼트 결합 불성립",
    116: "일정 전단 결합은 Schedule 추상 불성립",
    119: "바닥재 시공 일정표 결합 불명확",
    120: "선택 과목 소견 결합은 Elective 불명확",
    121: "거주민 권고 결합은 Resident 불성립",
    122: "사진 촬영 세미나 결합 불명확",
    123: "평점 선물 결합은 Rating 다의어 불성립",
    124: "면접관 리트리트 결합 불성립",
    125: "와이파이 토너먼트 결합 불성립",
    126: "차량 진단 전단 결합 불명확",
    127: "카페 관문 결합은 Portal 추상 불성립",
    128: "다이너 만 결합은 Bay 다의어 불성립",
    129: "비스트로 요약 결합은 Summary 불성립",
    130: "피자집 품목 결합은 Item 다의어 불성립",
    131: "데리 일련번호 결합은 Serial 불성립",
    132: "디저트 횟수 결합은 Count 불성립",
    133: "포장 예측 결합은 Forecast 불성립",
    134: "브런치 갱신 결합은 Renewal 불성립",
    135: "베이커리 길이 속성 결합은 Length 불성립",
    136: "제과 회차 결합은 Episode 불성립",
    138: "통행금지 핸드북 결합은 Curfew 불명확",
    139: "저자 일정표 결합 불명확",
    140: "공지 권고 결합은 Notice 다의어 불성립",
    141: "배기 시스템 세미나 결합 불명확",
    142: "베이글 선물 결합 불성립 - Gift",
    143: "수의 혈액 검사 리트리트 결합 불성립",
    144: "틀니 토너먼트 결합 불성립",
    145: "배변 훈련 전단 결합 불명확",
    146: "도넛 지도 결합은 Map 불성립",
    147: "에스프레소 관문 결합은 Gate 불성립",
    148: "라떼 디렉터리 결합은 Directory 다의어 불성립",
    149: "칫솔 탐색기 결합은 Finder 불성립",
    150: "스노클링 부스 결합은 Booth 불성립",
    151: "칵테일 창고 결합은 Bin 다의어 불성립",
    152: "치약 여권 결합은 Passport 다의어 불성립",
    153: "카약 선 결합은 Line 불성립",
    154: "바리스타 카드 결합은 Card 다의어 불성립",
    155: "구강청격 시트 결합은 Sheet 다의어 불성립",
    156: "폭포 메모 결합은 Note 다의어 불성립",
    157: "펍 파일 결합은 File 다의어 불성립",
    158: "마우스가드 수준 속성 결합은 Level 불성립",
    159: "일몰 갱신 결합은 Update 불성립",
    160: "스테이크하우스 알림 결합은 Reminder 불성립",
    161: "스마일 색인 결합은 Index 다의어 불성립",
    162: "수변 견적 결합은 Estimate 불성립",
    163: "스시 목록 결합은 List 불성립",
    164: "호흡 식탁 결합은 Table 불성립",
    165: "보드워크 샘플 결합은 Sample 다의어 불성립",
    166: "타코 전표 결합은 Stub 다의어 불성립",
    167: "코골이 정산 결합은 Statement 다의어 불성립",
    168: "해변 한도 결합은 Quota 속성어 불성립",
    169: "면집 회람 결합은 Circular 다의어 불성립",
    170: "교합 권고 결합은 Advisory 불성립",
    172: "해산물 품목 결합은 Item 다의어 불성립",
    173: "치과 단위 결합은 Unit 다의어 불성립",
    174: "배낭여행 비용 속성 결합은 Cost 불성립",
    175: "교정의 대출 결합은 Loan 불성립",
    176: "패러세일링 부채 결합은 Debt 불성립",
    177: "치위 청구 결합은 Charge 다의어 불성립",
    178: "야생동물 수당 결합은 Allowance 불성립",
    179: "치실 지분 결합은 Stake 불성립",
    180: "라군 벌금 결합은 Fine 불성립",
    181: "치석 링크 결합은 Link 불성립",
    182: "빙하 세부 결합은 Detail 불성립",
    183: "불소 속성 결합은 Attribute 불성립",
    184: "화산 형식 결합은 Format 불성립",
    185: "실런트 서명 결합은 Signature 불성립",
    186: "당일여행 잔액 결합은 Balance 불성립",
    187: "치은염 과세 결합은 Levy 불성립",
    188: "요트 보조금 결합은 Subsidy 불성립",
    189: "이갈이 선수금 결합은 Advance 불성립",
    190: "산책로 가산율 결합은 Markup 불성립",
    191: "구취 시험 결합은 Trial 다의어 불성립",
    192: "우릴 라벨 결합은 Label 불성립",
    194: "사막 배치도 결합은 Layout 불성립",
    195: "부정교합 개요 결합은 Outline 불성립",
    196: "와이너리 통지 결합은 Notification 불성립",
    197: "치수과 횟수 결합은 Count 불성립",
    198: "치주 위젯 결합은 Widget 불성립",
    199: "치료 교육 결합은 Treatment 추상 불명확",
    200: "결제 일정표 결합은 Billing 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 15, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 185, len(REJECT_REASON)
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
