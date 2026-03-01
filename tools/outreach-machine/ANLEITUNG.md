# Outreach Machine – Schnellanleitung

## 1) Datei initialisieren (einmalig)
```bash
cd /home/adrian/.openclaw/workspace
python3 tools/outreach-machine/outreach_machine.py init tools/outreach-machine/leads.csv
```

## 2) Heute fällige Follow-ups anzeigen
```bash
python3 tools/outreach-machine/outreach_machine.py due tools/outreach-machine/leads.csv
```

## 3) Kontakt aktualisieren / nachfassen
```bash
python3 tools/outreach-machine/outreach_machine.py touch tools/outreach-machine/leads.csv --name "Max Mustermann" --status contacted --note "Follow-up 1 gesendet"
```

## Status-Logik
- `contacted` → nächstes Follow-up in 3 Tagen
- `replied/qualified/won/lost` → kein automatisches Follow-up

## Tipp
Jeden Morgen einmal `due` ausführen und nur diese Liste abarbeiten.


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
