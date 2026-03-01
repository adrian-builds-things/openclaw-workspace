# Migration Log — 2026-02-16

Zeit: 2026-02-16 UTC

## Durchgeführt
- `plans/knowledge/eu-food-waste-regulatory-note.md` → `knowledge-vault/50-resources/research/eu-food-waste-regulatory-note.md`
- `plans/knowledge/google-calendar-safe-setup.md` → `knowledge-vault/20-playbooks/google-calendar-safe-setup.md`
- `plans/knowledge/obsidian-local-knowledge-bridge.md` → `knowledge-vault/20-playbooks/obsidian-local-knowledge-bridge.md`
- `plans/knowledge/syncthing-obsidian-bridge-setup.md` → `knowledge-vault/20-playbooks/syncthing-obsidian-bridge-setup.md`
- `plans/knowledge/knowledge-management-system-v1.md` → `knowledge-vault/10-domains/knowledge-management-system-v1.md`
- `knowledge-vault/templates/note-template.md` → `knowledge-vault/50-resources/templates/note-template.md`

## Angelegte Ordner
- `knowledge-vault/20-playbooks/`
- `knowledge-vault/50-resources/research/`
- `knowledge-vault/50-resources/templates/`
- `knowledge-vault/60-reports/`

## Hinweise
- Migration bewusst konservativ: nur Knowledge-/Template-Dateien verschoben.
- Keine Änderungen an `tools/`, `skills/`, `plans/biteclub|ops|sales|tax`.

## Phase 2 — Inbox (from-mac) bereinigt
- `00-inbox/from-mac/50-resources/test-sync.md` → `50-resources/research/test-sync.md`
- `00-inbox/from-mac/99-system/INBOX-WORKFLOW.md` → `99-system/inbox-workflow.md`
- `00-inbox/from-mac/99-system/inbox-processing-log.md` → `99-system/inbox-processing-log.md`
- `00-inbox/from-mac/99-system/templates/content-template.md` → `50-resources/templates/content-template.md`
- `00-inbox/from-mac/99-system/templates/decision-template.md` → `50-resources/templates/decision-template.md`
- `00-inbox/from-mac/99-system/templates/note-template.md` → `50-resources/templates/note-template-from-mac.md` (Konflikt mit bestehender Datei vermieden)
- `00-inbox/from-mac/99-system/openclaw-internal/*` → `90-archive/imports/from-mac-openclaw-internal/`
- `00-inbox/from-mac/README.md` → `90-archive/imports/from-mac-openclaw-internal/README-from-mac.md`

Ergebnis: `00-inbox/from-mac/` geleert (leere Ordner entfernt).
