# Prep: MindTrajour PostHog Analytics Setup (2026-02-25)

## 🎯 Ziel
PostHog vollständig aufsetzen, um den Google Tag Manager (GTM) zu ersetzen. Fokus: Revenue Tracking & Pageviews.

## 📝 Aufgabenherkunft
- **Fathom-Transkript:** `2026-02-22__team-sprint-planning-mindtrajour.md`
- **User-Update:** PostHog ersetzt GTM komplett.

## 🛠️ Vorarbeit & Ressourcen
- **PostHog Docs:** `https://posthog.com/docs`
- **Wichtige Events:** `pageview`, `signup_success`, `subscription_created`.
- **Known Issue:** Stripe-Webhooks vs. PostHog Destination Sources Connectivity (Analyse steht aus).

## 💡 Vorbereitung (Manne):
- Ich bereite morgen das Snippet für die `layout.tsx` (Next.js App Router) vor, falls noch nicht implementiert.
- Wir checken die Stripe-Integration in den PostHog-Einstellungen (Data Pipeline).
