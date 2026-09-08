import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk33_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk33_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    4: (0.7, "요양 인력 배치 교육으로 실재 (도메인 실무 개념)"),
    5: (0.6, "흰개미 방제 핸드북으로 실재 (Handbook 라인)"),
    9: (0.6, "장례 사전 계획 세미나로 실재 (Seminar 라인)"),
    31: (0.6, "브런치 예약 관리로 성립 (Appointment 예약 독해)"),
    32: (0.6, "신입 직원 온보딩 프로그램으로 실재 (실무 개념 독해)"),
    44: (0.6, "커피 명소 트레일 코스로 실재 (Trail 물리 코스 라인)"),
    60: (0.6, "초밥집 청구서로 성립 (Bill 라인)"),
    92: (0.6, "부정교합 도해 자료로 실재 (Schematic 라인)"),
    97: (0.6, "방제 계약 핸드북으로 실재 (Handbook 라인)"),
    105: (0.7, "아기 낮잠 훈련 교육으로 실재 (도메인 실무 개념)"),
    106: (0.6, "요양 인력 배치 핸드북으로 실재 (Handbook 라인)"),
    115: (0.7, "바닥재 시공 교육으로 실재 (도메인 실무 개념)"),
    125: (0.6, "카페 클래스 센터로 실재 (Center 클래스 공간 라인)"),
    126: (0.6, "다이너 부스 좌석으로 성립 (Booth 실물 공간 라인)"),
    135: (0.7, "저자 집필 출간 교육으로 실재 (도메인 실무 개념)"),
    161: (0.6, "초밥집 영수증으로 성립 (Receipt 라인)"),
    164: (0.6, "타코 트럭 이용 바우처로 성립 (Voucher 라인)"),
    191: (0.6, "치주염 관리 매뉴얼로 실재 (Manual 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "제품 판매 세미나 결합 불명확",
    2: "복약 순응도 선물 결합 불성립 - Gift",
    3: "선석 리트리트 결합 불성립",
    6: "잔디 깎기 일정표 결합 불명확",
    7: "객실 턴오버 소견 결합 불명확",
    8: "세탁 접수 권고 결합 불명확",
    10: "일정 선물 결합은 Schedule 추상 불성립",
    11: "처방 상담 리트리트 결합 불성립",
    12: "컨테이너 토너먼트 결합 불성립",
    13: "자격 인증 전단 결합 불명확",
    14: "선택 과목 교육 결합은 Elective 불명확",
    15: "거주민 핸드북 결합은 Resident 불명확",
    16: "사진 촬영 일정표 결합 불명확",
    17: "평점 소견 결합은 Rating 다의어 불명확",
    18: "면접관 권고 결합 불명확",
    19: "와이파이 세미나 결합 불명확",
    20: "차량 진단 선물 결합 불성립 - Gift",
    21: "서빙 리트리트 결합 불성립",
    22: "구충제 토너먼트 결합 불성립",
    23: "치실 전단 결합 불명확",
    24: "카페 단말 결합은 Terminal 불성립",
    25: "다이너 계수기 결합은 Counter 다의어 불성립",
    26: "비스트로 갱신 결합은 Update 불성립",
    27: "피자집 정리 결합은 Recap 다의어 불성립",
    28: "데리 속성 결합은 Attribute 불성립",
    29: "디저트 렌더링 결합은 Rendering 불성립",
    30: "포장 사본 결합은 Copy 다의어 불성립",
    33: "제과 용도 결합은 Usage 불성립",
    34: "공지 핸드북 결합은 Notice 다의어 불명확",
    35: "배기 시스템 일정표 결합 불명확",
    36: "베이글 소견 결합 불명확",
    37: "수의 혈액 검사 권고 결합 불명확",
    38: "틀니 세미나 결합 불명확",
    39: "배변 훈련 선물 결합 불성립 - Gift",
    40: "헤어 커트 리트리트 결합 불성립",
    41: "복약 상담 토너먼트 결합 불성립",
    42: "커패시터 전단 결합 불명확",
    43: "도넛 파도 결합은 Wave 추상 불성립",
    45: "라떼 일지 결합은 Journal 다의어 불성립",
    46: "칫솔 달력 결합 불성립",
    47: "스노클링 탐색기 결합은 Finder 불성립",
    48: "칵테일 명단 결합은 Roster 다의어 불성립",
    49: "치약 경보 결합은 Alert 불성립",
    50: "카약 여권 결합은 Passport 다의어 불성립",
    51: "바리스타 리포트 결합 불성립",
    52: "구강청격 기록 결합은 Log 불성립",
    53: "폭포 시트 결합은 Sheet 다의어 불성립",
    54: "펍 상태 결합은 Status 불성립",
    55: "마우스가드 뷰 결합은 View 추상 불성립",
    56: "일몰 파일 결합은 File 다의어 불성립",
    57: "스테이크하우스 초안 결합은 Draft 다의어 불성립",
    58: "스마일 요약 결합은 Summary 불성립",
    59: "수변 알림 결합은 Reminder 불성립",
    61: "호흡 영수증 결합 불성립",
    62: "보드워크 목록 결합은 List 불성립",
    63: "타코 통행 결합은 Pass 다의어 불성립",
    64: "코골이 바우처 결합 불성립",
    65: "해변 전표 결합은 Stub 다의어 불성립",
    66: "면집 탭 결합은 Tab 다의어 불성립",
    67: "교합 회람 결합은 Bulletin 다의어 불성립",
    68: "전망 회람 결합은 Circular 다의어 불성립",
    69: "해산물 정리 결합은 Recap 다의어 불성립",
    70: "치과 입장 결합은 Entry 다의어 불성립",
    71: "배낭여행 품목 결합은 Item 다의어 불성립",
    72: "교정의 가격 속성 결합은 Price 불성립",
    73: "패러세일링 세금 결합은 Tax 불성립",
    74: "치위 기금 결합은 Fund 불성립",
    75: "야생동물 판매 결합은 Sale 다의어 불성립",
    76: "치실 수당 결합은 Allowance 불성립",
    77: "라군 가치 속성 결합은 Value 불성립",
    78: "치석 벌금 결합은 Fine 불성립",
    79: "빙하 버전 결합은 Version 불성립",
    80: "불소 세부 결합은 Detail 불성립",
    81: "화산 분류 결합은 Category 불성립",
    82: "실런트 형식 결합은 Format 불성립",
    83: "당일여행 토큰 결합은 Token 불성립",
    84: "치은염 잔액 결합은 Balance 불성립",
    85: "요트 자산 결합은 Asset 불성립",
    86: "이갈이 보조금 결합은 Subsidy 불성립",
    87: "산책로 연체 결합은 Arrears 불성립",
    88: "구취 가산율 결합은 Markup 불성립",
    89: "우릴 연장 결합은 Extension 불성립",
    90: "치주염 라벨 결합은 Label 불성립",
    91: "사막 워크시트 결합 불명확",
    93: "와이너리 스케치 결합 불명확",
    94: "치수과 렌더링 결합은 Rendering 불성립",
    95: "치주 횟수 결합은 Count 불성립",
    96: "돌봄 교육 결합은 Care 추상 불명확",
    98: "관수 시스템 일정표 결합 불명확",
    99: "용품 공급 소견 결합은 Supply 추상 불성립",
    100: "세탁 수거 배달 권고 결합 불명확",
    101: "서비스 세미나 결합은 Service 다의어 불성립",
    102: "제품 판매 선물 결합 불성립 - Gift",
    103: "복약 순응도 리트리트 결합 불성립",
    104: "선석 토너먼트 결합 불성립",
    107: "흰개미 방제 일정표 결합 불명확",
    108: "잔디 깎기 소견 결합 불명확",
    109: "객실 턴오버 권고 결합 불명확",
    110: "세탁 접수 세미나 결합 불명확",
    111: "장례 사전 계획 선물 결합 불성립 - Gift",
    112: "일정 리트리트 결합은 Schedule 추상 불성립",
    113: "처방 상담 토너먼트 결합 불성립",
    114: "컨테이너 전단 결합 불명확",
    116: "선택 과목 핸드북 결합은 Elective 불명확",
    117: "거주민 일정표 결합은 Resident 불성립",
    118: "사진 촬영 소견 결합 불명확",
    119: "평점 권고 결합은 Rating 다의어 불명확",
    120: "면접관 세미나 결합 불명확",
    121: "와이파이 선물 결합 불성립 - Gift",
    122: "차량 진단 리트리트 결합 불성립",
    123: "서빙 토너먼트 결합 불성립",
    124: "구충제 전단 결합 불명확",
    127: "비스트로 피드 결합은 Feed 추상 불성립",
    128: "피자집 입장 결합은 Entry 다의어 불성립",
    129: "데리 필드 결합은 Field 불성립",
    130: "디저트 통지 결합은 Notification 불성립",
    131: "포장 독해 결합은 Reading 불성립",
    132: "브런치 피드백 결합은 Feedback 불성립",
    133: "베이커리 체크인 결합은 Checkin 불성립",
    134: "제과 상태 결합은 Condition 불성립",
    136: "공지 일정표 결합은 Notice 다의어 불성립",
    137: "배기 시스템 소견 결합 불명확",
    138: "베이글 권고 결합 불명확",
    139: "수의 혈액 검사 세미나 결합 불명확",
    140: "틀니 선물 결합 불성립 - Gift",
    141: "배변 훈련 리트리트 결합 불성립",
    142: "헤어 커트 토너먼트 결합 불성립",
    143: "복약 상담 전단 결합 불명확",
    144: "도넛 경로 결합은 Path 불성립",
    145: "에스프레소 사슬 결합은 Chain 불성립",
    146: "라떼 등록소 결합은 Registry 다의어 불성립",
    147: "칫솔 디렉터리 결합은 Directory 다의어 불성립",
    148: "스노클링 사무실 결합은 Office 불성립",
    149: "칵테일 경보 결합은 Alert 불성립",
    150: "치약 차트 결합은 Chart 불성립",
    151: "카약 로비 결합은 Lobby 불성립",
    152: "바리스타 기록 결합은 Log 위치 추상 불성립",
    153: "구강청격 서식 결합은 Form 다의어 불성립",
    154: "폭포 검사 결합은 Check 불성립",
    155: "펍 뷰 결합은 View 추상 불성립",
    156: "마우스가드 역사 결합 불성립",
    157: "일몰 수준 속성 결합은 Level 불성립",
    158: "스테이크하우스 요약 결합은 Summary 불성립",
    159: "스마일 타임라인 결합 불성립",
    160: "수변 색인 결합은 Index 다의어 불성립",
    162: "호흡 코드 결합은 Code 불성립",
    163: "보드워크 식탁 결합은 travel Table 불성립",
    165: "코골이 배지 결합은 Badge 다의어 불성립",
    166: "해변 정산 결합은 Statement 다의어 불성립",
    167: "면집 회람 결합은 Bulletin 다의어 불성립",
    168: "교합 요약 결합은 Brief 다의어 불성립",
    169: "전망 권고 결합은 Advisory 불성립",
    170: "해산물 입장 결합은 Entry 다의어 불성립",
    171: "치과 요금 속성 결합은 Fee 불성립",
    172: "배낭여행 단위 결합은 Unit 다의어 불성립",
    173: "교정의 운임 속성 결합은 Fare 불성립",
    174: "패러세일링 대출 결합은 Loan 불성립",
    175: "치위 현금 결합은 Cash 불성립",
    176: "야생동물 청구 결합은 Charge 다의어 불성립",
    177: "치실 관세 결합은 Tariff 불성립",
    178: "라군 지분 결합은 Stake 불성립",
    179: "치석 번호 속성 결합은 Number 불성립",
    180: "빙하 링크 결합은 Link 불성립",
    181: "불소 식별자 결합은 Identifier 불성립",
    182: "화산 속성 결합은 Attribute 불성립",
    183: "실런트 일련번호 결합은 Serial 불성립",
    184: "당일여행 서명 결합은 Signature 불성립",
    185: "치은염 이자 결합은 Interest 불성립",
    186: "요트 과세 결합은 Levy 불성립",
    187: "이갈이 할인 결합은 Discount 불성립",
    188: "산책로 선수금 결합은 Advance 불성립",
    189: "구취 상환 결합은 Redemption 불성립",
    190: "우릴 시험 결합은 Trial 다의어 불성립",
    192: "사막 도해 결합 불명확",
    193: "부정교합 배치도 결합은 Layout 불성립",
    194: "와이너리 개요 결합은 Outline 불성립",
    195: "치수과 통지 결합은 Notification 불성립",
    196: "치주 메시지 결합은 Message 불성립",
    197: "결제 교육 결합은 Billing 추상 불명확",
    198: "돌봄 핸드북 결합은 Care 추상 불성립",
    199: "방제 계약 일정표 결합 불명확",
    200: "관수 시스템 소견 결합 불명확",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 18, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 182, len(REJECT_REASON)
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
