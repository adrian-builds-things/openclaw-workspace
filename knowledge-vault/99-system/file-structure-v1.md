# File Structure v1 (Workspace + Vault)

## Ziel
Schnelle Ablage, klare Zuständigkeit, minimale Suchzeit.

## Workspace-Ebenen (oberste Ordnung)
- `tools/` → laufende Apps/Codebases (z. B. `adrian-ops`)
- `plans/` → operative Arbeitsdokumente (Roadmaps, Task-Pläne, SQL-Checks, Tax-Läufe)
- `knowledge-vault/` → dauerhaftes Wissen + Entscheidungen + Ressourcen
- `skills/` → installierte AgentSkills (Quelle der Agent-Fähigkeiten)
- `memory/` + `MEMORY.md` → Tages-/Langzeitgedächtnis
- `scripts/` → Automationen
- `config/` → lokale Konfigurationen

## Knowledge Vault Struktur (neu/vereinheitlicht)
- `00-inbox/`        Eingehende Notizen (unsortiert)
- `10-domains/`      Langfristige Themen-/Wissensdomänen
- `15-skills/`       Skill-Dokumentation & Skill-Management-Notizen
- `20-playbooks/`    SOPs/Runbooks/Checklisten
- `30-decisions/`    Entscheidungsprotokolle (ADR-light)
- `40-content/`      Rohinhalte/Content Assets
- `50-resources/`    Quellen, Referenzen, Links, Research
- `60-reports/`      KPI-, Revenue-, SQL- und Statusberichte
- `90-archive/`      Erledigtes/abgelegtes Material
- `99-system/`       Regeln, Logs, Indizes

## Ablageregel (Kurzform)
1. Hat es einen konkreten nächsten Schritt? → `plans/` (operativ) oder `20-playbooks/` (wiederholbarer Prozess)
2. Ist es dauerhafte Referenz? → `knowledge-vault/50-resources/` oder `10-domains/`
3. Ist es eine Entscheidung? → `30-decisions/`
4. Ist es Skill-bezogen? → `knowledge-vault/15-skills/` (Doku) + `skills/` (Skill-Dateien)
5. Ist es ein Bericht/Messung? → `60-reports/`

## Skills-Management (verbindlich)
- Installierte Skills liegen physisch in: `skills/<skill-name>/`
- Skill-Log bleibt in: `skills/installed-skills.log.md`
- Skill-Governance/Übersicht liegt in: `knowledge-vault/15-skills/skills-governance.md`
- Keine Skill-Implementierungen im Vault duplizieren (nur Doku/Standards im Vault).

## Naming
- Dateien: `kebab-case.md`
- Reports optional mit Datum: `yyyy-mm-dd-thema.md`

## Nächster Schritt
Bestehende Inhalte schrittweise migrieren (ohne harte Massenverschiebung), damit nichts bricht.
