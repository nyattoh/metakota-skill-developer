# Phase 2: Design（構造設計）

## 役割
タスク境界とリソース分割（references/scripts/assets）を設計し、スキル連携のハンドオフ仕様を定義する。

## 入力
- Discoveryの結果（具体例、品質基準、制約、環境要件）

## 出力
```yaml
design_result:
  task_breakdown:
    - phase: "Discovery|Design|Implementation|Review|Feedback"
      tasks: [...]
  references_structure:
    - file: "references/topic-name.md"
      load_timing: "Phase X"
  scripts:
    - name: "script-name.py"
      purpose: "automated task"
  assets:
    - name: "template-name.md"
      purpose: "template for..."
  handoff_spec:
    calls: []
    receives: []
```

## 設計項目
- タスク境界と入出力の定義
- 参照ファイル構成（何をreferences/に置くか）
- scripts候補（何を自動化するか）
- assets候補（どんなテンプレが必要か）
- 連携仕様（他スキルへのハンドオフ方法）

## 設計原則
| 原則 | 内容 |
|------|------|
| 1ファイル1トピック | referencesはトピックごとに分割 |
| 知識はreferencesへ | 重い知識はSKILL.mdに書かない |
| 決定的処理はscriptsへ | 反復・整形・検証を自動化 |
| 再利用可能なパターンはassetsへ | テンプレートとして外出し |

## チェック項目
- [ ] タスク境界が明確か
- [ ] 知識と仕様の分離が計画されているか
- [ ] 必要なscriptsが特定されているか
- [ ] 連携仕様が定義されているか

## 制約
- 1ファイル1トピックを守る
- 重い知識はreferencesへ移す
- スキル連携は2段以上の連鎖を避ける

## 参照
- references/context-engineering-notes.md
- references/portability-guidelines.md
- references/skill-handoff.md
