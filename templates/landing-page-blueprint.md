# Landing Page Blueprint (PostHog Inspired)

Diese Struktur dient als Vorlage für neue Landing Pages, basierend auf den Best Practices von PostHog und modernen SaaS-Prinzipien.

## 1. Hero Section (Awareness & Hook)
- **H1 Headline:** Klarer Value Prop. Fokus auf das Ergebnis (Result), nicht das Feature. (PostHog-Style: Direkt, fast schon frech, ehrlich).
- **Subheadline:** Wie erreichen wir das? (Process).
- **Primary CTA:** Markante Farbe (z. B. "Get Started - Free").
- **Visual:** Demo-Animation, Produkt-Screenshot oder ein High-Context Bild, das das Problem illustriert.

## 2. Social Proof / Trust Bar
- **Logo-Cloud:** Bekannte Kunden oder Partner.
- **Numbers:** "Used by 10k+ traders" oder "Processing 1M+ orders".

## 3. The "Pain" / The Problem (Context)
- Kurze Sektion: Warum ist der Status Quo schlecht?
- *Beispiel MindTrajour:* "Trading journals are either too complex or too manual."

## 4. Key Features (Solution)
- **Feature Cards (3-4):**
    - Icon / Kleine Illustration.
    - Title.
    - Kurze Beschreibung.
- **Deep Dive (Zick-Zack-Layout):**
    - Text links, Bild rechts (und umgekehrt).
    - Fokus auf Zeitersparnis oder Risikominimierung.

## 5. How it Works (The "Easy" Path)
- 3 einfache Schritte (1. Connect, 2. Analyze, 3. Prosper).
- Reduziert die kognitive Last.

## 6. Social Proof (Wall of Love)
- Testimonials mit echten Namen/Bildern/Links.
- Fokus auf spezifische Erfolge (nicht nur "Good tool").

## 7. Pricing / Transparency
- Klare Ansage: Startet kostenlos oder Preis X.
- Keine versteckten Gebühren (PostHog-Ehrlichkeit).

## 8. Final CTA
- Wiederholung des Primary CTAs am Ende der Seite.

## 9. Footer
- Links zu Docs, Pricing, Kontakt, Imprint.

---

## Umsetzungshinweise (Code & Design)
- **Stack:** Next.js + TailwindCSS + shadcn/ui.
- **Typography:** Klare Hierarchie. Große H1 (Text-5xl oder 6xl).
- **Spacing:** Viel White-Space (Padding-y 24-32). Lassen wir die Elemente atmen.
- **Performance:** Bilder optimiert (Next/Image), hohe PageSpeed Scores für SEO.
- **Mobile First:** Struktur muss auf dem Smartphone perfekt einspaltig fließen.
