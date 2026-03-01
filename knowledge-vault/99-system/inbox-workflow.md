# Inbox Workflow (Adrian → Manne)

## Ziel
Inbox nur dann automatisch verschieben, wenn die Zuordnung **100% sicher** ist.
Wenn nicht 100% sicher: sammeln, Vorschläge vorbereiten, zu einem festen Tageszeitpunkt gemeinsam sortieren.

## Input von Adrian
1. Notizen/Ideen einfach in `00-inbox/` ablegen.
2. Dateiname darf roh sein (z. B. `idea.md`, `meeting-notes.md`).

## Verarbeitungsregel (verbindlich)

### A) Auto-Move nur bei 100% Sicherheit
Manne darf automatisch verschieben **nur**, wenn alle Punkte klar sind:
1. Dokumenttyp ist eindeutig (Decision/Playbook/Resource/Report/Domain-Note).
2. Zielordner ist eindeutig (kein plausibler Zweitordner).
3. Kontext ist ausreichend (kein fehlender Kernkontext).

Dann:
- Datei verschieben
- Dateiname standardisieren (kebab-case)
- Frontmatter ergänzen
- Log in `99-system/inbox-processing-log.md`

### B) Bei Unsicherheit (auch leicht) → nicht verschieben
Wenn nicht 100% sicher:
- Datei bleibt in Inbox-Review-Pool: `00-inbox/needs-review/`
- Keine finale Ablage ohne Rückfrage
- Manne erstellt pro Datei einen Vorschlag:
  - empfohlener Zielordner
  - Sicherheit in %
  - 1 Satz Begründung

## Daily Review Regel
- Einmal täglich als gebündelte Review an Adrian ausspielen.
- Vorschlag-Zeitpunkt: **17:30 Europe/Berlin** (anpassbar).
- Format pro Datei:
  - `Datei:`
  - `Vorschlag:`
  - `Sicherheit:`
  - `Begründung (kurz):`
  - `Aktion:` [Bestätigen | Alternativordner]

## Ziel-Mapping (Standard)
- Bite Club Themen → `10-domains/biteclub/`
- MindTrajour Themen → `10-domains/mindtrajour/`
- Sales/Outreach/CRM → `10-domains/sales/`
- Ops/Organisation/System → `10-domains/ops/`
- Entscheidungen → `30-decisions/`
- Wiederholbare Prozesse → `20-playbooks/`
- Content-Ideen/Posts/Blog → `40-content/`
- Rohquellen/Links/Research → `50-resources/`
- Messungen/Reporting → `60-reports/`

## Sicherheitsprinzip
Lieber 1 Datei zu viel in `needs-review` als 1 Datei falsch abgelegt.
