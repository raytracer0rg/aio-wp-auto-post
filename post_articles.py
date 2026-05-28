import os
import re
import sys
import json
import base64
import requests
import anthropic

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WP_URL = os.environ.get("WP_URL", "https://aiotaisaku.com")
WP_USERNAME = os.environ.get("WP_USERNAME")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD")

CLAUDE_MODEL = "claude-opus-4-7"
CLAUDE_MAX_TOKENS = 16000


def load_claude_md() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, "CLAUDE.md")
    if not os.path.exists(path):
        raise FileNotFoundError(f"CLAUDE.md が見つかりません: {path}")
    with open(path, encoding="utf-8") as f:
        return f.read()


def build_prompt(claude_md: str) -> tuple[str, str]:
    system = f"以下の指示書に厳密に従って記事を生成してください。\n\n{claude_md}"
    user = (
        "指示書に従って3記事を作成してください。\n"
        "出力はJSON配列のみとし、コードブロック（```）は不要です。\n\n"
        "[\n"
        "  {\"title\": \"記事タイトル\", \"content\": \"記事本文（HTML形式）\"},\n"
        "  ...\n"
        "]"
    )
    return system, user


def generate_articles(system: str, user: str) -> list[dict]:
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=CLAUDE_MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = message.content[0].text.strip()
    match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if match:
        text = match.group(1)
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Claude API レスポンスのJSON解析に失敗しました: {e}")
        print(f"レスポンス先頭500文字:\n{text[:500]}")
        raise


def wrap_edit_hints(content: str) -> str:
    # WordPress は通常の HTML コメントを保存時に削除するため wp:html ブロック内で保持する。
    # CLAUDE.md の指示で既にラップ済みの場合も考慮し、一旦除去してから統一的に再付与する。
    content = re.sub(
        r'<!--\s*wp:html\s*-->\s*(<!--\s*✏️ EDIT HINT:.*?-->)\s*<!--\s*/wp:html\s*-->',
        r'\1',
        content,
        flags=re.DOTALL,
    )
    pattern = r'(<!--\s*✏️ EDIT HINT:.*?-->)'
    def replacer(m):
        return f"<!-- wp:html -->\n{m.group(1)}\n<!-- /wp:html -->"
    return re.sub(pattern, replacer, content, flags=re.DOTALL)


def post_draft(title: str, content: str) -> dict:
    hints = re.findall(r'<!--\s*✏️ EDIT HINT:.*?-->', content, re.DOTALL)

    print(f"\n{'=' * 60}")
    print(f"タイトル: {title}")
    print(f"EDIT HINT コメント数: {len(hints)}")
    for i, hint in enumerate(hints, 1):
        preview = hint[:120] + ("..." if len(hint) > 120 else "")
        print(f"  [{i}] {preview}")

    wrapped = wrap_edit_hints(content)

    print(f"\n--- WordPress送信直前コンテンツ（先頭600文字）---")
    print(wrapped[:600])
    print(f"{'=' * 60}\n")

    token = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    resp = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
        },
        json={
            "title": title,
            "content": wrapped,
            "status": "draft",
        },
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    print(f"[投稿成功] ID={result.get('id')}  URL={result.get('link')}")
    return result


def main():
    claude_md = load_claude_md()
    system, user = build_prompt(claude_md)

    if os.environ.get("DEBUG_PROMPT") == "1":
        print("=" * 60)
        print("[DEBUG] system prompt 全文:")
        print(system)
        print("-" * 60)
        print("[DEBUG] user message 全文:")
        print(user)
        print("=" * 60)

    print("Claude API で記事を生成中...")
    articles = generate_articles(system, user)
    print(f"生成記事数: {len(articles)}")
    for article in articles:
        post_draft(article["title"], article["content"])


if __name__ == "__main__":
    main()
