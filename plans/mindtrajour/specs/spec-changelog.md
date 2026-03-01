# Spec: Automated Changelog System

**Status:** Implemented
**Area:** Developer Infrastructure / Product Transparency
**Owner:** Adrian
**Last updated:** February 2026

---

## Dependency Map

```
Dependency Map
─────────────────────────────────────────────────────────────────
This spec              Depends on       Enables
─────────────────────────────────────────────────────────────────
Automated             semantic-release  Users understand what
Changelog System      OpenRouter /      changed in each release
                      Claude API        without reading raw
                      next-intl         commit messages
                      TanStack Query
                                        Feeds into Public
                                        Roadmap (Done column
                                        links to changelog
                                        entries)
```

---

## Problem Statement

Every time MindTrajour ships a release, traders who rely on the app have no way of knowing what changed unless they read raw GitHub commit messages — which are written for developers, not users. Feature improvements go unnoticed, bug fixes aren't communicated, and there is no "what's new" moment that builds product excitement.

The gap compounds because MindTrajour targets non-technical users (options traders, not developers). A commit message like `feat(options): add multi-leg trade recording` means nothing to a user. A changelog entry like "You can now record multi-leg strategies in a single trade entry" does.

---

## What We Are Building

A fully automated changelog pipeline with two surfaces:

**1. The Pipeline (backend)** — A `semantic-release` plugin that runs on every release. It reads the commit log, categorizes changes, calls the Claude API to rewrite technical commit messages as user-friendly language (in all configured languages), and writes the result to static JSON files in the repository.

**2. The UI (frontend)** — A set of React components that read those JSON files and display changelog content to users in two places: on the public landing page (a scrollable timeline) and inside the authenticated app (a dedicated `/changelog` route with filtering, read/unread tracking, and a notification toast on first login after a new release).

---

## Architecture Overview

```
On every git push to main:
  semantic-release runs
    → @semantic-release/changelog (standard CHANGELOG.md)
    → [our plugin] prepare()
        → categorizeCommits()     reads commits from context
        → translateWithClaude()   calls OpenRouter / Claude API
        → generateJSON()          writes JSON files to /public/changelogs/
    → @semantic-release/git       commits JSON files + CHANGELOG.md

At runtime (user visits the app or landing page):
  useChangelog hook
    → fetches /public/changelogs/index.json (TanStack Query)
    → reads read/unread state from localStorage
    → provides data to components

Components:
  ChangelogTimeline      → renders vertical list of ChangelogCards
  ChangelogCard          → shows one release (expandable)
  ChangelogBadge         → semver version badge with color
  ChangelogNotification  → toast shown once per new release
  ChangelogFilter        → category filter with URL params
```

---

## Workstream 1 — Configuration and Types

**Files:** `src/lib/changelog/types.ts`, `src/lib/changelog/changelog.config.ts`, `src/lib/changelog/index.ts`

The configuration schema defines how the changelog system behaves for a given project. For MindTrajour, this means specifying the supported languages (German and English), the AI model to use via OpenRouter, and the repository URL for generating links.

```typescript
// changelog.config.ts
export const changelogConfig = {
  languages: ['de', 'en'],
  aiModel: 'claude-3-5-sonnet',  // via OpenRouter
  repositoryUrl: 'https://github.com/mindtrajour/app'
}
```

The changelog data structure uses five fixed categories. These map directly to conventional commit types:

| Category | Emoji | Maps from commit type |
|----------|-------|-----------------------|
| `features` | ✨ | `feat:` commits |
| `bugfixes` | 🐛 | `fix:` commits |
| `performance` | ⚡ | `perf:` commits |
| `security` | 🔒 | commits with security in message or scope |
| `important` | ⚠️ | `BREAKING CHANGE` commits |

Commits with type `build`, `ci`, `docs`, or `test` are filtered out — they are not user-facing.

A Zod schema validates the JSON at runtime before writing to disk and before rendering in the UI.

---

## Workstream 2 — semantic-release Plugin

**Files:** `lib/semantic-release-changelog/index.ts`, `lib/semantic-release-changelog/categorize.ts`, `lib/semantic-release-changelog/translate.ts`, `lib/semantic-release-changelog/generate.ts`

The plugin hooks into the `prepare` phase of semantic-release (after the version number is known, before the git commit). This phase order matters:

```
.releaserc.json plugin order:
  1. @semantic-release/changelog    → writes CHANGELOG.md
  2. ./lib/semantic-release-changelog  → writes /public/changelogs/*.json
  3. @semantic-release/git          → commits both files together
```

### 2a. Commit Categorization

`categorizeCommits()` receives the commit list from the semantic-release context and groups them into the five category arrays. The function returns a structured object that feeds directly into the translation step.

### 2b. Claude API Translation

`translateWithClaude()` calls the Claude API via OpenRouter (the existing codebase pattern — not direct Anthropic API). It sends the categorized commits with a prompt that instructs the model to rewrite each item in plain user language with an informal but professional tone. The response is structured JSON with translations keyed by language code.

The prompt configures tone specifically for MindTrajour: language that a retail options trader would understand, not developer terminology. "Adds multi-leg options entry" becomes "Du kannst jetzt mehrbeinige Strategien wie Iron Condors in einem einzigen Eintrag erfassen."

If the API call fails for any reason, the plugin falls back to the original commit message text rather than blocking the release.

**Environment variable required:** `ANTHROPIC_API_KEY` (set in CI/CD pipeline, not committed to the repository).

### 2c. JSON File Generation

`generateJSON()` produces two files on every release:

**`/public/changelogs/v1.2.3.json`** — One file per version:
```json
{
  "version": "1.2.3",
  "date": "2026-02-15",
  "categories": {
    "features": ["...", "..."],
    "bugfixes": ["..."],
    "performance": [],
    "security": [],
    "important": []
  },
  "translations": {
    "de": { "features": ["..."], "bugfixes": ["..."] },
    "en": { "features": ["..."], "bugfixes": ["..."] }
  }
}
```

**`/public/changelogs/index.json`** — Running list of all versions (newest first), used by the frontend to enumerate releases without fetching every individual file.

Both files are validated against the Zod schema before writing. The plugin stages them so they are committed together with `CHANGELOG.md` in a single release commit.

---

## Workstream 3 — Frontend Data Layer

**File:** `src/features/changelog/hooks/useChangelog.ts`

`useChangelog` is the single data hook that all changelog components consume. It uses TanStack Query to fetch and cache `/public/changelogs/index.json`. It exposes:

| Value | Type | Description |
|-------|------|-------------|
| `changelogs` | `ChangelogEntry[]` | All releases, newest first |
| `latestVersion` | `string` | Version string of the most recent release |
| `isLoading` | `boolean` | True while the first fetch is in progress |
| `error` | `Error \| null` | Null on success |
| `isRead(version)` | `(v: string) => boolean` | Checks localStorage for `changelog_v{version}_seen` |
| `markRead(version)` | `(v: string) => void` | Sets the localStorage key |
| `markAllRead()` | `() => void` | Sets key for all loaded versions |

Read/unread state is stored in `localStorage` so it persists across sessions without requiring a backend call or database write.

---

## Workstream 4 — Frontend Components

**Directory:** `src/features/changelog/components/`

### ChangelogBadge

Displays a version number as a colored badge. Color signals the type of release at a glance:

| Release type | Color | Condition |
|---|---|---|
| Major | Red | `x.0.0` — breaking changes |
| Minor | Blue | `0.x.0` — new features |
| Patch | Green | `0.0.x` — bugfixes only |

Props: `version: string`, `size: 'sm' | 'md' | 'lg'`.

### ChangelogCard

Displays one release as a collapsible card. The collapsed state shows the version badge, release date, and a row of category icons indicating which types of changes are present. Clicking the card expands it to show all items in all non-empty categories.

The expand/collapse animation uses CSS grid transition (not Framer Motion) for performance. The chevron icon rotates 180° on expand.

### ChangelogTimeline

Takes the `changelogs` array from `useChangelog` and renders a vertical timeline. A continuous vertical line connects all cards. Newest releases appear at the top.

Each card fades in as it enters the viewport using an `IntersectionObserver`, which keeps the initial page load performant — only visible cards are animated.

### ChangelogNotification

A toast/modal that appears once after a user logs in and a new version exists that they haven't seen. It shows the version badge, release date, and the top three features from the latest release.

Two actions: **"Show Details"** (navigates to `/changelog`) and **"Dismiss"** (closes the toast and writes `changelog_v{version}_seen` to localStorage). The component is added to `src/app/app/layout.tsx` so it is only shown to authenticated users.

### ChangelogFilter

A filter control on the in-app changelog page. Allows filtering by category (All / Features / Bugfixes / Performance / Security / Important Updates). Filter state is serialized to URL query parameters so filtered views can be shared or bookmarked. Shows an empty state message when no items match the current filter.

---

## Workstream 5 — Integration Points

### Landing Page (`/changelog` section)

A `ChangelogSection` component is embedded in the landing page. It shows the five most recent releases using `ChangelogTimeline`. A "Load More" button fetches additional entries from the already-loaded index. The section is fully internationalised via `next-intl` (German and English).

### In-App Changelog Route (`/app/changelog`)

A dedicated page inside the authenticated app. Shows the full release history (no 5-entry limit). Includes the `ChangelogFilter` component and the "Mark all as read" button. Navigation shows a "What's New" badge if unread versions exist.

---

## Environment Variables

| Variable | Where | Required | Description |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | CI/CD (GitHub Actions / Vercel env) | Yes | Used by the semantic-release plugin at release time. Not needed at runtime. |

The key is only needed during the `semantic-release` run. It is never bundled into the frontend or exposed to users.

---

## Success Criteria

- [x] `changelog.config.ts` defines languages, AI model, and repository URL
- [x] Zod schema validates all changelog JSON at write and read time
- [x] Plugin runs in correct phase: after `@semantic-release/changelog`, before `@semantic-release/git`
- [x] Commits are categorized correctly (feat→features, fix→bugfixes, perf→performance, security, BREAKING→important)
- [x] Build/CI/docs/test commits are excluded from user-facing changelog
- [x] Claude API translation falls back gracefully if the API call fails
- [x] `/public/changelogs/index.json` updated on every release (newest first)
- [x] Version-specific JSON files pass Zod validation before being committed
- [x] `ChangelogBadge` colors correctly for major / minor / patch
- [x] `ChangelogCard` expands and collapses with animation
- [x] `ChangelogTimeline` fade-in on scroll (IntersectionObserver)
- [x] `ChangelogNotification` shown once per new version to authenticated users
- [x] Category filter persists in URL query params
- [x] "Mark all as read" clears the "What's New" badge
- [x] Landing page `/changelog` section loads first 5 releases with Load More
- [x] `ANTHROPIC_API_KEY` added to CI/CD environment (not committed to repo)

---

## Out of Scope (V1)

- User comments on changelog entries
- Email notification when a new version ships
- Rich text / image attachments in changelog entries
- Custom per-category tone in the AI prompt
- Diff view showing what changed in the UI (code-level)
- Changelog RSS feed

---

## Open Questions

| Question | Owner |
|----------|-------|
| Should the landing page `/changelog` section be visible without scrolling on desktop, or is it below the fold intentionally? | Adrian |
| German is primary language — should the AI prompt instruct "du" (informal) or "Sie" (formal) as the default tone? Currently set to informal. | Adrian |
| Should the `ChangelogNotification` modal show on every page load until dismissed, or only on the first page load after login? Currently: first page load only. | Adrian |
| Should the Public Roadmap "Done" column cards link to individual changelog entries (e.g. `/changelog?filter=features#v1.2.3`)? This would close the loop between the roadmap and the changelog. | Adrian |
