# Google Kalender Safe Setup (ohne Haupt-Gmail Zugriff)

Stand: 2026-02-16
Ziel: Kalenderdaten für Planung nutzbar machen, ohne Zugriff auf dein Hauptkonto.

## Sicherheitsprinzip
- Kein Zugriff auf Haupt-Gmail.
- Eigener dedizierter Account nur für Ops-Kalender.
- Minimalrechte (least privilege).

## Empfohlene Architektur

### Option A (empfohlen): Separater Google-Account
1. Neuen Account erstellen (z. B. `adrian.ops.calendar@...`).
2. Dort einen Kalender `Adrian Ops` anlegen.
3. Nur relevante Termine aus Hauptkalender spiegeln/eintragen.
4. Manne/OpenClaw bekommt nur diesen Account/API-Zugriff.

Vorteile:
- klare Trennung
- bei Kompromittierung kein Hauptpostfach betroffen

### Option B: Kalenderfreigabe mit Minimalrechten
1. Im Hauptkonto einen separaten Kalender erstellen (`Ops Share`).
2. Nur diesen Kalender für den Ops-Account freigeben (Editor/Reader je nach Bedarf).
3. Kein Zugriff auf Mail/Drive/Contacts.

## Berechtigungsmodell
- Für Manne ideal: nur Kalender-Lesen + ggf. Schreiben im Ops-Kalender.
- Niemals Vollzugriff aufs Hauptkonto.

## Betriebsprozess
- Du pflegst Haupttermine weiter wie bisher.
- Nur planungsrelevante Termine landen im `Adrian Ops` Kalender.
- Manne nutzt diesen Feed für Tagesplanung, Erinnerungen, Priorisierung.

## Optional: Noch strikter read-only
- Privater ICS-Feed nur lesen.
- Keine Schreibrechte durch Manne.

## Nächster Implementierungsschritt
- Nach Account-Erstellung: OpenClaw Kalender-Integration nur auf Ops-Account konfigurieren.
- Anschließend tägliche Zusammenfassung aus diesem Kalender erzeugen.
