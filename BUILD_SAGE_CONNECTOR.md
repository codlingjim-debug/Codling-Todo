# BUILD PROMPT — Sage Connector (PARKED until product is confirmed)

> Do NOT build this yet. Run `sage_discovery.py` first and produce
> `sage_discovery_report.json`. This spec branches on which Sage product USC runs.
> Paste this into Claude Code together with the discovery report once you have it.

## Guiding rule (applies to ALL branches)
**Estimating data is read-mostly.** Never write to Sage Estimating's own tables — a bad
write can corrupt a live bid. If estimate data must drive something, pull it into Jim's
own layer (the 30/60/90 tool / an analysis store) and write THERE. "Read + write" from the
requirements means write to *our* artifacts, not to Sage's estimating source of record.
Any write-back to Sage, if ever justified, goes only through a sanctioned, controlled path
(Sage SDK / Office Connector Write) with explicit per-record confirmation and an audit log.

## First: read `sage_discovery_report.json`
Use the `identification` and any `sql_tables` to pick the branch below. If ambiguous, STOP
and ask Jim to confirm with USC IT rather than guessing a schema.

---

## BRANCH A — Sage Estimating (Timberline)  [most likely for an estimating team]
- No public REST API. Integrate by reading the backing store:
  - **Newer installs:** Microsoft SQL Server. Connect read-only via `pyodbc` with a
    least-privilege, read-only SQL login provided by IT against a replica if possible.
  - **Older installs:** Pervasive PSQL / Btrieve via ODBC DSN.
- Build `sage_estimating_reader.py`:
  - Connect read-only; reflect the estimate schema (headers, cost items, assemblies,
    totals) discovered in the report.
  - Expose typed read functions: `list_estimates()`, `get_estimate(id)`,
    `get_cost_items(estimate_id)`, `get_totals(estimate_id)`.
  - Map nothing back to Sage. Output normalized JSON our tools can consume.
- Integration with the 30/60/90 tool: optional — e.g. surface "active bids" as read-only
  context cards, or let "Ask Claude" reference estimate totals when creating BD tasks.
  Estimate data is *reference*, not a task source it can mutate.

## BRANCH B — Sage Intacct  [only if estimating actually lives in Intacct, unlikely]
- Real Web Services API. Build `intacct_client.py` using sender-id + user credentials
  (store in .env, blank in example). OAuth where supported.
- Read GL / project / job financials. Writes only to custom objects we own, never core ledgers.
- Genuinely API-able; this is the clean branch if it applies.

## BRANCH C — Sage 100/300 CRE  [if estimating feeds an on-prem ERP]
- Limited surface. Read via ODBC against Sage data sources (Job Cost, Project Mgmt).
- Sanctioned write path is the paid **Sage Office Connector Write** add-on — only pursue if
  IT already owns it and there's a real need. Default to read-only Job Cost actuals for
  comparison against estimates.

---

## Deliverables (once a branch is chosen)
- The branch-appropriate reader/client module + `.env.example` additions.
- A `sage_to_plan.py` adapter that turns estimate/financial reads into READ-ONLY context
  for the 30/60/90 tool (no writes to Sage).
- README section: which Sage was identified, the exact access IT granted, the connection
  method, and an explicit "we do not write to estimating source data" statement for IT's
  comfort.

## What to tell USC IT (helps the access conversation)
"Read-only login (or a read replica) against the Sage [product] database. No writes to
estimating data. Least privilege, scoped to the estimate/job tables we name. All processing
is local." That request is far easier to approve than open read/write.
