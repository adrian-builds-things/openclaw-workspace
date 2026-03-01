# OpenClaw After-Setup Prompt Pack (Quelle)

- Gespeichert am: 2026-02-17
- Quelle: https://docs.google.com/document/d/e/2PACX-1vR0dKC9l0lJksxzKWopP3nkBT1v-2HCMw_4KWJuUEw5sOcHLGiVv33J9p7cjiz6nq-ai88me85Sg-31/pub

## Verknüpfungen
- Video-Notiz dazu: [[knowledge/video-notes/2026-02-17-openclaw-first-10-things-setup-video|How to Actually Use OpenClaw (First 10 Things to Set Up)]]
- Verwandte Video-Notiz: [[knowledge/video-notes/2026-02-17-openclaw-memory-muscles-reverse-prompting|OpenClaw verbessern (Memory, Muscles, Reverse Prompting)]]
- Übersicht: [[knowledge/video-notes/INDEX|Video-Notizen Index]]

---

OpenClaw After-Setup Prompt Pack
Copy-paste these prompts to your OpenClaw agent to set up everything from the video.
DISCLAIMER: READ EVERY PROMPT BEFORE USING. Depending on your OpenClaw Setup and some of these website’s, yours may or may not be able to actually go into the browser and do it itself. You dont have to use these prompts to get it to do it autonomously, you could also just ask it to guide you how to get the things it needs to get the tools connected. Some of these prompts will make your OpenClaw attempt to do autonomously, and if it can't it will immediately begin guiding you on how to get it what it needs.Any API keys it gets, tell it to save them as Secure ENV’s, then ask it to confirm that it was successful, then tell it “run a security audit”

Also considering getting your openclaw to develop skills and tools to be able to use these tools (apps)  more effectively
====================================
1. CONNECT GROQ WHISPER (Voice Messages)
====================================

- Go to groq.com make an account, generate an api key, give it to your openclaw and say:
Set up Groq Whisper for voice message transcription. Here’s my api key [INSERT KEY HERE]. Make sure you keep this key as a secure ENV.

====================================
2. SET UP SEARXNG (Self-Hosted Search)
====================================
Set up SearXNG on this server so you have access to real-time web search. Install it via Docker, configure it to hit Google, Bing, and DuckDuckGo, and bind it to localhost. Verify it works by running a test search.

====================================
3. CONNECT GOOGLE WORKSPACE (Gmail, Calendar, Drive)
====================================
(Hier enthält das Dokument den vollständigen Schritt-für-Schritt-Flow inkl. OAuth/API-Setup)

====================================
4. CONNECT NOTION (Second Brain & CRM)
====================================
(Hier enthält das Dokument den vollständigen Schritt-für-Schritt-Flow inkl. Integration/CRM-Test)

====================================
5. CONNECT GITHUB + VERCEL (Code & Deployment)
====================================
Set up GitHub and Vercel so you can create repos, push code, and deploy websites. Walk me through creating accounts if I don't have them, generating tokens, and connecting them to OpenClaw. Test it by deploying a simple hello world page.

====================================
6. THE DEEP-DIVE INTERVIEW (Personalization)
====================================
Interview-Prompt zur Profilerstellung für [[USER]].

====================================
7. CHATGPT/CLAUDE HISTORY IMPORT
====================================
Import-Prompt zur Auswertung historischer Chats.

====================================
8. THE USE CASE BRAINSTORM
====================================
Prompt für 20 priorisierte Use Cases.

====================================
9. CREATE YOUR FIRST SKILL
====================================
Prompt zur Skill-Erstellung.

====================================
10. SET UP [[HEARTBEAT]] (Proactive Monitoring)
====================================
Prompt für Heartbeat-Ideen.

====================================
11. CREATE A MORNING BRIEFING CRON JOB
====================================
Prompt für tägliches Briefing.

====================================
12-21
====================================
Weitere Audit-, Automations-, Skill-, Sub-Agent- und Systemoptimierungs-Prompts.

---

Hinweis: Das Originaldokument enthält alle Punkte im vollen Wortlaut. Falls du willst, speichere ich im nächsten Schritt eine 1:1 Vollabschrift als separaten Raw-Export ab.


## Kontext & Navigation
- [[DASHBOARD]]
- [[MEMORY]]
- [[OBSIDIAN_ROUTING]]
