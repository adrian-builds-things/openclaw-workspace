# TaskBoard MVP — Spec

## Vision
Persönliches Task-Management-Tool für Adrian + Team. Zwei Hauptansichten, Chat-Interface für KI-Interaktion, MD-File-Backend. Ästhetisch, minimal, anti-Overwhelm.

## Tech Stack
- Next.js 15 (App Router, TypeScript)
- TailwindCSS 4
- shadcn/ui
- File-based storage (MD files mit Frontmatter) — kein DB für MVP
- API Routes für CRUD + Chat

## Views

### 1. Focus View (Default)
- "Was steht heute/diese Woche an?"
- Max 5–7 sichtbare Tasks
- Große, klare Cards mit: Titel, Projekt-Badge, Prio-Indikator, Timebox, Assignee-Avatar
- "Top Queue" prominent oben (explizit markierte Next Actions)
- Subtile Progress-Info (3/7 diese Woche erledigt)

### 2. Planning View
- Kanban-Board: Inbox → Next → Doing → Waiting → Done
- Drag & Drop zwischen Spalten
- Filter: Projekt, Assignee, Prio
- Bulk-Aktionen (mehrere Tasks verschieben)

### 3. Chat Panel (Sidebar/Drawer)
- Rechte Seite oder Bottom-Sheet
- Nachricht an Manne senden
- Tasks referenzieren ("mach Task X als nächstes")
- Manne kann Tasks erstellen/updaten via Chat
- Integration: sendet Messages an OpenClaw Session

## Task Card Fields
- `id` (auto-generated)
- `title` (required)
- `description` (optional, Markdown)
- `status`: inbox | next | doing | waiting | done
- `priority`: critical | high | medium | low
- `project`: bite-club | mindtrajour | ai-stromlaufplan | openclaw | personal
- `assignee`: adrian | enes | luis | larissa | eve | manne | max | luna | rico
- `timebox`: duration in minutes (optional)
- `due`: date (optional)
- `created`: datetime
- `updated`: datetime
- `tags`: string[] (optional)

## MD File Format
```markdown
---
id: task-001
title: Lead Magnet Savings Calculator bauen
status: next
priority: high
project: bite-club
assignee: adrian
timebox: 120
due: 2026-02-25
created: 2026-02-22
updated: 2026-02-22
tags: [marketing, lead-gen]
---

## Details
Savings Calculator als Lead Magnet für Bite Club...

## Notes
- Referenz: [[plans/biteclub/lead-magnet-calculator]]
```

## Storage
- Tasks live in: `tasks/` directory (one MD file per task)
- App reads/writes these files via API routes
- File watcher or on-demand refresh

## Design Requirements
- Design Tokens: colors, spacing, radius, typography zentral definiert
- Two theme variants for A/B test:
  - **Theme A "Clean Focus"**: Weiß/Grau-Basis, sanfte Akzentfarbe (Blau/Indigo), viel Whitespace, große Typo, Cards mit subtle shadow
  - **Theme B "Warm Minimal"**: Leicht warmer Hintergrund (off-white/cream), erdige Akzente (amber/slate), rounded corners, softer feel
- Dark mode support von Anfang an
- Mobile-responsive (Adrian nutzt auch Handy)
- Keyboard shortcuts (j/k navigate, Enter open, Esc close)

## A/B Test Setup
- Theme-Switcher im UI (Toggle oben rechts)
- Beide Themes vollständig implementiert
- Adrian kann live hin- und herschalten und entscheiden

## Existing Tasks to Import
Quelle: `00-cockpit/tasks-master.md` + `plans/ops/tasks-2026-02-21.md`

### Top Priority
1. Bite Club — Lead Magnet Savings Calculator | high | bite-club | adrian
2. MindTrajour — Landingpage-Copy + CTA finalisieren | high | mindtrajour | adrian
3. MindTrajour — PostHog Events aufsetzen | high | mindtrajour | adrian
4. MindTrajour — Sprint Meeting Sonntag vorbereiten | critical | mindtrajour | adrian
5. Task-Management sauber finalisieren | high | openclaw | manne

### Bite Club
6. Supabase dietary restrictions + dishes übersetzen | medium | bite-club | enes
7. Content produzieren | medium | bite-club | adrian
8. Manne als Lead-Research-Tool ausbauen | low | bite-club | manne

### MindTrajour
9. Hero-Message präzisieren | high | mindtrajour | adrian
10. Above-the-fold Proof einbauen | high | mindtrajour | adrian
11. CTA-Struktur schärfen | high | mindtrajour | adrian
12. LP-Idee Candle-Chart einbauen | medium | mindtrajour | adrian
13. Aktien-Support | low | mindtrajour | enes
14. Trade-Bundles | low | mindtrajour | enes
15. Custom Strategy Builder | low | mindtrajour | enes
16. Changelog aufsetzen | low | mindtrajour | enes
17. Roadmap + Voting Feature | low | mindtrajour | adrian
18. Doku/Anleitung erstellen | low | mindtrajour | eve
19. Content produzieren | medium | mindtrajour | adrian
20. Lead Magnet definieren + bauen | medium | mindtrajour | adrian

### MindTrajour Dev (from Shortcut)
21. Renamings & small fixes — Feedback Markus Call | medium | mindtrajour | enes
22. Rework Asset Selector | medium | mindtrajour | enes
23. Import CSV Function | medium | mindtrajour | enes
24. Fix blurry Logo Dashboard-Export | low | mindtrajour | enes

### OpenClaw
25. "Text file" Email — 100 Fragen Schreibweise | low | openclaw | manne
26. GitHub-Anbindung | low | openclaw | manne
27. Gmail/Calendar Integration | medium | openclaw | manne
28. Obsidian-Anbindung | low | openclaw | manne

### AI Stromlaufplan
29. Erste Seite "Anschlussschema" fertig bauen | low | ai-stromlaufplan | adrian
30. Schaltplansymbole + Verdrahtung fixen | low | ai-stromlaufplan | adrian

## Phase 2 (nach MVP)
- Google Calendar Sync (Timeblocks aus Tasks generieren)
- Slack Integration (Tasks via Slack erstellen)
- Recurring Tasks
- Time Tracking
