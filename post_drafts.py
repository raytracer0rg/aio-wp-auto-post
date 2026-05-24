#!/usr/bin/env python3
"""AIO関連の最新ニュース記事をWordPressに下書き投稿するスクリプト。"""

import os
import json
import requests

WP_URL = os.environ.get("WP_URL", "https://aiotaisaku.com")
WP_USERNAME = os.environ.get("WP_USERNAME", "")
WP_APP_PASSWORD = os.environ.get("WP_APP_PASSWORD", "")

ARTICLES = [
    {
        "title": "【速報】Google 2026年5月コアアップデート開始！AI検索・AIO対策への影響と緊急チェックポイント",
        "content": """<p>2026年5月22日、Googleは「May 2026 Core Update（2026年5月コアアップデート）」のロールアウトを開始したと公式に発表しました。今年2回目となるこの広範なアルゴリズムアップデートは、完了まで最大2週間を要する見込みで、現在も継続中です。</p>

<h2>今回のアップデートの主な評価強化ポイント</h2>

<p>今回のコアアップデートでは、特に3つの要素が同時に評価強化されています。</p>

<h3>1. 検索意図の解釈精度の向上</h3>
<p>ユーザーが本当に求めている情報を理解する精度が高まります。従来のキーワードマッチング重視から、コンテキスト全体を踏まえた解釈へシフトしています。</p>

<h3>2. コンテンツの深さの重視</h3>
<p>表面的な情報をまとめただけのコンテンツではなく、独自の専門知識・一次情報・実体験を含む深いコンテンツが評価されます。生成AIが容易に複製できないオリジナルの洞察が求められます。</p>

<h3>3. ページ体験の強化評価</h3>
<p>Core Web Vitalsや安全性、モバイル対応といったページ体験指標の評価もあわせて強化されています。</p>

<h2>AI Overview（AIO）への直接的な影響</h2>

<p>2026年5月時点で全検索クエリの48%以上にAI Overviewが表示される中、今回のコアアップデートはAI検索の引用ソース選定にも直接影響します。GoogleのコアシステムとAI Overviewは同じランキング品質システムに根差しているため、コアアップデートでの順位変動はそのままAI引用への登場機会にも波及します。</p>

<p>過去のデータでは、AI Overviewの引用ソースは従来のトップ10サイトからの引用が約76%を占めていましたが、2026年初頭の調査では17〜54%まで低下。RedditやニッチなQ&Aサイト、構造化データソースからの引用が顕著に増加しており、今回のアップデートでこの傾向がさらに加速する可能性があります。</p>

<h2>今すぐ確認すべき対策</h2>

<p>コアアップデートへの対応として以下を確認してください。</p>

<ul>
<li>Google Search Consoleでクリック数・表示回数・AI Overview経由のトラフィック変化をモニタリング</li>
<li>既存コンテンツの独自性を見直し、他サイトでは書けない一次情報や専門的視点を補強</li>
<li>E-E-A-T（経験・専門性・権威性・信頼性）の観点からコンテンツを再評価</li>
<li>著者プロフィールや組織情報の透明性を高め、信頼性シグナルを強化</li>
</ul>

<p>コアアップデートは通常、公開から数日以内に大きな変動が見られます。まずは今週の動向を注視しながら、長期的なコンテンツ品質の向上に取り組むことが最善策です。</p>""",
    },
    {
        "title": "Google I/O 2026発表まとめ：AI検索が「答える」から「行動する」エージェント時代へ突入",
        "content": """<p>2026年5月19日〜20日に開催されたGoogle I/O 2026では、検索に関する重大な発表が相次ぎました。Googleは今回の検索体験刷新を「過去25年で最大の変革」と表現しており、AI検索が単に「答える」だけでなく、ユーザーに代わって「行動する」エージェントとして機能する時代が本格的に始まりました。</p>

<h2>AI Modeの全面展開とGemini 3.5の採用</h2>

<p>Google I/O 2026最大の発表の一つが「AI Mode」のグローバル全面展開です。Gemini 3.5 Flashをデフォルトモデルとして採用し、従来のキーワード検索に加え、AIが会話形式でユーザーの質問を深堀りしながら複雑なリクエストに対応します。</p>

<p>また、検索ボックス自体も過去25年で初めての大幅な拡張が行われました。ユーザーが自然言語でより詳細な条件や文脈を入力できるよう設計され、AIによる文脈理解を活かした精度の高い回答が可能になります。</p>

<h2>Search Agents（サーチエージェント）の登場</h2>

<p>特に注目すべきは「Search Agents」と呼ばれる新機能です。ユーザーが指定した条件（例：「駅から徒歩5分・3LDK・家賃15万円以下の物件」）に合う情報を継続的に追い続け、条件が満たされた際に自動的に通知する機能です。</p>

<p>これにより、「検索してリンク一覧を見る」という体験から「AIが代わりに探し続けて知らせてくれる」体験へと検索の本質が変わります。BtoBの文脈でも、競合動向・価格変動・入札情報などの継続モニタリングへの応用が期待されます。</p>

<h2>AIO・LLMOへの実務的な影響</h2>

<p>AI Modeの普及によって、ユーザーの検索行動はさらにAI回答へと移行します。これは従来のSEOクリックがAI回答で代替されるケースが増えることを意味しており、自然検索クリック率の低下が一層加速する見通しです。</p>

<p>一方で、AI ModeやSearch Agentsがソースとして参照するコンテンツには独自データや専門的洞察が求められており、質の高いコンテンツの重要性は増すばかりです。単なる情報の集約ではなく、AIが引用したくなる「一次情報・独自見解・実証データ」を持つコンテンツ制作への転換が急務です。</p>

<h2>今後のAIO戦略への示唆</h2>

<p>Google I/O 2026の発表を踏まえ、コンテンツ制作者・マーケターに求められる姿勢は明確です。AIに「使われるコンテンツ」を目指し、独自性の高い情報発信を続けることが、AI検索時代の生き残り戦略となります。</p>""",
    },
    {
        "title": "Google公式「生成AI検索最適化ガイド」解説：無効と断言された4施策と本当に効くAIO対策",
        "content": """<p>2026年5月15日、Googleは「Google検索の生成AI機能に向けたウェブサイト最適化（Optimizing your website for generative AI features on Google Search）」と題した公式ガイドを公開しました。AI検索の最適化（AIO・LLMO・GEO）についてGoogleが公式見解を示したのは初めてのことであり、業界に大きな反響をもたらしています。</p>

<h2>公式ガイドの核心メッセージ</h2>

<p>ガイドの最も重要なポイントは「AI OverviewsやAI Modeなどの生成AI機能は、コアとなる検索ランキング・品質システムに根差している」という宣言です。つまり、SEOの基本がAIO対策の基盤でもあるということであり、「AIO専用の特別なテクニック」を探している担当者には重要なメッセージといえます。</p>

<h2>Googleが「無効」と明言した4つの施策</h2>

<p>ガイドの中でGoogleは以下の施策について、明確に「効果がない」と否定しています。</p>

<h3>1. llms.txtなどのAI向けテキストファイルの作成</h3>
<p>AI検索クローラー専用の設定ファイルを設置しても、AI Overviewsへの引用可能性は変わりません。Googleのクローラーは標準のrobots.txtとHTMLの構造を参照しており、追加ファイルに特別な効果はありません。</p>

<h3>2. コンテンツの「チャンク化」</h3>
<p>LLMが処理しやすいよう文章を意図的に短く分割する手法です。Googleのシステムはコンテンツを文脈ごと理解するため、人為的なチャンク分割は不要どころか読みやすさを損なう可能性があります。</p>

<h3>3. AI検索向けのみのコンテンツ書き直し</h3>
<p>AI回答での引用を目的として既存コンテンツをリライトする行為は意味がないと明言されました。ユーザーにとって有益なコンテンツが結果的にAIにも引用されるという原則が改めて確認されました。</p>

<h3>4. 不正確なサイテーション工作</h3>
<p>ウェブ上で人工的に言及・引用を増やそうとするブラックハット的施策も明確に否定されています。</p>

<h2>Googleが推奨する本質的なAIO対策</h2>

<p>一方、Googleが有効と示す方向性は以下の通りです。</p>

<ul>
<li><strong>独自の一次情報・体験・専門知識を持つコンテンツの作成</strong>：生成AIが容易に複製できない固有の情報こそが引用価値を持つ</li>
<li><strong>技術的なクローラビリティの確保</strong>：適切なHTMLマークアップ、robots.txtの設定、ページ速度の最適化</li>
<li><strong>高品質な画像・動画の活用</strong>：テキスト以外のメディアも引き続き評価対象</li>
<li><strong>E-E-A-Tの継続的な強化</strong>：著者プロフィール・組織情報の充実、一次情報ソースへのリンク</li>
</ul>

<p>今後のAIO対策は「AIへの小手先テクニック」ではなく「本質的なコンテンツ価値の追求」に集約されることが、Googleの公式見解によって明確になりました。地道にE-E-A-Tを高め、独自情報を発信し続けることが最も確実なAI検索時代の生存戦略です。</p>""",
    },
]


def get_existing_titles(session):
    """既存の投稿タイトルを取得して重複投稿を防ぐ。"""
    resp = session.get(
        f"{WP_URL}/wp-json/wp/v2/posts",
        params={"status": "draft,publish", "per_page": 100},
        timeout=30,
    )
    if resp.status_code != 200:
        print(f"既存記事取得エラー: {resp.status_code} {resp.text[:200]}")
        return set()
    posts = resp.json()
    return {p["title"]["rendered"] for p in posts}


def post_draft(session, title, content):
    """記事を下書きとして投稿する。"""
    payload = {
        "title": title,
        "content": content,
        "status": "draft",
    }
    resp = session.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        json=payload,
        timeout=30,
    )
    return resp


def main():
    if not WP_USERNAME or not WP_APP_PASSWORD:
        raise SystemExit("WP_USERNAME / WP_APP_PASSWORD 環境変数が設定されていません")

    session = requests.Session()
    session.auth = (WP_USERNAME, WP_APP_PASSWORD)

    print("既存の投稿を確認中...")
    existing_titles = get_existing_titles(session)
    print(f"既存投稿数: {len(existing_titles)}")

    posted = 0
    skipped = 0

    for article in ARTICLES:
        title = article["title"]

        if title in existing_titles:
            print(f"[スキップ] 重複: {title}")
            skipped += 1
            continue

        print(f"[投稿中] {title}")
        resp = post_draft(session, title, article["content"])

        if resp.status_code == 201:
            data = resp.json()
            print(f"[成功] ID:{data['id']} ステータス:{data['status']} — {title}")
            posted += 1
        else:
            print(f"[失敗] {resp.status_code}: {resp.text[:300]}")

    print(f"\n完了: {posted}件投稿, {skipped}件スキップ")


if __name__ == "__main__":
    main()
