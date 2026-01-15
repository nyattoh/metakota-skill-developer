# Subagent / Command Invocation Notes (Client-Specific)

## Claude Code
- `/agents` でサブエージェント（Subagents）を管理できる。
- サブエージェントは Markdown + YAML frontmatter で定義する。
- 保存場所（優先順位あり）:
  - `.claude/agents/`（プロジェクト）
  - `~/.claude/agents/`（ユーザー）
- frontmatter で `skills` を指定すると、サブエージェント起動時にスキルをロードできる（**スキル連携の実装手段**）。
- Slash commands は `.claude/commands/` または `~/.claude/commands/` に置き、`/command` で呼び出す。
- `SlashCommand` ツールは **user-defined** コマンドのみ実行可能で、`description` を必須とする。

### Minimal subagent format
```
---
name: skill-feedback-boss
description: Collects feedback and applies minimal edits to improve skill quality.
# tools: Read, Glob, Grep (optional)
# model: sonnet (optional)
# skills: [metakota-skill-developer] (optional)
---
<system prompt>
```

### Minimal command format
```
---
description: Brief description
---
Your instructions here.
```

## Codex CLI (OpenAI)
- Codex は **custom prompts** を `/prompts:<name>` として呼び出せる。
- 置き場所は `~/.codex/prompts/` の直下（Markdownのみ）。
- **サブエージェント機能は公式には記載なし**。代替はカスタムプロンプトと明示的タスク分割。

### Minimal prompt format
```
---
description: Short summary
argument-hint: [KEY=value]
---
Your reusable instructions here.
```

## Gemini CLI
- コマンドは `.toml` で定義し、`~/.gemini/commands/`（グローバル）か `<project>/.gemini/commands/`（ローカル）から読み込む。
- コマンド名はパスから決まり、`/command` で実行する。
- **サブエージェント機能は公式には記載なし**。代替はコマンド化と明示的タスク分割。

### Minimal command format
```toml
description = "Brief summary"
prompt = """
Your reusable instructions here.
"""
```

## Sources
- Claude Code slash commands & SlashCommand tool: https://code.claude.com/docs/en/slash-commands
- Claude Code subagents (paths, frontmatter, skills): https://code.claude.com/docs/en/sub-agents
- Codex CLI custom prompts & slash commands: https://developers.openai.com/codex/custom-prompts
- Codex CLI slash commands: https://developers.openai.com/codex/cli/slash-commands
- Gemini CLI custom commands: https://geminicli.com/docs/cli/custom-commands/
