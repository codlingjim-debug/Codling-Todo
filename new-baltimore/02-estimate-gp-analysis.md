# 02 — Estimate / GP Analysis Across 39 Work Orders

**Status:** In progress — material reconciliation triage complete (Aug 5, 2026)

**Aug 5 update:** Built `NBALT_Material_Surplus_Triage.xlsx` from Jason Riley's 15 CWO reconciliation
workbooks + project rollup. Key findings: (1) the "truncated" DTE IM numbers in CUE PDFs are only
clipped visually — full values are intact in the PDF text layer, so no DTE exports are needed;
(2) validated CWO 73305080 end-to-end: reconciliation data matched the source exactly;
(3) project-wide position: ~$249k surplus / return candidates (91 IMs), ~$64k shortages (53 IMs),
~$322k required-with-no-captured-order (93 IMs — verify vs PLS; includes 81 cedar poles likely already
on order). Next: PLS line-item export to verify the order side before physical returns.
**Goal:** Determine where we stand based on actual material cost purchased, project where target GP will land, and identify where to adjust our approach **before construction begins next spring (2027)**.

## Key Inputs Needed
- [ ] Original estimate broken out by each of the 39 work orders (labor, material, equipment, subs, OH, markup)
- [ ] Actual material POs issued to date, mapped to work orders
- [ ] Committed-but-not-invoiced material costs
- [ ] Target GP % from the original bid/estimate
- [ ] List of the **8 underground POs being cancelled** — amounts and which WOs they hit

## Analysis Steps
1. [ ] Build a WO-by-WO comparison sheet: estimated material $ vs. actual/committed material $
2. [ ] Remove/credit the 8 cancelled underground POs from committed costs (and confirm whether the associated scope is also going away, or just being re-procured)
3. [ ] Compute variance per WO and in aggregate
4. [ ] Project GP at completion using actual material costs + remaining estimate
5. [ ] Identify the WOs driving the largest negative variance
6. [ ] Develop adjustment options for at-risk WOs (means/methods, crew mix, procurement strategy, scope clarification with DTE)
7. [ ] Present findings and recommended adjustments before spring 2027 mobilization

## Important Notes
- **8 underground POs will be cancelled** — do not count them in committed cost. Determine: is scope deleted, deferred, or re-sourced? Each answer changes the GP projection differently.
- Where TRK-4911 (see workstream 03) affects sequencing/escalation assumptions, flag it in the projection.
- Output of this analysis feeds the DTE open book (workstream 05) and the Master Schedule cost loading (workstream 04).

## Deliverable
A WO-level cost tracking workbook + a summary memo: current projected GP vs. target, variance drivers, recommended course corrections.

## Working Tracker (summary)

| Metric | Estimate | Actual/Committed | Variance | Notes |
|--------|----------|------------------|----------|-------|
| Total material (39 WOs) | | | | |
| Less: 8 cancelled UG POs | n/a | | | scope disposition TBD |
| Projected GP % | (target) | (projected) | | |
