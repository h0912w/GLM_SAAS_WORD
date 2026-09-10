# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-003906-KST"
req = json.load(open(base + r"\judgment\review_titles_recheck_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

FLIPS = {
 "Container Quantity": ("F", "T", "T", 0.65,
   "수량 지칭으로 제품 불분명(이번 라운드 Quantity 계열 전면 기각과 정합)"),
 "Welding Quantity": ("F", "T", "T", 0.65,
   "수량 지칭으로 제품 불분명(이번 라운드 Quantity 계열 전면 기각과 정합)"),
 "Guardianship Number": ("F", "T", "T", 0.65,
   "번호 지칭으로 제품 불분명(Number 계열 기각 선례와 정합)"),
 "Toast App": ("T", "T", "F", 0.65,
   "유명 SaaS 상표 Toast(레스토랑 POS)와 혼동 우려 - 상표 유사 검사에서 반박"),
}

lines = []
na = nr = 0
for t in titles:
    if t in FLIPS:
        c, d, m, conf, reason = FLIPS[t]
        lines.append(f"{t}\tR\t{c}\t{d}\t{m}\t{conf}\t{reason}")
        nr += 1
    else:
        lines.append(f"{t}\tA\tT\tT\tT\t0.6\t반박 근거 없음 - 명확성·의미중복·상표 재검토 후 1차 승인 유지")
        na += 1
out = base + r"\_dec_recheck.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"maintain={na} flip={nr} total={len(lines)}")
