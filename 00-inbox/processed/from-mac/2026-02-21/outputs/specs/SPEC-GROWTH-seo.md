# Spec: SEO Strategy

**Status:** Draft
**Area:** Growth / Marketing
**Last updated:** February 2026

---

## Dependency Map

```
This spec                       Depends on              Enables
─────────────────────────────────────────────────────────────────────────────
Keyword Research                (see SPEC-GROWTH-       Technical SEO on-page
(owned externally)               keyword-research.md)   Landing Page Copy (→ Google Ads)
                                                        Ad-Specific LPs (→ Google Ads)
                                                        Organic Content Strategy

Technical SEO                   Keyword Research        Google Ads Quality Score
                                Landing Page Copy       Organic ranking
                                (copy must be final     Ad-Specific LP credibility
                                before meta is written)

Organic Content Strategy        Keyword Research        Long-term organic traffic
(Longer Horizon)                Technical SEO baseline  Reduced CAC over time
```

**Cross-spec dependencies:**
- `SPEC-GROWTH-keyword-research.md` → Keyword Research is a shared upstream dependency, extracted into its own spec because both this spec and the Google Ads spec depend on it independently
- `SPEC-GROWTH-google-ads-prerequisites.md` (Landing Page Copy, Ad-Specific LPs) → reads from Keyword Research output
- Technical SEO in this spec → is a hard prerequisite for the Google Ads launch (affects Quality Score and CPC)
- The two specs share the same keyword foundation but have different goals: SEO maximizes organic visibility; Google Ads maximizes paid conversion.

---

## Problem Statement

MindTrajour currently has no defined SEO strategy. This creates two compounding problems:

**Organic:** There is no guarantee that the site ranks for the terms serious options traders actually search for — "options trading journal," "Wheel strategy tracker," "trading journal vs Excel." Without keyword-informed copy and technical hygiene, organic traffic will remain accidental rather than systematic. Organic traffic is the only traffic channel with a zero marginal cost per click — building it is a long-term competitive asset.

**Paid (Google Ads dependency):** Google's Quality Score algorithm rewards relevance between the search term, the ad, and the landing page. A landing page that does not contain the right keyword signals — correct meta title, aligned body copy, appropriate structured data — will receive a lower Quality Score, resulting in higher cost-per-click and worse ad placement. In other words, bad SEO directly raises the cost of paid advertising.

These two problems share the same root cause: no defined keyword strategy means there is no single source of truth for what terms MindTrajour is trying to own, in what priority order, and how those terms should be reflected in the site's copy and structure.

---

## Goals

1. A defined target keyword list exists — the terms MindTrajour is actively trying to own, prioritized by search volume, intent, and competitive difficulty.
2. Every page on the site (homepage, pricing, and each campaign landing page) has keyword-aligned meta titles and descriptions.
3. Technical SEO baseline is met: Core Web Vitals pass, structured data is in place, and no indexing issues exist.
4. On-page copy uses the exact language options traders search for — verified against the keyword list, not guessed.
5. (Longer horizon) A content strategy exists for building organic traffic through blog posts and long-form content targeting the right keyword clusters.

---

## Non-Goals

- **Google Ads campaign setup or conversion tracking** — handled in `SPEC-GROWTH-google-ads.md`
- **Ad-specific landing page copy** — page *copy* lives in the Google Ads spec; Technical SEO *applies to* those pages but the content decisions are made in the Google Ads context
- **Backlink building / off-page SEO** — this is a longer-horizon workstream; the current spec covers on-page and technical only
- **Multilingual SEO** — a German-language SEO strategy (for DE market) is a separate decision; this spec covers the English-language site first

---

## Workstream 1 — Keyword Research & Strategy

> **Owned by `SPEC-GROWTH-keyword-research.md`** — Keyword Research has been extracted into its own standalone spec because it is a shared upstream dependency for both this spec and `SPEC-GROWTH-google-ads-prerequisites.md`. It is documented separately to reflect this independence.

**Why this must come first:** Every other SEO decision — meta titles, body copy alignment, blog topics, ad campaign keywords — is only as good as the keyword research behind it. Without a defined keyword list, copy is written on intuition and may not match what traders actually type into Google.

**What this spec consumes from `SPEC-GROWTH-keyword-research.md`:**
- The prioritized keyword list (clusters: core product, comparison/switch, strategy-specific, problem-aware, income trading)
- The target page assignment per keyword (which MindTrajour page owns which term)
- Competition and volume data — to prioritize which terms to optimize meta copy for first

**What this spec does with it:**
- Writes keyword-aligned meta titles and descriptions for every page (Workstream 2)
- Aligns on-page H1 and body copy to the confirmed keyword targets
- Uses the keyword clusters as the foundation for the Organic Content Strategy topic list (Workstream 3)

**See `SPEC-GROWTH-keyword-research.md`** for: full keyword cluster table, deliverable definition, tool recommendations, the `marketing:seo-audit` skill reference for automated research, and open questions.

---

## Workstream 2 — Technical SEO

**Why:** Technical SEO is the infrastructure layer. It does not generate traffic on its own — but it ensures that every other effort (organic and paid) is not undermined by technical failures. A page with a missing meta title, slow load time, or unindexed status is invisible to Google regardless of how good the copy is.

**Direct impact on Google Ads:** Google's Quality Score evaluates the landing page for relevance and user experience. Pages that load slowly, have mismatched meta content, or lack mobile optimization receive lower scores — directly raising CPC. Technical SEO must be complete before any Google Ads spend begins.

**What is needed:**

**Meta titles — every page must have a targeted, keyword-aligned title:**

| Page | Example Meta Title |
|------|--------------------|
| Homepage | `MindTrajour — Options Trading Journal for Serious Traders` |
| Pricing | `MindTrajour Pricing — Plans for Options Traders` |
| LP: vs Excel | `MindTrajour vs Excel — Why Options Traders Switch` |
| LP: vs TraderSync | `MindTrajour vs TraderSync — A Better Options Journal` |
| LP: General | `Options Trading Journal App — Track Every Strategy` |

Format rules: primary keyword first, brand second, under 60 characters, no keyword stuffing.

**Meta descriptions — every page:**
- 150–160 characters
- Contains the target keyword naturally
- Communicates the value proposition clearly
- Has an implicit CTA ("Start tracking" / "See the difference")

**Core Web Vitals:**
- Largest Contentful Paint (LCP): < 2.5 seconds
- Cumulative Layout Shift (CLS): < 0.1
- Interaction to Next Paint (INP): < 200ms
- Measure using: Google PageSpeed Insights (free), Chrome DevTools

**Structured data (Schema.org):**
- `SoftwareApplication` — for the main product (name, description, category, price range, rating if available)
- `FAQPage` — on pages where an FAQ section exists (improves rich snippet eligibility)
- Implement via JSON-LD in the `<head>`

**Indexability check:**
- `robots.txt` — no critical pages accidentally blocked
- `sitemap.xml` — all pages included, submitted to Google Search Console
- No `noindex` tags on pages intended for ranking
- Canonical tags correct (especially for ad-specific landing pages)

**On-page keyword alignment:**
- Each page's H1 should contain the target keyword
- Body copy should use the keyword and related terms naturally — not stuffed, but present
- Image alt text should describe the image using relevant terms where appropriate

**Owner:** Enes (technical implementation) + Adrian (meta copy content)
**Dependency:** Keyword Research must be complete first (so meta titles target the right terms). Landing Page Copy (Google Ads) must be drafted first (so on-page copy is in its final state before meta is written around it).

---

## Workstream 3 — Organic Content Strategy *(Longer Horizon)*

**Note:** This workstream is not required for the Google Ads launch. It is documented here because it shares the same keyword foundation and should be planned in parallel — even if execution is deferred.

**Why organic content matters:** Paid traffic has a cost-per-click. Organic traffic, once established, is essentially free. A blog post that ranks for "how to track Wheel strategy trades" drives qualified visitors indefinitely after it is published — with no incremental ad spend. Over a 12-month horizon, organic content is the most scalable growth channel for a bootstrapped SaaS with MindTrajour's profile.

**Target content clusters:**

| Cluster | Example Article Titles |
|---------|----------------------|
| Strategy-specific guides | "How to Journal a Wheel Strategy: Step-by-Step", "Tracking Covered Calls: What Metrics Actually Matter" |
| Tool comparisons | "Options Trading Journal vs Spreadsheet: A Real Comparison", "TraderSync vs MindTrajour: Which Is Right for You?" |
| Education + product | "How to Calculate P&L on Multi-Leg Options Trades", "What Is a Trade Bundle and Why Income Traders Need One" |
| Income trading | "The Best Way to Track Options Income Over Time", "How to Measure Wheel Strategy Performance" |

**Production model:** One article per month minimum. Each article targets a specific keyword from the keyword list, follows SEO best practices (keyword in H1, H2 structure, internal linking), and includes a CTA to MindTrajour.

**Owner:** Adrian (content) — consider ghostwriting or content tools once volume increases
**Dependency:** Keyword Research complete, Technical SEO baseline in place

---

## Success Metrics

**Short-term (before / at Google Ads launch):**
- Keyword Research complete: target list of ≥ 20 priority keywords defined and prioritized
- All existing pages have keyword-aligned meta titles and descriptions
- Core Web Vitals pass on all pages (LCP < 2.5s, CLS < 0.1, INP < 200ms)
- Google Search Console is set up and sitemap submitted
- Structured data validated (Google Rich Results Test — no errors)

**Medium-term (1–3 months after launch):**
- MindTrajour appears in Google Search Console data for at least 5 target P0 keywords
- At least 2 blog articles published and indexed
- Organic traffic (non-paid sessions) shows a positive week-over-week trend

**Long-term (6–12 months):**
- MindTrajour ranks on page 1 for at least one high-intent keyword cluster
- Organic traffic accounts for ≥ 30% of new signups
- Content library includes ≥ 10 articles covering the priority keyword clusters

---

## Open Questions

| Question | Owner |
|----------|-------|
| Does MindTrajour have access to Google Search Console? If not, it must be set up before any SEO progress can be measured. | Enes |
| Is there a budget for keyword research tools (Ahrefs, Semrush) or will we rely on free tools (Google Keyword Planner, Ubersuggest)? | Adrian |
| Should comparison pages (vs Excel, vs TraderSync) be included in the sitemap and actively optimized for organic ranking, or kept as landing-page-only (noindex)? If noindex, they serve only paid traffic and contribute nothing to organic. | Adrian |
| Is there a German-language market SEO strategy planned? Separate DE pages would be needed (hreflang, DE keyword research), which is significant additional scope. | Adrian |

---

## Full Dependency Map (across all three specs)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│           SPEC-GROWTH-keyword-research.md  (no upstream deps)               │
│                                                                             │
│   [KR] Keyword Research                                                     │
│           │                                                                 │
└───────────┼─────────────────────────────────────────────────────────────────┘
            │ keyword list
            ├──────────────────────────────────────────────────────┐
            │                                                      │
            ▼                                                      ▼
┌───────────────────────────────────────┐   ┌────────────────────────────────────┐
│          SPEC-GROWTH-seo.md           │   │  SPEC-GROWTH-google-ads-           │
│                                       │   │  prerequisites.md                  │
│  [1] Technical SEO                    │   │                                    │
│       ◄── keyword list (from KR)      │   │  [1] Landing Page Copy             │
│       ◄── LP Copy (must be final      │   │       ◄── keyword list (from KR)   │
│            before meta written)       │   │       │                            │
│        │                              │   │       ▼                            │
│        └─── enables Quality Score ────┼───┼──► [2] Ad-Specific LPs            │
│                                       │   │       ◄── Technical SEO ready      │
│  [2] Organic Content Strategy         │   │       │                            │
│       (longer horizon)                │   │       ▼                            │
│       ◄── keyword list (from KR)      │   │  [3] PostHog Events               │
│       ◄── Technical SEO baseline      │   │       │                            │
│                                       │   │       ▼                            │
└───────────────────────────────────────┘   │  [4] PostHog Funnels              │
                                            │       │                            │
                                            │       ▼                            │
                                            │   Google Ads Launch                │
                                            └────────────────────────────────────┘
```
