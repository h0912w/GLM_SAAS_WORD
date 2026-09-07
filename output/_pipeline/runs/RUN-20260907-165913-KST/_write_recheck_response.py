import json, os
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
JDIR = os.path.join(HERE, "judgment")
REQ = os.path.join(JDIR, "review_titles_recheck_round1_request.json")
RESP = os.path.join(JDIR, "review_titles_recheck_round1_response.json")

with open(REQ, encoding="utf-8") as f:
    req = json.load(f)

CLARITY_FLIP = {
    3: "승인 근거가 다른 제목(심야 이사 물량)의 것으로 1차 판정 근거가 성립하지 않고, 자격 인증 압박은 의미 불명",
    10: "승인 근거(덕트 풍량)가 제목과 불일치하고, Airflow Depth는 덕트 깊이 시공 사양으로 읽혀 SaaS 불일치",
    18: "승인 근거가 석고보드 시공 보증의 것으로 불일치하고, 상각 약속은 의미 불명",
    19: "승인 근거가 석고보드 견적의 것으로 불일치하고, 상각 바코드는 의미 불명",
    70: "승인 근거가 용접 품질 검사의 것으로 불일치하고, 침해 호환성은 의미 불명",
    82: "승인 근거가 시제품 인증의 것으로 불일치하고, 뷔페 보증은 보증 대상이 불분명",
    100: "승인 근거가 네트워크 보호의 것으로 불일치하고, 카풀 워크숍은 의미 불명",
    103: "승인 근거가 뷔페 예약금의 것으로 불일치하고, 장바구니 보증은 보증 대상이 불분명",
    145: "승인 근거가 러닝 기록의 것으로 불일치하고, 클라우드 스테이지는 무대·단계로 오독해 의미 불명",
    185: "승인 근거가 채굴 장비 압력의 것으로 불일치하고, 승무원 온도는 체온으로 오독해 의미 불명",
    186: "승인 근거가 채굴 장비 온도의 것으로 불일치하고, 승무원 폭은 의미 불명",
    202: "승인 근거가 요가 재고의 것으로 불일치하고, 데이터베이스 실링은 의미 불명",
    242: "승인 근거가 카풀 매칭의 것으로 불일치하고, 기부 타이머는 의미 불명",
    251: "승인 근거가 장바구니 견적의 것으로 불일치하고, 석고보드 갱신은 리노베이션 시공으로 읽혀 SaaS 불일치",
    277: "승인 근거가 냉매 온도의 것으로 불일치하고, 채굴 장비 폭은 장비 사양으로 읽혀 SaaS 불일치",
    332: "승인 근거가 배관 피팅 호환 조회의 것으로 불일치하고, 개스킷 발생 빈도는 의미가 성립하지 않음",
    335: "승인 근거가 실내 환기 온도의 것으로 불일치하고, 제네릭 폭은 의미 불명",
    371: "승인 근거가 여과 펌프 압력의 것으로 불일치하고, 하이라이트 높이는 의미 불명",
    416: "승인 근거가 침해사고 빈도의 것으로 불일치하고, 지연 밝기는 의미 불명",
    471: "승인 근거가 멀칭 수요 예보의 것으로 불일치하고, 모기 참조는 참조 대상이 불분명해 의미 불명",
    482: "승인 근거가 세탁 얼룩 진단의 것으로 불일치하고, 멀칭 지속 기간은 의미 불명",
    505: "승인 근거가 통근비 정산의 것으로 불일치하고, 과수원 지명은 의미 불명",
    524: "승인 근거가 위탁 화물 빈도의 것으로 불일치하고, 급여 밝기는 의미 불명",
    610: "승인 근거가 용접 작업 기록의 것으로 불일치하고, 해결 호환성은 의미 불명",
    618: "승인 근거가 묘비 규격 선택의 것으로 불일치하고, 설치류 온보딩은 온보딩 대상이 불분명해 의미 불명",
    654: "승인 근거가 클리어런스 포털의 것으로 불일치하고, 판매자 호환성은 의미 불명",
    663: "승인 근거가 주차장 충전 전력의 것으로 불일치하고, 슬라이드쇼 전압은 의미 불명",
    664: "승인 근거가 주차장 조명의 것으로 불일치하고, 슬라이드쇼 전력은 의미 불명",
    674: "승인 근거가 해변 방문객의 것으로 불일치하고, Snake Pressure는 배관 오퍼 압력 사양이나 뱀으로 오독해 의미 불명",
    679: "승인 근거가 화장 처리량의 것으로 불일치하고, 얼룩 지속 기간은 의미 불명",
    694: "승인 근거가 네트워크 지연 빈도의 것으로 불일치하고, 터미널 밝기는 의미 불명",
}

TM_FLIP = {
    134: "CloudForecast 등 동명 클라우드 비용 예측 서비스와 유사한 상표 우려",
    543: "PhishLabs 보안 회사명과 유사한 상표 우려",
}

DUP_FLIP = {
    120: "이미 승인된 Clearance Alert와 같은 세일 가격 하락 알림·감시 계열 의미중복",
    139: "이미 승인된 Cloud Diagnostic와 같은 진단·측정 계열 의미중복",
    146: "이미 승인된 Database Temperature와 같은 서버실·데이터센터 온도 계열 의미중복",
    181: "이미 승인된 Cremation Load와 같은 화장 처리 물량 계열 의미중복",
    245: "이미 승인된 Donation Load와 같은 기부 접수·처리 물량 계열 의미중복",
    256: "이미 승인된 Dumbbell Scheduler와 같은 운동 일정·계획 계열 의미중복",
    298: "이미 승인된 Ferry Scheduler와 같은 페리 일정·배차 계열 의미중복",
    370: "이미 승인된 Filter Temperature와 같은 수영장 수온 관리 계열 의미중복",
    394: "이미 승인된 Request Load와 같은 고객 문의 처리 물량 계열 의미중복",
    439: "이미 승인된 Marina Availability와 같은 계류권 가용 조회 계열 의미중복",
    450: "이미 승인된 Medication Compatibility와 같은 약물 병용 호환 계열 의미중복",
    451: "이미 승인된 Medication 계열과 같은 복약 주기 의미중복",
    452: "이미 승인된 Medication Temperature와 같은 의약품 보관 온도 계열 의미중복",
    678: "이미 승인된 Stain Type과 같은 얼룩 식별·분류 계열 의미중복",
    702: "이미 승인된 Infant Height와 같은 영유아 성장 기록 계열 의미중복",
    703: "이미 승인된 Infant Temperature와 같은 영유아 체온 기록 계열 의미중복",
    712: "이미 승인된 Tractor Quote와 같은 임대 비용 산출 계열 의미중복",
    715: "이미 승인된 Tractor Warranty와 같은 장비 보증 계열 의미중복",
    743: "이미 승인된 Haul Frequency와 같은 이사 운행 빈도 계열 의미중복",
    784: "이미 승인된 Welding Diagnostic와 같은 용접 품질 검사 계열 의미중복",
    787: "이미 승인된 Welding Warranty와 같은 용접 품질 보증 계열 의미중복",
    799: "이미 승인된 Welding Load와 같은 용접 작업 물량 계열 의미중복",
}

FREQ_FOLD = {
    6: "이미 승인된 Admission Load와 같은 입소 처리 계열 의미중복",
    14: "이미 승인된 Alarm Load와 같은 경보 대응 계열 의미중복",
    30: "이미 승인된 Applicant Load와 같은 지원 처리 계열 의미중복",
    39: "이미 승인된 Arbitration Load와 같은 분쟁 중재 계열 의미중복",
    41: "이미 승인된 Assignment Load와 같은 사고 배정 처리 계열 의미중복",
    60: "이미 승인된 Bike Load와 같은 보관소 이용·수용 계열 의미중복",
    109: "이미 승인된 Checkout Load와 같은 주문 처리 계열 의미중복",
    123: "이미 승인된 Client Load와 같은 고객 배정 계열 의미중복",
    155: "이미 승인된 Compensation Load와 같은 클레임·보상 계열 의미중복",
    187: "이미 승인된 Custodian Load와 같은 시설 관리 작업 계열 의미중복",
    194: "이미 승인된 Database Load와 같은 DB 사용량 계열 의미중복",
    206: "이미 승인된 Daycare Load와 같은 보육 이용·수용 계열 의미중복",
    214: "이미 승인된 Diagnosis Load와 같은 진단 업무 계열 의미중복",
    216: "이미 승인된 Disclosure Load와 같은 공시 처리 계열 의미중복",
    221: "이미 승인된 Doctor Load와 같은 진료 배정 계열 의미중복",
    262: "이미 승인된 Emergency Load와 같은 응급 대응 계열 의미중복",
    266: "이미 승인된 Endorsement Load와 같은 특약 처리 계열 의미중복",
    268: "이미 승인된 Endpoint Load와 같은 단말 보안 점검 계열 의미중복",
    272: "이미 승인된 Equipment Load와 같은 채굴 장비 가동 계열 의미중복",
    285: "이미 승인된 Excursion Load와 같은 투어 처리 계열 의미중복",
    287: "이미 승인된 Exhibitor Load와 같은 행사 참가 운영 계열 의미중복",
    289: "이미 승인된 Extraction Load와 같은 발치 처리 계열 의미중복",
    291: "이미 승인된 Feedback Load와 같은 피드백 처리 계열 의미중복",
    307: "이미 승인된 Filing Load와 같은 사건 접수 계열 의미중복",
    317: "이미 승인된 Fluency Load와 같은 통역 배정 계열 의미중복",
    323: "이미 승인된 Funnel Load와 같은 퍼널 유입 계열 의미중복",
    336: "이미 승인된 Grazing Load와 같은 방목 운영 계열 의미중복",
    373: "이미 승인된 Hold Depth와 같은 대기열 계열 의미중복",
    395: "이미 승인된 Interaction Load와 같은 병용 검사 계열 의미중복",
    400: "이미 승인된 Interview Load와 같은 면접 처리 계열 의미중복",
    404: "이미 승인된 Job Load와 같은 채용 공고 처리 계열 의미중복",
    420: "이미 승인된 Licensing Load와 같은 라이선스 계약 처리 계열 의미중복",
    428: "이미 승인된 Locksmith Load와 같은 출동 작업 계열 의미중복",
    447: "이미 승인된 Medication Load와 같은 투약 관리 계열 의미중복",
    458: "이미 승인된 Monitoring Load와 같은 알림 처리 계열 의미중복",
    476: "이미 승인된 Motor Load와 같은 펌프 가동 계열 의미중복",
    490: "이미 승인된 Museum Load와 같은 관람객 수용 계열 의미중복",
    493: "이미 승인된 Offboarding Load와 같은 퇴사 처리 계열 의미중복",
    498: "이미 승인된 Orchard Load와 같은 농장 작업·수확 계열 의미중복",
    541: "이미 승인된 Phishing Load와 같은 피싱 대응 계열 의미중복",
    557: "이미 승인된 Plumbing Load와 같은 배관 작업 계열 의미중복",
    578: "이미 승인된 Punchlist Load와 같은 결함 작업 계열 의미중복",
    600: "이미 승인된 Reimbursement Load와 같은 환급 처리 계열 의미중복",
    608: "이미 승인된 Request Load와 같은 고객 문의 계열 의미중복",
    611: "이미 승인된 Resort Load와 같은 투숙 수용 계열 의미중복",
    730: "이미 승인된 Transfer Load와 같은 상담 이관 계열 의미중복",
    744: "이미 승인된 Underwriting Load와 같은 인수 심사 계열 의미중복",
    763: "이미 승인된 Venue Load와 같은 대관 수용 계열 의미중복",
    766: "이미 승인된 Vet Load와 같은 진료 계열 의미중복",
    776: "이미 승인된 Waybill Load와 같은 운송장 발행 계열 의미중복",
}

ALL_FLIPS = {}
for d in (CLARITY_FLIP, TM_FLIP, DUP_FLIP, FREQ_FOLD):
    overlap = set(ALL_FLIPS) & set(d)
    assert not overlap, f"flip index overlap: {overlap}"
    ALL_FLIPS.update(d)

n_items = len(req["items"])
assert all(1 <= k <= n_items for k in ALL_FLIPS), "flip index out of range"

decisions = []
for i, item in enumerate(req["items"], 1):
    title = item["title"]
    if i in CLARITY_FLIP:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": False, "duplication": True, "trademark": True},
                          "confidence": 0.7, "reason": CLARITY_FLIP[i]})
    elif i in TM_FLIP:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": True, "duplication": True, "trademark": False},
                          "confidence": 0.7, "reason": TM_FLIP[i]})
    elif i in ALL_FLIPS:
        decisions.append({"title": title, "approve": False,
                          "checks": {"clarity": True, "duplication": False, "trademark": True},
                          "confidence": 0.7, "reason": ALL_FLIPS[i]})
    else:
        decisions.append({"title": title, "approve": True,
                          "checks": {"clarity": True, "duplication": True, "trademark": True},
                          "confidence": 0.65,
                          "reason": "반박 불성립 - " + item["original_reason"]})

assert len(decisions) == n_items
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
print(f"items={n_items} approve={approved} flip={n_items-approved} "
      f"(clarity={len(CLARITY_FLIP)} trademark={len(TM_FLIP)} dup={len(DUP_FLIP)} freq_fold={len(FREQ_FOLD)})")
