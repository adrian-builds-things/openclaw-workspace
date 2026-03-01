# MindTrajour — Product Roadmap
**Last updated:** February 2026
**Sprint length assumption:** 2 weeks (adjust if different)
**Format:** Sprint-based · Two parallel tracks (Product / Growth)

**Navigation:** [Sprint Planning](./sprint-planning-2026-02.md) · [Quick Wins](./quick-wins-2026-02.md) · [Specs](./specs/)

---

## Team

| Person | Role | Owns |
|--------|------|------|
| **Adrian** | Product Owner + Developer + Copywriter | Product direction, feature specs, landing page copy, ad copy, some implementation |
| **Enes** | Developer | All technical implementation (product features, landing pages, technical SEO, PostHog) |
| **Larissa** | Marketing + Outreach | Customer & B2B outreach, newsletter, Google Ads campaign management (with Eve), Levi relationship |
| **Eve** | SEO + Marketing | SEO strategy & execution, keyword research (with Larissa), documentation content, supports Larissa on Google Ads |

> **Bottleneck:** Enes is the single technical resource across Product and Growth. His capacity must be sequenced explicitly — Product and Growth tasks compete for the same person.

---

## Strategic North Star

**1. Stop the bleeding.** Login bugs are losing warm leads with active Ads budget running. Fix today.

**2. Get Google Ads running — in Sprint 2.** Keyword Research → LP Copy → Tech SEO → Ad LPs → PostHog → Launch. This is the #1 priority. Every week of delay is revenue not captured.

**3. Land Levi.** Trade Bundles + Per-Leg Closing = Levi demo. That is the entire product track for the next 8 weeks after Google Ads is live.

---

## Dependency Map

```
  Quick Wins              Growth Track                 DB Cleanup
  (no deps)               (no deps)                    (only blocks
                                                        DB migrations)
  QW-1 Login bugs         G1 Keyword Research               │
  QW-2 Expired Worthless  G2 LP Copy (Adrian)               ▼
  QW-3 Default Fees       G3 Tech SEO (Enes+Eve)        SPEC-01
  QW-4 UX Bugs            G4 Ad-Specific LPs             Stock Support
  QW-5 Close Type           (Adrian copy+Enes build)         │
                          G5 PostHog (Enes)              ┌───┴────┐
                          G6 Google Ads Launch           ▼        ▼
                            (Larissa+Eve)            SPEC-02   resolves F6
                                                     Trade     (8 tx types)
                                                     Bundles
                                                         │
                                                         ▼
                                                     SPEC-03
                                                     Per-Leg Closing
                                                     + Roll + Assign
                                                         │
                                                         ▼
                                                     SPEC-04
                                                     Custom Strategy
                                                     Builder
```

---

## Track 1 — Product (Enes + Adrian)

### 🔴 Sprint 1 — Weeks 1–2

All Quick Wins are parallel and independent. DB Cleanup runs alongside. Goal: Enes clears the backlog and unblocks SPEC-01 by end of sprint.

| Item | Owner | Effort | Notes | Spec |
|------|-------|--------|-------|------|
| **DB Cleanup** | Enes | TBD (Enes to estimate) | Only blocks SPEC-01. Must be done this sprint so Stock Support can start in Sprint 2. | — |
| **Login / Signup Bugs** (QW-1) | Enes | 1–2 days | Ads budget is live. Patrick and Jörg are warm leads lost to a bug. Highest urgency. | — |
| **"Expired Worthless" + Close Type dropdown** (QW-2 + QW-5) | Enes | ~1 day | Win rate and P&L wrong for all income traders. Combinable into one story. | [SPEC-03](./specs/spec-03-option-lifecycle-actions.md) |
| **Default Transaction Fees** (QW-3) | Enes | 1–2 days | P&L accuracy for all existing users. Popup on Trade Details page. | [SPEC-DEFAULT-FEES](./specs/spec-default-fees.md) |
| **Trust-Breaking UX Bugs** (QW-4) | Enes | ~1.5 days | Chart bar order, Safari filter reset, decimal separator. Pietro is dual-tooling because MindTrajour "feels less polished." | — |
| **Trade Management Tool — multi-leg fix** (QW-6) | Enes | 1–2 days | SL/TP calculator currently wrong for spreads, condors, strangles. Net debit/credit and spread width not correctly aggregated. Silently wrong numbers for every multi-leg user. | [SPEC-TRADE-MANAGEMENT](./specs/spec-trade-management.md) |

**Sprint 1 exit:** All Quick Wins shipped. DB Cleanup done. Enes free to start SPEC-01.

---

### 🔴 Sprint 2 — Weeks 3–4

| Item | Owner | Effort | Notes | Spec |
|------|-------|--------|-------|------|
| **Stock Support** (SPEC-01) | Enes | 1–2 weeks | Foundation for Trade Bundles and Custom Strategy Types. Needs DB Cleanup from Sprint 1. If Enes has capacity after Sprint 1, start early. | [SPEC-01](./specs/spec-01-stock-support.md) |

> **Note:** If Enes's Sprint 2 is consumed by Growth tech work (Tech SEO + Ad LPs + PostHog), Stock Support moves to Sprint 3. The decision about Enes's Sprint 2 priority — Product vs. Growth — must be made in the Sprint 1 retro.

---

### 🟡 Sprint 3–4 — Weeks 5–8

| Item | Owner | Effort | Notes | Spec |
|------|-------|--------|-------|------|
| **Stock Support** (SPEC-01) | Enes | 1–2 weeks | If not finished in Sprint 2. | [SPEC-01](./specs/spec-01-stock-support.md) |
| **Trade Management Tool — stock extension** | Enes | 1–2 days | Extend SL/TP calculator to handle stock positions (price-based, not premium-based). Also: blended P&L view for Wheel/Covered Call (stock leg + options leg combined). Ships immediately after SPEC-01. | [SPEC-TRADE-MANAGEMENT](./specs/spec-trade-management.md) |
| **Trade Bundles** (SPEC-02) | Enes | 2–3 weeks | Levi precondition #1. Pietro's core request. 12+ users. Cannot start before SPEC-01. | [SPEC-02](./specs/spec-02-trade-bundles.md) |

**Sprint 3–4 exit:** Trade Bundles shipped. Levi outreach goes out.

---

### 🟡 Sprint 5–6 — Weeks 9–12

| Item | Owner | Effort | Notes | Spec |
|------|-------|--------|-------|------|
| **Per-Leg Closing + Roll + Assignment** (SPEC-03) | Enes | 1–2 weeks | Levi precondition #2. Per-Leg Closing is the hard blocker. Roll and Assignment complete the income trader picture. | [SPEC-03](./specs/spec-03-option-lifecycle-actions.md) |

**Sprint 5–6 exit:** Levi gets a demo. If it passes, promotion relationship begins.

---

### 🟢 Later — Sprint 7+

| Item | Owner | Effort | Notes | Spec |
|------|-------|--------|-------|------|
| **Custom Strategy Builder** (SPEC-04) | Enes | 2–4 weeks | Needs SPEC-01 + SPEC-02 + SPEC-03. Full foundation must be in place first. | [SPEC-04](./specs/spec-04-custom-strategy-builder.md) |
| **Custom Tags + Behavioral Analytics** (F9) | Enes | 2–3 days | Pietro's $10k insight. Core differentiator vs. basic journal. Fast once data model is stable. | — |
| **Broker / CSV Import** (F8) | Enes | 5–8 days | Hard adoption ceiling for Martin + Levi. Commit to timeline now so they don't leave. | — |
| **Multi-Currency Support** (F10) | Enes | 2–3 days | Pietro (EUR/HKD), Martin (EUR/USD). P&L refactor needed. | — |
| **Public Roadmap + Feature Voting** | Enes | 1–2 weeks | Community investment, reduces "why isn't X built yet?" friction. | [SPEC-ROADMAP](./specs/spec-public-roadmap-voting.md) |
| **Chart Data API Migration** | Enes | TBD | Yahoo Finance unreliable ($X data gaps). Evaluate Polygon.io / Tiingo. Adrian has research to share. | — |

---

## Track 2 — Growth (Larissa · Eve · Adrian)

**Target: Google Ads live by end of Sprint 2.** The entire chain must run in parallel during Sprints 1–2.

### 🔴 Sprint 1 — Weeks 1–2

| Item | Owner | Notes |
|------|-------|-------|
| **Keyword Research — finalize** (G1) | Larissa + Eve | Already in progress. Complete: monthly search volumes, P0/P1/P2 tiers, current rankings, comparison keywords. This unlocks LP copy. |
| **Main Landing Page Copy** (G2) | **Adrian** | Adrian writes the copy. Start immediately — core framing doesn't need keyword research to begin. Finalize with keywords once G1 is done. Options-trader language: "Wheel strategy," "covered calls," "P&L by strategy." |
| **Newsletter + Customer Outreach** | Larissa | Ongoing: newsletter to existing users, outreach to churned users (Thomas etc.), B2B pipeline. Runs every sprint, not a one-time task. |
| **Email Levi with roadmap + timeline** | Larissa | Send by end of Sprint 1. No financial commitments needed yet — just set expectations. |

---

### 🔴 Sprint 2 — Weeks 3–4 → **Google Ads Launch**

| Item | Owner | Notes |
|------|-------|-------|
| **Technical SEO** (G3) | Enes (build) + Eve (strategy) | Keyword-aligned meta titles + descriptions (Eve delivers copy, Enes implements). Core Web Vitals, structured data (SoftwareApplication schema). Hard Google Ads prerequisite — Quality Score depends on it. |
| **Ad-Specific Landing Pages** (G4) | Adrian (copy) + Enes (build) | Three pages: vs Excel / vs TraderSync / Options Trading Journal. Adrian writes copy off main LP. Enes builds. |
| **PostHog Events + Funnels** (G5) | Enes | 5 Customer Events + 6 Product Events. Cannot measure Google Ads without this. Must be live before launch. |
| **Google Ads — Campaign Launch** 🚀 (G6) | Larissa + Eve | Launch once G2 + G3 + G4 + G5 are all done. Do not launch without all four — wasted clicks. |
| **Documentation — Tier 1 content** (G7) | Eve (content) + Adrian (review) | Core workflow pages in German + English. No Enes dependency if using Mintlify/GitBook subdomain. Can run in parallel with tech work. See [SPEC-DOCUMENTATION](./specs/spec-documentation.md). |

**Sprint 2 exit:** Google Ads live. First conversion data in PostHog.

---

### 🟡 Sprint 3–4 and Beyond

| Item | Owner | Notes |
|------|-------|-------|
| **Google Ads — optimize** | Larissa + Eve | Ongoing from Sprint 3: analyze PostHog funnel data, improve Quality Score, adjust bids and copy based on results. |
| **Documentation — Tier 2 + Tier 3** | Eve | Tier 2: document features as they ship (Trade Bundles, Per-Leg Closing). Tier 3: comparison pages (vs TraderSync, vs Excel) — highest-converting intent. |
| **Organic Content Strategy** | Eve + Larissa | Blog posts targeting keyword clusters (strategy guides, Wheel explainers, "TraderSync alternative"). Long-term CAC reduction. Builds on Documentation foundation. |

---

## Partnership: Levi Woods

| When | Action | Owner |
|------|--------|-------|
| End Sprint 1 | Email with roadmap + concrete timeline (Trade Bundles + Per-Leg Closing by ~week 12) | Larissa |
| End Sprint 5–6 | Demo call — show live: Wheel strategy with bundles, bull-put spread with per-leg closing | Adrian |
| After demo | Revenue share / equity discussion | Adrian |

**His two preconditions:** Trade Bundles (SPEC-02) + Per-Leg Closing (SPEC-03). Both required. Nothing else.

---

## What Is Not On This Roadmap

| Item | Reason |
|------|--------|
| Option Chain Data / Live P&L (ORATS) | Very expensive, no clear ROI path. Evaluate after Levi is onboarded. |
| Changelog UI | Already implemented. No new work needed. |
| "Beginner tool" perception (F11) | Not a build task — resolves automatically once Trade Bundles + Per-Leg Closing ship. Thomas churned; Pietro dual-tools. Both would be resolved by the feature roadmap. |

---

## Summary View

```
         S1 (wk 1–2)         S2 (wk 3–4)         S3–4 (wk 5–8)      S5–6 (wk 9–12)    Later
         ────────────────────────────────────────────────────────────────────────────────────────

PRODUCT  [Enes]
         DB Cleanup ──►
         Quick Wins (incl. Trade Mgmt fix) ──────►
                             Stock Support ──────────────────────────►
                             Trade Mgmt stock ext. ──►  (after SPEC-01)
                                                  Trade Bundles ──────────────►
                                                                    Per-Leg ────►      Strategy Builder
                                                                                       Broker Import
                                                                                       Custom Tags
                                                                                       Multi-Currency

GROWTH   [Adrian:copy · Enes:tech · Larissa+Eve:SEO+ads]
         KW Research ─────►
         LP Copy ─────────────►  [Adrian]
                             Tech SEO ──────►     [Enes+Eve]
                             Ad LPs ─────────►    [Adrian+Enes]
                             PostHog ─────────►   [Enes]
                             🚀 GOOGLE ADS ──────────────────────────────────► [Larissa+Eve]
                             Docs T1 ─────────────────────────────────────────► [Eve]

OUTREACH [Larissa]
         Email Levi ──►      Newsletter/Outreach (every sprint) ──────────────────────────────►
                                                                              Demo Call ──►
```

---

## Open Items

| Question | Owner |
|----------|-------|
| **Sprint length confirmation:** Are sprints 2 weeks? This shapes all dates above. | Adrian |
| **Enes Sprint 2 priority:** Product (Stock Support) or Growth (Tech SEO + Ad LPs + PostHog)? Both compete for him. Must be decided in Sprint 1 retro. | Adrian + Enes |
| How long is DB Cleanup? This is the only thing blocking Stock Support. | Enes |
| What is the SPEC-01 (Stock Support) effort estimate? Trade Bundles timeline depends on it. | Enes |
| Documentation: `/docs` subfolder (better SEO, needs Enes) or `docs.mindtrajour.com` subdomain (Mintlify/GitBook — faster, no Enes)? If subdomain, G7 Documentation is fully unblocked. | Adrian + Enes |
| Q3 commitment to Martin + Levi for Broker Import: communicate now or after Sprint 5–6 demo? | Adrian |
