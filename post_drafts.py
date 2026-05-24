import os
import json
import glob
import requests
from requests.auth import HTTPBasicAuth

WP_URL = os.environ.get("WP_URL", "https://aiotaisaku.com")
WP_USERNAME = os.environ.get("WP_USERNAME")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD")

POSTS_ENDPOINT = f"{WP_URL}/wp-json/wp/v2/posts"


def get_existing_titles(auth):
    existing = set()
    page = 1
    while True:
        resp = requests.get(
            POSTS_ENDPOINT,
            params={"per_page": 100, "page": page, "status": "any"},
            auth=auth,
            timeout=30,
        )
        if resp.status_code != 200:
            break
        posts = resp.json()
        if not posts:
            break
        for post in posts:
            title = post.get("title", {}).get("rendered", "")
            existing.add(title.strip())
        page += 1
    return existing


def post_draft(auth, title, content):
    resp = requests.post(
        POSTS_ENDPOINT,
        json={"title": title, "content": content, "status": "draft"},
        auth=auth,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main():
    if not WP_USERNAME or not WP_APP_PASSWORD:
        raise SystemExit("ERROR: WP_USERNAME and WP_APP_PASSWORD must be set")

    auth = HTTPBasicAuth(WP_USERNAME, WP_APP_PASSWORD)

    print("既存投稿のタイトルを取得中...")
    existing_titles = get_existing_titles(auth)
    print(f"  既存記事数: {len(existing_titles)}")

    draft_files = sorted(glob.glob("drafts/*.json"))
    if not draft_files:
        print("投稿する下書きファイルが見つかりません")
        return

    posted = 0
    skipped = 0
    for path in draft_files:
        with open(path, encoding="utf-8") as f:
            draft = json.load(f)

        title = draft.get("title", "").strip()
        content = draft.get("content", "").strip()

        if not title or not content:
            print(f"  SKIP (空): {path}")
            skipped += 1
            continue

        if title in existing_titles:
            print(f"  SKIP (重複): {title}")
            skipped += 1
            continue

        result = post_draft(auth, title, content)
        print(f"  POSTED id={result['id']}: {title}")
        posted += 1

    print(f"\n完了: {posted}件投稿, {skipped}件スキップ")


if __name__ == "__main__":
    main()
