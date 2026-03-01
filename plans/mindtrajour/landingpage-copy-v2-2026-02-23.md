# MindTrajour — Landing Page Copy V2 + Site-Struktur

> Erstellt: 23.02.2026 | Basiert auf: Draft V1, Meeting 22.02., Keyword Research, Google Ads Spec
> Status: Draft zur Review

---

## Teil 1: Site-Struktur & Linkmap

### URL-Struktur (Hub & Spoke)

```
mindtrajour.com/                          ← Homepage (Hub)
│
├── /pricing                              ← Pricing Page
├── /signup                               ← Signup / Free Trial
│
├── /features/                            ← Features Hub
│   ├── /features/options-trading-journal  ← Options-spezifisches Journaling
│   ├── /features/emotional-tracking      ← Emotionales Trading Tracking
│   ├── /features/trade-management        ← SL/TP Calculator, Multi-Leg
│   └── /features/performance-analytics   ← Dashboard, Charts, P&L
│
├── /vs-excel                             ← Comparison: vs Excel/Sheets
├── /vs-tradezella                        ← Comparison: vs TradeZella
├── /vs-tradersync                        ← Comparison: vs TraderSync
│
├── /blog/                                ← Blog Hub
│   ├── /blog/options-trading-journal-guide
│   ├── /blog/wheel-strategy-tracking
│   ├── /blog/trading-psychology-journal
│   └── ...
│
├── /docs/                                ← Documentation Hub
│   ├── /docs/getting-started
│   ├── /docs/trade-entry
│   ├── /docs/ticker-search-tips         ← inkl. SPX/^SPX Workaround
│   └── ...
│
└── /testimonials                         ← Social Proof Page (optional)
```

### Primary Keywords pro Seite

| URL | Primary Keyword (EN) | Primary Keyword (DE) | Prio |
|-----|---------------------|---------------------|------|
| `/` | options trading journal | Options Trading Journal App | 🔴 P0 |
| `/features/` | trading journal features | Trading Journal Funktionen | 🟡 P1 |
| `/features/options-trading-journal` | options trading journal software | Options Trading Journal Software | 🟡 P1 |
| `/features/emotional-tracking` | emotional trading tracking | Emotionales Trading Tracking | 🟡 P1 |
| `/features/trade-management` | options trade management tool | Trade Management Tool | 🟢 P2 |
| `/features/performance-analytics` | trading performance dashboard | Trading Performance Dashboard | 🟡 P1 |
| `/vs-excel` | trading journal vs Excel | Trading Journal vs Excel | 🔴 P0 |
| `/vs-tradezella` | TradeZella alternative | TradeZella Alternative | 🟡 P1 |
| `/vs-tradersync` | TraderSync alternative | TraderSync Alternative | 🟡 P1 |
| `/pricing` | trading journal pricing | Trading Journal Preise | 🔴 P0 |
| `/blog/` | (varies per post) | | 🟢 P2 |
| `/docs/` | (varies per doc) | | 🟢 P2 |

### Interne Linkstruktur

```
HOMEPAGE
  ├─→ /features/ (Nav + Feature-Section Links)
  ├─→ /pricing (Nav + CTA Buttons)
  ├─→ /vs-excel (Footer + "Switching from Excel?" inline link)
  ├─→ /vs-tradezella (Footer)
  ├─→ /vs-tradersync (Footer)
  ├─→ /blog/ (Nav)
  └─→ /docs/ (Nav)

FEATURE PAGES
  ├─→ Homepage (Breadcrumb + CTA)
  ├─→ /pricing (CTA)
  └─→ Other feature pages (Related Features sidebar)

COMPARISON PAGES
  ├─→ Homepage (Breadcrumb)
  ├─→ /pricing (CTA "See Pricing")
  ├─→ /features/ (Inline links to specific features)
  └─→ /signup (Primary CTA)

BLOG POSTS
  ├─→ Relevant feature page (contextual links)
  ├─→ Homepage (Breadcrumb)
  └─→ /signup (CTA)
```

### Build-Reihenfolge

1. **Homepage** (P0 — diese Woche)
2. **Pricing** (P0 — parallel)
3. **/vs-excel** (P0 — erste Ad-Landing-Page, DE Kampagne)
4. **/features/** Hub + Options Trading Journal Feature Page (P1)
5. **/vs-tradezella** + **/vs-tradersync** (P1)
6. Remaining feature pages (P1-P2)
7. Blog + Docs (P2, ongoing)

---

## Teil 2: Homepage Copy

### Meta Tags

**EN:**
- **Title:** `MindTrajour — Options Trading Journal for Serious Traders`
- **Description:** `The options trading journal app built for multi-leg strategies, emotional tracking, and real performance analysis. Log trades in 60 seconds. Free 7-day trial.`

**DE:**
- **Title:** `MindTrajour — Options Trading Journal für ernsthafte Trader`
- **Description:** `Die Options Trading Journal App für Multi-Leg-Strategien, emotionales Tracking und echte Performance-Analyse. Trades in 60 Sekunden erfassen. 7 Tage kostenlos testen.`

---

### ENGLISH VERSION

#### [SECTION 1: HERO]

**H1:** The truth hurts. A blown account hurts more.

**Subheadline:** MindTrajour is the options trading journal that tracks your strategies *and* your psychology. Log bull put spreads, iron condors, and multi-leg options in under 60 seconds — then discover why you're *really* losing money.

**CTA:** `Start Your Free 7-Day Trial` → /signup
**Micro-text:** No credit card required. Cancel anytime.

---

#### [SECTION 2: VIDEO + SOCIAL PROOF BAR]

**[Embedded Video: Marcos Review]**
*Caption: "See MindTrajour in action — real trader, real trades, no script."*

**Trust Bar (below video):**
> ⭐ 4.8/5 from options traders · "Finally, a journal that gets multi-leg" — Pietro · "Replaced my 47-tab spreadsheet" — Martin

---

#### [SECTION 3: PROBLEM → AGITATION → SOLUTION]

##### Your brain is your biggest drawdown.

You know the Greeks. You've mastered the Bull Put Spread. But when candles turn red, logic leaves the room. You move your stop-loss "just a few ticks." You revenge trade to get back what the market took.

The result? You're not trading a strategy. You're trading a mood.

##### Hope is not a strategy. It's a liability.

Your broker shows you the *what* — the red numbers. But never the *why.* Without a structured trading journal, you're stuck in an infinite loop of the same $1,000 mistakes. You're not a trader. You're a gambler with a laptop.

##### MindTrajour: The mirror you can't hide from.

We didn't build another spreadsheet. We built a performance analysis machine for options traders who are done lying to themselves.

- **Options-native:** Log multi-leg options and complex spreads in under 60 seconds. No more Excel wrestling.
- **Emotions vs. Equity:** See exactly how your fear and greed correlate with your win rate.
- **The truth, automated:** Instant charts, deep analytics, and a clear view of your real edge.

---

#### [SECTION 4: FEATURES]

##### Built for options traders. Not for tourists.

**01. Trade Logging in < 60 Seconds**
Most traders quit journaling because their trade log is a mess. MindTrajour is an options trading journal first. Log multi-leg options, bull put spreads, and iron condors in seconds — not minutes.
→ [Learn more about options trade logging](/features/options-trading-journal)

**02. The Dashboard of Truth**
Your broker hides your mistakes. We highlight them. Filter by strategy, market phase, or ticker. See your consistency — not just your P&L.
→ [Explore the performance dashboard](/features/performance-analytics)

**03. Emotional Tracking**
Numbers tell the story. Emotions tell the *why.* Log your state of mind before and after every trade. Correlate revenge trades with your drawdown.
→ [How emotional tracking works](/features/emotional-tracking)

**04. Trade Management Tools**
Pre-calculate stop loss and take profit before you enter. Configurable rules for spreads, condors, and single-leg positions.
→ [See trade management features](/features/trade-management)

---

#### [SECTION 5: TESTIMONIALS]

> *"I was using a 47-tab Excel monster. MindTrajour replaced it in a day. My P&L by strategy is finally accurate."*
> — **Martin**, Income Trader, 50+ trades/week

> *"The emotional tracking changed how I think about my Wheel strategy. I can see exactly when I deviate from my rules."*
> — **Pietro**, Wheel & Covered Call Trader

> *"I need per-leg closing for my spreads. MindTrajour is the only journal that actually understands multi-leg."*
> — **Levi**, 60k YouTube Audience

---

#### [SECTION 6: SWITCHING FROM EXCEL?]

**Still using a spreadsheet?** You're not alone. But your Excel sheet can't track P&L by strategy, correlate emotions with performance, or show you where your edge really is.

→ [See why traders are switching from Excel](/vs-excel)
→ [Compare MindTrajour vs TradeZella](/vs-tradezella)
→ [Compare MindTrajour vs TraderSync](/vs-tradersync)

---

#### [SECTION 7: PRICING TEASER]

**Simple pricing. No surprises.**
One plan. All features. Start free for 7 days.

→ [See pricing](/pricing)

---

#### [SECTION 8: FINAL CTA]

**Your future self is either thanking you or blaming you.**

Stop guessing. Start tracking. Get the options trading journal built by traders who were tired of losing money to their own emotions.

**[Start Your Free 7-Day Trial — $0]** → /signup
*No credit card. No strings. Just the truth.*

---

---

### DEUTSCHE VERSION

#### [ABSCHNITT 1: HERO]

**H1:** Die Wahrheit tut weh. Ein geplatztes Konto noch mehr.

**Subheadline:** MindTrajour ist das Options Trading Journal, das deine Strategien *und* deine Psyche trackt. Erfasse Bull Put Spreads, Iron Condors und Multi-Leg-Optionen in unter 60 Sekunden — und finde endlich heraus, warum du *wirklich* Geld verlierst.

**CTA:** `Starte deine kostenlose 7-Tage-Testphase` → /signup
**Micro-text:** Keine Kreditkarte nötig. Jederzeit kündbar.

---

#### [ABSCHNITT 2: VIDEO + SOCIAL PROOF BAR]

**[Eingebettetes Video: Marcos Review]**
*Caption: "MindTrajour in Aktion — echter Trader, echte Trades, kein Skript."*

**Trust Bar:**
> ⭐ 4.8/5 von Options-Tradern · "Endlich ein Journal, das Multi-Leg versteht" — Pietro · "Hat meine 47-Tab-Tabelle ersetzt" — Martin

---

#### [ABSCHNITT 3: PROBLEM → AGITATION → LÖSUNG]

##### Dein Gehirn ist dein größter Drawdown.

Du kennst die Griechen. Du hast den Bull Put Spread drauf. Aber wenn die Kerzen rot werden, ist die Logik weg. Du verschiebst den Stop-Loss "nur ein paar Ticks." Du machst einen Revenge-Trade, um dir zurückzuholen, was der Markt genommen hat.

Das Ergebnis? Du tradest keine Strategie. Du tradest eine Laune.

##### Hoffnung ist keine Strategie. Sie ist ein Risiko.

Dein Broker zeigt dir das *Was* — die roten Zahlen. Aber nie das *Warum.* Ohne ein strukturiertes Trading-Journal steckst du in einer Endlosschleife der gleichen 1.000-Euro-Fehler. Du bist kein Trader. Du bist ein Zocker mit Laptop.

##### MindTrajour: Der Spiegel, vor dem du nicht weglaufen kannst.

Wir haben keine neue Tabelle gebaut. Wir haben eine Performance-Analyse-Maschine für Options-Trader gebaut, die aufgehört haben, sich selbst zu belügen.

- **Options-nativ:** Multi-Leg-Optionen und komplexe Spreads in unter 60 Sekunden erfassen. Kein Excel-Kampf mehr.
- **Emotionen vs. Eigenkapital:** Sieh genau, wie deine Angst und Gier mit deiner Win-Rate korrelieren.
- **Die Wahrheit, automatisiert:** Sofortige Charts, tiefe Analysen und ein klarer Blick auf deinen echten Edge.

---

#### [ABSCHNITT 4: FEATURES]

##### Gebaut für Options-Trader. Nicht für Touristen.

**01. Trade-Erfassung in < 60 Sekunden**
Die meisten Trader hören auf zu journalisieren, weil ihr Trade-Log ein Chaos ist. MindTrajour ist von Anfang an ein Options Trading Journal. Erfasse Multi-Leg-Optionen, Bull Put Spreads und Iron Condors in Sekunden.
→ [Mehr über Options-Trade-Logging](/features/options-trading-journal)

**02. Das Dashboard der Wahrheit**
Dein Broker versteckt deine Fehler. Wir zeigen sie dir. Filtere nach Strategie, Marktphase oder Ticker. Sieh deine Konsistenz — nicht nur dein P&L.
→ [Performance Dashboard entdecken](/features/performance-analytics)

**03. Emotionales Tracking**
Zahlen erzählen die Geschichte. Emotionen das *Warum.* Protokolliere deinen Zustand vor und nach jedem Trade. Korreliere Revenge-Trades mit deinem Drawdown.
→ [Wie emotionales Tracking funktioniert](/features/emotional-tracking)

**04. Trade Management Tools**
Berechne Stop Loss und Take Profit vorab. Konfigurierbare Regeln für Spreads, Condors und Single-Leg-Positionen.
→ [Trade Management Features ansehen](/features/trade-management)

---

#### [ABSCHNITT 5: TESTIMONIALS]

> *"Ich hatte ein 47-Tab-Excel-Monster. MindTrajour hat es an einem Tag ersetzt. Mein P&L nach Strategie stimmt endlich."*
> — **Martin**, Income Trader, 50+ Trades/Woche

> *"Das emotionale Tracking hat verändert, wie ich über meine Wheel-Strategie denke. Ich sehe genau, wann ich von meinen Regeln abweiche."*
> — **Pietro**, Wheel & Covered Call Trader

> *"Ich brauche Per-Leg Closing für meine Spreads. MindTrajour ist das einzige Journal, das Multi-Leg wirklich versteht."*
> — **Levi**, 60k YouTube Audience

---

#### [ABSCHNITT 6: WECHSEL VON EXCEL?]

**Nutzt du noch eine Tabelle?** Damit bist du nicht allein. Aber dein Excel kann kein P&L nach Strategie tracken, keine Emotionen mit Performance korrelieren, und dir nicht zeigen, wo dein Edge wirklich liegt.

→ [Warum Trader von Excel wechseln](/vs-excel)
→ [MindTrajour vs TradeZella vergleichen](/vs-tradezella)
→ [MindTrajour vs TraderSync vergleichen](/vs-tradersync)

---

#### [ABSCHNITT 7: PRICING TEASER]

**Einfache Preise. Keine Überraschungen.**
Ein Plan. Alle Features. 7 Tage kostenlos starten.

→ [Preise ansehen](/pricing)

---

#### [ABSCHNITT 8: FINALER CTA]

**Dein zukünftiges Ich dankt dir — oder verflucht dich.**

Hör auf zu raten. Fang an zu tracken. Hol dir das Options Trading Journal von Tradern, die es satt hatten, Geld an ihre eigenen Emotionen zu verlieren.

**[7 Tage kostenlos starten]** → /signup
*Keine Kreditkarte. Keine Haken. Nur die Wahrheit.*

---

---

## Teil 3: Subpage-Strukturen (Outline)

### /vs-excel

- **Primary Keyword:** `trading journal vs Excel` / `options trading spreadsheet alternative`
- **H1:** Your options trading spreadsheet is lying to you.
- **Meta Description:** `Still tracking options in Excel? See why serious traders switch to MindTrajour — automatic P&L by strategy, emotional tracking, and multi-leg support.`
- **Sections:**
  1. Hero: Pain of Excel (formula errors, manual linking, no strategy P&L)
  2. Side-by-side comparison table (Excel vs MindTrajour)
  3. 3 specific pain points with examples
  4. Testimonial (Martin — replaced his spreadsheet)
  5. CTA: "Import your first trades"
- **Internal Links:** → /features/options-trading-journal, → /pricing, → /signup

---

### /vs-tradezella

- **Primary Keyword:** `TradeZella alternative` / `TradeZella vs MindTrajour`
- **H1:** TradeZella is powerful. Here's where MindTrajour fits better.
- **Meta Description:** `Comparing TradeZella and MindTrajour? See the honest differences — options focus, German support, pricing, and strategy-level P&L.`
- **Sections:**
  1. Hero: Acknowledge TradeZella, differentiate honestly
  2. Comparison table (where each wins)
  3. German/European trader advantages (language, support, payment)
  4. Pricing comparison
  5. CTA: "Try MindTrajour free — no card required"
- **Internal Links:** → /features/, → /pricing, → /signup

---

### /vs-tradersync

- **Primary Keyword:** `TraderSync alternative`
- **H1:** TraderSync does a lot. MindTrajour does options better.
- **Meta Description:** `Looking for a TraderSync alternative focused on options? MindTrajour offers multi-leg support, emotional tracking, and strategy-level analytics.`
- **Sections:**
  1. Hero: TraderSync = generalist, MindTrajour = options specialist
  2. Comparison table
  3. Options-specific advantages
  4. CTA: "Start free trial"
- **Internal Links:** → /features/options-trading-journal, → /pricing, → /signup

---

### /features/ (Hub)

- **Primary Keyword:** `trading journal features`
- **H1:** Everything you need. Nothing you don't.
- **Meta Description:** `Explore MindTrajour's features: options trade logging, emotional tracking, performance analytics, trade management tools, and more.`
- **Sections:**
  1. Feature grid (4 cards linking to sub-feature pages)
  2. Quick comparison: "What makes us different"
  3. CTA: "Try it free"
- **Internal Links:** → each /features/* subpage, → /pricing, → /signup

---

### /features/options-trading-journal

- **Primary Keyword:** `options trading journal software`
- **H1:** Log any options trade in under 60 seconds.
- **Meta Description:** `Multi-leg options, bull put spreads, iron condors — log them all in seconds. MindTrajour is the options trading journal built for real strategies.`
- **Sections:**
  1. Hero: Speed + complexity handled
  2. Supported strategies (single-leg, spreads, condors, strangles, Wheel)
  3. Screenshot/demo of trade entry
  4. Comparison to Excel workflow
  5. CTA
- **Internal Links:** → /features/, → /vs-excel, → /pricing

---

### /features/emotional-tracking

- **Primary Keyword:** `emotional trading tracking` / `trading psychology journal`
- **H1:** Your emotions are costing you money. Now you can prove it.
- **Meta Description:** `Track your emotional state before and after every trade. See how fear, greed, and revenge trading correlate with your P&L.`
- **Sections:**
  1. Hero: The hidden cost of emotions
  2. How it works (log emotion → correlate with outcome)
  3. Example: Revenge trade correlation chart
  4. CTA
- **Internal Links:** → /features/, → /blog/trading-psychology-journal

---

### /features/trade-management

- **Primary Keyword:** `options trade management tool`
- **H1:** Know your exits before you enter.
- **Meta Description:** `Pre-calculate stop loss and take profit for spreads, condors, and single-leg options. Built-in trade management for serious options traders.`
- **Sections:**
  1. Hero: SL/TP for multi-leg
  2. Calculation logic (credit spread vs debit spread)
  3. Default fees setup
  4. CTA
- **Internal Links:** → /features/, → /pricing

---

### /features/performance-analytics

- **Primary Keyword:** `trading performance dashboard`
- **H1:** The numbers don't lie. Your broker just hides them.
- **Meta Description:** `Filter your trading performance by strategy, ticker, and time. See win rate, P&L, consistency, and where your real edge is.`
- **Sections:**
  1. Hero: Beyond P&L
  2. Dashboard screenshots (filter by strategy, charts)
  3. Key metrics explained
  4. CTA
- **Internal Links:** → /features/, → /pricing

---

### /pricing

- **Primary Keyword:** `trading journal pricing`
- **H1:** One plan. All features. No surprises.
- **Meta Description:** `MindTrajour pricing: full access to all features. Start with a free 7-day trial. No credit card required.`
- **Sections:**
  1. Pricing card (single plan, monthly/annual toggle)
  2. What's included (feature checklist)
  3. FAQ (billing, cancellation, trial)
  4. Comparison to competitors (if favorable)
  5. CTA: "Start free trial"
- **Internal Links:** → /signup, → /features/

---

### /blog/ (Struktur)

- **Hub Page:** Latest posts + categories
- **Planned Post Categories:**
  - Options Strategy Guides (Wheel, Covered Call, Spreads)
  - Trading Psychology
  - Journal Best Practices
  - Tool Comparisons (programmatic SEO potential)
- **First Posts (P1):**
  - "Why Every Options Trader Needs a Journal (And Excel Isn't One)"
  - "How to Track Your Wheel Strategy: A Complete Guide"
  - "The Psychology of Revenge Trading: How to Break the Cycle"
- **Internal Links:** Each post → relevant feature page + /signup CTA

---

### /docs/ (Struktur)

- **Hub Page:** Getting Started + Feature Docs + FAQ
- **Planned Sections:**
  - Getting Started (signup, first trade, dashboard overview)
  - Trade Entry (single-leg, multi-leg, expiration shortcuts)
  - Ticker Search Tips (SPX → ^SPX, DAX → ^GDAXI etc.)
  - Settings (default fees, notifications)
  - FAQ
- **Internal Links:** Each doc → relevant feature page
- **SEO Value:** Long-tail keywords, helps with "how to use" queries

---

## SEO Keywords (Combined)

### English
- options trading journal (primary — homepage)
- trading journal app
- options trading journal software
- trading performance dashboard
- trading journal vs Excel
- TradeZella alternative
- TraderSync alternative
- emotional trading tracking
- trading psychology journal
- bull put spread tracker
- multi-leg options journal
- trade management tool
- options trade log

### Deutsch
- Options Trading Journal App
- Trading Journal für Optionen
- Trading Performance Dashboard
- Trading Journal vs Excel
- Emotionales Trading Tracking
- Trading Tagebuch App
- Optionen Trading Journal Software
- Bull Put Spread Tracker
- Multi-Leg Optionen Journal
