MindTrajour – Consolidated Customer Feedback (Monthly Summary of Client Feedback February 2026)

🔥 PRIORITY 1 — Requested by MANY users 



1. Strategy-Based Trade Lifecycle & Stock Assignment Support

Requested by: Gerhard, Roland, Jennifer, Pietro, Andreas, Ilona, Jörg, Thomas, Wolf, Ulrich, Christin,





Enable strategy-based grouping of trades across time and within accounts.

Treat strategies as first-class entities, not isolated trade legs.

Required for:

Wheel strategy (flagship use case)

Multi-leg option strategies (Iron Condor, Butterfly, Jade Lizard)

Hedging strategies (e.g. Zero Hedge)

Implement native end-to-end Wheel lifecycle tracking:

Short Put → Assignment → Stock position → Covered Call → Exit

Fully support stock assignment handling:

Close trades with assigned shares

Include realized and unrealized stock P&L

Provide accurate strategy-level performance metrics, combining:

Option premiums

Stock P&L

Eliminate distorted results caused by leg-level tracking.

➡️ Foundational architectural requirement and primary differentiator for MindTrajour



2. Automated Broker Trade Import (IB / CapTrader / TWS / CSV / API)

Requested by: Martin, Roland (email), Roland (interview), Pietro, Ulrich, Jennifer (community), Martin

Automatic import from brokers (IB, CapTrader, TWS via Flex Queries)

CSV / API / JSON import as fallback

Optional hybrid model: auto-import + manual enrichment

Mandatory for:

High-frequency traders (50–100 trades/day)

0DTE traders

Without this feature, several users explicitly stated they cannot use MindTrajour

➡️ Hard adoption blocker



⚠️ PRIORITY 2 — High demand 

3. Custom Strategy Builder (User-Defined Multi-Leg Strategies)

Requested by: Jennifer, Pietro, Andreas, Jörg, Roland

Build & name custom strategies

Variable number of legs

Strategy templates:

Iron Condor

Butterfly

Jade Lizard

Collar

Strategy-level analytics & payoff logic



4. Partial Trade Closing (“Einzel-Schließen”)

Requested by: Martin (Power Trader)

Close trades in parts (e.g. 20 / 20 / 20 / 40 contracts)

Trade only considered closed once final leg is closed

Essential for professional options workflows



5. Multi-Currency Support (USD, EUR, CHF, HKD)

Requested by: Martin, Pietro, Chris

One account, multiple currencies

Automatic currency detection via ticker

Proper P&L aggregation

No manual conversion



6. Advanced Strategy & Performance Analytics

Requested by: Pietro, Roland, Thomas, Jennifer

Strategy-level analytics:

Win rate

Drawdown

Max risk vs realized loss

Replace external tools (TraderSync, Excel)

Time-based views:

Weekly / monthly / yearly P&L



🧠 PRIORITY 3 — UX, Psychology & Professional Workflow

7. Rename “Margin” → “Max Risk”

Requested by: Pietro, Jennifer, Gerhard

Margin is broker-specific and misleading

Users want to enter maximum possible loss

Add helper text / tooltip

idea: Make description for trade entry editable. (e.g. User can change margin to max risk ) 
OR 2. idea: change margin to max loss and auto fill when both strikeprices and premium and eventually order fee are entered. We can calculate max risk for spreads and make life easier for the user. 



8. “Trade Expired Worthless” Button

Requested by: Gerhard, Pietro

One-click close for expired options

Automatically sets exit price & fees to zero

Prevents statistical distortion





9. Required Fields Clearly Marked

Requested by: Larissa, onboarding feedback

Mark required fields at trade entry with *

Avoid confusion during trade entry
User thought all values are required, but they are not e.g. win probabilty or orderfee



10. Stop-Loss Calculation Bug (Critical)

Reported by: you

Spread stop-loss exceeds max theoretical loss

Bull Put Spread loss > defined strike risk

Calculation inconsistency between staging & prod

➡️ Trust-breaking bug



11. Filterable Tags (Errors, Emotions, Strategy Variants)

Requested by: Pietro, Gerhard

Custom tags (e.g. “revenge trade” Or "hedge trade"

Filter & analyze performance by tag

Enables behavioral edge discovery



12. Always-Visible Notes Field

Requested by: Pietro, Ilona

Notes visible directly in trade entry



potentially also enabling deletion of single notes and upload function for pictures. 



Encourage:

Trade plan

Emotions

Rationale



13. Emotion Tracking Linked to Performance

Requested by: Jennifer, Pietro

Track emotions per trade and show analysis on dashboard

Analyze emotional patterns vs results



🧩 PRIORITY 4 — Platform Stability, Access & Trust

14. Login & Email Confirmation Reliability

Reported by: Patrick, Jörg

Missing confirmation emails

Broken signup flow

Discount codes not working

➡️ Revenue blocker



15. Sorting & Filter Persistence Bugs

Reported by: Pietro, Thomas

Monthly bars not chronological

Filters reset after navigation (Safari issue)



16. Decimal Separator Handling (, vs .)

Reported by: Pietro

Regional input errors

Leads to incorrect data



17. Ticker Coverage & Documentation (SPX, Futures)

Reported by: Jörg, Ilona

SPX not found (Ilona reported that Pietro told her SPX can be found by  typing: ^SPX in our ticker search



Needs:

Help text

Docs / FAQ





18. Tax Estimation / Tax Reporting (Longer-Term)

Requested by: Roland, Jörg

Yearly tax estimation on options profits

Especially relevant for EU users



19. Documentation / Handbook

Requested by: Ilona

Users unsure if features exist or not

Reduces support load



🧠 Strategic Insight (Across All Feedback)

Current perception:

Excellent UI & onboarding

Analysis too shallow for professional traders

Clear message from advanced users:

“Make MindTrajour a serious analytics & execution companion — not just a journaling UI.”

If the Priority 1 + 2 features are delivered:

MindTrajour can replace Excel + TraderSync








Detailed User Feedback one by one



Pietro:



Meeting 2.2.26 https://fathom.video/share/U4snNKvxNwiJf3P3dpxTvL_awCscwi3v




- He wishes renaming of margin to Risk, he prefers to type in max loss rather than margin

Community 1 h Freiheit von Thomas Mangoldt- Affiliate Link share

Here’s a clear, product-ready English summary of the main feature wishes for the MindTrajour app, based on Pietro’s feedback session:



Core Problem: Missing Advanced Analytics

MindTrajour works very well for beginner traders thanks to its clean and simple overview.
However, advanced users lack deep analytical tools, which forces them to use a second platform (TraderSync) for serious performance analysis.

The goal is to fully replace external tools by adding advanced analytics directly into MindTrajour.



Key Feature Wishes

1. Filterable Tags (for Errors & Strategies)

What users want:

Ability to create custom tags (e.g. “emotional mistake”, “hedging”, “revenge trade”).

Apply these tags to trades.

Filter and analyze performance by tag.

Why it matters:

Enables behavioral analysis.

Example: Pietro discovered a $10,000 loss in 2025 caused purely by emotional mistakes — insight currently not possible in MindTrajour.



2. Custom Strategy Builder (Multi-Leg Strategies)

What users want:

A way to build and name custom strategies (e.g. Iron Condor, Wheel, Hedging setups).

Ability to group related trades into one strategy.

Why it matters:

Many strategies consist of multiple legs.

Without grouping, performance looks wrong because single legs appear as isolated losses.

Users want strategy-level P&L, not just trade-level.



3. Multi-Currency Support

What users want:

Track trades in different currencies (EUR, USD, CHF, HKD) within one account.

Automatic currency detection via ticker symbol.

Why it matters:

No need for multiple accounts.

No manual currency conversion.

Crucial for international traders.



Workflow & UX Improvements

4. “Expired Worthless” Button

What users want:

A button to mark a trade as expired worthless.

Automatically sets closing price and fees to zero.

Why it matters:

Saves time.

Ensures expired options are correctly included in statistics.



5. Always-Visible Notes Field

What users want:

A small visible notes field in the trade entry view underneath performance profile



Why it matters:

Encourages users to write down:

Trade plan

Reasoning

Emotions

Reduces friction compared to hidden note fields.



6. Automated Data Import

What users want:

API or CSV import from brokers (e.g. Interactive Brokers).

Why it matters:

Less manual work.

Fewer input errors.

Much faster journaling.



Critical Bugs to Fix

7. Random Monthly Performance Sorting

Monthly bars are not sorted chronologically.

Makes it impossible to see real performance trends.

8. Filters Reset After Navigation

Filters reset when switching pages.

Forces users to reapply them constantly.

Especially problematic in Safari.

9. Decimal Input Issues

Comma vs dot (, vs .) causes errors in some regions.

Leads to incorrect data entry.



Strategic Insight for Product Direction

MindTrajour’s positioning today:

Excellent for beginners.

Too shallow for professional traders.

What advanced users want:

“Turn MindTrajour into a serious analytics tool, not just a journaling UI.”

If these features are implemented, MindTrajour can:

Replace tools like TraderSync.

Become a single source of truth for both:

Behavioral trading psychology

Professional performance analytics.



Problems found by me: 



The stop loss for the spread seems incorrect.
On the stop-loss timeline slider, the loss shown exceeded the maximum possible loss defined by the strike prices.



It is a bull put spread strategy total loss is here over 900 which is not possible. 





in the staging environment the max loss is better, but still I dont get the exact calculation. 
in my opinion it is 500-70-3 = 427 not 426









The fields are prefilled with zeros, which always have to be manually deleted, for example in the gross total premium field.
Show required fields with a star (Gross entry premium, and Margin, some users thought all entry data is required









Mr. Holding



mr@mr-holding.de

Hallo Larissa,

Vielen Dank für Deine eMail.

Für mich „als Powertrader (Optionen)“ fehlen zwei elementare Funktionen um es wirklich nutzen zu können:

- Import der Trades vom Broker (IB / CapTrader) => damit ich sie dann „nur noch“ nachbearbeiten muss => ich mache pro Tag im Schnitt 50-100 Trades….. => der Broker würde dafür via Flex-Querys alles Bereitstellen ;)  

- "Einzel-Schließen" eines Trades => Beispiel:

   * Verkaufe 100 K. 100P 

   * Schließe (Rückkauf) 20 K. Noch Tag X

   * Schließe (Rückkauf) 20 K. Noch Tag X

   * Schließe (Rückkauf) 20 K. Noch Tag X

   * Schließe (Rückkauf) 40 K. Noch Tag X => erst jetzt ist Trade beendet => das lässt sich derzeit nicht abbilden…..

Das mein Feedback.

Herzliche Grüße

Martin



….ich nochmal ;)

Mein Depotkonten laufen in EUR; das OptionsTrading findet in USD statt. Prämieneinnahmen / eventueller Aktienkauf durch Zuteilung in USD => ja die beiden Währungen sind ein Thema……

Bzgl. Prio => ich bräuchte tatsächlich Import + „Einzelschließen von Trades“ bevor ich es wirklich nutzen kann.

liebe Grüße

Martin


 

Herzliche Grüße vom Chiemsee









Gerhard



Gerhard Interview 6.2. : https://fathom.video/share/LdsmCzsKhE2LsyEtHeEXWczhmop3WXXs



1. Trade Expiration Handling

Add a dedicated “Trade Expired” button

Allows users to close option trades that expire worthless with one click.

Automatically sets exit price to 0 and closes the trade correctly.

Reduces confusion and manual input errors.



2. Exit Price Default Behavior Improvement

Remove default “0” value from the Exit Price field

Current default value forces users to manually delete it.

Exit price field should be empty by default or context-aware.

Improves UX during trade closing workflows.



3. Margin Field Clarification & Guidance

Clarify the meaning of the “Margin” field

Explicitly communicate that users should enter maximum possible loss, not broker-required initial margin.

Could be implemented via:

Helper text

Tooltip

Inline explanation or example

Goal: ensure consistent and conservative risk tracking.



4. Strategy-Level Trade Grouping (Wheel Strategy)

Support “Wheel of Options” as a native strategy

Ability to link related trades (e.g. Short Put → Covered Call) into a single strategy unit.

Enables performance tracking of the full Wheel lifecycle instead of isolated trades.

Improves strategy-level analytics and learning.



5. Multi-Leg Options UX Enhancements

Improve UX for complex / multi-leg options (e.g. Bull Put Spreads)

Reduce ambiguity when entering:

Premium values

Entry vs. exit logic

Potential improvements:

Contextual hints per leg

Smarter defaults

Validation or warnings for inconsistent inputs



6. Risk Management Strategy Tracking (Future Enhancement)

Enable tracking or tagging of stop-loss logic

Allow users to document how a trade is managed (e.g. stock-based stop vs. option-price-based stop).

Supports post-trade analysis and comparison of risk management approaches.

Could be implemented as:

Trade tag

Strategy parameter

Optional notes with structured fields



7. Enhanced Trade Sharing (Optional Enhancement)

Improve trade-sharing via public or semi-public links

Shareable view should clearly display:

Strategy structure

Strikes

Premiums

Payoff visualization

Goal: make it easier to discuss and explain trades with others.


 



Patrick



patrick.weiss85@gmx.de

Hallo Larissa,

Ich habe versucht mich mehrmals anzumelden aber jedes Mal hat es nicht funktioniert 🥲. 

Gibt es da einen Trick das es funktioniert.. 

Gruß Patrick 
 



Jörg



ludwig68@me.com

Hallo Larissa,



vielen Dank für deine Nachricht.



Meine bisherige Erfahrung war leider nicht so gut – ich konnte den Zugang bislang nicht nutzen, da ich keine Bestätigungsmail erhalten habe. Ich habe mich diesbezüglich bereits an den Support gewandt, aber bisher leider noch keine Rückmeldung bekommen.



Ich bin über euer YouTube-Video auf das Tool aufmerksam geworden und würde auch gerne den 50 %-Rabatt in Anspruch nehmen. Allerdings finde ich den Rabattcode “easy” ebenfalls nicht bzw. konnte ihn bislang nicht einlösen.



Insgesamt also bisher leider kein optimaler Start – ich hoffe, das lässt sich noch klären.



Viele Grüße

Jörg



Hallo,
 

ich habe mir inzwischen die Zeit genommen, Ihr Trading Journal etwas genauer anzusehen und es zunächst abonniert.



In diesem Zusammenhang habe ich zwei Fragen:

Zum einen würde ich gerne für mich und meine Kinder jeweils eigene Konten anlegen. Ist dies grundsätzlich möglich?



Zum anderen interessiert mich, ob es möglich ist, eigene Strategien hinzuzufügen bzw. bestehende Strategien – zum Beispiel in Richtung einer Collar-Strategie – zu erweitern. Falls dies derzeit nicht möglich ist oder auch mittelfristig nicht geplant sein sollte, wäre der Nutzen für mich leider eingeschränkt, da ich mein bisheriges System in dem Fall parallel weiterführen müsste.



Abschließend noch eine Frage zur Perspektive: Ist eine steuerliche Auswertung auf mittel- bis langfristige Sicht vorgesehen?



Ich freue mich über eine kurze Rückmeldung zu den genannten Punkten.



Mit freundlichen Grüßen

Jörg Ludwig

Hallo,
beim Testen Ihres Trading Journals ist mir aufgefallen, dass der SPX offenbar nicht gefunden wird.

Könnten Sie mir bitte kurz mitteilen, woran das liegen könnte?



Vielen Dank im Voraus.

 





Christin



mueller-wenzel@mailbox.org



Hallo Larissa,

ich habe über das Youtube Video auf dem ezzy Kanal von euch erfahren. Ich habe mich für die Probeversion angemeldet und sowohl aus meinem Archiv geschlossene Trades und auch aktive Trades eingetragen. Was mir gleich aufgefallen ist, ich kann keine Verluste eintragen, wenn ich z.B. Aktien eingebucht bekommen habe. Oder ich habe es übersehen, wo ich das eintragen kann. Ich übe mich gerade in die Oberfläche ein. 

Dies als kurze Rückmeldung im Probemodus.

Herzliche Grüße

Christin

 



Thomas


thomas.biermann@mail.de

Feedback: Das Journal ist ganz nett, bietet mir aber nicht genug Übersicht. Ich muss zuviel zwischen den Seiten blättern und 
die Sortierfunktion springt immer wieder zurück. Die Strategien-Typen sind begrenzt usw. Letztlich bietet mir das Tool nicht
genug Mehrwert ggü einem selbst eingerichteten Excel-sheet, so dass ich mich entschieden habe, es nicht weiter zu nutzen.





Ulrich



fischer.ulrich@me.com

Hallo Larissa,

das Tool ist gut. Ich selbst werde es noch nicht nutzen. Wenn es nur um die Information geht, die Euer Tool sehr schoen darstellt, reicht mir mein Google sheets basierendes System. Was mir bei MindTrajour fehlt ist die Moeglichkeit Gewinne oder Verluste durch zugeteilte Aktien einzubeziehen, egal ob real oder Buch. 

Schoen waere auch eine Moeglichkeit die Trades direkt vom Broker in das Tool herunterzuladen. Sicher werdet Ihr das Tool weiter entwickeln und wird dann in Zukunft interessant werden fuer mich.

Viel Erfolg,

Ulrich





Roland



email + interview



Roland Interview 10.2. : https://fathom.video/share/FnS835yCVRV_7usj2QfuEKP2eVrbozc9





Roland



rolandgrupe@yahoo.com

Hallo,

ich habe ein Interview im Ezzy Kanal auf Youtube zu eurem Produkt gesehen und bin sehr interessiert es zu testen.

Im Video konnte ich aber nicht erkennen und auf der Webseite auch nichts dazu finden, ob ihr euch direkt mit Broker-Accounts verbinden könnt um die Trades zu synchronisieren.

Und falls nein, ob es einen Import im csv, xml oder json Format gibt.

Bei vielen Trades ist ein manuelles Eingeben recht aufwändig.

Für eine kurze Auskunft wäre ich danbar.

Gruß,

Roland Grupe





Hallo Larissa,

danke für die Antwort und schade, dass ein Import noch nicht möglich ist.

Aktuell habe ich meist so zwischen 1 und 10 Trades pro Tag. Das lässt sich manuell noch managen ist aber auf Dauer lästig.

Eine Zeit lange habe ich 0DTE Trades gemacht, da geht das gar.

Zur Zeit analysiere ich hauptsächlich via Excel, weshalb mich ja die tägliche Eingabe so nervt 😊

Da ich einen technischen Background habe, überlege ich selber was zu programmieren, aber das dauert.

Und da ich sonst noch kein passendes kommerzielles Angebot, insbesondere zum Option-Tracking, gefunden habe, war ich so begeistert von dem Beitrag zu Mindtrajour.

Grundsätzlich suche ich nach einigen wenigen Hauptfunktionen, die vermutlich recht gängig sind.

Neben einem automatisierten Import ist das ein smartes Gruppieren von Trades in Gruppen und Strategien.

Anzeige der noch laufenden offenen Trades mit Risikoanalyse.

Auswertung P&L der geschlossenen Trades nach Strategie und Zeit (Woche, Monat).

Im Idealfall noch eine Schätzung der Steuer aus Optionsgewinnen nach Jahr.

Wenn das ganze dann noch hübsch aussieht, wäre ich glücklich Emoji

Beste Grüße,

Roland


Hi Larissa,

das hört sich sehr spannend an, da können wir uns gern mal austauschen, ob wir da was machen wollen.

Da ich sowohl technisch interessiert bin und an der Börse unterwegs, würde mich das sehr reizen.

Ob ich als Programmierer unterstützen kann weiß ich nicht, da ich von Haus aus mehr aus der Datenbank / -verarbeitung komme (Daten einlesen liegt mir also 😊) und nur nebenbei/privat ein wenig Python programmiere.

Aber zumindest als eine Art Beta-Tester / Friendly User oder auch nur mal zum Austausch könnte es passen.

Wenn es passt, lass uns gern mal sprechen. Außer Montags bin ich zeitlich flexibel.

Schönen Abend,

Roland



Meeting Summary: 

1. Native Support for Wheel Strategy (Core Use Case)

Provide first-class support for the “Wheel” options strategy

Track the full lifecycle: Cash-Secured Put → Assignment → Covered Call → Exit.

Combine option premiums and stock P&L into one unified performance view.

Treat the Wheel as one strategy, not disconnected individual trades.



2. Multi-Strategy Support (Beyond Wheel)

Add native support for additional option strategies

Examples mentioned:

Strangle strategy

Commodity options (e.g. Gold, Silver)

Strategy templates should define:

Trade structure

Required legs

Strategy-level analytics



3. Unified Tracking of Options + Underlying Asset

Track options and underlying stock positions in a single dashboard

Combine:

Option premium income

Stock gains / losses from assignments

Enables realistic profitability analysis for strategies like the Wheel.



4. Simplified Trade Logging vs. Excel

Reduce friction compared to Excel-based trade tracking

Eliminate:

Manual data imports

Spreadsheet maintenance

Error-prone calculations

Focus on fast, structured trade entry optimized for options traders.



5. Strategy-Level Performance Analytics

Provide analytics focused on strategy performance

Identify which strategies are:

Consistently profitable

Low drawdown

High probability

Supports users who trade a small set of repeatable core strategies.



6. Risk-Focused Trade Evaluation

Emphasize risk and loss avoidance in performance metrics

Reflect the mindset of probability-based options traders.

Metrics could include:

Max loss vs. realized loss

Win rate

Drawdown per strategy

Helps users avoid large losses rather than chase maximum returns.



7. Beginner-to-Intermediate Options Trader Onboarding

Improve onboarding for users transitioning from learning to consistency

Roland represents users who:

Lost money during the learning phase

Now rely on a few proven strategies

Tool should support:

Reflection

Strategy validation

Confidence building through data



8. Beta Feedback Loop & Continuous Improvement

Enable structured beta user feedback

Support early users in:

Logging trades

Submitting feedback

Influencing feature priorities

Reinforces product-market fit through real trader workflows.



Jennifer PJM 



Jennifer PJM Feedback 10.2. : https://fathom.video/share/xQ1sWm5Hkm-48GLqCvi1xsoSR6MX7MFw



1. Rename “Margin” Field to “Max Risk”

Rename the “Margin” field to “Max Risk”

Avoids confusion with broker-specific margin requirements.

Better reflects the trader’s actual maximum loss exposure.

Aligns with professional risk-based decision-making.



2. Custom Strategy Builder for Multi-Leg Trades

Introduce a custom strategy builder

Allow users to define and save their own multi-leg option strategies.

Examples mentioned:

Butterflies

Jade Lizards

Other non-standard combinations

Strategy builder should support:

Variable number of legs

Custom payoff logic

Strategy-level analytics



3. Automated Broker Trade Import (Optional / Community-Driven)

Enable automated trade imports from brokers

High demand from the trading community for convenience.

Example broker mentioned: Interactive Brokers / TWS.

Should be optional to preserve:

Manual journaling

Reflection and learning workflows

Potential hybrid model:

Auto-import + manual confirmation/enrichment.





Andreas



andreasgruber@me.com

Hallo Larissa,

Ich würde gerne noch ein bisschen weiter testen und möchte dir danach alle meine Erfahrungen gesammelt übermitteln.

Jetzt gerade stehe ich vor eine kleinen Problem; ein „Butterfly" lässt sich nicht auswählen. Vielleicht könnt ihr diesen noch ergänzen ;-)

Danke

liebe Grüße Andreas aus Wien

Ps.. mein Cousin ist auch Programmierer und ich muss seine Sachen auch immer test, also sei gespannt ...





Wolf



w.menzel@u-mog.com

Hallo Larissa,

ich teste gerade Euer schönes Tool. Bei der Eingabe abgeschlossener Trades finde ich ad hoc keine Möglichkeit den Trade mit angedienten Aktien zu schließen - habe ich was übersehen?

Gibt es ein Handbuch?




Liebe Grüße

    Wolf Menzel

Hallo Larissa,

danke für Deine Antwort. Wann glaubt ihr dieses Feature implementiert zu haben? 

Es ist für mich persönlich sehr wichtig, da angediente Aktien ja eine direkt Folge des Short-Puts sind und diese wiederum als Basis für nachfolgende Covered Calls dienen.




Mit freundlichen Grüßen

Wolf





Marcus


hertzsch@wolfsburg.de



Hallo Larissa,
vielen Dank für deine Anfrage.
Grundsätzlich ist mein Eindruck der App gut und sicher auch wertvoll für
mich.
Da ich derzeit ein kostenlose Lifetime Version nutze kann ich mir kein
Bild von der Entwicklung der App machen.
Mein Eindruck ist aber schon so, das ich eingeschränkt in der Auswahl
der Strategien bin.
Leider kann ich auf der Website auch nicht erkennen, inwieweit ein
kostenpflichtige Abo für mich sinnvoll ist.
Du kannst mir die Vollversion gern zum testen zur Verfügung stellen,
damit ich eine Entscheidung für mich finde

LG Marcus





Ilona



elgerilona@gmail.com



Hallo liebe Larissa,

dankeschön für Deine Nachfrage.

Als erste Erfahrungen kann ich berichten, dass ich schnell und ohne große Anstrengungen meine
Echtgeld-Trades aus diesem Jahr im Trading Journal erfassen konnte.
Es sind zwar nicht sehr viele Trades, aber alles ging nahezu selbsterklärend  und  ist konform mit meinem bisherigen Excel-Trading-Journal und vor allem auch mit dem
Kontoauszug von IB/ CapTrader

Das Video von Ezzy.io  zwischen David und Dir habe ich erst danach gesehen, es ist ein wirklich gutes
Interview 🙂

Einige Anmerkungen/ Fragen habe ich bisher:

1.
Ich habe  lange nach dem Ticker SPX gesucht und die Frage dann Pietro Oliva bei 1SF gestellt.
Vielleicht wäre es für Andere auch hilfreich, seinen Hinweis  auf Eurer Seite zu finden ( falls ich es nicht einfach  nur übersehen habe)


-          ^SPX, ^SPY es kommt ein ^davor.  Bei Future zb. CLUSD oder GCUSD. Es werden die Ticker von Yahoo Finance verwendet.



2.
 Wie kann man erstellte Notizen zu den einzelnen Trades ändern, ergänzen  und/ oder löschen ? Kann man Links und PDFs einfügen ( z.B. Screenshots aus
TradingView ? Und kann man das Notizfenster vergrößern - z.B. wenn man dann gespeicherte Screenshots anschauen möchte ?

3. 
Kann man ganze Trades löschen ?

4. 
Ich nehme an, wenn man ein Abo eingeht, dann kann man Echtgeldkonto und Paperkonto getrennt nebeneinander führen.
Die Option "Neues Konto erstellen" ist wahrscheinlich nur in der Testphase noch nicht verfügbar.
Das ist dann Euer "Multi-Account" - richtig ?

Ich bin dabei, mich mit  für mich neuen Strategien vertraut zu machen bzw. die Vertical Power Strategie ( aus dem Buch von Thomas Mangold)  weiter zu üben.
Und ich habe gerade begonnen, die OptionsApp incl. der  darüber angebotenen 0DTE Brakeout Strategie zu lernen und möchte sie demnächst probieren.
 ->  das alles erst einmal längere Zeit  im PaperTrading.  Zwar meine ich, dass es in einem Video von OptionsApp hieß, dass man dann  ggf. kein gesondertes TradingJournal mehr benötigt, 
aber da ich noch nichts über OptionsApp gehandelt habe, kann ich das noch gar nicht einschätzen.

5.
Für mich wäre noch interessant, Gruppierungen innerhalb eines Accounts  vornehmen zu können - also, wenn verschiedene Trades  gedanklich im Zusammenhang stehen.
Z.B.  Hedgen des Depots mit Long Puts auf den SPX und zugleich eine Gegenfinanzierung der Kosten mittels verschiedener Optionskombos vorzunehmen.
 ( die Strategie des "Zero Hedge"  von Thomas Mangold/ Tradehelden)
Also wenn man sehen könnte,  wie sich verschiedene Trades aus einem Account ( die in einem gedanklichen Kontext stehen)  im Profit/ Loss  insgesamt darstellen.


Ich habe mit Sicherheit noch nicht alle Möglichkeiten entdeckt, die Mindtrajour bietet - es genügt gern einfach ein Hinweis, wo ich dazu weiter lesen kann.
Vielen lieben Dank !

Herzliche Grüße
Ilona Elger





nicole.eggert78@gmail.com



Hallo Larissa,

ich habe gerade Dein Interview mit David gesehen und direkt unter dem Video kommentiert. Da deine Mailadresse kurz eingeblendet war, war ich mal so frei, den direkten Weg zu wählen – ich hoffe, das ist okay für dich!

Dein Angebot „ezzy50“ habe ich direkt genutzt und freue mich darauf, das Tool nun auf Herz und Nieren zu testen. 



Da du im Interview erwähnt hast, dass ihr euch über Feedback freut, juckt es mir als Product Owner im IT-Umfeld (Schwerpunkt MS Power Platform, Architektur, Governance, Requirements Engineering) natürlich direkt in den Fingern.

Ich begleite täglich die Implementierung von Anforderungen im Scrum-Kontext und habe beim ersten Reinschauen direkt ein paar Impulse für eure Roadmap mitgenommen:

Community & Networking: Eine Plattform für „Trading Buddies“, um den Austausch über Trades und Software-Kniffe direkt im Ökosystem zu fördern.

Strukturiertes Feedback-Management: Anstelle von losen Mails könnte ein integriertes Board (mit Kategorien wie Dashboard, Export etc.) helfen. Wenn User Features voten können, hättet ihr die Priorisierung quasi direkt aus der Community validiert – und wir Kunden fühlen uns als Teil der Reise.

„Shadow Trading“-Log: Davids Idee fand ich super. Ein Bereich für Trades, die man doch nicht eingegangen ist, um das Learning (und die verpasste Chance) ohne echtes Risiko zu dokumentieren.

Ich finde es extrem spannend, was ihr da aufbaut. Da ich beruflich tief in der Anforderungsanalyse stecke, unterstütze ich euch gerne auch mal mit detailliertem Feedback oder einem tieferen Blick aus der PO-Perspektive auf die Usability, falls ihr mal einen Sparringspartner zum Testen braucht.

Ich freue mich darauf, zu sehen, wie sich Mind Trajour weiterentwickelt!

Beste Grüße

Nicole



Future feature Ideas for MindTrajour

Community & Trading Buddies

Integrated networking feature for traders

Exchange about trades, strategies, and software tips directly within the platform

Strengthens user engagement and peer learning

Structured Feedback & Feature Voting

Centralized, integrated feedback board (e.g. Dashboard, Export, Performance, UX)

Users can submit feature requests and vote on them

Community-validated prioritization for the product roadmap

Shadow Trading Log (Non-Executed Trades)

Documentation of trades that were intentionally not taken

Focus on learnings and missed opportunities without financial risk

Extends the trading journal with a psychological learning component