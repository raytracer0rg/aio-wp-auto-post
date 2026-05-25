#!/usr/bin/env python3
"""
AIOネタ自動下書き投稿スクリプト
CLAUDE.mdの手順に従い3記事をWordPressに下書き投稿する。

使用方法:
  1. .envファイルを作成して認証情報を設定
     WP_URL=https://aiotaisaku.com
     WP_USERNAME=<ユーザー名>
     WP_APP_PASSWORD=<アプリケーションパスワード>
  2. python3 post_drafts.py
"""

import os
import sys
import base64
import requests

def load_env():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip())

load_env()

WP_URL = os.environ.get("WP_URL", "https://aiotaisaku.com") + "/wp-json/wp/v2/posts"
WP_USER = os.environ.get("WP_USERNAME", "")
WP_PASS = os.environ.get("WP_APP_PASSWORD", "")

if not WP_USER or not WP_PASS:
    print("エラー: .envファイルにWP_USERNAMEとWP_APP_PASSWORDを設定してください。")
    sys.exit(1)

credentials = base64.b64encode(f"{WP_USER}:{WP_PASS}".encode()).decode()
headers = {
    "Authorization": f"Basic {credentials}",
    "Content-Type": "application/json",
}

# ============================================================
# 記事1: Google I/O 2026 AI検索大変革（海外情報ベース）
# ============================================================
article1_title = "Google I/O 2026でAI検索が激変——Gemini 3.5 Flash搭載AI Modeが10億ユーザー突破、SEO担当者が今すぐ取るべき対策とは"

article1_content = """
<p>「検索エンジンのSEO対策をしているのに、なぜかアクセスが落ちている」「AI検索が普及して、自分のサイトがどう評価されるのかわからない」——そんな悩みを抱えているWebマーケター・サイト運営者は、今や少なくないはずです。2026年5月、Googleは開発者向けカンファレンス「Google I/O 2026」で、検索体験を根本から変える一連のアップデートを発表しました。この発表は、SEOの世界に新たなパラダイムシフトをもたらすものとして、デジタルマーケティング業界で大きな波紋を呼んでいます。</p>

<h2>Google I/O 2026が示したAI検索の新時代</h2>

<p>Googleは今回のI/Oで、検索バー（Search Box）を「過去25年で最大規模の刷新」として「AI搭載の新しい検索ボックス」を発表しました。これまでのキーワード補完を超え、ユーザーが入力した内容に対してAIが動的に拡張し、画像・ファイルなどのマルチモーダル入力にも対応します。検索結果もリスト形式の「10本の青いリンク」から、AIが生成するサマリーと会話型UIへと大きく変化します。</p>

<p>中心となるのは「AI Mode」の全面展開です。I/O 2026の時点でAI Modeは月間10億ユーザーを突破しており、クエリ数は四半期ごとに2倍以上のペースで増加しています。これは、ChatGPTが1週間あたり10億クエリ以上を処理している事実と合わせて考えると、AI検索が一部の先進ユーザーだけのものではなく、一般的なWeb利用の中核になりつつあることを示しています。</p>

<p>さらに重要なのは、GoogleがAI Modeを新興国を含む約200カ国・98言語に順次展開し、無料で提供すると発表したことです。これにより日本語ユーザーにとってもAI検索はより身近なものとなります。</p>

<h2>Gemini 3.5 Flash導入と「情報エージェント」の登場</h2>

<h3>AIモデルのアップグレード</h3>

<p>Google I/O 2026では、AI ModeのデフォルトモデルがGemini 3.5 Flashに更新されることが発表されました。Gemini 3.5 Flashは、大規模フラッグシップモデルに匹敵する知性をFlashシリーズ特有の高速処理で実現するとされています。これにより、AI Overviewsの回答品質がさらに向上し、より複雑な多段階クエリにも対応できるようになります。また、GmailやGoogle Photosなどとの連携（パーソナライゼーション機能）も拡充され、ユーザーの個人情報を踏まえたより精度の高い回答が可能になります。</p>

<h3>情報エージェント（Information Agents）とは</h3>

<p>今回の発表で特に注目されたのが「情報エージェント」の概念です。これはユーザーが明示的に検索しなくても、バックグラウンドで常時Webを監視し、ユーザーの関心事に関連する新情報を自動的に収集・要約して通知するAIエージェントです。たとえば「希望条件に合う賃貸物件が新たに掲載されたら通知する」「特定の競合他社の動向を追跡する」といった使い方が可能になります。</p>

<p>情報エージェントは当初Google AI ProおよびUltraサブスクライバー向けに2026年夏ごろ提供開始の予定ですが、これはWebコンテンツのあり方を大きく変える可能性があります。ユーザーが「検索する」という行為そのものを行わなくても情報にたどり着けるとすれば、従来の「検索→クリック→サイト閲覧」というトラフィック獲得の前提が根底から崩れることになります。コンテンツを「見つけてもらう」だけでなく、「継続的に参照され続ける」存在になることが、これからのサイト運営者に求められます。</p>

<h2>SEOへの深刻な影響——クリック率はどう変わったか</h2>

<h3>ゼロクリック検索の急増</h3>

<p>Google I/O 2026前後のデータを見ると、SEOへの影響は既に数字に表れています。SparkToro・Datosのデータによれば、米国でのGoogleゼロクリック検索の割合は58.5%に達しています。つまり、Googleで検索した人の半数以上が、何もクリックせずに検索結果ページから離脱しているのです。Conductor社の分析では、2026年第1四半期の時点でGoogleの全クエリの25.11%にAI Overviewが表示されており、この数字は今後さらに増加が見込まれます。</p>

<p>さらに深刻なのが、AI Overviewsが表示されたクエリにおける1位サイトのクリック率の低下です。SISTRIX社のデータ（2026年3月）によれば、AI機能が表示される検索においてオーガニック1位のクリック率は従来の27%から約11%にまで低下しています。AI Overviewが表示されると、オーガニック1位サイトは約18%のクリックを失うというデータもあります。</p>

<h3>AI引用の商業価値——引用されることの方が価値が高い時代へ</h3>

<p>一方で、「AI Overviewsの中で引用・言及されたブランド」は、引用されていない競合と比較してオーガニッククリックが35%、有料広告クリックが91%多くなるというデータも存在します。つまり、検索結果の1位を取ることよりも、AI回答の中に言及されることの方が商業的価値が高い状況が生まれつつあるのです。Googleは意図的にSEOとAEO/GEOの間に壁を設けようとしているわけではありませんが、結果としてAI引用の有無が新たな競争軸になっています。</p>

<h2>SEO担当者・Webマーケターが今すぐ取るべき対策</h2>

<p>GoogleはI/O 2026に合わせて、生成AI機能向けのコンテンツ最適化ガイドを公式に公開しました（Google Search Central Blog、2026年5月）。このガイドが示すのは「AEO（Answer Engine Optimization）やGEO（Generative Engine Optimization）はSEOの延長線上にある」という明確なメッセージです。以下に具体的な対策を整理します。</p>

<p><strong>1. 独自性のある一次情報コンテンツを作る：</strong> AIが自分で生成できるような汎用情報は引用価値がありません。オリジナル調査・専門家の見解・独自事例など、AIが持っていない情報を提供することが引用される条件となります。AIコンテンツ生成ツールで量産した記事は評価されにくくなっています。</p>

<p><strong>2. 構造化データの実装を徹底する：</strong> FAQPage・HowTo・Article・Organizationなどのschema.orgマークアップを実装することで、AIが情報を抽出しやすくなります。FAQPage構造化データだけでAI引用率が平均30%向上するというデータもあります。</p>

<p><strong>3. AIクローラーのアクセスを許可する：</strong> OAI-SearchBot（OpenAI）、PerplexityBot、Google-Extended（Gemini）、ClaudeBot（Anthropic）などのAIクローラーをrobots.txtでブロックしていないか確認することが重要です。意図せずブロックしている場合は即座に解除しましょう。</p>

<p><strong>4. コンテンツの鮮度を維持する：</strong> AIには強い「新鮮さへの偏重（recency bias）」があり、3ヶ月以上更新されていないコンテンツへの引用は急落する傾向があります。重要ページは四半期ごとに更新・加筆することを検討してください。</p>

<p><strong>5. E-E-A-Tを強化する：</strong> 著者情報の明示・専門性を証明する資格・実績の記載・外部サイトからの言及（デジタルPR）など、AIがコンテンツの信頼性を評価できる要素を充実させることも欠かせません。</p>

<h2>まとめ：検索の「次の形」に備えるために</h2>

<p>Google I/O 2026は、「AIがすべての検索を書き換える」という宣言に等しい発表でした。AI Modeの月間10億ユーザー突破・Gemini 3.5 Flash導入・情報エージェントの登場——これらは単なる機能アップデートではなく、Webのトラフィック構造そのものを変えるイベントです。SEO担当者・サイト運営者は今すぐ、「検索順位を上げる」から「AIに引用される」という視点へのシフトを始めるべきタイミングに来ています。まずは自分のサイトのAIクローラーアクセス設定と構造化データの実装状況を確認することから始めてみてください。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://blog.google/products-and-platforms/products/search/search-io-2026/" target="_blank" rel="noopener">Google Search's I/O 2026 updates: AI agents and more（Google Blog、2026年5月）</a></li>
  <li><a href="https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing" target="_blank" rel="noopener">A new resource for optimizing for generative AI in Google Search（Google Search Central Blog、2026年5月）</a></li>
  <li><a href="https://www.searchenginejournal.com/seo-pulse-google-launches-core-update-amid-i-o-ai-search-overhaul/575676/" target="_blank" rel="noopener">Google Launches Core Update Amid I/O AI Search Overhaul（Search Engine Journal、2026年5月）</a></li>
  <li><a href="https://time.com/article/2026/05/20/google-search-ai-internet/" target="_blank" rel="noopener">Google Shifts to AI Search, Heralding Major Change in How People Use the Internet（TIME、2026年5月20日）</a></li>
  <li><a href="https://www.theslidefactory.com/post/google-ai-mode-seo-2026-what-changed-what-it-costs-you-and-how-to-adapt" target="_blank" rel="noopener">Google AI Mode SEO Impact 2026: What Changed & What to Do（The Slide Factory、2026年）</a></li>
</ul>
"""

# ============================================================
# 記事2: GEO実践戦略（海外情報ベース）
# ============================================================
article2_title = "Claude・Gemini・ChatGPTで「引用される」ための実践GEO戦略2026——各AIプラットフォームの引用傾向の違いと最適化手法を徹底解説"

article2_content = """
<p>「ChatGPTでは自社が言及されるのに、Geminiには全く出てこない」「パープレキシティのAI回答で競合が引用されているが、自分のサイトは一度も出ない」——こうした悩みを抱えるマーケターが急増しています。実は、ChatGPT・Gemini・Claude・Perplexityなど各AIプラットフォームは、コンテンツを引用・参照する際の基準が大きく異なります。2026年現在、GEO（Generative Engine Optimization：生成エンジン最適化）は「全AIにまとめて最適化する」という時代から「プラットフォームごとに戦略を変える」時代へと進化しています。本記事では、各AIの引用傾向の違いと、それぞれに対応した実践戦略を解説します。</p>

<h2>GEOとは何か——「検索結果の上位」から「AI回答の中」へ</h2>

<p>GEO（Generative Engine Optimization）とは、ChatGPT・Google AI Overviews・Perplexity・Claude・Copilotなどのようなai検索プラットフォームが回答を生成する際に、自社のコンテンツを引用・言及・推薦させるための最適化活動です。従来のSEOが「検索結果の10本のリンクの中に入る」ことを目指すものだとすれば、GEOは「AIが生成する回答そのものの中に名前が出る」ことを目指すものです。</p>

<p>2026年の現状を数字で見ると、ChatGPTは週あたり10億クエリ以上を処理し、Google AI Overviewsはすべての検索クエリの47%以上に表示されており、Perplexityの月間アクティブユーザーは1億5000万人を超えています。さらに、調査会社Brandlightによれば、GoogleのトップページリンクとAI引用ソースの重複は、かつての70%から現在は20%以下にまで低下しています。SEOで上位を取っていても、AI回答に出てくるとは限らないのです。</p>

<p>また、2026年第1四半期のデータでは、AI検索からのトラフィックが全オーガニック検索流入の5〜10%を占めるようになっており、年末までに20%に達するとも予測されています。特にB2Bテック分野では、AI Overviewsの表示率が36%から82%へと1年で急増しており、業種によってはAI検索対策が最優先事項になっています。</p>

<h2>各AIプラットフォームの引用傾向の違い</h2>

<h3>Claude（Anthropic）の引用パターン</h3>

<p>Machine Relations研究機関が1720万件以上の引用データを分析した結果、Claudeには独自の引用パターンがあることが明らかになっています。Claudeは、The New York Times・The Atlantic・The New Yorker・The Economistといった質の高い論説・ジャーナリズムコンテンツを好む傾向があります。また、ジャーナリズム記事の引用のうち過去12ヶ月以内のものは36%にとどまり（ChatGPTの56%と比較して低い）、より古い権威あるコンテンツも引用します。さらに、他のモデルと比べてユーザー生成コンテンツ（レビュー・ソーシャルメディア）を2〜4倍の比率で引用する特徴もあります。</p>

<p>Claudeで引用されるには、長期的な権威の積み上げと、専門家視点からの深い論説コンテンツが効果的です。短期の流行ニュースよりも、時代を超えて参照価値のある「エバーグリーン」なコンテンツが優位です。</p>

<h3>Gemini（Google）の引用パターン</h3>

<p>Geminiはすべてのセクターで最も「一次情報源（First-party）」を好む傾向が強く、その比率は分野によって22.4%〜54.0%に達します。これはGoogleの検索エンジンとの統合に基づくものと考えられており、公式ウェブサイト・政府機関・企業の公式ページなどの信頼できる一次情報源が優遇されます。Geminiで引用されたいなら、まず自社の公式ページのコンテンツ充実が最優先事項となります。Google検索での評価（SEO）とGeminiでの引用には高い相関関係があり、従来のSEO施策がそのままGemini対策につながります。</p>

<h3>ChatGPT（OpenAI）の引用パターン</h3>

<p>ChatGPTは最も新鮮なコンテンツを重視しており、引用ジャーナリズムコンテンツの56%が過去12ヶ月以内のものです。ニュースサイト・業界メディア・専門的なブログなど、定期的に更新される情報源から多く引用します。また、URLのアクセシビリティ（クローラーが到達できるか）・検索順位・「ファンアウトランク」（どれだけ多くのページから参照されているか）が引用される上位の要因とされています。コンテンツを3ヶ月以内に更新し、OAI-SearchBotのクローリングを許可することが基本施策です。</p>

<h3>Perplexity の引用パターン</h3>

<p>Perplexityは最も鮮度重視で、引用ソースの多くが直近数日以内のコンテンツです。ニュースサイト・プレスリリース・専門メディアの速報など、リアルタイム性の高い情報が重用されます。Perplexityへの露出を狙うなら、PRニュースリリースの配信や業界ニュースサイトへのコンテンツ提供が有効な手段となります。また、PerplexityBotのクローリング許可と、メタデータの正確な記述が引用率向上に寄与します。</p>

<h2>GEO最適化の実践戦略</h2>

<h3>1. 技術的基盤の整備——AIクローラーのアクセス確保</h3>

<p>どのAIプラットフォームに対しても共通して必要なのが、AIクローラーへのアクセス許可です。robots.txtで以下のボットをブロックしていないかを確認してください。OAI-SearchBot・ChatGPT-User（OpenAI系）、PerplexityBot（Perplexity）、Google-Extended（Gemini）、ClaudeBot（Anthropic）、Applebot-Extended（Apple）。これらをブロックしていると、いくらコンテンツが優れていてもAIに認識されません。また、コンテンツはJavaScriptで動的に生成されるのではなく、HTMLのソースコードに直接含まれている必要があります。SPAやReactアプリケーションを利用している場合は、サーバーサイドレンダリング（SSR）の導入を検討してください。</p>

<h3>2. コンテンツ品質の強化——AIが引用したくなるコンテンツとは</h3>

<p>「AI生成コンテンツはAI検索でパフォーマンスが悪い」というのは業界の共通見解となっています。LLMは自分が持っていない新しい情報を求めており、AIが自分で生成できるような汎用的な内容は引用価値がありません。引用されるために必要なコンテンツ要件は以下の通りです。</p>

<p>・独自調査・アンケートデータ・実測値などのオリジナルデータ<br>
・専門家インタビューや一次取材に基づいた独自視点<br>
・明確な事実主張と引用可能なステートメント（LLMがそのまま抜き出せる一文）<br>
・比較表・FAQ・定義など、構造化された情報<br>
・3ヶ月以内の情報更新（特にChatGPT・Perplexity向け）</p>

<h3>3. 構造化データと技術的最適化</h3>

<p>schema.orgによる構造化マークアップは、GEO施策の中で最も即効性のある施策の一つです。FAQPageスキーマの実装だけでAI引用率が平均30%向上するというデータがあります。Article・Organization・BreadcrumbList・Personスキーマも合わせて実装することで、AIがコンテンツの文脈・著者・組織を正確に理解しやすくなります。また、見出し構造（h1〜h3）・箇条書き・比較表などを使い、AIが特定のセクションを独立して引用できる構造にすることも重要です。</p>

<h3>4. 認知度の拡大——デジタルPRとエンティティ最適化</h3>

<p>AIは「多くのソースで言及されているブランド・概念・人物」を重要なエンティティとして認識します。自社ブランドや専門家個人が業界メディア・WikiData・Wikipediaなどに言及・登録されているかを確認し、デジタルPR活動を通じて多様なドメインからの言及を獲得することが長期的なAI可視性向上につながります。特にGEO最適化においては、リンクの数よりも「信頼できる多様なソースからの言及」の方が重要です。</p>

<h3>5. AI可視性の測定——新しいKPIの設定</h3>

<p>2026年のコンテンツ戦略では「GoogleのクリックとLLM引用は同じ四半期に逆の動きをすることがある」という現実を受け入れる必要があります。AI引用状況を定期的にモニタリングするために、ChatGPT・Perplexity・Gemini・Claudeで自社ブランド・製品・キーワードを定期検索し、引用されているかを確認することが求められます。Profound・TrackrなどのAI引用モニタリングツールの活用も選択肢の一つです。</p>

<h2>まとめ：プラットフォームごとの最適化がGEO成功の鍵</h2>

<p>2026年のGEO対策は、「どのAIプラットフォームで引用されたいか」によって戦略が変わります。Claudeには権威ある深い論説コンテンツ、Geminiには公式一次情報の充実、ChatGPTには定期更新される高品質ニュース・分析記事、Perplexityにはリアルタイム性の高いPR配信が効果的です。まずは自社サイトのAIクローラーアクセス設定を見直し、FAQPage構造化データを実装することから始めましょう。それだけでも引用される確率は大きく変わります。全プラットフォームに共通するのは「AIが自分で生成できない独自情報」を提供することです。そこからすべての対策が始まります。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://machinerelations.ai/research/ai-citation-behavior-across-models-2026" target="_blank" rel="noopener">AI Citation Behavior Across Models: Why One AI Visibility Strategy Fails Across Gemini, Claude, Perplexity, and SearchGPT（Machine Relations Research、2026年）</a></li>
  <li><a href="https://searchengineland.com/mastering-generative-engine-optimization-in-2026-full-guide-469142" target="_blank" rel="noopener">Mastering generative engine optimization in 2026: Full guide（Search Engine Land、2026年）</a></li>
  <li><a href="https://llmrefs.com/generative-engine-optimization" target="_blank" rel="noopener">Generative Engine Optimization (GEO): The 2026 Guide to AI Search Visibility（LLMrefs、2026年）</a></li>
  <li><a href="https://www.prnewswire.com/news-releases/5w-releases-ai-platform-citation-source-index-2026-the-50-websites-that-now-decide-what-brands-are-visible-inside-chatgpt-claude-perplexity-gemini-and-google-ai-overviews-302759804.html" target="_blank" rel="noopener">5W Releases AI Platform Citation Source Index 2026（PR Newswire、2026年）</a></li>
  <li><a href="https://www.yext.com/research/ai-citation-refresh-january-2026" target="_blank" rel="noopener">AI Citation Behavior Across Models: Evidence from 17.2 Million Citations（Yext Research、2026年1月）</a></li>
</ul>
"""

# ============================================================
# 記事3: 日本のAIO/LLMO対策（日本語ソースベース）
# ============================================================
article3_title = "日本企業のAIO/LLMO対策最前線2026——AI引用率420%向上事例に学ぶ構造化データ活用と実装ガイド"

article3_content = """
<p>「AI検索でライバル企業が引用されているのを見かけるが、自社はまったく出てこない」「AIO対策をしなければと思っているが、何から始めればいいかわからない」——こうした声が、日本のWebマーケター・SEO担当者から多く聞かれるようになっています。2026年5月時点でGoogleの全検索クエリの48%以上にAI Overviewが表示されており、AI検索最適化（AIO/LLMO）はもはや先進的な取り組みではなく、競争力を維持するための必須対策になっています。本記事では、日本企業の事例や国内支援企業の取り組みを交えながら、AIO/LLMO対策の実践的な実装ガイドをお届けします。</p>

<h2>日本でのAIO/LLMO対策の現状——市場はどこまで進んでいるか</h2>

<p>AIO（AI Overview最適化）・LLMO（Large Language Model Optimization：大規模言語モデル最適化）は、ChatGPT・Perplexity・Gemini・ClaudeといったAI検索エンジンに「引用される」「回答の情報源として選ばれる」ためのコンテンツ最適化施策です。従来のSEOが「検索順位を上げること」を目的とするのに対し、AIO/LLMOは「AIが回答を生成する際に自社コンテンツを参照させること」を目指します。</p>

<p>日本市場では2025年後半から急速に認知が高まり、2026年には専門的な支援サービスを提供する企業が数十社に上っています。その背景には、ゼロクリック検索の急増があります。AI Overviewが表示されたクエリでは、検索結果1位のサイトのクリック率が最大58%低下するというデータがあり、従来のSEO施策だけでは流入を守れなくなっています。</p>

<p>また、Webマーケティング業界では「SEOとAIO対策はどちらを優先すべきか」という議論が起きていますが、これは二項対立ではありません。AIOはSEOを土台とした発展形であり、SEO施策の上にAI引用を意識した構造化データ・著者情報明示・エンティティ最適化を加えることがAIO対策の基本です。両立が前提です。</p>

<h2>日本企業の具体的な取り組みと成果</h2>

<h3>株式会社メディアリーチ——AI引用率420%向上の事例</h3>

<p>国内のAIO/LLMO対策支援において注目される実績の一つが、株式会社メディアリーチの顧客事例です。同社はChatGPT・Perplexity・AI Overviewでの引用獲得やAIブランド推薦を見据えた戦略設計・診断・改善支援に対応しており、AI引用率420%向上という具体的な数値を公表しています。この実績は、適切な施策を実施すれば短期間で大きな成果を出せることを示しており、業界から注目を集めています。同社の支援では、まずAI引用状況の診断を行い、引用されるための障壁を特定した上で、構造化データ実装・コンテンツ改善・デジタルPRを組み合わせたアプローチを取っています。</p>

<h3>株式会社Faber Company「ミエルカGEO」</h3>

<p>SEOツール「ミエルカ」で知られる株式会社Faber Companyは、2025年に生成AI時代の検索最適化に特化したサービス「ミエルカGEO」を開始しました。AI検索での自社コンテンツの引用状況を可視化するツールと、コンサルタントによる施策提案を組み合わせた「ツール×コンサル統合型」のサービス形態が特徴です。データに基づいて現状を把握し、継続的に改善するPDCAサイクルを回すことができます。特に、どのコンテンツが・どのAIプラットフォームで・どのキーワードで引用されているかを可視化する機能は、施策の優先順位付けに役立ちます。</p>

<h3>株式会社CINC——GEO/LLMO/AIOコンサルティング</h3>

<p>SEO分析ツール「Keywordmap」を提供する株式会社CINCは、AI検索最適化（GEO/LLMO/AIO/AEO）コンサルティングサービスを展開しています。独自のデータ分析基盤を活かし、どのキーワード・コンテンツがAI検索で引用されているかを可視化した上で、具体的な改善施策を提案する体制を整えています。大企業からスタートアップまで幅広いクライアントを支援しており、B2B・B2Cいずれの業態にも対応しています。</p>

<h2>AIO/LLMO対策の具体的な実装手順</h2>

<h3>Step 1：現状診断——AIクローラーのアクセス状況を確認する</h3>

<p>最初に行うべきは、自社サイトがAIクローラーにアクセスされているかの確認です。robots.txtを確認し、OAI-SearchBot（OpenAI）・PerplexityBot（Perplexity）・Google-Extended（Gemini）・ClaudeBot（Anthropic）などのAI系クローラーをブロックしていないかを確認します。また、サイト内のコンテンツがJavaScriptではなく生のHTMLに含まれているかも重要です。コンテンツがJavaScriptで動的に生成されている場合、AIクローラーが読み取れない可能性があります。</p>

<p>次に、主要なAIプラットフォーム（ChatGPT・Perplexity・Gemini）で自社ブランド名や主要キーワードを検索し、現在どの程度引用されているかを把握します。競合他社が引用されているかも確認し、自社との差分を把握することで、どこに注力すべきかが明確になります。</p>

<h3>Step 2：構造化データの実装——FAQPageから始める</h3>

<p>AIO/LLMO対策において、最も即効性が高い施策が構造化データ（schema.org）の実装です。特にFAQPageスキーマは、実装するだけでAIへの引用率が平均30%向上するという実績データがあります。</p>

<p>実装すべき主要なスキーマは以下の通りです。</p>

<p>・<strong>FAQPage</strong>：よくある質問とその回答をAIが直接抽出できる形式で提供<br>
・<strong>Article</strong>：記事の著者・公開日・更新日・見出しなどを明示<br>
・<strong>Organization</strong>：企業の基本情報・連絡先・創業年などを明確化<br>
・<strong>Person</strong>：著者・専門家の経歴・資格・専門分野を明示<br>
・<strong>BreadcrumbList</strong>：サイト構造をAIに理解させる</p>

<p>WordPressを使用しているサイトであれば、Yoast SEOやRank Math などのプラグインを使って構造化データを簡単に実装できます。また、Google Search Consoleのリッチリザルトテストツールで実装後の検証も忘れずに行いましょう。</p>

<h3>Step 3：E-E-A-T強化——AIが信頼できると判断するコンテンツ要素</h3>

<p>E-E-A-T（Experience・Expertise・Authoritativeness・Trustworthiness）はSEOの概念ですが、AIO/LLMO対策においても同様に重要です。AIは「誰が書いたか」「その人はどの程度信頼できるか」を評価します。具体的な強化方法としては、著者プロフィールページの充実（資格・実績・経験年数の記載）、記事への著者名の明示とschema.orgのPersonスキーマでの紐付け、外部メディアへの寄稿や言及の獲得（デジタルPR）、そして情報の更新日を明示することが挙げられます。</p>

<h3>Step 4：コンテンツ構造の最適化——AIが引用しやすい文章の書き方</h3>

<p>AI回答に引用されやすいコンテンツには共通する構造的特徴があります。まず、記事の冒頭部分で「何について書いているか」「結論は何か」を明確に述べる「直接回答型の冒頭」が重要です。AIはページの最初の部分を重視して引用する傾向があります。</p>

<p>また、h2・h3見出しを使って情報を整理し、AIが特定のセクションを独立して引用できる構造にすることも効果的です。箇条書きや比較表を活用して情報を視覚的に整理することで、LLMが情報を抽出しやすくなります。さらに、「〇〇とは△△のことです」「〇〇の主な特徴は××です」のように、エンティティと属性の関係を明確に述べる文章を意識することで、AIが引用しやすいステートメントを提供できます。</p>

<h3>Step 5：llms.txtの導入——AI向けサイトマップ</h3>

<p>2025年から注目されている施策が「llms.txt」です。これは、AIクローラーに対して「このサイトで最も重要なページはここです」「このコンテンツはAIに利用してください」といった情報を伝えるためのファイルです。robots.txtと同様にサイトのルートディレクトリに設置し、AIクローラーへのナビゲーション情報を提供します。llms.txtを実装することで、AIが自社の最重要コンテンツを確実に把握できるようになり、引用される確率が高まります。特に、コンテンツが多いサイトでは、AIに優先して読んでほしいページを明示することが重要です。</p>

<h2>AIO/LLMO対策の効果測定——何を見るべきか</h2>

<p>AIO/LLMO対策では、従来のSEO指標（検索順位・オーガニッククリック数）だけでは成果を測れません。AI検索での可視性を測るためには、ChatGPT・Perplexity・Gemini・Claudeなどで特定のキーワードを検索した際に自社が引用されているかを定期的に確認する「AIブランドモニタリング」が必要です。</p>

<p>国内では「ミエルカGEO」のほか、海外ツールでは「Profound」「Trackr」などのAI引用モニタリングツールが登場しています。2026年のコンテンツ戦略では、「GoogleのクリックとLLM引用は同じ四半期に逆の動きをすることがある」という新しい現実を受け入れ、両方の指標を並行して追跡することが求められます。効果測定の指標としては、①AI引用率（特定クエリでの引用回数）②ブランドメンション数（AI回答中での言及数）③AI経由のリファラートラフィック——の3つを最低限把握することを推奨します。</p>

<h2>まとめ：まず「FAQPage構造化データ」と「AIクローラー許可」から始めよう</h2>

<p>日本でのAIO/LLMO対策は着実に成熟しつつあり、AI引用率420%向上のような具体的な成果事例も生まれています。しかし多くの企業はまだ対策を始めていないか、始めたばかりの段階です。今すぐ始められることは、robots.txtでAIクローラーをブロックしていないかの確認と、FAQPage構造化データの実装です。この2つだけでも、AI検索での引用可能性は大きく変わります。競合他社がAI引用を獲得し始める前に、自社の施策を一歩先に進めましょう。AIに「選ばれる」コンテンツを作ることが、2026年以降のWebマーケティングの中心課題です。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://uravation.com/media/aio-llmo-technical-implementation-30-2026/" target="_blank" rel="noopener">【2026年最新】AIO/LLMO対策テクニカル30選｜AI検索流入を取りに行く実装ガイド（株式会社Uravation、2026年）</a></li>
  <li><a href="https://uravation.com/media/aio-ai-search-seo-guide/" target="_blank" rel="noopener">【2026年4月最新】AIO対策とは？AI検索時代のSEO完全ガイド（株式会社Uravation、2026年4月）</a></li>
  <li><a href="https://flagout.co.jp/aio-seo-btob-guide/" target="_blank" rel="noopener">【2026年最新】BtoB企業のAIO対策完全ガイド｜生成AI検索で引用されるための10要件（株式会社フラグアウト、2026年）</a></li>
  <li><a href="https://www.cinc-j.co.jp/service/analytics/geoconsulting" target="_blank" rel="noopener">AI検索最適化（GEO/LLMO/AIO/AEO）コンサルティングサービス（株式会社CINC、2026年）</a></li>
  <li><a href="https://webtan.impress.co.jp/e/2026/03/09/52139" target="_blank" rel="noopener">2026年、今までのSEOは通用するのか？「AIO（AI最適化）」の最前線（Web担当者Forum、2026年3月9日）</a></li>
</ul>
"""

articles = [
    {"title": article1_title, "content": article1_content},
    {"title": article2_title, "content": article2_content},
    {"title": article3_title, "content": article3_content},
]

for i, article in enumerate(articles, 1):
    print(f"\n--- 記事{i}を投稿中 ---")
    print(f"タイトル: {article['title'][:60]}...")
    payload = {
        "title": article["title"],
        "content": article["content"],
        "status": "draft",
    }
    try:
        resp = requests.post(WP_URL, headers=headers, json=payload, timeout=30)
        if resp.status_code in (200, 201):
            data = resp.json()
            print(f"✓ 投稿成功！ 投稿ID: {data.get('id')}  ステータス: {data.get('status')}")
            print(f"  管理画面: https://aiotaisaku.com/wp-admin/post.php?post={data.get('id')}&action=edit")
        else:
            print(f"✗ 投稿失敗 HTTPステータス: {resp.status_code}")
            print(f"  レスポンス: {resp.text[:300]}")
    except Exception as e:
        print(f"✗ エラー: {e}")

print("\n=== 全記事の投稿処理が完了しました ===")
