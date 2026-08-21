# CLAUDE.md — Operating Guide for This Project

This is **Jim Codling's 30/60/90 day plan** as SVP Engineering at USC / Hydaker-Wheatlake,
leading the CVR engineering division. Use this file to understand how to work inside the repo.

## What this project is
A living, file-based execution system for the first 90 days. Every commitment, task,
relationship, and hire lives as a markdown file with structured frontmatter so progress
can be rolled up programmatically.

## Structure
```
phase-1-30day/ phase-2-60day/ phase-3-90day/   # tasks, organized by phase then function
  <function>/NN-task-slug.md
functions/      # one master note per function (cross-phase mandate + targets)
staff/          # one file per person — expectations, 1:1 logs, retention flags
clients/        # one file per anchor relationship (engineering-services scope only)
project.json    # machine-readable config (phases, functions, clients, staff, dates)
scaffold.py     # regenerates structure; idempotent, never overwrites existing files
status.py       # rollup dashboard by phase / function / staff / client
```

## The three lenses (how tasks are indexed)
Every task carries frontmatter tagging it to:
- **phase** — 30 / 60 / 90
- **function** — engineering-delivery, business-development, client-relationships,
  talent-org-design, financial-pnl, operations-tools, quality-standards, strategy-growth
- **staff** and **clients** — arrays linking the task to people and accounts

This lets the same task surface in a phase view, a function view, a person's view, or a
client's view without duplication.

## Anchor clients (Schedule A scope)
Southern Company, AEP, FirstEnergy, CenterPoint, SCE — **utility engineering services only**.
These are pre-existing relationships Jim brings; keep all activity within the engineering-services
carve-out and out of USC's labor/construction/materials lines.

## Operating principles to enforce
1. **Verbal → written.** Any task with `written_commitment: true` represents a verbal
   understanding that must be converted to a signed/written artifact. Surface these early and
   chase them. `python status.py --commitments` lists them.
2. **Diagnose before acting.** Phase 1 is assessment; resist standing up new processes before the
   current-state diagnosis files are filled in.
3. **Retention exposure.** Staff files have a `risk_flag`. The trusted FE lead carried from a prior
   role gets special attention — note exposure, don't create it.
4. **Evidence, not activity.** Each task's "Evidence / Output" must point to a real deliverable.

## Common commands
```
python scaffold.py              # add any newly-defined functions/clients/staff safely
python status.py                # full dashboard
python status.py --by function
python status.py --by staff
python status.py --by client
python status.py --blocked
python status.py --commitments
```

## When asked to add a task
Create a file under the right `phase/function/` folder using the existing frontmatter schema
(see `project.json` → `task_frontmatter_schema`). Tag `clients` and `staff` arrays so it rolls up.
Number the file with the next NN prefix in that folder.

## When asked "where do things stand"
Run `status.py` (and the relevant `--by` view), then summarize: what's done, what's blocked,
what's due in the current phase window, and any open written-commitment items.

## Confidentiality
This contains live compensation context, named relationships, and personnel notes. Treat as
confidential. Do not move anchor-client work outside the engineering-services scope.
