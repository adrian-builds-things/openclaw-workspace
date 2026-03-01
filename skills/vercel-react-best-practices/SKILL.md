---
name: vercel-react-best-practices
description: Apply Vercel React/Next performance best practices across data fetching, bundle size, rendering, and re-render behavior. Use when reviewing or implementing React/Next UI for performance and scalability.
---

# Vercel React Best Practices

Source: https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices

## Priority order
1. Eliminate waterfalls.
2. Reduce bundle size.
3. Optimize server-side performance.
4. Improve client data fetching and re-render behavior.

## Working style
- Prefer parallel async patterns and Suspense-aware structure.
- Avoid heavy imports and unnecessary client serialization.
- Optimize rerender dependencies and derived state usage.
