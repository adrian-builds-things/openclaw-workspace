# MindTrajour — PostHog Funnel & Analytics Plan

**Ziel:** Tracking des kompletten Conversion-Funnels von Awareness bis Activation + Retention für die Low-Touch-SEO-Engine.

---

## 1. Funnel-Stufen (Conversion Path)

```
Landing → Signup → App Login → First Trade Entry → Consistent Usage → Expansion
```

---

## 2. Core Events & Properties

### **Phase 1: Landing & Awareness**

| Event | Wann? | Properties | Quelle | Was sagt es uns? |
|-------|-------|-----------|--------|------------------|
| `page_view` | Nutzer sieht Landing Page | `page`, `utm_source`, `utm_medium`, `utm_campaign`, `referrer` | Frontend (PostHog SDK) | Top-of-Funnel Traffic-Qualität |
| `scroll_depth` | Nutzer scrollt Seite | `percent_scrolled`, `page` | Frontend (Custom Event) | Landing Page Engagement (Qualität) |
| `cta_click` | Click auf „Sign Up" oder „Try Free" | `button_text`, `section`, `button_position` | Frontend | Intent Signal |

**→ Was sagt uns das:** Welche Traffic-Quellen / UTMs bringen beste Nutzer? Wo brauchen wir Copy-Fixes?

---

### **Phase 2: Signup & Onboarding**

| Event | Wann? | Properties | Quelle | Was sagt es uns? |
|-------|-------|-----------|--------|------------------|
| `signup_start` | Nutzer klickt Signup-Form | `form_context`, `utm_source` | Frontend | Intention confirmed |
| `signup_field_filled` | Nutzer füllt Feld | `field_name`, `field_sequence` | Frontend (Optional: nur wen problematisch) | Friction-Punkte identifizieren |
| `signup_complete` | Form submitted, User erstellt | `signup_time_ms`, `plan_selected`, `utm_source` | Backend | Conversion |
| `email_verified` | User verifiziertEmail | `hours_to_verify` | Backend | Activation Intent |
| `first_login` | Nutzer logged sich ein | `days_since_signup`, `device`, `browser` | Backend | Onboarding Completion |

**→ Was sagt uns das:** Wo droppen Nutzer? Welche Traffic-Quellen convertieren best?

---

### **Phase 3: App Activation (First Trade Entry)**

| Event | Wann? | Properties | Quelle | Was sagt es uns? |
|-------|-------|-----------|--------|------------------|
| `app_open` | App gestartet | `device`, `app_version`, `days_since_signup` | Frontend (SDK) | Daily/Weekly Active Users (DAU/WAU) |
| `onboarding_started` | Nutzer startet Setup | `onboarding_step` | Frontend | Ist Nutzer bereit zu verwenden? |
| `onboarding_step_completed` | Step fertig (z. B. „Broker verbunden") | `step_name`, `step_duration_ms` | Frontend | Progress tracking |
| `onboarding_completed` | Vollständig fertig | `total_duration_ms`, `steps_skipped` | Frontend | **AHA-Moment erreicht** |
| `first_trade_entry` | Nutzer erstellt erste Trade | `trade_type`, `instrument`, `entry_price` | Backend | **CRITICAL ACTIVATION EVENT** |
| `trade_entry_form_abandoned` | Nutzer bricht ab | `form_step`, `time_in_form_ms` | Frontend | Friction Points in Core UX |

**→ Was sagt uns das:** Wie lang dauert es bis zur ersten Trade-Entry? Wo braucht Onboarding-Redesign?

---

### **Phase 4: Engagement & Retention**

| Event | Wann? | Properties | Quelle | Was sagt es uns? |
|-------|-------|-----------|--------|------------------|
| `trade_completed` | Trade geschlossen | `profit_loss`, `duration_days`, `instrument` | Backend | User macht Sinn des Tools |
| `trade_analysis_viewed` | Nutzer liest Analyse-Feedback | `analysis_type`, `time_spent_ms` | Frontend | Learning Engagement |
| `journal_entry_added` | Notiz zu Trade hinzugefügt | `entry_type`, `character_count` | Backend | Reflective Use = Stickiness |
| `stats_viewed` | Stats/Dashboard betrachtet | `time_on_stats`, `metrics_viewed` | Frontend | Habit Formation |
| `export_used` | Nutzer exportiert Journal | `format` | Backend | Advanced Usage |

**→ Was sagt uns das:** Welche Nutzer bleiben? Welche Features treiben Retention?

---

### **Phase 5: Expansion (Churn Risk + Upsell)**

| Event | Wann? | Properties | Quelle | Was sagt es uns? |
|-------|-------|-----------|--------|------------------|
| `subscription_checked` | Nutzer schaut Pricing | `days_since_signup`, `current_plan` | Frontend | Consideration Signal |
| `upgrade_click` | Nutzer upgradet | `from_plan`, `to_plan`, `upgrade_reason` | Backend | Revenue Event |
| `inactivity_alert` | >7 Tage keine Nutzung | `days_inactive`, `cohort` | Backend (Cron) | Churn Risk Alert |
| `return_after_inactivity` | Nutzer kommt zurück | `reactivation_campaign` | Backend | Retention Win |
| `premium_feature_used` | Nutzer nutzt Premium-Feature | `feature_name` | Frontend | Value Realization |

**→ Was sagt uns das:** Wer upgradet? Wer churned? Welche Features sind Premium-Gründe?

---

## 3. Funnel Analysis (PostHog Native)

### **Primary Conversion Funnel**
```
Landing → CTA Click → Signup → Email Verified → First Login → Onboarding Complete → First Trade Entry
```

**KPIs:**
- Conversion Rate pro Stufe (%)
- Drop-off Rate & Abandonment Reasons
- Time-to-Conversion (pro Stufe)

### **Secondary Funnels**
1. **Retention Funnel:** First Trade → 2nd Trade → 5th Trade → Monthly Active
2. **Upgrade Funnel:** Free User → Views Pricing → Clicks Upgrade → Payment
3. **SEO Cohort Funnel:** Organic Traffic → Signup → Trade Entry (ist SEO-Traffic anders als Paid?)

---

## 4. Data Sources & Implementation

### **Frontend Events** (PostHog Web SDK)
- Hosted in Next.js App
- SDK initialized on App Load
- Track automatically:
  - `$pageview` (all routes)
  - `$click` (all buttons — filter later)
- Custom events via:
  ```typescript
  posthog.capture("event_name", { property: "value" })
  ```

### **Backend Events** (Server/API)
- From Next.js API Routes or Backend Service
- Use PostHog Node SDK:
  ```javascript
  posthog.capture(userId, "event_name", { property: "value" })
  ```
- Events to trigger:
  - `signup_complete` (when user created in DB)
  - `first_trade_entry` (when trade record inserted)
  - `inactivity_alert` (via nightly cron job)

### **Database Queries** (if not event-driven)
- If trade data comes from API (broker integration), query Supabase:
  - Trades per user
  - Average hold duration
  - Win/Loss ratio
  - Last trade date → **inactivity detection**

---

## 5. Data Quality Standards

### **Validation Rules**
- All `user_id` must be anonymized (use PostHog's native anonymous ID + identified user)
- Timestamp must be UTC
- Properties must match defined schema (no typos)
- Critical events (signup, first_trade) get server-side validation

### **Testing Checklist Before Production**
- [ ] Test events fire on all device types (mobile, desktop)
- [ ] Test anonymous user journey (before signup)
- [ ] Test identified user journey (post-signup)
- [ ] Verify funnels match expected paths
- [ ] Check property cardinality (no unbounded strings)

### **Monitoring**
- PostHog Dashboard: Alert if `first_trade_entry` events drop >20% day-over-day
- Weekly review: Check funnel drop-offs, identify churn cohorts

---

## 6. Immediate Next Steps (Priority Order)

| Priority | Task | Owner | Timeline |
|----------|------|-------|----------|
| **1** | Implement Phase 1 + 2 (Landing → Signup) | Dev | Week 1 |
| **2** | Implement Phase 3 (Activation: First Trade) | Dev | Week 2 |
| **3** | Build Funnel Dashboard in PostHog | Analytics | Week 2 |
| **4** | Add Phase 4 + 5 (Retention + Expansion) | Dev | Week 3 |
| **5** | Set up Alerts + Weekly Reviews | Ops | Week 3 |

---

## 7. Expected Insights (After 2-4 weeks of data)

You'll be able to answer:
- ✅ **Awareness:** Welche Traffic-Quellen sind best? (Organisch vs. Paid vs. Referral)
- ✅ **Conversion:** Wo droppen Nutzer? (Landing → Signup Drop höher als Signup → First Trade?)
- ✅ **Activation:** Wie lang bis zur ersten Trade? (2 Tage? 2 Wochen?)
- ✅ **Retention:** Welche Nutzer sind Sticky? (mehrere Trades, regelmäßig nutzend)
- ✅ **Expansion:** Wer upgradet & warum? (Feature-driven oder Price-driven?)
- ✅ **Cohort Analysis:** Unterscheiden sich Q1-2025 Signups (SEO) von Q1-2026 (Bezahlt)?

---

## Notes

- **PostHog Freeplan:** 1M events/month = ausreichend für aktuelles Volumen
- **Anonym tracking:** Nutzer können sich abmelden → anonym weitertracking (für Privacy)
- **Custom Property Limits:** Halte Property-Liste kurz (maximal 20–30 properties pro Event) um Datenqualität zu sichern
