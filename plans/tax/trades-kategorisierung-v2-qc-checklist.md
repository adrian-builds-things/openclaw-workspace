# QC-Checklist – Trades-Kategorisierung v2

## 1) Extraktions-Integrität
- [x] PDF vollständig gelesen (11 Seiten)
- [x] Rohtext-Extrakt erstellt: `raw-mtm-v2-extract.txt`
- [x] Jede Datum+Uhrzeit-Tradezeile in CSV übernommen
- [x] Ergebnis: **190 Event-Zeilen** (Aktie 18, Option 171, Devisen 1)

## 2) Summen-/Plausibilitätsabgleich
- [x] Kategorien gegen sichtbare Abschnittsstruktur geprüft (Aktien / Aktien- & Indexoptionen / Devisen)
- [ ] Vollständiger Broker-Report-Tradecount-Abgleich **nicht möglich**, da MTM-PDF keinen verlässlichen offiziellen Trade-Zähler enthält
- [x] Anzahl extrahierter Zeilen dokumentiert

## 3) Doppelte Trades / Teilfills
- [x] Exakt identische Schlüsselzeilen identifiziert (Zeitstempel+Symbol+Aktion+Menge+Preis)
- [x] Ergebnis: **18 Duplicate-Gruppen**, **23 zusätzliche Zeilen** (typisch Teilfills, nicht automatisch Fehler)
- [x] Keine automatische Deduplizierung vorgenommen (audit-safe: Rohsicht bleibt erhalten)

## 4) Entry/Exit-Zuordnung
- [x] FIFO-Heuristik implementiert
- [x] Exit-Zeilen mit Pair-ID markiert, wenn Gegenbein gefunden
- [x] Ergebnis: **72** gepaarte Exit-Zeilen
- [x] Unmatched Exits explizit gelistet (3 Fälle)

## 5) Offene Positionen / fehlende Exit-Daten
- [x] Optionen offen nach Heuristik: `CSCO 16FEB24 48 P` qty 4
- [x] Aktien offen nach Heuristik: `FCX` short 700, `HAL` short 700
- [x] Hinweis dokumentiert: Vorperioden-/fehlende Gegenbeine wahrscheinlich

## 6) Realized P/L Validierung
- [x] `realized_pnl` nur aus verfügbaren MTM-Zeilenwerten gesetzt
- [x] Jede nicht eindeutige Ableitung klar markiert (`uncertainty`)
- [x] Keine unmarkierten Schätzungen

## 7) FX/Währungsanteil
- [x] Pro-Trade-FX als nicht belastbar markiert
- [x] Summen-Methode dokumentiert (nur Aggregat-EUR aus Report)

## 8) Reproduzierbarkeit
- [x] Ergebnisdateien erstellt:
  - `trades-kategorisierung-v2-vollstaendig.md`
  - `trades-kategorisierung-v2-vollstaendig.csv`
  - `trades-kategorisierung-v2-qc-checklist.md`
- [x] Warn-/Unklarheitsliste erzeugt: `trades-kategorisierung-v2-warn-rows.txt`

## 9) Blocker für 100% revisionssichere Einzeltrade-Sicht
- [x] Fehlende Primärdaten benannt: Activity Statement Detailed inkl. Trades/Fills/Exec-ID/FX-Transaktionen


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
