# Integrated Engineering / Estimating / Procurement / PM Process — CVR & HWC

**Status:** Executive summary — for CEO/COO approval
**Process owner:** CVR
**Applicability:** **Mandatory for all projects $500k and above**, unless otherwise approved by the SVP Engineering or the COO.

## Executive Summary

CVR proposes one integrated process for how CVR and HWC take capital projects from design through construction closeout — engineering, estimating, procurement, and project management operating on a single cost and schedule backbone, run with the same **Capital Delivery** discipline our investor-owned utility clients apply to their own capital programs.

Today those functions sit in different organizations with manual handoffs between them. The cost of those seams is real: estimates built without design quantities, purchase orders placed without engineering verification, GP surprises discovered after the money is spent, and schedules that don't drive procurement. As our IOU clients (DTE and others) move toward open-book commercial arrangements, they are effectively auditing our project controls — predictable delivery is becoming a condition of winning the work.

**Decisions requested of the CEO/COO:**

1. **Adopt the integrated process** as mandatory for all projects ≥ $500k, with exceptions approved by the SVP Engineering or COO.
2. **Transition the estimating team from HWC into CVR**, reporting to the SVP of Engineering.
3. **Stand up the dedicated CVR project management team** — PMP/PE-credentialed PMs, separate from the engineering leads, operating in the Capital Delivery model with P6.
4. **Endorse the engineer-verified CVR → PLS transmittal system** as the single channel for material procurement.
5. **Pilot on the New Baltimore program** ahead of the spring 2027 construction start, then roll out across CVR/HWC.

## Key Definitions

| Term | Meaning in this document |
|------|--------------------------|
| **Capital Delivery** | An operating mindset borrowed from how investor-owned utilities run their capital programs: every project managed as a **financial investment, not just a construction job** — baselined budget/schedule, committed-dollar visibility, monthly forecast-at-completion, gated leadership decisions. For CVR/HWC: managing GP the way an IOU's capital program office manages rate-base spend — proactively, with standing reports instead of after-the-fact reconciliation. |
| **IOU** | Investor-Owned Utility — shareholder-owned, commission-regulated (e.g., DTE). Their capital program performance flows into rate cases, which is why they expect open-book transparency and professional project controls from partners. |
| **EOR** | Engineer of Record — the licensed engineer responsible for the project design; in this process, also the technical authority for all procurement content. |
| **GP** | Gross Profit — revenue minus direct project costs. The primary financial measure at project and work-order level. |
| **Committed cost** | Dollars obligated by PO/subcontract whether or not invoiced. Tracking commitments is what makes early GP forecasting possible. |
| **Open book** | Commercial arrangement sharing the full cost buildup (directs, OH, markup/fee, contingency) with the client. |
| **P6** | Oracle Primavera P6 — industry-standard scheduling platform; logic-driven CPM schedules carrying resources and costs. |
| **Resource / cost loading** | Assigning crews, staff, and dollars to schedule activities so the schedule forecasts manpower, cash flow, and material need dates. |
| **Transmittal** | Numbered, revision-controlled release of engineer-verified material requirements from CVR to PLS — the auditable record of what was ordered and on whose authority. |
| **Need date / lead time** | Date material must be on site (from P6) and supplier time from PO to delivery. PO deadline = need date − lead time. |
| **WBS / cost codes** | Common breakdown structure shared by estimating, procurement, scheduling, accounting — so estimate, POs, schedule, and actuals reconcile automatically. |
| **RACI** | Responsible / Accountable / Consulted / Informed — exactly one Accountable owner per activity. |

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

## Systems Roadmap

**Current state:** email and network drives — cannot support committed-cost visibility, schedule-driven procurement, or auditable transmittals. Principle: **process first, platform second** — the system decision must not stall the process launch.

### Phased Approach

| Phase | What | Timing | ROM Cost* | Purpose |
|-------|------|--------|-----------|---------|
| **Crawl** | SharePoint/Teams transmittal form + register, WO cost workbook, templates | Now – 60 days | $0 software; ~$10–15k internal effort | Prove the discipline; generate platform requirements |
| **Walk** | Platform pilot on New Baltimore (Unifier vs. InEight) + estimating tool selection | Q4 2026 – Q2 2027 | $75–150k first year | Stress-test against the 39-WO reconciliation before spring 2027 |
| **Run** | Full rollout: platform + P6 + estimating tool + ERP feed for actuals | 2027–2028 | $150–400k/yr run-rate | One backbone, GP forecast as a standing report |

### Platform Options

| Option | Role | P6 integration | ROM cost* | Fit |
|--------|------|----------------|-----------|-----|
| **Oracle Primavera Unifier** | Capital program cost management tied to P6 WBS/CBS; cash flow; change mgmt; configurable workflows (incl. transmittals) | **Native, bi-directional** | $75–250k/yr + $100–300k implementation (4–9 mo) | Strongest match to Capital Delivery; same tooling class as IOU clients. Heaviest lift. |
| **InEight** | Contractor suite, estimating-rooted; estimate → cost codes → controls | Connector | $50–150k/yr + $50–150k implementation (3–6 mo) | Lighter-lift challenger; evaluate head-to-head with Unifier |
| **Oracle Aconex** | Controlled transmittals & doc control | Oracle ecosystem | $30–100k/yr | Add-on if transmittal volume outgrows SharePoint |
| **Procore** | Field/construction PM; best UX for HWC field | 3rd-party connector | $40–120k/yr; light implementation | Strong at field end, shallow cost controls — complement, not backbone |
| **e-Builder / Kahua** | Owner-side capital program platforms | Varies | $75k+/yr | Built for owners like DTE — not recommended for CVR backbone |

### Estimating Tools (evaluation underway)

| Tool | Strength | ROM cost* | Fit |
|------|----------|-----------|-----|
| **HCSS HeavyBid** | Utility/heavy-civil standard; crew-based production estimating | $15–35k first year; ~$10–20k/yr after | Structured export seeds P6 cost loading + shared WBS |
| **InEight Estimate** | Deep integration with InEight suite | $20–50k/yr (3–5 seats) | Strongest if InEight wins platform evaluation |
| **Excel (status quo)** | Familiar, free | $0 | No structured export/version control — today's reconciliation pain |

\*ROM = rough order of magnitude, planning-level only; validate with vendor quotes. Budgetary quotes from Oracle and InEight are a Walk-phase deliverable — no software commitment requested beyond the pilot evaluation.

### Decision Path
1. Launch Crawl on approval of this document (no new spend).
2. Fold the current estimating tool evaluation into the platform evaluation — choose the estimate data model and cost-controls data model together.
3. Bring budgetary quotes and the Unifier-vs-InEight recommendation to the quarterly Portfolio/Governance Review for the platform decision.

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
