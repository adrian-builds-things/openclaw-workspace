# Spec: Public Roadmap & Feature Voting

**Status:** Draft
**Area:** Growth / Product Transparency
**Owner:** TBD
**Last updated:** February 2026

---

## Dependency Map

```
Dependency Map
─────────────────────────────────────────────────────────────────
This spec              Depends on       Enables
─────────────────────────────────────────────────────────────────
Public Roadmap         Supabase         Users understand what is
& Feature Voting       (already set up) being built and why —
                                        reduces "why isn't X
                                        done yet?" support load

                                        Feature suggestions feed
                                        into internal sprint
                                        planning input
```

---

## Problem Statement

Users who invest time learning MindTrajour have no visibility into what is coming next. When a feature they need is missing, they have no way to know whether it is planned, being built, or not on the roadmap at all. This creates two problems: users churn to competitors without knowing the gap would be closed soon, and users who stay feel unheard — they cannot signal which missing features matter most to them.

The current alternative is direct email or the Discord community. Both are low-signal: email generates one-off requests with no aggregation, and Discord feedback is not systematically tracked against development priorities.

---

## What We Are Building

A public-facing page on mindtrajour.com with two components:

**1. Roadmap Board (Kanban)**
A read-only Kanban-style board showing all feature cards the team has entered, organized into four columns:

| Column | Meaning |
|--------|---------|
| Backlog | Planned but not yet scheduled |
| In Vorbereitung | Scoped and scheduled for an upcoming sprint |
| In Progress | Actively being built |
| Done | Shipped — links to changelog entry where applicable |

**2. Feature Suggestion Form**
A simple contact-style form where any visitor can submit a feature idea. Submissions go to the team — they do not appear on the board automatically. The team decides whether to add a suggestion as a votable card.

---

## What Users Can and Cannot Do

| Action | Users | Team (Admin) |
|--------|-------|--------------|
| View the roadmap board | ✅ Yes — no login required | ✅ Yes |
| Upvote a feature card | ✅ Yes — login required (prevents duplicate votes) | ✅ Yes |
| See vote counts on cards | ✅ Yes | ✅ Yes |
| Submit a feature suggestion | ✅ Yes — via form (login optional) | ✅ Yes |
| Create a feature card on the board | ❌ No | ✅ Yes — via admin/Supabase |
| Edit or delete a card | ❌ No | ✅ Yes |
| Move a card between columns | ❌ No | ✅ Yes |

Users **submit suggestions** — they do not place items on the board. The board is team-curated.

---

## User Flows

### Flow 1 — Viewing the Roadmap
1. User visits `/roadmap` on mindtrajour.com
2. Board renders with all four columns and feature cards
3. Each card shows: title, short description, vote count, optional tag (e.g. "options", "import")
4. "Done" column cards optionally link to the corresponding changelog entry
5. No login required to view

### Flow 2 — Upvoting a Feature
1. User sees a feature card they care about
2. User clicks the upvote button on the card
3. If not logged in: prompt to log in / sign up (one-click, same auth as the app)
4. If logged in: vote is recorded, count increments immediately
5. User can remove their vote by clicking again (toggle)
6. One vote per user per feature card

### Flow 3 — Submitting a Feature Suggestion
1. User clicks "Suggest a Feature" button on the roadmap page
2. Form opens (modal or dedicated section): Title (required), Description (optional), Email (optional — pre-filled if logged in)
3. User submits — confirmation message shown ("Thanks, we'll review it!")
4. Submission lands in Supabase `feature_suggestions` table
5. Team reviews periodically and decides whether to promote to a votable card

---

## Data Model (Supabase)

### Table: `roadmap_items`
Stores all feature cards on the board. Managed by the team.

| Column | Type | Description |
|--------|------|-------------|
| `id` | uuid | Primary key |
| `title` | text | Feature card title (shown on board) |
| `description` | text | Short description (1–2 sentences) |
| `status` | enum | `backlog` / `in_progress` / `preparing` / `done` |
| `tags` | text[] | Optional labels (e.g. "options", "analytics", "import") |
| `changelog_url` | text | Link to changelog entry (for Done items, nullable) |
| `created_at` | timestamptz | When created |
| `updated_at` | timestamptz | Last status change |
| `sort_order` | int | Manual ordering within a column |

### Table: `roadmap_votes`
One row per user per roadmap item. Enforces one vote per user.

| Column | Type | Description |
|--------|------|-------------|
| `id` | uuid | Primary key |
| `roadmap_item_id` | uuid | FK → `roadmap_items.id` |
| `user_id` | uuid | FK → `auth.users.id` |
| `created_at` | timestamptz | When voted |

**Constraint:** `UNIQUE (roadmap_item_id, user_id)` — enforces one vote per user per item.

### Table: `feature_suggestions`
Stores user-submitted suggestions. Not shown publicly.

| Column | Type | Description |
|--------|------|-------------|
| `id` | uuid | Primary key |
| `title` | text | Suggestion title (required) |
| `description` | text | Additional detail (optional) |
| `submitted_by_email` | text | Submitter email (optional) |
| `user_id` | uuid | FK → `auth.users.id` if logged in (nullable) |
| `created_at` | timestamptz | Submission time |
| `reviewed` | bool | Whether the team has reviewed it (internal flag) |
| `promoted_to_item_id` | uuid | FK → `roadmap_items.id` if promoted (nullable) |

---

## Vote Count Query

To avoid storing a `vote_count` column that can go stale, vote counts are computed via a Supabase view or aggregation at read time:

```sql
SELECT
  ri.*,
  COUNT(rv.id) AS vote_count
FROM roadmap_items ri
LEFT JOIN roadmap_votes rv ON rv.roadmap_item_id = ri.id
GROUP BY ri.id
ORDER BY ri.status, ri.sort_order;
```

Alternatively, a `vote_count` column can be maintained via a Postgres trigger for performance at scale.

---

## Row-Level Security (Supabase RLS)

| Table | Read | Insert | Update | Delete |
|-------|------|--------|--------|--------|
| `roadmap_items` | Public (anon) | Team only | Team only | Team only |
| `roadmap_votes` | Authenticated | Authenticated (own rows) | ❌ | Authenticated (own rows) |
| `feature_suggestions` | Team only | Public (anon + auth) | Team only | Team only |

---

## Success Criteria

- [ ] Roadmap page accessible at `/roadmap` without login
- [ ] All four columns render correctly with team-entered cards
- [ ] Vote button visible on all cards; login required to vote
- [ ] One vote per user per card enforced at database level (UNIQUE constraint)
- [ ] Vote count displayed on each card and updates without full page reload
- [ ] Feature suggestion form submits to `feature_suggestions` table
- [ ] Suggestion form works for both logged-in and anonymous users
- [ ] Done items link to changelog entries where available
- [ ] Team can manage board items via Supabase (no custom admin UI required for V1)

---

## Out of Scope (V1)

- Custom admin UI for managing roadmap items — team uses Supabase dashboard directly in V1
- Comments on feature cards
- User notifications when a voted feature ships
- Sorting or filtering by tag on the public board (V2)
- Embedding individual roadmap cards in emails or social posts

---

## Open Questions

| Question | Owner |
|----------|-------|
| Where does the roadmap page live — within the app (authenticated area) or on the public marketing site? Affects auth flow for voting. | Adrian |
| Should anonymous (non-logged-in) users be able to vote via email verification, or is login strictly required? | Adrian |
| Should the suggestion form require a Captcha / rate limiting to prevent spam? | Enes |
| Do we want a "notify me when this ships" option on voted cards? Would require storing email + sending a notification when status moves to Done. | Adrian |
| V1 team admin via Supabase dashboard — acceptable for launch, or does the team need a lightweight custom admin UI from day one? | Adrian + Enes |
