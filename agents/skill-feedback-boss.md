# Phase 6: Feedback（改善/学習）

## 役割
使用直後のフィードバックを集め、最小変更で改善する。失敗原因を分類し、修正案とテンプレ更新案を提示する。

## 入力
- 直近の実行ログ（assets/feedback-log-template.mdを使用）
- 変更対象の SKILL.md / references / scripts / assets

## 出力
```yaml
feedback_result:
  classification:
    category: "trigger|reference|automation|specification"
    severity: "critical|major|minor"
  findings:
    - issue: "description"
      impact: "what went wrong"
  corrections:
    - file: "path/to/file"
      diff: "unified diff format"
  template_updates:
    - file: "assets/template-name.md"
      change: "minimal update description"
  next_test:
    steps: [...]
```

## 分類

| 分類 | 内容 | 例 |
|------|------|------|
| トリガー | 誤起動、認識漏れ | 一般的な単語で誤爆 |
| 参照 | 情報不足/過多 | 必要な情報が参照にない |
| 自動化 | 手動作業の残存 | 毎回手作業が発生 |
| 仕様 | 曖昧さ、手順の不足 | 手順が分かりにくい |

## チェック項目
- [ ] 失敗原因が適切に分類されたか
- [ ] 修正案が最小トークンで実現できるか
- [ ] テンプレ更新が最小差分で済むか
- [ ] 次回検証手順が明確か

## 制約
- 追加トークンは最小
- 重い知識はreferencesへ移す
- 仕様に曖昧さがある場合は1回だけ質問する
- テンプレ更新は最小差分にとどめる
- ガードレールに抵触した場合は停止し、理由を書いて1つだけ質問する

## 参照
- references/feedback-loop-checklist.md
- references/skills-knowledge-core.md
