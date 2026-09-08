import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk46_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk46_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    2: (0.6, "실런트 스케치 학습자료로 실재 (dental 도해 계열)"),
    16: (0.7, "손해사정 교육으로 실재 (보험 실무 개념)"),
    23: (0.6, "모금 캠페인 전단으로 실재 (Flyer 라인)"),
    24: (0.6, "보험 특약 핸드북으로 실재 (Handbook 라인)"),
    28: (0.6, "셔틀 운영 세미나로 실재 (Seminar 라인)"),
    36: (0.6, "옷장 정리 세미나로 실재 (Seminar 라인)"),
    40: (0.6, "잠금 서비스 전단으로 실재 (Flyer 라인)"),
    50: (0.7, "과외 운영 교육으로 실재 (교육 실무 개념)"),
    51: (0.6, "포트홀 보수 핸드북으로 실재 (Handbook 라인)"),
    55: (0.6, "범퍼 수리 세미나로 실재 (Seminar 라인)"),
    58: (0.6, "현장학습 안내 전단으로 실재 (Flyer 라인)"),
    97: (0.6, "불소 관리 워크시트로 실재 (dental 도해 계열)"),
    113: (0.6, "손해사정 핸드북으로 실재 (Handbook 라인)"),
    116: (0.6, "어메니티 서비스 세미나로 실재 (Seminar 라인)"),
    123: (0.6, "재고 보충 세미나로 실재 (Seminar 라인)"),
    127: (0.6, "윤작 안내 전단으로 실재 (Flyer 라인)"),
    128: (0.7, "이벤트 녹화 운영 교육으로 실재 (이벤트 실무 개념)"),
    132: (0.6, "기저귀 교육 세미나로 실재 (산후교실 개념)"),
    136: (0.6, "구역 온도 관리 전단으로 실재 (Flyer 라인)"),
    143: (0.6, "포장 주문 송장으로 실재 (Invoice 라인 준용)"),
    146: (0.7, "단열 시공 교육으로 실재 (건설 실무 개념)"),
    147: (0.6, "과외 운영 핸드북으로 실재 (Handbook 라인)"),
    151: (0.6, "민원 대응 세미나로 실재 (Seminar 라인)"),
    154: (0.6, "치과 마취 안내 전단으로 실재 (Flyer 라인)"),
    171: (0.6, "미백 시술 확인서로 성립 (Confirmation 라인 준용)"),
    193: (0.6, "불소 도포 도해 학습자료로 실재 (dental 도해 계열)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "화산 도해 결합은 여행 서비스와 결합 불명확",
    3: "당일여행 렌더링 결합은 여행 서비스와 결합 불명확",
    4: "치은염 횟수 결합은 Count 불성립",
    5: "요트 합계 결합은 여행 서비스와 결합 불명확",
    6: "이갈이 공지 결합은 Announcement 불성립",
    7: "산책로 변환기 결합은 Converter 추상 불성립",
    8: "구취 견적기 결합은 Estimator 추상 불성립",
    9: "우릴 탐지기 결합은 Detector 추상 불성립",
    10: "치주염 보호자 결합은 Guardian 추상 불성립",
    11: "사막 단계 결합은 Stage 다의어 불성립",
    12: "부정교합 연승 속성 결합은 Streak 불성립",
    13: "와이너리 추이 속성 결합은 Trend 불성립",
    14: "치수과 제안 결합은 Proposal 불성립",
    15: "치주 사본 결합은 Copy 다의어 불성립",
    17: "입찰 일정표 결합 불명확",
    18: "풀필먼트 소견 결합 불명확",
    19: "어메니티 권고 결합 불명확",
    20: "등록금 세미나 결합은 Tuition 결합 불명확",
    21: "설비 정지 선물 결합 불성립 - Gift",
    22: "작물 리트리트 결합 불성립",
    25: "채용 후보자 일정표 결합 불명확",
    26: "하자보증 소견 결합 불명확",
    27: "재고 보충 권고 결합 불명확",
    29: "수업 운영 선물 결합 불성립 - Gift",
    30: "계측기 교정 리트리트 결합 불성립",
    31: "윤작 토너먼트 결합 불성립",
    32: "외식 핸드북 결합은 Dine 단독 결합 불명확",
    33: "중성화 일정표 결합 불명확",
    34: "치아미백 소견 결합 불명확",
    35: "기저귀 권고 결합 불명확",
    37: "왁싱 선물 결합 불성립 - Gift",
    38: "시럽 리트리트 결합 불성립",
    39: "구역 온도 관리 토너먼트 결합 불성립",
    41: "카페 등록부 결합은 Registry 불성립",
    42: "다이너 전망 속성 결합은 View 불성립",
    43: "비스트로 요약 결합은 Brief 다의어 불성립",
    44: "피자집 규칙 결합은 Rule 불성립",
    45: "델리 배치도 결합은 매장 운영과 결합 불명확",
    46: "디저트 보증 속성 결합은 Guarantee 불성립",
    47: "포장 피드백 결합은 Feedback 불성립",
    48: "브런치 크기 속성 결합은 Size 불성립",
    49: "베이커리 에피소드 결합은 Episode 불성립",
    52: "뉴스레터 일정표 결합 불명확",
    53: "복리후생 소견 결합 불명확",
    54: "민원 권고 결합 불명확",
    56: "제과 선물 결합 불성립 - Gift",
    57: "치과 마취 토너먼트 결합 불성립",
    59: "베이글 지도 결합은 Map 다의어 불성립",
    60: "도넛 지도집 결합은 Atlas 불성립",
    61: "에스프레소 만 결합은 Bay 불성립",
    62: "라떼 시트 결합은 Sheet 다의어 불성립",
    63: "칫솔 점수 결합은 Score 불성립",
    64: "스노클링 프로필 결합은 Profile 다의어 불성립",
    65: "칵테일 피드 결합은 Feed 불성립",
    66: "치약 초안 결합은 Draft 다의어 불성립",
    67: "카약 리마인더 결합은 Reminder 불성립",
    68: "바리스타 영수증 결합은 서비스 결합 불명확",
    69: "구강청격 코드 결합은 Code 불성립",
    70: "폭포 전표 결합은 Slip 다의어 불성립",
    71: "펍 잔표 결합은 Stub 불성립",
    72: "마우스가드 명세서 결합은 Statement 불성립",
    73: "일몰 한도 결합은 Quota 불성립",
    74: "스테이크하우스 자문 결합은 Advisory 추상 불성립",
    75: "스마일 청원 결합은 Petition 불성립",
    76: "수변 요약 결합은 Recap 불성립",
    77: "스시 플랜 결합은 Taco Plan 기각 라인 준용 불명확",
    78: "호흡 비용 속성 결합은 Cost 불성립",
    79: "보드워크 요금 속성 결합은 Fare 불성립",
    80: "타코 기금 결합은 Fund 불성립",
    81: "코골이 현금 결합은 Cash 불성립",
    82: "해변 청구 결합은 Charge 다의어 불성립",
    83: "면집 가치 속성 결합은 Value 불성립",
    84: "교합 지분 결합은 Stake 불성립",
    85: "전망 벌금 결합은 Fine 불성립",
    86: "해산물 규칙 결합은 Rule 불성립",
    87: "치과 세부 결합은 Detail 불성립",
    88: "배낭여행 분류 결합은 Category 불성립",
    89: "교정의 일련번호 결합은 Serial 불성립",
    90: "패러세일링 서명 결합은 Signature 불성립",
    91: "치위 자산 결합은 Asset 불성립",
    92: "야생동물 기한 결합은 Due 불성립",
    93: "치실 연체 결합은 Arrears 불성립",
    94: "라군 벌칙 결합은 Penalty 불성립",
    95: "치석 연장 결합은 Extension 불성립",
    96: "빙하 그래프 결합은 Graph 불성립",
    98: "화산 도식 결합은 여행 서비스와 결합 불명확",
    99: "실런트 개요 결합은 Outline 불성립",
    100: "당일여행 통지 결합은 여행 서비스와 결합 불명확",
    101: "치은염 메시지 결합은 Message 불성립",
    102: "요트 위젯 결합은 여행 서비스와 결합 불명확",
    103: "이갈이 계산기 결합은 Calculator 추상 불성립",
    104: "산책로 생성기 결합은 Generator 추상 불성립",
    105: "구취 점검기 결합은 Checker 추상 불성립",
    106: "우릴 타이머 결합은 Timer 추상 불성립",
    107: "치주염 조력자 결합은 Helper 추상 불성립",
    108: "사막 결과 속성 결합은 Result 불성립",
    109: "부정교합 순위 속성 결합은 Rank 불성립",
    110: "와이너리 비교 속성 결합은 Comparison 불성립",
    111: "치수과 보증 속성 결합은 Guarantee 불성립",
    112: "치주 판독 결합은 Reading 다의어 불명확",
    114: "입찰 소견 결합 불명확",
    115: "풀필먼트 권고 결합 불명확",
    117: "등록금 선물 결합은 Tuition 결합 불성립",
    118: "설비 정지 리트리트 결합 불성립",
    119: "작물 토너먼트 결합 불성립",
    120: "보험 특약 일정표 결합 불명확",
    121: "채용 후보자 소견 결합 불명확",
    122: "하자보증 권고 결합 불명확",
    124: "셔틀 선물 결합 불성립 - Gift",
    125: "수업 운영 리트리트 결합 불성립",
    126: "계측기 교정 토너먼트 결합 불성립",
    129: "외식 일정표 결합은 Dine 단독 결합 불명확",
    130: "중성화 소견 결합 불명확",
    131: "치아미백 권고 결합 불명확",
    133: "옷장 정리 선물 결합 불성립 - Gift",
    134: "왁싱 리트리트 결합 불성립",
    135: "시럽 토너먼트 결합 불성립",
    137: "카페 달력 결합은 Calendar 불성립",
    138: "다이너 이력 속성 결합은 History 불성립",
    139: "비스트로 회람 결합은 Circular 다의어 불성립",
    140: "피자집 세부 결합은 Detail 불성립",
    141: "델리 스케치 결합은 매장 운영과 결합 불명확",
    142: "디저트 기록 속성 결합은 Record 불성립",
    144: "브런치 길이 속성 결합은 Length 불성립",
    145: "베이커리 주기 속성 결합은 Cycle 불성립",
    148: "포트홀 일정표 결합 불명확",
    149: "뉴스레터 소견 결합 불명확",
    150: "복리후생 권고 결합 불명확",
    152: "범퍼 선물 결합 불성립 - Gift",
    153: "제과 리트리트 결합 불성립",
    155: "베이글 액자 결합은 Frame 불성립",
    156: "도넛 관리인 결합은 Keeper 추상 불성립",
    157: "에스프레소 게시 결합은 Post 다의어 불성립",
    158: "라떼 점검 결합은 Check 불성립",
    159: "칫솔 노트 결합은 Note 불성립",
    160: "스노클링 상태 속성 결합은 Status 불성립",
    161: "칵테일 초안 결합은 Draft 다의어 불성립",
    162: "치약 요약 결합은 Summary 불성립",
    163: "카약 색인 결합은 Index 불성립",
    164: "바리스타 코드 결합은 Code 불성립",
    165: "구강청격 목록 결합은 List 불성립",
    166: "폭포 샘플 결합은 Sample 다의어 불성립",
    167: "펍 명세서 결합은 Statement 불성립",
    168: "마우스가드 메모 결합은 Memo 불성립",
    169: "일몰 탭 결합은 Tab 다의어 불성립",
    170: "스테이크하우스 청원 결합은 Petition 불성립",
    172: "수변 항목 결합은 Entry 다의어 불성립",
    173: "스시 비용 속성 결합은 Cost 불성립",
    174: "호흡 가격 속성 결합은 Price 불성립",
    175: "보드워크 세금 결합은 Tax 불성립",
    176: "타코 현금 결합은 Cash 불성립",
    177: "코골이 판매 결합은 Sale 다의어 불성립",
    178: "해변 의무 결합은 Duty 불성립",
    179: "면집 지분 결합은 Stake 불성립",
    180: "교합 마진 속성 결합은 Margin 불성립",
    181: "전망 번호 속성 결합은 Number 불성립",
    182: "해산물 세부 결합은 Detail 불성립",
    183: "치과 식별자 결합은 Identifier 불성립",
    184: "배낭여행 속성 결합은 Attribute 불성립",
    185: "교정의 토큰 결합은 Token 불성립",
    186: "패러세일링 마커 결합은 Marker 불성립",
    187: "치위 부과금 결합은 Levy 불성립",
    188: "야생동물 보조금 결합은 Subsidy 불성립",
    189: "치실 선수금 결합은 Advance 불성립",
    190: "라군 가산율 결합은 Markup 불성립",
    191: "치석 체험 결합은 Trial 불성립",
    192: "빙하 라벨 결합은 Label 불성립",
    194: "화산 배치도 결합은 여행 서비스와 결합 불명확",
    195: "실런트 렌더링 결합은 Rendering 불성립",
    196: "당일여행 키트 결합은 여행 서비스와 결합 불명확",
    197: "치은염 합계 결합은 Total 불성립",
    198: "요트 저장소 결합은 여행 서비스와 결합 불명확",
    199: "이갈이 변환기 결합은 Converter 추상 불성립",
    200: "산책로 기록기 결합은 Recorder 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 26, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 174, len(REJECT_REASON)
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
