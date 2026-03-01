# [[TOOLS]] - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Google Calendar

- **Aufgabenplanung** (Primary for work): `c_1ed5caf4a7972cd8b8b29749656f92c02a4213405280f36a510e22848bede6b7@group.calendar.google.com`

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

### SSH / Tailscale

- OpenClaw Dashboard Tunnel (auf dem Mac ausführen, **nicht** auf dem VPS):
  - `ssh -N -L 18789:127.0.0.1:18789 adrian@100.78.193.125`
- Danach im Browser auf dem Mac öffnen:
  - `http://localhost:18789`
- Gateway-Token im Dashboard per URL-Query setzen (korrekt):
  - `http://localhost:18789/?token=DEIN_TOKEN`
- Für neue Services/Apps mit eigenem Port: Port immer per SSH-Tunnel auf `localhost` vom Mac weiterleiten.
  - Muster: `ssh -N -L <LOKALER_PORT>:127.0.0.1:<REMOTE_PORT> adrian@100.78.193.125`
  - Dann lokal öffnen: `http://localhost:<LOKALER_PORT>`
