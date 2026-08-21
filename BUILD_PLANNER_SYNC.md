# BUILD PROMPT — "Planner Sync" for the USC 30/60/90 Framework

> Paste this whole file into Claude Code from inside the `usc-30-60-90/` project.
> It builds a Python tool that turns this plan into a live Microsoft Planner board
> with a sleek UI and reminders — and it encodes the actual logic of the 30/60/90
> plan so the tool understands the plan, not just the file format.

---

## PART A — THE PLAN LOGIC (embed this; it is the source of truth)

You are operating inside Jim Codling's first-90-days plan as **SVP Engineering at USC /
Hydaker-Wheatlake**, leading the **CVR engineering division**. The strategic arc is
**Rebuild → Hire → Acquire**, executed in three phases.

### Phases & objectives
- **Phase 1 — First 30 Days — "Assess, Align, Reconnect"**
  Objective: establish the mandate, diagnose the team / portfolio / P&L, and personally
  re-anchor the five key client relationships before changing anything. Diagnose before acting.
- **Phase 2 — Days 31–60 — "Stabilize, Stand Up, Win"**
  Objective: stand up pipeline + QA/QC discipline, open priority engineering reqs, and
  convert at least one anchor reconnect into a scoped pursuit.
- **Phase 3 — Days 61–90 — "Scale, Hire, Acquire"**
  Objective: close hires, submit the first major proposal under the new structure, and
  deliver a 12-month growth/hiring plan plus 90-day results to Brad (COO).

### The eight functions (every task belongs to one)
engineering-delivery, business-development, client-relationships, talent-org-design,
financial-pnl, operations-tools, quality-standards, strategy-growth.

### The five anchor relationships (engineering services ONLY — Schedule A scope)
Southern Company, AEP, FirstEnergy, CenterPoint, SCE. These are pre-existing relationships
Jim brings. ALL activity stays within the utility-engineering-services carve-out and OUT of
USC's labor / construction / materials lines. Each client has a 30/60/90 motion:
**30 reconnect → 60 position → 90 convert.**

### Operating principles the tool must reinforce
1. **Verbal → Written.** Any task flagged `written_commitment: true` is a verbal understanding
   that must be converted to a signed/written artifact. These are first-class: surface them,
   flag them ⚑, and never let them sit silent.
2. **Diagnose before acting** — Phase 1 assessment tasks gate Phase 2 build tasks.
3. **Retention exposure** — staff carry a `risk_flag`; the trusted FE lead carried from a prior
   role gets special care. Note exposure, don't create it.
4. **Evidence, not activity** — every task resolves to a real deliverable/decision.
5. **Milestone discipline** — Day 30, 60, 90 are hard checkpoints, each with a review deliverable.

### Seed task model (generate these into Planner, mapped to buckets)
Phase 1: reconnect five anchors (high); diagnose engineering team skills/capacity (high);
baseline CVR division P&L + utilization (high); review active portfolio & at-risk jobs (high);
inventory engineering tools & workflows (medium).
Phase 2: stand up pipeline + win-rate baseline (high); open TE/DE lead reqs (high); establish
design QA/QC review gates (medium); convert one anchor reconnect into a scoped pursuit (high).
Phase 3: draft 12-month growth & hiring plan for Brad (critical); submit first major proposal
(high); close two engineering hires (high); present 90-day results & revised forecast (critical).
Read the live task files for the authoritative list; the above is the intended shape.

---

## PART B — WHAT TO BUILD

A standalone Python app that reads this repo's task files and syncs them **directly into
Microsoft Planner** via Microsoft Graph, presented through a sleek local web UI, with
reminders to Jim. Two-way status read-back is a plus.

### Source data
Tasks are markdown files under `phase-1-30day/ phase-2-60day/ phase-3-90day/` with YAML
frontmatter: title, phase, function, owner, status, priority, due, depends_on, clients,
staff, written_commitment. `project.json` holds the taxonomy. `CLAUDE.md` explains structure.
**Start by reading project.json and one sample task file to confirm the schema.**

### Tech / architecture
- Python 3.11+. FastAPI backend + single-page UI served locally (HTML/CSS/JS, no heavy
  framework). Uvicorn to run. Also expose `python -m planner_sync --dry-run` as a CLI path.
- Microsoft Graph for Planner. Auth via **MSAL**, Authorization Code flow with **PKCE**,
  opening the system browser. Disk token cache (encrypt at rest if practical). No hardcoded secrets.
- Graph scopes: `Tasks.ReadWrite`, `Group.ReadWrite.All` (Planner plans live in M365 Groups),
  `User.Read`, `offline_access`. Document these in the README.
- Config via `.env`: TENANT_ID, CLIENT_ID, (CLIENT_SECRET only for a confidential client),
  PLAN_ID or GROUP_ID, REDIRECT_URI, **ANTHROPIC_API_KEY, ANTHROPIC_MODEL** (default
  `claude-sonnet-4-6`). Ship `.env.example` with blanks — Jim adds real USC credentials and his
  Anthropic key when they land.

### Mapping rules (use Part A logic)
- Each phase → a Planner **bucket** ("First 30 Days", "Days 31–60", "Days 61–90").
  Create buckets if missing, in order.
- Task frontmatter → Planner task:
  - title → title; due → dueDateTime
  - priority low/medium/high/critical → Planner priority 9/5/3/1
  - status not-started/in-progress/blocked/done → percentComplete 0/50/0/100; apply a
    "blocked" category when blocked
  - function, clients, staff → Planner labels/categories where possible, else into the
    task description/notes
  - `written_commitment: true` → add a "⚑ Verbal→Written" label and pin in the UI
  - For anchor-client tasks, include the 30/60/90 client motion (reconnect/position/convert)
    in the task notes.
- **Idempotency:** write the created Planner taskId back into the markdown frontmatter as
  `planner_id`, so re-syncs UPDATE not duplicate. Match on planner_id, then title-within-bucket.

### Reminders
Planner's native reminders are weak, so default to **Microsoft To Do** (same Graph API/tenant)
linked tasks with `reminderDateTime` — this is what actually nudges Jim. Default: 9:00 AM local,
2 days before due (configurable per task in the UI). Provide an **.ics** per-task fallback if the
tenant restricts To Do. Additionally, create three **milestone reminders** at Day 30 / 60 / 90
for the phase review deliverables.

### UI (genuinely sleek — not a default form)
- Dark, modern, high-contrast. Deep slate background, one restrained accent color, generous
  spacing, real type scale, subtle card elevation, smooth status pills.
- Layout: phase sections → buckets → task cards. Each card: title, due + countdown, priority
  chip, status pill, function tag, client/staff chips, ⚑ flag for written-commitment items.
- Top bar: "Sync to Planner" button, auth status indicator, last-sync timestamp, dry-run toggle.
- Filter row: by phase / function / status / commitments-only / anchor-client.
- Live sync log panel (created/updated/skipped + errors surfaced clearly).
- A "Verbal→Written" panel that lists all open written-commitment items prominently.

### "Ask Claude" — natural-language task editing (the plan is a moving target)
Add an **Ask Claude** panel to the UI: a text box where Jim types plain-English requests to
add, modify, complete, reschedule, or re-prioritize tasks, and the tool turns them into
concrete changes to the markdown task files AND queues a Planner sync. Examples it must handle:
- "Add a high-priority client-relationships task to reconnect with AEP's T&D VP by next Friday."
- "Mark the CVR P&L baseline done and push the tools inventory task to day 30."
- "Create a Phase 2 hiring task for a substation lead, flag it verbal→written, due Aug 25."
- "Move everything blocked into Phase 2 and show me what's now overdue."

Implementation:
- New module `ask_claude.py` calling the **Anthropic Messages API** (model
  `claude-sonnet-4-6`, or read `ANTHROPIC_MODEL` from .env). Read `ANTHROPIC_API_KEY`
  from .env; ship it blank in `.env.example`.
- Build the system prompt FROM `plan_logic.py` so Claude knows the phases, the eight
  functions, the five anchor clients (engineering-services scope only), the frontmatter
  schema, and the operating principles. Pass the current task list (titles, ids, phase,
  function, status, due) as context each call so edits are grounded in real tasks.
- **Require structured output:** instruct the model to return ONLY JSON describing an
  array of operations, e.g.
  `{"operations":[{"action":"create|update|complete|reschedule|reprioritize|move",
  "target_planner_id_or_title":"...","fields":{...},"reason":"..."}]}`.
  Parse, validate against the schema, and reject anything that invents a function/phase/
  client outside the taxonomy or pushes anchor-client work outside engineering scope.
- **Confirmation step, not blind apply:** render the proposed operations as a diff card
  ("will create X in Phase 2 / will mark Y done / will move Z") with Apply and Discard
  buttons. Nothing writes to files or Planner until Jim clicks Apply. Honor the existing
  dry-run toggle here too.
- On Apply: write the markdown changes via `markdown_io.py`, then run the normal idempotent
  Planner sync (creating buckets/labels/reminders as needed) and write back any new
  `planner_id`s. Log every operation in the sync log panel.
- Guardrails: if a request is ambiguous, the model should ask a clarifying question (surface
  it in the panel) rather than guess; if a request would delete a task, require an extra
  explicit confirm. Never let Claude fabricate a planner_id — only the sync layer assigns those.

### Robustness
- Handle Graph throttling (429) with backoff; refresh expired tokens silently, re-prompt
  sign-in only when needed.
- Friendly errors when credentials are missing OR when the tenant blocks third-party app
  registration / admin consent (USC IT may restrict `Group.ReadWrite.All` — detect and explain).
- Runs locally; nothing leaves the machine except Graph API calls.

### Deliverables
- `planner_sync/` package: `app.py` (FastAPI), `graph_client.py`, `todo_reminders.py`,
  `markdown_io.py` (frontmatter read/write incl. planner_id), `plan_logic.py` (encodes the
  Part A phase/function/client/commitment rules), `ask_claude.py` (natural-language task
  editing via the Anthropic API, returns validated JSON operations), `config.py`.
- `static/` with `index.html`, `styles.css`, `app.js`.
- `requirements.txt`, `.env.example`, `README.md` covering: Azure app registration steps, the
  Graph scopes, how to find PLAN_ID/GROUP_ID, how to run (uvicorn), and the USC-tenant
  admin-consent caveat.

### Build order
1. Read `project.json` + one task file; confirm schema.
2. Scaffold the package.
3. Build `graph_client.py` auth FIRST; prove a token round-trip with a `whoami` endpoint
   before wiring sync.
4. Implement `plan_logic.py` (Part A rules) and `markdown_io.py`.
5. Wire sync (buckets → tasks → planner_id write-back) with a working `--dry-run`.
6. Add To Do reminders + milestone reminders.
7. Add the `ask_claude.py` natural-language layer with the JSON-operations contract and the
   Apply/Discard confirmation flow.
8. Build the UI last, against the working API — including the Ask Claude panel and its diff card.
