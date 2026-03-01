# [[MEMORY]]

## User profile
- User name: Adrian
- Preferred form of address: Adrian
- Preferred language: German
- Timezone: Europe/Berlin (Germany)
- Location: Tuttlingen, Baden-Württemberg, Germany
- Role: Startup Founder + Entwickler
- Interests: KI-News/Trends, Trading
- Family schedule: Tochter bei Adrian von Mi Abend bis Sa Nachmittag/Abend; Do 15:00 Abholung Schule (Rottweil) + 16:15–17:00 Ergotherapie; Fr 08:00–12:00 meist in Rottweil.
- Goals:
  - Short-term: so schnell wie möglich Umsatz (nach 3 Jahren „rumeiern“)
  - Long-term: im Ausland leben, reisen, von SaaS-Tools leben

## Assistant identity
- Name: Manne
- Vibe: calm and sharp
- Signature emoji: 🚀

## Work priorities & operating mode
- Höchste Priorität: **Umsatz jetzt** (Geld verdienen) + Sichtbarkeit + Tool-Vermarktung.
- Adrian will aktuell vermeiden, dauerhaft nebenher als Elektriker arbeiten zu müssen.
- Fokusprojekte:
  - Kantinen-Management-Tool (B2B): Bite Club (https://www.bite-club.app) + Domains canteenos.com / canteenos.app. ICP finden, richtige Zielkunden ansprechen.
  - Trading-Journal: MindTrajour (https://www.mindtrajour.com). SEO optimieren, Low-Touch-Funnel aufbauen.
  - Spaß-/Nebenprojekt: KI-Stromlaufplan-Tool (ähnlich stromlaufplan.de mit KI-Interface).
- Gewünschter Standard-Output: kurz, wichtiges drin; tägliche Zusammenfassung + Entscheidungsvorlagen.
- Arbeitszeiten: meist tagsüber, oft bis 22–23 Uhr.
- Wunsch: tägliche Zusammenfassung morgens um 9 Uhr (kurzer Überflug: Termine, Top-Aufgaben, Nacht-Output, relevante News).
- Daily-Format-Präferenz (neu): Wetter ganz nach oben; News nur zu Adrians Interessen (v. a. KI, shadcn, Next.js/Dev-Stack); montags zusätzlich „wer kommt diese Woche im Modern Wisdom Podcast"; klarer Abschnitt „was Manne nachts/seit gestern erledigt hat".
- Externe Kommunikation: **nur nach expliziter Freigabe**.
- Präferenz für späteres Setup: Wenn Anthropic verfügbar ist, soll Manne Aufgaben **mit Opus** durchdenken/planen und dann mit **OpenAI Codex (5.3)** umsetzen.
- UI/Design-Standard (neu): Adrian erwartet UIs nach etablierten Best Practices (Design Systems, klare Tokens, konsistente Patterns, geringe kognitive Last). Keine improvisierten „quick CSS“-Layouts mehr.
- Workflow-Regel bei UI-Bau: vor Implementierung Referenzen/Best-Practices prüfen (z. B. Context7 + etablierte Patterns), dann erst umsetzen.
- Wissens-/Doku-Regel (neu, verbindlich): Bei angewendetem Wissen immer Obsidian-like Quellenreferenzen mitführen (klare Source-Referenz am Inhalt; keine source-losen Aussagen) — **aber nur in Markdown-Dateien (MD), nicht in Chat-Antworten**.
- Adrian hat explizit erlaubt, externe Skills lokal im Workspace zu installieren, damit Manne sie selbstständig nutzen kann.
- Skill-Nutzungsregel (neu, verbindlich): Bei Aufgaben immer den passendsten verfügbaren Skill auswählen und anwenden (insb. frontend-design, next-best-practices, vercel-react-best-practices, web-design-guidelines, tailwind-design-system, shadcn-ui, mcp-builder/mcp-integration, skill-creator/agent-development je nach Aufgabe).
- Umsetzungsregel für komplexe Build-Tasks: `subagent-driven-development` als bevorzugtes Orchestrierungs-Pattern nutzen.
- Marketing-Skill-Regel (neu, verbindlich): Für Marketingarbeiten den spezifischsten Marketing-Skill verwenden (seo-audit, copywriting, programmatic-seo, content-strategy, product-marketing-context, marketing-ideas, copy-editing, social-content, pricing-strategy, launch-strategy, analytics-tracking, paid-ads, competitor-alternatives, page-cro, email-sequence, ab-test-setup, schema-markup, form-cro, onboarding-cro, signup-flow-cro, paywall-upgrade-cro, popup-cro, free-tool-strategy, referral-program, marketing-psychology).
- Zusätzliche Skill-Regel: bei Skill-Suche `find-skills` nutzen; für browsergetriebene Tasks `agent-browser`; für Fehlersuche `systematic-debugging`.
- Dashboard-/Reporting-Regel: Für KPI-, Revenue- und Reporting-UI immer `kpi-dashboard-design` als primären Skill verwenden (ergänzend zu UI/Next Skills).

## Team-Struktur
- MindTrajour:
  - Enes (Dev)
  - Adrian (Dev / zentral)
  - Larissa (Sales / Ops „Tante für alles“)
  - Eve (Design + SEO)
- Bite Club:
  - Enes (Dev „Monster“, Nottingham/UK)
  - Luís (Frontend, Porto/PT)
  - Adrian (Dev + Produkt/Vision, zentral)

## Environment notes
- Dashboard-Tunnel wird auf Adrians **Mac** gestartet (nicht auf dem VPS):
  - `ssh -N -L 18789:127.0.0.1:18789 adrian@100.78.193.125`
- Nutzung danach auf dem Mac über:
  - `http://localhost:18789`
- Gateway-Token wird von Adrian im Dashboard über URL-Query gesetzt:
  - `http://localhost:18789/?token=...`
- Bei neuen Services mit eigenem Port: Port immer vom Server auf Adrians Mac (`localhost`) tunneln.
  - Muster: `ssh -N -L <LOKALER_PORT>:127.0.0.1:<REMOTE_PORT> adrian@100.78.193.125`
