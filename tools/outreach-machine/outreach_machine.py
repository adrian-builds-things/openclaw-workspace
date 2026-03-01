#!/usr/bin/env python3
import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path

FIELDS = [
    "name", "company", "channel", "first_contact_date", "status",
    "last_touch_date", "next_followup_date", "notes"
]

FOLLOWUP_GAPS = {
    "new": 0,
    "contacted": 3,
    "replied": None,
    "qualified": None,
    "won": None,
    "lost": None,
}

def parse_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()

def fmt(d):
    return d.isoformat() if d else ""

def read_rows(path):
    if not path.exists():
        return []
    with path.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write_rows(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

def cmd_init(path):
    if path.exists():
        print(f"Exists: {path}")
        return
    write_rows(path, [])
    print(f"Created: {path}")

def cmd_due(path):
    rows = read_rows(path)
    today = date.today()
    due = []
    for r in rows:
        nfd = r.get("next_followup_date", "").strip()
        status = r.get("status", "").strip() or "new"
        if status in {"won", "lost"}:
            continue
        if nfd:
            try:
                d = parse_date(nfd)
                if d <= today:
                    due.append(r)
            except Exception:
                pass
    if not due:
        print("No follow-ups due today.")
        return
    print(f"Follow-ups due: {len(due)}")
    for r in due:
        print(f"- {r.get('name','?')} | {r.get('company','?')} | {r.get('channel','?')} | status={r.get('status','new')} | due={r.get('next_followup_date','')}")

def cmd_touch(path, name, status, note):
    rows = read_rows(path)
    today = date.today()
    found = False
    for r in rows:
        if r.get("name", "").strip().lower() == name.strip().lower():
            found = True
            if status:
                r["status"] = status
            r["last_touch_date"] = fmt(today)
            gap = FOLLOWUP_GAPS.get(r["status"], None)
            if gap is None:
                r["next_followup_date"] = ""
            else:
                r["next_followup_date"] = fmt(today + timedelta(days=gap))
            if note:
                prev = r.get("notes", "")
                stamp = today.isoformat()
                r["notes"] = (prev + " | " if prev else "") + f"{stamp}: {note}"
            break
    if not found:
        rows.append({
            "name": name,
            "company": "",
            "channel": "",
            "first_contact_date": fmt(today),
            "status": status or "contacted",
            "last_touch_date": fmt(today),
            "next_followup_date": fmt(today + timedelta(days=3)),
            "notes": f"{today.isoformat()}: {note}" if note else ""
        })
    write_rows(path, rows)
    print(f"Updated: {name}")

def main():
    p = argparse.ArgumentParser(description="Outreach Machine")
    sp = p.add_subparsers(dest="cmd", required=True)

    p_init = sp.add_parser("init")
    p_init.add_argument("csv_file")

    p_due = sp.add_parser("due")
    p_due.add_argument("csv_file")

    p_touch = sp.add_parser("touch")
    p_touch.add_argument("csv_file")
    p_touch.add_argument("--name", required=True)
    p_touch.add_argument("--status", default="contacted")
    p_touch.add_argument("--note", default="")

    args = p.parse_args()
    path = Path(args.csv_file)

    if args.cmd == "init":
        cmd_init(path)
    elif args.cmd == "due":
        cmd_due(path)
    elif args.cmd == "touch":
        cmd_touch(path, args.name, args.status, args.note)

if __name__ == "__main__":
    main()
