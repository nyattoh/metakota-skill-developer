# Phase 4: Implementation（実装）

## 役割
SKILL.mdとreferences/scripts/assetsを実装し、スキル連携テンプレと呼び出し規約を反映する。

## 入力
- Allocateの結果（allocation-plan.yaml）
- Designの結果（設計案、参照資料）

## 出力
- SKILL.md
- references/*.md
- scripts/*.py
- assets/*

## 実装順序
1. SKILL.mdの作成
2. references/*.mdの作成
3. scripts/*.pyの作成（必要なら）
4. assets/*の作成（必要なら）

## SKILL.mdの構造
```yaml
---
name: skill-name
description: いつ使うかを簡潔に記述
---
本文: 手順・判断基準のみ
```

## 実装制約
| 項目 | 制約 |
|------|------|
| frontmatter | nameとdescriptionのみ |
| SKILL.md本文 | 手順と判断基準のみ、知識は書かない |
| references | 1ファイル1トピック、読み込みタイミング明記 |
| scripts | 決定的処理のみ、エラーハンドリング含む |
| assets | テンプレート形式、使用例を含む |

## チェック項目
- [ ] frontmatterが正しいか
- [ ] SKILL.md本文が手順中心か
- [ ] referencesが1ファイル1トピックか
- [ ] 読み込みタイミングが明記されているか
- [ ] scriptsが決定的処理のみか
- [ ] assetsがテンプレート形式か

## 参照
- references/skills-knowledge-core.md
- references/context-engineering-notes.md
- references/skill-handoff.md
- references/portability-guidelines.md
