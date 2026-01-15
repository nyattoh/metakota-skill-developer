# Phase 4: Review（レビュー）

## 役割
構造・トリガー・移植性・トークン効率をレビューし、スキル連携の手順とテンプレが守られているかを確認する。

## 入力
- 完成したスキル一式

## 出力
```yaml
review_result:
  passed: true/false
  findings:
    critical: []
    major: []
      - issue: "description"
        location: "file:line"
        fix: "correction"
    minor: []
  recommendations: [...]
```

## レビュー観点

| 観点 | 確認内容 |
|------|----------|
| 構造 | 仕様/知識/自動化の分離が正しいか |
| トリガー | 明確で競合しないか |
| 移植性 | 複数クライアント対応できているか |
| トークン効率 | 冗長な記述がないか |
| 連携 | スキル連携の手順が守られているか |
| assets | 有無と用途が適切か |

## チェック項目
- [ ] 仕様/知識/自動化の分離が崩れていないか
- [ ] assetsの有無と用途が適切か
- [ ] 全てのレビュー観点をパスしたか
- [ ] 指摘事項がすべて対応されたか

## 制約
- 仕様/知識/自動化の分離が崩れていないか確認する
- assetsの有無と用途を確認する
- 重要度順に指摘事項をまとめる

## 参照
- references/feedback-loop-checklist.md
- references/portability-guidelines.md
- references/skill-handoff.md
