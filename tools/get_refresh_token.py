"""
Google Ads OAuth2 Refresh Token 발급 스크립트.

사용법 (PC 브라우저 가능 환경):
    python tools/get_refresh_token.py            # 브라우저 열고 localhost:8080 수신

사용법 (Termius 등 SSH/핸드폰 원격 환경 - 브라우저는 휴대폰 것을 쓴다):
    1) python tools/get_refresh_token.py --print-url
       → 출력된 URL을 휴대폰 브라우저로 열어 Google 승인
    2) 승인 후 휴대폰이 http://localhost:8080/?code=... 로 리다이렉트되면
       "연결할 수 없음" 화면이 떠도 주소창의 code=... 값을 통째로 복사
       (code 유효시간 약 10분, 1회용)
    3) python tools/get_refresh_token.py --code "4/0Axxx..."
       → refresh_token으로 교환해 .env.local에 자동 반영
    4) python tools/get_refresh_token.py --verify
       → 현재 .env.local 토큰으로 access token 발급 시험 (오류 코드만 출력)

필요 정보: Client ID, Client Secret (Google Cloud Console에서 발급, .env.local 자동 로드)
"""

import json
import os
import sys
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

SCOPE = "https://www.googleapis.com/auth/adwords"
REDIRECT_URI = "http://localhost:8080"
AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

_auth_code: str | None = None


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global _auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            _auth_code = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write("<h2>OK - 터미널로 돌아가세요</h2>".encode("utf-8"))
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write("<h2>code 파라미터가 없습니다</h2>".encode("utf-8"))

    def log_message(self, *_):
        pass


def _env_local_path() -> Path:
    return Path(__file__).parent.parent / ".env.local"


def _load_env_local() -> dict:
    env_path = _env_local_path()
    values: dict = {}
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                values[k.strip()] = v.strip()
    return values


def build_auth_url(client_id: str) -> str:
    params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent",
    }
    return AUTH_URL + "?" + urllib.parse.urlencode(params)


def exchange_code(client_id: str, client_secret: str, code: str) -> str:
    data = urllib.parse.urlencode({
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        token_data = json.loads(resp.read())
    refresh_token = token_data.get("refresh_token")
    if not refresh_token:
        raise RuntimeError(f"refresh_token 없음. 응답 키: {sorted(token_data)}")
    return refresh_token


def update_env_local(new_token: str) -> None:
    """GOOGLE_ADS_REFRESH_TOKEN만 교체하고 나머지 줄은 그대로 유지한다(원자적 교체)."""
    env_path = _env_local_path()
    lines = env_path.read_text(encoding="utf-8").splitlines() if env_path.exists() else []
    replaced = False
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("GOOGLE_ADS_REFRESH_TOKEN=") and not stripped.startswith("#"):
            out.append(f"GOOGLE_ADS_REFRESH_TOKEN={new_token}")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        if out and out[-1].strip():
            out.append("")
        out.append(f"GOOGLE_ADS_REFRESH_TOKEN={new_token}")
    tmp = env_path.with_suffix(".tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    os.replace(tmp, env_path)


def verify() -> int:
    env = _load_env_local()
    missing = [k for k in ("GOOGLE_ADS_REFRESH_TOKEN", "GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET") if not env.get(k)]
    if missing:
        print(f"검증 불가: .env.local에 {', '.join(missing)} 없음", file=sys.stderr)
        return 1
    data = urllib.parse.urlencode({
        "refresh_token": env["GOOGLE_ADS_REFRESH_TOKEN"],
        "client_id": env["GOOGLE_ADS_CLIENT_ID"],
        "client_secret": env["GOOGLE_ADS_CLIENT_SECRET"],
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        try:
            err = json.loads(detail)
            print(f"검증 실패: HTTP {exc.code} - {err.get('error')}: {err.get('error_description', '')}")
        except json.JSONDecodeError:
            print(f"검증 실패: HTTP {exc.code} - {detail[:200]}")
        return 1
    print("검증 성공: access token 발급 정상 (토큰 값은 출력하지 않음)")
    return 0


def main():
    args = sys.argv[1:]
    env = _load_env_local()
    client_id = env.get("GOOGLE_ADS_CLIENT_ID") or input("Client ID: ").strip()
    client_secret = env.get("GOOGLE_ADS_CLIENT_SECRET") or input("Client Secret: ").strip()

    if "--print-url" in args:
        print(build_auth_url(client_id))
        return

    if "--code" in args:
        idx = args.index("--code")
        if idx + 1 >= len(args):
            print("사용법: --code \"4/0Axxx...\" (승인 후 주소창에서 복사한 값)", file=sys.stderr)
            sys.exit(1)
        code = args[idx + 1].strip()
        refresh_token = exchange_code(client_id, client_secret, code)
        update_env_local(refresh_token)
        print("OK: 새 refresh_token을 .env.local에 반영했습니다. `--verify`로 시험하세요.")
        return

    if "--verify" in args:
        sys.exit(verify())

    print(f"Client ID: {client_id[:30]}...")
    url = build_auth_url(client_id)
    print(f"\n브라우저가 열립니다. Google 계정으로 승인 후 돌아오세요.\n{url}\n")
    webbrowser.open(url)

    server = HTTPServer(("localhost", 8080), _Handler)
    server.handle_request()

    if not _auth_code:
        print("인증 코드를 받지 못했습니다.", file=sys.stderr)
        sys.exit(1)

    refresh_token = exchange_code(client_id, client_secret, _auth_code)
    print("\n=== .env.local 에 넣을 값 ===")
    print(f"GOOGLE_ADS_REFRESH_TOKEN={refresh_token}")


if __name__ == "__main__":
    main()
