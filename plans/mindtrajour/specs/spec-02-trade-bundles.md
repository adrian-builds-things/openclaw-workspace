# Feature Spec: Trade Bundles

**Status:** Draft
**Product area:** Core Journaling
**Dependencies:** SPEC-01 (Stock Support) — stock transactions must exist to be included in bundles
**Enables:** SPEC-03 (Option Lifecycle Actions), SPEC-04 (Custom Strategy Builder)
**Last updated:** February 2026

---

## Problem Statement

Options income strategies are not single trades — they are sequences of related transactions that together constitute one deliberate strategy run. A Wheel on AAPL in Q1 2026 might involve selling a put, rolling it, getting assigned shares, and selling covered calls — all of which are individual entries in MindTrajour. There is currently no way to say "these trades are all part of the same strategy run on the same asset." As a result, traders cannot see the combined P&L of a strategy, cannot tell if it is still open or completed, and cannot analyze their strategies as the logical units they actually are.

A bundle is not an arbitrary grouping. It is always the **execution of a specific strategy on a specific underlying asset** — "Wheel on AAPL, started Q1 2026." That context — strategy, asset, timeframe — is what makes the grouping meaningful and what separates a bundle from a random collection of trades.

This is confirmed independently by Pietro and Levi, who both articulate the same fundamental need:

**Pietro:** *"I run a Wheel strategy on Apple — for that I need 3–5 trades as one logical unit."*
**Levi:** *"My trade reference is the only thing that keeps me sane. All I need is one text input field — and all of a sudden you'd be able to recreate a log of 470 trades off of one line of entry."*

---

## Goals

1. Traders can group related trades into a bundle that represents one strategy run on one underlying — with strategy name, asset, and timeframe clearly identified.
2. Traders can see the combined P&L of all trades in a bundle, not just individual trade P&L.
3. Traders can tell at a glance whether a bundle is still open (positions remain) or fully closed.
4. Traders can filter their trade history by bundle to focus on one strategy run at a time.
5. Levi's primary precondition for active use and promotion is met — he can start logging and grouping his 76 active positions.

---

## Non-Goals

- **Defined strategy structures or templates** — this spec does not define what legs a Wheel or Calendar Spread should have, or enforce any structure. That is SPEC-04 (Custom Strategy Builder). In this spec, the strategy name is a free-text field.
- **Strategy-type analytics** (e.g., "how do all my Wheel runs compare on average?") — requires SPEC-04.
- **Option lifecycle events within a bundle** (Roll, Assignment, Called Away) — these are actions on specific legs, handled in SPEC-03.
- **Automated grouping or detection** — traders assign trades to bundles manually. Broker import auto-matching is a separate feature.

---

## User Stories

### Income Strategy Trader (Pietro, Levi, and similar)

- As an income strategy trader, I want to create a bundle with a strategy name, underlying asset, and start date, so that I have a clearly identified container for all trades belonging to that strategy run.
- As a trader logging a new trade, I want to assign it to an existing bundle or create a new one inline, so that every trade is correctly linked from the moment I log it.
- As a trader with many open positions, I want to see all my bundles in one view — strategy, asset, status, and combined P&L — so that I can immediately understand where I stand across all my active strategy runs.
- As a trader reviewing a completed strategy run, I want to see the total realized P&L across all trades in the bundle, so that I know whether that run was profitable as a whole.

### Any Active Trader

- As a trader, I want to add existing trades to a bundle after the fact, so that I can organize trades logged before bundles existed.
- As a trader filtering my history, I want to filter by bundle so that I see only the trades belonging to a specific strategy run.

---

## Requirements

### P0 — Must Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Create a bundle with strategy name, asset, and start date | Trader can create a bundle by specifying: strategy name (free text, e.g. "Wheel"), underlying ticker (e.g. "AAPL"), and a start date. |
| Assign a trade to a bundle when logging | When creating a new trade, trader can assign it to an existing bundle or create a new bundle inline. |
| Assign existing trades to a bundle | Trader can add a previously logged trade to a bundle. |
| Bundle list view | Trader sees all bundles with: strategy name, asset, start date, status (open/closed), combined P&L. |
| Bundle detail view | Opening a bundle shows all trades within it, each with their individual P&L, plus the combined total. |
| Bundle open/closed status | A bundle is "open" if any trade within it is still open; "closed" when all are closed. |
| Filter trade history by bundle | Trader can filter the main trade list to show only trades belonging to a specific bundle. |

### P1 — Nice to Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Remove a trade from a bundle | Trader can unlink a trade if it was added to the wrong bundle. |
| Bundle notes field | Free-text field on the bundle for strategy thesis, observations, or context. |
| Search/filter bundles | Trader can search bundles by strategy name or asset ticker. |

### P2 — Future Consideration

| Requirement | Notes |
|-------------|-------|
| Bundle timeline view | Chronological view of all trades in a bundle — foundation for Wheel strategy lifecycle visualization (after SPEC-03). |
| Cross-bundle analytics | Compare performance across bundles of the same strategy type — requires SPEC-04. |

---

## Success Metrics

**Leading indicators** (visible within weeks of release):
- % of active users who create at least one bundle within 30 days of release.
- Levi confirms he can log and group his positions — marks precondition #1 as met.

**Lagging indicators** (visible over 1–2 sprints):
- Reduction in "no way to group trades" feedback.
- Pietro moves MindTrajour from secondary tool to primary journal.

---

## Open Questions

| Question | Owner |
|----------|-------|
| Should the strategy name be a free-text field only, or should we offer a preset list of common strategies (Wheel, Covered Call, Calendar Spread, etc.) with free-text as fallback? A preset list would give SPEC-04 a cleaner foundation to build on. | Product |
| Should a trade be assignable to more than one bundle (e.g., a hedge that spans multiple strategy runs), or is it always one bundle per trade? | Product |
| When is a bundle marked "closed" — automatically when all trades are closed, or manually by the trader? | Product |
| How is the bundle identified visually — does the trader write "Wheel AAPL Q1 2026" as a single name, or is the display name auto-composed from the three fields (strategy + asset + date)? | Product |

---

## Timeline & Sequencing

- **Requires:** SPEC-01 (Stock Support) — stock transactions must be loggable before they can be included in bundles.
- **Enables:** SPEC-03 (Option Lifecycle Actions) — Roll, Assignment, Called Away are leg-level actions that occur within the context of a bundle.
- **Enables:** SPEC-04 (Custom Strategy Builder) — adds defined strategy structures and cross-bundle analytics on top of the bundle concept introduced here.
- This is Levi's stated precondition #1 for active use and promotion.
