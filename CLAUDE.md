# AIOネタ自動下書き投稿 Routine

## 目的
AIO（AI最適化）・GEO・LLMO関連の最新情報を週1回収集し、aiotaisaku.comに下書きとして3記事投稿する。

## 実行手順

### Step 1：情報収集（英語・日本語の両方で検索）

以下の英語キーワード10個で検索し、直近7日以内の海外情報を優先して収集する：

1. "AI search optimization 2026"
2. "LLM visibility SEO latest"
3. "Google AI Mode update"
4. "ChatGPT search engine optimization"
5. "Generative Engine Optimization GEO"
6. "AI Overviews Google ranking"
7. "Claude Gemini search citation"
8. "LLMO strategy 2026"
9. "AI answer engine optimization"
10. "Perplexity Bing Copilot SEO impact"

加えて、以下の日本語キーワードでも検索する：
- 「AIO対策 2026」
- 「AI検索最適化 最新」
- 「LLMO AIO 事例」

### Step 2：記事テーマの選定

収集した情報から、以下の配分で3つのトピックを選ぶ：
- **記事1**：海外情報ベース（英語ソースから）
- **記事2**：海外情報ベース（英語ソースから）
- **記事3**：国内情報ベース（日本語ソースから、または海外情報の日本向け解説）

3記事が似たような内容・切り口にならないよう、異なる視点を選ぶこと。

### Step 3：記事の作成（3記事）

各記事を以下の形式で作成する：

**タイトル：**
- 具体的でSEOを意識したもの
- 数字・年月・固有名詞を含める
- 例：「Google AI Mode、2026年5月アップデートで検索結果が激変——AIO対策の新常識とは」

**本文：3000文字以上**を以下の構成で書く：

1. 導入（200文字）：読者の悩みや疑問を提示
2. 背景・概要（500文字）：トピックの背景と重要性
3. 詳細解説（1500文字）：具体的な内容をh2/h3見出しで整理
4. 実践・活用方法（500文字）：読者がすぐ試せる内容
5. まとめ（200文字）：要点の整理と次のアクション

**情報ソースの記載（必須）：**
記事末尾に「参考情報」セクションを設け、引用した情報ソースをリンク付きで記載する。
形式：
```
<h2>参考情報</h2>
<ul>
  <li><a href="https://実際のURL" target="_blank" rel="noopener">記事タイトル（サイト名、公開日）</a></li>
  <li><a href="https://実際のURL" target="_blank" rel="noopener">記事タイトル（サイト名、公開日）</a></li>
</ul>
```

**ステータス：** 必ず `draft`（下書き）で投稿

### Step 4：WordPress REST APIで3記事を下書き投稿

- エンドポイント：https://aiotaisaku.com/wp-json/wp/v2/posts
- 認証：.envファイルのWP_CREDENTIALSを使用
- status: "draft" を必ず指定
- 3記事を順番に投稿する

## 注意事項

- 同じ記事を重複投稿しない（タイトルで判断）
- 必ず下書きとして投稿する（公開しない）
- 日本語で記事を書く（ソースが英語でも記事本文は日本語）
- 3記事それぞれ異なるテーマ・切り口にする
- 以前、投稿したのと似たテーマ・切り口のものは避ける
- 「AIOとは」「LLMOが求められている理由」など、読者がすでに知っている基本的な内容は書かない
- 箇条書きだけでなく、説明文の段落も充実させる
- 参考情報のリンクは実在するURLのみ記載する（架空のURLは絶対に入れない）
