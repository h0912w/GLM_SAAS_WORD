# -*- coding: utf-8 -*-
import json

base = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20260910-153852-KST"
req = json.load(open(base + r"\judgment\review_titles_chunk50_round1_request.json", encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

A = {}

R_DUP = {}

R = {
 "Mirror Advice": "선례 기각(App 기각) 계열",
 "Expiration Workbook": "워크북 대상 불분명",
 "Impressioning Spec": "선례 기각(App 기각) 계열",
 "Testimonial Quantity": "수량 대상 불분명",
 "Balcony Login": "선례 기각(App 기각) 계열",
 "Picnic Analysis": "선례 기각(App 상표 기각) 계열",
 "Tuning Coach": "코칭 대상 불분명",
}

lines = []
na = nr = 0
for t in titles:
    if t in A:
        conf, reason = A[t]
        lines.append(f"{t}\tA\tT\tT\tT\t{conf}\t{reason}")
        na += 1
    elif t in R_DUP:
        lines.append(f"{t}\tR\tT\tF\tT\t0.65\t{R_DUP[t]}")
        nr += 1
    elif t in R:
        lines.append(f"{t}\tR\tF\tT\tT\t0.6\t{R[t]}")
        nr += 1
    else:
        raise SystemExit(f"미판정: {t}")
out = base + r"\_dec_c51.tsv"
open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
print(f"approve={na} reject={nr} total={len(lines)}")
