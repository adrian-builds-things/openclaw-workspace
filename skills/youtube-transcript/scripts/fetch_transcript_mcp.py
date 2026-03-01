#!/usr/bin/env python3
"""
Fetch YouTube transcript via MCP-server-youtube-transcript.
This bypasses IP blocking by using the MCP server's implementation (Android client emulation).
"""

import sys
import json
import subprocess
import os

MCP_PATH = os.path.expanduser("~/.openclaw/workspace/mcp-server-youtube-transcript")

def extract_video_id(url_or_id):
    """Extract video ID from URL or return as-is."""
    import re
    patterns = [
        r"(?:v=|/v/|youtu\.be/|/embed/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$"
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id

def fetch_via_mcp(video_id, lang='en'):
    """Execute the MCP server logic via node."""
    js_code = f"""
    import {{ getSubtitles }} from './dist/youtube-fetcher.js';
    try {{
        const result = await getSubtitles({{ videoID: '{video_id}', lang: '{lang}' }});
        console.log(JSON.stringify(result));
    }} catch (e) {{
        console.error(JSON.stringify({{ error: e.message }}));
        process.exit(1);
    }}
    """
    
    try:
        result = subprocess.run(
            ["node", "--input-type=module", "-e", js_code],
            cwd=MCP_PATH,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode != 0:
            err_msg = result.stderr.strip()
            try:
                return json.loads(err_msg)
            except:
                return {"error": err_msg or "Unknown node error"}
        
        return json.loads(result.stdout)
    except Exception as e:
        return {"error": str(e)}

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: fetch_transcript.py <video_id_or_url> [language]"}))
        sys.exit(1)
    
    video_input = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else "en"
    
    video_id = extract_video_id(video_input)
    
    data = fetch_via_mcp(video_id, lang)
    
    if "error" in data:
        print(json.dumps(data))
        sys.exit(1)
    
    # Map MCP output to the structure expected by youtube-transcript skill
    # MCP returns: { metadata: { title, author, ... }, lines: [ { text, start, duration } ], actualLang }
    
    metadata = data.get("metadata", {})
    lines = data.get("lines", [])
    full_text = " ".join([l.get("text", "") for l in lines])
    
    output = {
        "video_id": video_id,
        "title": metadata.get("title", "Unknown"),
        "author": metadata.get("author", "Unknown"),
        "language": data.get("actualLang", lang),
        "entries": len(lines),
        "full_text": full_text,
        "transcript": lines
    }
    
    print(json.dumps(output))

if __name__ == "__main__":
    main()
