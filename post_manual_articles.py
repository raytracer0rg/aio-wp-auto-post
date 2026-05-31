#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3記事を手動で生成してWordPressに下書き投稿するスクリプト
"""
import base64
import re
import sys
import os
import requests

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WP_URL = "https://aiotaisaku.com"
WP_USERNAME = "kr_aiota_20250512"
WP_APP_PASSWORD = "fQe7 0nkE rXbm 8gCL BObs qRbs"

_EDIT_HINT_TPL = (
    '<!-- wp:quote {{"className":"edit-hint-block"}} -->\n'
    '<blockquote class="wp-block-quote edit-hint-block">\n'
    '<p>✏️ <strong>EDIT HINT</strong>：{hint}</p>\n'
    '<cite>※このブロックは編集後に削除してください</cite>\n'
    '</blockquote>\n'
    '<!-- /wp:quote -->'
)

_IMAGE_HINT_TPL = (
    '<!-- wp:quote {{"className":"image-hint-block"}} -->\n'
    '<blockquote class="wp-block-quote image-hint-block">\n'
    '<p>🖼️ <strong>IMAGE HINT</strong>：{hint}</p>\n'
    '<cite>※Canva等で作成して画像ブロックに差し替え、このブロックは削除してください</cite>\n'
    '</blockquote>\n'
    '<!-- /wp:quote -->'
)


def eh(hint: str) -> str:
    return _EDIT_HINT_TPL.format(hint=hint)


def ih(hint: str) -> str:
    return _IMAGE_HINT_TPL.format(hint=hint)


def post_draft(title: str, content: str) -> dict:
    edit_count = len(re.findall(r'<!-- wp:quote \{"className":"edit-hint-block"\}', content))
    image_count = len(re.findall(r'<!-- wp:quote \{"className":"image-hint-block"\}', content))
    print(f"\n{'=' * 60}")
    print(f"タイトル: {title}")
    print(f"EDIT HINT: {edit_count}  IMAGE HINT: {image_count}")

    token = base64.b64encode(f"{WP_USERNAME}:{WP_APP_PASSWORD}".encode()).decode()
    resp = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts",
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
        },
        json={"title": title, "content": content, "status": "draft"},
        timeout=30,
    )
    resp.raise_for_status()
    result = resp.json()
    print(f"[投稿成功] ID={result.get('id')}  URL={result.get('link')}")
    return result


# ==============================================================
# 記事1: Google I/O 2026「Search Agent」時代のAIO戦略
# ==============================================================
TITLE_1 = "Google I/O 2026「Search Agent」時代の幕開け——Gemini 3.5 Flash搭載AI Modeが月間10億ユーザー突破、AIO戦略はどう変わるか"

CONTENT_1 = f"""
<p>2026年5月19日に開催されたGoogle I/Oは、AI検索の歴史において過去最大級の変革を宣言するイベントとなった。AI Modeはローンチから約1年で月間10億ユーザーを突破し、クエリ数は四半期ごとに倍増を続けている。新デフォルトモデル「Gemini 3.5 Flash」の採用にとどまらず、AIが能動的にウェブを巡回してユーザーに情報を届ける「Search Agent（情報エージェント）」という全く新しい概念が実装段階に入った。これは「ユーザーが検索した時だけ引用を争う」という従来のAIO戦略の前提を根底から問い直すものだ。AI Modeのクエリは従来の検索クエリの3倍の長さになり、マルチモーダルクエリ（音声・画像・動画）が全クエリの16%以上を占める今、AIO専門家が取るべき戦略はどう変わるのか。本稿でその全容を解説する。</p>

{ih("Google I/O 2026の主要発表3点を視覚的に整理した比較表。Gemini 3.5 Flash採用・Search Agent・Personal Intelligence無料化を縦軸に、変更内容・AIOへの影響・実装推奨度を横軸に配置した3×3マトリクス")}

<h2>AI Modeの現在地：月間10億ユーザーと急成長の数字が示す構造変化</h2>

<p>まずGoogle I/O 2026が提示したデータを整理する。AI Modeの月間ユーザー数は10億人を突破し、クエリ数は四半期ごとに2倍以上のペースで増加している。クエリの長さは従来の検索クエリの3倍、マルチモーダルクエリの割合は全体の16%超。この数字は「AI検索がニッチな用途から汎用的な検索行動に主流化しつつある」ことを示している。</p>

<p>同時にAI Overviewsの表示率も急拡大した。2025年2月時点で全クエリの30%だったAI Overviews表示率は、2026年2月には48%に達し、わずか1年で58%増加した。現在200カ国・40言語でAI Overviewsが展開されている。AIO専門家にとってもはや「AI Overviewsが表示されないクエリを探す」という回避策は機能しない段階に入ったと認識すべきだ。</p>

<p>Semrushの調査では、2028年にはAI検索経由の訪問者数が従来の検索経由を上回ると予測されており、既に多くのビジネスでLLM検索からのトラフィックが総有機流入の5〜10%を占め始めている。さらに複数の調査でLLM経由のトラフィックは従来の検索経由と比べてコンバージョン率が5倍高いというデータも報告されており、流入数は少なくても質の高いユーザーを獲得できる経路として評価が高まっている。</p>

{eh("ここに自社サイトのGA4データを参照し、AI AssistantチャネルとOrganicチャネルのコンバージョン率比較データを追加する。「実際にAI経由の方が〇〇%高かった」という自社の数値があると信頼性が大幅に向上する")}

<h2>Gemini 3.5 Flash採用：AI Modeの「推論能力」が変えるコンテンツ評価軸</h2>

<p>Gemini 3.5 FlashがAI Modeのデフォルトモデルとなったことの意味は、単なるモデルアップグレード以上だ。Gemini 3.5 Flashの設計コンセプトは「エージェント・コーディング用途に最適化された持続的なフロンティアパフォーマンス」であり、複数ステップの推論と長文コンテキストの理解を強みとするモデルだ。</p>

<p>AIO観点での影響は具体的だ。従来のAI Overviewsは「この質問に最も直接的に答えるページ」を優先する傾向があったが、Gemini 3.5 Flashは「複数の情報源を統合して複雑な問いに包括的に答える」能力が格段に向上している。ユーザーがAI Modeに投げかけるクエリが3倍長くなっているという事実は、より複雑な意図・複合的な情報ニーズをAI Modeに求めていることを示す。</p>

<p>この変化に対応するために重要になったのが「セマンティック完全性（Semantic Completeness）」だ。AI Overviewsの引用要因を分析した複数の調査では、セマンティック完全性スコアが8.5/10以上のコンテンツはAI引用率が4.2倍高いというデータが報告されている。セマンティック完全性とは、単に答えを書くだけでなく「現象→原因→背景→具体例→影響→対策」という文脈の網羅度を指す。「答え」を書くだけでなく「なぜそうなるのか」「どういう状況で起きるのか」「実際にどう対処するか」まで説明するコンテンツが引用対象として選ばれやすくなっている。</p>

<p>また、マルチモーダルコンテンツの重要性も高まっている。テキスト・画像・動画を組み合わせたマルチモーダルコンテンツは、テキストのみのページと比べて156%高いAI Overview選択率が報告されている。音声クエリへの対応も含め、コンテンツの「多面的な表現」への投資が引用率向上に直結する時代になった。</p>

{ih("セマンティック完全性の6段階モデルを示すピラミッド図。下から「現象」「原因」「背景」「具体例」「影響」「対策」を積み上げ、上に行くほどAI引用率が高まる構造を矢印で示す。各段階に短い説明文を添える")}

<h2>Search Agent：「受動的引用」から「能動的選択」へのパラダイム転換</h2>

<p>Google I/O 2026で最も革新的な発表は「Search Agent（情報エージェント）」の概念だ。2026年夏からGoogle AI Pro・Ultraサブスクライバー向けに先行提供される情報エージェントは、ユーザーが設定したトピックについて24時間365日インターネットを自律的に巡回し、新しい情報が出たときにプッシュ通知する機能だ。エージェントはブログ・ニュースサイト・SNS投稿だけでなく、金融・ショッピング・スポーツのリアルタイムデータにもアクセスする。</p>

<p>この機能が普及したとき、AIOの競争構造はどう変わるか。これまでのAIO戦略は「ユーザーが検索した瞬間に引用される」という単発的なモデルだった。Search Agentが普及すると「エージェントが定期的に参照するソースリストに入り続ける」という継続的なモデルに移行する。一度エージェントの「信頼ソースリスト」に入ると、そのユーザーが関連トピックについて情報収集するたびに自動的に参照される可能性がある。</p>

<p>エージェントがソースを選ぶ際の判断基準として重要なのは3点だ。第一に**コンテンツの鮮度**：エージェントは新しい情報を優先するため、定期的にアップデートされているサイトが有利になる。3ヶ月以内のコンテンツはAI引用率が古いコンテンツの3倍という調査データがある。第二に**エンティティの明確性**：エージェントはトピック関連のエンティティを軸に情報源を選ぶため、自社がどのトピック・エンティティと強く関連付けられているかが重要だ。WikidataやOrganization schemaでエンティティを明確化することがエージェントの認識精度に影響する。第三に**構造化データの整備**：schema.orgのArticle・NewsArticle・FAQPageのマークアップは、エージェントがコンテンツの性質と鮮度を把握する重要なシグナルとなる。FAQPageのマークアップを実装したページはAI Overview選択率が平均30%改善するというデータもある。</p>

{eh("ここにSearch Agentへの対応として実際に自分が試した「定期更新スケジュール設定」「dateModified markup実装」の手順や結果を1〜2段落で補足する。実装後の計測結果（AI経由トラフィックの変化等）があれば具体性が格段に増す")}

<p>なお、Search AgentはRSS・サイトマップを活用して更新を検知するため、定期更新コンテンツには必ずdateModifiedのschema.orgマークアップを施し、XMLサイトマップへの更新反映を速やかに行う運用が重要になる。</p>

<h2>AI Overview引用格差の拡大：被引用サイトと非引用サイトの二極化データ</h2>

<p>Google I/O 2026前後でのAI Overview引用の二極化が鮮明になっている。被引用ページはオーガニッククリック35%増・ペイドクリック91%増という大きな恩恵を受ける一方、AI Overviewが表示されながら引用されなかった上位表示ページのCTRは平均34.5%低下する。一部のメディア・パブリッシャーでは20〜60%のトラフィック減少を報告している。</p>

<p>注目すべき逆転現象がある。AI Overview引用の47%がオーガニック検索5位以下のページから来ていることだ。つまり、SEO順位とAI引用は実質的に独立した変数であり、「SEO上位表示」とは別軸の最適化が必要だということを示している。2026年のAI Overview引用と相関が高い要因はセマンティック完全性（r=0.87）、E-E-A-Tシグナル（強いE-E-A-Tを持つページは順位に関わらず2.3倍の引用頻度）、コンテンツの鮮度（3ヶ月以内で3倍の引用率）、マルチモーダル統合（テキスト+画像+動画で156%高い選択率）だ。一方でドメインオーソリティ（DA）の相関係数はr=0.18にとどまり（2024年の0.23から低下）、従来のリンク構築を軸にした間接的なAIO最適化の効果は薄れている。</p>

{ih("AI Overview引用有無によるCTR変化を示す棒グラフ。左列：引用ありページ（+35% organic、+91% paid）、中央列：引用なしページ（-34.5% organic）、右列：AI Overview非表示クエリ（基準値100%）を比較表示")}

<h2>Personal Intelligence無料開放：パーソナライズ時代のコンテンツ設計</h2>

<p>Google I/O 2026でのもう一つの重要な発表は、Personal IntelligenceがGmail・Google Photos・Google Calendar・YouTubeと連携する形で約200カ国・98言語に無料で展開されたことだ。これはAI Pro/Ultraサブスクリプション不要でPersonal Intelligenceが利用可能になることを意味する。</p>

<p>Personal Intelligenceが変えるのは「検索文脈がパーソナル化される」という点だ。「来週のミーティングで紹介できるAIO対策の最新情報を教えて」という質問に対して、AIはGoogleカレンダーのミーティング情報・Gmailの過去のやり取り・ウェブ上の最新情報を統合して回答する。ユーザーの過去の行動・スケジュール・関心事が文脈に入り込む。</p>

<p>AIO戦略への影響は「状況依存型コンテンツの引用率向上」だ。「一般的なAIO解説」よりも「特定の状況（競合分析、予算策定、月次レポート作成など）に使える実践情報」が、パーソナライズされた検索文脈で引用されやすくなる。コンテンツの切り口を「よくある状況への対応策」として設計することで、Personal Intelligence環境でも引用対象になれる可能性が高まる。また、著者のExperience・Expertise（実際の経験・専門性）をページに明示することで、AIがパーソナライズされた文脈でそのコンテンツを「信頼できる実践情報」として位置付けやすくなる。</p>

<h2>実践：2026年5月以降に優先すべきAIO施策ロードマップ</h2>

<p>以上を踏まえ、AIO専門家が今すぐ取り組むべき施策を優先度順に整理する。</p>

<p><strong>最優先①：セマンティック完全性の強化</strong><br>
既存のコンテンツ、特にサイトの中核テーマに関するハブページを選定し、「現象→原因→背景→具体例→影響→対策」の6段階で深掘りを追加する。一段落一段落の情報密度を高め、回答だけでなく「なぜそうなのか」「どういう状況で当てはまるか」という文脈情報を充実させることがAI引用率向上の最短ルートだ。</p>

<p><strong>優先②：エージェント対応のための更新管理体制の構築</strong><br>
Search Agentが鮮度を重視する以上、重要なコンテンツには定期更新スケジュールを設定する。dateModifiedのschema.orgマークアップを全ページに実装し、XMLサイトマップへの更新反映を速やかに行う運用体制を整える。更新ログをFAQPage構造化データに組み込み「最新のQ&Aを提供するサイト」として認識させることも有効だ。</p>

<p><strong>優先③：GA4 AI Assistantチャネルの即時活用</strong><br>
2026年5月13日からGA4に追加された「AI Assistantチャネル」で、AI検索からの流入を専用セグメントで計測する。どのページがAI経由トラフィックを獲得しているかを分析し、そのコンテンツパターン（構造・深度・フォーマット）を他ページに横展開する戦略が効率的だ。</p>

<p><strong>中期④：エンティティ管理の強化</strong><br>
Search AgentとPersonal Intelligenceが連携する環境では、Googleが自社ブランド・著者をどのエンティティとして認識しているかが継続的な引用の可否を左右する。Wikipedia・Wikidata・Organization/Person schemaでエンティティの明確化を行い、メンション獲得のためのデジタルPR施策を組み合わせることで、エージェントの「信頼ソースリスト」への定着を図る。</p>

<p><strong>中期⑤：マルチモーダル対応の整備</strong><br>
全クエリの16%超がマルチモーダルになっている現状では、テキストだけでなく、画像のalt属性と構造化キャプション、動画のトランスクリプトとVideoObject schema、音声検索に対応した自然言語構造の整備が引用率向上につながる。特に複雑な概念の説明には、テキストと図解の組み合わせが効果的だ。</p>

{eh("ここに上記5つのロードマップのうち、自社で実際に取り組んでいる優先順位や、実際にやってみて効果が出た施策・出なかった施策の実体験を追加すると、読者に刺さる内容になる。特に「GA4 AI Assistantチャネルで計測したら思ったより〇〇だった」という実感が貴重")}

<h2>まとめ</h2>

<p>Google I/O 2026は「AI検索における競争のルールが変わった」ことを明確に告げるイベントだった。Gemini 3.5 Flash・Search Agent・Personal Intelligenceの三重の変化により、AIO戦略は「一時的なクエリへの引用獲得」から「エージェントに継続的に選ばれる権威コンテンツとしての確立」へとシフトする。2026年夏のSearch Agent正式展開が迫る今、セマンティック完全性・エンティティ管理・コンテンツ更新管理の三つを軸にしたAIO基盤の構築を急ぎたい。AI引用の二極化が加速する中、今が取り組みのタイミングとして最も重要だ。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://blog.google/products-and-platforms/products/search/search-io-2026/" target="_blank" rel="noopener">Google Search's I/O 2026 updates: AI agents and more（Google公式、2026年5月）</a></li>
  <li><a href="https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/" target="_blank" rel="noopener">100 things we announced at Google I/O 2026（Google公式、2026年5月）</a></li>
  <li><a href="https://discoveredlabs.com/blog/google-ai-mode-may-2026-search-update" target="_blank" rel="noopener">Google AI Mode and the May 2026 search update（Discovered Labs、2026年5月）</a></li>
  <li><a href="https://heroicrankings.com/seo/managed/google-ai-overview-statistics-2026/" target="_blank" rel="noopener">Google AI Overview Statistics: 2026 Trends and Impact（Heroic Rankings、2026年）</a></li>
  <li><a href="https://wellows.com/blog/google-ai-overviews-ranking-factors/" target="_blank" rel="noopener">Google AI Overviews Ranking Factors: 2026 Guide to Winning Citations（Wellows、2026年）</a></li>
  <li><a href="https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing" target="_blank" rel="noopener">A new resource for optimizing for generative AI in Google Search（Google Search Central、2026年5月）</a></li>
</ul>
"""

# ==============================================================
# 記事2: LLMパーセプション・ドリフト
# ==============================================================
TITLE_2 = "LLMパーセプション・ドリフト——AIがブランドを「どう語るか」が月単位で変動する2026年の新SEO指標と計測・管理戦略"

CONTENT_2 = f"""
<p>あなたのブランドについて、ChatGPTやClaudeやPerplexityはどう語っているだろうか。そしてその「語り方」は先月と今月で変わっていないだろうか。2026年のAI検索・SEO領域で急速に注目を集めている「LLMパーセプション・ドリフト（LLM Perception Drift）」という概念は、まさにこの問いに答えるために生まれた指標だ。SEO順位が変わっていないのに、AIがブランドを引用しなくなった、あるいは競合他社への言及が増えた——そうした「AI内でのブランド認知のずれ」を追跡・管理するための新しいフレームワークが、2026年のAIO専門家の必須知識となっている。本稿では、LLMパーセプション・ドリフトの仕組みから計測方法・具体的な管理戦略まで、実践的な観点で解説する。</p>

{ih("LLMパーセプション・ドリフトの概念を示すタイムライン図。横軸が月（1月〜12月）、縦軸がブランドのAI言及スコア。「Slack」が8.10ポイント低下、「Atlassian」が5.50ポイント上昇する推移を折れ線グラフで対比表示し、LLMの再学習タイミングを矢印でマーキング")}

<h2>LLMパーセプション・ドリフトとは何か：概念と発生メカニズム</h2>

<p>LLMパーセプション・ドリフトとは、大規模言語モデルがブランド・企業・製品について持つ「認識・語り口」が時間とともに変化する現象を指す。より正確に定義すると、「LLMが特定のブランドや製品を言及・引用する頻度、その文脈における評価・トーン・関連付けられる属性が、モデルの再学習・ファインチューニング・RLHF（人間からのフィードバックによる強化学習）サイクルに伴って変動するプロセス」だ。</p>

<p>これがなぜ起きるかを理解するには、LLMの学習構造を把握する必要がある。主要なLLM（GPT-4o、Claude Sonnet、Gemini等）は定期的に新しいウェブデータで再学習され、ファインチューニングが行われる。この再学習の際に「どのコンテンツが引用されているか」「どのメディアでどう取り上げられているか」「ユーザーがどのブランドを高評価しているか」というシグナルが新たに組み込まれる。その結果、前回のモデルではAに関連付けられていた「革新的」という属性がBに移ったり、Cブランドへの言及頻度が減ったりする変化が起きる。</p>

<p>SEO順位は変わっていないのにAI内でのブランド認知が変わる——これがLLMパーセプション・ドリフトの恐ろしい点だ。従来のSEO指標（順位・流入数・被リンク数）を監視していても、この変化は検出できない。AIを主要なタッチポイントとして活用している企業ほど、この見えないリスクにさらされていることになる。</p>

{eh("ここに自社ブランドまたはクライアントブランドに対してChatGPT・Perplexity・Claudeに同じ質問を投げかけた実体験を追加する。「〇〇について教えて」と質問した際に、各LLMがどう回答したか・競合との言及頻度の差などを実際の出力例で示すと説得力が格段に増す")}

<h2>2026年のリアルデータ：Slack、Atlassian事例が示す変動の実態</h2>

<p>LLMパーセプション・ドリフトが実際にどれほどの規模で起きているかを示す具体的なデータがある。2026年に報告された調査では、プロジェクト管理ツール領域において、SlackのLLM内ブランド認識スコアが8.10ポイント低下し、一方でAtlassianが5.50ポイント上昇したという観測結果が記録されている。同期間にSlackのSEO順位は大きく変動しておらず、この変化はLLMの内部認識の変化によるものとされている。</p>

<p>同じ期間にMonday.comとTrelloも注目すべき低下を示した。これらのツールは従来のオーガニック検索では安定したパフォーマンスを示していたにもかかわらず、LLM内での言及・推薦頻度が顕著に低下した。逆にAtlassianが上昇した背景を分析すると、この時期にAtlassianが開発者コミュニティ向けの技術文書とケーススタディを大量に公開し、StackOverflow・GitHub等のAIが高く評価するプラットフォームでの言及が増加していたことが要因として挙げられている。</p>

<p>この事例が示す重要な教訓は3つある。第一に、LLMパーセプション・ドリフトは予告なく発生し、変化の速度は「月単位」であること。第二に、変化の方向性は「どのコンテンツがAI学習データとして高評価を受けているか」に依存するため、SEO施策だけでは管理できないこと。第三に、ドリフトは競合との相対評価でも起きるため、「自社のスコアが維持されていても、競合が上昇すれば相対的に不利になる」ということだ。</p>

{ih("プロジェクト管理ツール領域のLLMパーセプション・ドリフト事例を示す棒グラフ。Atlassian（+5.50）、Monday.com（変化量）、Slack（-8.10）、Trello（変化量）を横並びに比較。変化幅をプラス・マイナスで色分け（青：上昇、赤：低下）")}

<h2>LLMパーセプション・ドリフトが発生する5つのトリガー</h2>

<p>LLMパーセプション・ドリフトはランダムに起きるわけではない。研究と実務観察から、変化を引き起こす主なトリガーが特定されている。</p>

<p><strong>トリガー①：LLMの定期再学習サイクル</strong><br>
主要なLLMは数ヶ月に一度の周期で新しいデータで再学習される。この再学習時に取り込まれるウェブデータの構成が変わると、ブランドへの認識が更新される。新しい論文・技術記事・メディア報道が大量に追加されると、その内容に基づいてブランドの「専門性」「革新性」「信頼性」等の属性評価が更新される。</p>

<p><strong>トリガー②：ユーザーフィードバック（RLHF）の偏り</strong><br>
LLMの応答はユーザーのフィードバック（高評価・低評価・修正）によってファインチューニングされる。特定のブランドに関する回答が継続的に低評価を受けると、そのブランドへの言及頻度が減少するよう調整される可能性がある。逆に専門家コミュニティで高評価を受けるコンテンツを作るブランドは、RLHFを通じて言及頻度が高まることがある。</p>

<p><strong>トリガー③：競合のコンテンツ投資の増加</strong><br>
LLMは相対的な評価を行う。競合がAI学習に適した高品質コンテンツ（原著研究・詳細なケーススタディ・専門家インタビュー等）を大量に公開すると、相対的に自社の位置づけが低下する。Atlassianの事例はまさにこれに当たる。</p>

<p><strong>トリガー④：外部メディアでの言及トーンの変化</strong><br>
LLMはウェブ上のメディア・ブログ・SNS等の外部コンテンツを学習データとして取り込む。業界メディアでの否定的な報道や、SNSでのブランド批判の増加は、LLMのブランド認識に影響を与える可能性がある。逆に著名メディアでの肯定的な言及の増加は、プラス方向のドリフトを引き起こす。</p>

<p><strong>トリガー⑤：構造化データ・公式情報の変更</strong><br>
Wikipedia・Wikidata・会社公式ページ・Google Businessプロフィール等の「公式情報ソース」の内容変更は、LLMの認識に比較的速く反映される。企業の事業領域・製品カテゴリ・技術的特徴等の公式情報が更新されると、それに連動してAI内での位置づけが変化することがある。</p>

{eh("ここに上記5つのトリガーのうち、自分が実際に観察したケースを挿入する。例えば「クライアントの競合がケーススタディを集中公開した時期にChatGPTの推薦頻度が逆転した」など、実際のモニタリング経験に基づく事例があると説得力が大きく増す")}

<h2>計測方法：LLMパーセプション・ドリフトの追跡フレームワーク</h2>

<p>LLMパーセプション・ドリフトを管理するためには、まず計測できる状態を作ることが必要だ。2026年時点で実践されている計測フレームワークを紹介する。</p>

<p><strong>Step 1：計測クエリセットの設計</strong><br>
ブランドが「被引用されるべき」クエリを20〜30個選定する。一般的なカテゴリクエリ（「プロジェクト管理ツールのおすすめは」）、比較クエリ（「AツールとBツールを比べると」）、専門クエリ（「エンタープライズ向けのXXの選び方」）等を含める。競合ブランドも同じクエリで計測することで、相対的なポジション変化を把握できる。</p>

<p><strong>Step 2：複数LLMでの定期的なプロービング</strong><br>
設計したクエリをChatGPT・Perplexity・Claude・Geminiの複数LLMに毎月同じタイミングで投げかけ、応答を記録する。計測する指標は「ブランド言及率（何%の回答でブランドが言及されたか）」「言及時の文脈（肯定的・中立・否定的）」「競合との相対的な言及順序」「関連付けられる属性・形容詞」だ。</p>

<p><strong>Step 3：ツールを使ったスケーリング</strong><br>
手動での計測は限界があるため、LLM可視性の専門ツールを活用することが推奨される。2026年時点で「LLM Boostエージェンシー」と呼ばれる専門サービスが急増しており、ブランドのAI内認知をモニタリングするSaaSツールも複数登場している。これらのツールは設定したクエリに対してLLMを自動的にプロービングし、ブランドの言及スコアを時系列グラフで可視化する機能を持つ。</p>

<p><strong>Step 4：ドリフト原因の特定</strong><br>
スコア変化が検出されたら、タイムラインを遡って変化のトリガーを特定する。競合の大型コンテンツ公開・自社の外部メディアへの露出変化・業界ニュースでの言及・主要LLMの再学習タイミング等を照合することで、ドリフトの原因を推測できる。因果関係は完全に特定できないケースも多いが、「仮説→施策→計測」のPDCAを回すことが重要だ。</p>

{ih("LLMパーセプション・ドリフトの計測ダッシュボードのイメージ図。上部に複数LLMのブランド言及率の月次推移（折れ線グラフ）、下部に競合ブランドとの相対スコア比較（レーダーチャート）。各LLM（ChatGPT・Perplexity・Claude・Gemini）を色分けして表示")}

<h2>ドリフト防止・修正のための実践的な管理戦略</h2>

<p>LLMパーセプション・ドリフトを防止・修正するための施策を優先度順に整理する。AIO専門家としてこれらを自社またはクライアントの戦略に組み込むことが、2026年以降の競争優位の源泉となる。</p>

<p><strong>防止策①：「AIが引用したくなるコンテンツ」の継続的な生産</strong><br>
LLMが最も評価するコンテンツの特徴は、①他では得られないオリジナルデータ・研究・調査を含む、②主張に対して必ず根拠（数値・引用・実験結果）が添えられている、③著者の実体験・実名が明示されている（E-E-A-Tのexperienceシグナル）、の3点だ。プリンストン大学のGEO研究では「出典の明記」「統計の追加」「引用文の追加」という3つの最適化でAI可視性が30〜40%向上することが示されている。</p>

<p><strong>防止策②：権威ある外部プラットフォームでの存在感確立</strong><br>
LLMの学習データとして高く評価されるのは、Wikipedia・ Stack Overflow・GitHub・業界学術誌・著名業界メディアでの言及だ。これらのプラットフォームでブランドが正確に・ポジティブに言及されるよう、デジタルPR施策と技術コミュニティへの貢献（OSS公開・技術解説記事の投稿・登壇等）を組み合わせることが効果的だ。</p>

<p><strong>防止策③：エンティティの明確化と公式情報の最新化</strong><br>
Wikipedia・Wikidata・Google Businessプロフィール・Organization schemaを定期的に更新し、自社ブランドの「正確な定義」をLLMが正しく取り込めるよう管理する。特に事業内容・製品カテゴリ・主要実績の記述は、競合との差別化が明確になるよう精緻に管理する。</p>

<p><strong>修正策：ドリフト検出後の緊急対応プロセス</strong><br>
スコア低下が検出された場合の対応は迅速さが重要だ。まず、低下が起きたクエリカテゴリを特定し、そのカテゴリに関連するコンテンツを集中的にアップデートする。次に、競合が何を公開したかを分析し、不足している情報の補完を行う。また、低下したカテゴリに関する専門家インタビュー・ケーススタディ・オリジナルデータ等の「LLMが引用したくなるコンテンツ」を速やかに公開する。LLMの再学習サイクルは数ヶ月単位のため、修正が反映されるまで継続的なモニタリングが必要だ。</p>

{eh("ここに上記の防止策・修正策を自社またはクライアント向けに実際に試みた結果を追加する。「Wikipedia更新後にLLMの言及頻度が変わったか」「デジタルPR施策の後にAI引用スコアが回復したか」等、LLMパーセプション管理サイクルの実体験を具体的なタイムラインで示すと実践的な価値が増す")}

<h2>まとめ</h2>

<p>LLMパーセプション・ドリフトは、AI検索が主要なタッチポイントになった2026年において、見えないリスクとして多くのブランドを蝕んでいる。SEO順位が安定していても、AIがブランドを「どう語るか」が変われば、AI検索経由の流入・問い合わせ・引用が静かに減少する。SlackとAtlassianの事例が示すように、月単位での変動は現実であり、変化への対応は「気づいてから」では遅い。2026年のAIO戦略においてLLMパーセプション・ドリフトの計測と管理を組み込み、SEO順位と並ぶ核心指標として扱うことが、今後の競争環境で生き残るための必須条件だ。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://searchengineland.com/why-llm-perception-drift-will-be-2026s-key-seo-metric-465676" target="_blank" rel="noopener">Why LLM perception drift will be 2026's key SEO metric（Search Engine Land、2026年）</a></li>
  <li><a href="https://www.digitalapplied.com/blog/llm-perception-drift-new-seo-metric-brand-tracking-2026" target="_blank" rel="noopener">LLM Perception Drift: The New SEO Metric for Brands（Digital Applied、2026年）</a></li>
  <li><a href="https://drivenly.io/llm-perception-drift-the-new-seo-for-2026/" target="_blank" rel="noopener">LLM Perception Drift: The New SEO for 2026（Drivenly、2026年）</a></li>
  <li><a href="https://seoprofy.com/blog/llm-seo/" target="_blank" rel="noopener">LLM SEO in 2026: 8 Strategies to Boost AI Search Visibility（SEOProfy、2026年）</a></li>
  <li><a href="https://www.webpronews.com/llm-perception-drift-ais-shifting-brand-views-and-seo-strategies/" target="_blank" rel="noopener">LLM Perception Drift: AI's Shifting Brand Views and SEO Strategies（WebProNews、2026年）</a></li>
</ul>
"""

# ==============================================================
# 記事3: Bing AI Performance Report + マルチLLM計測戦略
# ==============================================================
TITLE_3 = "Bing AI Performance Report解説とマルチLLM計測の実践——2026年版「どのAIに何回引用されたか」を正確に把握するための新しいAIO効果測定フレームワーク"

CONTENT_3 = f"""
<p>AIO・LLMO対策を実施していても「本当に効果が出ているのか」を正確に測定できている担当者はまだ少ない。GA4でAI経由トラフィックが増えているのは分かる。でもそれがGoogle AI Overviewsなのか、ChatGPTなのか、Bing Copilotなのか、Perplexityなのか——どこから来ているのかが見えていない。2026年5月以降、この「マルチLLM計測」問題を解決するための新しいツールとチャネル分類が相次いで登場した。Microsoftは「Bing Webmaster Tools AI Performance Report」を正式公開し、GoogleはGA4に「AI Assistantチャネル」を追加し、Perplexityは独自のアナリティクス機能を強化した。本稿では、これらの新しい計測手段を横断的に整理し、2026年における実践的なマルチLLM効果測定フレームワークを解説する。</p>

{ih("マルチLLM計測の全体構造を示す図。中央に「自社サイト」を置き、左から「Google AI Overviews → GA4 AI Assistantチャネル」「Bing Copilot → Bing Webmaster Tools AI Performance Report」「Perplexity → Perplexity Analytics」「ChatGPT → UTMパラメータ計測」という4つの計測経路を矢印で示す")}

<h2>なぜマルチLLM計測が必要か：各AIの引用ロジックと流入特性の違い</h2>

<p>マルチLLM計測が必要な理由は、各AIプラットフォームの引用ロジック・ユーザー行動・トラフィック特性が大きく異なるからだ。一つの計測手段で全体を把握しようとすると、重要な示唆を見逃す可能性が高い。</p>

<p>まず**引用数の違い**を理解する必要がある。Perplexityは1回の応答で平均3倍以上の引用元をChatGPTより多く提示し、ほぼ全ての主要な主張に引用番号を付ける。一方でBing Copilotは1回の応答で平均6.89個の引用を示すが、どの引用がどの主張に対応するかの紐付けが曖昧なことが多い。ChatGPTは引用数が相対的に少なく、特定の「ベストソース」を選ぶ傾向がある。</p>

<p>次に**クリック率の違い**だ。Perplexityからの被引用は、クリック率がGoogle AI Overviewsからの引用より高い傾向がある。Perplexityのユーザーはリサーチ目的のユーザーが多く、引用元を確認してサイト訪問する行動が多いためだ。一方、Google AI Overviewsは引用されてもクリック率が低いケースがある——AI Overviewsがそれ自体で完結した回答を提供するため、ユーザーが元ソースを訪問する動機が薄くなる場合がある。</p>

<p>さらに**被引用と非被引用の相関関係の違い**も重要だ。調査によると、ChatGPT・Perplexity・Copilotが引用するURLの80%がGoogleの上位100位以内にランクされていないという事実がある。つまり、LLMの引用はGoogleのSEO評価とは独立した基準で選ばれていることが多く、各AIプラットフォームを個別に最適化・計測する必要がある。</p>

{eh("ここに自社サイトまたはクライアントサイトで実際に計測したマルチLLM引用データを追加する。「GoogleとBingとPerplexityで引用されたページが異なっていた」「ChatGPTが引用するページはGoogleでは5位以下だった」等の実体験があれば、理論を裏付ける貴重な事例になる")}

<h2>Bing Webmaster Tools AI Performance Report：具体的な活用方法</h2>

<p>2026年、Microsoftは「Bing Webmaster Tools AI Performance Report」を正式公開した。これはBing CopilotがどのページをどれだけAI応答の根拠（グラウンディングデータ）として使用したかを計測できる初の公式ツールだ。</p>

<p>主な機能は「AI引用数の表示」だ。Copilotが自社ウェブサイトを引用した回数を、ページ単位・期間単位で確認できる。どのページが最もCopilotの応答に使われているかを把握することで、Copilot引用獲得に成功しているコンテンツの特徴を分析できる。</p>

<p>重要な注意点がある。このAI Performance Reportは「引用数（Impressions相当）」は表示するが、「そこからのクリック数」は現時点では表示しない。Copilotがサイトを引用しても、ユーザーが元ページをクリックしたかどうかは別途分析が必要だ。Microsoftは2026年のMicrosoft Clarityのアップデートで、Copilotの回答に使われた「グラウンディングクエリ（Copilotが答えを導くために参照したユーザーの質問）」をClarityダッシュボードで確認できる機能も追加しており、引用されたコンテキストの把握に役立てることができる。</p>

<p>Bing Copilot引用最適化において実証されているポイントを整理する。第一に**BingBotのクロール許可確認**：robots.txtでBingBotがブロックされていると、Copilotの引用対象から外れる。第二に**構造化データの整備**：FAQ・HowTo・Article等のschema.orgマークアップがCopilotの引用選択に影響する。第三に**E-E-A-Tシグナルの強化**：著者情報・組織情報・実績の明示がBing Copilotの「信頼できるソース」判定に重要だ。第四に**コンテンツの直接的回答形式**：Copilotはクエリに対して最初の段落または2〜3段落で直接的に答えるページを好む傾向があり、冒頭に明確な回答を置くライティングスタイルが有効だ。</p>

{ih("Bing Webmaster Tools AI Performance Reportの画面モックアップ。上部に「AI引用数の推移グラフ（月別）」、下部に「引用数上位ページ一覧（URL、引用数、前月比）」のテーブルを配置。実際の管理画面をイメージした構成で示す")}

<h2>GA4「AI Assistantチャネル」：Google AI経由トラフィックの計測新機能</h2>

<p>2026年5月13日、GoogleはGA4（Google Analytics 4）の「デフォルトチャネルグループ」に新しい分類「AI Assistant」チャネルを追加した。これはGoogle AI Overview・AI Mode経由のセッションを既存の「Organic Search」とは別枠で計測するための機能だ。</p>

<p>この追加の背景には、AI検索経由の流入と従来のオーガニック検索からの流入を区別して分析したいというマーケターの需要があった。従来はGA4のデフォルト設定では、AI Overview引用からのクリックも「Organic Search」に分類されており、AIが流入増減に与えた影響が見えなかった。</p>

<p>AI Assistantチャネルを活用した分析で特に有益なのは以下の3点だ。第一に**AI経由流入のコンバージョン率分析**：AI検索経由のユーザーと通常のオーガニック検索経由のユーザーとでコンバージョン率・セッション深度・滞在時間を比較することで、AI経由ユーザーの質を評価できる。第二に**AI引用獲得ページの特定**：AI Assistantチャネルから流入のあるページをリスト化し、それらのページの共通要素（構造・長さ・フォーマット・スキーマ）を分析することで、自社サイトにおけるAI引用パターンを把握できる。第三に**AI vs SEO流入の推移モニタリング**：月次でAI Assistantチャネルと他のチャネルの流入推移を比較し、AI移行の速度と自社への影響を定量的に追跡できる。</p>

<p>実装面での注意事項がある。GA4のAI Assistantチャネルは2026年5月13日以降のデータから自動的に分類されるため、過去データへの遡及適用はない。また、Google AI Overview以外のAI（ChatGPT・Perplexity等）からの流入は、リファラーURLの形式が異なるため別途設定が必要になる場合がある。Google Search Console側でも2026年以降は「AI Overview引用クエリ」の可視化が強化されており、GA4とSearch Consoleを連携させることでより詳細な計測が可能になる。</p>

{eh("ここにGA4 AI Assistantチャネルを実際に設定・計測した際の気づきや、通常オーガニックとのコンバージョン率差、計測データで意外だったことを追加する。「AI Assistant経由は直帰率が低かった」「特定カテゴリのページがほぼAI経由だった」等の実体験が読者の参考になる")}

<h2>Perplexity・ChatGPT引用の計測：UTMパラメータとリファラー分析</h2>

<p>Google AI OverviewsとBing Copilotには専用の計測ツールが整備されてきたが、Perplexity・ChatGPTからの流入はどう計測するか。これらのプラットフォームは公式のアナリティクス機能が限定的なため、現時点では代替手段の組み合わせが必要だ。</p>

<p>最も実践的な方法は**リファラーURLの分析**だ。Perplexityからのクリックは通常 `perplexity.ai` ドメインのリファラーとしてGA4に記録される。GA4の「参照元レポート」で `perplexity.ai` を抽出し、どのページがPerplexityから流入を獲得しているかを確認できる。ChatGPT SearchからのクリックはOpenAIドメイン（`chatgpt.com` や `openai.com`）のリファラーとして記録される場合がある。</p>

<p>ただしリファラー分析には限界がある。プライバシー保護の観点からリファラー情報が省略されるケースが増えており、「ダイレクト流入」として分類されるAI経由トラフィックも少なくない。このため、「AI引用によるブランド認知向上→後日のダイレクト流入」というインダイレクトな効果は、リファラー分析だけでは捕捉できない。</p>

<p>より精度の高い計測を行うための補完手段として、**Perplexity Analytics**（Perplexityが企業向けに提供し始めたダッシュボード機能）の活用が2026年以降に普及してきている。また、LLM可視性専門ツール（LLMrefs・Profound・Otterly等）は複数のAIプラットフォームにわたるブランド言及を定期的に計測し、「AIに何回引用されたか」を統合ダッシュボードで表示する機能を提供している。これらのツールは月額数万円から利用でき、中規模以上のAIO投資をしている企業にとってROI計測の必須ツールになりつつある。</p>

{ih("マルチLLM効果測定のKPIダッシュボードの構成案。左列：Google AI（AI Assistantチャネル流入数・CTR変化）、中列：Bing Copilot（AI Performance Report引用数・Microsoft Clarity Grounding Queries）、右列：Perplexity/ChatGPT（リファラー流入数・専用ツールの言及スコア）を3カラムで比較")}

<h2>2026年版：マルチLLM計測フレームワークの実装ステップ</h2>

<p>以上を踏まえ、AIO専門家が今すぐ実装すべきマルチLLM計測フレームワークを段階的に整理する。</p>

<p><strong>Phase 1（即時実施）：基盤計測の設定</strong><br>
GA4のデフォルトチャネルグループでAI Assistantチャネルが正しく動作しているか確認する。2026年5月13日以降のデータから自動分類されているはずだが、カスタム設定が必要な場合もある。同時にBing Webmaster Toolsにサイトを登録し（未登録の場合）、AI Performance Reportにアクセスできる状態にする。</p>

<p><strong>Phase 2（1〜2週間）：ベースラインデータの収集</strong><br>
GA4でAI Assistantチャネルの流入量・上位流入ページ・コンバージョン率を確認する。Bing Webmaster ToolsでCopilot引用の上位ページをリスト化する。GA4のリファラーレポートでperplexity.ai・openai.com等からの流入を抽出しベースラインを記録する。これらを月次で更新するKPIテンプレートに落とし込む。</p>

<p><strong>Phase 3（1ヶ月）：クロスプラットフォーム引用パターンの分析</strong><br>
「Google AI Overviewに引用されているページ」「Bing Copilotに引用されているページ」「Perplexityから流入しているページ」の重複・差異を分析する。引用率の高いページの共通要素（コンテンツタイプ・長さ・構造・更新頻度・スキーマ）を抽出し、他のページへの展開方針を策定する。</p>

<p><strong>Phase 4（継続）：LLMパーセプション・ドリフトとの連動監視</strong><br>
前述のLLMパーセプション・ドリフト計測と組み合わせ、「LLMが自社ブランドをどう語るか（定性）」と「LLM経由の実際のトラフィック（定量）」の両軸でモニタリングを行う。定性的な認識変化が定量的なトラフィック変化として現れるタイムラグを把握することで、早期警戒システムとして機能させる。</p>

{eh("ここにこの4フェーズのマルチLLM計測フレームワークを実際に導入した際の所感や、想定外の発見（例：「BingとGoogleで引用されているページが全く違った」「Perplexityからのコンバージョンが一番高かった」等）を追加すると、フレームワークの有用性がより具体的に伝わる")}

<h2>まとめ</h2>

<p>2026年のAIO効果測定は、単一プラットフォームの計測では不十分な時代に入った。Google AI Overview・Bing Copilot・Perplexity・ChatGPTはそれぞれ異なる引用ロジックを持ち、異なるユーザー層を抱え、異なる計測手段が必要だ。GA4 AI Assistantチャネルの登場とBing AI Performance Reportの公開により、主要プラットフォームの計測基盤は整いつつある。今すぐ計測基盤を構築し、どのAIプラットフォームで何が引用されているかを正確に把握することが、AIO投資のROIを最大化するための第一歩だ。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://almcorp.com/blog/bing-webmaster-tools-ai-performance-report-guide/" target="_blank" rel="noopener">Bing Webmaster Tools Unveils AI Performance Report: Complete Guide（ALM Corp、2026年）</a></li>
  <li><a href="https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/" target="_blank" rel="noopener">Inside Bing's New AI Performance Report: What 20,000 Copilot Citations Taught Us（Search Influence、2026年）</a></li>
  <li><a href="https://llmrefs.com/blog/perplexity-vs-copilot" target="_blank" rel="noopener">Perplexity vs Copilot SEO & Marketing Showdown 2026 Guide（LLMrefs、2026年）</a></li>
  <li><a href="https://www.searchenginejournal.com/microsoft-clarity-now-shows-grounding-queries-behind-ai-citations/575279/" target="_blank" rel="noopener">Microsoft Clarity Now Shows Grounding Queries Behind AI Citations（Search Engine Journal、2026年）</a></li>
  <li><a href="https://prtimes.jp/main/html/rd/p/000000028.000166736.html" target="_blank" rel="noopener">月刊AI検索業界レポート2026年5月号——Googleが「AI対策＝SEO」と明言（ナレッジホールディングス、2026年5月）</a></li>
  <li><a href="https://webtan.impress.co.jp/e/2026/04/07/52273" target="_blank" rel="noopener">AI検索利用率が8か月で3.5倍に急増「AI検索白書2026」（Web担当者Forum、2026年4月）</a></li>
</ul>
"""


def main():
    articles = [
        (TITLE_1, CONTENT_1),
        (TITLE_2, CONTENT_2),
        (TITLE_3, CONTENT_3),
    ]
    for title, content in articles:
        post_draft(title, content)
    print("\n✅ 全3記事の投稿が完了しました。")


if __name__ == "__main__":
    main()
