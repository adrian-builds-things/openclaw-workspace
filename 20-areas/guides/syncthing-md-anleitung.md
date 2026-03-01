# Syncthing Setup (Mac <-> Server) für Wissensdaten

## Ziel
Nur Wissensdaten synchronisieren (Markdown/Notizen/Memory/Pläne), kein Runtime-/Build-/venv-Müll.

## Pfade
- **Server Folder:** `/home/adrian/.openclaw/workspace`
- **Mac Folder:** z. B. `~/Obsidian/Manne-Workspace`

## 1) Device Pairing prüfen
Auf beiden Seiten in Syncthing GUI:
- Gegenseitige Device-ID muss als **Connected** erscheinen.
- Wenn nicht: Device hinzufügen und einmal akzeptieren.

## 2) Folder auf Server anlegen/freigeben
- Add Folder
- Folder Path: `/home/adrian/.openclaw/workspace`
- Folder Type: **Send & Receive**
- Share with: dein Mac Device
- Save

## 3) Folder auf Mac akzeptieren
- Incoming folder request akzeptieren
- Local Path setzen: `~/Obsidian/Manne-Workspace`
- Folder Type: **Send & Receive**
- Save

## 4) Ignore-Regeln aktiv
- Datei liegt im Root: `.stignore`
- Syncthing liest sie automatisch ein.
- Bei Bedarf in GUI auf Folder -> Edit -> Ignore Patterns öffnen und prüfen.

## 5) Versioning aktivieren (Rollback)
Empfehlung:
- Folder -> Edit -> File Versioning
- **Simple File Versioning**
- Keep: z. B. 10–30 Versionen

## 6) Initialer Test
1. Auf Mac Datei anlegen: `00-inbox/from-mac/test-sync.md`
2. Warten bis `Up to Date`
3. Prüfen auf Server, ob Datei ankommt
4. Datei auf Server nach `00-inbox/processed/` verschieben
5. Prüfen auf Mac, ob Verschiebung synchronisiert wurde

## 7) Daily Workflow
- Neue Quellen vom Mac immer in `00-inbox/from-mac/` ablegen.
- Manne sortiert nach `[[OBSIDIAN_ROUTING]]` ein.
- Ergebnis landet in Zielordnern und synced zurück auf den Mac.

## Troubleshooting (kurz)
- **Out of Sync:** Rescan Folder auf beiden Seiten.
- **Nichts kommt an:** Prüfen, ob `.stignore` Pfad erlaubt.
- **Falscher lokaler Pfad:** Folder auf Mac neu mappen und erneut akzeptieren.


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
