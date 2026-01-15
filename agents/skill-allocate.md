# Phase 3: Allocate（配分）

## 役割
実行順序と担当（エージェント/手作業/スクリプト）を明確化し、最小コストで回すための割当計画を作る。

## 入力
- Designの結果（タスク境界、scripts/assets候補、連携仕様）

## 出力
```yaml
allocation_plan:
  version: 1
  steps:
    - phase: "Discovery|Design|Allocate|Implementation|Review|Feedback"
      agent: "agents/skill-*.md|human|script"
      inputs: ["path/to/input"]
      outputs: ["path/to/output"]
      stop: "completion criteria"
  review_gate:
    script: "scripts/validate_skill_structure.py"
    required: true
```

## 配分ルール
- 1フェーズ=1担当を基本にする（迷いを減らす）
- 検証はスクリプト優先（LLM判断を減らす）
- 連鎖呼び出しは2段以上にしない

## チェック項目
- [ ] 各フェーズの担当が明記されているか
- [ ] 入出力と停止条件が明確か
- [ ] 自動検証のゲートが設定されているか
- [ ] allocation-plan.yaml が作成されているか

## 制約
- 実行順序を最小ステップに圧縮する
- LLM呼び出し回数が増える割当を避ける

## 参照
- assets/allocation-plan-template.yaml
- references/skill-handoff.md
