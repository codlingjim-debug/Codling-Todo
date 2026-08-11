#!/usr/bin/env python3
"""
status.py — roll up all task files by phase, function, staff, and client.
No external deps; parses YAML-ish frontmatter directly.
Usage:
  python status.py                 # full dashboard
  python status.py --by function   # group by function
  python status.py --by staff
  python status.py --by client
  python status.py --blocked       # only blocked/at-risk
  python status.py --commitments   # written-commitment items (verbal->written tracker)
"""
import os, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
PHASE_DIRS = ["phase-1-30day", "phase-2-60day", "phase-3-90day"]

def parse_frontmatter(path):
    with open(path) as f:
        text = f.read()
    if not text.startswith("---"):
        return {}
    fm = text.split("---", 2)[1]
    data = {}
    for line in fm.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        # strip trailing inline comments (e.g. "medium   # low | medium | high")
        if "#" in v and not v.startswith('"'):
            v = v.split("#", 1)[0].strip()
        v = v.strip().strip('"')
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            v = [x.strip() for x in inner.split(",")] if inner else []
        data[k] = v
    data["_path"] = os.path.relpath(path, ROOT)
    return data

def load_tasks():
    tasks = []
    for pd in PHASE_DIRS:
        for path in glob.glob(os.path.join(ROOT, pd, "**", "*.md"), recursive=True):
            fm = parse_frontmatter(path)
            if fm.get("title"):
                tasks.append(fm)
    return tasks

ICON = {"done":"✓", "in-progress":"◐", "blocked":"✗", "not-started":"○"}

def line(t):
    return f"  {ICON.get(t.get('status','not-started'),'○')} [{t.get('priority','?'):>8}] {t.get('title','(untitled)')}  ({t.get('due','')})"

def dashboard(tasks):
    by_status = {}
    for t in tasks:
        by_status.setdefault(t.get("status","not-started"), 0)
        by_status[t.get("status","not-started")] += 1
    total = len(tasks)
    done = by_status.get("done",0)
    print(f"\n=== USC 30/60/90 — {done}/{total} complete ===")
    for s in ["critical-first"]:
        pass
    for pd in PHASE_DIRS:
        ptasks = [t for t in tasks if t.get("phase")==pd]
        pdone = sum(1 for t in ptasks if t.get("status")=="done")
        print(f"\n{pd}  ({pdone}/{len(ptasks)})")
        for t in sorted(ptasks, key=lambda x: x.get("due","")):
            print(line(t))

def group_by(tasks, key):
    print(f"\n=== Grouped by {key} ===")
    buckets = {}
    for t in tasks:
        vals = t.get(key) or ["(unassigned)"]
        if isinstance(vals, str): vals = [vals]
        for v in vals:
            buckets.setdefault(v, []).append(t)
    for k in sorted(buckets):
        print(f"\n{k}  ({len(buckets[k])})")
        for t in buckets[k]:
            print(line(t))

def filtered(tasks, pred, label):
    print(f"\n=== {label} ===")
    hits = [t for t in tasks if pred(t)]
    if not hits:
        print("  (none)")
    for t in hits:
        print(line(t) + f"   → {t.get('_path')}")

if __name__ == "__main__":
    tasks = load_tasks()
    args = sys.argv[1:]
    if "--by" in args:
        group_by(tasks, args[args.index("--by")+1])
    elif "--blocked" in args:
        filtered(tasks, lambda t: t.get("status")=="blocked", "Blocked / at-risk")
    elif "--commitments" in args:
        filtered(tasks, lambda t: str(t.get("written_commitment")).lower()=="true",
                 "Written-commitment items (verbal → written)")
    else:
        dashboard(tasks)
