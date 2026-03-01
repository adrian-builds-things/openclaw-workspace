# Learnings

- 2026-02-28: Recurring autonomy works best as two separate cron jobs (brief + done) with strict output schema and explicit delivery channel.
- 2026-02-28: Delegation quality improves when every handoff includes Objective, Context, Definition of Done, and Output format.

## [LRN-20260228-001] best_practice

**Logged**: 2026-02-28T14:01:10Z
**Priority**: high
**Status**: pending
**Area**: ops

### Summary
Anti-Loop Guardrail für Tool-Calls eingeführt, um Hängenbleiben und Antwortlücken zu verhindern.

### Details
Bei Gateway/Exec-Operationen kann ein fehlerhafter Call oder ein unerwartetes Tool-Result zu einer Antwortverzögerung führen. Das führte zu einer wahrgenommenen Funkstille im Chat.

### Suggested Action
Verbindliches Anti-Loop-Protokoll:
1. Max 2 Versuche pro identischer Operation.
2. Wenn Versuch 2 fehlschlägt: sofort Nutzer-Update senden (Status + nächster sicherer Schritt).
3. Danach Fallback nutzen (z. B. `openclaw status` statt wiederholtem Restart).
4. Vor jedem "done" zwingender Verifikationscheck mit 1 unabhängiger Probe.
5. Bei Laufzeit >30s ohne Output: proaktiv kurze Zwischenmeldung an Nutzer.

### Metadata
- Source: user_feedback
- Related Files: /home/adrian/.openclaw/workspace/.learnings/ERRORS.md
- Tags: anti-loop, reliability, communication

---
