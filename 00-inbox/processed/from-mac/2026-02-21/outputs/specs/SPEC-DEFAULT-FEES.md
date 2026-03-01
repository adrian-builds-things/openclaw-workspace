# Spec: Default Transaction Fees

**Status:** Draft
**Area:** Core Product / Trade Entry
**Owner:** TBD
**Effort estimate:** 1–2 days
**Last updated:** February 2026

---

## Dependency Map

```
Dependency Map
────────────────────────────────────────────────────────────────
This spec         Depends on         Enables
────────────────────────────────────────────────────────────────
Default           User settings      Correct P&L and net
Transaction       table (Supabase,   profit on every trade
Fees              already exists)    without manual fee
                                     entry on each trade

                                     Prerequisite for
                                     accurate win rate
                                     and strategy P&L
                                     once Trade Bundles ship
```

---

## Problem Statement

Options traders pay a fixed commission per contract to their broker — $0.65/contract is the standard at TD Ameritrade and Schwab, $0.50/contract at Tastytrade, $0.00 at some discount brokers. This fee is identical for virtually every trade a given trader places.

Currently, every time a user creates a trade entry in MindTrajour, they must manually enter this fee. A trader placing 10 trades per week with 5 contracts each is typing the same $0.65 value 50 times per week. In practice, users skip it — which silently corrupts every P&L calculation, win rate, and strategy analysis in the app. A trade that shows "$120 profit" before fees may actually be "$87.50 profit" after a $32.50 commission on 50 contracts.

This is a data quality problem disguised as a minor UX annoyance.

---

## What Users Can Do

| Action | Available |
|--------|-----------|
| Set a default fee per contract (options trades) | ✅ Yes |
| Set a default flat fee per trade (all trade types) | ✅ Yes |
| Override the pre-filled fee on any individual trade | ✅ Yes |
| Leave fees at zero (opt out of the default) | ✅ Yes |
| Set different defaults per broker account | ❌ No — V2 |
| Have regulatory fees (SEC, ORF) auto-calculated | ❌ No — V2 |

---

## User Flow

The primary interaction point is the **Trade Details page**, not a settings page. The default is managed contextually — right where fees appear — so users never need to navigate away to configure it.

### First Use (no default set yet)

1. User opens a trade entry or the Trade Details page
2. The Order Fee field is empty
3. Next to the Order Fee field there is a small icon button (e.g., ⚙️ or a gear/pencil icon)
4. User clicks it → a popup opens
5. Popup shows two fields: **Fee per contract** and **Flat fee per order**, both empty
6. User enters their broker's standard rates (e.g., `0.65` per contract)
7. User confirms → popup closes, the fee field is now pre-filled with the new default
8. Success state: small confirmation ("Default saved") inline or as a brief toast

### Normal Use (default already set)

1. User opens a new trade entry
2. Order Fee field is **pre-filled** from the stored default
3. That's it — no interaction needed for the common case

### Overriding the Fee on a Single Trade

The Order Fee field on the trade form is always a normal editable input. The user types a different value directly — no popup, no confirmation required. The stored default is not affected. This handles edge cases like free trades, broker promotions, or trades with unusual contract sizes.

### Updating the Default Fee

1. User is on any Trade Details page
2. User clicks the small icon button next to the Order Fee field
3. Popup opens, showing the **current default values** pre-filled
4. User edits one or both values and confirms
5. Popup closes — the new defaults are saved to Supabase
6. The current trade's fee field updates to reflect the new default (if the user hasn't manually overridden it)

```
Trade Details page — Order Fee row:

  Order Fee   [ 0.65  ] $ per contract  ⚙️
              [ 0.00  ] $ flat fee

              Total commission: $3.25  (5 contracts × $0.65)

  ⚙️ icon opens the "Set Default Fees" popup:

  ┌─────────────────────────────────────────┐
  │  Default Order Fees                     │
  │                                         │
  │  Per contract   [ 0.65  ] $             │
  │  Flat per order [ 0.00  ] $             │
  │                                         │
  │  Applied to all new trades.             │
  │  You can always adjust per trade.       │
  │                                         │
  │              [ Cancel ]  [ Save ]       │
  └─────────────────────────────────────────┘
```

---

## Data Model

No new table required. Add two columns to the existing user settings table:

```sql
ALTER TABLE user_settings
  ADD COLUMN default_fee_per_contract DECIMAL(8, 4) NOT NULL DEFAULT 0,
  ADD COLUMN default_flat_fee_per_trade DECIMAL(8, 4) NOT NULL DEFAULT 0;
```

Default values of `0` mean no change to existing behavior — users who have never set a default see the same empty fields they see today.

---

## Fee Calculation

Total commission per trade:

```
total_commission = (num_contracts × default_fee_per_contract) + default_flat_fee_per_trade
```

Net P&L:

```
net_pnl = gross_pnl - total_commission
```

The fee fields are editable, so the actual stored value is whatever the user confirms on the trade entry form — the default merely pre-fills those fields.

---

## UI Details

### Icon Button (Trade Details page)

Small, unobtrusive — does not compete visually with the fee input itself. A gear (⚙️) or pencil icon works. Tooltip on hover: "Set as default fee." Visible at all times, not only when the field is empty.

### Popup

- Title: **"Default Order Fees"**
- Two numeric inputs: "Per contract" (suffix `$`) and "Flat per order" (suffix `$`)
- Helper text below inputs: *"Applied to all new trades. You can always adjust per trade."*
- Two buttons: **Cancel** (closes popup, no changes) and **Save** (persists to Supabase, closes popup)
- On save: brief inline confirmation or toast — "Default saved"
- Popup does not block the trade form behind it — user can still see their trade context

### Fee Display on Trade Form

The Order Fee row on the trade form shows:
- Per-contract fee input (pre-filled)
- Flat fee input (pre-filled)
- Calculated total commission: `(contracts × per-contract) + flat` — shown read-only below or next to the inputs, updates live as the user edits either field

---

## Success Criteria

- [ ] Small icon button (⚙️ or pencil) visible next to the Order Fee field on the Trade Details page
- [ ] Clicking the icon opens the "Default Order Fees" popup with current defaults pre-filled
- [ ] User can set or update `default_fee_per_contract` and `default_flat_fee_per_trade` via the popup
- [ ] Saving the popup persists the values to Supabase user_settings
- [ ] Brief confirmation shown after saving ("Default saved")
- [ ] New trade entries are pre-filled from stored defaults immediately after saving
- [ ] The Order Fee field on the trade form is always directly editable — user can override the pre-filled value without opening the popup
- [ ] Overriding the fee on a trade does not change the stored default
- [ ] Total commission shown live on the trade form: `(contracts × per-contract fee) + flat fee`
- [ ] Users who have never set a default see empty fee fields — no regression
- [ ] Defaults of zero are valid — no validation error
- [ ] Works for both options trades (per-contract fee applies) and stock trades (flat fee only)

---

## Out of Scope (V1)

- Per-broker-account fee defaults (V2 — requires broker account model)
- Automatic regulatory fee calculation: SEC fee, ORF, FINRA TAF
- Retroactive fee application to past trades
- Fee schedule imports (CSV with broker fee tables)
- Different fee tiers by contract count (e.g., volume discounts)
- Tax treatment of commissions

---

## Open Questions

| Question | Owner |
|----------|-------|
| Should stock trades support a "per-share fee" option in addition to the flat fee? (Some brokers charge per share, not per trade.) | Adrian |
| Should the ⚙️ icon also appear on the trade list/overview, or only on the Trade Details page? | Enes |
| Should we show total commissions paid anywhere in the statistics view? (E.g., "You paid $312 in commissions this month") — this would make the default fee data valuable beyond just P&L accuracy. | Adrian |
| Should existing trades with no fee recorded get a retroactive default applied? Or only new trades going forward? | Adrian |
