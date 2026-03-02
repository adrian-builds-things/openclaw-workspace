#!/usr/bin/env python3
import asyncio
import json
from pathlib import Path
from crawl4ai import AsyncWebCrawler

URLS = [
    "https://example.com",
    "https://docs.crawl4ai.com/",
]
OUT_DIR = Path("crawl4ai_output")


async def run(urls: list[str]):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    async with AsyncWebCrawler(verbose=False) as crawler:
        for url in urls:
            res = await crawler.arun(url=url)
            item = {
                "url": url,
                "success": res.success,
                "status_code": res.status_code,
                "title": (res.metadata or {}).get("title"),
                "markdown_path": None,
            }

            if res.success:
                safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")
                md_path = OUT_DIR / f"{safe_name}.md"
                md_path.write_text(res.markdown or "", encoding="utf-8")
                item["markdown_path"] = str(md_path)

            results.append(item)

    (OUT_DIR / "summary.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Done. Summary: {OUT_DIR / 'summary.json'}")
    for r in results:
        print(f"- {r['url']} -> success={r['success']} status={r['status_code']} file={r['markdown_path']}")


if __name__ == "__main__":
    asyncio.run(run(URLS))
