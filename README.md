# metakota-skill-developer

## 概要
Claudeに限らず、**スキル設計やメタスキル運用**に使える汎用スキルです。SKILL.md を中心に、agents / references / scripts / assets を分離し、段階的ロードで再利用しやすいスキル構成を設計します。

## 特徴
- スキル構成要素を明確に分離し、再利用性を高める。
- 参照情報を references に集約し、必要なときだけ読む設計。
- scripts による抽出・整形・検証で作業を自動化。

## 動作要件
- スキル読み込みに対応したクライアント（Codex / Gemini / Claude / Cursor など）
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

### スラッシュコマンドが使える場合
クライアントがスラッシュコマンドやエイリアス登録に対応しているなら、以下のように登録して起動します。
- `/metakota`
- `/metakota-skill`

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

## ライセンス
MIT
