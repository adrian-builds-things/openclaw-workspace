# [[OBSIDIAN_ROUTING]]

Verbindliche Ablage-Regel für einen **klaren PARA-Workflow**.

## Prinzip
- Vorne nur **[[DASHBOARD]]** als Cockpit.
- Danach klare Ordner (PARA) + feste Ablageorte.
- Keine neuen Root-Dateien ohne guten Grund.

## PARA-Struktur
- `00-cockpit/` → tägliche Steuerung, Prioritäten, Master-Tasks
- `10-projects/` → aktive Projekte mit konkreten Deliverables
- `20-areas/` → laufende Verantwortungsbereiche (Ops, Guides, Routinen)
- `30-resources/` → Wissen, Referenzen, Literatur, Video-Notizen
- `40-archive/` → abgeschlossene/alte Inhalte

## Technische Source-Ordner (bleiben bestehen)
Diese Ordner bleiben aus Systemgründen erhalten und werden weiter genutzt:
- `memory/` + [[MEMORY]]
- `plans/`
- `content/`
- `knowledge/`
- `tools/`
- `scripts/`
- `archive/`

## Routing-Matrix (praktisch)
1. Tagesnotiz / Status → `memory/YYYY-MM-DD.md`
2. Langzeitwissen über Adrian / Entscheidungen → [[MEMORY]]
3. Konkreter Projekt-Task → `10-projects/<projekt>/...`
4. Wiederkehrende Betriebs-/Prozessnotiz → `20-areas/...`
5. Recherche, Literatur, externe Quellen → `30-resources/...` (bzw. `knowledge/...`)
6. Erledigt / veraltet → `40-archive/...` (bzw. `archive/...`)

## Naming
- Dateinamen: `kebab-case.md`
- Datumsdateien: `YYYY-MM-DD.md`

## Einstieg
- [[DASHBOARD]]
- [[NAVIGATION]]
- [[00-cockpit/tasks-master|Tasks Master]]
