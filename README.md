# metakota-skill-developer

## 概要
Codexに限らず、**スキル設計やメタスキル運用**に使える汎用スキルです。SKILL.md を中心に、agents / references / scripts / assets を分離し、段階的ロードで再利用しやすいスキル構成を設計します。

## 特徴
- スキル構成要素を明確に分離し、再利用性を高める。
- 参照情報を references に集約し、必要なときだけ読む設計。
- scripts による抽出・整形・検証で作業を自動化。

## 動作要件
- スキル読み込みに対応したクライアント（Codex / Gemini / Claude など）
- Git（更新・履歴管理）
- Python 3（`scripts/` を使う場合）

## セットアップ
### 1) 置き場所の決定
各クライアントの「スキル検索ディレクトリ」に、このリポジトリを**1フォルダ分**配置します。
以下は**よくある例**です（実際のパスは各クライアントの設定に従ってください）。

- Windows（例）
  - Codex: `C:\Users\<User>\.codex\skills\metakota-skill-developer\`
  - Gemini: `C:\Users\<User>\.gemini\skills\metakota-skill-developer\`
  - それ以外: `C:\Users\<User>\.ai-skills\metakota-skill-developer\` など
- macOS / Linux（例）
  - Codex: `~/.codex/skills/metakota-skill-developer/`
  - Gemini: `~/.gemini/skills/metakota-skill-developer/`
  - それ以外: `~/.ai-skills/metakota-skill-developer/` など

※ クライアント側に「スキルディレクトリの設定」がある場合は、親ディレクトリ（`.../skills/`）を指定してください。

### 2) ダウンロード方法
#### ZIPで取得する場合
1. GitHubの「Code → Download ZIP」を使ってダウンロード。
2. 解凍して、上記のスキルディレクトリ配下に配置。
3. フォルダ名が `metakota-skill-developer` になるよう調整。

#### Gitで取得する場合
```bash
git clone https://github.com/nyattoh/metakota-skill-developer.git
```
- クライアントが読み込む `.../skills/` の直下に配置します。

### 3) 最終的なディレクトリ構造
```
metakota-skill-developer/
  SKILL.md
  agents/
  assets/
  references/
  scripts/
```

## 使い方（トリガーと起動）
### 推奨トリガー
他のスキルと衝突しにくい**固有トリガー**を推奨します。
- `metakota`
- `metakota-skill`
- `metakota-skill-developer`

### スラッシュコマンド / エイリアス（クライアント別）
クライアントが**カスタムコマンド**に対応している場合、`/metakota` のような短い呼び出しを作れます。
以下は代表的な例です（詳細は各公式ドキュメント参照）。

#### Gemini CLI
- コマンド定義は `~/.gemini/commands/`（グローバル）か、`<project>/.gemini/commands/`（プロジェクト）
- `.toml` で定義し、ファイル名が `/コマンド名` になる

最小例（`~/.gemini/commands/metakota.toml`）:
```toml
prompt = "metakota でスキル構成を設計して。SKILL.md と agents/references/scripts/assets を分離して提案して。"
```

#### Claude Code
- コマンド定義は `~/.claude/commands/`（個人）か、`<project>/.claude/commands/`（プロジェクト）
- `.md` で定義し、ファイル名が `/コマンド名` になる

最小例（`~/.claude/commands/metakota.md`）:
```
metakota でスキル構成を設計して。SKILL.md と agents/references/scripts/assets を分離して提案して。
```

### 本当に起動するかの確認方法
1. チャット入力で `/` を打ち、`metakota` が一覧に出るか確認。
2. 一覧から選ぶか `/metakota` を実行して反応を見る。
3. 出てこない場合は、配置場所・ファイル名・拡張子を再確認。

### 通常の指示例（コマンド非対応の環境）
- 「metakota を使ってスキル構成を設計して」
- 「metakota-skill-developer として、SKILL.md を作って」
- 「metakota でスキルの構造を見直して」

## 参照論文/記事
| 論文/記事名 | URL | 備考 |
| --- | --- | --- |
| **Recursive Language Models** | https://arxiv.org/abs/2512.24601 | スレ主張のRLM（MIT側論文）。 |
| **RLM PDF** | https://arxiv.org/pdf/2512.24601 | 同上のPDF版。 |
| **RETRO Blog** | https://deepmind.google/blog/improving-language-models-by-retrieving-from-trillions-of-tokens/ | DeepMindの検索拡張モデル。 |
| **RAG（arXiv）** | https://arxiv.org/abs/2005.11401 | RAGの元論文。 |
| **Recursive Transformer (DeepMind)** | https://deepmind.google/research/publications/122290/ | 別系研究。 |

※ 詳細なメモは `references/rlm-inference-notes.md` を参照。

## 参考（コマンド定義の公式ドキュメント）
- Gemini CLI Custom Commands: https://geminicli.com/docs/cli/custom-commands/
- Claude Code Slash Commands: https://docs.claude.com/en/docs/claude-code/slash-commands
- Claude Code SDK Slash Commands: https://docs.claude.com/en/docs/claude-code/sdk/sdk-slash-commands

## ライセンス
MIT
