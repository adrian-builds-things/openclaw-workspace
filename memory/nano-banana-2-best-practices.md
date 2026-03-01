# Nano Banana 2 – Best Practices (Gemini)

Erstellt: 2026-03-01
Kontext: Auswertung einer weitergeleiteten E-Mail („🍌 Banana.“)

## Quelle
- Ursprung: Substack-Post von Ruben Hassid, Titel „🍌 Banana. / How to set up the new Nano Banana 2 from Gemini"
- Link (aus der Mail): https://open.substack.com/pub/ruben/p/banana-2-3bd
- E-Mail-Metadaten:
  - Gmail Message ID: `19ca865c12be7b61`
  - Datum: 2026-03-01 07:55 (UTC, laut Gmail-Ausgabe)
  - Betreff: `Fwd: 🍌 Banana.`

## Kernaussagen aus der Quelle
- Zugriff in Gemini:
  1. `gemini.google.com` öffnen
  2. In `Tools` auf `🍌 Create image`
  3. `Thinking`-Modell nutzen
- Vom Autor genannte Stärken von Nano Banana 2:
  - Sehr gute fotorealistische Bildgenerierung
  - Character/Style-Konsistenz über mehrere Bilder
  - Upscaling bis 2k/4k
  - Bessere/lesbare Texte in Bildern (Poster, Mockups, Infografiken)

## Praktische Prompt-Patterns (destilliert)
1. **Gezielte Bild-Edits**
   - Muster: `Change [X] on [position] with [Y].`
2. **Infografik aus Artikel/URL**
   - Muster: `Make an infographic of this article (ratio 4:5): [link]`
3. **Upscaling**
   - Muster: `Upscale this image to 2k/4k.`
4. **Farbänderung**
   - Muster: `Change the color of [X] to [Y].`
5. **Style-Transfer**
   - Muster: `Change the style into [X].`
6. **Blur → Sharp**
   - Muster: `Transform this blurred photo into an ultra-sharp realistic editorial shot without changing composition or objects.`
7. **LinkedIn/Headshot-Variante**
   - Muster: `Generate a corporate headshot of my image in the style of reference image 2 (don’t copy the second face).`

## Best-Practice-Workflow (für Adrian)
1. Immer mit **Thinking-Modell** starten.
2. Erst **1 klares Ziel pro Prompt** (z. B. nur Farbe ändern), dann iterativ verfeinern.
3. Für reproduzierbare Ergebnisse:
   - Motiv + Stil + Komposition explizit benennen
   - Bei Referenzen klar sagen, was übernommen werden soll und was nicht
4. Bei Text im Bild:
   - explizit `readable text`, `high legibility`, gewünschte Sprache/Schrift nennen
5. Bei Qualitätszielen:
   - erst Basisbild erzeugen, danach separater Upscale-Schritt (2k/4k)
6. Für Corporate/Marketing-Assets:
   - Format direkt nennen (`1:1`, `4:5`, `16:9`) + Kanal (`LinkedIn post`, `ad creative`)

## Hinweis zur Verlässlichkeit
- Die Quelle ist ein Newsletter-Beitrag (Praxis-Guide), kein offizielles Google-Release-Dokument.
- Für kritische Workflows ggf. gegen offizielle Gemini-Doku gegenprüfen.
