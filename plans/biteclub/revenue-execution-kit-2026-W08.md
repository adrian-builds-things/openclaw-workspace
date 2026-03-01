# Bite Club – Revenue Execution Kit (W08)

Stand: 2026-02-17 (Night Shift)
Ziel: In 7 Tagen messbar mehr Pipeline-Qualität + höhere Wahrscheinlichkeit auf Erstgespräche.

## 1) Business Goal → Audience → Offer → Channel → KPI

### Business Goal (7 Tage)
- **3 qualifizierte Erstgespräche** mit Zielkunden in der DACH-ICP.
- **20 personalisierte Outbound-Kontakte** (nicht generisch) an passende Buyer.

### Audience (Primary ICP)
- Unternehmen in DACH mit 150–1.500 Mitarbeitenden, Office-/Hybrid-Fokus.
- Rollen: Workplace/Office Manager, People Ops, Head of Operations, COO.

### Offer (Call Hook)
- „Lunch Ops ohne Chaos: weniger Admin-Aufwand + bessere Kostentransparenz + konstantere Employee Experience.“
- 15-Minuten Benchmark-Call als niedrigschwelliger CTA.

### Channel (W08 Fokus)
1. LinkedIn DM (nach Connect)
2. Cold Email
3. Follow-up Sequenz (D+2, D+5, D+8)

### KPI (Leading)
- Kontakte gesendet: Ziel 20
- Antwortquote: Ziel >= 15%
- Positive Reply Rate: Ziel >= 8%
- Calls gebucht: Ziel >= 3

---

## 2) ICP-Triage für jede Lead-Zeile

### Tier A (jetzt priorisieren)
- 150–1.500 Mitarbeitende
- mehrere Office-Tage / Hybrid
- sichtbarer Lunch-/Catering-Prozess
- Rolle mit operativer Verantwortung erreichbar

### Tier B
- 80–149 Mitarbeitende oder unklare Lunch-Verantwortung

### Tier C (vorerst parken)
- <80 Mitarbeitende
- kein Office-Lunch-Use-Case erkennbar
- sehr lange Procurement-Zyklen / öffentlicher Bereich (frühe Phase)

---

## 3) Outreach-Messaging Matrix (einfach, testbar)

### Angle A – Admin-Zeit sparen
- Hook: „Wie viel Abstimmungszeit kostet Lunch-Orga aktuell pro Woche?“
- Best für: Office/Workplace Ops

### Angle B – Kosten-/Transparenzdruck
- Hook: „Wie transparent sind Lunch-Kosten, Nutzung und Waste heute?“
- Best für: Ops Lead / COO / Finance-nahe Entscheider

### Angle C – Employee Experience / RTO
- Hook: „Wie stabil ist euer Lunch-Erlebnis an Office-Tagen?“
- Best für: People Ops / HR Ops

Regel: Pro Kontakt **nur 1 Angle** nutzen, um Signal sauber auswerten zu können.

---

## 4) 7-Tage Ablauf (max. 60–90 min/Tag)

### Tag 1 (heute)
- 20 Leads in CSV vorbereiten (mind. Firma, Rolle, Mitarbeitende, Trigger)
- Tiers vergeben (A/B/C)
- Angle pro Lead festlegen

### Tag 2
- 8 Tier-A Kontakte personalisiert anschreiben
- Tracking-Spalten aktualisieren (sent_at, channel, status)

### Tag 3
- 6 weitere Kontakte senden (A/B)
- Follow-up 1 für ausbleibende Antworten von Tag 2

### Tag 4
- 6 weitere Kontakte senden
- Positive Antworten sofort auf 15-min Call-CTA führen

### Tag 5
- Follow-up 1/2 je nach Alter des Kontakts
- Message-Pattern vergleichen (Angle A/B/C)

### Tag 6
- Restliche offenen A-Leads nachziehen
- Offensichtliche Non-Fit Leads parken

### Tag 7 (Review)
- KPI-Check + Musteranalyse
- Entscheidung: Welcher Angle + welcher Kanal gewinnt?
- Nächste Woche nur Top-Kombination skalieren

---

## 5) Minimal-CRM Felder (Pflicht)

- company
- first_name
- last_name
- role
- email
- linkedin_url
- employee_band
- sites
- icp_tier (A/B/C)
- angle (admin_time|cost_visibility|employee_experience)
- trigger
- channel (linkedin|email)
- status (new|contacted|replied|meeting_booked|parked)
- last_touch_at
- next_step
- notes

---

## 6) Entscheidungen, die Adrian in <10 Min treffen kann

1. **W08 KPI fixieren:** 20 Kontakte + 3 Erstgespräche (ja/nein).
2. **Kanal-Priorität:** LinkedIn first oder Email first.
3. **Angle-Priorität:** A/B/C – welcher zuerst mit 60% Volumen getestet wird.
4. **Pilot-Regel:** Nur Tier A in den ersten 3 Tagen (empfohlen: ja).

---

## 7) Sofort-Nächster Schritt

- CSV `tools/adrian-ops/data/biteclub-leads-template.csv` befüllen.
- Script `tools/adrian-ops/scripts/build-biteclub-outreach-queue.mjs` laufen lassen.
- Ergebnisdatei priorisiert abarbeiten (Top-down).


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
