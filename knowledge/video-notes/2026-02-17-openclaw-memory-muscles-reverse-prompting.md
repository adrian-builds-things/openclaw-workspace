# Video-Notiz: OpenClaw verbessern (Memory, Muscles, Reverse Prompting)

- **Gespeichert am:** 2026-02-17
- **Video:** https://youtu.be/UTCi_q6iuCM?si=noJzKKt0h_kIoOm1
- **Typ:** Umsetzungs-Playbook / Setup-Optimierung

## Zusammenfassung (vom Nutzer bereitgestellt)

Hier ist eine detaillierte Schritt-für-Schritt-Anleitung, basierend auf dem Video, um Open Claw (ClawdBot) drastisch zu verbessern:

### 1) Das Gedächtnis optimieren (Memory Fix)
Standardmäßig vergisst das System nach einer sogenannten "Memory Compaction" viele Details. Zwei versteckte Einstellungen sollen aktiviert werden.

**Prompt aus dem Video:**
> "Enable memory flush before compaction and session memory search in my Clawdbot config. Set compaction.memoryFlush.enabled to true and set memorySearch.experimental.sessionMemory to true with sources including both memory and sessions. Apply the config changes."

**Effekt laut Zusammenfassung:**
- Merkt sich Details über Kompaktierung hinaus.
- Kann Gesprächsverlauf über Memory + Sessions durchsuchen.

### 2) Die richtigen „Muskeln“ zuweisen (Modell-Optimierung)
- Nicht alles auf einem Hauptmodell laufen lassen.
- Spezialisierte Tools/APIs je nach Aufgabe nutzen.

**Beispiele aus der Zusammenfassung:**
- Gemini API für Websuche
- Grok API für Social-Media-Suche
- Codec CLI für Coding

### 3) Kontext-Dumping & Erwartungsmanagement
- OpenClaw wie Mitarbeiter behandeln, nicht wie Suchmaschine.
- 10-Minuten Brain-Dump: Ziele, Routinen, Projekte, Vorlieben.
- Klare Proaktivitäts-Erwartung setzen (Overnight-Output).

### 4) Reverse Prompting
Regelmäßige Meta-Fragen verwenden, z. B.:
- „Basierend auf meinen Zielen: Welche Aufgaben solltest du jetzt erledigen?“
- „Welche Infos brauchst du, um produktiver zu sein?“

### 5) Eigene Tools bauen lassen
- Coding-Modul aktivieren.
- Interne Tools anfordern (Kanban, Document Viewer, CRM etc.).

## Kern-Philosophie
OpenClaw als „Brain“ + spezialisierte Tools/APIs als „Muscles“ + viel relevanter Kontext + klare Erwartungen = höhere Geschwindigkeit, bessere Qualität und proaktiveres Arbeiten.

## Verknüpfungen
- Übersicht: [[knowledge/video-notes/INDEX|Video-Notizen Index]]
- Verwandtes Setup-Video: [[knowledge/video-notes/2026-02-17-openclaw-first-10-things-setup-video|How to Actually Use OpenClaw (First 10 Things to Set Up)]]
- Zugehörige Quellnotiz: [[knowledge/source-docs/2026-02-17-openclaw-after-setup-prompt-pack|OpenClaw After-Setup Prompt Pack (Quelle)]]

## Update (2026-02-21)
Erneut von Adrian bestätigt/gewünscht, dass diese Anleitung als referenzierbare Standard-Notiz im System geführt wird.

## Hinweis
Diese Notiz ist eine strukturierte Ablage der vom Nutzer gelieferten Zusammenfassung. Konfigurationsänderungen wurden in dieser Ablage **nicht** automatisch ausgeführt.


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
