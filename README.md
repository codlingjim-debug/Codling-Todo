# USC SVP Engineering — 30/60/90 Day Framework

A file-based execution system for the first 90 days leading the CVR engineering division
at USC / Hydaker-Wheatlake. Designed to be driven from Claude Code.

## Quick start
```bash
python scaffold.py     # generate / extend the structure (safe to re-run)
python status.py       # see where everything stands
```
Open `CLAUDE.md` first if you're Claude Code — it explains how to operate here.

## How it's organized
Tasks are indexed three ways at once — **by phase**, **by function**, and **by staff/client** —
through frontmatter tags, so one task shows up in every relevant view without duplication.

- `phase-1-30day/`, `phase-2-60day/`, `phase-3-90day/` → tasks grouped by function
- `functions/` → master note per function (mandate, targets, risks)
- `staff/` → per-person expectations, 1:1 logs, retention flags
- `clients/` → per-anchor-relationship plans (engineering-services scope only)
- `project.json` → machine-readable config
- `status.py` → rollup dashboard

## Customize before you start
1. Set the real start date in `scaffold.py` (`START_DATE`) and re-run.
2. Replace placeholder staff IDs in `STAFF` with real names; re-run `scaffold.py`.
3. Fill in the `functions/*.md` diagnosis sections during week one.
4. Flag any verbal terms as `written_commitment: true` so they get chased.

## Anchor clients
Southern Company, AEP, FirstEnergy, CenterPoint, SCE — utility **engineering services only**,
consistent with the Schedule A carve-out. Keep activity inside that scope.
