import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk15_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk15_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    3: (0.6, "HR 교육 세미나로 실재 (Seminar 라인)"),
    7: (0.6, "기획 기사 세미나 모집 전단으로 실재 (Flyer 라인)"),
    14: (0.6, "카약 강습 코스로 실재 (Route 물리 경로)"),
    20: (0.6, "일몰 감상 일지로 성립 (Journal 라인)"),
    23: (0.6, "수변 안내 부스로 실재 (Booth 실물 공간)"),
    25: (0.6, "호흡 이상 감지 알림으로 실재 (Alert 라인)"),
    39: (0.6, "사파리 투어 영수증으로 성립 (Receipt 라인)"),
    42: (0.6, "스케일링 바우처로 성립 (Voucher 라인)"),
    47: (0.6, "당일여행 예약 확정서로 성립 (Confirmation 라인)"),
    60: (0.6, "후원 약정 핸드북으로 실재 (Handbook 라인)"),
    64: (0.6, "운전 안전 세미나로 실재 (Seminar 라인)"),
    69: (0.6, "사일로 관리 교육으로 실재 (Tutorial 라인)"),
    78: (0.6, "캡션 작성 교육으로 실재 (Tutorial 라인)"),
    79: (0.6, "감정 분석 핸드북으로 실재 (Handbook 라인)"),
    83: (0.6, "카페 창업 세미나로 실재 (Seminar 라인)"),
    87: (0.6, "식기세척기 안내 전단으로 실재 (Flyer 라인)"),
    99: (0.6, "합주 교육으로 실재 (Tutorial 라인)"),
    100: (0.6, "부상 처치 핸드북으로 실재 (Handbook 라인)"),
    104: (0.6, "보험 조정 실무 세미나로 실재 (Seminar 라인)"),
    124: (0.6, "수변 안내 키오스크로 실재 (Kiosk 실물 공간)"),
    126: (0.6, "호흡 기록 차트로 성립 (Chart 라인)"),
    139: (0.6, "스케일링 청구서로 성립 (Bill 라인)"),
    150: (0.6, "요트 투어 계획으로 성립 (Plan 라인)"),
    161: (0.6, "토양 관리 교육으로 실재 (Tutorial 라인)"),
    165: (0.6, "기록물 관리 세미나로 실재 (Seminar 라인)"),
    171: (0.6, "사일로 핸드북으로 실재 (Handbook 라인)"),
    178: (0.6, "경계 보안 세미나 모집 전단으로 실재 (Flyer 라인)"),
    179: (0.6, "예산 편성 교육으로 실재 (Tutorial 라인)"),
    180: (0.6, "캡션 핸드북으로 실재 (Handbook 라인)"),
    184: (0.6, "차량 관리 세미나로 실재 (Seminar 라인)"),
    188: (0.6, "공예 수업 모집 전단으로 실재 (Flyer 라인)"),
    200: (0.6, "카지노 게임 안내 교육으로 실재 (Tutorial 라인)"),
}

TRADEMARK_REJECT = {}

DUP_REJECT = {}

REJECT_REASON = {
    1: "리모델링 소견 결합 불명확",
    2: "보험 조정 권고 결합 불명확",
    4: "패티오 선물 결합 불성립 - Gift",
    5: "편입 리트리트 결합 불성립",
    6: "구 토너먼트 결합 불성립 - Ward",
    8: "에스프레소 책상 결합은 Desk 불성립",
    9: "라떼 지도 결합은 Map 불성립",
    10: "칫솔 기반 결합은 Base 추상 불성립",
    11: "스노클링 게시판 결합은 Board 다의어 불성립",
    12: "칵테일 포털 결합은 Portal 불성립",
    13: "치약 콘솔 결합은 Console 불성립",
    15: "바리스타 연결점 결합은 Nexus 불성립",
    16: "구강청격 지도집 결합은 Atlas 추상 불성립",
    17: "폭포 엔진 결합은 Engine 추상 불성립",
    18: "펍 등록부 결합 불성립",
    19: "마우스가드 운영 결합은 Ops 불성립",
    21: "스테이크하우스 탐색기 결합은 Finder 불성립",
    22: "스마일 사무실 결합 불성립",
    24: "스시 명부 결합은 Roster 불성립",
    26: "보드워크 수거함 결합은 Bin 불성립",
    27: "타코 창 결합은 Window 다의어 불성립",
    28: "코골이 순서 결합은 Roll 다의어 불성립",
    29: "해변 기록 결합 불성립",
    30: "면집 검사 결합 불명확",
    31: "교합 점수 결합은 Score 불성립",
    32: "전망 태그 결합은 Tag 다의어 불성립",
    33: "해산물 이력 결합 불성립",
    34: "치과 파일 결합은 File 다의어 불성립",
    35: "배낭여행 요율 속성 결합은 Rate 불성립",
    36: "교정의 요약 결합 불성립",
    37: "패러세일링 알림 결합 불성립",
    38: "치위 주문 결합은 Order 다의어 불성립",
    40: "치실 표 결합은 Table 다의어 불성립",
    41: "라군 샘플 결합은 Sample 다의어 불성립",
    43: "빙하 전표 결합은 Stub 불성립",
    44: "불소 한도 결합은 Quota 속성어 불성립",
    45: "화산 회람 결합은 Bulletin 다의어 불성립",
    46: "실런트 권고 결합은 Advisory 불성립",
    48: "치은염 요금 결합은 Fee 불성립",
    49: "요트 단위 결합은 Unit 다의어 불성립",
    50: "이갈이 가격 속성 결합은 Price 불성립",
    51: "산책로 세금 결합은 Tax 불성립",
    52: "구취 부채 결합 불성립",
    53: "우릴 현금 결합 불성립",
    54: "치주염 의무 결합 불성립",
    55: "사막 관세 결합은 Tariff 불성립",
    56: "부정교합 지분 결합은 Stake 불성립",
    57: "와이너리 벌금 결합은 Fine 불성립",
    58: "치수과 버전 결합은 Version 불성립",
    59: "치주과 세부 결합은 Detail 불성립",
    61: "공청회 일정표 결합은 Hearing 다의어 불명확",
    62: "소재 의견 결합 불명확",
    63: "아카이브 권고 결합 불명확",
    65: "로밍 선물 결합 불성립 - Gift",
    66: "감사 리트리트 결합 불성립",
    67: "파이프라인 토너먼트 결합 불성립",
    68: "환불 전단 결합 불명확",
    70: "장부 일정표 결합 불명확",
    71: "투표 의견 결합 불명확",
    72: "배치 권고 결합 불명확",
    73: "피드 세미나 결합 불명확",
    74: "허가 선물 결합 불성립 - Gift",
    75: "네트워크 리트리트 결합 불성립",
    76: "경계 토너먼트 결합 불성립",
    77: "런북 전단 결합 불명확",
    80: "리크루터 일정표 결합 불명확",
    81: "랜야드 의견 결합 불명확",
    82: "점검 권고 결합 불명확",
    84: "진드기 선물 결합 불성립 - Gift",
    85: "잇몸 리트리트 결합 불성립",
    86: "공예 토너먼트 결합 불성립",
    88: "다이너 실험실 결합은 Lab 불성립",
    89: "비스트로 탐색기 결합은 Locator 불성립",
    90: "피자집 파일 결합은 File 다의어 불성립",
    91: "데리 회람 결합은 Circular 다의어 불성립",
    92: "디저트 링크 결합은 Link 불성립",
    93: "포장 워크시트 결합은 Worksheet 불성립",
    94: "브런치 무대 결합은 Stage 다의어 불성립",
    95: "베이커리 사례 결합은 Case 다의어 불성립",
    96: "제과 예측기 결합은 Predictor 불성립",
    97: "베이글 높이 속성 결합은 Height 불성립",
    98: "도넛 가동률 결합은 Utilization 불성립",
    101: "채권자 일정표 결합 불명확",
    102: "냉장 컨테이너 소견 결합 불명확",
    103: "리모델링 권고 결합 불명확",
    105: "교육 선물 결합 불성립 - Gift",
    106: "패티오 리트리트 결합 불성립",
    107: "편입 토너먼트 결합 불성립",
    108: "구 전단 결합 불명확 - Ward",
    109: "에스프레소 레이더 결합은 Radar 불성립",
    110: "라떼 액자 결합은 Frame 불성립",
    111: "칫솔 핵심 결합은 Core 추상 불성립",
    112: "스노클링 갑판 결합은 Deck 불성립",
    113: "칵테일 콘솔 결합은 Console 불성립",
    114: "치약 패널 결합은 Panel 불성립",
    115: "카약 레일 결합은 Rail 다의어 불성립",
    116: "바리스타 지도집 결합은 Atlas 추상 불성립",
    117: "구강청격 관리인 결합은 Keeper 불성립",
    118: "폭포 조수 결합은 Assistant 불성립",
    119: "펍 운영 결합은 Ops 불성립",
    120: "마우스가드 플레이북 결합 불성립",
    121: "선셋 등록부 결합 불성립",
    122: "스테이크하우스 사무실 결합 불성립",
    123: "스마일 계수기 결합은 Counter 다의어 불성립",
    125: "스시 알림 결합 불명확",
    127: "보드워크 여권 결합은 Passport 다의어 불성립",
    128: "타코 순서 결합은 Roll 다의어 불성립",
    129: "코골이 리포트 결합 불성립",
    130: "해변 서식 결합은 Form 다의어 불성립",
    131: "면집 점수 결합은 Score 불성립",
    132: "교합 메모 결합은 Note 다의어 불성립",
    133: "전망 프로필 결합 불성립",
    134: "해산물 파일 결합은 File 다의어 불성립",
    135: "치과 수준 속성 결합은 Level 불성립",
    136: "배낭여행 갱신 결합 불성립",
    137: "교정의 타임라인 결합 불성립",
    138: "패러세일링 색인 결합은 Index 다의어 불성립",
    140: "야생동물 코드 결합은 Code 불성립",
    141: "치실 전표 결합은 Slip 다의어 불성립",
    142: "라군 슬롯 결합은 Slot 다의어 불성립",
    143: "치석 배지 결합 불성립",
    144: "빙하 정산 결합은 Statement 불성립",
    145: "불소 탭 결합은 Tab 다의어 불성립",
    146: "화산 요약 결합은 Brief 다의어 불성립",
    147: "실런트 청원 결합은 Petition 불성립",
    148: "당일여행 정리 결합은 Recap 다의어 불성립",
    149: "치은염 항목 결합은 Item 다의어 불성립",
    151: "이갈이 요금 결합은 Fare 다의어 불성립",
    152: "산책로 대출 결합 불성립",
    153: "구취 기금 결합 불성립",
    154: "우릴 판매 결합은 Sale 다의어 불성립",
    155: "치주염 수당 결합 불성립",
    156: "사막 가치 결합은 Value 불성립",
    157: "부정교합 마진 속성 결합은 Margin 불성립",
    158: "와이너리 번호 속성 결합은 Number 불성립",
    159: "치수과 링크 결합은 Link 불성립",
    160: "치주과 식별자 결합은 Identifier 불성립",
    162: "약정 일정표 결합 불명확",
    163: "공청회 소견 결합은 Hearing 다의어 불명확",
    164: "소재 권고 결합 불명확",
    166: "운전 선물 결합 불성립 - Gift",
    167: "로밍 리트리트 결합 불성립",
    168: "감사 토너먼트 결합 불성립",
    169: "파이프라인 전단 결합 불명확",
    170: "처리량 튜토리얼 결합은 Throughput 속성어 불성립",
    172: "장부 소견 결합 불명확",
    173: "투표 권고 결합 불명확",
    174: "배치 세미나 결합 불명확",
    175: "피드 선물 결합 불성립 - Gift",
    176: "허가 리트리트 결합 불성립",
    177: "네트워크 토너먼트 결합 불성립",
    181: "감정 분석 일정표 결합 불명확",
    182: "리크루터 소견 결합 불명확",
    183: "랜야드 권고 결합 불명확",
    185: "카페 선물 결합 불성립 - Gift",
    186: "진드기 리트리트 결합 불성립",
    187: "잇몸 토너먼트 결합 불성립",
    189: "다이너 역 결합은 Station 다의어 불성립",
    190: "비스트로 탐색기 결합은 Finder 불성립",
    191: "피자집 수준 속성 결합은 Level 불성립",
    192: "데리 권고 결합은 Advisory 불성립",
    193: "디저트 규칙 결합은 Rule 불성립",
    194: "포장 도식 결합은 Diagram 불성립",
    195: "브런치 결과 결합은 Result 불성립",
    196: "베이커리 매치 결합은 Match 다의어 불성립",
    197: "제과 봉인 결합은 Seal 다의어 불성립",
    198: "베이글 폭 속성 결합은 Width 불성립",
    199: "도넛 혜택 결합은 Benefit 추상 불성립",
}

n = len(req["items"])
assert n == 200, n
assert len(APPROVE) == 32, len(APPROVE)
assert len(TRADEMARK_REJECT) == 0, len(TRADEMARK_REJECT)
assert len(DUP_REJECT) == 0, len(DUP_REJECT)
assert len(REJECT_REASON) == 168, len(REJECT_REASON)
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
