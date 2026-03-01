# Skills Usage Rules (Audit)

Stand: 2026-02-16

## Ergebnis der Prüfung
- Installierte Skills mit `SKILL.md`: **44**
- Für alle existiert eine Trigger-Description in `SKILL.md`.
- In MEMORY sind globale Nutzungsregeln für Skill-Auswahl hinterlegt.

## Entscheidungslogik (verbindlich)
1. Immer den **spezifischsten** Skill wählen.
2. Bei Unsicherheit zuerst `find-skills` nutzen.
3. Kombinationen nur wenn nötig (z. B. `kpi-dashboard-design` + `shadcn-ui` + `next-best-practices`).

## Priorisierte Skill-Zuordnung nach Aufgabentyp

### UI / Frontend
- `frontend-design`
- `web-design-guidelines`
- `tailwind-design-system`
- `shadcn-ui`
- `vercel-react-best-practices`
- `next-best-practices`

### Dashboard / KPI / Revenue
- `kpi-dashboard-design` (primär)
- plus UI/Frontend Skills je nach Bedarf

### Marketing
- Strategie: `content-strategy`, `product-marketing-context`, `marketing-ideas`
- Content: `social-content`, `copywriting`, `copy-editing`, `email-sequence`
- Growth/CRO: `page-cro`, `form-cro`, `onboarding-cro`, `signup-flow-cro`, `paywall-upgrade-cro`, `popup-cro`, `ab-test-setup`, `analytics-tracking`
- SEO: `seo-audit`, `programmatic-seo`, `schema-markup`, `competitor-alternatives`
- Distribution: `paid-ads`, `referral-program`, `free-tool-strategy`, `launch-strategy`, `pricing-strategy`, `marketing-psychology`

### Engineering / Debug / Execution
- Debugging: `systematic-debugging`
- Quality gate: `verification-before-completion`, `webapp-testing`
- Orchestrierung: `subagent-driven-development`
- MCP: `mcp-builder`, `mcp-integration`

### Browser Research
- `agent-browser`, `browser-use`

## Hinweis
Nach Skill-Installationen ist ein Neustart/Neuer Chat empfehlenswert, damit die Skills sicher in die aktive Skill-Liste übernommen werden.
