# [[HEARTBEAT]] - Ghost (DevOps)

## Alle 4 Stunden

- MindTrajour App: Online? /api/health response OK?
- Bite Club App: Online? /api/health response OK?
- n8n: Läuft? Kritische Workflows aktiv?
- Supabase: Connection Pool normal?

## Täglich

- SSL Zertifikate — Ablaufdatum prüfen (Warnung bei <30 Tage)
- Disk Usage auf Hetzner VPS
- Backup-Status: letztes Backup erfolgreich?

## Wöchentlich

- npm audit auf beiden Projekten
- Dependency Updates prüfen
- Security Headers prüfen

## Eskaliere SOFORT wenn:

🔴 App down (>2 Minuten keine Response)
🔴 Database Connection Error in Production
🔴 SSL Zertifikat expires in <7 Tage
🔴 n8n kritischer Workflow gestoppt
🔴 Ungewöhnliche API-Calls / potentieller Security Breach
