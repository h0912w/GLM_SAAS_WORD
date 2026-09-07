import json, sys, collections, os
sys.stdout.reconfigure(encoding="utf-8")
base = os.path.join(os.path.dirname(__file__), "judgment")
domains = {"Kayak","Runway","Hangar","Marina","Snake","Beach","Overnight","Quarter","Mayor","Deadbolt","Refrigerant","Weighbridge","Wax","Ferry","Urn","Dumbbell","Truck","Surgery","Festival"}
stats = collections.Counter(); ex = collections.defaultdict(list)
for n in range(1, 48):
    with open(os.path.join(base, f"review_titles_chunk{n}_round1_response.json"), encoding="utf-8") as f:
        resp = json.load(f)
    for d in resp["decisions"]:
        w = d["title"].split()
        if len(w) == 2 and w[0] in domains:
            stats[(w[0], d["approve"])] += 1
            if d["approve"] and len(ex[(w[0], True)]) < 4:
                ex[(w[0], True)].append(d["title"] + " (" + d["reason"][:40] + ")")
for dom in sorted(domains):
    a = stats[(dom, True)]; r = stats[(dom, False)]
    print(f"{dom:12s} approve={a:3d} reject={r:3d} | A: {ex[(dom, True)]}")
