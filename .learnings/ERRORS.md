# ERRORS.md – Mistakes & Corrections

## 2026-03-02: Missing Context Before Agent Config Update

**What happened:**
- Adrian sent agent workspace configs to update
- I immediately copied them to `~/.agents/` without checking what already existed
- Never ran `memory_search` to understand the history
- Never verified the existing state before proceeding

**Root cause:**
- Skipped mandatory context-gathering step (memory_search + existing state check)
- Treated "update" as "copy new stuff" instead of "sync with existing"
- Didn't read AGENTS.md which would have clarified the multi-agent setup

**Impact:**
- Worked out fine, but by accident not design
- Could have corrupted existing agent configs if there were conflicts
- Lost credibility on "knowing the workspace"

**Fix:**
For ANY task that touches existing infrastructure (agents, configs, workspaces):
1. `memory_search(<domain>)` — understand what was before
2. List actual state: `ls -la ~/.agents/`, `docker ps`, etc.
3. THEN decide: copy? merge? overwrite? backup?
4. Document what you're changing and why

**Rule:**
- "Update/sync/refresh" tasks = destructive by nature
- Always verify current state first
- Always have a rollback plan (git, backup)
- NEVER assume the state based on requests

---

## Format for next errors
- **What happened:** Observable facts
- **Root cause:** Why did I miss this?
- **Impact:** What went wrong? (or "nothing, lucky")
- **Fix:** Specific action to prevent repeat
- **Rule:** General principle to apply everywhere
