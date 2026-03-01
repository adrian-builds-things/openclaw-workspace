# Entwurf: Lokales Wissensmanagement mit Obsidian (ohne Cloud)

Stand: 2026-02-16
Ziel: Adrian pflegt Wissen lokal in Obsidian; Manne kann es strukturiert lesen und nutzen.

## Prinzip
- **Single Source of Truth:** ein lokaler Obsidian Vault im Workspace oder per symlink eingebunden
- **Keine Cloud nötig:** reine Dateien (Markdown, JSON) lokal auf dem Host
- **Agent-read-only Standard:** Manne liest standardmäßig; schreibt nur in klar definierte Bereiche

## Option A (einfach, empfohlen)
Obsidian-Vault direkt unter:
`/home/adrian/.openclaw/workspace/knowledge-vault/`

Vorteile:
- keine Sync-Abhängigkeit
- sofort für Agent erreichbar
- Backup über Git/rsync möglich

## Option B (bestehender Vault bleibt extern)
- Bestehender Vault bleibt z. B. unter `~/Documents/Obsidian/Adrian`
- Im Workspace nur Link:
  `knowledge-vault -> ~/Documents/Obsidian/Adrian`

Vorteil: keine Umgewöhnung in Obsidian.

## Ordnerstruktur (MVP)
- `00-inbox/` (ungeordnet, schnell erfassen)
- `10-domains/` (Bite Club, MindTrajour, Sales, Ops)
- `20-playbooks/` (SOPs, Checklisten)
- `30-decisions/` (ADR-ähnliche Entscheidungsnotizen)
- `40-content/` (LinkedIn, Blog, Ideen)
- `90-archive/`

## Datei-Template (Frontmatter)
```md
---
title: ""
domain: biteclub|mindtrajour|ops|sales
type: note|decision|playbook|content
status: draft|active|done
updated: 2026-02-16
tags: []
---
```

## Übergabe an Manne (konkret)
1. Adrian schreibt Notizen in Obsidian wie gewohnt.
2. Manne liest täglich:
   - neue Dateien in `00-inbox`
   - geänderte Dateien in `10-domains` und `30-decisions`
3. Manne erzeugt:
   - Task-Vorschläge
   - Content-Vorschläge
   - Entscheidungsvorlagen

## Technische Brücke (später)
- `knowledge-index.json` erzeugen (lokaler Index)
- optional: lokale semantische Suche (wenn API/Auth sauber)
- nightly digest aus Vault-Änderungen

## Sicherheits-/Betriebsregeln
- Keine Exfiltration / kein Cloud-Upload
- Externe Kommunikation nur nach expliziter Freigabe
- Änderungen von Manne nur in freigegebenen Ordnern (`40-content/drafts`, `00-inbox/processed`)

## Nächste 3 Schritte
1. Vault-Pfad festlegen (Option A oder B)
2. Struktur + Templates anlegen
3. Erste automatische Routine: täglicher „Vault -> Action Digest"
