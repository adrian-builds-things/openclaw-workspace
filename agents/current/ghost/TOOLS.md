# TOOLS.md - Ghost (DevOps) Local Notes

## Coolify

Monitoring via:
- Dashboard: https://[coolify-host]/dashboard
- API: Coolify REST API
- Logs: Container Logs via Dashboard

Health Check Pattern:
```
GET /api/health
Expected: 200 OK, {"status": "ok"}
```

## Hetzner

- Server Monitoring: Hetzner Cloud Console
- SSH: [host alias aus openclaw.json]

## Key Commands

```bash
# Check deployment status
# (via Coolify Dashboard oder API)

# Docker logs
# (via Coolify → Container Logs)

# n8n Status
# curl http://[n8n-host]:5678/healthz

# Supabase Health
# Supabase Dashboard → Health Monitor
```

## Alert Channels

- CRITICAL: Telegram → Adrian direkt
- WARNING: Tages-Log in memory/YYYY-MM-DD.md
- INFO: Weekly Summary

## Bekannte Gotchas

- Coolify: Health checks müssen auf /api/health antworten (200 OK)
- Next.js: Build kann fehlschlagen bei TypeScript Errors — immer Logs prüfen
- Supabase: Connection Pool kann überlaufen bei vielen concurrent requests
