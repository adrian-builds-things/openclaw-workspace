# MindTrajour Sprint Planning — February 2026

> **Sources:** In-depth interview Pietro × Larissa (02.02.2026, 62 min) · Consolidated User Feedback Feb 2026 (~15 users) · Levi Woods Partnership Call (29.09., 77 min)
> **Strategic Goal:** From entry-level tool to trading companion for professional traders
> **Roadmap:** [→ View full roadmap (Now / Next / Later)](./roadmap-2026-02.md) · [→ Quick Wins checklist](./quick-wins-2026-02.md)
> **Navigation:** [→ Dashboard](../../DASHBOARD.md) · [→ Specs folder](./specs/)

---

## Sprint Planning Agenda

| Time | Topic | Owner |
|------|-------|-------|
| 00–05 | Check-in & meeting goals | Adrian |
| 05–15 | Research overview: 3 sources, what did we learn? | Larissa |
| 15–35 | 11 Core Findings: walkthrough + discussion | Larissa + Team |
| 35–45 | Strategic framing: Levi partnership as growth lever | Adrian |
| 45–65 | Sprint prioritization: which stories make the cut? | All |
| 65–80 | Create stories in Shortcut + estimate | Enes + Team |
| 80–90 | Owners, target dates, next steps | Adrian |

---

## User Segments

| Segment | Representative | Status | Core Problem |
|---------|---------------|--------|--------------|
| Power Trader | Martin (50–100 trades/day) | 🔴 Blocked | No broker import |
| Complex Strategist | Levi Woods (60k YT, 76 active trades) | 🟡 Interested | Trade Bundles + Per-Leg Closing missing |
| Intermediate | Pietro (Wheel + Hedging) | 🟡 Dual-tool | Running parallel with TraderSync |
| Active Users | Gerhard, Ulrich, Roland, others | 🟢 Active | Want more features |
| Churned | Thomas | ⚫ Cancelled | "Too basic for serious traders" |
| Onboarding Problem | Patrick, Jörg | 🔴 Lost | Login/signup bugs |

---

## ⭐ Strategic Opportunity: Levi Woods Partnership

> **Context:** Levi Woods is a YouTube educator with 60,000 subscribers (many German-speaking), 8+ years of trading experience, and currently sells his own options spreadsheets. He is actively looking for an app to replace his spreadsheets and is open to a Revenue Share / Equity partnership.

**His preconditions for promotion — only 2 things need to be implemented:**

1. **Trade Bundles** — the ability to group multiple individual transactions under one named strategy
2. **Per-Leg Closing** — the ability to close individual legs of a multi-leg trade independently

**Levi's exact words:** *"When you guys are at a point where that reference is in there, and then I can start logging [...] we'll get on the phone again, and I'll give you guys some real feedback."*

**Why this matters:**
- 60k subscribers = potentially the largest single user acquisition channel to date
- He would recommend MindTrajour to his own audience as a replacement for his spreadsheets
- Subscription model (vs. one-time payment) would be an upgrade even for him
- Revenue Share / Equity as incentive — he is not in a rush, but open

**Next steps with Levi:**
- Email him once Trade Bundles + Per-Leg Closing are live
- No financial commitments needed before feature implementation

---

## 11 Core Findings (prioritized by frequency × impact)

### F1 — Trade Bundles: Grouping Transactions into Strategies 🔴 CRITICAL
**Sources:** Pietro interview + Levi call + 12+ user feedback items | **Confidence:** very high

**What:** The ability to group multiple individual transactions under a single named strategy — e.g., all the puts, rolls, assignments, and covered calls that make up one Wheel run on AAPL are tagged as "Wheel AAPL Q1 2026" and can be viewed and analyzed as a single unit.

**Why it matters:** Options strategies like Wheel, Covered Calls, Calendar Spreads, and dividend-capture trades are inherently composed of sequences of related transactions. Without grouping:
- There is no aggregate P&L for the full strategy — only individual trade P&L
- It is impossible to tell whether a strategy is still open or fully closed
- Win/loss metrics are meaningless — e.g., winning the covered call leg while losing on assignment is not captured correctly
- Traders cannot compare strategy performance over time across different underlyings

This is not a nice-to-have. It is the fundamental missing concept that prevents any serious options trader from using MindTrajour as their primary tool. Pietro, Levi, and 12+ other users independently confirm this gap.

**Pietro:** *"I run a Wheel strategy on Apple — for that I need 3–5 trades as one logical unit."*
**Levi:** *"My trade reference is the only thing that keeps me sane. All I need is one text input field — and all of a sudden you'd be able to recreate a log of 470 trades off of one line of entry."*

**Competitive displacement:** TraderSync (Pietro) and Levi's own spreadsheets. Both would be replaced by this feature.

---

### F2 — Custom Strategy Types 🔴 CRITICAL
**Sources:** Levi call | **Confidence:** high

**What:** Levi actively trades structurally distinct multi-leg options strategies — diagonal spreads, calendar spreads, covered calls, and others. Each strategy type has a different risk profile, different success criteria, and different questions a trader asks ("is this calendar spread working?"). The app currently treats all trades as generic entries and has no concept of strategy type.

**Why it matters:** Without the ability to categorize trades by strategy type, traders cannot:
- Get analytics that are meaningful for a specific strategy (e.g., average return on calendar spreads vs. diagonals)
- Understand whether a strategy they use systematically is profitable over time
- Distinguish between an experiment and a repeatable approach

Trade Bundles (F1) tell you *which* transactions belong together. Strategy Types tell you *what kind of strategy* a bundle represents. Both are needed for Levi to fully replace his spreadsheets with MindTrajour.

**Levi's current workaround:** Manually built spreadsheet tabs per strategy type — one tab per strategy, hand-tracked over 8 years. This is what MindTrajour needs to replace.

**Connection to partnership:** F1 is Levi's stated precondition for promotion. F2 is the layer that makes MindTrajour genuinely superior to his spreadsheets — the real long-term hook for the partnership.

---

### F3 — Login / Signup Bugs Are Blocking Revenue 🔴 CRITICAL
**Sources:** User feedback | **Confidence:** very high | **Effort:** 1–2 days

Patrick cannot log in. Jörg receives no confirmation email and his discount code is broken. Both are warm YouTube leads — they never converted. With active Google Ads budget running, we are currently spending money on users we lose to a bug.

---

### F4 — "Expired Worthless" Button Missing 🔴 HIGH / Quick Win
**Sources:** User feedback (8+ users) | **Confidence:** high | **Effort:** ~0.5 days

Options that expire worthless are not captured in statistics → win rate, P&L, and all metrics are distorted. Gerhard: *"If my put option expires worthless, that is my maximum profit — but MindTrajour doesn't show me that."*

---

### F5 — Per-Leg Closing (Close Individual Legs Independently) 🔴 HIGH
**Sources:** Levi call (demonstrated live) | **Confidence:** very high | **Effort:** 2–3 days

Levi demonstrated live: on a bull-put spread, he wants to close only the long leg (let it expire worthless) while keeping the short leg active. Currently, both legs must be closed together — this blocks all complex multi-leg strategies.

**Levi:** *"Each trade is individual. I would never take that off as two, because I want to leave my long leg on as a bonus."*

**Direct connection:** This is one of Levi's two preconditions for active use and potential promotion.

---

### F6 — Incomplete Transaction Type Coverage 🟡 HIGH
**Sources:** Levi call | **Confidence:** high | **Effort:** 1–2 days

**What:** Options traders interact with the market through a clearly defined set of transaction types. MindTrajour does not support the full range of transactions that are part of everyday trading — this means traders cannot accurately log their activity, and key events like dividends or directional stock trades go untracked.

**Why it matters:** If a trader cannot log all their transaction types, their journal is incomplete by definition. P&L is wrong, position tracking is wrong, and the app fails at its core job. This affects any trader who combines options with stock positions or dividends — which describes the Wheel, Covered Call, and most income strategies.

Levi mapped out the complete required set:
1. Buy Stock
2. Sell Stock
3. Sell to Open Call
4. Buy to Close Call
5. Sell to Open Put
6. Buy to Close Put
7. Dividend received
8. Dividend paid (on assigned short shares)

*"There's only eight. If the leg dropdown had those eight options, all of a sudden you'd be able to track everything."*

---

### F7 — Trust-Breaking UX Bugs 🟡 MEDIUM → HIGH
**Sources:** Pietro interview + user feedback (5+ users) | **Confidence:** very high (confirmed live on screen share)

- **Bug 1:** Monthly bars in charts displayed in random order — confirmed live on Pietro's screen share
- **Bug 2:** Filter reset in Safari — all filters revert on page reload (Jennifer, Christin)
- **Bug 3:** Decimal separator — EU users have issues with comma vs. period

---

### F8 — Broker Import (IB / CapTrader / CSV) 🔴 HIGH — Adoption Blocker
**Sources:** User feedback (Martin + Levi call) | **Confidence:** high | **Effort:** 5–8 days (Q2)

**What:** Active traders execute far more trades than any journal can absorb through manual entry. Both Martin (50–100 trades/day) and Levi (76 active positions) hit this wall directly — the time cost of manual logging makes the app unusable as a primary tool at their volume.

**Why it matters:** This is a hard adoption ceiling for power users. MindTrajour can build every feature on the list, but a trader with 50 trades per day will never become a daily active user if the onboarding cost is 2 hours of data entry.

Levi: *"As an active trader, there's no way, I just don't have time."*

**Not this sprint** — but commit to Martin and Levi with a concrete Q2 timeline.

---

### F9 — Custom Tags + Behavioral Analytics 🟡 HIGH — Differentiation
**Sources:** Pietro interview | **Confidence:** high | **Effort:** 2–3 days (Tags MVP)

Pietro discovered a $10,000 emotional trading error through tag-based analysis in TraderSync. *"On FOMO trades I always lose. That saved me $10,000. I want that in MindTrajour."* This is the core differentiator between a trading journal and a real trading coach.

---

### F10 — Multi-Currency Support 🟡 MEDIUM
**Sources:** Pietro, Martin | **Confidence:** medium-high | **Effort:** 2–3 days (Q2)

Pietro: EUR + HKD. Martin: EUR account, USD products. All P&L shown without currency conversion.

---

### F11 — "Beginner Tool" Perception — Strategic Positioning Gap
**Type:** Cross-sprint | **Three independent confirmations:** Thomas (churned), Pietro (dual-tool), Levi (not yet a full user)

Thomas cancelled because it was "too basic." Pietro runs TraderSync in parallel. Levi cannot fully use the app yet. This is not a feature gap — it is a product positioning problem that resolves itself once F1 + F4 + F5 + F9 are built.

---

## Chart Data API Migration 🟡 HIGH — Infrastructure

**Source:** Adrian (internal observation) | **Confidence:** high

**Problem:** MindTrajour currently pulls chart data from Yahoo Finance. Several issues are emerging:
- **Data quality:** Ticker `X` (U.S. Steel Corp) is not displaying correctly — significant data gaps in the chart
- **Free tier risk:** Unclear how long the current free tier access will remain sufficient as the user base grows
- **Reliability:** Yahoo Finance is an unofficial/undocumented API — subject to breaking changes without notice

**Why it matters now:** Incorrect or missing chart data directly undermines trader trust. A professional trader seeing gaps in $X data will question the reliability of all data.

**Potential alternatives:** Polygon.io, Alpha Vantage, Tiingo, IEX Cloud (to be evaluated — Adrian has research to share).

**Note:** Levi also raised the cost of option chain data separately (ORATS) — the API strategy may need to address both market data and options chain data together.

**Action:** Adrian to share existing API research → Enes evaluates migration effort → decision in next sprint.

---

## Spec Index

| Spec | Area | Status | File |
|------|------|--------|------|
| SPEC-01 | Stock Support | Draft | [→ Open](./specs/spec-01-stock-support.md) |
| SPEC-02 | Trade Bundles | Draft | [→ Open](./specs/spec-02-trade-bundles.md) |
| SPEC-03 | Option Lifecycle Actions | Draft | [→ Open](./specs/spec-03-option-lifecycle-actions.md) |
| SPEC-04 | Custom Strategy Builder | Draft | [→ Open](./specs/spec-04-custom-strategy-builder.md) |
| SPEC-DEFAULT-FEES | Default Transaction Fees | Draft | [→ Open](./specs/spec-default-fees.md) |
| SPEC-GROWTH-KR | Keyword Research | In Progress | [→ Open](./specs/spec-growth-keyword-research.md) |
| SPEC-GROWTH-SEO | SEO Strategy | Draft | [→ Open](./specs/spec-growth-seo.md) |
| SPEC-GROWTH-ADS | Google Ads Prerequisites | Draft | [→ Open](./specs/spec-growth-google-ads-prerequisites.md) |
| SPEC-ROADMAP | Public Roadmap & Feature Voting | Draft | [→ Open](./specs/spec-public-roadmap-voting.md) |
| SPEC-CHANGELOG | Automated Changelog System | Implemented | [→ Open](./specs/spec-changelog.md) |
| SPEC-DOCUMENTATION | Feature Documentation & SEO Knowledge Base | Draft | [→ Open](./specs/spec-documentation.md) |
| SPEC-TRADE-MANAGEMENT | Trade Management Tool (SL/TP Calculator) | Draft | [→ Open](./specs/spec-trade-management.md) |

---

## ⚡ Quick Wins

> **[→ Open Quick Wins Overview](./quick-wins-2026-02.md)** — 7 stories, all shippable independently, < 2 days each. Includes the Shortcut story checklist.

Items: Login/Signup Bugs (QW-1), "Expired Worthless" button (QW-2), Default Transaction Fees (QW-3), 3 UX/trust bugs (QW-4), Close Type dropdown (QW-5).

---

## Recommended Focus Areas

*These are open problem areas to be discussed and prioritized in the sprint planning meeting. Actual tickets are created in Shortcut based on this discussion.*

---

### 🔴 Supabase Database Cleanup — Must Be Done First

**What:** Cleanup work on the Supabase database. Must be completed before other development work proceeds.

**Owner:** Enes
**Priority:** Immediate — blocks subsequent development work
**Status:** Not yet started

---

### 🟡 Keyword Research — Shared Upstream Dependency

**What:** A prioritized keyword list covering all clusters: core product terms ("options trading journal"), comparison/switch terms ("trading journal vs Excel," "TraderSync alternative"), strategy-specific terms ("Wheel strategy tracker"), and income trader terms. The list includes monthly search volume estimates, competition level, target page per keyword, and current Google ranking position.

**Why it is its own block:** Keyword Research has no upstream dependencies of its own, but two otherwise independent specs both depend on it — [SPEC-GROWTH-seo.md](./specs/spec-growth-seo.md) (Technical SEO meta copy, Organic Content topics) and [SPEC-GROWTH-google-ads-prerequisites.md](./specs/spec-growth-google-ads-prerequisites.md) (Landing Page Copy, Ad-Specific LPs). This shared dependency is the structural proof that Keyword Research is a standalone deliverable, not a subtask of either spec.

**Owner:** Larissa + Eve
**Status:** A preliminary cluster list exists. Full prioritization with search volume + competition data is pending.

**Tool:** `marketing:seo-audit` skill (Cowork) can execute this automatically — provides keyword research, on-page analysis, content gap analysis, and competitor comparison. See [SPEC-GROWTH-keyword-research.md](./specs/spec-growth-keyword-research.md) for full details and execution instructions.

**See [SPEC-GROWTH-keyword-research.md](./specs/spec-growth-keyword-research.md)** for deliverable definition, keyword clusters, and open questions.

---

### 🔴 SEO — CRITICAL / Time-Sensitive (upstream prerequisite for Google Ads)

**What:** With the keyword list in place, MindTrajour needs technical SEO hygiene and on-page alignment before Google Ads can be run profitably. SEO is also the foundation for long-term organic traffic — reducing dependence on paid spend over time.

**Why it matters:** Google assigns a Quality Score to each ad based on keyword relevance and landing page quality. Poor Technical SEO directly raises cost-per-click.

**The two workstreams (see [SPEC-GROWTH-seo.md](./specs/spec-growth-seo.md) for details):**

**1 — Technical SEO** *(depends on Keyword Research above)*
Keyword-aligned meta titles and descriptions on all pages, Core Web Vitals passing, structured data (SoftwareApplication schema), indexability audit. This is a hard prerequisite for Google Ads — without it, Quality Scores suffer and CPC rises.

**2 — Organic Content Strategy** *(longer horizon)*
Blog content targeting the keyword clusters — strategy-specific guides, comparison articles, educational content. This is the long-term free traffic channel; execution can be deferred relative to the Google Ads launch.

**Dependency:** Keyword Research (above) → Technical SEO → Google Ads launch. See [SPEC-GROWTH-seo.md](./specs/spec-growth-seo.md).

---

### 🔴 Google Ads — CRITICAL / Time-Sensitive (depends on SEO above)

**What:** With SEO in place as the foundation, MindTrajour needs campaign-specific infrastructure to convert paid traffic profitably: intent-matched landing pages and conversion measurement.

**Why it matters:** Sending paid traffic to a generic homepage wastes every click. Each campaign keyword represents a searcher with a specific intent — only a page built for that intent converts. Without PostHog tracking, there is no feedback loop: no way to know which campaign, page, or step in the funnel is working.

**The four workstreams (see [SPEC-GROWTH-google-ads-prerequisites.md](./specs/spec-growth-google-ads-prerequisites.md) for details):**

**1 — Main Landing Page Copy** *(depends on Keyword Research from SEO)*
Conversion-focused rewrite of the main landing page in the language of options traders: "Wheel strategy," "covered calls," "P&L by strategy," "multi-leg spreads." This page is the core value proposition — all ad-specific pages derive from it.

**2 — Ad-Specific Landing Pages** *(depends on Technical SEO + Main LP Copy)*
One dedicated page per campaign, each built to match the exact search intent: **vs Excel** (for traders using spreadsheets, side-by-side comparison), **vs TraderSync** (for product-aware traders evaluating alternatives), **Options Trading Journal** (general intent, top of funnel).

**3 — PostHog Events** *(depends on pages finalized)*
Business-centric event architecture — 5 Customer Events (milestones) + 6 Product Events (flow analysis) + 1 Interaction Event. Full event table with parameters and cardinality warnings in [SPEC-GROWTH-google-ads-prerequisites.md](./specs/spec-growth-google-ads-prerequisites.md).

**4 — PostHog Funnels** *(depends on events live)*
Configured funnel: `landing_page_viewed` → `signup_flow_started` → `account_created` → `account_activated` → `trade_first_logged` → `subscription_created`. Segmentable by traffic source and landing page variant.

**Dependency:** Keyword Research (SEO) → Technical SEO (SEO) → Landing Page Copy → Ad-Specific LPs → PostHog Events → PostHog Funnels → Google Ads launch.

---

### 🔴 Foundation (prerequisite for multiple features above)

**Stock Support** — stocks must exist as a first-class asset type before Trade Bundles and Custom Strategy Types can work for real-world strategies. Wheel strategy and Covered Calls both involve stock assignments; without stock support, these strategies cannot be fully logged. Stock support also resolves the incomplete transaction type coverage (F6) as a side-effect: Buy/Sell Stock and Dividends received/paid are exactly the missing types — once stocks are in, all 8 transaction types are covered.

**Dependency chain:**
```
Stock Support → Trade Bundles (Wheel, Covered Calls work correctly)
             → Custom Strategy Types (stock-based strategies become definable)
             → Resolves F6: all 8 transaction types covered (incl. dividends)
```

---

### 🔴 Core Product Gaps (from user research)

| # | Problem Area | Key Evidence | Priority |
|---|-------------|--------------|----------|
| 0 | **Stock Support** — foundation for #1, #2, and F6 | Multiple users + Levi | 🔴 Critical / Foundation |
| 1 | Trade Bundles — grouping transactions into strategies | Pietro + Levi + 12 users | 🔴 Critical — needs #0 |
| 2 | Custom Strategy Types | Levi call | 🔴 Critical — needs #0 + #1 |
| 3 | Login / Signup bugs blocking revenue | Patrick, Jörg | 🔴 Critical |
| 4 | "Expired Worthless" not trackable | 8+ users | 🔴 High / Quick win |
| 5 | Per-Leg Closing | Levi call | 🔴 High — Levi precondition |
| 6 | Incomplete transaction type coverage | Resolved by #0 (Stock Support) | 🟢 Resolved via #0 |
| 7 | Trust-breaking UX bugs (chart order, Safari, decimals) | Pietro + 5 users | 🟡 High |
| 8 | Default transaction fees — P&L silently wrong without them | All users | 🟡 High / Quick win |
| 9 | Trade Management Tool broken for multi-leg options — wrong SL/TP for all spread traders; stock extension needed once SPEC-01 ships | Adrian (internal) | 🔴 High / Quick win (Phase 1) |

### 🟡 Longer Horizon

| Problem Area | Notes |
|-------------|-------|
| Broker / CSV Import | Hard adoption ceiling for power users — Q2 commitment to Martin + Levi |
| Custom Tags + Behavioral Analytics | Core differentiator vs. basic journal |
| Chart Data API Migration | Yahoo Finance unreliable; $X has data gaps; free tier risk |
| Multi-Currency Support | Pietro EUR/HKD, Martin EUR/USD |
| Option Chain Data / Live P&L | Expensive (ORATS etc.) — evaluate costs |
| Changelog | Users always know what changed in the app — builds trust and reduces confusion after updates. See [SPEC-CHANGELOG.md](./specs/spec-changelog.md) |
| Public Roadmap + Feature Voting | Transparency toward users: upcoming features visible, users can vote on priorities, see what's in progress. Reduces "why isn't X built yet?" friction and creates community investment in the product direction. Data stored in Supabase. See [SPEC-PUBLIC-ROADMAP-VOTING.md](./specs/spec-public-roadmap-voting.md) |
| Organic SEO Content Strategy | Keyword Research + Technical SEO are Google Ads prerequisites (see 🔴 SEO block above). The longer-horizon layer is organic content: blog posts targeting keyword clusters (strategy guides, comparison articles), backlink building, and ongoing refinement. Goal: reduce CAC by shifting from paid to organic over time. Documented in [SPEC-GROWTH-seo.md](./specs/spec-growth-seo.md), Workstream 3. |

---

## Next Steps

| # | Action | Owner | When |
|---|--------|-------|------|
| 1 | Sprint planning meeting: prioritize focus areas → create tickets in Shortcut | Enes + Team | This week |
| 2 | Keyword Research: complete prioritized list with volume + competition data — or run `marketing:seo-audit` skill (see [SPEC-GROWTH-keyword-research.md](./specs/spec-growth-keyword-research.md)) | Larissa + Eve | Before Technical SEO |
| 3 | SEO: Technical SEO — meta titles, descriptions, Core Web Vitals, structured data (see [SPEC-GROWTH-seo.md](./specs/spec-growth-seo.md)) | Enes (implementation) + Eve (strategy) | After keyword research (#2) |
| 4 | Google Ads: rewrite main landing page copy (based on keyword list) | Adrian | After keyword research |
| 5 | Google Ads: build ad-specific landing pages (vs Excel, vs TraderSync, general intent) | Adrian + Enes | After main LP copy |
| 6 | Google Ads: instrument PostHog events (business-centric event architecture) | Enes | After pages finalized |
| 7 | Google Ads: configure PostHog signup → subscription funnel | Enes | After events live |
| 7a | **Google Ads: launch campaigns** (after G3 + G4 + G5 + G6 all done) | Larissa + Eve | April/May — #1 growth priority |
| 8 | Levi: email with roadmap + preconditions timeline | Larissa | This week |
| 9 | Martin: confirm broker import Q2 commitment | Adrian | This week |
| 10 | Pietro: recruit as beta tester for Trade Bundles | Larissa | This week |
| 11 | Share Chart API research with Enes | Adrian | This week |
| 12 | Sketch partnership terms for Levi (Revenue Share %) | Adrian | Before next Levi call |
