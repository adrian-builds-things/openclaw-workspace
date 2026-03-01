# Voice of Customer — Bite Club

Updated: 2026-02-28 13:23 UTC

## Persona Lens
- Primary lens: canteen operations lead / admin / B2B sponsor

## Extracted Signals (from Key Takeaways)
### 2026-02-13 — Impromptu Google Meet Meeting (id 122206235)
- - Report Fix is Top Priority: The "Company Meal Distribution" report is inaccurate, counting meals instead of people. This blocks fair cost allocation between companies and must be fixed before implementing new policies.
- - New Features Prioritized: After the report fix, the team will build a "cancel tomorrow's meal" feature (with admin control) and a "close canteen" function for holidays.
- - Weekly Planner UI Updated: The new planner UI is ready for release. A proposed "day-by-day" meal-entry workflow will be considered for a future update to avoid delaying the current release.
- - Food Waste Data Needed: Adrian requested food waste reduction stats from Casais to use as marketing proof for the app's landing page.

### 2026-01-18 — Impromptu Google Meet Meeting (id 115118614)
- - Customer Acquisition is the \#1 Priority: The team will shift focus from development to marketing to secure 2–4 new clients.
- - Roles Defined: Adrian will lead marketing (lead magnets, outreach), Enes will lead development (bugs, features), and Luís will lead design/UX cleanup.
- - Technical Foundation: The repo will move to the Mindtreasure org to enable GitHub Actions for E2E tests, unblocking critical refactors like centralizing routes.
- - Branding Refresh: The current logo will be replaced with a new wordmark and icon, with Luís exploring options based on existing proposals.

### 2025-11-28 — Bite Club Multi Canteen and Presentation (id 104897323)
- - Critical Glitches Found: The new Blankenberg canteen revealed bugs: meal orders are lost when workers switch canteens, and soup-only orders are miscounted and block check-ins.
- - Presentation Opportunity: Filipe will present the project to \~1,000 attendees, including senior leadership, to secure buy-in for expansion. Adrian will provide data and help prepare.
- - Food Waste Reduction: The system is successfully cutting food waste, aligning with the new EU directive (30% reduction by 2030). This is a key selling point for the presentation.
- - Admin Tooling: An upcoming admin tool to place orders for workers is a high-priority fix for managing late selections and worker transfers.

### 2025-11-04 — Impromptu Google Meet Meeting (id 98921252)
- - Pricing Proposal: Propose a new €2,000/mo minimum fee, justified by the project's scope expansion and high customization for Kassaj.
- - Distribution Page Redesign: Prioritize a redesign to improve usability on tablets, addressing critical height constraints and making the scan history the primary focus.
- - E2E Testing: Make building end-to-end (E2E) tests a top priority to prevent regressions and ensure features work correctly for all user roles (e.g., admin vs. kitchen).
- - New Business Strategy: Launch a landing page and explore new markets (offshore catering, government subsidies) to diversify revenue and reduce reliance on a single, highly customized client.

### 2025-10-07 — Impromptu Google Meet Meeting (id 92336193)
- - Successfully set up local development environment accessible from mobile devices on same network
- - Created initial UI for manual order lookup by internal user ID
- - Attempted to implement NFC reading but encountered device compatibility issues
- - Discussed potential fallback options like background Android service if Web NFC API not widely supported

### 2025-10-07 — Impromptu Google Meet Meeting (id 92322877)
- - Implement a simple NFC-based check-in system for the canteen, focusing on an easy solution first
- - Use NFC cards with unique IDs to retrieve user meal information for the current day
- - Consider fallback options (QR codes, manual ID input) for devices without NFC support
- - Plan to work together on implementing the NFC feature soon

### 2025-10-07 — Impromptu Google Meet Meeting (id 92269354)
- - NFC card implementation is the top priority for improving canteen efficiency
- - App is providing value but needs refinement; aiming for full implementation by November 1st
- - Potential to expand app usage across other Kazaj locations and even to other companies
- - Adrian invited to Kazaj Christmas party on December 13th for networking and live app demo

### 2025-06-05 — App Prototype Demo (id 66621582)
- - Prototype demonstrates core functionality for workers, chefs, and admins including meal selection, check-ins, menu creation, and reporting
- - Key areas for refinement: menu creation workflow, multi-canteen support, reporting/analytics, and UI/UX improvements
- - Development proposal: free initial build with revenue share model based on food waste savings (e.g. 25-30%)
- - Timeline: Aiming for trial launch on July 21st, with full launch event on July 28th

### 2025-05-28 — Impromptu Google Meet Meeting (id 65023708)
- - Defined core MVP features: worker management, canteen/company management, menu creation, meal selection, and basic reporting
- - Agreed to focus on functionality first, then improve UX and design later
- - Identified issues with theming and color schemes in the current implementation
- - Decided on task division: Adrian to work on menu management and backend, Luís on UI improvements and theming

### 2025-05-25 — Impromptu Google Meet Meeting (id 64566909)
- - Prioritized tasks: menu creation/validation, dish/table/meal search, worker assignment, email confirmation
- - UI focus: avoid pop-ups and complex flows, emphasize mobile readiness and simplicity
- - Database structure needed for meals and assignments; AI consultation planned for optimal UI design
- - Decoupling menu creation from Superbase initially, using JSON objects for flexibility

## Verbatim O-Töne (Transcript-basiert)
- Siehe: `/home/adrian/.openclaw/workspace/voice-of-customer/biteclub-otone.md`
- Diese Datei enthält 20 direkte Zitate mit Speaker + Timestamp + Meeting-ID.

## Calibration Notes
- Extracted Signals oben basieren auf AI summaries.
- Die O-Ton-Datei basiert auf Transcript-Segmenten und ist die bessere Quelle für Persona-Sprache.
