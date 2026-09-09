import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260909-063619-KST"
req = json.load(open(base + r"\judgment\review_titles_recheck_round1_request.json", encoding="utf-8"))

flips = {
    "Brunch Locator": "반박: 승인된 Brunch Finder(매장 검색기)와 동일 대상 검색 도구로 의미 중복",
    "Daytrip Locator": "반박: 승인된 Daytrip Finder(당일치기 코스 검색)와 동일 대상으로 의미 중복",
    "Deli Locator": "반박: 승인된 Deli Finder(델리 가게 검색)와 동일 대상으로 의미 중복",
    "Desert Locator": "반박: 승인된 Desert Finder(투어 검색)와 동일 대상으로 의미 중복",
    "Dessert Locator": "반박: 승인된 Dessert Finder(디저트 전문점 검색)와 동일 대상으로 의미 중복",
    "Glacier Locator": "반박: 승인된 Glacier Finder(빙하 투어 검색)와 동일 대상으로 의미 중복",
    "Lagoon Locator": "반박: 승인된 Lagoon Finder(라군 명소 검색)와 동일 대상으로 의미 중복",
    "Promenade Locator": "반박: 승인된 Promenade Finder(산책 코스 검색)와 동일 대상으로 의미 중복",
    "Rainforest Locator": "반박: 승인된 Rainforest Finder(투어 검색)와 동일 대상으로 의미 중복",
    "Takeout Locator": "반박: 승인된 Takeout Finder(매장 검색)와 동일 대상으로 의미 중복",
    "Volcano Locator": "반박: 승인된 Volcano Finder(화산 투어 검색)와 동일 대상으로 의미 중복",
    "Wildlife Locator": "반박: 승인된 Wildlife Finder(야생동물 관찰지 검색)와 동일 대상으로 의미 중복",
    "Winery Locator": "반박: 승인된 Winery Finder(와이너리 검색)와 동일 대상으로 의미 중복",
    "Yacht Locator": "반박: 승인된 Yacht Finder(요트 투어 검색)와 동일 대상으로 의미 중복",
    "Bruxism Guarantor": "반박: 보험 청구 보증인 관리 개념이 이갈이 치료와 결합 불자연, 보증인 대상 불명",
    "Gingivitis Guarantor": "반박: 보험 청구 보증인 관리 개념이 잇몸염 치료와 결합 불자연, 보증인 대상 불명",
    "Sealant Guarantor": "반박: 보험 청구 보증인 관리 개념이 실란트 시술과 결합 불자연, 보증인 대상 불명",
    "Floss Registry": "반박: 승인된 Floss Journal(치실 사용 기록 저널)와 의미 중복",
    "Wildlife Registry": "반박: 승인된 Wildlife Register(관찰 기록 대장)와 의미 중복",
    "Cafe Timer": "반박: 승인된 Espresso Clock(에스프레소 추출 타이머)와 동일 기능으로 의미 중복",
    "Espresso Timer": "반박: 승인된 Espresso Clock(에스프레소 추출 타이머)와 동일 도메인 동일 기능 의미 중복",
    "Latte Timer": "반박: 승인된 Espresso Clock(에스프레소 추출 타이머)와 동일 기능으로 의미 중복",
    "Cafe Estimator": "반박: 승인된 Cafe Calculator(원가 계산기)와 동일 도메인 동일 기능 의미 중복",
    "Espresso Estimator": "반박: 승인된 Espresso Calculator(원가 계산기)와 동일 도메인 동일 기능 의미 중복",
    "Latte Estimator": "반박: 승인된 Latte Calculator(음료 원가 계산기)와 동일 도메인 동일 기능 의미 중복",
    "Cafe Message": "반박: 승인된 Cafe Notification(주문 알림 발송)과 의미 중복",
    "Espresso Message": "반박: 승인된 Espresso Notification(주문 알림 발송)과 의미 중복",
    "Snorkeling Evaluation": "반박: 승인된 Snorkeling Rating·Review(평점·후기 수집)와 의미 중복",
    "Waterfall Opinion": "반박: 승인된 Waterfall Review·Rating(후기·평점 수집)과 의미 중복",
    "Takeout Plan": "반박: 승인된 Takeout Planner(테이크아웃 계획 도구)와 의미 중복",
    "Yacht Journal": "반박: 승인된 Yacht Log(요트 운항 기록지)와 동일 대상 기록 도구로 의미 중복",
    "Skyline Trail": "반박: 승인된 Skyline Route(도심 전망 투어 코스)와 의미 중복",
    "Volcano Passport": "반박: 승인된 Volcano Card(화산 투어 스탬프 카드)와 동일 스탬프 개념 의미 중복",
    "Periodontitis Bill": "반박: 승인된 Periodontics Bill(치주 치료 청구 도구)와 치주염·치주과 동일 대상 의미 중복",
    "Periodontitis Estimate": "반박: 승인된 Periodontics Estimate(치주 치료 견적 도구)와 동일 대상 의미 중복",
    "Periodontitis Order": "반박: 승인된 Periodontics Order(치주 치료 지시 관리)와 동일 대상 의미 중복",
}

keeps = {
    "Floss Followup": "치실 사용 지도 후속 관리 도구 (1차 사유의 불소 도포 표기는 도메인 불일치였으나 제목 자체는 성립)",
    "Floss Questionnaire": "치실 사용 습관 문진표 관리 도구 (1차 사유의 불소 도포 표기는 도메인 불일치였으나 제목 자체는 성립)",
    "Hygienist Followup": "치위생 시술 후속 관리 도구 (1차 사유의 도포 표기는 도메인 불일치였으나 제목 자체는 성립)",
    "Hygienist Questionnaire": "치위생 문진표 관리 도구 (1차 사유의 도포 표기는 도메인 불일치였으나 제목 자체는 성립)",
}

titles = [it["title"] for it in req["items"]]
missing_f = [t for t in flips if t not in titles]
missing_k = [t for t in keeps if t not in titles]
assert not missing_f, f"flip 대상 없음: {missing_f}"
assert not missing_k, f"keep 교정 대상 없음: {missing_k}"

lines = []
na = nr = 0
for it in req["items"]:
    t = it["title"]
    if t in flips:
        lines.append(f"{t}\tR\tF\tT\tT\t0.6\t{flips[t]}")
        nr += 1
    else:
        reason = keeps.get(t) or it.get("original_reason") or "1차 판정 기준 재적용, 반박 근거 없음"
        lines.append(f"{t}\tA\tT\tT\tT\t0.6\t{reason}")
        na += 1

out = base + r"\_dec_recheck.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
