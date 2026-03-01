---
name: youtube-summarizer
description: Automatically fetch YouTube video transcripts, generate structured summaries, and send full transcripts to messaging platforms. Detects YouTube URLs and provides metadata, key insights, and downloadable transcripts.
version: 1.1.0
author: abe238
tags: [youtube, transcription, summarization, video]
---

# YouTube Summarizer Skill

Automatically fetch transcripts from YouTube videos, generate structured summaries, and deliver full transcripts to messaging platforms.

## When to Use

Activate this skill when:
- User shares a YouTube URL (youtube.com/watch, youtu.be, youtube.com/shorts)
- User asks to summarize or transcribe a YouTube video
- User requests information about a YouTube video's content

## Dependencies

**Required:** MCP YouTube Transcript server must be installed at:
`~/.openclaw/workspace/mcp-server-youtube-transcript`

## Workflow

### 1. Detect YouTube URL
Extract video ID from these patterns:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`
- Direct video ID: `VIDEO_ID` (11 characters)

### 2. Fetch Transcript
Use the standardized MCP fetcher:
```bash
python3 /home/adrian/.openclaw/workspace/skills/youtube-transcript/scripts/fetch_transcript_mcp.py <VIDEO_ID> [lang]
```

This returns JSON with metadata and full transcript text.

### 3. Generate Summary

Create a structured summary using this template:

```markdown
📹 **Video:** [title]
👤 **Channel:** [author] | 👁️ **Views:** [views] | 📅 **Published:** [date]

**🎯 Main Thesis:**
[1-2 sentence core argument/message]

**💡 Key Insights:**
- [insight 1]
- [insight 2]
- [insight 3]
- [insight 4]
- [insight 5]

**📝 Notable Points:**
- [additional point 1]
- [additional point 2]

**🔑 Takeaway:**
[Practical application or conclusion]
```

### 4. Save Full Transcript

Save the complete transcript to your local memory or a timestamped file in `~/.openclaw/workspace/transcripts/` if persistence is needed.

### 5. Reply with Summary

Send the structured summary as your response to the user.

## Error Handling

- If transcript fetch fails (node error or no captions), inform the user.
- Try `en` as a fallback if the requested language is missing.
