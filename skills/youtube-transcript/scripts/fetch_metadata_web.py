import sys
import json
import subprocess
import re

def fetch_metadata(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        # Use curl with a generic User-Agent to get the HTML
        result = subprocess.run(
            ["curl", "-s", "-L", "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", url],
            capture_output=True,
            text=True,
            timeout=15
        )
        if result.returncode != 0:
            return {"error": "Curl failed"}
        
        html = result.stdout
        
        # Title: inside <title> tag usually follows pattern "Title - YouTube"
        title_match = re.search(r'<title>(.*?) - YouTube</title>', html)
        if not title_match:
            title_match = re.search(r'<meta name="title" content="([^"]+)">', html)
            
        # Author: sometimes in "owner": {"videoOwnerRenderer": {"title": {"runs": [{"text": "NAME"}]}}}
        author_match = re.search(r'"author":"([^"]+)"', html)
        if not author_match:
            # Fallback for Author in runs
            author_match = re.search(r'"owner":\{"videoOwnerRenderer":\{"title":\{"runs":\[\{"text":"([^"]+)"', html)
            
        date_match = re.search(r'"publishDate":"([^"]+)"', html)
        view_match = re.search(r'"viewCount":"(\d+)"', html)
        
        return {
            "title": title_match.group(1) if title_match else "Unknown",
            "author": author_match.group(1) if author_match else "Unknown",
            "date": date_match.group(1) if date_match else "Unknown",
            "views": view_match.group(1) if view_match else "Unknown"
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No video ID"}))
        sys.exit(1)
    print(json.dumps(fetch_metadata(sys.argv[1])))
