import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk14_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk14_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    8: (0.6, "사일로 저장 정원은 실제 농업 운영 항목 - silo capacity 실재"),
    15: (0.6, "리모델링 시공 계획서는 실제 건축 문서 - Plan 라인(Concrete Plan 정합)"),
    16: (0.6, "전기 공사 보조금 관리는 실제 시공 운영 항목 - Subsidy 라인(Demolition Subsidy 정합)"),
    19: (0.6, "지붕 시공 검증 관리는 실제 시공 운영 항목 - Verification 라인(Waterproofing Verification 정합)"),
    20: (0.6, "바닥 자재 클레임 관리는 실제 시공 운영 항목 - Claim 라인(Bankruptcy Claim 정합)"),
    21: (0.6, "연수기 설치 처리 정원은 실제 배관 운영 항목 - 설비 capacity 실재"),
    22: (0.6, "여행객 이용 통계는 실제 관광 운영 지표 - Traveler Capacity 정합"),
    42: (0.6, "할부 제안서는 실제 금융 문서 - Proposal 라인(Savings Proposal 정합)"),
    44: (0.6, "파산 서류 날인 관리는 실제 법률 운영 항목 - Seal 라인(Flooring Seal 정합)"),
    45: (0.6, "방수 공사 환불 관리는 실제 시공 운영 항목 - Refund 라인(Flooring Refund 정합)"),
    48: (0.6, "변속기 정격 용량은 실제 자동차 운영 항목 - transmission capacity 실재(Reefer/Flatbed 자산 준용)"),
    49: (0.6, "동물 안락사 서비스 이용 통계는 실제 수의 운영 지표 - Euthanasia Capacity 정합"),
    57: (0.6, "냉장 컨테이너 대여 승인은 실제 물류 운영 항목 - Reefer 라인(Reefer Breakdown 정합)"),
    64: (0.6, "파산 전문가 패널은 실제 금융 도구 - Panel 금융 도구 라인(Wealth Panel 정합)"),
}

DUP_REJECT = {}

REJECT_REASON = {
    1: "자산 수호자 결합은 Keeper 앵커 불성립(Watch/Guardian와 별개 미성립)",
    2: "예방접종 습도 결합은 Humidity + 기각 follower 불성립",
    3: "방역 약품 사이클 결합은 Cycle + 기각 follower 불성립",
    4: "가격 책정 접수 결합은 Reception + 기각 follower 불성립",
    5: "묘지 후속 결합은 Followup + 기각 follower 불성립",
    6: "커미션 승인 결합은 승인 대상 불분명",
    7: "약국 조제 행렬 결합은 Matrix + 기각 follower 불성립",
    9: "투표 습도 결합은 Humidity + 기각 follower 불성립",
    10: "피드 사이클 결합은 Feed 불성립 + Cycle 불성립",
    11: "네트워크 센서 결합은 물리 센서 + 기각 follower 불성립",
    12: "경계 방어 접수 결합은 Reception + 기각 follower 불성립",
    13: "런북 후속 결합은 Followup + 기각 follower 불성립",
    14: "콜백 승인 결합은 승인 대상 불분명",
    17: "직불 변환기 결합은 Converter 기술 일반어 불성립",
    18: "저축 약정 결합은 Agreement 앵커 불성립(계약서 계열 미성립)",
    23: "백신 조건 결합은 Condition + 기각 follower 불성립",
    24: "송금 습도 결합은 Humidity + 기각 follower 불성립",
    25: "트레일러 에피소드 결합은 Episode + 기각 follower 불성립",
    26: "예비비 사이클 결합은 Cycle + 기각 follower 불성립",
    27: "배상 면책 고장 결합은 Breakdown + 기각 follower 불성립",
    28: "퇴직 정리 센서 결합은 물리 센서 + 기각 follower 불성립",
    29: "도장 접수 결합은 Reception + 기각 follower 불성립",
    30: "선수과목 후속 결합은 Followup + 기각 follower 불성립",
    31: "자막 행렬 결합은 Matrix + 기각 follower 불성립",
    32: "송금 기반 결합은 Base 불성립",
    33: "사이딩 스튜디오 결합은 Studio 불성립",
    34: "자산 동반자 결합은 Companion 앵커 불성립(Gutter Companion 준용)",
    35: "홈통 등록부 결합은 Registry 불성립",
    36: "주식 카드 결합은 Card 불성립(Foundation Card 준용)",
    37: "기초 태그 결합은 Tag 기호 불성립",
    38: "골조 스텁 결합은 Stub 기술 일반어 불성립",
    39: "콘크리트 의무 결합은 Duty 불성립",
    40: "철거 할인 결합은 Discount 앵커 미확정으로 불성립",
    41: "굴착 저장소 결합은 Repository 기술 일반어 불성립",
    43: "포장 참조 결합은 Reference 앵커 미확정으로 불성립(Roofing Reference 준용)",
    46: "상속 깊이 결합은 Depth 물리 사양 명사 불성립(Deck Depth 준용)",
    47: "데크 하중 결합은 Load 물리 사양 명사 불성립",
    50: "임플란트 조건 결합은 Condition + 기각 follower 불성립",
    51: "자장가 습도 결합은 Humidity + 기각 follower 불성립",
    52: "스타일링 에피소드 결합은 Episode + 기각 follower 불성립",
    53: "약품 대체 조제 사이클 결합은 Cycle + 기각 follower 불성립",
    54: "카지노 센서 결합은 물리 센서 + 기각 follower 불성립",
    55: "부상 접수 결합은 Reception + 기각 follower 불성립",
    56: "채권자 후속 결합은 Followup + 기각 follower 불성립",
    58: "리노베이션 행렬 결합은 Matrix + 기각 follower 불성립",
    59: "파티오 허브 결합은 Hub 불성립",
    60: "채무자 파형 결합은 Wave 불성립",
    61: "가구 기반 결합은 Base 불성립(Siding Base 준용)",
    62: "수취인 실험실 결합은 Lab 불성립(Countertop Lab 준용)",
    63: "조정대 센터 결합은 Center 불성립(Masonry Center 준용)",
    65: "석공 경로 결합은 Route 불성립(Carpentry Route 준용)",
    66: "신탁 반지 결합은 Ring 물건 불성립(Carpentry Ring 준용)",
    67: "목공 결절점 결합은 Nexus 불성립(Wealth Nexus 준용)",
    68: "자산 관리자 결합은 Manager 앵커 불성립(Trading Manager 준용) + 기존 자산관리 서비스명 유사",
}

n = len(req["items"])
assert n == 68, n
assert len(APPROVE) == 14, len(APPROVE)
assert len(DUP_REJECT) == 0
assert len(REJECT_REASON) == 54, len(REJECT_REASON)
covered = set(APPROVE) | set(DUP_REJECT) | set(REJECT_REASON)
assert covered == set(range(1, n + 1)), f"coverage mismatch: missing={sorted(set(range(1,n+1))-covered)} extra={sorted(covered-set(range(1,n+1)))}"
overlap = (set(APPROVE) & set(DUP_REJECT)) | (set(APPROVE) & set(REJECT_REASON)) | (set(DUP_REJECT) & set(REJECT_REASON))
assert not overlap, f"overlapping indices: {sorted(overlap)}"

decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in APPROVE:
        conf, reason = APPROVE[i]
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": conf, "reason": reason})
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
print(f"approve={approved} reject={len(decisions)-approved} (dup={len(DUP_REJECT)})")
