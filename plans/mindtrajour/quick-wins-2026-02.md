# MindTrajour — Quick Wins

> **Purpose:** Ship small, high-impact changes fast. No upstream dependencies. Every item here can be built in isolation. Ordered by impact-to-effort ratio.
>
> **Scope:** Items with < 2 days of effort and direct user-visible value. Larger features (Stock Support, Trade Bundles, Per-Leg Closing, Broker Import) are not here — those are in the sprint planning doc.
>
> **Navigation:** [Sprint Planning](./sprint-planning-2026-02.md) · [Roadmap](./roadmap-2026-02.md) · [Specs](./specs/)

---

## 🔴 Priority 0 — Ship Immediately

### QW-6 — Trade Management Tool Broken for Multi-Leg Options
**Effort:** 1–2 days | **Source:** Adrian (internal) | **Spec:** [SPEC-TRADE-MANAGEMENT](./specs/spec-trade-management.md)

The Stop Loss / Take Profit calculator currently works for single-leg options but produces wrong results for multi-leg trades (spreads, condors, strangles). A spread's risk/reward is defined by the **net debit or credit** of the whole position and the **spread width** — not by individual legs calculated in isolation. Any trader using a bull put spread, iron condor, or any other multi-leg structure is getting silently incorrect SL/TP values.

**What to fix:**
- Aggregate leg premiums to derive net debit / net credit as the primary calculation basis
- Calculate max profit and max loss correctly from net premium + spread width
- Apply configurable TP % and SL % rules to the aggregate position
- Single-leg behavior must remain unchanged (no regression)

**Phase 2 (not now):** Stock support extension — deferred until SPEC-01 ships.

Full details in [SPEC-TRADE-MANAGEMENT.md](./specs/spec-trade-management.md).

---

### QW-1 — Login / Signup Bugs Blocking New Users
**Effort:** 1–2 days | **Source:** Patrick, Jörg (both warm YouTube leads who never converted) | **Revenue impact:** Direct

Two bugs are silently killing conversions while Google Ads budget runs:

- Patrick cannot log in at all
- Jörg's confirmation email is not delivered; his discount code is broken

With paid traffic active, we are paying to send users to a broken door. This is the only item on this list that has an immediate monetary cost if left unfixed.

**No spec needed — investigate, fix, test. One Shortcut story.**

---

### QW-2 — "Expired Worthless" Action
**Effort:** ~0.5 days | **Source:** 8+ users | **Spec:** [SPEC-03](./specs/spec-03-option-lifecycle-actions.md) (P1, extractable)

> *"If my put option expires worthless, that is my maximum profit — but MindTrajour doesn't show me that."* — Gerhard

Options that expire worthless are the most common positive outcome in income strategies (Wheel, CSP, Covered Call). Currently: traders cannot log this event, so it disappears from their journal. Win rate is wrong, P&L is wrong, premium income is invisible.

**What to build:**
- On any open options position, add an **"Expired Worthless"** action button
- Clicking it closes the position at $0.00 with today's date (editable)
- The full premium received at open is recognized as profit
- Position status becomes "Expired Worthless" (distinct from "Closed")

**This is a standalone action — no dependency on SPEC-01 (Stock Support) or SPEC-02 (Trade Bundles).**

---

### QW-3 — Default Transaction Fees
**Effort:** 1–2 days | **Source:** General data quality issue | **Spec:** [SPEC-DEFAULT-FEES](./specs/spec-default-fees.md)

Traders pay the same fee every trade (e.g., $0.65/contract at Schwab). Currently they enter it manually each time — in practice they skip it, silently corrupting every P&L calculation in the app.

**What to build:**
- Settings page: two fields — "Options fee per contract" + "Flat fee per order"
- New trade entry: both fields pre-filled from settings, always editable
- Total commission preview on the trade form: `(contracts × fee) + flat fee`

Full details in [SPEC-DEFAULT-FEES.md](./specs/spec-default-fees.md).

---

## 🟡 Priority 1 — Next Two Weeks

### QW-4 — Trust-Breaking UX Bugs
**Effort:** ~1.5 days total (3 bugs) | **Source:** Pietro + 5 users

Three bugs that make professional traders distrust the app's data integrity:

| Bug | Description | Reported by | Effort |
|-----|-------------|-------------|--------|
| Chart bars in random order | Monthly bars in charts displayed in wrong/random sequence — visible on Pietro's screen share | Pietro (confirmed live) | ~0.5 days |
| Safari filter reset | All filters revert to default on page reload in Safari | Jennifer, Christin | ~0.5 days |
| Decimal separator | EU users have trouble with comma vs. period in numeric input fields | Multiple EU users | ~0.5 days |

These are perception-of-quality bugs. Pietro is dual-tooling with TraderSync specifically because MindTrajour "feels less polished." Fixing chart order alone is visible on every chart view.

**No spec needed — three separate Shortcut bug stories.**

---

### QW-5 — "Close Type" on Option Close
**Effort:** ~0.5–1 day | **Source:** F4 / SPEC-03 P1

When a trader closes an options position, they should be able to specify *how* it closed. Currently there is no distinction between "Bought to Close" (paid to exit) and "Expired Worthless" (max profit) — both look identical in the journal.

Add a **"Close Type" dropdown** on the close-position form:
- Buy to Close
- Expired Worthless ← this is the core value (QW-2 above)
- Sell to Close (for long options)

**Note:** QW-2 and QW-5 can be built together in the same story — they address the same UX flow.

---

## What Is NOT a Quick Win

The following items look small but have hard upstream dependencies:

| Item | Blocker | Why |
|------|---------|-----|
| Per-Leg Closing (F5 / SPEC-03 P0) | Needs SPEC-02 Trade Bundles | Per-leg close requires the multi-leg trade data model |
| Roll, Assignment, Called Away (SPEC-03 P0) | Needs SPEC-01 Stock Support | Assignment creates a stock position — needs stock model first |
| Custom Strategy Types (SPEC-04) | Needs SPEC-01 + SPEC-02 | Depends on both stock and bundle models |
| Broker / CSV Import (F8) | Standalone but large | 5–8 days, Q2 work |
| Multi-Currency (F10) | Needs P&L model refactor | Cannot be bolted on cleanly |

---

## Quick Win Dependency Map

```
No dependencies (ship any time):
  QW-1  Login/Signup Bugs
  QW-2  Expired Worthless button
  QW-3  Default Transaction Fees
  QW-4  Trust-Breaking UX Bugs (3 separate stories)
  QW-5  Close Type dropdown
  QW-6  Trade Management Tool — multi-leg bug fix

Can be combined:
  QW-2 + QW-5 → single "Options close flow" story

After quick wins, next natural progression:
  Stock Support (SPEC-01)
    → Trade Management Tool Phase 2 (stock extension)
    → Trade Bundles (SPEC-02)
      → Per-Leg Closing (SPEC-03)
      → Custom Strategy Types (SPEC-04)
```

---

## Shortcut Story Checklist

- [ ] QW-1 · Bug: Login broken for Patrick / Signup confirmation not delivered for Jörg
- [ ] QW-2 · Feature: "Expired Worthless" action on open options positions
- [ ] QW-3 · Feature: Default transaction fees in settings (per contract + flat fee)
- [ ] QW-4a · Bug: Monthly chart bars displayed in random order
- [ ] QW-4b · Bug: All filters reset on page reload in Safari
- [ ] QW-4c · Bug: Decimal separator issues for EU users (comma vs period)
- [ ] QW-5 · Feature: Close Type dropdown on option close form (Buy to Close / Expired Worthless / Sell to Close)
- [ ] QW-6 · Bug: Trade Management Tool — wrong SL/TP calculations for multi-leg options (spreads, condors, strangles)
