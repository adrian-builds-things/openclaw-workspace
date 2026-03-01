# MindTrajour — Team Meeting Prep (2026-02-22)

## Meeting Goal
Make clear decisions in 90 minutes so next week’s execution is unblocked.

## Expected Outcomes
- Prioritized sprint scope (**now** vs **later**)
- Clear owners per topic
- Dependency-based execution order
- Final ticket list for Shortcut

---

## 1) Quick Context (5 min)

- Current bottleneck: conversion and revenue.
- Paid traffic only makes sense when signup/login is stable and measurable.
- Product leverage for serious traders: Trade Bundles + Per-Leg Closing (incl. Levi potential).

**Decision rule:** Revenue leaks first → Growth engine second → Core product depth third.

---

## 2) Priority Clusters & Next Steps

## A) Revenue Protection & Quick Wins (immediate)
**Goal:** Stop losing warm leads and remove trust-breaking bugs.

**Next steps**
1. Fix login/signup/confirmation issues (incl. discount code flow)
2. Add “Expired Worthless” + Close Type in exit flow
3. Add default fees in settings + pre-fill in trade entry
4. Fix trust bugs: chart order, Safari filter, EU decimal formatting
5. Fix multi-leg trade management (correct net debit/credit basis)

**Done when**
- Signup/signin is stable
- Top trust/UX bugs are closed
- Quick wins are live or release-ready

## B) Growth Engine (parallel, but sequenced)
**Goal:** Launch ads profitably, not blindly.

**Next steps (order matters)**
1. Finalize keyword priorities (volume + difficulty + intent)
2. Align landing page copy with search intent
3. Complete technical SEO (meta, schema, CWV)
4. Build ad-specific LPs (vs Excel, vs TraderSync, generic)
5. Ship PostHog event schema + funnel tracking
6. Launch Google Ads only after tracking is reliable

**Done when**
- LP → Signup → Activation → Subscription funnel is measurable
- Campaign optimization can run on reliable data

## C) Trading Core Foundation
**Goal:** Position MindTrajour as the go-to tool for complex strategies.

**Next steps (dependency-aware)**
1. Ship stock support as foundation
2. Build trade bundles (cross-strategy grouping)
3. Add per-leg closing + roll/assignment flows
4. Support strategy types at bundle level

**Done when**
- Wheel/spread workflows are fully loggable
- Bundle P&L and status are accurate

## D) Scale & Differentiation (later)
1. Broker/CSV import
2. Custom tags + behavioral insights
3. Multi-currency P&L
4. Chart API migration

---

## 3) Proposed Agenda (90 min)

- **0–10 min:** Alignment (goal + decision rule)
- **10–30 min:** Cluster A scope, owner, sequence, 7–10 day commitment
- **30–50 min:** Cluster B go-live criteria + delivery ownership
- **50–70 min:** Cluster C dependencies + stock support start + Levi milestones
- **70–85 min:** Translate epics into ordered Shortcut tickets
- **85–90 min:** Final top-3 goals, blockers, follow-up owners

---

## 4) Must-Decide Questions

1. What gets Enes capacity in the next 2 weeks: Cluster A remaining work, Growth tech, or stock support start?
2. Which tasks are hard ad-launch criteria vs nice-to-have?
3. When do we re-approach Levi, and what feature state must be live first?
4. Which 3 tickets create the biggest revenue/learning impact by next meeting?

---

## 5) Recommended Top-3 Outcomes for Tomorrow

1. **Quick Wins committed:** login/signup + expired worthless + trade management fix prioritized and scheduled
2. **Growth committed:** LP + PostHog + funnel sequence finalized
3. **Core committed:** stock support start window + bundle/per-leg milestone confirmed

---

## 6) Fast Meeting Notes Template

- Decision 1:
- Decision 2:
- Decision 3:
- Owner per decision:
- Deadline per decision:
- Open risks:
- Next check-in date:
