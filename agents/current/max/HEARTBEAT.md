# HEARTBEAT.md - Max (CTO) Background Checks

# Keep this file empty (or with only comments) to skip heartbeat API calls.
# Add tasks below when you want the agent to check something periodically.

## Aktive Checks (alle 4 Stunden)

- Coolify: Beide Apps (MindTrajour + Bite Club) online und healthy?
- n8n: Workflow Fehler in den letzten 4h?
- Supabase: Connection Pool Auslastung normal?

## Eskaliere sofort wenn:
- App-Deployment fehlgeschlagen
- Database Connection Errors
- n8n kritischer Workflow gestoppt
- Security Alert in Logs

## Wöchentlich (Montag früh):
- Dependency Update Check (npm audit)
- Backup Status prüfen
- Performance Metrics Review
