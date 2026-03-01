# Feature Spec: Option Lifecycle Actions

**Status:** Draft
**Product area:** Core Journaling
**Dependencies:** SPEC-01 (Stock Support) — Assignment and Called Away create or close stock positions; SPEC-02 (Trade Bundles) — lifecycle events occur within the context of a bundle strategy run
**Enables:** SPEC-04 (Custom Strategy Builder) — strategy templates need to understand lifecycle events to correctly model Wheel and multi-leg strategies
**Last updated:** February 2026

---

## Problem Statement

Options strategies do not end where they begin. A put that is sold may be rolled to a different expiry, assigned into a stock position, or simply expired worthless. A covered call may be called away, ending the underlying stock position. Each of these is a distinct event with real P&L and position-state consequences — and none of them can currently be logged in MindTrajour.

Without the ability to record lifecycle events, traders face two equally bad choices: either close the original position manually and open a new one with no connection between them, or simply skip logging the event and accept an inaccurate record. The result is a journal that does not reflect reality — open positions that do not actually exist, missing P&L from option premiums, and no audit trail of how a strategy actually unfolded.

This affects every trader who runs income strategies. Rolling puts and calls is routine in Wheel and Covered Call strategies. Assignment is not an exception — it is the designed outcome of a short put when the thesis plays out. Called Away is the designed outcome of a Covered Call. These are not edge cases; they are the core lifecycle of the most popular strategies in our user base.

Additionally, multi-leg strategies (spreads, iron condors, diagonals) require the ability to close individual legs independently — not all legs at once. Levi demonstrated this directly: on a bull-put spread, he wants to let the long leg expire worthless while actively closing the short leg. Currently, all legs must be closed together, which prevents accurate journaling of any complex spread.

---

## Goals

1. Traders can log a Roll — closing an existing option leg and opening a replacement — as a single connected action, preserving the relationship between the original and new position.
2. Traders can log an Assignment — a short put resulting in a stock purchase — as a lifecycle event that correctly creates the corresponding stock position.
3. Traders can log a Called Away event — a short call resulting in the sale of underlying shares — as a lifecycle event that correctly closes the corresponding stock position.
4. Traders can close individual legs of a multi-leg trade independently, so that each leg has its own open/close lifecycle.
5. All lifecycle events correctly flow into bundle P&L and position status (SPEC-02).

---

## Non-Goals

- **Automatic detection of lifecycle events** — traders log these events manually. Broker import automation is a separate feature.
- **Option chain data or live pricing** — no market data feed is required. All values are entered by the trader.
- **Strategy structure enforcement** — this spec does not define what a Roll or Assignment must look like for a specific strategy type. That is SPEC-04 (Custom Strategy Builder).
- **Stock position P&L calculation** — the stock position created by Assignment is handled by SPEC-01 (Stock Support); this spec only defines the trigger event.

---

## User Stories

### Income Strategy Trader (Pietro, Levi, and similar)

- As a Wheel trader, I want to log a Roll when I extend the expiry of my short put, so that the old and new positions are clearly connected and the net debit or credit of the roll is tracked.
- As a Wheel trader whose short put is assigned, I want to log an Assignment event, so that the resulting stock purchase is automatically created and linked to my existing position record.
- As a Covered Call trader whose shares are called away, I want to log a Called Away event, so that the stock position closes correctly and the final P&L of the full strategy run reflects the call premium received.
- As a trader running a bull-put spread, I want to close only the long leg when I decide to let it expire worthless, while the short leg remains active — so that my journal reflects the actual state of the position.

### Any Active Options Trader

- As a trader managing a multi-leg spread, I want to close each leg on its own timeline, so that I can accurately reflect partial closures, early exits on one leg, or expirations on individual legs.
- As a trader reviewing a bundle, I want to see all lifecycle events — rolls, assignments, called away — in the bundle's timeline, so that I can understand how the strategy unfolded from start to finish.

---

## Requirements

### P0 — Must Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Per-leg closing on multi-leg trades | A trader can close individual legs of a multi-leg trade independently. Each leg has its own status (open/closed) and close price/date. |
| Log a Roll | Trader can record a Roll on an existing option position: specifies the closing of the old leg (strike, expiry, price) and the opening of the replacement leg (new strike, new expiry, new premium). The two legs are linked; the net credit or debit of the roll is shown. |
| Log an Assignment | Trader can record an Assignment on a short put: the option leg closes at the strike price, and a corresponding stock Buy transaction is automatically created (ticker, shares = contract size × number of contracts, price = strike price, date = assignment date). Links to SPEC-01 stock tracking. |
| Log a Called Away event | Trader can record a Called Away on a short call: the option leg closes, and the corresponding stock Sell transaction is automatically created (ticker, shares, price = strike price, date). Links to SPEC-01 stock tracking. |
| Lifecycle events appear in bundle timeline | All lifecycle events (Roll, Assignment, Called Away) are visible in the bundle detail view (SPEC-02) as part of the strategy run timeline. |
| Lifecycle events contribute to bundle P&L | The net credits/debits from Rolls, premiums from closed legs, and stock transactions triggered by Assignment/Called Away all flow into the bundle's combined P&L. |

### P1 — Nice to Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Roll history on a position | A position that has been rolled multiple times shows the full roll chain — each generation of the position, in sequence. |
| Expiry type on close | When closing a leg, trader can specify how it closed: Buy to Close, Expired Worthless, Assigned, Called Away — so that the reason for closure is captured alongside the P&L. |
| Notes field on lifecycle events | Trader can add a note to a Roll, Assignment, or Called Away event to record their reasoning or market context at the time. |

### P2 — Future Consideration

| Requirement | Notes |
|-------------|-------|
| Visual Wheel lifecycle diagram | A graphical view of a Wheel bundle's full lifecycle: short put → assignment → stock → covered call → called away. Requires all lifecycle events to be consistently logged. |
| Automated lifecycle detection from broker import | When importing trade history, Roll and Assignment events are detected and linked automatically. Requires broker import feature. |

---

## Success Metrics

**Leading indicators** (visible within weeks of release):
- % of active users who log at least one Roll, Assignment, or Called Away within 30 days of release.
- Levi confirms Per-Leg Closing and lifecycle logging meet his requirements — precondition #2 for promotion is met.

**Lagging indicators** (visible over 1–2 sprints):
- Bundle P&L is reported as accurate by users who run Wheel and Covered Call strategies.
- Pietro can complete a full Wheel run — put → assignment → covered call → called away — in MindTrajour without switching to TraderSync.

---

## Open Questions

| Question | Owner |
|----------|-------|
| On Assignment: should the resulting stock transaction be editable after creation, or should it always mirror the assignment price exactly? (Edge case: broker may adjust the cost basis.) | Product + Enes |
| For a Roll: is the "new leg" always part of the same bundle as the original, or can a Roll effectively start a new bundle on a different underlying? | Product |
| Should Per-Leg Closing require that at least one leg remains open (to prevent accidentally "half-closing" a spread), or is full flexibility preferred? | Product |
| How is a Called Away distinguished from a regular Sell Stock transaction in the UI — does it require explicit selection of the "Called Away" event type, or can it be inferred from context? | Product |

---

## Timeline & Sequencing

- **Requires:** SPEC-01 (Stock Support) — Assignment and Called Away create/close stock positions; stock transactions must exist as a first-class type before lifecycle events can trigger them.
- **Requires:** SPEC-02 (Trade Bundles) — lifecycle events are most meaningful within the context of a bundle; the bundle detail view and combined P&L are where Roll/Assignment/Called Away become visible.
- **Enables:** SPEC-04 (Custom Strategy Builder) — strategy templates need to understand and sequence lifecycle events to correctly model Wheel runs and validate multi-leg structures.
- Levi's precondition #2 (Per-Leg Closing) is contained in this spec.
