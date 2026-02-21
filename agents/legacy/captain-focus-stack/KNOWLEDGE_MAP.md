# Wo liegen die erarbeiteten Infos? (Knowledge Map)

## Bereits vorhanden
- Langzeitkontext: `/home/adrian/.openclaw/workspace/MEMORY.md`
- Tages-/Verlaufsnotizen: `/home/adrian/.openclaw/workspace/memory/YYYY-MM-DD.md`
- Bot-Souls: `/home/adrian/.openclaw/workspace/agents/souls/*.md`
  - inkl. neu: `06_outbound_prospecting.md`, `07_executive_productivity.md`
- Strukturübersicht: `/home/adrian/.openclaw/workspace/agents/souls/README.md`
- Routing-Regeln: `/home/adrian/.openclaw/workspace/agents/MODEL_ROUTING.md`
- Sicherheits-/Freigaberegeln: `/home/adrian/.openclaw/workspace/agents/GUARDRAILS.md`

## Empfehlung zur Sicherung (ab jetzt)
1. Wöchentlicher Backup-Ordner:
   - `/home/adrian/.openclaw/workspace/archive/weekly/YYYY-WW/`
2. Dort speichern:
   - aktuelle Souls
   - Guardrails + Routing
   - Board-Exports / Ticket-Backups
3. Zusätzlich Git-Commit für jede Regeländerung:
   - Commit-Message-Präfix: `ops:`, `soul:`, `policy:`

## Single Source of Truth
- Policies: `agents/`
- Operative Tickets/Kanban: euer Board-Tool
- Personen-/Langzeitpräferenzen: `MEMORY.md`
