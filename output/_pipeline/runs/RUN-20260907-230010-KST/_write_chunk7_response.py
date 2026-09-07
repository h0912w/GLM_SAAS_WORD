import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_chunk7_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_chunk7_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

APPROVE = {
    32: (0.6, "공유기 장애·다운 알림은 실제 통신 운영 항목 - 명확"),
    41: (0.6, "활주로 점검 이력 관리는 실제 항공 운영 항목 - 명확"),
    46: (0.6, "뷔페 예약 시간 슬롯 관리는 실제 외식 운영 항목 - 명확"),
    50: (0.6, "핫스팟 데이터 사용 한도 관리는 실제 통신 운영 항목 - 명확"),
    53: (0.6, "요가 수강료 관리는 실제 피트니스 운영 항목 - 명확"),
    68: (0.6, "사진 업로드·편집 처리 물량은 실제 언론 운영 지표 - 명확"),
}

DUP_REJECT = {
    18: "이미 승인된 Financing Load와 같은 차량 금융 처리 계열 의미중복",
    55: "이미 승인된 Headstone Fee와 같은 묘비 제작 비용 관리 계열 의미중복",
    78: "이미 승인된 Freight Load와 같은 화물 물량 관리 계열 의미중복",
}

REJECT_REASON = {
    1: "구충 호환성은 호환 대상이 불분명해 의미 불명",
    2: "키리스 깊이는 의미 불명",
    3: "커뮤니티 시설 높이는 의미 불명",
    4: "스키 폭은 의미 불명",
    5: "병원 온도는 온도 대상이 불분명해 의미 불명",
    6: "벌크 압력은 의미 불명",
    7: "비교 매물 물량은 의미 불명",
    8: "지급 전압은 의미 불명",
    9: "수습 와트는 의미 불명",
    10: "루브릭 밝기는 의미 불명",
    11: "국민투표 빈도는 빈도 대상이 불분명해 의미 불명",
    12: "기사 호환성은 호환 대상이 불분명해 의미 불명",
    13: "크리에이티브 깊이는 의미 불명",
    14: "아카이브 높이는 의미 불명",
    15: "기사 폭은 의미 불명",
    16: "로밍 온도는 의미 불명",
    17: "레퍼런스 와트는 의미 불명",
    19: "송풍기 깊이는 설비 사양으로 읽혀 SaaS 불일치",
    20: "자물쇠 높이는 잠금 사양으로 읽혀 SaaS 불일치",
    21: "통역 폭은 의미 불명",
    22: "조명 압력은 의미 불명",
    23: "답례품 물량은 처리 대상이 불분명해 의미 불명",
    24: "점유자 전압은 의미 불명",
    25: "헹굼 밝기는 의미 불명",
    26: "뻥튀기 빈도는 의미 불명",
    27: "관광 호환성은 호환 대상이 불분명해 의미 불명",
    28: "용접 부스는 시설로 읽혀 제품 불명확",
    29: "농기계 키오스크는 시설로 읽혀 제품 불명확",
    30: "기부 베이는 시설로 읽혀 제품 불명확",
    31: "카풀 명단은 명부 서류로 읽혀 제품 불명확",
    33: "비밀번호 차트는 차트 문서 오독 우려로 제품 불명확",
    34: "클라우드 저장함은 시설·용기로 읽혀 제품 불명확",
    35: "러닝머신 로그는 운영 기록 서류로 읽혀 제품 불명확",
    36: "모기 시트는 서류로 읽혀 제품 불명확",
    37: "멀칭 검사는 검사 대상이 불분명해 의미 불명",
    38: "얼룩 노트는 오독으로 의미 불명",
    39: "화장 태그는 오독으로 의미 불명",
    40: "마리나 뷰는 오독으로 의미 불명",
    42: "채석 파일은 오독으로 의미 불명",
    43: "상각 청구서는 오독으로 의미 불명",
    44: "석고보드 전표는 오독으로 의미 불명",
    45: "장바구니 샘플은 오독으로 의미 불명",
    47: "시제품 바우처는 교환권 오독 우려",
    48: "과수원 배지는 오독으로 의미 불명",
    49: "통근 메모는 오독으로 의미 불명",
    51: "피싱 탭은 UI 요소 오독으로 의미 불명",
    52: "데이터베이스 공지는 서류로 읽혀 제품 불명확",
    54: "방역 플랜은 계획 대상이 불분명해 의미 불명",
    56: "카약 론은 대출로 오독 우려",
    57: "격납고 합계는 오독으로 의미 불명",
    58: "급여 번호는 번호 대상이 불분명해 의미 불명",
    59: "세일 식별자는 기술 은어로만 읽혀 제품 불명확",
    60: "기기 형식은 형식 대상이 불분명해 의미 불명",
    61: "덤벨 부과금은 오독 우려로 의미 불명",
    62: "윗 체납은 오독 우려로 의미 불명",
    63: "페리 마진율은 오독 우려로 의미 불명",
    64: "호갱 투어 깊이는 의미 불명",
    65: "책임 높이는 의미 불명",
    66: "압류 폭은 의미 불명",
    67: "선택과목 온도는 의미 불명",
    69: "평가 전압은 의미 불명",
    70: "면접관 와트는 의미 불명",
    71: "와이파이 밝기는 의미 불명",
    72: "웨이터 호환성은 호환 대상이 불분명해 의미 불명",
    73: "콘덴서 깊이는 부품 사양으로 읽혀 SaaS 불일치",
    74: "키리스 높이는 의미 불명",
    75: "커뮤니티 시설 폭은 의미 불명",
    76: "스키 기온은 온도 대상이 불분명해 의미 불명",
    77: "병원 압력은 은유 오독으로 의미 불명",
    79: "비교 매물 전압은 의미 불명",
    80: "지급 와트는 의미 불명",
    81: "수습 밝기는 의미 불명",
    82: "루브릭 빈도는 빈도 대상이 불분명해 의미 불명",
    83: "국민투표 호환성은 호환 대상이 불분명해 의미 불명",
}

assert len(APPROVE) == 6
assert len(DUP_REJECT) == 3
covered = set(APPROVE) | set(DUP_REJECT) | set(REJECT_REASON)
assert covered == set(range(1, 84)), f"coverage mismatch: missing={sorted(set(range(1,84))-covered)} extra={sorted(covered-set(range(1,84)))}"
assert not (set(APPROVE) & set(DUP_REJECT) | set(APPROVE) & set(REJECT_REASON)
            | set(DUP_REJECT) & set(REJECT_REASON))

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
                          "confidence": 0.7,
                          "reason": REJECT_REASON.get(i, "clarity 탈락 - 의미 불명")})

assert len(decisions) == len(req["items"]) == 83
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
