# metakota-skill-developer

## 概要
Codex用の「スキル作成/更新」メタスキル。SKILL.md を中心に、agents / references / scripts / assets を分離し、段階的ロードで再利用しやすいスキル構成を設計します。

## 使い方
1. `SKILL.md` の手順に従って、目的・トリガー・入出力を整理する。
2. 知識は `references/`、機械処理は `scripts/`、テンプレは `assets/` に分割する。
3. 必要に応じて `scripts/` を使い、抽出・整形・検証を自動化する。

## 参照論文
- Recursive Language Models (RLM)
- LongBench-v2 (CodeQA)
- BrowseComp-Plus
- OOLONG / OOLONG-Pairs
- S-NIAH

※ 詳細なメモは `references/rlm-inference-notes.md` を参照。
