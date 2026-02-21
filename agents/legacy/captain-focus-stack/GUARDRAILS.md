# Guardrails v1 (Bots, Repos, Deploy)

## 1) Autonomiegrenzen

### Ohne Freigabe erlaubt
- Recherche, Analysen, Entwürfe, lokale Implementierung
- Arbeit in lokalen Repos/Branches
- Interne Doku und Ticketpflege

### Mit Freigabe erforderlich
- Externe Kommunikation (E-Mail/DM/Post) -> Adrian sendet selbst
- Merge auf produktive/geschützte Branches in MTJ/BC
- Deploy auf produktive Umgebungen in MTJ/BC
- Preis-/Angebotsänderungen

## 2) Repo-/Deploy-Regeln nach Kontext

### Eigene Bot-Tools/Experimente
- Freie Bahn für Build/Merge/Deploy erlaubt
- Trotzdem: grundlegende QA vor Release

### MindTrajour + Bite Club
- Bots dürfen lokal entwickeln und konkrete Vorschläge machen
- Niemals pushen ohne explizite Freigabe
- Niemals selbst in produktive Umgebungen deployen

## 3) GitHub-Zugriffskonzept (ohne Adrian-Account-Zugriff)

Ziel: Bot hat aktuelle Codebase, aber keinen Zugriff auf Adrians persönlichen Account.

Empfohlene Varianten:
1. Read-only Mirror per Deploy Key/PAT (nur Lesen)
2. Snapshot-Artefakte via CI (nur Lesen)
3. Optional Fork-Flow ohne Org-Schreibrechte

## 4) QA-Gates vor "Done"
- Technisch: Build/Test/Smoke OK
- Tracking: Events/Properties geprüft (falls relevant)
- Copy/UX/SEO Grundchecks erfüllt (falls relevant)
- Risiken/Fallback dokumentiert

## 5) Compliance für Outbound
- Keine erfundenen Fakten
- Kein automatischer Versand
- Personalisierung nur aus nachvollziehbaren Signalen
