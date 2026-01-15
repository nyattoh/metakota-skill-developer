# metakota-skill-developer

## 概要
Codex用の「スキル作成/更新」メタスキル。SKILL.md を中心に、agents / references / scripts / assets を分離し、段階的ロードで再利用しやすいスキル構成を設計します。

## 特徴
- スキル構成要素を明確に分離し、再利用性を高める。
- 参照情報を references に集約し、必要なときだけ読む設計。
- scripts による抽出・整形・検証で作業を自動化。

## 動作要件
- Codex CLI（スキル読み込みに対応した環境）
- Git（履歴管理）
- Python 3（`scripts/` を使う場合）

## 使い方
1. `SKILL.md` の手順に従って、目的・トリガー・入出力を整理する。
2. 知識は `references/`、機械処理は `scripts/`、テンプレは `assets/` に分割する。
3. 必要に応じて `scripts/` を使い、抽出・整形・検証を自動化する。

## 参照論文/記事
| 論文/記事名 | URL | 備考 |
| --- | --- | --- |
| **Recursive Language Models** | https://arxiv.org/abs/2512.24601 | スレ主張のRLM（MIT側論文）。 |
| **RLM PDF** | https://arxiv.org/pdf/2512.24601 | 同上のPDF版。 |
| **RETRO Blog** | https://deepmind.google/blog/improving-language-models-by-retrieving-from-trillions-of-tokens/ | DeepMindの検索拡張モデル。 |
| **RAG（arXiv）** | https://arxiv.org/abs/2005.11401 | RAGの元論文。 |
| **Recursive Transformer (DeepMind)** | https://deepmind.google/research/publications/122290/ | 別系研究。 |

※ 詳細なメモは `references/rlm-inference-notes.md` を参照。
