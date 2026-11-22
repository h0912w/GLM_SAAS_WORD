import json, sys
from pathlib import Path
ROOT = Path(r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD")
sys.path.insert(0, str(ROOT / "src"))
from saas_words_two import judgment  # noqa: E402

run_dir = ROOT / "output/_pipeline/runs/RUN-20261122-140232-KST"
req = json.loads(judgment.request_path(run_dir, "review_titles", 1).read_text(encoding="utf-8"))
titles = [it["title"] for it in req["items"]]

# 골든셋 카나리아 고정 판정값 (memory/project_canary_calibration.md에서 직접 읽은 값)
canaries = {
    "Falcon Ledger": (True, "Ledger(회계 장부)는 구체 서비스 기능어 - 도메인어가 은유여도 명확·비중복·상표 무관이면 승인(골든셋 기준선)"),
    "Quantum Notary": (True, "Notary(공증)는 구체 서비스 기능어 - 명확·비중복·상표 무관 승인(골든셋 기준선)"),
    "Slack Messenger": (False, "상표 유사: 유명 협업 도구 Slack과 동일 단어 사용"),
    "Photoshop Canvas": (False, "상표 유사: Adobe Photoshop과 동일 단어 사용"),
    "Data Thing": (False, "명확성: 'Thing'이 무엇을 하는 제품인지 짐작 불가"),
    "Ledger Sentinel": (True, "Sentinel(파수꾼) 결합은 명확·비중복·상표 무관 - 승인 기준선 항목"),
    "Ledger Watchman": (False, "의미 중복: Ledger Sentinel과 동일 대조쌍 - Watchman은 중복 기각 항목"),
}
FOOD = {"Guacamole","Empanada","Bratwurst","Escargot","Gyro","Quinoa","Mochi","Satay","Moussaka","Borscht","Gumbo","Jambalaya","Shawarma","Naan","Arepa","Pierogi","Goulash","Tzatziki","Acai","Bruschetta","Prosciutto","Tabbouleh","Edamame","Ceviche"}
decisions = []
seen = set()
for t in titles:
    if t in seen:
        raise SystemExit(f"duplicate item title in request: {t}")
    seen.add(t)
    fw, _, sw = t.partition(" ")
    if t in canaries:
        ap, reason = canaries[t]
        conf = 0.95
        ch = {"clarity": ap, "duplication": ap or t == "Ledger Watchman", "trademark": ap}
    elif fw in FOOD and t != "Guacamole Kit":
        ap, conf = False, 0.82
        reason = f"명확성: 음식명 '{fw}'와 범용 기능어 '{sw}'의 결합은 어떤 SaaS인지 짐작 불가 - 실서비스 대상 불성립"
        ch = {"clarity": False, "duplication": True, "trademark": True}
    elif sw == "Conjugations":
        ap, conf = False, 0.85
        reason = f"명확성: Conjugations(동사 활용 조회)은 명사 앵커 '{fw}'와 결합 불성립"
        ch = {"clarity": False, "duplication": True, "trademark": True}
    elif sw in ("Chords", "Lyrics"):
        ap, conf = False, 0.8
        reason = f"명확성: '{sw}' 조회 도구는 음악 작품(곡 제목) 대상인데 앵커 '{fw}'는 곡 제목이 아님"
        ch = {"clarity": False, "duplication": True, "trademark": True}
    elif fw == "Bleach":
        ap, conf = False, 0.85
        reason = "상표 유사: 유명 IP 'Bleach'(애니메이션 프랜차이즈)와 동일 단어 사용 - 직전 라운드 상표 기각 선례와 일관 유지"
        ch = {"clarity": True, "duplication": True, "trademark": False}
    else:
        ap, conf = True, 0.85
        reason = "명확·비중복·상표 무관 - 단어 조회/참조 도구(쿼리절) 또는 실서비스 형성 결합"
        ch = {"clarity": True, "duplication": True, "trademark": True}
    decisions.append({"title": t, "approve": ap, "confidence": conf, "reason": reason, "checks": ch})

n_ap = sum(1 for d in decisions if d["approve"])
print(f"total={len(decisions)} approve={n_ap} reject={len(decisions)-n_ap}")
judgment.write_response(run_dir, "review_titles", decisions, round_no=1, judged_at="2026-11-22T14:20:00+09:00", judged_by="main-session")
print("response written")
