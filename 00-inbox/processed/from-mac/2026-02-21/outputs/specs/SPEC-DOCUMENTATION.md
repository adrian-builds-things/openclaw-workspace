# Spec: Feature Documentation & SEO Knowledge Base

**Status:** Draft
**Area:** Growth / Product Transparency / SEO
**Owner:** TBD (Eve for content, Enes for implementation)
**Effort estimate:** Content: ongoing | Implementation: 3–5 days
**Last updated:** February 2026

---

## Dependency Map

```
Dependency Map
────────────────────────────────────────────────────────────────
This spec         Depends on         Enables
────────────────────────────────────────────────────────────────
Feature           Keyword Research   Organic search traffic
Documentation     (SPEC-GROWTH-KR)   via long-tail keywords
& SEO Knowledge   for Tier 2+3
Base              keyword targeting   Users understand HOW
                                      to use the product
                  Existing features   (reduces confusion,
                  to document         support load, and
                                      silent churn)

                  German-language     German users get
                  content             guidance in their
                                      native language

                                      Feeds directly into
                                      Google Ads Quality
                                      Score (page relevance)
```

---

## Problem Statement

Users who sign up for MindTrajour often know that the product exists and roughly what it does. The gap is not feature awareness — it is usage confidence. There is no structured place that explains, in plain language, how to actually use the tool: what to do, how it works, and what to watch out for.

This matters in two concrete ways:

**User side:** Without clear guidance, users figure it out by clicking around. Some succeed; some get stuck and quietly leave. Even active users may not be using the app to its full potential — not because features are hidden, but because there is no explanation of the workflow, the logic behind the numbers, or edge cases to be aware of (e.g. what happens to P&L if you forget to set an order fee, how to correctly log an assignment, what "expired worthless" means for win rate calculation).

**SEO side:** High-value long-tail queries go unanswered — "how to track a Wheel strategy," "how to log an expired put option," "options journal with P&L by strategy" — because there is no content to rank for them. These are exactly the queries that signal buying intent from traders actively looking for a tool like MindTrajour.

A structured, bilingual (German + English) documentation site solves both: it gives existing users a reliable reference in their language, and it brings in new users via organic search.

---

## What We Are Building

A public documentation and help center at `/docs` (or `/help`) on the MindTrajour marketing site, written in **both German and English**. Each page covers one feature or workflow with:

- A clear title targeting a specific search query
- Plain-language explanation of how the feature works and what to watch out for
- Step-by-step instructions with screenshots
- Relevant internal links to related features
- Structured markup (H1, H2, meta description) aligned with the keyword list from SPEC-GROWTH-KR

German is a first-class language, not a future add-on. MindTrajour's core user base is German-speaking; the documentation needs to serve them directly. English docs run in parallel for SEO reach and international users.

This is not a wall of text. It is a collection of short, scannable, task-oriented pages — one page per feature or workflow, in two languages.

---

## Content Scope

Each page answers three questions for the user: **what is this**, **how does it work**, and **what should I watch out for**. The goal is that a user who is confused or stuck can find a clear answer without contacting support.

### Tier 1 — Core Workflows (ship first, no keyword research needed)

These pages cover the core things every MindTrajour user needs to do. They can be written immediately with existing knowledge — no keyword research dependency.

| Page | What it explains | Priority |
|------|-----------------|----------|
| Getting started / Account setup | First steps, how to configure the account, what to set before logging the first trade | P0 |
| How to log an options trade | Fields, what each one means, what to watch out for (fees, contract count, open/close) | P0 |
| Understanding P&L in MindTrajour | How gross vs. net P&L is calculated, what affects the numbers, common mistakes | P0 |
| How to log a Wheel strategy | The full cycle: CSP → assignment → covered call; how to connect the trades | P0 |
| How to log a Covered Call | Entry, management, close — what changes if stock is called away | P0 |
| How to mark an option as expired worthless | Why it matters for win rate + P&L, step-by-step | P0 |
| How to use the Order Fee / Transaction Fee field | What it is, why it matters for accurate P&L, how to set a default | P0 |

### Tier 2 — Advanced Features (ship as features mature)

| Page | Target keyword examples | Priority |
|------|------------------------|----------|
| How to group trades into a strategy (Trade Bundles) | "strategy grouping options journal" | P1 — ship after SPEC-02 |
| How to close individual legs of a spread | "per-leg closing options", "multi-leg spread journal" | P1 — ship after SPEC-03 |
| How to roll an option | "rolling options journal", "how to log a roll" | P1 — ship after SPEC-03 |
| How to track multi-currency P&L | "EUR USD options journal", "multi-currency trading journal" | P2 — ship after F10 |
| How to use custom tags for trading psychology | "trading psychology journal", "tag analysis trading" | P2 — ship after F9 |

### Tier 3 — Comparison / Switch Content (SEO intent: evaluation)

These pages target traders actively comparing tools — the highest-converting search intent:

| Page | Target keyword | Priority |
|------|---------------|----------|
| MindTrajour vs TraderSync | "MindTrajour vs TraderSync", "TraderSync alternative" | P1 |
| MindTrajour vs Excel spreadsheet | "options journal vs Excel", "trading journal Excel alternative" | P1 |
| Why switch from a spreadsheet to MindTrajour | "trading journal spreadsheet", "options Excel tracker replacement" | P1 |

> Note: Tier 3 pages depend on Keyword Research (SPEC-GROWTH-KR) for final keyword targeting. Tier 1 content can start immediately with current knowledge.

---

## Technical Implementation

### Option A — MDX pages in the Next.js app (recommended)

Add a `/docs` route to the existing Next.js marketing site. Each page is an MDX file. Advantages: full control over styling, no third-party dependency, pages are indexed with the rest of the domain (SEO benefit from domain authority).

```
/docs
  /getting-started
  /features
    /logging-a-trade
    /tracking-pnl
    /wheel-strategy
    /expired-worthless
    ...
  /comparisons
    /vs-tradersync
    /vs-excel
  /changelog  ← links to existing Changelog system
```

### Option B — Third-party docs tool (Mintlify, GitBook)

Faster to set up, but lives on a subdomain (`docs.mindtrajour.com`). Subdomain SEO is weaker than a subfolder (`mindtrajour.com/docs`). Suitable for MVP if Enes needs to prioritize product work.

**Recommendation:** Start with Option B for speed, migrate to Option A when capacity allows.

---

## SEO Structure Per Page

Every documentation page follows this template:

```
<title> How to Log a Wheel Strategy — MindTrajour Docs </title>
<meta description> Learn how to track your Wheel strategy trades in MindTrajour.
  Log CSPs, assignments, covered calls, and full-cycle P&L in one place. </meta>

H1: How to Track a Wheel Strategy in MindTrajour

Intro paragraph (2–3 sentences): what this page covers, who it's for

H2: What is the Wheel Strategy?
  → 1–2 short paragraphs (context for SEO, helpful for beginners)

H2: Step 1 — Log your opening short put
  → Screenshot + numbered steps

H2: Step 2 — Log an assignment or roll
  → Screenshot + numbered steps

H2: Step 3 — Log the covered call phase
  → Screenshot + numbered steps

H2: Viewing your full Wheel P&L
  → Screenshot showing P&L summary

Related pages: [Trade Bundles] · [Per-Leg Closing] · [P&L Overview]
```

---

## Success Criteria

- [ ] `/docs` section live on marketing site (or docs subdomain as interim)
- [ ] All Tier 1 pages published in **both German and English**
- [ ] Each page covers: what the feature is, how it works step-by-step, and what to watch out for
- [ ] Screenshots included on all core feature pages
- [ ] Title, meta description, and H1/H2 structure aligned with target keywords (English pages; German pages optimized for German-language queries)
- [ ] Internal links between related pages (cross-linking improves crawlability and time on site)
- [ ] Docs pages indexed by Google (verify via Search Console)
- [ ] At least one Tier 3 comparison page live (vs TraderSync or vs Excel)
- [ ] Docs linked from main navigation on the marketing site
- [ ] New features are documented within 2 weeks of shipping (process, not just one-time work)

---

## Out of Scope (V1)

- In-app contextual help tooltips (could link to docs pages later)
- Video tutorials
- Community forum or user-generated content
- Searchable docs with full-text search index (can add later via Algolia DocSearch or similar)
- Versioned docs (not needed until API or breaking changes)
- Languages beyond German and English

---

## Open Questions

| Question | Owner |
|----------|-------|
| `/docs` subfolder (on main domain) or `docs.mindtrajour.com` subdomain? The subfolder is better for SEO but requires Enes. The subdomain (Mintlify/GitBook) is faster to launch. | Adrian + Enes |
| Who writes/owns the German content — Adrian, Eve, or a mix? Write English first then translate, or write German-first and translate to English? | Adrian |
| Should docs pages include pricing CTAs / signup prompts at the bottom? This converts docs traffic into trials. | Adrian |
| Who takes the screenshots — Adrian, or should there be a process (e.g., staging environment screenshot workflow)? | Adrian |
| Should comparison pages (vs TraderSync, vs Excel) live under `/docs` or as standalone landing pages under `/compare`? Standalone landing pages can be more conversion-optimized. | Adrian |
