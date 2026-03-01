# Outreach Machine (Mini-Tool)

Ein einfaches CLI-Tool, um Bite-Club-Outreach als Pipeline zu steuern.

## Nutzen
- Kontakte als CSV verwalten
- Follow-up-Fälligkeiten automatisch berechnen
- Tagesliste mit "heute fällig" erzeugen

## Datei-Format
CSV mit Spalten:
- name
- company
- channel (email|linkedin)
- first_contact_date (YYYY-MM-DD)
- status (new|contacted|replied|qualified|won|lost)
- last_touch_date (YYYY-MM-DD)
- next_followup_date (YYYY-MM-DD)
- notes

## Commands

```bash
python3 outreach_machine.py init leads.csv
python3 outreach_machine.py due leads.csv
python3 outreach_machine.py touch leads.csv --name "Max Mustermann" --status contacted --note "Erstkontakt gesendet"
```

## Follow-up Logik
- Erstkontakt: Tag 0
- Follow-up 1: +3 Tage
- Follow-up 2: +7 Tage


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
