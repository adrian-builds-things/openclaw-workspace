# Skills Governance

## Zweck
Zentrale Regeln, wie Skills im Workspace verwaltet, dokumentiert und genutzt werden.

## Speicherorte
- **Code/Skill-Dateien:** `/skills/<skill-name>/`
- **Install-Log:** `/skills/installed-skills.log.md`
- **Regeln zur Nutzung:** `/skills/USAGE-RULES.md`
- **Dauerhafte Doku/Policies:** `/knowledge-vault/15-skills/`

## Lifecycle
1. Skill installieren
2. Smoke-Test durchführen
3. In `installed-skills.log.md` dokumentieren
4. Optional: kurze Usage-Notiz in Vault ergänzen

## Qualitätsregeln
- Für jede Aufgabe den spezifischsten Skill wählen.
- Bei Multi-Step-Tasks: Skill-Kombination dokumentieren.
- Neue Learnings in Vault dokumentieren, nicht in verstreuten Chats belassen.

## Minimales Skill-Register (aktuelle Cluster)
- Dev/UI: `frontend-design`, `shadcn-ui`, `next-best-practices`, `kpi-dashboard-design`
- Marketing: `seo-audit`, `content-strategy`, `copywriting`, `programmatic-seo`, `page-cro`
- Ops/Automation: `obsidian`, `self-improving-agent`, `verification-before-completion`

## Regel für neue Channels/Flows
Wenn neuer Kanal (z. B. Slack) eingebunden wird:
- Skill-Impact prüfen (welche Skills laufen dort sinnvoll)
- Sicherheitsgrenzen dokumentieren (Allowlist/Policies)
- Test-Playbook in `20-playbooks/` ergänzen
