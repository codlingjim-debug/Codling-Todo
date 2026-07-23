# Integrated Engineering / Estimating / Procurement / PM Process — CVR & HWC

**Status:** Operating model defined — ready for leadership review and pilot
**Process owner:** CVR
**Applicability:** **Mandatory for all projects $500k and above**, unless otherwise approved by the SVP Engineering or the COO.

## Big Picture

A **CVR-led process**, working closely with **HWC Construction/Operations PMs**, that:

1. **Builds accurate estimates** — the estimating team sits **inside CVR, reporting to the SVP of Engineering** (transitioning from HWC), building estimates from real design input and validating them with HWC Construction/Operations PMs who know field conditions and production rates.
2. **Leads procurement through PLS (Power Line Supply)** — equipment procurement is led by the **Lead Engineer, who is the Engineer of Record (EOR) for the project**, ensuring accurate part numbers, quantities, and technical requirements before anything is ordered.
3. **Runs projects with a dedicated CVR Project Manager** — a **PMP and/or PE, separate from the engineering lead** — operating in a **"Capital Delivery" mindset**: solid financial performance, on-time purchasing/ordering of equipment for the most efficient delivery possible, and professional tracking using P6 resource-loaded schedules.

> **Critical relationship:** the interaction between the **CVR PM and the HWC Construction PM** is the backbone of this process. The CVR PM owns capital delivery (cost, schedule, procurement, reporting); the HWC Construction PM owns field execution (crews, production, constructability). Neither succeeds without the other — this pairing meets weekly, shares one schedule and one cost picture, and jointly owns the project outcome.

## Governance

| Rule | Detail |
|------|--------|
| Threshold | Projects **≥ $500k** must follow this process |
| Exception authority | SVP Engineering or COO may approve an alternate approach for a given project |
| Below threshold | Lightweight path (defined separately); teams may still opt in |
| Gate decision timing | At project award / kickoff, documented in the kickoff record |

## Organization

- **Estimating team → CVR**, reporting to the **SVP of Engineering** (org move from HWC).
  - [ ] Define transition plan: reporting change date, systems access, template/cost-code standardization
- **Lead Engineer = Engineer of Record (EOR)** for the project. Owns design integrity and technical procurement content.
- **CVR PM** = dedicated **PMP/PE**, separate person from the EOR. Owns capital delivery.
- **HWC Construction PM** = field execution owner and constructability voice from estimate through closeout.
- **CVR PM support team** provides P6 scheduling, cost tracking, and reporting horsepower behind the CVR PM.

## Process Flow (target state)

```
Design (CVR Engineering — EOR)
   │  quantity takeoffs, technical specs
   ▼
Estimate (CVR Estimating + HWC Construction PM constructability review)
   │  shared cost code structure
   ▼
Procurement (EOR-verified content → CVR-PLS Transmittal → PLS)
   │  PO timing driven by P6 schedule need dates
   ▼
Execution (CVR PM ↔ HWC Construction PM partnership)
   │  P6 resource-loaded schedule, cost tracking vs. estimate
   ▼
Closeout / lessons + actuals feed back into estimating library
```

## CVR ↔ PLS Transmittal System (proposed)

A controlled, numbered transmittal is the only way material requirements move from CVR to PLS — no verbal orders, no email-thread BOMs.

**Transmittal package (per release):**

| Field | Content |
|-------|---------|
| Transmittal No. | `[Project]-PLS-###` sequential, with revision letter (e.g., `NB-PLS-004 Rev B`) |
| Bill of Material | Line-item part numbers, descriptions, quantities, units |
| Technical requirements | Specs, standards, ratings, approved manufacturers/equals |
| Need dates | Required-on-site dates pulled from the P6 schedule |
| Deliver-to | Site/laydown/warehouse instructions |
| Authorization | **EOR signature** (technical accuracy) + **CVR PM signature** (budget/schedule alignment) |
| PLS acknowledgment | PLS returns confirmation with pricing, lead times, and promise dates within a defined SLA (suggest 5 business days) |

**Change control:** any change to part number, quantity, spec, or need date requires a revised transmittal (new revision letter) with the same dual signature — this creates a clean audit trail of what was ordered, when, and on whose authority, and eliminates procurement rework from bad part numbers.

**Suggested platform:** start with a standardized transmittal form + register in SharePoint/Teams (both orgs already live there), with the transmittal register tracking status: Issued → Acknowledged → PO Placed → Delivered. If volume justifies it, graduate to a procurement module (e.g., Procore, or ERP requisitioning) — but the discipline matters more than the tool.

- [ ] Build the transmittal form template and register
- [ ] Agree SLA and acknowledgment format with PLS
- [ ] Define PLS's promise-date feedback loop into the P6 schedule

## Meeting Cadence

| Meeting | Frequency | Required attendees | Purpose |
|---------|-----------|--------------------|---------|
| Project Kickoff / Process Gate | Once, at award | CVR PM, EOR, Estimating lead, HWC Construction PM, PLS rep; SVP Eng/COO if exception sought | Confirm process applicability (≥$500k), baseline scope/budget/schedule, assign RACI names |
| **CVR PM ↔ HWC Construction PM sync** | **Weekly** | CVR PM, HWC Construction PM (+ superintendent as needed) | The critical pairing: 3-week lookahead, crew/resource needs, field issues, schedule progress |
| Procurement & Expediting Review | Biweekly | EOR, CVR PM, PLS rep, PM support (scheduler) | Transmittal register status, promise dates vs. need dates, expediting actions |
| Project Cost / GP Review | Monthly | CVR PM, Estimating lead, EOR, HWC Construction PM | Estimate vs. committed vs. actual by WO, GP forecast, trend/change log |
| P6 Schedule Update & Re-forecast | Monthly (feeding cost review) | PM support scheduler, CVR PM, HWC Construction PM | Progress the schedule, re-forecast, update resource loading |
| Portfolio / Governance Review | Quarterly | SVP Engineering, COO, CVR PMs, Estimating lead | Portfolio GP performance, process exceptions granted, lessons learned, process improvements |

Principles: the weekly CVR PM ↔ HWC Construction PM sync is non-negotiable and never cancelled — everything else flexes around it. Monthly cost review uses the P6 update from the same week so cost and schedule tell one story.

## RACI

**Roles:** EOR (Lead Engineer, CVR) · CVR PM (PMP/PE) · EST (CVR Estimating) · HWC PM (Construction PM) · PLS · PMS (CVR PM Support team) · SVP (SVP Engineering) · COO

R = Responsible, A = Accountable, C = Consulted, I = Informed

| Activity | EOR | CVR PM | EST | HWC PM | PLS | PMS | SVP | COO |
|----------|-----|--------|-----|--------|-----|-----|-----|-----|
| Process applicability decision (≥$500k / exception) | C | R | I | I | — | — | **A** | **A** |
| Design deliverables & quantity takeoffs | **A/R** | I | C | C | — | — | I | — |
| Estimate development | C | C | **A/R** | C | C (pricing) | — | I | — |
| Constructability review of estimate | C | C | C | **A/R** | — | — | — | — |
| Estimate approval / bid sign-off | C | R | R | C | — | — | **A** | I |
| Project baseline (budget + P6 schedule) | C | **A/R** | C | C | I | R | I | — |
| BOM: part numbers, quantities, tech requirements | **A/R** | C | C | C | C | — | — | — |
| Transmittal issuance to PLS | R (tech) | **A** / R (budget-schedule) | I | I | I | R (register) | — | — |
| PO placement & supplier management | C | I | — | I | **A/R** | I | — | — |
| Expediting & promise-date management | C | **A** | — | C | R | R | — | — |
| Material receipt & field verification | I | I | — | **A/R** | C | I | — | — |
| P6 schedule updates & resource loading | C | **A** | — | C | I | R | — | — |
| Field execution (crews, production, safety) | C | C | — | **A/R** | — | — | — | I |
| Cost tracking: estimate vs. committed vs. actual | I | **A/R** | C | C | I | R | I | I |
| GP forecast & monthly project report | I | **A/R** | C | C | — | R | I | I |
| Change management (scope/spec/quantity changes) | R (tech) | **A/R** (commercial) | C | C | I | I | I | — |
| Client-facing commercial deliverables (e.g., open book) | C | **A/R** | R | C | — | R | I | I |
| Closeout: actuals into estimating library, lessons learned | C | **A** | R | R | I | R | I | — |
| Process improvement & standards ownership | C | R | R | C | C | C | **A** | I |

Notes on the RACI:
- The **CVR PM is Accountable for capital delivery** end to end — that's the Capital Delivery mindset made structural.
- The **EOR is Accountable for everything technical** — design and procurement content. The dual-signature transmittal is where those two accountabilities meet.
- The **HWC Construction PM is Accountable for the field** — and Consulted on nearly everything upstream, because constructability input early is what makes the estimate and schedule real.
- **SVP/COO are Accountable only at the gates** — process applicability, estimate sign-off, and portfolio governance — so projects run without leadership in the critical path day-to-day.

## Rollout Plan
- [ ] Leadership review: confirm this operating model with SVP Engineering / COO (incl. estimating org move)
- [ ] Execute estimating team transition from HWC → CVR (reporting, systems, standards)
- [ ] Build the CVR-PLS transmittal form, register, and SLA agreement
- [ ] Stand up the meeting cadence with named attendees
- [ ] Pilot on New Baltimore (workstreams 02/04 exercise exactly these seams)
- [ ] Document, train, roll out across CVR/HWC

## Success Criteria
- Any WO's estimated vs. committed vs. actual cost is answerable without a manual reconciliation exercise.
- Material need dates in the P6 schedule drive PO placement dates automatically.
- Zero procurement rework from wrong part numbers/quantities — EOR verification and transmittal change control catch it before the PO.
- GP projection is a standing report, not a fire drill.
- Every ≥$500k project has a documented gate decision; exceptions are visible to SVP/COO quarterly.
