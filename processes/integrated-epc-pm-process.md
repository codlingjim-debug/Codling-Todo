# Integrated Engineering / Estimating / Procurement / PM Process — CVR & HWC

**Status:** Not started
**Goal:** Establish one integrated process spanning engineering, estimating, procurement, and project management for CVR/HWC, so handoffs are defined and cost/schedule data flows in one direction of truth.

## Why (problem statement)
- (Capture current pain points here — e.g., estimates built without engineering input, procurement not tied to schedule need dates, PM discovering cost issues late. New Baltimore workstream 02 is a live example of reconciling after the fact instead of by design.)

## Target-State Process Sketch

1. **Engineering** produces design deliverables with quantity takeoffs in a standard format.
2. **Estimating** builds estimates from those takeoffs with a shared cost code structure (same codes used by accounting/PM).
3. **Procurement** buys against the estimate line items; PO commitments map back to work orders automatically.
4. **PM** runs cost/schedule from the same structure — the Master Schedule is cost- and resource-loaded from estimating data, and actuals flow back for GP tracking.

## Design Decisions to Make
- [ ] Common WBS / cost code structure across all four functions
- [ ] Handoff gates: what does engineering owe estimating, and when? What does estimating owe procurement/PM?
- [ ] System of record for each data type (estimate, POs, actuals, schedule)
- [ ] Review cadence: estimate-vs-actual reconciliation frequency
- [ ] Roles/RACI across CVR and HWC — who owns each step in each org

## Action Items
- [ ] Map the current-state process (interviews with each function lead)
- [ ] Draft target-state workflow and RACI
- [ ] Pilot on an active project (New Baltimore is the obvious candidate — workstreams 02/04 exercise exactly these seams)
- [ ] Document, train, roll out to CVR/HWC

## Success Criteria
- Any WO's estimated vs. committed vs. actual cost is answerable without a manual reconciliation exercise.
- Material need dates in the schedule drive PO placement dates automatically.
- GP projection is a standing report, not a fire drill.
