# TOOLS.md - Max (CTO) Local Notes

## Stack Details

### MindTrajour
- **Framework:** Next.js 15 (App Router)
- **DB:** Supabase (PostgreSQL)
- **Auth:** Supabase Auth
- **Styling:** Tailwind CSS
- **Testing:** Playwright (E2E), Vitest (Unit)
- **Observability:** OpenTelemetry → PostHog

### Bite Club
- **Framework:** Next.js 15 (App Router)
- **DB:** Supabase (PostgreSQL)
- **Auth:** Supabase Auth
- **Styling:** Tailwind CSS

## Infrastructure

### Coolify (Hetzner)
- Deployment: Git-triggered via webhook
- Environments: Production, Preview (per PR)
- Logs: `openclaw browser` → Coolify Dashboard

### Supabase
- Migrations: `supabase db push` (lokal testen erst!)
- RLS immer aktivieren
- Indexes: bei >10k Rows reviewen

### n8n
- Self-hosted auf Hetzner
- Workflows: Invoice Processing, Lead Processing, Alert Routing
- API: intern erreichbar

## Häufige Commands

```bash
# Lokal dev
pnpm dev

# Tests
pnpm test          # Unit
pnpm test:e2e      # Playwright

# Deploy (über Coolify)
git push origin main  # auto-deploy

# DB Migration
supabase db diff --file migration_name
supabase db push
```

## Code Style Preferences

- TypeScript strict mode: true
- Keine `any` Types außer Ausnahmen dokumentiert
- Server Components by default, Client Components explizit markieren
- `'use server'` für API actions

## Known Issues / Gotchas

- Supabase RLS: immer aktiviert — vergiss nicht Policies zu setzen
- Next.js 15 App Router: `params` ist jetzt ein Promise
- Coolify: Health checks müssen auf `/api/health` zeigen
