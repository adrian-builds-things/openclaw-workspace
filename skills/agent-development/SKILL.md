---
name: agent-development
description: Create and maintain autonomous agent definitions (frontmatter, trigger examples, system prompts, tool scopes, model settings). Use when building Claude Code style agents for focused subprocess work.
---

# Agent Development

Source: https://skills.sh/anthropics/claude-code/agent-development

## Agent file standards
- Strong frontmatter: `name`, `description`, `model`, `color`, optional `tools`.
- Description includes concrete trigger examples and commentary.
- System prompt defines role, responsibilities, process, output format, edge cases.

## Best practices
- Use least-privilege tool sets.
- Prefer `model: inherit` unless special needs.
- Test triggering quality with realistic prompts.
- Keep agent identity specific, not generic.
