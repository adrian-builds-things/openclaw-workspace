# Rollout-Plan (Slack → Obsidian → Workflow) 

Stand: 2026-02-16

## Entscheidung (fix)
1. **Slack zuerst**
2. **Obsidian + strukturierter Shared Workspace danach**
3. **Workflow-Optimierung & Dashboard-Ausbau danach**

ByteClub Reporting läuft parallel als operatives Tages-Thema.

---

## Warum diese Reihenfolge sinnvoll ist
- Aktueller Engpass ist **Kommunikation + Dateichaos**, nicht fehlende Features.
- Slack gibt dir sofort klare Steuerung und weniger Telegram-Noise.
- Obsidian stabilisiert das Wissen (Second Brain), damit Agenten konsistent arbeiten.
- Erst dann lohnt es sich, komplexere Boards/Automationen auszubauen.

---

## Phase 1 — Slack produktiv (Tag 1)

### Ziel
Du kannst mit Agenten in Slack sauber arbeiten (Threads, Routing, klare Kanäle).

### Minimal-Setup
- 1 Slack App (Socket Mode)
- 1 Bot Token + 1 App Token
- 3 Channels:
  - `#ops-hq`
  - `#biteclub-data`
  - `#mindtrajour`
- 1 Agent erst mal als sicherer Start, dann Schrittweise auf mehrere Agenten erweitern.

### Danach Erweiterung auf Rollen-Agenten
- `claw` (OpenClaw/System)
- `bernard` (Dev)
- `vale` (Marketing)
- `gumbo` (Assistant/Glue)

### Erfolgscheck
- Nachricht in jedem Channel kommt an
- Antwort wird korrekt im Thread geroutet
- Kein Cross-Talk zwischen Kanälen

---

## Phase 2 — Obsidian + Brain (Tag 2–3)

### Ziel
Sauberes Wissenssystem statt Dateiwust.

### Struktur
- `00-inbox`
- `10-domains`
- `20-playbooks`
- `30-decisions`
- `40-content`
- `90-archive`

### Governance
- Jede neue Idee zuerst in `00-inbox`
- Wichtige Entscheidungen in `30-decisions`
- Wiederholbare Prozesse in `20-playbooks`
- Link-Bibliothek in `10-domains/link-library.md`

### Sync-Ansatz (lokal-first)
- Mac als Primary Authoring in Obsidian
- selektiver Sync zum OpenClaw-Workspace (nur freigegebene Ordner)
- private Ordner bleiben draußen

### Erfolgscheck
- Neue Notiz vom Mac erscheint im Workspace
- Agent kann Datei lesen, kategorisieren, verlinken
- keine ungeordneten Files außerhalb der Struktur

---

## Phase 3 — Workflow + Dashboard (Tag 4–7)

### Ziel
Fokus auf Output statt Tool-Spielerei.

### Kernpunkte
- Daily Priorisierung (Top 3)
- Timeboxing-Blöcke
- EOD-Review
- Dashboard: nur entscheidungsrelevante Metriken

### Wichtige Regel
**Kanban erst erweitern, wenn Slack + Brain stabil laufen.**

---

## ByteClub Reporting (parallel, höchste operative Priorität)

### Sofort-Workflow
- Zeitraum fixieren
- SQL vs Report Reconciliation Sheet
- Delta/Ursache je KPI dokumentieren

### Output
- „passt / passt nicht" pro KPI
- Abweichungsursachen klar gelistet

---

## Architektur-Ideen aus Brian-Casel-Ansatz (angepasst)

- Gateway-Host bleibt dediziert/always-on
- Rollenbasierte Agenten statt 1 Universal-Agent
- gemeinsamer Workspace + klare Identity/Memory
- Slack als primäres Interface mit Thread-Disziplin
- Modellstrategie nach Aufgabe (teures Denken, effizientes Bauen)

---

## Nächster konkreter Schritt (jetzt)
1. Slack Tokens + Channel-IDs bereitstellen
2. Slack in OpenClaw konfigurieren
3. Test mit `#ops-hq`
4. Danach Obsidian-Sync finalisieren
