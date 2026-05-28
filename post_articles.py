import os
import re
import sys
import json
import base64
import requests
import anthropic
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
load_dotenv()

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
        return json.loads(text, strict=False)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Claude API レスポンスのJSON解析に失敗しました: {e}")
        print(f"レスポンス先頭500文字:\n{text[:500]}")
        raise


_QUOTE_BLOCK_TPL = (
    '<!-- wp:quote {{"className":"edit-hint-block"}} -->\n'
    '<blockquote class="wp-block-quote edit-hint-block">\n'
    '<p>✏️ <strong>EDIT HINT</strong>：{hint}</p>\n'
    '<cite>※このブロックは編集後に削除してください</cite>\n'
    '</blockquote>\n'
    '<!-- /wp:quote -->'
)


def wrap_edit_hints(content: str) -> str:
    # 新形式（引用ブロック）はそのまま通す。
    # 旧形式（<!-- wp:html -->＋HTMLコメント）と裸のHTMLコメントを新形式に変換する。

    def hint_to_block(hint_text: str) -> str:
        return _QUOTE_BLOCK_TPL.format(hint=hint_text.strip())

    def replace_old_wrapped(m):
        raw = m.group(1)
        hint_text = re.sub(r'<!--\s*✏️ EDIT HINT:\s*(.*?)\s*-->', r'\1', raw, flags=re.DOTALL)
        return hint_to_block(hint_text)

    # 旧形式: <!-- wp:html --> + HTMLコメント
    content = re.sub(
        r'<!--\s*wp:html\s*-->\s*(<!--\s*✏️ EDIT HINT:.*?-->)\s*<!--\s*/wp:html\s*-->',
        replace_old_wrapped,
        content,
        flags=re.DOTALL,
    )

    # 裸のHTMLコメント（新形式ブロック内には存在しないため誤マッチしない）
    content = re.sub(
        r'<!--\s*✏️ EDIT HINT:\s*(.*?)\s*-->',
        lambda m: hint_to_block(m.group(1)),
        content,
        flags=re.DOTALL,
    )

    return content


def post_draft(title: str, content: str) -> dict:
    wrapped = wrap_edit_hints(content)
    hint_count = len(re.findall(r'<!-- wp:quote \{"className":"edit-hint-block"\}', wrapped))

    print(f"\n{'=' * 60}")
    print(f"タイトル: {title}")
    print(f"EDIT HINT ブロック数: {hint_count}")

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
