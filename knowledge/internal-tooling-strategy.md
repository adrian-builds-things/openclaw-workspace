# Learning: Effektives Internal Tooling mit Coding Agents (Claude Code / OpenClaw)

## Kern-Informationen (Source: Towards Data Science / Eivind Kjosbakken)
Der Artikel beschreibt einen Paradigmenwechsel: Durch Coding Agents (wie Claude Code oder Manne/OpenClaw) sinkt die "Build-Bar" für interne Tools massiv. 
- **Früher:** Nur Tools für extrem repetitive/zeitfressende Aufgaben (da Build-Aufwand hoch).
- **Heute:** "Hyper-personalisierte" Tools lohnen sich schon für kleine Bottlenecks, da sie in unter einer Stunde gebaut sind.

### Strategische Prinzipien
1. **Determinismus:** Code ist deterministischer als Menschen. Tools sorgen dafür, dass Prozesse jedes Mal gleich ablaufen.
2. **Generalisierung:** Tools sollten nicht nur das exakte Problem lösen, sondern Varianten davon (mit dem LLM "Plan Mode" diskutieren).
3. **Agent Awareness:** Interne Tools müssen für KI-Agenten sichtbar gemacht werden (Einträge in `AGENTS.md`, `TOOLS.md`, `CLAUDE.md`).
4. **Shared Repositories:** Tools in einem zentralen Repo ablegen, auf das alle Agenten Zugriff haben.

---

## Relevanz & Einsatz für Adrian (Bite Club & MindTrajour)

Basierend auf deinem Profil habe ich folgende Einsatzmöglichkeiten identifiziert:

### 1. Kundenspezifische Sales-Landingpages (MindTrajour)
Der Artikel betont die Fähigkeit, von "0 auf 1" zu kommen. 
- **Einsatz:** Ein Script, das basierend auf den Pain Points eines Leads (z.B. "Excel-Hass") automatisch eine personalisierte Subpage-Struktur oder einen Vergleichs-Draft generiert (Agent-basiert).

### 2. GitHub Review Bot (Speed-Up für Enes & Luis)
Der Autor nutzt einen Bot, der PRs zusammenfasst und auf bekannte Fehler aus der Historie prüft.
- **Einsatz:** Reduziert deine Review-Zeit für Enes (Nottingham) und Luís (Porto). Ein Agent prüft PRs gegen deine "Coding-Standards" in `IDENTITY.md` oder `USER.md` (z.B. shadcn/ui Best Practices), bevor du sie ansiehst.

### 3. Lead-Handling Automatisierung (Bite Club)
Der Artikel nennt "Automatisches Routing" als Beispiel.
- **Einsatz:** Ein Tool, das n8n-Trigger ergänzt, um Leads aus DACH (Konstruktion/Energie) vorzuqualifizieren (Web-Research via Agent), damit du nur noch "warm" telefonieren musst.

### 4. Determinismus bei Deployments (Coolify/Hetzner)
- **Einsatz:** Kleine Scripte, die vor dem Push zu Coolify deine spezifischen Playwright-Tests oder OTel-Configs prüfen, um menschliche Flüchtigkeitsfehler auszuschließen.

---

## Operative Umsetzung (Manne's Job)
Ich werde folgende Punkte in unseren Arbeitsalltag integrieren:
- **`TOOLS.md` Pflege:** Jedes kleine Script, das wir bauen (z.B. Ticker-Search Research), wird dort dokumentiert, damit ich (und andere Sub-Agents) wissen, dass es existiert.
- **Plan-Mode:** Bevor wir etwas bauen, frage ich dich: "Soll ich das generalisierbar machen, damit wir es auch für Bite Club nutzen können?"
- **Cron-Jobs:** Ich werde proaktiver Vorschläge machen, welche manuellen Checks wir in nächtliche Cron-Jobs auslagern können (ähnlich dem Email-Report des Autors).

---
**Quelle:** [Build Effective Internal Tooling with Claude Code](https://towardsdatascience.com/build-effective-internal-tooling-with-claude-code/)
**Datum:** 2026-02-24
