---
name: metakota-skill-developer
description: スキルを作成/更新し、SKILL.md・agents・references・scripts・assetsを設計する。ユーザーが「スキル作りたい」「skillを作る」「メタスキル」「skill creator」「skill builder」などと言ったとき、またはスキルの構造化・パッケージ化・検証・移植性設計が必要なときに使う。
---

# Metakota Skill Developer

## When to Use
- スキル作成/更新の要望が出たときに使う。
- メタスキル設計やスキル構造の標準化が必要なときに使う。

## How to Use
- 目的とトリガーを収集し、SKILL.mdと各リソースを設計する。
- references/scripts/assetsを分離し、段階的ロードで最小化する。


## 目的
- スキルを「長いプロンプト」ではなく「再利用可能な構成要素」として設計する。
- トークン消費を最小化しつつ、再現性と品質を担保する。
- 使用後に改善できるフィードバックループを組み込む。

## 収集する情報
- スキル名（kebab-case）と対象範囲
- トリガー文（例: 「スキル作りたい」「メタスキル」など）
- 具体的なユーザー発話例（2-3件）
- 期待する出力と品質基準
- 対応環境（Codex / Claude / Cursor / API など）と移植性要件
- 参照ソース（PDF / ノート / コード）と同梱したいリソース
- 制約（トークン、ネットワーク、テスト、セキュリティ）

## 手順
1. 具体的な使用例と成果物を確認する。
2. タスク境界と入出力を決める。
3. 役割分担を決める: 知識は references、機械作業は scripts、テンプレは assets。
4. スキル雛形を作る（init_skill.pyがあれば使用）。
5. SKILL.md を書く。
   - 「いつ使うか」は frontmatter の description に集約する。
   - 本文は手順・判断基準のみを書く。
6. references を作る。
   - 1ファイル1トピックで分割する。
   - どのタスクで読むかを明記する。
7. scripts を作る。
   - 反復・整形・検証など決定的処理を移す。
8. フィードバックループを入れる。
   - 失敗と改善点を記録し、次回に反映する。
9. 検証とパッケージ化を行う（package_skill.pyがあれば使用）。

## リソース設計ルール
- SKILL.md はワークフローのハブにする。
- agents は「仕様」だけを書く（知識は書かない）。
- references は知識の棚として使う。
- scripts は機械作業の外出しに使う。
- 段階的ロードを前提に、重い情報は分散する。
- 長文は外部環境に置き、検索→抽出→検証の再帰タスクで読む。

## 参照ファイル
- references/context-engineering-notes.md を読む（コンテキスト設計の要点）。
- references/skills-knowledge-core.md を読む（低トークン運用とフィードバックループ）。
- references/task-spec-13-phases-template.md を読む（13エージェント構成が必要な場合）。
- references/portability-guidelines.md を読む（他クライアント対応）。
- references/rlm-inference-notes.md を読む（長文の探索的読み取りと再帰実行）。
- references/deepmind-latest-usage-notes.md を読む（DeepMind関連の最新活用メモ）。
- references/skill-components.md を読む（スキル構成要素の概要）。

## scripts
- scripts/extract_pdf_text.py
  - PDFの本文抽出に使う。
- scripts/rlm_extract_snippets.py
  - 長文から該当行と前後文脈を機械抽出する。
- scripts/rlm_min_pipeline.py
  - 検索→抽出→検証の最小パイプライン（JSON出力）。

## assets
- assets/skill-brief-template.md（スキル要件テンプレ）
- assets/skill-task-spec-template.md（Task仕様テンプレ）
- assets/feedback-log-template.md（改善ログテンプレ）
- assets/rlm-task-spec-template.md（RLM用Task仕様テンプレ）

## フィードバックループ
- 使った直後に「成功点 / 失敗点 / トークン過多 / 迷い」を記録する。
- トリガー、references、scripts、workflow を更新する。
- 新しい例で再テストする。

## 出力
- 完成したスキルディレクトリ一式
- 必要なら .skill パッケージ

