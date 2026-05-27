import os
import re
import json
import base64
import requests

WP_URL = os.environ.get("WP_URL", "https://aiotaisaku.com")
WP_USERNAME = os.environ.get("WP_USERNAME")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD")


def wrap_edit_hints(content: str) -> str:
    """<!-- ✏️ EDIT HINT: ... --> を Gutenberg カスタム HTML ブロックで囲む。
    通常のHTMLコメントはGutenbergが保存時に削除するが、wp:html ブロック内なら保持される。
    """
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
    articles_file = "articles.json"
    if not os.path.exists(articles_file):
        print(f"[ERROR] {articles_file} が見つかりません")
        return

    with open(articles_file, encoding="utf-8") as f:
        articles = json.load(f)

    print(f"投稿対象記事数: {len(articles)}")
    for article in articles:
        post_draft(article["title"], article["content"])


if __name__ == "__main__":
    main()
