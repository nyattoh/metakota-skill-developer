---
name: metakota-skill-developer
description: スキルを作成/更新し、SKILL.md・agents・references・scripts・assetsを設計する。スキル連携や低トークン化の設計が必要なとき、または「metakota」で始まる明示的な指示があるときに使う。
---

# Metakota Skill Developer

## 目的
- スキルを「長いプロンプト」ではなく「再利用可能な構成要素」として設計する。
- トークン消費を最小化しつつ、再現性と品質を担保する。
- 使用後に改善できるフィードバックループを組み込む。
- スキル連携/サブエージェント設計をスキルに組み込む。

## 収集する情報
- スキル名（kebab-case）と対象範囲
- トリガー文（例: 「metakota でスキル設計」などの固有呼び出し）
- 具体的なユーザー発話例（2-3件）
- 期待する出力と品質基準
- 対応環境（Codex / Claude / Gemini / API など）と移植性要件
- 参照ソース（PDF / ノート / コード）と同梱したいリソース
- スキル連携の対象・依存関係・ハンドオフ方法
- 制約（トークン、ネットワーク、テスト、セキュリティ）

## 手順
1. 具体的な使用例と成果物を確認する。
2. タスク境界と入出力を決める。
3. スキル連携の有無を決め、ハンドオフ仕様を定義する。
4. 役割分担を決める: 知識は references、機械作業は scripts、テンプレは assets。
5. スキル雛形を作る（init_skill.pyがあれば使用）。
6. SKILL.md を書く。
   - 「いつ使うか」は frontmatter の description に集約する。
   - 本文は手順・判断基準のみを書く。
7. references を作る。
   - 1ファイル1トピックで分割する。
   - どのタスクで読むかを明記する。
8. scripts を作る。
   - 反復・整形・検証など決定的処理を移す。
9. フィードバックループを入れる。
   - 失敗と改善点を記録し、次回に反映する。
10. 検証とパッケージ化を行う（package_skill.pyがあれば使用）。

## リソース設計ルール
- SKILL.md はワークフローのハブにする。
- agents は「仕様」だけを書く（知識は書かない）。
- references は知識の棚として使う。
- scripts は機械作業の外出しに使う。
- 段階的ロードを前提に、重い情報は分散する。
- 長文は検索→抽出→検証→統合の再帰タスクで読む。

## スキル連携ルール
- 呼び出しは `assets/skill-call-template.md` の形式で統一する。
- 2段以上の連鎖呼び出しは避ける。
- Claude Code では subagent frontmatter の `skills` でスキル連携できる（詳細は references/subagent-usage.md）。

## 参照ファイル
- references/context-engineering-notes.md（コンテキスト設計の要点）
- references/skills-knowledge-core.md（低トークン運用とフィードバックループ）
- references/task-spec-13-phases-template.md（13エージェント構成が必要な場合）
- references/portability-guidelines.md（他クライアント対応）
- references/rlm-inference-notes.md（長文の探索的読み取りと再帰実行）
- references/long-context-retrieval-notes.md（RLM/RAG/RETRO/Recursive Transformer要点）
- references/subagent-usage.md（サブエージェント/コマンド呼び出し）
- references/skill-handoff.md（スキル連携の最小プロトコル）
- references/deepmind-latest-usage-notes.md（DeepMind関連の最新活用メモ）
- references/skill-components.md（スキル構成要素の概要）

## agents
- agents/skill-discovery.md（要件・トリガー抽出）
- agents/skill-design.md（リソース分割・連携設計）
- agents/skill-implementation.md（SKILL.md / resources 実装）
- agents/skill-review.md（品質・移植性・連携のレビュー）
- agents/skill-feedback-boss.md（フィードバック収集と最小修正）

## scripts
- scripts/extract_pdf_text.py（PDF本文抽出）
- scripts/rlm_extract_snippets.py（該当行と前後文脈抽出）
- scripts/rlm_min_pipeline.py（検索→抽出→検証の最小パイプライン）

## assets
- assets/skill-brief-template.md（スキル要件テンプレ）
- assets/skill-task-spec-template.md（Task仕様テンプレ）
- assets/feedback-log-template.md（改善ログテンプレ）
- assets/rlm-task-spec-template.md（RLM用Task仕様テンプレ）
- assets/skill-call-template.md（スキル連携テンプレ）

## フィードバックループ
- 使った直後に「成功点 / 失敗点 / トークン過多 / 迷い」を記録する。
- agents/skill-feedback-boss.md で最小修正案をまとめる。
- トリガー、references、scripts、workflow を更新する。
- 新しい例で再テストする。

## 出力
- 完成したスキルディレクトリ一式
- 必要なら .skill パッケージ
