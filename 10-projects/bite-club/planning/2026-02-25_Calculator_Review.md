# Review: Bite Club Savings Calculator (Branch: feature/sc-258/savings-calculator-feature)

## 🎯 Status: Fast fertig (90%)
Die technische Implementierung ist sehr solide. Die Kernlogik, das PDF-Engagement und die Tracking-Events sind vorhanden. Der Fokus liegt jetzt nur noch auf dem Polishing der Übersetzungen und dem finalen Testing.

## 🛠️ Technische Quick-Analysis
- **Branch:** `feature/sc-258/savings-calculator-feature` (ausgecheckt)
- **Repo-Location:** `/home/adrian/.openclaw/workspace/repositories/bite-club`
- **Core-Features:** 
  - Interaktives Formular (shadcn/ui + Lucide Icons)
  - Echtzeit-Berechnung (Annual Loss, Savings Potential)
  - Fortschrittsanzeige (Progress Bar)
  - PDF-Report Generierung (Backend API)
  - Lead-Capture via Supabase Migration (`20260206222022_create_calculator_leads_table.sql`)

## 📝 Review & To-Dos (Morgen 14:00)

### 1. Übersetzungen (The Missing Pieces)
Die meisten DE/EN Übersetzungen in `src/messages/de/calculator.json` sind vorhanden, aber:
- [ ] **PDF-Report:** Die Übersetzungen in `src/features/calculator/pdf/translations.ts` sind hardcoded (separat von `next-intl`). Diese müssen morgen final geprüft werden, da sie direkt im versendeten PDF landen.
- [ ] **Pluralisierung:** In `calculator.json` sind ICU-Message-Formate für `comparison_equipment` und `comparison_salaries` drin. Morgen kurzes Testen, ob diese in der UI korrekt gerendert werden (z.B. "1 Profi-Küchengerät" vs "3 Profi-Küchengeräte").
- [ ] **Validation:** Fehlermeldungen für `meals_max` (1000) und `waste_max` (50%) prüfen – sind diese Limits für DACH-Betriebskantinen realistisch oder zu niedrig?

### 2. UI/UX Polishing
- [ ] **Auto-Modal:** Das E-Mail-Modal öffnet sich nach 3 Sek automatisch (`Calculator.tsx`). Wir sollten morgen prüfen, ob das zu aggressiv ist oder ob ein Scroll-Trigger besser wäre.
- [ ] **Currency Formatting:** Die Utility `src/features/calculator/utils.ts` nutzt `formatCurrency`. Sicherstellen, dass für Locale `de` das Euro-Zeichen am Ende steht (z.B. `1.234 €`).

### 3. Outreach Integration (15:30)
- [ ] Der Calculator hat bereits References auf Blog-Posts zur EU-Richtlinie (`post_1` in `related_resources`). Wir müssen morgen sicherstellen, dass diese Links nicht auf 404s laufen.

## 🇪🇺 Strategische Analyse: EU-Regulation & Benchmarks (Drafting)

### 1. EU Lebensmittelabfall-Ziele (Basis für den "Compliance-Hook")
*   **Die Regulation:** Die Europäische Kommission hat im Juli 2023 einen Gesetzesvorschlag zur Änderung der Abfallrahmenrichtlinie vorgelegt.
*   **Das Ziel:** Mitgliedstaaten müssen bis **31. Dezember 2030** den Lebensmittelabfall in der Gastronomie und Gemeinschaftsverpflegung (Catering, Restaurants, Kantinen) um **30 % pro Kopf** reduzieren (im Vergleich zu 2020).
*   **Rechenweg für den Hook:** 
    *   `Target_2030 = Aktueller_Abfall * 0.7`
    *   `Gap_to_Compliance = Aktueller_Abfall - Target_2030`
    *   **Botschaft:** *"Um die EU-Vorgaben 2030 zu erfüllen, müssen Sie Ihren Abfall von {wastePercentage}% auf {targetPercentage}% reduzieren. Das bedeutet eine zusätzliche Ersparnis von {gapEuro} € pro Jahr."*

### 2. Branchendurchschnitte (Benchmarks)
Unsere aktuellen Werte im Code (`types.ts`) decken sich weitgehend mit Daten des **Thünen-Instituts** und der **BMEL-Strategie**:
*   **Betriebskantinen:** ~20-25% (Code: 22%)
*   **Schulen/Kitas:** ~25-30% (Code: 28%)
*   **Krankenhäuser:** ~15-20% (Code: 18%)
*   **Quelle:** Thünen-Report 2019/2023 zur Lebensmittelverschwendung in Deutschland ("Wider die Verschwendung").

### 3. Vergleichswerte ohne eigene Daten?
Wenn wir noch keine 10.000 eigenen Datensätze haben, nutzen wir **wissenschaftliche Sekundärdaten** als Benchmark-Anker:
*   Wir vergleichen den User-Wert nicht mit "unseren Kunden", sondern mit dem **"nationalen Durchschnitt"** (Thünen-Institut).
*   **Vorteil:** Das wirkt objektiver und weniger wie eine Verkaufsmasche.
*   **Formulierung:** *"Ihr Abfall liegt {deviation}% über dem Durchschnitt deutscher Betriebskantinen (Quelle: BMEL/Thünen-Institut)."*

### 4. CO2-Impact (Der ESG-Hebel)
*   **Faktor:** 1 kg Lebensmittelabfall ≈ **2,5 kg CO2-Äquivalente** (Durchschnittswert für gemischte Kantinenabfälle).
*   **Gewicht-Schätzung:** Falls der User nur "Mahlzeiten" angibt, rechnen wir mit ca. **150g-200g Abfall pro Mahlzeit** (Branchendurchschnitt bei 25% Waste).
*   **Berechnung:** `Annual_CO2_kg = Annual_Waste_kg * 2.5`.

---
*Die oben genannten Punkte habe ich für die Implementierung morgen (14:00) vorbereitet.*
