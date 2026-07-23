# Integrated Engineering / Estimating / Procurement / PM Process — CVR & HWC

**Status:** Framework defined — detailed process design in progress
**Process owner:** CVR
**Governance:** Per-project use of the process is approved by the **SVP Engineering and/or the COO**, based on project value.

## Big Picture

A **CVR-led process**, working closely with **HWC Construction/Operations PMs**, that:

1. **Builds accurate estimates** — CVR engineering and estimating working from real design input, validated with HWC Construction/Operations PMs who know field conditions and production rates.
2. **Leads procurement through PLS (Power Line Supply)** — equipment procurement is **led by an engineer inside CVR**, ensuring accurate part numbers, quantities, and technical requirements before anything is ordered.
3. **Runs projects with a dedicated CVR Project Management support team** operating in a **"Capital Delivery" mindset**: solid financial performance, on-time purchasing/ordering of equipment for the most efficient delivery possible, and professional project tracking using scheduling tools like **P6** with resource-loaded schedules.

## Roles & Responsibilities

| Function | Owner | Responsibility |
|----------|-------|----------------|
| Process leadership | CVR | Owns and runs the integrated process end to end |
| Estimating | CVR, with HWC Construction/Operations PMs | Accurate estimates grounded in design + field reality |
| Technical procurement | **CVR engineer (lead)** | Part numbers, quantities, technical requirements — verified by engineering before ordering |
| Procurement execution | PLS (Power Line Supply) | Sourcing and supply of equipment/material per CVR-verified specs |
| Project management | CVR dedicated PM support team | Capital Delivery mindset: financials, procurement timing, P6 resource-loaded schedules, professional tracking |
| Construction/Operations input | HWC PMs | Constructability, production rates, sequencing, field feedback into estimates and schedules |
| Governance / project opt-in | SVP Engineering and/or COO | Approve whether a given project uses the main process, based on value |

## Process Flow (target state)

```
Design (CVR Engineering)
   │  quantity takeoffs, technical specs
   ▼
Estimate (CVR Estimating + HWC Constr/Ops PM review)
   │  shared cost code structure
   ▼
Procurement (CVR engineer-led → PLS)
   │  verified part numbers, quantities, tech requirements
   │  PO timing driven by schedule need dates
   ▼
Execution (CVR PM support team + HWC Construction/Operations)
   │  P6 resource-loaded schedule, cost tracking vs. estimate
   ▼
Closeout / feedback loop into next estimate
```

## Capital Delivery Principles (CVR PM Support Team)

- **Financial performance first** — estimate-to-actual tracking is standing, not reactive; GP protected by early visibility.
- **Buy on time, every time** — procurement milestones live in the P6 schedule; material need dates drive PO placement dates, sized for lead times.
- **Resource-loaded schedules** — P6 schedules carry crews, engineering, and PM resources, not just dates.
- **Professional tracking** — consistent update cadence, earned-value-style progress, no surprise variances.

## Governance Model

- Default: qualifying projects run through the main integrated process.
- **Per-project decision** on whether to use the main process, driven by project value.
- Approval authority: **SVP Engineering and/or COO**.
- [ ] Define the value threshold / criteria that triggers the decision (dollar size, complexity, client requirements?)
- [ ] Define the lightweight alternative path for projects that don't use the main process

## Design Decisions Still to Make
- [ ] Common WBS / cost code structure across engineering, estimating, procurement (PLS), and PM
- [ ] Handoff gates: what engineering owes estimating and when; what estimating owes procurement/PM
- [ ] System of record for each data type (estimate, POs, actuals, P6 schedule)
- [ ] Named roles: who is the CVR procurement-lead engineer? Who staffs the dedicated PM support team?
- [ ] PLS interface: how do CVR-verified specs and quantities transmit to PLS (format, approval step, change control)?
- [ ] Estimate-vs-actual reconciliation cadence and report format
- [ ] Value threshold + approval workflow for the SVP Engineering / COO project opt-in decision

## Rollout Plan
- [ ] Map current-state process (interviews with CVR engineering/estimating, HWC Constr/Ops PMs, PLS)
- [ ] Draft target-state workflow + RACI against the framework above
- [ ] Review with SVP Engineering / COO — confirm governance model and thresholds
- [ ] Pilot on an active project (New Baltimore is the obvious candidate — workstreams 02/04 exercise exactly these seams)
- [ ] Document, train, roll out across CVR/HWC

## Success Criteria
- Any WO's estimated vs. committed vs. actual cost is answerable without a manual reconciliation exercise.
- Material need dates in the P6 schedule drive PO placement dates automatically.
- Zero procurement rework from wrong part numbers/quantities — engineering verification catches it before the PO.
- GP projection is a standing report, not a fire drill.
- Clear, fast SVP/COO decision on process applicability at project kickoff.
