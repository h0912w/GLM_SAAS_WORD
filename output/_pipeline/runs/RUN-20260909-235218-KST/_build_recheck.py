import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260909-235218-KST"
req = json.load(open(base + r"\judgment\review_titles_recheck_round1_request.json", encoding="utf-8"))

flips = {
    "Backpacker Locator": "반박: 승인된 Backpacker Finder(숙소·여행지 검색)와 동일 대상 검색 도구로 의미 중복",
    "Floss Report": "반박: 승인된 Floss Journal(치실 사용 기록 저널)과 동일 사용 이력 기록·요약 의미 중복",
    "Mouthwash Watch": "반박: 승인된 Mouthwash Beacon(재구매 알림)과 재구매 관점 구분 모호, 동일 도메인 중복",
    "Matter Timetable": "반박: 승인된 Paralegal Timetable(사건·기한 일정표)과 동일 도메인 동일 기능 의미 중복",
    "Headhunter Timetable": "반박: 승인된 Recruiting Timetable(채용 일정표)과 동일 채용 일정 관리 의미 중복",
    "Policy Timetable": "반박: 승인된 Policyholder Timetable(보험 갱신·납입 일정표)과 동일 갱신 일정 의미 중복",
    "Deductible Timetable": "반박: 승인된 Policyholder Timetable(보험 갱신 일정표)과 동일 보험 일정 관리 의미 중복",
}

keeps = {
    "Deli Check": "델리 품질·위생 점검 도구 (재고 상태는 승인된 Deli Status가 담당, 점검 기능으로 구분 성립)",
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
