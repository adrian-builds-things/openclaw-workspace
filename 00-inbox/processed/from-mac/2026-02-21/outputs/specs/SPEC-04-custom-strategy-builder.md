# Feature Spec: Custom Strategy Builder

**Status:** Draft
**Product area:** Core Journaling + Analytics
**Dependencies:** SPEC-01 (Stock Support), SPEC-02 (Trade Bundles), SPEC-03 (Option Lifecycle Actions) — all three must exist for strategy types to be meaningful
**Last updated:** February 2026

---

## Problem Statement

Trade Bundles (SPEC-02) tell you which transactions belong together. They do not tell you what kind of strategy is being executed, what legs it should have, or how to measure whether it is working.

Levi has been manually solving this problem with spreadsheets for 8 years: one tab per strategy type, each with its own columns, metrics, and structure. A tab for Wheel runs. A tab for Calendar Spreads. A tab for Diagonal Spreads. Each tab captures exactly what matters for that strategy — not generic trade data, but strategy-specific performance. He has 470 trades organized this way and would switch to MindTrajour immediately if it could replicate this structure.

Without strategy types, MindTrajour treats a Wheel run, a Calendar Spread, and a naked put as identical containers — all labeled "bundle." There is no way to ask "how does my average Wheel run perform?" or "which calendar spreads have I run on SPY, and were they profitable?" These are the questions serious options traders actually ask. They are also the questions that transform a trade journal into a genuine analytical tool.

The Custom Strategy Builder gives traders the ability to define their own strategy types — each with its own leg structure, its own naming conventions, and its own performance metrics — and to categorize all their bundles against these types. The result is analytics that are meaningful not just in aggregate, but by strategy.

---

## Goals

1. Traders can define custom strategy types (Wheel, Covered Call, Calendar Spread, Diagonal Spread, Iron Condor, etc.) with a description of the leg structure they expect.
2. A bundle can be assigned a strategy type — giving it semantic meaning beyond a free-text name.
3. Traders can see analytics grouped by strategy type: how many runs, average P&L, win rate, average duration.
4. Traders can compare all their Wheel runs against each other, or all their Calendar Spreads — by underlying, by time period, by outcome.
5. Levi can replace his strategy-specific spreadsheet tabs with MindTrajour views — one per strategy type, tracking the same metrics he currently tracks manually.

---

## Non-Goals

- **Automated trade detection or signal generation** — this spec does not involve live market data, automated strategy detection, or any form of automated execution.
- **Options pricing models or risk metrics** (Greeks, IV analysis) — these are separate from the journaling and analytics scope of this spec.
- **Enforcing leg structure compliance** — the strategy builder organizes and analyzes; it does not validate or block trades that deviate from the expected structure. Traders run strategies in reality, not in theory.
- **Broker import integration** — matching imported trades to strategy types is a separate feature.
- **Shared strategy templates across users** — strategy types are private per account at launch. A public template library is a future consideration.

---

## User Stories

### Advanced Options Trader (Levi and similar)

- As a trader who runs multiple distinct strategy types, I want to define what a "Wheel" is — e.g., a short put → assignment → covered call sequence on the same underlying — so that every bundle I tag as a Wheel is categorized consistently.
- As a trader reviewing my Wheel performance, I want to see all my Wheel bundles in a single view — with entry date, underlying, duration, total P&L, and whether it ended in Called Away or was still running — so that I can compare runs and identify patterns.
- As a trader who runs Calendar Spreads, I want to see average P&L and win rate for my Calendar Spread bundles separately from my Wheel runs, so that I know which strategy type actually works for me.

### Intermediate Strategist (Pietro and similar)

- As a trader who runs a Wheel strategy on AAPL, I want to define my Wheel type once and apply it to every bundle that fits, so that my journal has a consistent structure without requiring me to re-describe the strategy each time.
- As a trader, I want to see which strategy types I run most often and which are most profitable, so that I can focus my time on what works.

---

## Requirements

### P0 — Must Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Create a custom strategy type | Trader can define a strategy type with: name (e.g., "Wheel"), description (free text, describes the legs and mechanics), and expected transaction types (e.g., Sell Put → Assign Stock → Sell Call). |
| Assign a strategy type to a bundle | When creating or editing a bundle (SPEC-02), trader can select a defined strategy type. The bundle's strategy name field (SPEC-02 free text) is superseded or complemented by the structured strategy type. |
| Strategy type view | Trader can see all bundles of a given strategy type in one view: underlying, start date, duration, total P&L, open/closed status. |
| Cross-bundle analytics by strategy type | Trader sees aggregate stats for a strategy type: number of completed runs, average P&L per run, win rate (positive P&L runs / total runs), average duration. |

### P1 — Nice to Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Filter cross-bundle analytics by underlying | Trader can filter the strategy type view to show only Wheel runs on AAPL, or only Calendar Spreads on SPY, etc. |
| Filter cross-bundle analytics by time period | Trader can filter by date range: "show me all Wheel runs in 2025." |
| Strategy type comparison view | Trader can compare two or more strategy types side by side: avg P&L, win rate, number of runs. |
| Preset strategy library | MindTrajour provides a set of common predefined strategy types (Wheel, Covered Call, Cash-Secured Put, Bull Put Spread, Calendar Spread, Diagonal Spread, Iron Condor) that traders can adopt without defining from scratch. Traders can customize or extend these. |

### P2 — Future Consideration

| Requirement | Notes |
|-------------|-------|
| Strategy type leg validation | When logging a lifecycle event (SPEC-03), MindTrajour can optionally warn the trader if the event does not match the expected leg sequence for the assigned strategy type. |
| Strategy type dashboard | A dedicated view per strategy type showing P&L over time, performance by underlying, and streak tracking (consecutive wins/losses). |
| Strategy type sharing / export | Trader can export or share a strategy type definition — e.g., share a custom Wheel template with another MindTrajour user. |

---

## Success Metrics

**Leading indicators** (visible within weeks of release):
- % of active users who define at least one custom strategy type within 30 days of release.
- Levi confirms MindTrajour can replicate the structure of his strategy-specific spreadsheet tabs.

**Lagging indicators** (visible over 1–2 sprints):
- Traders who previously maintained separate spreadsheets per strategy type consolidate into MindTrajour only.
- "No way to compare strategies" disappears from user feedback.
- Levi confirms MindTrajour is meaningfully superior to his spreadsheets as an analytical tool.

---

## Open Questions

| Question | Owner |
|----------|-------|
| Should the strategy type's "leg structure" be a structured definition (dropdown of transaction types in sequence) or free text? A structured definition enables validation (SPEC-03) and automation, but adds complexity to setup. Free text is simpler but has no machine-readable semantics. | Product |
| If MindTrajour provides preset strategy templates (Wheel, Covered Call, etc.), should they be locked or editable? Locked presets ensure consistency; editable ones match how traders actually implement strategies. | Product |
| How is the transition handled from SPEC-02's free-text strategy name to SPEC-04's structured strategy type? Can a free-text bundle be retroactively categorized, or does the type need to be assigned at creation? | Product + Enes |
| Should strategy type analytics distinguish between "intentionally closed" and "assignment/called away" as different outcomes for the purposes of win/loss calculation? | Product |

---

## Timeline & Sequencing

- **Requires:** SPEC-01 (Stock Support) — stock-based strategies (Wheel, Covered Calls) cannot be defined without stock as a first-class asset type.
- **Requires:** SPEC-02 (Trade Bundles) — strategy types are categories applied to bundles; bundles must exist first.
- **Requires:** SPEC-03 (Option Lifecycle Actions) — lifecycle events (Roll, Assignment, Called Away) are the key events within a strategy run; their structured tracking is what makes cross-bundle comparison meaningful.
- This is the top of the feature dependency chain. SPEC-01 → SPEC-02 → SPEC-03 → SPEC-04.
- This spec is the analytical layer that transforms MindTrajour from a trade log into a trading performance tool — and the feature that makes Levi's spreadsheets fully replaceable.
