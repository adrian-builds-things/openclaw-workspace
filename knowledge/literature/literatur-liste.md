# Literaturliste

_Zentrale Leseliste mit Status pro Buch._

Quelle (für diese Liste): https://youtube.com/shorts/aA60etii-kQ?si=kUZOWTSoqofo0xOS

## Bücher + Lese-Status (Dataview)

```dataview
TABLE WITHOUT ID
  file.link AS Buch,
  author AS Autor,
  status AS "Lese-Status",
  priority AS Priorität,
  source AS Quelle
FROM "knowledge/literature"
WHERE type = "book"
SORT
  choice(status = "In Arbeit", 0,
    choice(status = "Nicht gestartet", 1,
      choice(status = "Fertig", 2, 3))) ASC,
  file.name ASC
```

## Fallback (ohne Dataview)

- [[knowledge/literature/book-free-to-lead-unleash-your-hidden-leadership-genius|Free to Lead: Unleash Your Hidden Leadership Genius]]
- [[knowledge/literature/book-real-confidence-a-simple-guide-to-go-from-unsure-to-unshakeable|Real Confidence: A Simple Guide to Go from Unsure to Unshakeable]]
- [[knowledge/literature/book-the-5-year-old-ceo-the-power-of-childlike-curiosity-in-leadership|The 5-Year-Old CEO: The Power of Childlike Curiosity in Leadership]]
- [[knowledge/literature/book-the-upside-of-down-a-survivor-s-guide-to-turning-setbacks-into-success|The Upside of Down: A Survivor's Guide to Turning Setbacks into Success]]
- [[knowledge/literature/book-play-a-bigger-game-seven-universal-principles-to-experience-true-fulfillment-and-win-at-li|Play a Bigger Game: Seven Universal Principles to Experience True Fulfillment and Win at Life]]
- [[knowledge/literature/book-community-market-fit-the-blueprint-for-building-unstoppable-communities|Community Market Fit: The Blueprint for Building Unstoppable Communities]]
- [[knowledge/literature/book-you-only-die-once-how-to-make-it-to-the-end-with-no-regrets|You Only Die Once: How to Make It to the End with No Regrets]]
- [[knowledge/literature/book-wild-courage-go-after-what-you-want-and-get-it|Wild Courage: Go After What You Want and Get It]]
- [[knowledge/literature/book-die-gewinnerformel|Die Gewinnerformel]]
- [[knowledge/literature/ali-abdaal-recommendations-2025|Bücher-Liste Ali Abdaal (2025 Update)]]
- [[knowledge/literature/book-influence-cialdini|Influence (Robert Cialdini) – Copy Posse Must-Read]]
- [[knowledge/literature/book-alchemy-sutherland|Alchemy (Rory Sutherland) – Copy Posse Must-Read]]
- [[knowledge/literature/book-made-to-stick-heath|Made to Stick (Chip & Dan Heath) – Copy Posse Must-Read]]
- [[knowledge/literature/book-everybody-writes-handley|Everybody Writes (Ann Handley) – Copy Posse Must-Read]]
- [[knowledge/literature/book-the-war-of-art-pressfield|The War of Art (Steven Pressfield) – Copy Posse Must-Read]]
- [[knowledge/literature/book-identity-marketing-romney|Identity Marketing (Veronica Romney) – Copy Posse Must-Read]]
- [[knowledge/literature/book-breakthrough-advertising-schwartz|Breakthrough Advertising (Eugene Schwartz) – Copy Posse Must-Read]]
- [[knowledge/literature/book-building-a-storybrand-miller|Building a StoryBrand (Donald Miller) – Copy Posse Must-Read]]
- [[knowledge/literature/book-this-is-marketing-godin|This is Marketing (Seth Godin) – Copy Posse Must-Read]]
- [[knowledge/literature/book-ogilvy-on-advertising|Ogilvy on Advertising (David Ogilvy) – Copy Posse Must-Read]]


## Status-Legende
- Nicht gestartet
- In Arbeit
- Fertig
- Abgebrochen

## Kontext & Navigation
- [[DASHBOARD]]
- [[NAVIGATION]]
- [[knowledge/video-notes/INDEX]]