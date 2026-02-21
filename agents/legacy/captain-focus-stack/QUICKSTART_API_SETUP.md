# Quickstart: Nur noch API-Setup

## 1) Voraussetzungen
- Syncthing Sync ist aktiv für alle `.md` im Workspace.
- Agent-Dateien liegen unter `agents/definitions/`.
- Policies liegen unter `agents/MODEL_ROUTING.md` und `agents/GUARDRAILS.md`.

## 2) API-Provider setzen
Richte in deinem OpenClaw-Setup die gewünschten Provider ein:
- Anthropic (für Opus-Tasks)
- OpenAI/Codex (für Coding)
- Gemini (für Research)

## 3) Agenten starten
Nutze die Definitionen in `agents/definitions/*.md`.
Jeder Agent hat:
- klare Rolle
- Tool-Scopes
- Output-Format
- Guardrail-Hinweise

## 4) Betriebsregel (wichtig)
- Externe Nachrichten werden **nie automatisch gesendet**.
- Für MTJ/BC: lokal arbeiten, Vorschläge liefern, nicht pushen/deployen ohne Freigabe.
- Eigene Bot-Tools: freier (gemäß `GUARDRAILS.md`).

## 5) Empfohlener Start (Tag 1)
1. Käptn Fokus priorisiert 5 Tickets.
2. Forge zieht 2 technische Tickets.
3. Echo + Scout erstellen Go-To-Market Material.
4. Pulse definiert Tracking/KPI je Ticket.
5. Atlas plant Tages-Timeboxes mit Adrian.
