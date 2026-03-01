# Syncthing Obsidian Bridge Setup (Mac ↔ VPS)

Stand: 2026-02-16
Ziel: Obsidian-Notizen ohne Cloud und ohne manuellen Aufwand vom Mac zum VPS spiegeln.

## Architektur
- Quelle (Mac): `~/Documents/Obsidian/Manne-Share`
- Ziel (VPS): `/home/adrian/.openclaw/workspace/knowledge-vault/00-inbox/from-mac`
- Sync: Syncthing (peer-to-peer, verschlüsselt)

## Sicherheitsregeln
- Nur `Manne-Share` freigeben (nicht den gesamten Vault).
- In `Manne-Share` nur Inhalte, die Manne sehen darf.
- Optional: Unterordner `private` lokal halten und nicht teilen.

## Schritt 1 — Syncthing auf Mac installieren
Option Homebrew:
```bash
brew install --cask syncthing
```
Dann starten (GUI über Browser):
```bash
open /Applications/Syncthing.app
```

## Schritt 2 — Syncthing auf VPS installieren
```bash
sudo apt update
sudo apt install -y syncthing
systemctl --user enable --now syncthing
```
Status prüfen:
```bash
systemctl --user status syncthing
```

## Schritt 3 — Web-GUI erreichbar machen
### Auf VPS (localhost-Tunnel über SSH vom Mac)
```bash
ssh -N -L 8384:127.0.0.1:8384 adrian@100.78.193.125
```
Dann auf Mac öffnen:
- http://localhost:8384 (VPS Syncthing)

Mac-Syncthing läuft lokal ebenfalls auf http://localhost:8384.
=> Falls Kollision: zuerst Mac konfigurieren, dann VPS-Tunnel separat.

## Schritt 4 — Geräte koppeln
- Auf Mac Device ID kopieren.
- Auf VPS als Remote Device hinzufügen.
- Gegenseitig bestätigen.

## Schritt 5 — Ordner freigeben
### Mac-Seite
- Folder: `~/Documents/Obsidian/Manne-Share`
- Folder ID: `manne-share`
- Share with: VPS device

### VPS-Seite
- Folder ID: `manne-share` akzeptieren
- Path: `/home/adrian/.openclaw/workspace/knowledge-vault/00-inbox/from-mac`
- Folder Type: **Send & Receive**

## Empfohlene Struktur auf Mac
`~/Documents/Obsidian/Manne-Share/`
- `00-inbox/`
- `10-domains/`
- `30-decisions/`
- `40-content/`
- `_attachments/`

## Betrieb
- Du schreibst in Obsidian wie gewohnt.
- Syncthing spiegelt automatisch.
- Manne indexiert + verarbeitet Inhalte in Tasks/Entscheidungen/Content.

## Troubleshooting
- Sync hängt: Device online? Firewall offen? Folder paused?
- Konflikte: Syncthing conflict files prüfen.
- Zu viele Dateien: Nur relevante Unterordner teilen.
