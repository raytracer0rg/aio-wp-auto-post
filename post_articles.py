#!/usr/bin/env python3
"""
AIOネタ自動下書き投稿スクリプト
対象: aiotaisaku.com
実行: python3 post_articles.py
"""

import urllib.request
import urllib.error
import json
import base64
import sys

WP_URL = "https://aiotaisaku.com"
WP_USER = "kr_aiota_20250512"
WP_PASS = "fQe7 0nkE rXbm 8gCL BObs qRbs"

# ── 記事1 ─────────────────────────────────────────────────────────────────────
ARTICLE_1_TITLE = "Google I/O 2026でAI Mode 10億ユーザー突破——Information Agentsが変えるAIOコンテンツ戦略の新常識"

ARTICLE_1_CONTENT = """
<p>2026年5月20日、GoogleはサンフランシスコのShoreline Amphitheatreで開催したGoogle I/O 2026において、検索の「25年来最大のアップデート」を正式に発表した。AI Modeが月間アクティブ10億ユーザーを突破したことが明かされ、Gemini 3.5 Flashを新デフォルトモデルとして採用。さらに、バックグラウンドで常時稼働する「Information Agents」というまったく新しいコンセプトが世界へ示された。すでにAIO・LLMOを実践しているマーケターにとって、このアップデートが示す方向性は看過できない。今後のコンテンツ戦略をどう変えるべきか、データとともに整理する。</p>

<h2>AI ModeとAI Overviewの普及規模——数字が示す検索行動の変容</h2>

<p>Google I/O 2026のキーノートが公開した数字は、AIが検索の中心となりつつあることを裏付ける。AI Modeの月間利用者数は10億人を超え、デビューからわずか1年での達成となった。AI Overviewの月間利用者数は25億人。クエリ数はAI Modeのローンチ以来、四半期ごとに倍増を続けており、1回の検索が従来の3倍の長さを持ち、フォローアップクエリは米国だけで月40%のペースで増えている。</p>

<p>BrightEdgeの2026年2月時点のデータでは、追跡対象クエリの約48%にAI Overviewが表示されており、前年比58%増の水準だ。Conductorが21.9百万件の検索を分析したデータでは、2026年Q1時点で25.11%のクエリがAI Overviewを伴っていた。これはSEOのトラフィック構造を根本から変えており、AI Overviewが表示されるクエリでは検索1位のCTRが最大58%低下するという報告もある。</p>

<p>こうした数字は、コンテンツがAIに引用されるかどうかが、従来の「1位表示」と同等以上の重みを持ち始めたことを示している。Ahrefsの大規模調査（86万3千キーワード、400万件のAI Overview URL対象）では、AI Overviewに引用されているページのうち上位10位に入っているのは38%にすぎず、7ヶ月前の76%から大幅に落ち込んでいる。上位表示≠引用という新常識が、データによって確認された形だ。</p>

<h2>Gemini 3.5 Flash：デフォルトモデル変更がAIO引用パターンを変えた</h2>

<p>GoogleはAI ModeのデフォルトモデルをGemini 3.5 Flashに変更し、2026年1月27日に全世界展開した。Ahrefsの調査では、この時期を境にAI Overview引用パターンが大きく変化していることが確認されている。</p>

<p>Gemini 3.5 Flashは高速かつ推論能力が向上しており、「query fan-out」と呼ばれる手法——1つのクエリをAIが複数のサブクエリへ分解し、それぞれのソースを探索してから統合する仕組み——をより高度に実施する。このメカニズムにより、AIは単一のキーワードに強いページではなく、「関連するサブトピックを網羅している」ページを優先して引用する傾向が強まる。</p>

<p>たとえば「AI検索 最適化 方法」というクエリに対し、Geminiは「AI検索とは」「最適化の具体施策」「導入企業の事例」「測定方法」といったサブクエリを内部で生成し、それぞれの最良ソースを組み合わせた回答を形成する。コンテンツがこのfan-outに応答できる構造になっていなければ、引用から外れるリスクが高まる。</p>

<h2>Information Agents：常時稼働するAIが求めるコンテンツ鮮度要件</h2>

<p>Google I/O 2026で最も注目すべきアナウンスの一つが「Information Agents」だ。これはユーザーの代わりにウェブを24時間365日監視し、関連性の高い変化が起きた際に合成ブリーフィングをプッシュ通知で届けるAIエージェントである。Googleは「Google Alertsの次の進化形」と表現しているが、単なるキーワード通知ではなく、情報の収集・分析・要約まで自動化している点が本質的に異なる。</p>

<p>Information AgentsはGoogle AI ProおよびUltraサブスクライバー向けに2026年夏に先行提供される予定で、将来的には一般展開も見込まれる。このエージェントが常時ウェブを巡回するということは、「エージェントが参照したいコンテンツ」であり続けることが新たなAIO要件として浮上してくる。</p>

<p>GEO研究では、コンテンツが3ヶ月以上経過するとAI引用率が急落するというデータがある。Information Agentsの登場はこの傾向をさらに加速させる可能性が高く、重要コンテンツの更新頻度を四半期単位から月次単位へと引き上げる必要性が生まれている。また、最終更新日を明示的に示すことで、Perplexityなどのリアルタイム検索系AIエンジンからの引用率が最大30%向上するというデータも報告されている。</p>

<h2>マルチモーダル検索の拡大：テキスト外コンテンツの最適化が急務</h2>

<p>Google I/O 2026では、検索ボックスの大幅刷新も発表された。動的に拡張されるUI、画像・ファイルのマルチモーダル入力、AIによるインテント先読みサジェストが実装された。現時点でAI Modeのクエリの16%以上がすでに音声・画像・動画を組み合わせたマルチモーダル形式だ。</p>

<p>この変化は、テキストのみで構成されたコンテンツへの依存から脱却する必要性を示している。画像のalt属性の充実、動画コンテンツへの字幕・全文トランスクリプトの追加、インフォグラフィックのテキスト版の整備——こうした対応が、マルチモーダルクエリでの引用機会を生み出す。特にYouTubeはすでにAI Overviewの全引用のうちトップ100外からの引用の18.2%を占める最多引用ドメインとなっており、動画コンテンツのAIO最適化も戦略に組み込む価値が高い。</p>

<h2>実践：Google I/O 2026アップデートへの具体的対応策</h2>

<p>Google I/O 2026のアップデートを踏まえ、今週から着手できる施策を3点に絞る。</p>

<p><strong>① コンテンツ更新サイクルの月次化</strong><br>
主要コンテンツページに「最終更新日」を明示し、少なくとも月1回の内容更新を実施する。更新内容は単なる日付変更ではなく、最新データへの差し替えや新しい事例の追加といった実質的な改訂が必要だ。Information Agentsが求めるのは「今日この瞬間に最も正確な情報」であることを意識する。</p>

<p><strong>② query fan-outを見越したコンテンツ設計</strong><br>
主要なトピックページに対し、Geminiが生成しうるサブクエリを想定した見出し・FAQセクションを追加する。たとえばメインテーマの概要・具体施策・測定方法・事例・注意点という5つの軸を1ページ内で網羅することで、fan-out引用の受け皿になりやすくなる。FAQPageスキーマを実装するとAI引用率が最大2倍という報告もある。</p>

<p><strong>③ マルチモーダル素材の整備</strong><br>
既存の主要コンテンツに対して、画像alt属性の見直し、動画トランスクリプトの追加、インフォグラフィックのテキスト補足を段階的に実施する。マルチモーダル検索が16%を超えた現在、テキスト一辺倒のページはこのシェアを取り逃がしている。</p>

<h2>まとめ</h2>

<p>Google I/O 2026は、AI検索が「追加オプション」から「デフォルトの検索体験」へと完全移行する宣言だった。AI Mode 10億ユーザー、Information Agentsの登場、Gemini 3.5 Flashの推論強化——これらの変化が示すのは、コンテンツがAIによって消費・引用・配信される時代の本格到来だ。コンテンツの鮮度、query fan-out対応、マルチモーダル整備の3軸を今期中に強化し、2026年後半のAIO競争で先行したい。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://blog.google/products-and-platforms/products/search/search-io-2026/" target="_blank" rel="noopener">Google Search's I/O 2026 updates: AI agents and more（Google Blog、2026年5月）</a></li>
  <li><a href="https://discoveredlabs.com/blog/google-ai-mode-may-2026-search-update" target="_blank" rel="noopener">Google AI Mode and the May 2026 search update: what marketers should do this quarter（Discovered Labs、2026年5月）</a></li>
  <li><a href="https://www.digitalapplied.com/blog/google-search-overhaul-ai-mode-1b-users" target="_blank" rel="noopener">Google Search Overhaul 2026: AI Mode Hits 1B Users（Digital Applied、2026年）</a></li>
  <li><a href="https://thelettertwo.com/2026/05/22/ai-economy-google-search-ai-seo-aeo-io-2026/" target="_blank" rel="noopener">The AI Economy: Google Rebuilt Search With AI at I/O 2026（The Letter Two、2026年5月22日）</a></li>
  <li><a href="https://heroicrankings.com/seo/managed/google-ai-overview-statistics-2026/" target="_blank" rel="noopener">Google AI Overview Statistics: 2026 Trends and Impact（Heroic Rankings、2026年）</a></li>
</ul>
"""

# ── 記事2 ─────────────────────────────────────────────────────────────────────
ARTICLE_2_TITLE = "AI OverviewはSEO上位サイトをもう引用しない——Ahrefsの86万クエリ調査が明かす引用ロジックの崩壊と再設計"

ARTICLE_2_CONTENT = """
<p>SEO上位に立てば、Google AI Overviewにも引用される——そんな前提がデータによって否定されつつある。Ahrefsが実施した86万3千キーワード・400万件のAI Overview URLを対象とした大規模調査では、AI Overviewに引用されているページのうち検索上位10位内に入っているのはわずか38%。7ヶ月前は76%だったことを考えると、急激な乖離が進んでいる。この変化は何を意味し、何を実践すれば引用されるのか。データを深掘りする。</p>

<h2>76%から38%へ——AI Overview引用とSEOランキングの乖離が加速</h2>

<p>Ahrefsの調査で浮き彫りになったのは、AIが引用するソースと検索エンジンが上位表示するページの関係が急速に解体されているという事実だ。2024年後半時点では、AI Overviewの引用元のうち約76%がGoogle検索の上位10位内に入るページだった。それが2026年には38%まで落ちた。残りの引用は11位〜100位のページが31.2%、上位100位外のページが31%とほぼ均等に分散している。</p>

<p>5W ResearchもこれとほぼAgreeing するデータを別途発表しており、「上位Google順位とAI引用元の重複は70%から20%未満に崩壊した」と指摘している。この乖離は偶発的な変動ではなく、2026年1月27日のGemini 3への移行を契機とした構造的なシフトと見られている。</p>

<p>さらに、ドメインオーソリティ（DA）の相関係数はr=0.18まで低下しており、大手メディアや権威あるサイトだから引用されるという従来の法則が崩れている。AI Overviewの引用元の47%はGoogle検索5位以下のページから来ているというデータも示されている。</p>

<h2>なぜ乖離が起きるのか：query fan-outの仕組み</h2>

<p>この乖離を理解するカギが「query fan-out」だ。Googleが公式に確認しているこのメカニズムは、AI Overviewを生成する際に1つのクエリを複数のサブクエリへ分解し、それぞれについて最適なソースを個別に探索した上で、統合した回答を生成するというプロセスだ。</p>

<p>たとえば「AI Overview対策の具体的な方法」というクエリが入力された場合、AIは内部で「AI Overviewとは」「引用されるコンテンツの特徴」「技術的な実装方法」「測定方法」などのサブクエリを生成する。それぞれのサブクエリで最適なページを選ぶため、最終的な引用元は多様なドメイン・順位位置のページに分散する。</p>

<p>つまり、「このキーワードで1位を取る」という集中戦略よりも、「特定の角度で最も詳しく・信頼性が高い」ページになるという専門性戦略の方が、AI Overviewへの引用には有利に働く。自社サイトが何かのサブトピックで「ここにしかない情報」を持つことが、引用確率を高める。</p>

<h2>引用されるコンテンツの具体的特徴——semantic completenessとパッセージ長</h2>

<p>1万5847件のAI Overview結果を分析した調査では、semantic completeness（意味的完全性）スコアが8.5/10以上のコンテンツは、4.2倍引用されやすいという結果が得られている。意味的完全性とは、あるトピックに関して「問い・背景・証拠・結論・反証・応用」という構造が揃っているかを評価する指標だ。</p>

<p>パッセージ長に関しても重要なデータがある。AI Overviewが引用するコンテンツの62%は100〜300語（日本語換算で200〜600文字程度）のパッセージを含むページからの引用であり、最適なパッセージ長は134〜167語とされている。長大な説明文よりも、明確に区切られた短め〜中程度の段落が引用の単位になりやすい。</p>

<p>また、引用されたコンテンツを持つページは、引用されていない競合と比較して有機検索クリックが35%増、ペイドクリックが91%増という業績インパクトも報告されている。AI引用はトラフィック増加と有意な相関があることが確認されている形だ。</p>

<h2>YouTubeが最多引用ドメインに浮上——動画コンテンツのAIO価値</h2>

<p>Ahrefsの調査で特筆すべきもう一つの発見が、YouTubeの急浮上だ。YouTubeは現在、Google AI Overviewの全引用のうち上位100位外からの引用の18.2%を占める最多引用ドメインとなっている。テキストコンテンツ一辺倒のSEO戦略では捉えきれないこの傾向は、動画コンテンツのAIO最適化の重要性を示している。</p>

<p>動画が引用されやすい要因として考えられるのは、①動画トランスクリプトがテキストとして検索可能、②視覚的・実演的な情報はテキストでは代替しにくい独自性がある、③視聴者エンゲージメント指標（完視聴率・コメント数）がコンテンツ品質のシグナルになっている、という3点だ。特に専門的なハウツー・事例紹介・比較レビューの動画は引用対象になりやすい。</p>

<h2>2026年3月のコアアップデート：Information Gainが強化</h2>

<p>Googleの2026年3月コアアップデートでは「Information Gain」——既存の検索結果と比較して、そのコンテンツがどれだけ新しい知見を提供するかを測るシグナル——が再重視されるよう重み付けが変更された。このアップデートは、オリジナルリサーチ、独自データ、一次情報に基づくコンテンツを優遇する方向を強化している。</p>

<p>AIが生成した文章や既存情報の言い換えは、Information Gainスコアが低くなるため、この流れと逆行する。自社調査・クライアント事例・実測データといった「その組織にしか書けない情報」を記事の中核に置くことが、2026年後半のコンテンツ戦略の軸となる。</p>

<h2>実践：AI Overview引用を獲得するための設計変更</h2>

<p>前述のデータを踏まえ、引用獲得のために今すぐ実施できる設計変更を整理する。</p>

<p><strong>① コンテンツをパッセージ単位で構造化する</strong><br>
100〜300語（日本語200〜600文字）の明確な段落を意識してライティングを行う。各段落が独立して引用可能な「一問一答」的な構造を持たせることで、query fan-outの各サブクエリに対応しやすくなる。見出し直後に明確な定義・結論から始まる段落設計が効果的だ。</p>

<p><strong>② semantic completenessを高める</strong><br>
主要コンテンツページに対し、「問いの提示→背景→証拠データ→実践方法→例外・注意点→まとめ」という6要素を揃える。FAQ構造とFAQPageスキーマを組み合わせることで、AI引用率が最大2倍に向上するという報告がある。</p>

<p><strong>③ Information Gainを確保する</strong><br>
記事に含める情報のうち、少なくとも一つは「他のサイトにはない独自データ・事例・分析」を盛り込む。自社顧客への調査結果、実際のテスト結果の数値、一次資料への独自インタビューなどがこれにあたる。AIが「引用する価値のある情報」を持つページであり続けることが最重要だ。</p>

<h2>まとめ</h2>

<p>Google AI OverviewがSEO上位ページへの引用を76%から38%へ減らしたという事実は、「上位表示が引用を保証する」というAIO戦略の前提が崩れたことを意味する。query fan-out、semantic completeness、Information Gain——これらの概念を軸に、コンテンツをAIが引用したくなる専門性の源泉として再設計することが、2026年後半のAIO戦略の核心だ。順位を守ることと引用されることを、別の最適化課題として並行して取り組む時代が到来している。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://almcorp.com/blog/google-ai-overview-citations-drop-top-ranking-pages-2026/" target="_blank" rel="noopener">Google AI Overview Citations From Top-10 Pages Dropped From 76% to 38%（ALM Corp、2026年）</a></li>
  <li><a href="https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/" target="_blank" rel="noopener">Google AI Overview Citations From Top-Ranking Pages Drop Sharply（Search Engine Journal、2026年）</a></li>
  <li><a href="https://www.prnewswire.com/news-releases/new-5w-research-overlap-between-top-google-rankings-and-ai-cited-sources-has-collapsed-from-70-to-under-20-302760132.html" target="_blank" rel="noopener">New 5W Research: Overlap Between Top Google Rankings and AI-Cited Sources Has Collapsed From 70% to Under 20%（PR Newswire、2026年）</a></li>
  <li><a href="https://wellows.com/blog/google-ai-overviews-ranking-factors/" target="_blank" rel="noopener">Google AI Overviews Ranking Factors: 2026 Guide to Winning Citations（Wellows、2026年）</a></li>
  <li><a href="https://www.evertune.ai/resources/insights-on-ai/googles-march-2026-core-update-a-content-best-practices-guide-for-seo-and-ai-search" target="_blank" rel="noopener">Google's March 2026 Core Update: A Content Best Practices Guide for SEO and AI Search（Evertune AI、2026年）</a></li>
</ul>
"""

# ── 記事3 ─────────────────────────────────────────────────────────────────────
ARTICLE_3_TITLE = "ChatGPTとPerplexityの引用ドメインは11%しか重複しない——マルチプラットフォーム時代のLLMO戦略とプラットフォーム別最適化の実践"

ARTICLE_3_CONTENT = """
<p>ChatGPTで引用されているブランドとPerplexityで引用されているブランドに、どれほど重複があるだろうか。AuthorityTechが2026年に実施した調査の答えはわずか11%だ。つまり、ある企業がChatGPTで高頻度に引用されていても、Perplexityではほとんど存在しない可能性があり、逆もまた然りだ。複数のAIプラットフォームが並立する現在、「LLMOをやっている」と言いながら特定の一プラットフォームしか最適化していない企業は、大半の引用機会を逃している。プラットフォームの引用ロジックの違いを整理し、マルチプラットフォーム対応のLLMO戦略を構築する方法を解説する。</p>

<h2>ChatGPTとPerplexityは引用ロジックが根本的に異なる</h2>

<p>ChatGPTとPerplexityの引用元が11%しか重複しない最大の理由は、情報取得の仕組みが根本的に異なるためだ。</p>

<p>ChatGPTはハイブリッドアプローチを採用しており、学習データ（知識カットオフ以前）とSelective Web Retrievalを組み合わせた回答生成を行う。学習データに含まれているブランドや情報はそのまま活用され、ウェブ検索が必要な場合のみリアルタイム取得を行う。このため、長期にわたって多くのウェブサイトで言及・引用されてきたブランドや情報が、ChatGPTでは引用されやすい傾向がある。</p>

<p>一方のPerplexityは、すべてのクエリに対してリアルタイムウェブ検索を実行し、GoogleとBingの複数の検索APIを組み合わせてソースを収集する。学習データへの依存が低く、現時点でのウェブ上の評判・情報鮮度・検索可視性が引用に直接影響する。また、Perplexityは1回の回答に平均21.9件の引用を含むのに対し、ChatGPTの引用は平均10.4件と半数以下だ。引用の量が多いPerplexityは、より多くのブランドに露出機会を与えるが、競合も多いという側面がある。</p>

<h2>B2B購買行動におけるAI検索の台頭——引用の経済的価値</h2>

<p>LLMOの実践を急ぐ理由は、AIが引用されることの経済的リターンが明確になってきたためだ。2026年の調査では、B2B購買担当者の90%が購買プロセスでGenerative AIツールを活用しており、そのうち半数がGoogleではなくChatGPTなどのAIプラットフォームを最初のリサーチ起点にしていることが示されている。</p>

<p>AI引用に登場する企業はそうでない競合と比較してコンバージョン率が3.2倍高いというデータもあり、単なる認知向上を超えたビジネスインパクトが確認されつつある。また、2026年2月時点でB2BブランドのオーガニックトラフィックのうちAIアシスタント経由が31%を占め、2025年1月の時点では同数値が従来検索68%対AIアシスタント不在という構造だったことを考えると、変化のスピードは急速だ。</p>

<p>日本においても、2026年時点でのGoogleの全検索クエリの48%以上にAI Overviewが表示されており、「AI検索経由問い合わせが4倍になった」という国内事例も出てきている。LLMOは海外事例だけでなく、国内マーケットでも実績が積み上がり始めた段階にある。</p>

<h2>プラットフォーム別引用ロジックと最適化アプローチ</h2>

<h3>ChatGPT：第三者メンション戦略が鍵</h3>

<p>ChatGPTへの引用を増やすうえで最も重要な要素は、第三者サイトからのブランドメンションだ。AIの回答中に登場するブランドの85%は自社サイトではなくサードパーティからの言及から引用されているという調査がある。つまり、業界メディアへの寄稿・プレスリリースの配信・専門家コミュニティでの活動・他ブランドとのコラボレーション——こうしたオフサイト戦略がChatGPTでのプレゼンスを左右する。</p>

<p>加えて、ChatGPTは学習データに含まれる情報を重視するため、長期にわたって業界の権威サイト（Wikipedia、業界協会、主要メディアなど）で言及されてきたブランドが優位に立ちやすい。これはすぐに変えられるものではないが、中長期的に権威性の高いサイトへの掲載を増やしていく活動が重要だ。</p>

<h3>Perplexity：リアルタイムSEOとコンテンツ鮮度が直結</h3>

<p>Perplexityはリアルタイム検索をベースにしているため、従来のSEO施策（上位表示の維持・新規コンテンツの定期発行・内部リンク強化）との相性が良い。特に「最終更新日」の明示が引用率に直接影響しており、可視性の高い場所に更新日を表示することでPerplexity引用率が最大30%向上するというデータがある。</p>

<p>Perplexityは回答あたりの引用数が21.9件と多いため、ニッチなトピックや特定の質問に特化した専門コンテンツを量産することで引用機会を増やしやすい。コンテンツのカバレッジ（話題の網羅性）を高めることが、Perplexityでの引用面積を広げる実践的なアプローチだ。</p>

<h3>Google AI Overview：query fan-outとsemantic completenessへの対応</h3>

<p>Google AI Overviewについては前述の通り、semantic completeness（意味的完全性）と100〜300語の適切なパッセージ長が引用と相関している。日本語コンテンツにおいても、200〜600文字の適切な段落に区切り、各段落が独立した情報単位として成立するように設計することが重要だ。また、FAQPageスキーマの実装によりAI引用率が最大2倍向上するというデータもある。</p>

<h2>高速で引用率を上げる3つの横断施策</h2>

<p>どのプラットフォームでも共通して引用率向上に効果があると報告されている施策が3つある。</p>

<p><strong>① 統計データ＋方法論の明記</strong><br>
具体的な数値・データとその調査方法論を明記したコンテンツへの改訂は、ChatGPT・Perplexity・Google AIの全プラットフォームで引用可視性が22〜28%向上するという報告がある。「約半数」「多くの企業」といった曖昧な記述を「48%」「B2B企業367社中193社」といった具体的な数値表現に変えるだけでも効果がある。</p>

<p><strong>② ヘッダー間の段落を120〜180語（日本語240〜360文字）に再構成</strong><br>
既存の高パフォーマンスコンテンツをこのパッセージ長に再構成した結果、引用率が40%改善したという事例が報告されている。見出し直後に結論を置き、続く段落で根拠・具体例・応用を展開するという「逆ピラミッド構造」を適用することが実践的だ。</p>

<p><strong>③ 「最終更新日」の明示</strong><br>
記事ページのメタデータと本文の両方に最終更新日を表示することで、Perplexityでの引用率向上（+30%）に加え、全般的なAI検索での信頼性シグナルが強化される。更新日を表示するだけでなく、実際に内容を更新した証拠となる具体的な記述変更を伴わせることが重要だ。</p>

<h2>プラットフォーム別引用状況の測定方法</h2>

<p>LLMOの最大の課題の一つが測定だ。ChatGPT・Perplexityへの自社ブランドの引用状況を定期的にモニタリングする仕組みを整えておく必要がある。</p>

<p>実践的な方法として、①自社ブランド名・主要サービス名・代表的な専門用語を含む20〜30のテストプロンプトを設定、②週次または月次でChatGPT・Perplexity・Google AI Overviewそれぞれに実行してスプレッドシートに記録、③引用の有無・引用位置・引用される文言の変化を追跡するというプロセスを確立する。これにより、どの施策が引用率改善に効果があったかを逆算して評価できるようになる。</p>

<p>国内では「AI検索経由問い合わせが4倍」という実績を持つ企業も出始めており、測定を伴った継続的な最適化がLLMOの成果を積み上げていく。プラットフォームごとのロジックの違いを理解し、横断的に対応する体制を構築することが、2026年後半のLLMO戦略の競争優位を生む。</p>

<h2>まとめ</h2>

<p>ChatGPTとPerplexityの引用ドメイン重複率11%という事実は、LLMOが「単一プラットフォームの最適化」では不十分であることを突きつける。それぞれのプラットフォームが持つ引用ロジック——ChatGPTは第三者メンションと学習データ、Perplexityはリアルタイム検索とコンテンツ鮮度——に対応した施策を並行して実施することが必要だ。統計データの明記・パッセージ長の最適化・更新日の明示という3つの横断施策から着手し、自社のAI引用をマルチプラットフォームで測定しながら継続改善していきたい。</p>

<h2>参考情報</h2>
<ul>
  <li><a href="https://authoritytech.io/blog/how-to-get-cited-by-chatgpt-perplexity-ai-overview-2026" target="_blank" rel="noopener">How to Get Your Brand Cited by ChatGPT, Perplexity, and Google AI Overviews in 2026（AuthorityTech、2026年）</a></li>
  <li><a href="https://authoritytech.io/curated/ai-citation-11-percent-platform-overlap-per-engine-audit-2026" target="_blank" rel="noopener">ChatGPT and Perplexity Share Only 11% of Cited Domains（AuthorityTech、2026年）</a></li>
  <li><a href="https://quickseo.ai/blog/chatgpt-vs-perplexity-for-ai-visibility-in-2026-citations-traffic-and-conversion-compared" target="_blank" rel="noopener">ChatGPT vs Perplexity for AI Visibility in 2026（Quick SEO、2026年）</a></li>
  <li><a href="https://www.averi.ai/how-to/chatgpt-vs.-perplexity-vs.-google-ai-mode-the-b2b-saas-citation-benchmarks-report-(2026)" target="_blank" rel="noopener">ChatGPT vs. Perplexity vs. Google AI Mode: The B2B SaaS Citation Benchmarks Report 2026（Averi AI、2026年）</a></li>
  <li><a href="https://uravation.com/media/aio-llmo-technical-implementation-30-2026/" target="_blank" rel="noopener">【2026年最新】AIO/LLMO対策テクニカル30選｜AI検索流入を取りに行く実装ガイド（Uravation、2026年）</a></li>
</ul>
"""

# ── WordPress投稿関数 ──────────────────────────────────────────────────────────

def post_to_wordpress(title: str, content: str) -> dict:
    credentials = f"{WP_USER}:{WP_PASS}"
    token = base64.b64encode(credentials.encode()).decode()

    payload = json.dumps({
        "title": title,
        "content": content,
        "status": "draft",
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts",
        data=payload,
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "AIO-AutoPost/1.0",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def main():
    articles = [
        (ARTICLE_1_TITLE, ARTICLE_1_CONTENT),
        (ARTICLE_2_TITLE, ARTICLE_2_CONTENT),
        (ARTICLE_3_TITLE, ARTICLE_3_CONTENT),
    ]

    print("WordPress下書き投稿を開始します...\n")

    for i, (title, content) in enumerate(articles, 1):
        print(f"[{i}/3] 投稿中: {title[:50]}...")
        try:
            result = post_to_wordpress(title, content)
            post_id = result.get("id")
            post_link = result.get("link", "")
            print(f"  ✓ 投稿成功: ID={post_id}  URL={post_link}")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")
            print(f"  ✗ HTTPエラー: {e.code} {e.reason}\n  {body[:300]}")
            sys.exit(1)
        except Exception as e:
            print(f"  ✗ エラー: {type(e).__name__}: {e}")
            sys.exit(1)

    print("\n完了: 3記事を下書きとして投稿しました。")


if __name__ == "__main__":
    main()
