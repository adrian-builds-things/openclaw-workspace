# Model Routing Policy v1 (Brain/Muscle)

Ziel: Maximale Ergebnisqualität bei minimalen Kosten.

## Grundprinzip
cheap draft -> focused review -> premium polish nur bei high-stakes Artefakten.

## Modellrollen

### Opus 4.6 (Brain / teuer)
Nutzen für:
- Strategische Entscheidungen (Positioning, GTM, Architektur-Trade-offs)
- High-stakes Copy final (Landingpage Hero, Offer, Kernbotschaften)
- Komplexe Planungs- und Denkaufgaben mit hohem Risiko

Nicht nutzen für:
- Fleißarbeit, einfache Umformulierungen, Massenvarianten

### Codex CLI (Muscle Coding)
Nutzen für:
- Implementierung, Refactoring, Tests, technische Doku
- Strukturierte Code-Aufgaben mit klaren Anforderungen

Nicht nutzen für:
- Primäre Marketingstrategie ohne klaren Tech-Anteil

### Gemini CLI (Muscle Research)
Nutzen für:
- Webrecherche, Quellenvergleich, Marktsignale, Lead-Pre-Recherche
- Sammeln und Vorstrukturieren von Informationen

Nicht nutzen für:
- Endgültige kritische Entscheidungen ohne Review

## Routing nach Bot
- Orchestrator/PO: primär günstiges Modell + Opus bei strategischen Weichen
- Engineering+Architect: Codex als Default; Opus bei Architektur-Memo
- Growth/Copy/SEO: günstiges Modell für Drafts, Opus fürs Final bei Kernseiten
- Analytics: günstiges Modell für Auswertungen, Opus bei kritischen Entscheidungen
- Content Studio: günstige Modelle + selektives Premium-Polishing
- Outbound Prospecting: Gemini/Research-first + finale Qualitätsprüfung
- Executive Productivity: günstiges Modell (strukturierte Routinen)

## Cost Guardrails
- Tagesbudget je Bot definieren und tracken.
- Premium-Calls nur mit Grund (Decision-Impact / Revenue-Impact).
- Wiederkehrende Aufgaben standardisieren (Templates).
