# Trades-Kategorisierung v2 (vollständig, MTM-PDF Neu-Auswertung)

Quelle: `/home/adrian/.openclaw/media/inbound/file_28---79a1d4aa-18d5-47e4-87eb-4c7d2d1fb6dd.pdf`  
Reporttyp laut PDF: **MTM-Übersicht** (01.01.2024–31.12.2024), 11 Seiten.

## Ergebnis in einem Satz
Ich habe **jede im PDF als Datums-/Zeit-Tradezeile sichtbare Buchung** extrahiert und in CSV erfasst (**190 Zeilen**), inklusive Kategorie, Entry/Exit-Heuristik und Unsicherheitsmarkierung; zugleich ist transparent dokumentiert, dass diese MTM-PDF **nicht ausreicht**, um für *jeden* Trade einen regulatorisch belastbaren Realized-P/L pro Roundtrip eindeutig zu beweisen.

## Vollständigkeit (aus dieser PDF)
- Extrahierte Trade-Event-Zeilen (Datum+Uhrzeit): **190**
  - **Aktie:** 18
  - **Stillhalter (Optionen):** 171
  - **Termingeschäft (Devisen/FX):** 1
- Zeitbereich der extrahierten Zeilen: **2023-12-29 bis 2024-11-05**
  - Davon 2024: **188** Zeilen
  - Vorperiode (im Report enthalten): **2** Zeilen (FCX/HAL Verfall 2023-12-29)

## Was pro Zeile geliefert wird (CSV)
Datei: `trades-kategorisierung-v2-vollstaendig.csv`
- Instrument/Ticker (`symbol`, `description`)
- Kategorie (`category`): Aktie / Stillhalter / Termingeschäft
- Entry-/Exit-Felder (`entry_*`, `exit_*`) via FIFO-Heuristik
- Realized-P/L Feld (`realized_pnl`) aus MTM-Zeile (wenn zuordenbar)
- FX-Felder (`fx_component_eur`, `fx_method`)
- Harte Unsicherheitsmarkierung (`uncertainty`)

## Harte Limitationen der Datengrundlage (wichtig)
Die vorliegende MTM-Übersicht ist **kein vollständiger Trade-/Fill-Ledger**. Daher:
1. **Keine eindeutigen Trade-IDs / Exec-IDs** je Fill in diesem PDF.
2. Mehrfachzeilen mit identischem Zeitstempel (Teilfills) sind vorhanden; Zuordnung ist nur heuristisch.
3. Für Aktien-Assignments/Positionswechsel (z. B. FCX/HAL) fehlt teils das Gegenbein im selben Zeitraum (Vorperiodenabhängigkeit).
4. **FX pro Trade** ist nicht sauber isolierbar; im PDF liegen FX-Effekte überwiegend aggregiert auf Klassenebene vor.

=> Deshalb sind in CSV alle nicht zweifelsfreien Zuordnungen explizit markiert. **Keine stillen Schätzungen.**

## Explizite unklare/fehlende Zuordnungen
Unmatched Exit-Zeilen (kein zuordenbarer ENTRY innerhalb der extrahierten Daten):
1. `2024-02-15 10:15:41` CSCO `Kauf` qty 4
2. `2023-12-29 16:20:00` FCX `Verfallen` qty 7
3. `2023-12-29 16:20:00` HAL `Verfallen` qty 7

Offene Restpositionen nach FIFO-Heuristik (innerhalb dieser Datenbasis):
- Option offen: `CSCO 16FEB24 48 P` qty 4
- Aktie offen: `FCX` short qty 700
- Aktie offen: `HAL` short qty 700

Hinweis: Diese offenen/fehlenden Gegenbeine sind mit hoher Wahrscheinlichkeit durch Vorperioden-/außerhalb-dieses-Reports liegende Buchungen erklärbar.

## FX/Währungsanteil pro Trade
- Pro Trade **nicht belastbar rückrechenbar** aus diesem MTM-PDF allein.
- Im CSV daher: `fx_component_eur` leer und `fx_method` mit Methodik-Hinweis befüllt.
- Summenmethode: nur aggregierte EUR-Gesamtwerte je Abschnitt aus Report nutzbar (Klassen-/Gesamtebene, nicht Trade-Ebene).

## Verbindlicher Next-Step (für 100% auditfeste "jeder Trade"-Sicht)
Bitte exakt diesen Export aus IBKR/CapTrader bereitstellen:
1. **Activity Statement (Detailed)** für 01.01.2024–31.12.2024
2. Sektionen aktiviert: **Trades**, **Fills**, **Option Exercises/Assignments**, **Corporate Actions**, **FX Transactions**, **Commissions**, **Withholding Tax**, **Open/Closed Positions**
3. Mit Feldern inkl. **Trade ID / Exec ID**, Order-ID, Zeitstempel (inkl. Zeitzone), Menge, Preis, Währung, Gebühren, Realized P/L, FX-Rate
4. Format: **CSV** (bevorzugt) oder XML

Erst damit kann pro Trade Entry/Exit + realisierter Gewinn/Verlust + FX-Anteil ohne Heuristik final und revisionssicher abgeschlossen werden.
