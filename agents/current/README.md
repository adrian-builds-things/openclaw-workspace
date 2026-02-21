# Current Agents (Runtime Backup)

Dieser Ordner enthält einen **echten Snapshot** der aktuell laufenden Agent-Workspaces,
nicht nur Platzhalter.

Quelle je Agent:
- `main` -> `/home/adrian/.openclaw/workspace`
- `max|luna|rico|hunter|sherlock|zen|pixel|neo|ghost` -> `/home/adrian/.openclaw/workspace-<agent-id>`

Enthalten pro Agent (falls vorhanden):
- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `MEMORY.md`
- `.openclaw/workspace-state.json`

Zusätzlicher globaler Runtime-Snapshot:
- `config/runtime-snapshot/openclaw.redacted.json`
- `config/runtime-snapshot/cron-jobs.json`
- `config/runtime-snapshot/subagent-runs.json`
- `config/runtime-snapshot/devices-paired.json`

Hinweis: Secrets/Tokens wurden in `openclaw.redacted.json` automatisch geschwärzt.
