import json, sys, urllib.request, urllib.error
from pathlib import Path

env = {}
for line in (Path(__file__).resolve().parents[4] / ".env.local").read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip()

data = urllib.parse.urlencode({
    "refresh_token": env.get("GOOGLE_ADS_REFRESH_TOKEN", ""),
    "client_id": env.get("GOOGLE_ADS_CLIENT_ID", ""),
    "client_secret": env.get("GOOGLE_ADS_CLIENT_SECRET", ""),
    "grant_type": "refresh_token",
}).encode()
req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read())
    sys.exit(0 if body.get("access_token") else 1)
except urllib.error.HTTPError:
    sys.exit(1)
