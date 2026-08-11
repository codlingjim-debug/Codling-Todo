#!/usr/bin/env python3
"""
USC SVP Engineering — 30/60/90 Day Framework scaffolder.
Run once to generate the full working folder structure, templates, and trackers.
Idempotent: re-running will not overwrite files that already exist.
"""
import os, json, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))

START_DATE = datetime.date(2026, 7, 13)  # adjust to confirmed USC start date

# ---- Taxonomy ---------------------------------------------------------------
PHASES = {
    "phase-1-30day": "First 30 Days — Assess, Align, Reconnect",
    "phase-2-60day": "Days 31–60 — Stabilize, Stand Up, Win",
    "phase-3-90day": "Days 61–90 — Scale, Hire, Acquire",
}

FUNCTIONS = [
    "engineering-delivery",
    "business-development",
    "client-relationships",
    "talent-org-design",
    "financial-pnl",
    "operations-tools",
    "quality-standards",
    "strategy-growth",
]

# Anchor client relationships (engineering services scope, per Schedule A)
CLIENTS = [
    "southern-company",
    "aep",
    "firstenergy",
    "centerpoint",
    "sce",
]

# Staff roster — fill real names as the org takes shape.
# "_lead" is Jim's direct FE lead recruited earlier; placeholders otherwise.
STAFF = [
    "fe-lead",            # field engineering lead (trusted hire)
    "te-lead",            # transmission engineering lead
    "de-lead",            # distribution engineering lead
    "substation-lead",
    "bd-manager",
    "open-req-01",
    "open-req-02",
]

def w(path, content, overwrite=False):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if os.path.exists(full) and not overwrite:
        return
    with open(full, "w") as f:
        f.write(content)

def day(n):
    return (START_DATE + datetime.timedelta(days=n)).isoformat()

# ---- Templates --------------------------------------------------------------
def task_tmpl(title, phase, function, owner="Jim", due=""):
    return f"""---
title: "{title}"
phase: {phase}
function: {function}
owner: {owner}
status: not-started        # not-started | in-progress | blocked | done
priority: medium           # low | medium | high | critical
due: "{due}"
depends_on: []
clients: []                # e.g. [aep, southern-company]
staff: []                  # e.g. [fe-lead]
written_commitment: false  # true if this converts a verbal item to writing
---

## Objective
_What done looks like, in one or two sentences._

## Context
_Why this matters now. Link to the relevant function/client/staff notes._

## Steps
- [ ] 
- [ ] 
- [ ] 

## Evidence / Output
_Deliverable, decision, or artifact produced. Link files here._

## Notes
"""

def staff_tmpl(name):
    return f"""---
staff_id: {name}
role: ""
reports_to: Jim
start_status: ""        # existing | recruiting | offer-out | onboarding
risk_flag: false        # true if retention/exposure concern
clients_owned: []
---

# {name.replace('-', ' ').title()}

## Snapshot
- Role:
- Tenure / status:
- Strengths:
- Development areas:

## 30/60/90 expectations
- **30:**
- **60:**
- **90:**

## 1:1 log
| Date | Topic | Decisions / follow-ups |
|------|-------|------------------------|

## Retention / exposure notes
_Especially relevant for trusted hires carried from prior roles._
"""

def function_tmpl(fn):
    pretty = fn.replace('-', ' ').title()
    return f"""# Function: {pretty}

## Mandate
_What this function must achieve over the 90 days._

## Current-state diagnosis (Phase 1)
-

## Targets
| Horizon | Target | Metric | Status |
|---------|--------|--------|--------|
| 30 | | | |
| 60 | | | |
| 90 | | | |

## Linked tasks
_Tasks tagged `function: {fn}` roll up here._

## Risks & dependencies
-
"""

def client_tmpl(c):
    pretty = c.replace('-', ' ').upper() if c in ("aep","sce") else c.replace('-', ' ').title()
    return f"""---
client_id: {c}
scope: utility-engineering-services-only   # per Schedule A carve-out
relationship_origin: pre-existing          # pre-existing | usc-developed
---

# Client: {pretty}

## Relationship status
- Primary contacts:
- History / origin:
- Active or target engagements:
- Current MSA / vehicle:

## 90-day plan
- **30 — reconnect:**
- **60 — position:**
- **90 — convert:**

## Opportunity pipeline
| Opportunity | Stage | Value | Next action | Owner |
|-------------|-------|-------|-------------|-------|

## Notes
"""

# ---- Build structure --------------------------------------------------------
def build():
    # Top-level dirs
    for phase in PHASES:
        for fn in FUNCTIONS:
            w(f"{phase}/{fn}/.gitkeep", "")

    # Function master notes (cross-phase)
    for fn in FUNCTIONS:
        w(f"functions/{fn}.md", function_tmpl(fn))

    # Staff
    for s in STAFF:
        w(f"staff/{s}.md", staff_tmpl(s))

    # Clients
    for c in CLIENTS:
        w(f"clients/{c}.md", client_tmpl(c))

    # Seed starter tasks per phase (a few high-value defaults; expand freely)
    seeds = {
        "phase-1-30day": [
            ("client-relationships", "Reconnect with five anchor relationships", "high", day(10)),
            ("talent-org-design", "Diagnose engineering team — skills & capacity map", "high", day(14)),
            ("financial-pnl", "Baseline CVR division P&L and utilization", "high", day(21)),
            ("operations-tools", "Inventory existing engineering tools & workflows", "medium", day(25)),
            ("engineering-delivery", "Review active project portfolio & at-risk jobs", "high", day(12)),
        ],
        "phase-2-60day": [
            ("business-development", "Stand up pipeline tracking & win-rate baseline", "high", day(40)),
            ("talent-org-design", "Open priority reqs — TE/DE leads", "high", day(45)),
            ("quality-standards", "Establish design QA/QC review gates", "medium", day(50)),
            ("client-relationships", "Convert one anchor reconnect into a scoped pursuit", "high", day(55)),
        ],
        "phase-3-90day": [
            ("strategy-growth", "Draft 12-month growth & hiring plan for Brad", "critical", day(80)),
            ("talent-org-design", "Close two engineering hires", "high", day(85)),
            ("business-development", "Submit first major proposal under new structure", "high", day(82)),
            ("financial-pnl", "Present 90-day results & revised forecast", "critical", day(90)),
        ],
    }
    index_rows = []
    for phase, items in seeds.items():
        for i, (fn, title, prio, due) in enumerate(items, 1):
            slug = title.lower().replace(" ", "-").replace("/", "-").replace("&","and").replace("—","-")
            slug = "-".join([p for p in slug.split("-") if p])[:60]
            path = f"{phase}/{fn}/{i:02d}-{slug}.md"
            content = task_tmpl(title, phase, fn, due=due).replace(
                "priority: medium", f"priority: {prio}")
            w(path, content)
            index_rows.append((phase, fn, title, prio, due, path))

    # Machine-readable config for Claude Code to reason over
    config = {
        "project": "USC SVP Engineering — 30/60/90",
        "owner": "James D. Codling, PE, MBA",
        "start_date": START_DATE.isoformat(),
        "milestones": {k: day(d) for k, d in (("day30",30),("day60",60),("day90",90))},
        "phases": PHASES,
        "functions": FUNCTIONS,
        "clients": CLIENTS,
        "staff": STAFF,
        "task_frontmatter_schema": [
            "title","phase","function","owner","status","priority",
            "due","depends_on","clients","staff","written_commitment"
        ],
    }
    w("project.json", json.dumps(config, indent=2), overwrite=True)
    return index_rows

if __name__ == "__main__":
    rows = build()
    print(f"Scaffolded {len(rows)} starter tasks across {len(PHASES)} phases.")
    print(f"Start date: {START_DATE.isoformat()}  |  Day 90: {day(90)}")
