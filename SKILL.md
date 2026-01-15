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

## 原則
- **分離**: 知識はreferences、仕様はSKILL.md/agents、機械作業はscripts、テンプレはassets
- **段階的ロード**: 必要な情報だけを必要なタイミングで読む
- **統一ハンドオフ**: スキル連携は統一的なプロトコルで行う
- **最小トークン**: 実行に必要な情報だけを残し、知識はreferencesへ
- **Fail-Closed**: 検証に失敗したら停止し、理由を書いて1つだけ質問する

---

## ガードレール（TDD的ゲート）
- すべてのフェーズ開始前に `scripts/preflight.py` を実行する
- Allocate完了後に `scripts/validate_phase_output.py --require allocation-plan.yaml` を実行する
- Reviewで `scripts/validate_skill_structure.py` を実行する
- いずれかがFAILなら**必ず停止**し、理由を短く書いて**1つだけ質問**する

---

## ワークフロー（6フェーズ）

### Phase 1: Discovery（要件抽出）
**いつ実行**: ユーザーからスキル作成依頼があった場合

**収集する情報**:
| 項目 | 内容 |
|------|------|
| スキル名 | kebab-case、対象範囲 |
| トリガー文 | 2-5件（固有で分かりやすい言葉） |
| ユーザー発話例 | 2-3件（実際の使い方） |
| 成果物 | 期待する出力、品質基準 |
| 対応環境 | Codex/Claude/Gemini/API、移植性要件 |
| 参照ソース | PDF/ノート/コード、同梱リソース |
| 連携先 | 依存関係、ハンドオフ方法 |
| 制約 | トークン、ネットワーク、テスト、セキュリティ |

**出力**: スキル名案、トリガー、ユーザー発話、成果物定義、連携有無

**チェック項目**:
- [ ] トリガー文が具体性を持っているか
- [ ] ユーザー発話例が実際的か
- [ ] 成果物定義が明確か
- [ ] スキル連携の有無が判定できたか

詳細: `agents/skill-discovery.md`

---

### Phase 2: Design（構造設計）
**いつ実行**: Discovery完了後

**設計項目**:
- タスク境界と入出力の定義
- 参照ファイル構成（何をreferences/に置くか）
- scripts候補（何を自動化するか）
- assets候補（どんなテンプレが必要か）
- 連携仕様（他スキルへのハンドオフ方法）

**設計原則**:
- 1ファイル1トピック
- 重い知識はreferencesへ
- 決定的処理はscriptsへ
- 再利用可能なパターンはassetsへ

**出力**: タスクリスト、参照ファイル構成案、scripts/assets候補、連携仕様

**チェック項目**:
- [ ] タスク境界が明確か
- [ ] 知識と仕様の分離が計画されているか
- [ ] 必要なscriptsが特定されているか
- [ ] 連携仕様が定義されているか

詳細: `agents/skill-design.md`

---

### Phase 3: Allocate（配分）
**いつ実行**: Design完了後

**目的**:
- 実行順序と担当（エージェント/手作業/スクリプト）を明確化する
- 迷いを減らし、LLM呼び出し回数を増やさない

**出力**: allocation-plan.yaml（配分計画）

**ゲート**:
- `scripts/validate_phase_output.py --require allocation-plan.yaml`

**チェック項目**:
- [ ] 各フェーズの担当が明記されているか
- [ ] 入出力と停止条件が明確か
- [ ] 自動検証のゲートが設定されているか

詳細: `agents/skill-allocate.md`

---

### Phase 4: Implementation（実装）
**いつ実行**: Allocate完了後

**実装順序**:
1. SKILL.mdの作成
2. references/*.mdの作成
3. scripts/*.pyの作成（必要なら）
4. assets/*の作成（必要なら）

**SKILL.mdの構造**:
```yaml
---
name: skill-name
description: いつ使うかを簡潔に記述
---
本文: 手順・判断基準のみ
```

**制約**:
- frontmatterはnameとdescriptionのみ
- 本文は手順と判断基準のみ、知識は書かない
- referencesは1ファイル1トピック、読み込みタイミング明記

**出力**: SKILL.md、references、scripts、assets

**チェック項目**:
- [ ] frontmatterが正しいか
- [ ] SKILL.md本文が手順中心か
- [ ] referencesが1ファイル1トピックか
- [ ] 読み込みタイミングが明記されているか

詳細: `agents/skill-implementation.md`

---

### Phase 5: Review（レビュー）
**いつ実行**: Implementation完了後

**レビュー観点**:
| 観点 | 確認内容 |
|------|----------|
| 構造 | 仕様/知識/自動化の分離が正しいか |
| トリガー | 明確で競合しないか |
| 移植性 | 複数クライアント対応できているか |
| トークン効率 | 冗長な記述がないか |
| 連携 | スキル連携の手順が守られているか |
| assets | 有無と用途が適切か |

**自動検証**: `scripts/validate_skill_structure.py` を実行して構造検証を行う

**出力**: 指摘事項（重要度順）、修正案、パッケージ化

**チェック項目**:
- [ ] 全てのレビュー観点をパスしたか
- [ ] 指摘事項がすべて対応されたか
 - [ ] 自動検証をパスしたか

詳細: `agents/skill-review.md`

---

### Phase 6: Feedback（改善/学習）
**いつ実行**: スキル使用後、改善が必要な場合

**分類**:
| 分類 | 内容 |
|------|------|
| トリガー | 誤起動、認識漏れ |
| 参照 | 情報不足/過多 |
| 自動化 | 手動作業の残存 |
| 仕様 | 曖昧さ、手順の不足 |

**改善原則**:
- 追加トークンは最小
- 重い知識はreferencesへ移動
- 仕様の曖昧さがある場合は1回だけ質問
- assetsテンプレとチェックリストを最小修正で更新する

**出力**: 指摘事項、修正案（差分）、次回検証用テスト手順、テンプレ更新案

詳細: `agents/skill-feedback-boss.md`

---

## スキル構成要素

| ディレクトリ | 内容 | 原則 |
|-------------|------|------|
| SKILL.md | ワークフローのハブ | 手順・判断基準のみ、知識は書かない |
| agents/ | 各フェーズの仕様 | 仕様だけを書く、知識はreferencesへ |
| references/ | 知識の棚 | 1ファイル1トピック、どのタスクで読むか明記 |
| scripts/ | 機械作業 | 反復・整形・検証などの決定的処理 |
| assets/ | テンプレート | 雛形・フォーマット定義 |

---

## スキル連携ルール
- 呼び出しは `assets/skill-call-template.md` の形式で統一する
- 2段以上の連鎖呼び出しは避ける
- Claude Code では subagent frontmatter の `skills` でスキル連携できる
- 詳細: `references/skill-handoff.md`

---

## 参照ファイル

| ファイル | 内容 | 使用フェーズ |
|----------|------|-------------|
| references/context-engineering-notes.md | コンテキスト設計の要点 | Design, Implementation |
| references/skills-knowledge-core.md | 低トークン運用とフィードバックループ | 全フェーズ |
| references/task-spec-13-phases-template.md | 13エージェント構成テンプレ | Design |
| references/portability-guidelines.md | 他クライアント対応 | Design, Review |
| references/rlm-inference-notes.md | 長文の探索的読み取り | Discovery, Implementation |
| references/long-context-retrieval-notes.md | RLM/RAG/RETRO要点 | Design |
| references/subagent-usage.md | サブエージェント/コマンド呼び出し | Design |
| references/skill-handoff.md | スキル連携の最小プロトコル | Design, Implementation |
| references/deepmind-latest-usage-notes.md | DeepMind関連の最新活用メモ | Design |
| references/skill-components.md | スキル構成要素の概要 | Discovery |
| references/feedback-loop-checklist.md | フィードバック収集チェックリスト | Feedback |

---

## agents

### スキル開発用（5フェーズ）

| ファイル | 内容 |
|----------|------|
| agents/skill-discovery.md | Phase 1: 要件・トリガー抽出 |
| agents/skill-design.md | Phase 2: リソース分割・連携設計 |
| agents/skill-allocate.md | Phase 3: 配分計画の作成 |
| agents/skill-implementation.md | Phase 4: SKILL.md / resources 実装 |
| agents/skill-review.md | Phase 5: 品質・移植性・連携のレビュー |
| agents/skill-feedback-boss.md | Phase 6: フィードバック収集と最小修正 |

### メタプロンプト用（Operator/Guardian分離型）

| ファイル | 役割 | 内容 |
|----------|------|------|
| agents/meta-control.md | 協調制御 | Operator/Guardian の調整、One-Question Gate |
| agents/meta-guardian.md | 制御系 | 安全・ポリシー・コスト監視、プリセット選択 |
| agents/meta-operator.md | 実行系 | タスク実行、ツール利用、出力生成 |

**メタプロンプト構成**:
- Guardian が安全・コストを監視し、Operator に実行許可/制限を与える
- Operator は Guardian の許可のもとでタスクを実行
- 分離により役割が明確になり、コスト圧縮と保守性が向上

---

## scripts

| ファイル | 内容 |
|----------|------|
| scripts/extract_pdf_text.py | PDF本文抽出 |
| scripts/rlm_extract_snippets.py | 該当行と前後文脈抽出 |
| scripts/rlm_min_pipeline.py | 検索→抽出→検証の最小パイプライン |
| scripts/validate_skill_structure.py | 最小構造の自動検証 |
| scripts/preflight.py | 事前チェック（Fail-Closed） |
| scripts/validate_phase_output.py | フェーズ成果物の検証 |

---

## assets

| ファイル | 内容 |
|----------|------|
| assets/skill-brief-template.md | スキル要件テンプレ |
| assets/skill-task-spec-template.md | Task仕様テンプレ |
| assets/feedback-log-template.md | 改善ログテンプレ |
| assets/rlm-task-spec-template.md | RLM用Task仕様テンプレ |
| assets/skill-call-template.md | スキル連携テンプレ |
| assets/allocation-plan-template.yaml | 配分計画テンプレ |

---

## フィードバックループ
1. 使った直後に「成功点 / 失敗点 / トークン過多 / 迷い」を記録
2. `assets/feedback-log-template.md` を使用してログ化
3. Phase 5（Feedback）で最小修正案をまとめる
4. トリガー、references、scripts、workflow を更新
5. 新しい例で再テスト

---

## 出力
- 完成したスキルディレクトリ一式
- 必要なら .skill パッケージ
