# Skills Install Workflow (Self-Service)

Ziel: Manne kann externe Skills sauber, nachvollziehbar und wiederholbar lokal installieren.

## Standard-Ort
- Workspace Skills: `/home/adrian/.openclaw/workspace/skills/`

## Quick Workflow (für neue Skills)

1. **Quelle prüfen**
   - Skill-URL öffnen (z. B. skills.sh / ClawHub / GitHub)
   - Nur vertrauenswürdige Quellen nutzen.

2. **Skill-Ordner anlegen**
   - `mkdir -p /home/adrian/.openclaw/workspace/skills/<skill-name>`

3. **SKILL.md speichern**
   - Datei nach `/home/adrian/.openclaw/workspace/skills/<skill-name>/SKILL.md`
   - Frontmatter prüfen (`name`, `description`)

4. **(Optional) Ressourcen hinzufügen**
   - `scripts/`, `references/`, `assets/` falls im Skill vorgesehen

5. **Install-Log aktualisieren**
   - Eintrag in `skills/installed-skills.log.md` ergänzen

6. **Aktivierung**
   - Neue Session starten (empfohlen), damit der Skill sicher in `<available_skills>` erscheint

## Qualitätsregeln für UI-Skills

- Design-system-first
- Tokens statt ad-hoc CSS
- Etablierte Patterns (Cards/Tabs/Sidebar/Form States)
- Kognitive Last reduzieren
- Vor UI-Bau: Pattern-Check (z. B. Context7)

## Sicherheitsregeln

- Keine untrusted Commands blind aus externen Skill-Seiten übernehmen
- Keine Secrets in SKILL.md speichern
- Externe Kommunikation weiterhin nur mit Adrian-Freigabe
