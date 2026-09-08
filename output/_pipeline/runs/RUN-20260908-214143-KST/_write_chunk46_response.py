import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk45_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk45_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    5: (0.6, "실런트 도식 학습자료로 실재 (dental 도해 계열)"),
    19: (0.7, "입찰 작성 교육으로 실재 (건설 실무 개념)"),
    20: (0.6, "풀필먼트 운영 핸드북으로 실재 (Handbook 라인)"),
    24: (0.6, "작물 재배 세미나로 실재 (Seminar 라인)"),
    27: (0.6, "브랜딩 서비스 전단으로 실재 (Flyer 라인)"),
    28: (0.6, "채용 후보자 관리 교육으로 실재 (HR 실무 개념)"),
    29: (0.6, "하자보증 핸드북으로 실재 (Handbook 라인)"),
    33: (0.6, "계측기 교정 세미나로 실재 (Seminar 라인)"),
    36: (0.7, "중성화 수술 교육으로 실재 (수의 실무 개념)"),
    37: (0.6, "치아미백 핸드북으로 실재 (Handbook 라인)"),
    41: (0.6, "복약 교육 세미나로 실재 (Seminar 라인)"),
    45: (0.6, "이사 파손 보상 안내 전단으로 실재 (Flyer 라인)"),
    55: (0.7, "뉴스레터 제작 교육으로 실재 (미디어 실무 개념)"),
    56: (0.6, "복리후생 핸드북으로 실재 (Handbook 라인)"),
    75: (0.6, "펍 이용권으로 성립 (Voucher 라인 준용)"),
    111: (0.6, "치주염 실습 워크숍으로 실재 (Workshop 라인)"),
    117: (0.6, "입찰 작성 핸드북으로 실재 (Handbook 라인)"),
    121: (0.6, "가동 중단 대응 세미나로 실재 (Seminar 라인)"),
    124: (0.6, "의원실 주민 안내 전단으로 실재 (Flyer 라인)"),
    125: (0.7, "보험 특약 안내 교육으로 실재 (보험 실무 개념)"),
    126: (0.6, "채용 후보자 관리 핸드북으로 실재 (Handbook 라인)"),
    130: (0.6, "수업 운영 연수 세미나로 실재 (Seminar 라인)"),
    133: (0.6, "후원 안내 전단으로 실재 (Flyer 라인)"),
    135: (0.6, "중성화 수술 핸드북으로 실재 (Handbook 라인)"),
    139: (0.6, "왁싱 기술 세미나로 실재 (Seminar 라인)"),
    143: (0.6, "통번역 서비스 전단으로 실재 (Flyer 라인)"),
    153: (0.6, "포트홀 보수 교육으로 실재 (도로 관리 실무 개념)"),
    154: (0.6, "뉴스레터 제작 핸드북으로 실재 (Handbook 라인)"),
    158: (0.6, "제과 기술 세미나로 실재 (Seminar 라인)"),
    161: (0.6, "네일 서비스 전단으로 실재 (Flyer 라인)"),
    164: (0.6, "커피 키오스크 매장 형태로 실재 (서비스 장소)"),
    179: (0.6, "수변 투어 확인서로 성립 (Confirmation 라인 준용)"),
    200: (0.6, "불소 도포 매뉴얼로 실재 (dental 도해 계열)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "치석 벌칙 결합은 Penalty 불성립",
    2: "빙하 리딤 결합은 Redemption 불성립",
    3: "불소 그래프 결합은 Graph 불성립",
    4: "화산 매뉴얼 결합은 여행 서비스와 결합 불명확",
    6: "당일여행 스케치 결합은 여행 서비스와 결합 불명확",
    7: "치은염 통지 결합은 Notification 불성립",
    8: "요트 횟수 결합은 여행 서비스와 결합 불명확",
    9: "이갈이 위젯 결합은 Widget 불성립",
    10: "산책로 공지 결합은 Announcement 불성립",
    11: "구취 생성기 결합은 Generator 추상 불성립",
    12: "우릴 견적기 결합은 Estimator 추상 불성립",
    13: "치주염 타이머 결합은 Timer 추상 불성립",
    14: "사막 보호자 결합은 Guardian 추상 불성립",
    15: "부정교합 단계 결합은 Stage 다의어 불성립",
    16: "와이너리 연승 속성 결합은 Streak 불성립",
    17: "치수과 추이 속성 결합은 Trend 불성립",
    18: "치주 보증 속성 결합은 Guarantee 불성립",
    21: "어메니티 일정표 결합 불명확",
    22: "등록금 소견 결합은 Tuition 결합 불명확",
    23: "설비 정지 권고 결합 불명확",
    25: "모금 리트리트 결합 불성립",
    26: "주민 대응 토너먼트 결합 불성립",
    30: "재고 보충 일정표 결합 불명확",
    31: "셔틀 소견 결합 불명확",
    32: "수업 운영 권고 결합 불명확",
    34: "윤작 선물 결합 불성립 - Gift",
    35: "후원자 관리 토너먼트 결합 불성립",
    38: "기저귀 일정표 결합 불명확",
    39: "옷장 정리 소견 결합 불명확",
    40: "왁싱 권고 결합 불명확",
    42: "구역 온도 관리 선물 결합 불성립 - Gift",
    43: "잠금 장치 리트리트 결합 불성립",
    44: "통번역 토너먼트 결합 불성립",
    46: "카페 플레이북 결합은 Playbook 추상 불성립",
    47: "다이너 프로필 결합은 Profile 다의어 불성립",
    48: "비스트로 탭 결합은 Tab 다의어 불성립",
    49: "피자집 버전 속성 결합은 Version 불성립",
    50: "델리 도해 결합은 매장 운영과 결합 불명확",
    51: "디저트 비교 속성 결합은 Comparison 불성립",
    52: "포장 바코드 결합은 Barcode 불성립",
    53: "브런치 온보딩 결합은 Onboarding 추상 불성립",
    54: "베이커리 상태 속성 결합은 Condition 불성립",
    57: "민원 일정표 결합 불명확",
    58: "범퍼 소견 결합 불명확",
    59: "제과 권고 결합 불명확",
    60: "치과 마취 선물 결합 불성립 - Gift",
    61: "현장학습 리트리트 결합 불성립",
    62: "네일 폴리시 토너먼트 결합 불성립",
    63: "베이글 경로 결합은 Path 불성립",
    64: "도넛 관문 결합은 Gate 불성립",
    65: "에스프레소 부스 결합은 Booth 다의어 불성립",
    66: "라떼 양식 결합은 Form 다의어 불성립",
    67: "칫솔 시트 결합은 Sheet 다의어 불성립",
    68: "스노클링 노트 결합은 Note 불성립",
    69: "칵테일 요율 속성 결합은 Rate 불성립",
    70: "치약 갱신 결합은 Update 불성립",
    71: "카약 요약 결합은 Summary 불성립",
    72: "바리스타 주문 결합은 Order 다의어 불성립",
    73: "구강청격 청구서 결합은 제품 청구 결합 불명확",
    74: "폭포 목록 결합은 List 불성립",
    76: "마우스가드 배지 결합은 Badge 다의어 불성립",
    77: "일몰 명세서 결합은 Statement 불성립",
    78: "스테이크하우스 요약 결합은 Brief 다의어 불성립",
    79: "스마일 회람 결합은 Circular 다의어 불성립",
    80: "수변 청원 결합은 Petition 불성립",
    81: "스시 품목 결합은 Item 다의어 불성립",
    82: "호흡 단위 결합은 Unit 다의어 불성립",
    83: "보드워크 비용 속성 결합은 Cost 불성립",
    84: "타코 합계 결합은 Sum 불성립",
    85: "코골이 채무 결합은 Debt 불성립",
    86: "해변 현금 결합은 Cash 불성립",
    87: "면집 수당 결합은 Allowance 불성립",
    88: "교합 관세 결합은 Tariff 불성립",
    89: "전망 지분 결합은 Stake 불성립",
    90: "해산물 버전 속성 결합은 Version 불성립",
    91: "치과 링크 결합은 Link 불성립",
    92: "배낭여행 세부 결합은 Detail 불성립",
    93: "교정의 필드 결합은 Field 불성립",
    94: "패러세일링 일련번호 결합은 Serial 불성립",
    95: "치위 잔액 결합은 Balance 불성립",
    96: "야생동물 자산 결합은 Asset 불성립",
    97: "치실 보조금 결합은 Subsidy 불성립",
    98: "라군 연체 결합은 Arrears 불성립",
    99: "치석 가산율 결합은 Markup 불성립",
    100: "빙하 연장 결합은 Extension 불성립",
    101: "불소 라벨 결합은 Label 불성립",
    102: "화산 워크시트 결합은 여행 서비스와 결합 불명확",
    103: "실런트 배치도 결합은 Layout 불성립",
    104: "당일여행 개요 결합은 여행 서비스와 결합 불명확",
    105: "치은염 키트 결합은 Kit 불성립",
    106: "요트 메시지 결합은 여행 서비스와 결합 불명확",
    107: "이갈이 저장소 결합은 Repository 불성립",
    108: "산책로 계산기 결합은 Calculator 추상 불성립",
    109: "구취 기록기 결합은 Recorder 추상 불성립",
    110: "우릴 점검기 결합은 Checker 추상 불성립",
    112: "사막 조력자 결합은 Helper 추상 불성립",
    113: "부정교합 결과 속성 결합은 Result 불성립",
    114: "와이너리 순위 속성 결합은 Rank 불성립",
    115: "치수과 비교 속성 결합은 Comparison 불성립",
    116: "치주 기록 속성 결합은 Record 불성립",
    118: "풀필먼트 일정표 결합 불명확",
    119: "어메니티 소견 결합 불명확",
    120: "등록금 권고 결합은 Tuition 결합 불명확",
    122: "작물 선물 결합 불성립 - Gift",
    123: "모금 토너먼트 결합 불성립",
    127: "하자보증 일정표 결합 불명확",
    128: "재고 보충 소견 결합 불명확",
    129: "셔틀 권고 결합 불명확",
    131: "계측기 교정 선물 결합 불성립 - Gift",
    132: "윤작 리트리트 결합 불성립",
    134: "외식 교육 결합은 Dine 단독 결합 불명확",
    136: "치아미백 일정표 결합 불명확",
    137: "기저귀 소견 결합 불명확",
    138: "옷장 정리 권고 결합 불명확",
    140: "시럽 선물 결합 불성립 - Gift",
    141: "구역 온도 관리 리트리트 결합 불성립",
    142: "잠금 장치 토너먼트 결합 불성립",
    144: "카페 저널 결합은 Journal 다의어 불성립",
    145: "다이너 상태 속성 결합은 Status 불성립",
    146: "비스트로 게시물 결합은 Bulletin 다의어 불성립",
    147: "피자집 링크 결합은 Link 불성립",
    148: "델리 도식 결합은 매장 운영과 결합 불명확",
    149: "디저트 제안 결합은 Proposal 불성립",
    150: "포장 예약 결합은 Appointment 불성립",
    151: "브런치 체크인 결합은 Checkin 불성립",
    152: "베이커리 습도 속성 결합은 Humidity 불성립",
    155: "복리후생 일정표 결합 불명확",
    156: "민원 소견 결합 불명확",
    157: "범퍼 권고 결합 불명확",
    159: "치과 마취 리트리트 결합 불성립",
    160: "현장학습 토너먼트 결합 불성립",
    162: "베이글 지점 결합은 Point 다의어 불성립",
    163: "도넛 연결점 결합은 Nexus 추상 불성립",
    165: "라떼 카드 결합은 Card 다의어 불성립",
    166: "칫솔 점검 결합은 Check 불성립",
    167: "스노클링 태그 결합은 Tag 다의어 불성립",
    168: "칵테일 갱신 결합은 Update 불성립",
    169: "치약 피드 결합은 Feed 불성립",
    170: "카약 타임라인 결합은 Timeline 불성립",
    171: "바리스타 청구서 결합은 서비스 청구 결합 불명확",
    172: "구강청격 영수증 결합은 제품 결합 불명확",
    173: "폭포 테이블 결합은 Table 불성립",
    174: "펍 배지 결합은 Badge 다의어 불성립",
    175: "마우스가드 잔표 결합은 Stub 불성립",
    176: "일몰 메모 결합은 Memo 불성립",
    177: "스테이크하우스 회람 결합은 Circular 다의어 불성립",
    178: "스마일 자문 결합은 Advisory 추상 불성립",
    180: "스시 단위 결합은 Unit 다의어 불성립",
    181: "구취 관리 플랜 결합은 Breath 다의어 불명확",
    182: "보드워크 가격 속성 결합은 Price 불성립",
    183: "타코 채무 결합은 Debt 불성립",
    184: "코골이 기금 결합은 Fund 불성립",
    185: "해변 판매 결합은 Sale 다의어 불성립",
    186: "면집 관세 결합은 Tariff 불성립",
    187: "교합 가치 속성 결합은 Value 불성립",
    188: "전망 마진 속성 결합은 Margin 불성립",
    189: "해산물 링크 결합은 Link 불성립",
    190: "치과 규칙 결합은 Rule 불성립",
    191: "배낭여행 식별자 결합은 Identifier 불성립",
    192: "교정의 형식 결합은 Format 불성립",
    193: "패러세일링 토큰 결합은 Token 불성립",
    194: "치위 이자 결합은 Interest 불성립",
    195: "야생동물 부과금 결합은 Levy 불성립",
    196: "치실 할인 결합은 Discount 불성립",
    197: "라군 선수금 결합은 Advance 불성립",
    198: "치석 리딤 결합은 Redemption 불성립",
    199: "빙하 체험 결합은 Trial 불성립",
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
