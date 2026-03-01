# Feature Spec: Stock Support

**Status:** Draft
**Product area:** Core Journaling
**Dependencies:** None — this is a foundation feature
**Enables:** Trade Bundles (SPEC-02), Option Lifecycle Actions (SPEC-03), Custom Strategy Builder (SPEC-04)
**Last updated:** February 2026

---

## Problem Statement

MindTrajour currently supports only options trades. A trader who wants to log a stock purchase, a stock sale, or a dividend payment has no way to do so. This means the app is unusable as a primary journal for anyone who holds stocks — whether they trade stocks exclusively or alongside their options activity. The portfolio P&L is incomplete, open positions are missing, and the trading record does not reflect reality.

This is not a niche use case. Nearly every active options trader in our research also holds or trades stocks. Without stock support, MindTrajour cannot be a complete trading journal for the majority of its user base.

---

## Goals

1. A trader who trades stocks — whether exclusively or alongside options — can log their full stock activity in MindTrajour.
2. Stock transactions appear in the trade history and contribute to the overall portfolio P&L.
3. Traders can see what stock positions they currently hold.
4. Dividend income is trackable as part of the total return on a stock position.
5. Stock support is in place as the foundation for Trade Bundles and Option Lifecycle Actions to build on top of.

---

## Non-Goals

- **Option lifecycle events** (Assignment, Called Away, Roll) — these connect options to stocks and are a separate feature (SPEC-03: Option Lifecycle Actions).
- **Live stock prices or real-time position valuation** — traders log transactions manually; no market data feed is required for this feature.
- **Automatic trade import or broker sync** — manual entry only. Broker import is a separate feature.
- **Multi-currency conversion for stock positions** — currency handling is a separate feature.
- **Stock analytics** beyond basic P&L and position tracking — sector breakdown, correlation analysis, etc. are out of scope.
- **Linking stock trades to strategies or bundles** — that is handled in SPEC-02 (Trade Bundles).

---

## User Stories

### Stock-Only Trader

- As a trader who holds stocks, I want to log a stock purchase with ticker, quantity, price, and date, so that my position and cost basis are correctly recorded.
- As a trader, I want to log a stock sale, so that my realized gain or loss is calculated and shown in my history.
- As a trader, I want to see which stock positions I currently have open and at what cost basis, so that I know what I own at any given moment.

### Dividend Investor

- As a trader who receives dividends, I want to log a dividend payment on a stock I hold, so that my total return on that position includes income — not just capital gains from price movement.
- As a trader who holds short stock positions that pay dividends, I want to log a dividend paid, so that this cost is correctly deducted from my P&L.

### Any Active Trader

- As a trader with a mix of options and stock activity, I want to see stock transactions in the same trade history as my options trades, so that I have one complete record of everything I've done.

---

## Requirements

### P0 — Must Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Log a Buy Stock transaction | Trader can record: ticker, number of shares, price per share, date. Appears in trade history, contributes to portfolio P&L. |
| Log a Sell Stock transaction | Trader can record: ticker, number of shares, price per share, date. Realized gain/loss is calculated and shown. |
| Log Dividend Received | Trader can record: ticker, dividend amount, date. Amount is included in total P&L. |
| Log Dividend Paid | Trader can record: ticker, dividend amount, date. Amount is deducted from P&L. |
| Stock transactions appear in trade history | Stock entries appear in the same trade log as options trades, clearly labeled by transaction type. |
| Stock transactions contribute to portfolio P&L | Total portfolio P&L reflects all stock-related transactions, not just options. |

### P1 — Nice to Have

| Requirement | Acceptance Criteria |
|-------------|---------------------|
| Open stock positions visible | Trader can see which stock positions are currently open: ticker, quantity held, average cost basis. |
| Unrealized P&L on open stock positions | Trader can see unrealized gain/loss on currently held shares. *(See Open Questions — requires current price.)* |

### P2 — Future Consideration

| Requirement | Notes |
|-------------|-------|
| Stock position history | How a position changed over time through buys, sells, and dividends. |
| Per-stock P&L analytics | Which stocks contributed most to overall returns over a given period. |

---

## Success Metrics

**Leading indicators** (visible within weeks of release):
- % of active users who log at least one stock transaction within 30 days of release.
- "Can't log stocks" disappears from user feedback.

**Lagging indicators** (visible over 1–2 sprints):
- Traders who previously split their journal between MindTrajour and a spreadsheet consolidate into MindTrajour only.

---

## Open Questions

| Question | Owner |
|----------|-------|
| For open stock positions: should unrealized P&L be shown? If yes, does the trader enter the current price manually, or is it fetched from a data source? | Product + Enes |
| How do we handle partial position changes — e.g., buying 50 shares at one price and 50 more at another? Is cost basis averaging automatic? | Product |
| Does a stock transaction need a notes or tags field at launch, or does that come with the broader Tags feature? | Product |

---

## Timeline & Sequencing

No hard external deadline. However, this is a prerequisite for:

- **SPEC-02 Trade Bundles** — stock transactions need to exist before they can be included in a bundle
- **SPEC-03 Option Lifecycle Actions** — Assignment and Called Away create or close stock positions
- **SPEC-04 Custom Strategy Builder** — stock-based strategies (Wheel, Covered Calls) cannot be defined without stock support
