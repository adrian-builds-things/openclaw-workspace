# CONTROL TOWER — Bot Command Center

Status: aktivierbar, sobald APIs gesetzt sind.

## 1) Live-Übersicht (Daily)

- **Datum:** 
- **Top Revenue-Ziel heute:** 
- **Fokusprodukt:** BC / MTJ / beide
- **Betriebsmodus:** Build / GTM / Mixed

---

## 2) Bot-Status

| Bot | Rolle | Name | Status | Modellroute | Aktuelles Ticket | Nächster Checkpoint |
|---|---|---|---|---|---|---|
| 01 | Orchestrator/PO | Käptn Fokus | ⬜ idle / 🟢 running / 🔴 blocked | cheap + Opus bei Weichen |  |  |
| 02 | Engineering+Architect | Forge | ⬜ / 🟢 / 🔴 | Codex default, Opus für Architektur |  |  |
| 03 | Growth/Copy/SEO | Echo | ⬜ / 🟢 / 🔴 | cheap draft + Opus final |  |  |
| 04 | Analytics | Pulse | ⬜ / 🟢 / 🔴 | cheap default, Opus bei krit. Entscheidungen |  |  |
| 05 | Content Studio | Nova | ⬜ / 🟢 / 🔴 | cheap default, selective premium polish |  |  |
| 06 | Outbound Prospecting | Scout | ⬜ / 🟢 / 🔴 | Gemini research + quality review |  |  |
| 07 | Productivity Assistant | Atlas | ⬜ / 🟢 / 🔴 | cheap structured planning |  |  |

---

## 3) Kanban-Snapshot (Single Source)

- **Backlog:** 
- **Ready (max 5):** 
- **Doing (WIP-Limit 3):** 
- **Review:** 
- **Done (heute):** 

### Ticket-Template (Kurz)
- **ID:** 
- **Problem:** 
- **Ziel/KPI:** 
- **Owner-Bot:** 
- **DoD:** 
- **Risiko:** 

---

## 4) Guardrails-Check (vor jeder Session)

- [ ] Externe Nachrichten nur manuell durch Adrian
- [ ] MTJ/BC: nur lokal arbeiten, nicht pushen/deployen ohne Freigabe
- [ ] Eigene Bot-Tools: Build/Merge/Deploy ok
- [ ] Kein Ticket ohne KPI + DoD

Referenz: `GUARDRAILS.md`

---

## 5) Modell-Routing-Check

- [ ] Opus nur für High-Stakes Denken/Finalisierung
- [ ] Codex für Coding/Umsetzung
- [ ] Gemini für Research/Signals
- [ ] cheap-first bei Drafts/Varianten

Referenz: `MODEL_ROUTING.md`

---

## 6) Outbound Desk (Scout)

### Ziel heute
- **Produktfokus:** BC / MTJ
- **Leads Zielmenge (qualitativ):** 
- **Mindest-Fit-Score:** 

### Output-Checklist je Lead
- [ ] Quelle + Profil-Link
- [ ] ICP-Fit-Score
- [ ] 1–2 personalisierte Hooks
- [ ] Cold Email Draft
- [ ] LinkedIn DM Draft
- [ ] Connect-Note <=200 Zeichen

---

## 7) Productivity Desk (Atlas)

### Morning (10 min)
- **Top 1:** 
- **Top 3:** 
- **Fixtermine heute:** 
- **Fokusblöcke (25/50/90):** 

### Midday (5 min)
- **Was driftet?** 
- **Was wird geschnitten?** 

### Evening (10 min)
- **Was shipped?** 
- **Was blockiert?** 
- **Carry-over mit klarem Next Step:** 

---

## 8) Entscheidungen & Learnings

### Entscheidungen (heute)
- 

### Learnings
- 

Ablage langfristig:
- `MEMORY.md`
- `memory/YYYY-MM-DD.md`

---

## 9) Schnellstart-Reihenfolge (pro Tag)

1. Käptn Fokus: Priorisierung + WIP setzen
2. Forge + Echo: Execution auf Top-Tickets
3. Scout: qualifizierte Outbound-Pakete
4. Pulse: KPI/Tracking/Validierung
5. Atlas: Timeboxing + Tagessteuerung
6. Nova: Content-Output + Repurposing

---

## 10) API-Setup Status

- [ ] Anthropic API gesetzt
- [ ] OpenAI/Codex API gesetzt
- [ ] Gemini API gesetzt
- [ ] Smoke-Test je Bot durchgeführt

