# Team Sprint Planning - February 22, 2026

## Metadata

- recorded_at: 2026-02-22
- duration: 90 min
- speakers: Adrian Rinnus, Enes Zorlu, Larissa Lange, Eve (E F)
- source: Fathom via Slack upload

## Summary

Sprint Planning für MindTrajour. Enes hat begrenzte Kapazität (6 Tage weg + Promotion-Präsentation). Sprint-Fokus: DB Cleanup + Quick-Win Bugs. Google Ads Vorbereitung parallel (Keyword Research done, LP Copy nächster Schritt, PostHog Setup durch Adrian). Eve hat Google Ads Kampagnen bereits vorbereitet (DE + EN + Excel-Switcher). Budget: 20€/Tag, erstmal DACH, deutsch. Larissa geht zur Investmesse im April. Markus-Video erscheint nächsten Samstag.

## Key Decisions

1. **Enes Sprint-Kapazität:** Max DB Cleanup + einige Quick-Win Bugs (Login/Signup, Default Fees, ggf. Expired Worthless)
2. **Google Ads Budget:** 20€/Tag, deutsch, DACH-Region zuerst, 1 Woche Testlauf
3. **LP Copy:** Adrian übernimmt Rework (mit Eves Keywords)
4. **PostHog:** Adrian setzt es auf (ersetzt Google Tag Manager)
5. **Ticker-Suche:** Name-Search enablen (Yahoo/FMP API hat Endpoint dafür)
6. **Bug-Reporting:** Larissa erstellt Shortcut-Tickets mit maximalem Kontext (Browser, OS, Schritte)
7. **Expiration-Date-Buttons:** Ändern auf "Next Friday" statt "Next Week" für Klarheit bei Multi-Expiry-Tickers
8. **Gross Premium Input:** Fix analog zu Strike Price (Placeholder statt Zero-Default)
9. **Investmesse April:** Larissa bucht Hotel/Flug

## Bugs besprochen

- Gross Premium Feld: Zero-Default statt Placeholder (Backend-Logik mit Minus)
- Expiration Buttons: "Next Week" mehrdeutig bei Tickers mit Mon/Wed/Fri Expiries (Apple etc.)
- Trade Management: Kein SL/TP-Calc für Multi-Leg Trades
- Login/Signup: Email-Zustellung (Spam) + kein Re-Request möglich nach Fenster-Schließung

## Transcript

[Full transcript preserved below]

---

@1:00 - Larissa Lange (MindTrajour)
I see just half of my face. I also saw only half of your face, but now you are fine.

@1:06 - E F
Okay, perfect.

@1:08 - Enes Zorlu
Hello. Hello. Hello.

@1:10 - Adrian Rinnus
Good evening.

[... full transcript as provided ...]
