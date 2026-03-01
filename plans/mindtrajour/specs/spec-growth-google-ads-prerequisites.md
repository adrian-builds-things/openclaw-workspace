# Spec: Google Ads Launch Prerequisites

**Status:** Draft
**Area:** Growth / Marketing
**Last updated:** February 2026

---

## Dependency Map

```
This spec                       Depends on                      Enables
─────────────────────────────────────────────────────────────────────────────
Landing Page Copy               SPEC-GROWTH-keyword-            Ad-Specific LPs
                                research.md (keyword list)       PostHog Events

Ad-Specific Landing Pages       SPEC-GROWTH-keyword-            PostHog Events
                                research.md (keyword list)
                                SPEC-GROWTH-seo.md
                                (Technical SEO ready)
                                Landing Page Copy

PostHog Events                  Landing Page Copy (final)        PostHog Funnels
                                Ad-Specific LPs (final)

PostHog Funnels                 PostHog Events live              Google Ads Launch
```

**Hard prerequisite from SEO spec:** Technical SEO (`SPEC-GROWTH-seo.md`, Workstream 2) must be complete before any ad spend begins. Google's Quality Score algorithm evaluates landing page relevance and page speed — poor Technical SEO directly raises cost-per-click. This spec does not own Technical SEO; it only consumes it.

**Keyword list prerequisite:** The keyword list from `SPEC-GROWTH-keyword-research.md` must exist before Landing Page Copy and Ad-Specific LPs are written. Keyword Research is its own standalone spec — it is a shared upstream dependency for both this spec and `SPEC-GROWTH-seo.md`, extracted because the two are otherwise independent of each other.

---

## Problem Statement

MindTrajour is preparing to run Google Ads. The platform and audience are well-defined: serious options traders who search for structured journaling tools. The problem is that the infrastructure to convert these visitors profitably does not yet exist.

Three structural gaps make ad spend wasteful today:

**1. The landing page doesn't speak to paid traffic intent.** Visitors from Google Ads arrive with a specific search query and make a split-second decision. If the page doesn't immediately address their exact pain point — not "track your trades" in the abstract, but "replace your trading spreadsheet" or "this is better than TraderSync" — they leave. Every departure is a wasted click.

**2. Campaign pages don't exist.** Sending all campaigns to the same homepage ignores a fundamental principle: search intent varies by keyword. A user searching "trading journal vs Excel" needs a different argument than one searching "options trading journal." Without campaign-specific pages, MindTrajour either runs one generic campaign (suboptimal) or runs multiple campaigns to the same page (poor Quality Score, poor conversion).

**3. Conversion is invisible.** There is currently no way to see whether users who click an ad ever sign up, log a first trade, or start a subscription. Without event tracking and funnel configuration, there is no data to optimize ad spend — only costs without attribution.

---

## Goals

1. Main landing page copy speaks directly to the target segment: serious options traders who currently use spreadsheets or other tools.
2. Each Google Ads campaign has a dedicated landing page that matches the search intent of that campaign's keywords.
3. All critical conversion events are tracked in PostHog with a business-centric architecture (not click-tracking noise).
4. The signup-to-subscription funnel is configured and segmentable by campaign, landing page, and traffic source.
5. Google Ads ROI is measurable from day one.

---

## Non-Goals

- **Technical SEO** — owned by `SPEC-GROWTH-seo.md`. This spec assumes Technical SEO is complete before launch.
- **Keyword research** — owned by `SPEC-GROWTH-keyword-research.md`. This spec consumes the keyword list; it does not produce it.
- **Organic content / blog strategy** — `SPEC-GROWTH-seo.md`, Workstream 3.
- **Google Ads campaign configuration** — bidding strategy, match types, ad creative, and budget allocation are a separate workstream.
- **A/B testing infrastructure** — baseline tracking first; experimentation after.

---

## Workstream 1 — Main Landing Page Copy

**Depends on:** Keyword Research complete (`SPEC-GROWTH-seo.md` Workstream 1)

**Problem:** The current landing page does not speak to the audience that Google Ads will attract. Paid traffic visitors have specific intent and make a decision to sign up or leave within seconds. If the page doesn't immediately use the language they searched for — options strategies, P&L by strategy, Wheel strategy, income trading — they leave and the click cost is wasted.

This page also serves as the copy template for the ad-specific landing pages. It must be written first, since all campaign pages derive from the same core value proposition — they just angle it differently per audience.

**What is needed:**

- **Above the fold:** Clear, keyword-aligned value proposition that directly addresses the target audience. Not generic ("track your trades better") but specific ("A structured journal for options traders who run the Wheel, Covered Calls, and multi-leg income strategies").
- **Copy language:** Must use the exact terms traders search for — pulled from the keyword list. "Wheel strategy," "covered calls," "income trading," "multi-leg spreads," "P&L by strategy," "win rate," "trade bundle."
- **Differentiator section:** Explicit comparison to the status quo (spreadsheets and TraderSync). Not vague superiority claims — specific, demonstrable differences.
- **Social proof:** At minimum, quotes from real users (Pietro, Martin, Levi) that speak to the specific pain points addressed.
- **CTA:** Specific and tied to the visitor's pain point. "Stop managing your Wheel in a spreadsheet" > "Try it free."

**Owner:** Adrian
**Output:** Finalized homepage copy (text document or Figma)
**Enables:** Ad-Specific Landing Pages (same value prop, different framing per intent) + PostHog Events (instrument the final page)

---

## Workstream 2 — Ad-Specific Landing Pages

**Depends on:** Technical SEO ready (`SPEC-GROWTH-seo.md` Workstream 2) + Keyword Research complete + Landing Page Copy finalized

**Problem:** Different campaigns target different searcher intents. Sending all campaigns to the homepage means the page speaks to none of them precisely. Google also penalizes this: an ad for "trading journal vs Excel" pointing to a generic homepage gets a lower Quality Score, which raises CPC and lowers placement.

Each campaign needs a dedicated page that mirrors the ad's exact promise.

---

### Page A — MindTrajour vs Excel

**URL suggestion:** `mindtrajour.com/vs-excel`
**Target keywords:** `trading journal Excel`, `options trading spreadsheet alternative`, `replace Excel trading journal`
**Target audience:** Traders currently using Excel or Google Sheets — typically have a complex, hand-built spreadsheet they know isn't working well but haven't found a better alternative.

**Page structure:**

1. **Headline (above fold):** Leads with the pain, not the product. Example: *"Your options trading spreadsheet is lying to you."* or *"Excel wasn't built for Wheel traders."*
2. **Pain Points section:** Specific problems traders hit with spreadsheets — not generic UX complaints but domain-specific: no automatic P&L per strategy run, manually linking option assignments to stock positions, formula errors that corrupt multi-month data, no win rate by strategy type.
3. **Side-by-side comparison table:**

| Feature | Excel / Sheets | MindTrajour |
|---------|---------------|-------------|
| P&L by strategy run | ❌ Manual formula | ✅ Automatic |
| Multi-leg option grouping | ❌ Manual rows | ✅ Trade Bundles |
| Roll / Assignment tracking | ❌ Workaround needed | ✅ Structured lifecycle events |
| Win rate by strategy type | ❌ Complex formula | ✅ Automatic |
| Charts overlaid on trades | ❌ Not possible | ✅ Built-in |

4. **Proof:** A real user quote (e.g., from Martin or Levi) that specifically mentions replacing a spreadsheet.
5. **CTA:** Specific — *"Import your first trades and see your P&L in minutes."*

---

### Page B — MindTrajour vs TraderSync

**URL suggestion:** `mindtrajour.com/vs-tradersync`
**Target keywords:** `TraderSync alternative`, `TraderSync vs MindTrajour`, `TraderSync Deutsch`
**Target audience:** Traders who know TraderSync, use it, or have evaluated it — they are already product-aware and in active comparison mode.

**Page structure:**

1. **Headline:** Acknowledge TraderSync's position, then differentiate. Not "TraderSync is bad" — that's easily dismissed. Instead: *"TraderSync is a powerful tool. Here's where MindTrajour fits better."*
2. **Honest comparison table:** Where MindTrajour wins (German-language support, simpler UX for income traders, strategy-level P&L, pricing for solo traders), where TraderSync is stronger (broker integration depth, established user base). Honesty builds credibility with this audience.
3. **Specific differentiators for European / German-speaking traders:** Language, payment methods, customer support responsiveness.
4. **Pricing comparison** (if favorable).
5. **CTA:** For this audience, a free trial with no credit card is the lowest friction entry point. *"Try MindTrajour free — no card required."*

---

### Page C — Options Trading Journal (General Intent)

**URL suggestion:** `mindtrajour.com/options-trading-journal` (or homepage, if homepage is rewritten to target this)
**Target keywords:** `options trading journal`, `options journal app`, `Optionen Trading Tagebuch`, `trading journal app`
**Target audience:** Top-of-funnel traders looking for any journal tool — haven't committed to a specific alternative yet.

**Page structure:**

1. **Headline:** Problem-first, then product. *"A journal that understands how options traders actually think."*
2. **What MindTrajour is:** Specific, not generic. Structured strategy tracking, multi-leg support, P&L by strategy run — not just "log your trades."
3. **Use case section:** Wheel strategy example, Covered Call example, spread example — showing the product in the context of real strategies.
4. **Social proof / testimonials.**
5. **CTA:** *"Start your free journal."*

**Owner:** Adrian (copy) + Enes (page build)
**Note on SEO:** Whether these pages are indexed for organic ranking or kept as paid-only (noindex) is a decision documented in `SPEC-GROWTH-seo.md` Open Questions. It has a material impact on their long-term value.

---

## Workstream 3 — PostHog Event Tracking

**Depends on:** Landing Page Copy final + Ad-Specific LPs live

**Problem:** Conversion is currently invisible. There is no data on whether users who click an ad ever complete signup, log a trade, or start a subscription. Every optimization decision is made on intuition.

**Design principle:** Events follow a business-centric architecture (`[entity]_[action]` naming, three-level hierarchy). The guiding question for every event: *What business question does this data answer?* See `prompts/event-architecture-prompt.md` for the full methodology.

---

### Customer Events — The 5 Conversion Milestones

Every funnel report, acquisition analysis, and ad ROI calculation is built on these 5 events.

| Event Name | Trigger | Key Parameters |
|------------|---------|----------------|
| `account_created` | User completes signup | `traffic_source` (cpc / organic / social / direct), `landing_page_variant` (general / vs_excel / vs_tradersync), `utm_campaign` |
| `account_activated` | User verifies email | `hours_since_created` (bucketed: 0–1 / 1–6 / 6–24 / 24+) |
| `trade_first_logged` | User logs their very first trade | `trade_type` (option / stock / dividend), `days_since_created` (bucketed: 0 / 1 / 2–7 / 8–30 / 30+) |
| `subscription_created` | User starts a paid subscription | `plan_name` (monthly / annual), `traffic_source`, `days_since_created` (bucketed) |
| `subscription_cancelled` | User cancels subscription | `plan_name`, `subscription_duration` (bucketed: <7d / 7–30d / 31–90d / 90d+), `cancellation_reason` (select-only) |

---

### Product Events — Flow & Drop-off Analysis

| Event Name | Trigger | Key Parameters |
|------------|---------|----------------|
| `landing_page_viewed` | User views a marketing page | `page_variant` (general / vs_excel / vs_tradersync / pricing), `traffic_source`, `utm_campaign`, `utm_medium` |
| `signup_flow_started` | User clicks any CTA to begin signup | `cta_location` (hero / pricing / footer / nav), `page_variant` |
| `signup_step_completed` | User completes each signup step | `step_name` (email_entered / password_set / verification_sent), `step_number` |
| `pricing_page_viewed` | User views the pricing page | `traffic_source`, `referrer_page` (landing / app / direct) |
| `trade_logged` | Any trade is logged (ongoing) | `trade_type`, `is_first_trade` (true/false), `has_bundle` (true/false) |
| `bundle_created` | User creates a trade bundle | `has_strategy_type` (true/false) |

---

### Interaction Events — Kept Minimal

| Event Name | Trigger | Key Parameters |
|------------|---------|----------------|
| `cta_clicked` | Any CTA button click | `button_text`, `button_location` (hero / pricing / nav / footer / inline), `page_variant` |

---

### Cardinality Warnings

- **`utm_campaign`** — use for campaign-level breakdowns only; primary funnel analysis should use `traffic_source`
- **`cancellation_reason`** — fixed dropdown only; free text creates unresolvable cardinality
- **User or trade IDs** — never pass as parameters; high-cardinality by definition
- **Exact timestamps or prices** — always bucket (`days_since_created`, `plan_name`)

**Owner:** Enes
**Dependency:** Instrument the final, live pages — not drafts.

---

## Workstream 4 — PostHog Funnel Configuration

**Depends on:** All events firing correctly

**Problem:** Events alone produce a pile of data. A configured funnel produces a conversion rate and a drop-off point — the actionable information needed to optimize ad spend.

**What is needed:**

Full funnel in PostHog:
```
landing_page_viewed
    → signup_flow_started
    → account_created
    → account_activated
    → trade_first_logged
    → subscription_created
```

Segmentable by: `traffic_source` (organic vs. cpc), `landing_page_variant` (general / vs_excel / vs_tradersync), time period.

A shared PostHog dashboard — accessible to Adrian, Larissa, and Enes — that shows the funnel alongside key metrics (conversion rate per step, time between steps, drop-off by variant).

**Owner:** Enes
**Dependency:** All events must be firing before funnel is configured.

---

## Success Metrics

**Before Google Ads launch (all must be ✅):**
- [ ] `SPEC-GROWTH-seo.md` Workstreams 1 + 2 complete (keyword list + Technical SEO)
- [ ] Landing Page Copy approved by Adrian
- [ ] All 3 ad-specific landing pages live and SEO-ready (meta titles + speed verified)
- [ ] All 5 Customer Events + 6 Product Events firing correctly (verified with a test run)
- [ ] PostHog funnel configured and showing data

**After launch — first 2 weeks:**
- CPS (cost per signup) measurable and attributable by landing page variant
- Google Quality Scores ≥ 7/10 across all campaign keywords
- Drop-off point in funnel identified within 5 business days of launch
- At least one data-driven page or flow iteration shipped within 2 weeks

---

## Open Questions

| Question | Owner |
|----------|-------|
| Should comparison pages (vs-excel, vs-tradersync) be indexed for organic ranking, or kept as paid-only (noindex)? This decision sits at the intersection of both specs and has strategic implications. | Adrian |
| What UTM parameter naming convention will we use? Must be agreed before events are instrumented. Example: `utm_source=google`, `utm_medium=cpc`, `utm_campaign=vs-excel`. | Adrian + Enes |
| Is email verification a hard requirement for login? The current bug (Patrick) suggests this step may have elevated drop-off — consider fixing before launching ads. | Enes |
| What CPS threshold makes Google Ads profitable, given current free-to-paid conversion rate? | Adrian |
| German vs. English pages: should the ad-specific landing pages be available in German for DE campaigns, or is English acceptable for the initial launch? | Adrian |

---

## Timeline & Sequencing (cross-spec)

```
SPEC-GROWTH-keyword-research.md
─────────────────────────────────────────────────────────────────────────

[KR] Keyword Research
         │
         ├───────────────────────────────────────────────────────────┐
         │                                                           │
         ▼                                                           ▼
SPEC-GROWTH-seo.md                          SPEC-GROWTH-google-ads-prerequisites.md
─────────────────────────────────────────────────────────────────────────

[SEO-1] Technical SEO ──────────────────────────────► [ADS-1] Landing Page Copy
         │   (applies to all pages)                              │
         │                                                       ▼
         └──────────────────────────────────────────► [ADS-2] Ad-Specific LPs
                                                                 │
[SEO-2] Organic Content Strategy                                 ▼
         (longer horizon, parallel)                     [ADS-3] PostHog Events
                                                                 │
                                                                 ▼
                                                        [ADS-4] PostHog Funnels
                                                                 │
                                                                 ▼
                                                          Google Ads Launch
```
