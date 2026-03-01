---
name: frontend-design
description: Design and implement production-grade frontend UIs with strong design-system discipline, clear information hierarchy, low cognitive load, and established UX patterns. Use for pages, dashboards, components, and app shells where visual quality, consistency, and usability matter.
---

# Frontend Design

Use this skill to avoid ad-hoc UI work and produce interfaces that feel deliberate, consistent, and high quality.

## Workflow

1. Define the interface goal, user, and primary job-to-be-done.
2. Choose a clear visual direction that matches the context (not generic defaults).
3. Translate the direction into system primitives:
   - typography scale
   - spacing scale
   - color tokens
   - radius, border, shadow tokens
   - interaction states
4. Structure information architecture before styling:
   - overview first
   - progressive disclosure
   - strong section hierarchy
   - predictable navigation
5. Implement with reusable components and tokens (design-system first).
6. Validate with a quick quality pass:
   - readability/scannability
   - contrast/accessibility
   - consistent spacing/alignment
   - reduced cognitive load

## Non-Negotiables

- Avoid one-off "quick CSS" patches when a component/token solution exists.
- Prefer established patterns (cards, tabs, sidebars, table/list, forms, empty/loading/error states).
- Keep dense screens manageable: fewer concurrent decisions, clearer defaults, and grouped actions.
- Make UI states explicit: hover, focus, active, disabled, selected.

## Implementation Guidance

- Use component primitives from the existing UI library first.
- Keep layout composition predictable (shell -> sections -> cards -> controls).
- Use typography and spacing to communicate hierarchy, not decoration.
- Use color intentionally for meaning (status, emphasis), not noise.
- Motion should support orientation and feedback, never distract.

## Done Criteria

A UI change is done only when:

- It follows design tokens and reusable components.
- It reduces, not increases, cognitive load.
- It matches established product patterns.
- It is production-usable and visually coherent.
