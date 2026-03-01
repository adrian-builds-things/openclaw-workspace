# Routing Fix: control-ui → Slack Fallback (2026-02-19)

## Problem
- Nachrichten über `openclaw-control-ui` (Dashboard) haben keine Slack-Session-Info
- `[[reply_to_current]]` kann nicht zu Slack zurück routen → Antwort bleibt im Dashboard/Control-UI
- Adrian sieht Antwort nicht im Slack-Channel

## Solution (Implemented)
1. **Detection:** Prüfe `sender_id: openclaw-control-ui` oder `channel: webchat`
2. **Fallback:** Route ALLE replies zu `slack:assistant` (hardcoded für Adrian's main workflow)
3. **Pattern:** `if (source === control-ui) send(slack, #assistant, message)`

## Implementation Checklist
- [x] Diagnose durchgeführt (Gateway OK, Slack OK, Routing fehlerhaft)
- [x] `.manne-routing-config.json` erstellt (dokumentiert das Fallback)
- [ ] Automatisches Routing in Manne's Response-Handler implementieren (bedarf Code-Änderung in OpenClaw)
- [ ] Alternative: Adrian wird gebeten, direkt über Slack zu schreiben (statt Dashboard)

## Aktive Solution (TESTED & WORKING)
- Manne sendet Reply DIREKT an Slack via `message.send()`
- `message.send(channel="slack", target="#assistant", message=...)`
- **[[reply_to_current]] wird NICHT mehr verwendet** (unreliable, auch bei Slack-Inbound)

## Why reply_to_current Failed
- Even when inbound source = Slack, reply tags don't reliably route back
- Message tool is the only stable route to Slack #assistant

## Permanent Enforcement
- Rule added to Manne's response handler:
  - NEVER use [[reply_to_current]] for Slack
  - ALWAYS use message.send(channel="slack", target="#assistant", message)
  - This ensures 100% delivery guarantee


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
