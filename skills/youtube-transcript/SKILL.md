---
name: youtube-transcript
description: Fetch and summarize YouTube video transcripts. Use when asked to summarize, transcribe, or extract content from YouTube videos. Handles transcript fetching via MCP server (Android emulation) to bypass YouTube's cloud IP blocks.
---

# YouTube Transcript

Fetch transcripts from YouTube videos and optionally summarize them.

## Quick Start

```bash
# Internal tool usage prefers the MCP-based script for stability
python3 scripts/fetch_transcript_mcp.py <video_id_or_url> [language]
```

**Examples:**
```bash
python3 scripts/fetch_transcript_mcp.py dQw4w9WgXcQ
python3 scripts/fetch_transcript_mcp.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
python3 scripts/fetch_transcript_mcp.py dQw4w9WgXcQ "de"
```

**Output:** JSON with `video_id`, `title`, `author`, `full_text`, and timestamped `transcript` array.

## Workflow

1. Run `fetch_transcript_mcp.py` with video ID or URL.
2. The script calls the `mcp-server-youtube-transcript` (installed in the workspace) via Node.js.
3. This bypasses typical cloud IP blocks by using Android client emulation.
4. Returns JSON with full transcript text.
5. Summarize the `full_text` field as needed.

## Language Codes

Default: `en`

Override with second argument: `python3 scripts/fetch_transcript_mcp.py VIDEO_ID "de"`

## Legacy Methods

The script `scripts/fetch_transcript.py` (VPN method) is still present but deprecated in favor of the more stable MCP-based approach.

## Setup & Configuration

- Requires `mcp-server-youtube-transcript` to be installed and built in `~/.openclaw/workspace/mcp-server-youtube-transcript`.
- Python 3 with `requests` library.
