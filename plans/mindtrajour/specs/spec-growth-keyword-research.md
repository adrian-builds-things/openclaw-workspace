# Spec: Keyword Research

**Status:** In Progress *(preliminary keyword clusters defined; full prioritized list with search volume + current rankings pending)*
**Area:** Growth / Marketing
**Owner:** Eve
**Last updated:** February 2026

---

## Why This Is a Standalone Spec

Keyword Research has no upstream dependencies of its own. It is a shared upstream dependency for two otherwise independent specs:

- `SPEC-GROWTH-seo.md` — Technical SEO meta titles and on-page copy must be aligned to the keyword list
- `SPEC-GROWTH-google-ads-prerequisites.md` — Landing Page Copy and Ad-Specific LPs must use the terms traders actually search for

The fact that two unrelated specs depend on the same artifact — and that those two specs have no dependency on each other — is the structural proof that Keyword Research is its own discrete deliverable, not a subtask of either.

```
Dependency Map
─────────────────────────────────────────────────────────────────
This spec              Depends on       Enables
─────────────────────────────────────────────────────────────────
Keyword Research       (none)           SPEC-GROWTH-seo.md
                                        (Technical SEO — meta titles,
                                        on-page copy alignment,
                                        Organic Content Strategy)

                                        SPEC-GROWTH-google-ads-
                                        prerequisites.md
                                        (Landing Page Copy,
                                        Ad-Specific Landing Pages)
```

---

## Problem Statement

MindTrajour currently has no defined, verified list of the terms serious options traders type into Google. Copy is written on intuition. Meta titles are not keyword-informed. Landing pages cannot be built for search intent if the intent is not known.

Without a prioritized keyword list, every downstream copy and SEO decision — meta titles, body copy, ad landing page headlines, blog topics — is a guess. Two parallel tracks waste effort: SEO writes meta titles for terms that Google Ads doesn't bid on; Google Ads bids on terms the site doesn't rank for. The keyword list is the shared foundation that makes both tracks coherent.

---

## Existing Keyword Data

The team has already provided a keyword dataset. The raw data has been extracted and saved to:

| File | Description |
|------|-------------|
| [`keyword-research/keyword-research-summary.md`](computer:///sessions/eager-elegant-heisenberg/mnt/outputs/keyword-research/keyword-research-summary.md) | Full summary with all keywords organized by type and intent, plus key observations |
| [`keyword-research/keywords-DE.csv`](computer:///sessions/eager-elegant-heisenberg/mnt/outputs/keyword-research/keywords-DE.csv) | 77 German-language keywords with intent, type, content placement, volume, and competition |
| [`keyword-research/market-keywords-EN.csv`](computer:///sessions/eager-elegant-heisenberg/mnt/outputs/keyword-research/market-keywords-EN.csv) | 16 EN market keywords with volume + KD across Germany, Nigeria, USA |

**What is still missing from the existing data:** Monthly search volume numbers and current Google ranking positions. These need to be filled in using Google Keyword Planner / Ahrefs + Google Search Console before the list is complete.

---

## Deliverable

A keyword research document (spreadsheet or Notion database) containing, for each keyword:

| Column | Description |
|--------|-------------|
| Keyword | Exact search phrase |
| Cluster | Category (see table below) |
| Intent | high / mid / low purchase intent |
| Priority | P0 / P1 / P2 |
| Monthly Search Volume | Estimated (tool-provided) |
| Competition | low / medium / high |
| Target Page | Which MindTrajour page targets this keyword |
| Current Ranking | Position in Google (if any) — requires Search Console |

**Minimum:** ≥ 20 priority keywords across all P0 and P1 clusters, with volume estimates and competition ratings.

---

## Preliminary Keyword Clusters

*These clusters were defined based on user interviews and competitive context. The table below is the starting structure — full volume data and competition ratings must be filled in using a keyword tool.*

| Cluster | Example Keywords | Intent | Priority |
|---------|-----------------|--------|----------|
| Core product | "options trading journal", "options journal app", "Optionen Trading Tagebuch" | High — direct | P0 |
| Comparison / Switch | "trading journal vs Excel", "options trading spreadsheet alternative", "TraderSync alternative", "TraderSync vs MindTrajour" | High — comparison | P0 |
| Strategy-specific | "Wheel strategy tracker", "covered call journal", "cash-secured put tracker" | Mid — specific intent | P1 |
| Problem-aware | "how to track options trades", "best way to journal options trades", "options P&L tracking" | Mid — educational | P1 |
| Income trading | "income trading journal", "options income tracker", "selling options journal" | Mid | P2 |

---

## Recommended Tool for Execution

**Recommended approach for a bootstrapped, niche SaaS:**
- Google Keyword Planner (free — available within Google Ads account) for volume estimates
- Ubersuggest or Ahrefs (if budget available) for competition data and additional keyword ideas
- Google Search Console for current ranking positions (must be set up first — see Open Questions)

**Note on niche volume:** Keyword volumes for options trading tools are low in absolute terms. A keyword with 100–500 monthly searches but high purchase intent and low competition is more valuable than a high-volume term with poor conversion intent. Prioritize intent quality over raw search volume.

---

## Skill: Automated Keyword Research

> **Future execution:** This workstream can be run using the `marketing:seo-audit` skill available in Cowork. The skill performs keyword research, on-page analysis, content gap analysis, and competitor comparison. To execute: open Cowork, select the `marketing:seo-audit` skill, provide the MindTrajour URL and target market context (options traders, income strategies, Wheel/Covered Call/spreads). The output maps directly to the deliverable columns above.
>
> **When to run it:** Before the Technical SEO meta title rewrite and before Landing Page Copy is drafted. If the preliminary cluster list above has already been used as input, run the skill to validate, fill in missing volume data, and identify keywords not yet in the list.

---

## Success Criteria

- [ ] All P0 and P1 keywords have estimated monthly search volume and competition rating
- [ ] Each keyword has a designated target page on mindtrajour.com
- [ ] Current ranking position captured for all keywords (requires Google Search Console)
- [ ] Keyword list reviewed and approved by Adrian
- [ ] List delivered by Eve to: Enes (meta title implementation) + Adrian (copy writing)

---

## Open Questions

| Question | Owner |
|----------|-------|
| Is Google Search Console set up? Current rankings cannot be retrieved without it — this must be resolved before the keyword list is considered complete. | Enes |
| Is there budget for a keyword research tool (Ahrefs ~$99/mo, Semrush ~$129/mo), or will we use free tools (Google Keyword Planner + Ubersuggest)? Free tools are sufficient for a first pass. | Adrian |
| Should German-language keywords be included in the initial list, or deferred to a DE-market SEO strategy? DE keywords require separate meta content and potentially separate pages (hreflang). | Adrian |
