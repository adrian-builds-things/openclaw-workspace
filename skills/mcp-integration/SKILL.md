---
name: mcp-integration
description: Integrate MCP servers into plugins and workflows (stdio/SSE/HTTP/WS), including auth, env vars, tool allowlists, and reliability checks. Use when wiring external tools/services via MCP.
---

# MCP Integration

Source: https://skills.sh/anthropics/claude-code/mcp-integration

## Core guidance
- Prefer portable paths and env expansion.
- Configure secure auth (OAuth/tokens/env vars) without hardcoding secrets.
- Use specific MCP tool allowlists instead of broad wildcards.
- Add graceful handling for connection/auth/tool failures.

## Validation checklist
- Config syntax valid and documented.
- Required env vars listed.
- Tools visible and callable.
- Error/fallback flows tested.
