# Adrians Aufgaben — Priorisiert (22.02.2026)

> Sortiert nach Umsatz-Impact × Dringlichkeit. Nur Adrians Tasks.
> Aktualisiert mit Meeting-Kontext vom 22.02.2026 (Team Sprint Planning).

---

## 🔴 Sofort (diese Woche)

### 1. Shortcut-Tickets erstellen ✅ (erledigt in Shortcut)
**Kontext:** Adrian hat im Meeting zugesagt, Tickets nach dem Call zu erstellen. Enes bat: "Vielleicht einfach die Basis-Info reinkopieren, dann fülle ich den Rest aus." Enes hat max. Kapazität für DB Cleanup + ein paar Bugs diesen Sprint — er ist 6 Tage weg + Promotion-Vorbereitung (Präsentation am Mittwoch).
**Tickets (aus Meeting-Entscheidungen):**
- **Login/Signup Fix:** Re-Request-Seite für Bestätigungsmail wenn Fenster geschlossen + Spam-Hinweis. Enes: "Es ist wirklich einfach." Problem: Patrick und Jörg konnten sich nicht einloggen — Bestätigungsmail landet im Spam. Adrian hat Jörg 5 Emails geschrieben, keine Antwort → vermutlich auch im Spam. PostHog-Session prüfen ob mehr Infos da sind.
- **Default Transaction Fees:** Stift-Icon (⚙️/Pencil) neben Total Order Fee. Enes: "Ist nicht kompliziert, perfekt dort." Design im Meeting entschieden: direkt neben dem Fee-Feld, Popup mit 2 Feldern (per contract + flat fee). → Spec: `spec-default-fees.md`
- **Expired Worthless Button:** Quick Win, wenn Enes Kapazität hat. Häufigster positiver Outcome bei Income-Strategien. Position auf $0.00 schließen, Datum editierbar.
- **Gross Premium Input Fix:** Placeholder statt Zero wie bei Strike Price. Enes: "Es ist wegen der Backend-Logik, die Minus als Pay behandelt. Wenn es einfach ist, mach ich's. Wenn nicht, lass ich's." → kein Force, nur wenn machbar.
- **Expiration-Date Buttons:** Meeting-Entscheidung: "Next Friday" statt "Next Week" für die nächsten 2 Wochen, danach "In 1 Month" etc. Apple/SPY haben jetzt Mo+Mi+Fr Expiries (neu seit 2026). Montag/Mittwoch nicht als Buttons abdecken — sind bereits im Kalender sichtbar. Enes: "Die sind schon auf dem Screen sichtbar."
- **PostHog Analytics Event:** Tracking ob User die Expiry-Shortcuts oder den Kalender nutzt. Adrian im Meeting: "Bitte, lieber Notetaker, erinnere dich: wir wollen ein PostHog-Analytics-Event um zu sehen wie viele Leute die Shortcuts nutzen."
**Status:** Tickets in Shortcut bereits aktualisiert. Markdown-Specs hier mit Kontext ergänzt.

### 2. Landing Page Copy Rework
**Kontext:** Im Sprint Planning (22.02.) entschieden: Adrian schreibt den LP-Text. Eve hat Keywords fertig — primary: "options trading journal", long-tail für Nische (multi-leg, strategy support, Excel-Alternative). Eve: "Wir sollten auf High-Intent Long-Tail Keywords fokussieren, weil bei den generischen Keywords zu viel Competition ist."
**Meeting-Entscheidung Hero Section:** Team einig: Hauptseite braucht emotionalen Hook (Problem → Agitation → Solution) UND SEO-Keywords. Adrian: "Die Hero Section sollte über das Problem sprechen, den Pain erhöhen und dann die Lösung bieten — nicht Features." Enes stimmt zu: "Fluff raus, Values rein, dann kannst du den Ton machen wie du willst." Eve: "Wir können beides — emotionaler Copy UND Google-konforme Struktur." TradeZella rankt #1 weil "trading journal" in Description + Subtext steht — wir brauchen das auch prominent, aber nicht zwingend in der Headline.
**Heatmap-Insight:** PostHog Heatmap zeigt: "Bewertungen" werden am meisten geklickt → mehr Social Proof auf der LP.
**Deliverable:** Neuer Hero-Text + CTA-Struktur + Proof above-the-fold. Eve liefert Keyword-Set zum Einarbeiten.
**Warum jetzt:** Ohne saubere LP verbrennen Google Ads Geld. Ads sollen in ~2 Wochen starten.

### 3. PostHog Setup & Funnels
**Kontext:** Im Meeting klar entschieden: PostHog ersetzt Google Tag Manager komplett. Adrian: "PostHog sollte alles übernehmen, wir brauchen Tag Manager nicht mehr." Eve kannte PostHog noch nicht, studiert jetzt GA4 + GTM parallel. Adrian hat gezeigt: Google Ads + Stripe bereits in PostHog Destination Sources verbunden (Connection failed → muss gefixt werden). Heatmap funktioniert über Toolbar (Apps → Toolbar → URL eingeben → Launch).
**Revenue-Bug:** Eve hat gesehen: Revenue Analytics zeigt All-Time nur $425 statt real ~$1000. Adrian: "Muss ich fixen." Zeitraum-Filter und Setup prüfen.
**Deliverable:** 5 Customer Events + 6 Product Events + Signup→Subscription Funnel. Revenue-Tracking mit Stripe abgleichen. Google Ads Replay-Daten einrichten.
**Warum jetzt:** Ohne Funnel-Tracking sind Google Ads Blindflug. Kein Enes-Dependency.

### 4. Eves Google Ads Kampagnen reviewen
**Kontext:** Eve hat im Meeting komplett ausgearbeitete Kampagnen präsentiert (Screen geteilt):
- **3 Segmente:** DE (deutsch), EN (englisch), Excel-Switcher (Tool-Wechsler)
- **Struktur pro Kampagne:** Pinned Headlines (2), Rotating Headlines (8-10, nach Kategorie: Score Value, Differentiation, Measurement, Reframes Hook), 4 Descriptions, Negative Keywords (free template, download, Excel etc.), Callout Assets ("No Excel, No Guesswork", "Log Trades Under 60 Seconds", "Built by Options Traders", "7-Day Free Trial")
- **Site Link Assets:** Core Features, Trader Testimonials, Pricing & Plans
**Meeting-Entscheidungen:**
- Budget: 20€/Tag (Enes + Adrian einig), ~1 Woche laufen lassen für Statistik. CPC geschätzt €1.52–2.50.
- Zuerst deutsch, DACH-Markt. Enes: "Deutscher Markt macht mehr Sinn — weniger Competition, deutsches Unternehmen = mehr Trust."
- Eve prüft ob Whole-Europe mit deutschen Keywords sinnvoll ist (deutsche Expats im Ausland).
- Larissa setzt die Kampagne auf, braucht Adrians Freigabe.
- 1.200€ Ads-Budget verfügbar.
**Deliverable:** Review + Freigabe + ggf. Copy-Anpassungen. Eve teilt Dokument in Slack.
**Warum jetzt:** Ads sollen in 1-2 Wochen live gehen. Eve wartet auf Feedback.

---

## 🟡 Diese + nächste Woche

### 5. Ad-spezifische Landing Pages (Copy)
**Kontext:** Aus Roadmap: 3 intent-spezifische Seiten (vs Excel / vs TraderSync / Options Trading Journal). Team einig dass Vergleichsseiten legal sind. Eve: "Vergleich ist legal, solange wir deren Keywords nicht als unsere eigenen nutzen." Enes: "Wenn wir die Wahrheit sagen, können sie uns nicht verklagen — es sind öffentliche Daten." Larissa hatte Bedenken (Flat-Baby-Fall), aber Team hat geklärt: Vergleichsseiten ≠ Trademark-Missbrauch.
**Deliverable:** Copy-Drafts für 3 Subpages.
**Warum jetzt:** Google Ads Quality Score hängt von Landing Page Relevanz ab.

### 6. Scope-Disziplin: Enes' Sprint schützen
**Kontext:** Enes ist 6 Tage weg + Promotion-Vorbereitung (Präsentation am Mittwoch). Max-Kapazität: DB Cleanup + ein paar Bugs. Enes: "Das ist das Maximum diesen Sprint, leider. Vielleicht vor meinem ganzen Tag kann ich schnelle Sachen machen." Kein Feature-Creep.
**Action:** Keine neuen Requests an Enes bis Sprint-Ende. Nur die vereinbarten Tickets.

### 7. Ticker Name-Search + API Research
**Kontext:** Im Meeting aufgekommen: User können nur per Ticker suchen, nicht per Name (z.B. "Apple" findet nichts, nur "AAPL"). SPX ist nur über ^SPX findbar — Larissa wusste das nicht, konnte User nicht helfen. Enes: "Wir müssen Name-Search aktivieren. FMP hat eine API dafür. Yahoo hat auch einen Search-Endpoint." FMP Starter Pack: $19/Monat (annual) oder $29/Monat. Enes: "Zu früh um zu zahlen." Alternativer Fund: Marketstack hat Market Data API für $12/Monat. Adrian: "Ich schau mir das an."
**Meeting-Entscheidung:** Erst mal kein Geld ausgeben. Wenn API-Limit (100 Calls/Tag) erreicht wird, dann evaluieren.
**Deliverable:** Research-Doc an Enes schicken für Evaluierung nächsten Sprint.

---

## 🟢 Nächste 2-4 Wochen

### 8. Levi-Deal vorantreiben
**Kontext:** 60k YouTube Audience. Seine 2 Preconditions: Trade Bundles + Per-Leg Closing. Beides braucht erst Stock Support (SPEC-01) + DB Cleanup. Larissa soll Timeline-Email schicken.
**Action:** Sicherstellen dass Larissa Email mit konkretem Lieferdatum sendet. Kein finanzielles Commitment nötig.

### 9. Martin: Broker Import Q2 zusagen
**Kontext:** Martin (50-100 Trades/Tag) braucht CSV/IB Import. Hard Adoption Ceiling. 5-8 Tage Aufwand.
**Action:** Klare Q2-Zusage kommunizieren damit er nicht abspringt.

### 10. Investmesse April vorbereiten
**Kontext:** Larissa bucht bereits Hotel/Flug/Zug. Im Meeting: "Ich fand es 2024 super. Letztes Jahr war zu früh wegen App-Relaunch. Dieses Jahr ist perfektes Timing für B2B-Kontakte."
**Action:** Bis dahin: LP + Ads + erste Resultate haben. Demo-Material vorbereiten.

### 11. Marcos-Video veröffentlichen
**Kontext:** Larissa im Meeting: "Wir veröffentlichen unser Video nächsten Samstag. Marcos hat ca. 200 Views auf seinen Videos. Bei 1-2% Conversion Rate wären das 1-2 zahlende Kunden." Larissa hat beim Video-Dreh mit Marcos einen Bug gefunden (Expiry-Buttons, s.o.).
**Action:** Video-Launch tracken, Conversion messen.

### 12. Dokumentation / Feature-Beschreibungen
**Kontext:** Im Meeting angesprochen: Letzter Partner-Kontakt fragte nach Doku. Adrian: "Das kann auch SEO-relevant sein — Feature-Beschreibungen als Doku, die auch Google indexiert." Kein Enes-Dependency wenn externes Tool.
**Zusatz:** Larissa: SPX-Suche (^SPX) als Doku-Eintrag, bis Name-Search implementiert ist.
**Action:** Entscheiden: /docs Subfolder (besser SEO, braucht Enes) oder Subdomain (schneller, kein Enes).

### 13. Margin → Max Risk Diskussion
**Kontext:** Larissa: "Viele User fragen ob Margin editierbar sein kann oder in Max Risk umbenannt werden sollte. Wenn wir es Max Risk nennen, können wir es sogar automatisch berechnen (Strike-Differenz minus Premium)." Adrian: "Das ist komplex, wir hatten das schon in der alten Version. Und wir müssen mit Markus reden — er hat den Namen vorgeschlagen. Wenn alle höhere Werte eingeben, sinkt die angezeigte Rendite, und Markus ist unglücklich." → Nicht jetzt, aber als Diskussionspunkt für nächstes Meeting festhalten.

---

## ❌ Jetzt NICHT tun

- Custom Strategy Builder (braucht Stock Support + Trade Bundles + Per-Leg Closing erst)
- Broker Import bauen (Q2, nicht jetzt)
- Multi-Currency (Q2)
- Option Chain Data / ORATS (zu teuer, kein klarer ROI)
- Margin→Max Risk Umbenennung (Markus-Diskussion nötig, kein Umsatz-Impact jetzt — s. Task 13)
- Ticker Name-Search implementieren (nice-to-have, Enes hat keine Kapazität — s. Task 7 für API-Research)

---

## Wöchentliche Checkpoints

| KPI | Ziel |
|-----|------|
| LP Copy Draft | fertig bis Fr 28.02. |
| Tickets in Shortcut | fertig bis Mo 24.02. |
| PostHog Funnel live | fertig bis Fr 07.03. |
| Google Ads Review done | bis Mi 26.02. |
| Ads live | ~KW 10-11 |
