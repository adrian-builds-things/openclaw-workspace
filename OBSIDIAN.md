# OBSIDIAN.md

## Canonical Vault (no-copy setup)

**Vault root:** `/home/adrian/.openclaw/workspace`

Damit nutzen wir die bestehenden Default-Ordner direkt als Obsidian-Vault (ohne ständiges Hin- und Herkopieren).

## Navigation-Layer (nur Symlinks, keine Duplikate)

Für saubere Obsidian-Navigation gibt es zusätzlich folgende Alias-Ordner:

- `01-memory -> memory`
- `02-projects -> plans`
- `03-content -> content`
- `04-reference -> knowledge`
- `05-systems -> tools`
- `99-archive -> archive`

Diese Symlinks zeigen auf die echten Quellordner.

## Single Source of Truth

- Erinnerungen: `MEMORY.md`, `memory/*.md`
- Agent-Identität/Regeln: `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`
- Planungs- und Projektwissen: `plans/`, `content/`, `knowledge/`
- Betriebs-/Toolwissen: `tools/`, `scripts/`

## Regeln gegen Chaos

1. **Keine zweite Wissenskopie anlegen** (kein zusätzliches Spiegeln in Parallel-Vaults).
2. Neue Wissens-Markdowns immer in einen der Source-Ordner einordnen (siehe `OBSIDIAN_ROUTING.md`).
3. `knowledge-vault/` gilt als Altbestand/Legacy und ist **nicht** die primäre Quelle.
4. Strukturänderungen immer zuerst in `OBSIDIAN_ROUTING.md` dokumentieren.

## Obsidian auf dem Mac

Öffne auf dem Mac den per Syncthing synchronisierten Ordner, der auf diesen Serverpfad zeigt.
Dann arbeitet Obsidian direkt auf denselben Dateien wie OpenClaw.
