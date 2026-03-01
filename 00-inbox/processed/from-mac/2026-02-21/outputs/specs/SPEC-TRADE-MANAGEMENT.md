# Spec: Trade Management Tool

**Status:** Draft — Bug fix P0, Stock extension pending SPEC-01
**Area:** Core Trading Experience
**Owner:** Enes
**Effort estimate:** Bug fix (multi-leg): 1–2 days | Stock extension: 1–2 days (after SPEC-01)
**Last updated:** February 2026

---

## Dependency Map

```
Dependency Map
────────────────────────────────────────────────────────────────
This spec         Depends on         Enables
────────────────────────────────────────────────────────────────
Phase 1           Nothing —          Correct SL/TP for all
Bug Fix           fix today          current option trades
(multi-leg)                          (single + multi-leg)

Phase 2           SPEC-01            Correct SL/TP for
Stock extension   Stock Support      stock positions and
                                     stock legs in Wheel /
                                     Covered Call strategies
```

---

## Problem Statement

The Trade Management Tool helps traders pre-calculate where they would stop out (Stop Loss) and where they would take profit (Take Profit) before entering or managing a trade. For **single-leg options** (a single put or call), the calculations are working correctly.

For **multi-leg options** (spreads, condors, strangles — any trade with more than one option leg), the tool produces wrong numbers or behaves unexpectedly. A spread is not the sum of its legs in isolation — the risk/reward profile of the position is defined by the **net debit or credit** of the spread as a whole, and by the **spread width** (difference between strikes). If the tool calculates each leg independently, the resulting Stop Loss and Take Profit targets are meaningless.

Additionally, once **Stock Support (SPEC-01)** ships, the tool must be extended to handle stock positions, which follow a fundamentally different calculation model (price-based rather than premium-based).

---

## Trade Types and Calculation Logic

### Phase 1 — Options (Bug Fix)

#### Single Leg (currently working — maintain)

| Trade type | Max loss | Max profit | Common SL rule | Common TP rule |
|------------|----------|------------|----------------|----------------|
| Short put / Short call (premium seller) | Uncapped (put: strike − credit) | Net credit received | Close at 200% of credit received | Close at 50% of max profit |
| Long call / Long put (premium buyer) | Premium paid | Uncapped | Close at 50% of premium paid | Close at 2× or 3× premium paid |

**Key inputs:** premium per contract, number of contracts, strike(s)

#### Multi-Leg / Spreads (Phase 1 fix)

The fundamental input for all spread types is the **net premium** (credit received or debit paid for the whole spread) and the **spread width** (difference between the two strikes in a vertical spread).

| Spread type | Net position | Max loss | Max profit |
|-------------|-------------|----------|------------|
| Credit spread (bull put, bear call) | Net credit received | (Spread width − net credit) × contracts × 100 | Net credit × contracts × 100 |
| Debit spread (bull call, bear put) | Net debit paid | Net debit × contracts × 100 | (Spread width − net debit) × contracts × 100 |
| Iron condor / Iron butterfly | Net credit received | (Wider spread width − net credit) × contracts × 100 | Net credit × contracts × 100 |
| Strangle / Straddle | Net debit paid | Net debit × contracts × 100 | Uncapped (usually target 2×–3× debit) |

**Common multi-leg rules:**
- Credit spreads: take profit at 50% of max profit (buy back the spread at 50% of the credit); stop loss at 200% of credit received
- Debit spreads: take profit at 50%–75% of max profit; stop loss at full debit paid

**What the tool must calculate:**
1. Aggregate leg premiums → net debit or credit
2. Identify spread width from strikes
3. Derive max profit and max loss from those two numbers
4. Apply configurable % targets (TP %, SL %) to produce absolute dollar values and price levels

---

### Phase 2 — Stocks (after SPEC-01 ships)

Stocks do not have premiums or expirations. Stop Loss and Take Profit are price-based.

| Calculation | Formula |
|-------------|---------|
| Stop Loss level | Entry price − (SL % × entry price) for long; Entry price + (SL % × entry price) for short |
| Take Profit level | Entry price + (TP % × entry price) for long; Entry price − (TP % × entry price) for short |
| Dollar risk (long) | (Entry price − Stop Loss price) × shares |
| Dollar gain target (long) | (Take Profit price − Entry price) × shares |
| Risk/Reward ratio | Dollar gain target ÷ Dollar risk |

**What the tool must calculate:** SL price, TP price, dollar risk, dollar gain, R:R ratio.

For **Wheel / Covered Call trades** (stock + options combined): the stock leg and the options leg should each be calculated according to their own model, but the tool should also surface the **blended P&L** for the full position.

---

## UX

### Current (single-leg) — maintain

The tool currently shows inputs for a single leg and calculates SL/TP based on that leg's premium. This flow stays unchanged for single-leg trades.

### Multi-Leg (Phase 1 fix)

When a trade has more than one options leg:
- The tool should aggregate leg premiums automatically to show **net debit / net credit** as the primary input
- Show **max profit** and **max loss** as calculated values (not inputs)
- Allow the trader to set **TP %** (e.g., 50% of max profit) and **SL %** (e.g., 200% of credit) → tool converts these to dollar amounts

### Stocks (Phase 2)

When a trade is a stock position:
- Inputs: entry price, number of shares, SL %, TP %
- Outputs: SL price, TP price, dollar risk, dollar gain, R:R ratio

---

## Success Criteria

### Phase 1 (Bug Fix — Sprint 1)

- [ ] Multi-leg option trades show **net debit or net credit** as the primary P&L basis, not individual leg premiums summed incorrectly
- [ ] Max profit and max loss correctly reflect the spread structure (credit spread vs. debit spread formula)
- [ ] SL and TP targets derived from configurable % rules applied to max profit / max loss
- [ ] Single-leg behavior is unchanged (no regression)
- [ ] Verified manually on: bull put spread, bear call spread, iron condor, debit call spread

### Phase 2 (Stock Extension — after SPEC-01)

- [ ] Stock positions show price-based SL / TP (not premium-based)
- [ ] Dollar risk and dollar gain correctly calculated from shares × price delta
- [ ] R:R ratio displayed
- [ ] Wheel / Covered Call blended view shows stock leg + options leg P&L separately and combined

---

## Out of Scope

- Broker-integrated stop orders (the tool calculates targets — it does not place orders)
- Greeks-based stop management (delta, theta hedging) — too advanced for V1
- Multi-currency position sizing — deferred until Multi-Currency (F10) ships
- Automated alerts when SL/TP levels are hit — no live pricing in V1

---

## Open Questions

| Question | Owner |
|----------|-------|
| How are multi-leg trades currently entered in the UI — as one combined entry form or as separate individual legs? This determines whether the bug is in data aggregation or in the calculation layer. | Enes |
| Should the TP % and SL % be configurable per-trade only, or also saveable as defaults (similar to the Default Transaction Fees feature)? | Adrian |
| For the Wheel strategy (stock + multiple option legs over time), should the Trade Management Tool operate on each leg independently or on the whole Wheel cycle P&L? The latter requires Trade Bundles (SPEC-02). | Adrian |
| Is the "Trade Management Tool" a separate modal/panel, or is it embedded in the trade entry form? | Adrian |
