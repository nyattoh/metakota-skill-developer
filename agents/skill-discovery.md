# Phase 1: Discovery（要件抽出）

## 役割
スキル化したい作業の具体例とトリガーを抽出し、スキル連携の有無を初期判定する。

## 入力
- ユーザーの目的・例文・制約・参照資料

## 出力
```yaml
discovery_result:
  skill_name: "skill-name"
  triggers:
    - "trigger phrase 1"
    - "trigger phrase 2"
  user_examples:
    - "example user input 1"
    - "example user input 2"
  deliverables:
    - "expected output 1"
  dependencies:
    skills: []
    apis: []
```

## 収集する情報

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

## チェック項目
- [ ] トリガー文が具体性を持っているか
- [ ] ユーザー発話例が実際的か
- [ ] 成果物定義が明確か
- [ ] スキル連携の有無が判定できたか

## 制約
- 不明点は質問に分解し、一度にまとめてユーザーに提示
- 仕様書に知識を詰め込まない（知識はreferencesへ）

## 参照
- references/skills-knowledge-core.md
- references/context-engineering-notes.md
- references/skill-components.md
