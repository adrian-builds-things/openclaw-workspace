# OBSIDIAN_ROUTING.md

Diese Datei ist die verbindliche Ablage-Regel für OpenClaw im Workspace.

## Routing-Matrix

- `MEMORY.md` -> Langzeitgedächtnis (Root)
- `memory/YYYY-MM-DD.md` -> Tageslog / Kurzzeitkontext
- `00-inbox/` -> ungeordnete Eingänge
- `plans/` -> aktive Projekt- und Umsetzungspläne
- `content/` -> Content-Entwürfe, SEO, Copy
- `knowledge/` -> Referenzwissen, Research, extrahierte Quellen
- `tools/` -> operative Tool-Dokumentation, Integrationen, Runbooks
- `scripts/` -> Automationsskripte + technische Helfer
- `archive/` -> abgeschlossene oder alte Stände
- `.learnings/` (je Projekt) -> Lessons Learned / Fehler / Feature-Wünsche

## Entscheidungslogik (für neue Dateien)

1. Ist es eine tägliche Notiz/Status? -> `memory/`
2. Ist es dauerhaft wichtig für Kontext über Wochen/Monate? -> `MEMORY.md` (destilliert)
3. Ist es ein konkreter Umsetzungsplan? -> `plans/`
4. Ist es Marketing-/SEO-/Sales-Content? -> `content/`
5. Ist es Recherche oder Nachschlagewissen? -> `knowledge/`
6. Ist es Tooling, Setup, Betrieb oder SOP? -> `tools/`
7. Ist es ausführbarer Code/Automation? -> `scripts/`
8. Ist es erledigt/veraltet? -> `archive/`

## Naming-Standard

- Dateinamen: `kebab-case.md`
- Datumsdateien: `YYYY-MM-DD.md`
- Keine neuen Root-Dateien ohne klaren Grund

## Obsidian-Navigation (Alias)

Die folgenden Symlinks sind reine Navigationshilfen im Vault:

- `01-memory`
- `02-projects`
- `03-content`
- `04-reference`
- `05-systems`
- `99-archive`

Sie enthalten keine eigenen Daten, sondern zeigen auf bestehende Source-Ordner.
