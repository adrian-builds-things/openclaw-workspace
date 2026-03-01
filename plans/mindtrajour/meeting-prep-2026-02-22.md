# MindTrajour — Team Meeting Prep (2026-02-22)

## Meeting Goal
Make clear, binding decisions in 90 minutes so the team can execute next week without ambiguity.

## Required Outcomes (must be final by the end)
- Priorities for the next 7–14 days are clear
- Clear owner per topic
- Sequence based on dependencies is fixed
- Ticket list for immediate implementation in Shortcut is finalized

---

## Decision Logic (use this for every discussion)
1. Close revenue leaks first
2. Then build the growth engine properly
3. Then push core product to pro level

---

## Priorities & Next Steps

### A) Revenue Protection & Quick Wins (immediate)
**Goal:** Stop losing warm leads due to bugs.

**Next Steps**
1. Fix login/signup/confirmation bugs (including discount code)
2. Exit flow: support `Expired Worthless` + `Close Type` correctly
3. Default fees in settings + pre-fill in trade entry
4. Fix trust bugs: chart order, Safari filter, EU decimal handling
5. Trade management multi-leg fix (correct net debit/net credit basis)

**Definition of Done**
- Signup/signin is stable
- Top trust/UX bugs are closed
- Quick wins are live or release-ready

### B) Growth Engine (parallel, but properly sequenced)
**Goal:** Launch ads with a measurable funnel (no blind budget burn).

**Next Steps (order matters)**
1. Final keyword prioritization (volume + difficulty + intent)
2. Align landing page copy with search intent
3. Technical SEO: meta, schema, Core Web Vitals
4. Build ad-specific LPs: vs Excel, vs TraderSync, generic
5. PostHog event schema + funnel live
6. Only then: Google Ads launch

**Definition of Done**
- Funnel LP → Signup → Activation → Subscription is measurable
- Campaigns can be optimized based on reliable data

### C) Trading Core Foundation
**Goal:** Position MindTrajour as a true tool for complex strategies.

**Next Steps (with dependencies)**
1. Stock support as foundation
2. Trade bundles (cross-strategy grouping)
3. Per-leg closing + roll/assignment flows
4. Strategy types on bundle level

**Definition of Done**
- Wheel/spread workflows are fully loggable
- Bundle P&L and status are correctly calculated

### D) Scale & Differentiation (later)
**Goal:** Retain power users and strengthen product edge.

**Next Steps**
1. Broker/CSV import
2. Custom tags + behavioral insights
3. Multi-currency P&L
4. Chart API migration

---

## Proposed Agenda (90 minutes)

### 0–10 min: Alignment
- Confirm meeting goal
- Confirm decision logic (Revenue → Growth → Core)

### 10–30 min: Cluster A
- Finalize scope
- Assign owners + sequence
- Commit for next 7–10 days

### 30–50 min: Cluster B
- Define go-live criteria
- Lock task sequence
- Set owners + deadlines

### 50–70 min: Cluster C
- Confirm dependencies
- Decide stock support start timing
- Set Levi-relevant milestones

### 70–85 min: Ticket Translation
- Break epics into concrete tickets
- Set story order in Shortcut

### 85–90 min: Wrap-up
- Top 3 goals until next meeting
- Risks/blockers + owners
- Set follow-up date

---

## Must-Decide Questions in the Meeting
1. For Enes capacity in the next 2 weeks: Cluster A remaining work, growth tech, or stock support start?
2. Which tasks are hard launch criteria for ads vs nice-to-have?
3. When do we actively re-engage Levi (which feature state must be live)?
4. Which 3 tickets will create the highest revenue/learning impact by next meeting?

---

## Target Top-3 Outcomes for Tomorrow
1. **Quick-wins commitment:** Login/signup + expired worthless + trade-management fix prioritized and scheduled
2. **Growth commitment:** LP + PostHog + funnel sequence agreed and binding
3. **Core commitment:** Stock support start window + bundle/per-leg milestone confirmed

---

## Copy/Paste Meeting Notes Template
- Decision 1:
- Decision 2:
- Decision 3:
- Owner per decision:
- Deadline per decision:
- Open risks:
- Next check-in date: