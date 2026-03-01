---
title: "OpenClaw Selbst-Optimierungs-Guide (Kosten um bis zu 97% senken)"
date: 2026-02-19
time_utc: "10:37"
source: "slack://channel/C0AFPLGD2L9/message/1771497471.899349"
author: "Adrian"
tags: [openclaw, kostenoptimierung, token-effizienz, qmd, exa, openrouter, ollama, guide]
related:
  - "[[Knowledge Base]]"
  - "[[OpenClaw Optimization]]"
  - "[[QMD Skill]]"
  - "[[Exa MCP]]"
  - "[[Model Routing]]"
  - "[[Heartbeat Setup]]"
  - "[[Ablage-Regeln]]"
---

# Originalnachricht (voller Inhalt)

Hier ist eine strukturierte Anleitung, die du direkt in deinen OpenClaw-Systemprompt kopieren oder dem Agenten als Anweisung geben kannst, um sich selbst zu optimieren.
Ich habe diese Anleitung auch als Notiz für dich gespeichert.

## OpenClaw Selbst-Optimierungs-Guide

**Ziel:** Reduktion der Kosten um bis zu 97 % durch maximale Token-Effizienz.

- **Lokale Wissensextraktion (QMD Skill):**
  - Anweisung: „Verwende für die Recherche in meiner Knowledge-Base den QMD Skill. Lade Dokumente niemals komplett in den Kontext, sondern indexiere sie lokal via BM25/Vector Search und sende mir nur die relevanten Snippets.“
  - Ressource: https://github.com/levineam/qmd-skill

- **Session-Management & Context-Cleaning:**
  - Anweisung: „Wende strikte Session Initialization Rules an. Lade beim Start jeder Sitzung ausschließlich die Dateien [[SOUL]], [[USER]] und [[IDENTITY]]. Lade keine alte Historie oder vorherige Tool-Outputs automatisch. Nutze memory_search() nur bei expliziter Nachfrage.“

- **Kostenlose Websuche (Exa.ai):**
  - Anweisung: „Nutze für Web-Recherchen das Exa.ai MCP. Binde es als Skill ein, um aktuelle Informationen ohne zusätzliche API-Kosten für teure Drittanbieter zu erhalten.“

- **Intelligentes Model-Routing:**
  - Anweisung: „Verwende OpenRouter für das automatische Routing. Delegiere einfache Aufgaben (Syntax-Checks, kurze Fragen) an Sub-$1-Modelle wie Claude Haiku. Reserviere teure Modelle (Opus) ausschließlich für hochkomplexe Logikprobleme.“

- **Lokale Heartbeats via Ollama:**
  - Anweisung: „Führe periodische Heartbeat-Checks über eine lokale Instanz von Ollama (z.B. Llama 3.2 3B) aus. Nutze dafür keine bezahlten API-Credits.“

## Video-Referenz

**I Cut My OpenClaw Costs by 97%**

Das Video von Dubibubii bietet einen 5-Schritte-Leitfaden, um die Kosten für OpenClaw massiv (laut Video um bis zu 97 %) zu senken. Die Strategie basiert darauf, nicht einfach das Modell zu wechseln, sondern die Effizienz bei der Token-Nutzung zu steigern.

Hier sind die praktikablen Schritte und Belege aus dem Video:

### 1. Lokale Suche mit dem "QMD Skill" (95 % Token-Ersparnis)
Anstatt ganze Dokumente in den Prompt zu laden, was extrem viele Token verbraucht, nutzt dieser Skill eine lokale Indexierung (BM25 und Vector Search).
- Schritt: Installiere den QMD Skill von GitHub.
- Effekt: OpenClaw greift nur noch auf relevante Text-Snippets aus deinen Markdown-Dateien zu, anstatt die gesamte Wissensdatenbank zu senden.
- Beleg: Reduziert den Token-Verbrauch für Recherchen um ca. 90-95 %.

### 2. Session-Initialisierungs-Regeln (Kosten senken von $0,40 auf $0,05)
Standardmäßig laden Agenten oft die gesamte Historie (ca. 50 KB pro Nachricht), was pro Sitzung Millionen von Token verschwenden kann.
- Schritt: Füge eine Regel zum System-Prompt deines Agenten hinzu, die festlegt, dass nur essenzielle Dateien (z. B. [[USER]], [[SOUL]]) geladen werden.
- Prompt-Beispiel aus dem Video:
  > "SESSION INITIALIZATION RULE: On every session start: Load ONLY these files: [[SOUL]], [[USER]]... DO NOT auto-load: Session history...".
- Beleg: Die Kontext-Größe sinkt von 50 KB auf 8 KB pro Start.

### 3. Kostenlose Websuche mit Exa.ai
Anstatt teure APIs wie Perplexity (bis zu $270/Monat) für die Websuche zu nutzen, kannst du Exa.ai verwenden.
- Schritt: Gehe zu Exa.ai, aktiviere unter "Extra MCP" die Funktion "Enable all" und kopiere den Link. Sage deinem OpenClaw: "Wrap this MCP up into a skill [Link einfügen]".
- Beleg: Ermöglicht kostenlose Websuche in Echtzeit.

### 4. Automatic Model Routing (Ferraris nicht für den Wocheneinkauf nutzen)
Oft wird für einfache Aufgaben das teuerste Modell (z. B. Claude Opus) verwendet.
- Schritt: Nutze OpenRouter oder Claw Router als Zwischenschicht.
- Funktion: Das System wählt automatisch das günstigste Modell für die jeweilige Aufgabe (z. B. Haiku für Syntax-Checks, Sonnet für mittlere Aufgaben und Opus nur für komplexe Probleme).
- Beleg: Verhindert, dass 80 % der täglichen Anfragen unnötig auf teuren "Heavyweight"-Modellen laufen.

### 5. Heartbeat-Checks auf lokale LLMs umleiten ($0 Kosten)
OpenClaw sendet periodische "Heartbeats", um die Verbindung zu prüfen. Wenn diese über eine bezahlte API laufen, summieren sich die Kosten bei 24/7 Betrieb schnell.
- Schritt: Installiere Ollama lokal (z. B. mit Llama 3.2 3B). Konfiguriere OpenClaw so, dass Heartbeats über Ollama laufen.
- Beleg: Senkt die Kosten für diese rein technischen Abfragen auf $0.

### Zusammenfassung der Ersparnis
Durch die Kombination dieser Schritte konnte der Ersteller seine monatliche Rechnung von über $1.000 auf ca. $36 senken.

Link: https://youtu.be/ZrBvPoFBVUo?si=

## Notiz

Ablage als eigenständige Obsidian-kompatible Knowledge-Base-Datei gemäß Adrians Regel (voller Inhalt statt nur Zusammenfassung).

## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
