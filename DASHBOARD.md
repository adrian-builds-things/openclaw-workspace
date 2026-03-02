---
cssclass: dashboard
---

<div class="title">COCKPIT</div>

# ⚡ Jetzt
- 🧭 Heute Fokus
  - [[tasks|Task-Ordner]]
  - **Top 1:** Bite Club Lead-Gen Asset shippen
  - **Top 2:** MindTrajour Money Pages live
  - **Top 3:** 5 echte Outreach-Kontakte starten
- ✅ Nächster Schritt (5 Min)
  - [[10-projects/bite-club/bite-club-todo|Bite Club TODO]] öffnen → 1 Blocker lösen

# 🗓️ Termine
- Diese Woche (Fix)
  - **Do 15:00** Schule Abholung (Rottweil)
  - **Do 16:15–17:00** Ergotherapie
  - **Fr 08:00–12:00** meist Rottweil
- Kalender / Planung
  - [[plans]]
  - [[tasks]]

# ✅ Aufgaben
- 🔥 Umsatz (Priorität)
  - [[00-cockpit/tasks-master|Master Tasks]]
  - [[00-cockpit/tasks-board|Task Board]]
  - [[00-cockpit/tasks-inbox|Tasks Inbox]]
  - [[00-cockpit/tasks-weekly-review-template|Weekly Review (10 Min)]]
  - [[10-projects/bite-club/bite-club-todo|Bite Club TODO]]
  - [[10-projects/mindtrajour/mindtrajour-todo|MindTrajour TODO]]
- 🧱 Build & Ops
  - [[tasks/brain_dump_2026-02-20|Brain Dump]]
  - [[HEARTBEAT]]
- 📥 Sammeln
  - [[00-inbox]]
  - [[30-resources/README|Resources]]

# 🚀 Projekte
- Bite Club
  - [[10-projects/bite-club/bite-club-todo|Bite Club TODO]]
  - [[memory/2026-02-21]]
- MindTrajour
  - [[10-projects/mindtrajour/mindtrajour-todo|MindTrajour TODO]]
  - [[plans/mindtrajour/sprint-planning-2026-02|Sprint Planning (Feb 2026)]]
  - [[plans/mindtrajour/roadmap-2026-02|Roadmap (Feb 2026)]]
  - [[plans/mindtrajour/quick-wins-2026-02|Quick Wins (Feb 2026)]]
  - [[plans/mindtrajour/specs|Specs]]
  - [[MEMORY]]
- OpenClaw
  - [[TOOLS]]
  - [[AGENTS]]

# 🧰 Navigation
- Daily
  - [[memory/2026-02-21]]
  - [[memory/2026-02-20]]
- Wissen
  - [[MEMORY]]
  - [[USER]]
  - [[knowledge/literature/literatur-liste|Literaturliste]]
- System
  - [[SOUL]]
  - [[IDENTITY]]

---

```dataview
TASK
FROM ""
WHERE !completed
AND (
  contains(file.path, "bite-club-todo") OR
  contains(file.path, "mindtrajour-todo") OR
  contains(file.path, "tasks/")
)
SORT file.mtime desc
LIMIT 12
```


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]


## Navigation
- [[NAVIGATION]]
