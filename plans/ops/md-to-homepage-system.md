# MD → Homepage System (Design + SEO)

## Ziel
Aus **einer Input-Markdown-Datei** in kurzer Zeit eine **gut designte** und **SEO-optimierte** Homepage erzeugen (inkl. klarer Struktur, Copy, Metadaten, Schema, CTA-Flow).

## Erfolgskriterien
- < 24h von Input bis veröffentlichter Seite
- Lighthouse SEO >= 95
- Core Web Vitals im grünen Bereich
- Klare Conversion-Route (Primary + Secondary CTA)
- Konsistentes UI (Tokens, Komponenten, Layout-Rhythmus)

## Benötigte Skills (Reihenfolge)
1. `product-marketing-context` – ICP, Jobs-to-be-done, Positionierung
2. `copywriting` – Hero, Nutzenargumentation, CTA-Sprache
3. `page-cro` – Struktur und Conversion-Pfad
4. `seo-audit` + `schema-markup` – On-page SEO, rich results
5. `frontend-design` + `tailwind-design-system` + `shadcn-ui` – sauberes UI
6. `next-best-practices` + `vercel-react-best-practices` – technische Umsetzung
7. `web-design-guidelines` + `verification-before-completion` – QA vor Abschluss

## Mindest-Input von Adrian (Input-MD Spec)
```md
# Page Brief

## 1) Offer
- Produktname:
- Kategorie:
- Preis/Modell:
- Primäres Ziel der Seite (z. B. Demo-Call, Signup, Purchase):

## 2) Zielgruppe
- ICP:
- Hauptproblem:
- Trigger-Moment:
- Einwand #1-3:

## 3) Nutzenversprechen
- Core Promise (1 Satz):
- Top 3 Outcomes:
- Differenzierung vs Alternativen:

## 4) Proof
- Zahlen/Ergebnisse:
- Testimonials:
- Logos/Referenzen:
- Screenshots/Assets:

## 5) SEO Input
- Hauptkeyword:
- Nebenkeywords:
- Suchintention:
- Region/Sprache:

## 6) Brand/Ton
- Tonalität:
- No-go Wörter:
- CTA-Stil:

## 7) Technik
- Ziel-Repo:
- Route (z. B. /canteen-software):
- Analytics Events:
```

## Output-Template (was erzeugt wird)
1. **PRD (`.md`)**
   - Seiten-Ziel, Zielgruppe, Messaging-Hierarchie, Block-Struktur
2. **SEO-Pack (`.md`)**
   - Title, Description, H1/H2 Plan, Internal Links, Schema JSON-LD
3. **UI-Spec (`.md`)**
   - Design-Tokens, Komponentenliste, Responsive-Regeln
4. **Implementation Tasks (`.md`)**
   - Kleine Codex-fähige Arbeitspakete
5. **Build (Code)**
   - Next.js Route + Komponenten + Metadata + Schema + Events
6. **QA-Report (`.md`)**
   - Design-, CRO-, SEO-, Performance-Checkliste

## Standard-Prozess (SOP)
1. Input-MD validieren (fehlende Pflichtfelder markieren)
2. Messaging + Seitenarchitektur ableiten
3. SEO-Struktur + Schema definieren
4. UI-Spec erstellen (Komponenten + Tokens)
5. Umsetzung in Next.js (modular, wiederverwendbar)
6. QA und Korrekturschleife
7. Publish + Tracking validieren

## Nächste Schritte (Handlungsanweisung)
1. ✅ Eine erste `input-md` Vorlage als Datei anlegen und fixieren (`templates/homepage-system/homepage-input-template.md`)
2. ✅ Kunden-Questionnaire erstellen (`templates/homepage-system/kunden-questionnaire-homepage.md`)
3. Für MindTrajour eine Test-Homepage mit echter Briefing-Datei pilotieren
4. Output-Artefakte als Standardordner definieren (`content/money-pages/<slug>/`)
5. QA-Gate verbindlich machen (ohne QA kein "fertig")
6. Nach 2-3 Piloten: aus dem Ablauf eine eigene Skill-Definition bauen

## Bot → Skill Routing (für Seiten-Umsetzung)
- **Manne (main, Orchestrierung)**
  - `find-skills`, `subagent-driven-development`, `agent-browser`
  - Aufgabe: Intake, Delegation, Reihenfolge/Gates, finaler Abgleich

- **Luna (CMO, Messaging/SEO/CRO)**
  - `product-marketing-context`, `copywriting`, `copy-editing`, `page-cro`, `seo-audit`, `schema-markup`, `analytics-tracking`
  - Aufgabe: Positionierung, Copy, SEO-Pack, CTA-Flow, Messplan

- **Pixel (CPO, UX/UI Spec)**
  - `frontend-design`, `tailwind-design-system`, `shadcn-ui`, `web-design-guidelines`
  - Aufgabe: Layout-System, Komponenten-Spec, visuelle Konsistenz

- **Max (CTO, Implementierung)**
  - `next-best-practices`, `vercel-react-best-practices`, `webapp-testing`
  - Aufgabe: Next.js Build, Performance, technische Qualität

- **Neo (Analyst, QA/Reporting)**
  - `analytics-tracking`, `verification-before-completion`
  - Aufgabe: KPI/Event-Validierung, QA-Report, Freigabeempfehlung

## Install-Status (2026-02-22)
Die relevanten Skills für den MD→Homepage-Flow sind im Workspace bereits installiert:
`find-skills`, `frontend-design`, `web-design-guidelines`, `vercel-react-best-practices`, `next-best-practices`, `tailwind-design-system`, `shadcn-ui`, `seo-audit`, `schema-markup`, `copywriting`, `copy-editing`, `page-cro`, `analytics-tracking`, `webapp-testing`, `subagent-driven-development`, `agent-browser`, `browser-use`.

## Pilot-Kandidaten
- MindTrajour: Landingpage für „Trading Journal für Options-Trader"
- Bite Club: B2B Seite „Kantinen-Vorbestellung gegen Lebensmittelverschwendung"
