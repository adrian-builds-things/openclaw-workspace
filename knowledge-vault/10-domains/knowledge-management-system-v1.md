# Knowledge Management System v1 (lokal, ohne Cloud)

Stand: 2026-02-16

## Ziel
Adrian pflegt Wissen lokal (Obsidian-kompatibel), Manne kann es zuverlässig lesen, priorisieren und in Tasks/Content/Entscheidungen übersetzen.

## Umgesetzt (jetzt)
- Lokaler Vault angelegt: `/home/adrian/.openclaw/workspace/knowledge-vault/`
- Struktur angelegt:
  - `00-inbox`
  - `10-domains`
  - `20-playbooks`
  - `30-decisions`
  - `40-content`
  - `90-archive`
  - `templates`
- Template angelegt:
  - `knowledge-vault/templates/note-template.md`
- Lokaler Index-Builder gebaut:
  - `scripts/knowledge/build-knowledge-index.mjs`
- Index-Datei erzeugt:
  - `memory/knowledge-index.json`

## So teilst du Wissen mit mir (minimal friction)
1. Notizen in Obsidian direkt im Vault schreiben (oder bestehenden Vault symlinken).
2. Wenn du etwas wichtig markierst, lege es in:
   - `10-domains/*` (Fachwissen)
   - `30-decisions/*` (Entscheidungen)
   - `40-content/*` (Content-Ideen)
3. Ich lese es, verdichte es und überführe es in:
   - konkrete To-dos
   - Content-Entwürfe
   - Entscheidungs-Optionen

## Betriebsmodell
- Single source of truth: Markdown im lokalen Vault.
- Kein Cloud-Zwang.
- Keine externe Exfiltration ohne Freigabe.

## Nächster Ausbau (ohne dich zu nerven)
1. Dashboard-Widget: „Knowledge Update Feed“ aus `knowledge-index.json`
2. Auto-Digest: letzte geänderte Notizen -> Tagesfokus
3. Mapping: Domain-Notizen -> Ops-Tasks (semi-automatisch)
