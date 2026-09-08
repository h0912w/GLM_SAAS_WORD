import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk36_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk36_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.6, "세탁 수거 배달 서비스 전단으로 실재 (Flyer 라인)"),
    6: (0.6, "알레르기 유발물질 관리 핸드북으로 실재 (Handbook 라인)"),
    8: (0.6, "육아 낮잠 교육 세미나로 실재 (Seminar 라인)"),
    12: (0.6, "턴오버 청소 서비스 전단으로 실재 (Flyer 라인)"),
    17: (0.6, "바닥재 시공 세미나로 실재 (Seminar 라인)"),
    32: (0.7, "보험 수익자 지정 교육으로 실재 (도메인 실무 개념)"),
    33: (0.6, "연공제 이해 핸드북으로 실재 (Handbook 라인)"),
    37: (0.6, "저자 집필 출간 세미나로 실재 (Seminar 라인)"),
    55: (0.6, "스테이크하우스 케이터링 견적으로 성립 (Estimate 라인 준용)"),
    60: (0.6, "보드워크 명소 이용권으로 성립 (Voucher 라인 준용)"),
    64: (0.6, "면집 예약 확정서로 성립 (Confirmation 라인)"),
    86: (0.6, "구취 진료 매뉴얼로 실재 (Manual 라인)"),
    88: (0.6, "치주염 스케치 자료로 실재 (Sketch 라인)"),
    105: (0.6, "영양 교육 세미나로 실재 (Seminar 라인)"),
    109: (0.6, "잔디 깎기 서비스 전단으로 실재 (Flyer 라인)"),
    113: (0.6, "급여 압류 처리 세미나로 실재 (Seminar 라인)"),
    117: (0.6, "사진 촬영 서비스 전단으로 실재 (Flyer 라인)"),
    128: (0.7, "홈 스테이징 교육으로 실재 (도메인 실무 개념)"),
    129: (0.6, "보험 수익자 지정 핸드북으로 실재 (Handbook 라인)"),
    136: (0.6, "배기 정비 서비스 전단으로 실재 (Flyer 라인)"),
    183: (0.6, "구취 진료 워크시트로 실재 (Worksheet 라인)"),
    198: (0.6, "관수 시공 서비스 전단으로 실재 (Flyer 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "방제 계약 선물 결합 불성립 - Gift",
    2: "관수 리트리트 결합 불성립",
    3: "용품 공급 토너먼트 결합은 Supply 추상 불성립",
    5: "주행거리 속성 결합은 Mileage 불명확",
    7: "영양 권고 결합 불명확",
    9: "요양 인력 배치 선물 결합 불성립 - Gift",
    10: "흰개미 방제 리트리트 결합 불성립",
    11: "잔디 깎기 토너먼트 결합 불성립",
    13: "운송 경로 핸드북 결합은 Lane 다의어 불명확",
    14: "부동산 점검 일정표 결합은 Walkthrough 다의어 불명확",
    15: "배상책임 소견 결합 불명확",
    16: "급여 압류 권고 결합 불명확",
    18: "선택 과목 선물 결합은 Elective 불명확",
    19: "주민 리트리트 결합은 Resident 불성립",
    20: "사진 촬영 토너먼트 결합 불성립",
    21: "평점 전단 결합은 Rating 다의어 불명확",
    22: "카페 규모 속성 결합은 Scale 다의어 불성립",
    23: "다이너 명단 결합은 Roster 다의어 불성립",
    24: "비스트로 색인 결합은 Index 다의어 불성립",
    25: "피자집 비용 속성 결합은 Cost 불성립",
    26: "데리 마커 결합은 Marker 불성립",
    27: "디저트 위젯 결합은 Widget 불성립",
    28: "포장 물량 속성 결합은 Volume 불성립",
    29: "브런치 예치금 결합은 Deposit 불성립",
    30: "베이커리 범위 속성 결합은 Range 불성립",
    31: "제과 센서 결합은 Sensor 불성립",
    34: "방수 일정표 결합 불명확",
    35: "멘토링 소견 결합 불명확",
    36: "통행금지 권고 결합은 Curfew 불명확",
    38: "공지 리트리트 결합은 Notice 다의어 불성립",
    39: "배기 시스템 토너먼트 결합 불성립",
    40: "베이글 전단 결합 불명확",
    41: "도넛 코어 결합은 Core 추상 불성립",
    42: "에스프레소 관리인 결합은 Keeper 불성립",
    43: "라떼 사무실 결합은 Office 불성립",
    44: "칫솔 부스 결합은 Booth 불성립",
    45: "스노클링 게시 결합은 Post 다의어 불성립",
    46: "칵테일 전광판 결합은 Ticker 불성립",
    47: "치약 선 결합은 Line 다의어 불성립",
    48: "카약 보고서 결합은 Report 불성립",
    49: "바리스타 점수 결합은 Score 불성립",
    50: "구강청격 메모 결합은 Note 다의어 불성립",
    51: "폭포 상태 결합은 Status 다의어 불성립",
    52: "펍 갱신 결합은 Update 불성립",
    53: "마우스가드 피드 결합은 Feed 다의어 불성립",
    54: "일몰 요약 결합은 Summary 불성립",
    56: "스마일 주문 결합은 Order 다의어 불성립",
    57: "수변 영수증 결합은 Receipt 불성립",
    58: "스시 샘플 결합은 Sample 다의어 불성립",
    59: "호흡 슬롯 결합은 Slot 불성립",
    61: "타코 한도 결합은 Quota 불성립",
    62: "코골이 탭 결합은 Tab 다의어 불성립",
    63: "해변 요약 결합은 Brief 다의어 불성립",
    65: "교합 요약 결합은 Recap 불성립",
    66: "전망 요금 속성 결합은 Fee 불성립",
    67: "해산물 비용 속성 결합은 Cost 불성립",
    68: "치과 가격 속성 결합은 Price 불성립",
    69: "배낭여행 세금 결합은 Tax 불성립",
    70: "교정의 기금 결합은 Fund 불성립",
    71: "패러세일링 판매 결합은 Sale 다의어 불성립",
    72: "치위 관세 결합은 Tariff 불성립",
    73: "야생동물 지분 결합은 Stake 불성립",
    74: "치실 번호 속성 결합은 Number 불성립",
    75: "라군 링크 결합은 Link 불성립",
    76: "치석 식별자 결합은 Identifier 불성립",
    77: "빙하 속성 결합은 Attribute 불성립",
    78: "불소 일련번호 결합은 Serial 불성립",
    79: "화산 서명 결합은 Signature 불성립",
    80: "실런트 이자 결합은 Interest 불성립",
    81: "당일여행 과세 결합은 Levy 불성립",
    82: "치은염 할인 결합은 Discount 불성립",
    83: "요트 선수금 결합은 Advance 불성립",
    84: "이갈이 리딤 결합은 Redemption 불성립",
    85: "산책로 시험 결합은 Trial 다의어 불성립",
    87: "우릴 도해 결합 불명확",
    89: "사막 렌더링 결합은 Rendering 불성립",
    90: "부정교합 키트 결합은 Kit 불성립",
    91: "와이너리 메시지 결합은 Message 불성립",
    92: "치수과 위젯 결합은 Widget 불성립",
    93: "치주 계산기 결합은 Calculator 추상 불성립",
    94: "트레이드 교육 결합은 Trade 다의어 불명확",
    95: "수의 처방 일정표 결합 불명확",
    96: "치료 소견 결합은 Treatment 추상 불성립",
    97: "결제 세미나 결합은 Billing 추상 불성립",
    98: "돌봄 선물 결합은 Care 추상 불성립",
    99: "방제 계약 리트리트 결합 불성립",
    100: "관수 토너먼트 결합 불성립",
    101: "용품 공급 전단 결합은 Supply 불명확",
    102: "물류 교육 결합은 Logistics 추상 불명확",
    103: "주행거리 핸드북 결합은 Mileage 불명확",
    104: "알레르기 일정표 결합 불명확",
    106: "아기 낮잠 선물 결합 불성립 - Gift",
    107: "요양 인력 배치 리트리트 결합 불성립",
    108: "흰개미 방제 토너먼트 결합 불성립",
    110: "운송 경로 일정표 결합은 Lane 다의어 불명확",
    111: "부동산 점검 소견 결합은 Walkthrough 다의어 불명확",
    112: "배상책임 권고 결합 불명확",
    114: "바닥재 시공 선물 결합 불성립 - Gift",
    115: "선택 과목 리트리트 결합은 Elective 불명확",
    116: "주민 토너먼트 결합은 Resident 불성립",
    118: "카페 경로 결합은 Route 불성립",
    119: "다이너 알림 결합은 Alert 불성립",
    120: "비스트로 티켓 결합 불성립",
    121: "피자집 가격 속성 결합은 Price 불성립",
    122: "데리 잔액 결합은 Balance 불성립",
    123: "디저트 저장소 결합은 Repository 불성립",
    124: "포장 진단 결합은 Diagnostic 불성립",
    125: "브런치 자격 결합은 Certification 추상 불성립",
    126: "베이커리 한도 속성 결합은 Limit 불성립",
    127: "제과 접수처 결합은 Reception 불성립",
    130: "연공 일정표 결합 불명확",
    131: "방수 소견 결합 불명확",
    132: "멘토링 권고 결합 불명확",
    133: "통행금지 세미나 결합은 Curfew 불명확",
    134: "저자 선물 결합 불성립 - Gift",
    135: "공지 토너먼트 결합은 Notice 다의어 불성립",
    137: "베이글 추적기 결합은 Tracker 추상 불성립",
    138: "도넛 원장 결합은 Ledger 불성립",
    139: "에스프레소 관리자 결합은 Manager 추상 불성립",
    140: "라떼 계수기 결합은 Counter 다의어 불성립",
    141: "칫솔 키오스크 결합은 Kiosk 불성립",
    142: "스노클링 항구 결합은 Harbor 불성립",
    143: "칵테일 선 결합은 Line 다의어 불성립",
    144: "치약 창 결합은 Window 다의어 불성립",
    145: "카약 기록 결합은 Log 다의어 불성립",
    146: "바리스타 메모 결합은 Note 다의어 불성립",
    147: "구강청격 태그 결합은 Tag 다의어 불성립",
    148: "폭포 뷰 결합은 View 다의어 불성립",
    149: "펍 피드 결합은 Feed 다의어 불성립",
    150: "마우스가드 초안 결합은 Draft 다의어 불성립",
    151: "일몰 타임라인 결합 불성립",
    152: "스테이크하우스 주문 결합은 Order 다의어 불성립",
    153: "스마일 청구 결합은 Bill 불명확",
    154: "수변 코드 결합은 Code 불성립",
    155: "스시 슬롯 결합은 Slot 불성립",
    156: "호흡 패스 결합은 Pass 다의어 불성립",
    157: "보드워크 배지 결합은 Badge 다의어 불성립",
    158: "타코 탭 결합은 Tab 다의어 불성립",
    159: "코골이 게시물 결합은 Bulletin 다의어 불성립",
    160: "해변 회람 결합은 Circular 다의어 불성립",
    161: "면집 요약 결합은 Recap 불성립",
    162: "교합 항목 결합은 Entry 다의어 불성립",
    163: "전망 품목 결합은 Item 다의어 불성립",
    164: "해산물 가격 속성 결합은 Price 불성립",
    165: "치과 요금 속성 결합은 Fare 불성립",
    166: "배낭여행 대출 결합은 Loan 불성립",
    167: "교정의 현금 결합은 Cash 불성립",
    168: "패러세일링 청구 결합은 Charge 다의어 불성립",
    169: "치위 가치 속성 결합은 Value 불성립",
    170: "야생동물 마진 속성 결합은 Margin 불성립",
    171: "치실 버전 결합은 Version 불성립",
    172: "라군 규칙 결합은 Rule 불성립",
    173: "치석 분류 결합은 Category 불성립",
    174: "빙하 필드 결합은 Field 불성립",
    175: "불소 토큰 결합은 Token 불성립",
    176: "화산 마커 결합은 Marker 불성립",
    177: "실런트 자산 결합은 Asset 불성립",
    178: "당일여행 기한 결합은 Due 불성립",
    179: "치은염 연체 결합은 Arrears 불성립",
    180: "요트 벌칙 결합은 Penalty 불성립",
    181: "이갈이 연장 결합은 Extension 불성립",
    182: "산책로 그래프 결합은 Graph 불성립",
    184: "우릴 도식 결합 불명확",
    185: "치주염 개요 결합은 Outline 불성립",
    186: "사막 통지 결합은 Notification 불성립",
    187: "부정교합 횟수 결합은 Count 불성립",
    188: "와이너리 총액 결합은 Total 불성립",
    189: "치수과 저장소 결합은 Repository 불성립",
    190: "치주 변환기 결합은 Converter 추상 불성립",
    191: "명찰 교육 결합은 Badge 다의어 불명확",
    192: "트레이드 핸드북 결합은 Trade 다의어 불명확",
    193: "수의 처방 소견 결합 불명확",
    194: "치료 권고 결합은 Treatment 추상 불성립",
    195: "결제 선물 결합은 Billing 추상 불성립",
    196: "돌봄 리트리트 결합은 Care 추상 불성립",
    197: "방제 계약 토너먼트 결합 불성립",
    199: "물류 핸드북 결합은 Logistics 추상 불명확",
    200: "주행거리 일정표 결합은 Mileage 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 22, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 178, len(REJECT_REASON)
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
