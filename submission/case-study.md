# Material loss: establish the truth, then improve the cut
## 1 | Executive decision
Client B - Structural steel | Confidential hiring assessment | 14 October 2026

**Two-sentence problem statement.** The client cannot reliably attribute material loss, distinguish reusable inventory from scrap, or quantify the avoidable cost of its cutting decisions. It asked where to apply AI, especially nesting, but first needs reconciled material evidence and a fair comparison of manual planning with automation it already owns.

Approve a six-week engagement capped at USD 45,000: USD 15,000 for discovery/native-tool benchmarking, then USD 30,000 only if the week-2 evidence justifies a pilot. No build is an acceptable outcome; measurement, operator practice or Strumis configuration may capture value faster.

Reported plate loss of 20-25%, profile loss of 5-10% and overall loss of 7-10% are unverified and may mix scrap, offcuts and revisions. Call 2 describes 80,000 t/year as capacity, yet 7,000-8,000 t/month implies 84,000-96,000 t/year. Separate capacity, shipped output, raw input and actual throughput; none is yet a validated savings denominator.

## 2 | Operating model and loss mechanisms
BD bids -> Estimation prices -> Planning schedules -> Engineering releases drawings -> Procurement buys per project -> Yard/inventory receives -> Nesting plans -> CNC sizing cuts -> Fabrication/welding -> Coating -> Dispatch.

Sequence: call 2; handoffs, receipt controls and system ownership are inferred. Drawings change but budgets stay fixed (call 1). Project-specific cost loading blocks sharing without finance, contract and operational approval.

Strumis and an unnamed PLM support nesting. The shift toward Strumis includes an automatic option; reported manual superiority is untested. Offcuts are recorded and checked; identity, accessibility, reuse and accounting effectiveness remain unverified.

**Evidence gaps.** Revision history is unclear; issues, cut results, returns and scrap sales may not reconcile. Yard access, held projects, changes, purchased sizes or offcut identity may dominate geometry. Separate client revisions (potential claims, not guaranteed), engineering errors, cut loss and unexplained variance; unknown is not scrap.

## 3 | People and the decision they own
Confirmed attendees: Cost Control engineer; a colleague briefly joined. Sponsor status is provisional; other roles below are anticipated, with authority to be confirmed.

| Stakeholder | Incentive / likely objection | Evidence needed; validate or approve |
|---|---|---|
| Cost Control / likely sponsor | Explain budget variance; weak attribution | Reconciled loss ledger; own measurement and coordinate access |
| Management / economic buyer | Cash and delivery; speculative ROI | Downside economics; approve spend and gates |
| Nesting lead and operators | Feasible cuts; unfair comparisons | Equal constraints, review time; validate benchmark and every plan |
| Engineering / revision owners | Correct releases; blame risk | Revision lineage and cause codes; certify released geometry |
| Planning and procurement | Due dates and availability; stock disruption | Demand, reservations, purchase sizes; approve scheduling assumptions |
| Yard / inventory | Find and move stock; added scanning | Physical identity and access; attest available offcuts |
| Finance / project accounting | Accurate margin; unauthorised transfers | Costs, salvage, claims; sign value and ownership rules |
| CNC / production managers | Safe quality and throughput; downtime | Machine constraints; approve every execution and stop authority |
| Strumis / PLM technical owners | Stable systems; unsupported export | Versions, licences, settings; validate export and benchmark setup |
| IT / security / integration | Confidentiality; access burden | Read-only design and retention; approve access and storage |

<!-- PAGEBREAK -->

# Discovery and choice
## 4 | Exactly five ranked questions for the next call
**1. Can we reconcile 30 representative jobs from released drawings and stock issues through cut parts, returned offcuts, weighed scrap and project costs, and show the denominators behind the reported loss and throughput figures?** Why: establish whether avoidable loss is measurable at all. Decision: start a benchmark or a measurement repair engagement. Until answered: records are fragmented but a bounded sample is recoverable. If false: stop software work, deliver a capture/reconciliation plan and reprice only by agreement.

**2. Will the nesting lead and production manager walk us through one plate job and one profile job, including kerf, spacing, margins, rotations, grade, heat traceability, machine limits, due dates and why plans are rejected?** Why: a high-yield but uncuttable layout has no value. Decision: eligible job types and operational acceptance rules. Assumption: operators can document a stable subset and review plans. If false: narrow further or stop; never infer machine safety constraints.

**3. Which Strumis/PLM versions, nesting licences, settings and supported read-only exports are available, and can an experienced operator run native automatic nesting on the same jobs under the same constraints?** Why: existing automation may already solve the problem; integration is unverified. Decision: configure/train versus build, and whether file ingestion is viable. Assumption: client-approved CSV or comparable files and a runnable native mode are available. If false: vendor-assisted manual extraction or a readiness-only result; no invented API or hidden integration commitment.

**4. Can the yard and engineering owners trace each candidate stock/offcut to its physical location, dimensions, grade/section, required heat/lot, reservation, project owner and the latest released drawing revision, including who caused each change?** Why: phantom stock and stale drawings can invalidate savings and claims. Decision: safe eligibility and whether offcut visibility or revision control is the priority. Assumption: a small verified subset exists. If false: quarantine uncertain records and improve identification/release controls before suggestions.

**5. Who can approve material reuse within a project and transfers between projects, and how do finance and contracts price transfers, salvage, client revision claims and incremental handling?** Why: technical fit does not establish permission or cash benefit. Decision: project boundary and economic value. Assumption: within-project reuse is allowed subject to reservation checks; cross-project allocation is prohibited. If false: tighten to explicitly approved stock only; expand across projects solely after written finance, contract and production approval.

## 5 | Options and conditional recommendation
Illustrative relative assessment, subject to access. Value means measurable net value, not promised yield. H/M/L = high/medium/low; costs are relative except the quoted pilot.

| Option | Value / data readiness | Complexity / integration | Adoption / deployment risk | First result / cost | Explainability / reversibility |
|---|---|---|---|---|---|
| A. Measure + improve workflow | Foundational / M | L / L | H / L | Week 1 / L | H / H |
| B. Benchmark native Strumis | Potentially H / M | L-M / unverified | M-H / L in shadow | Week 2 / L-M | M-H / H |
| C. Narrow reviewed assistant | Conditional / L-M | M / file exports | M / M | Weeks 3-6 / M | H / H |
| D. Custom OR/constraint engine | Unproven / L | H / H | M / H | Beyond pilot / H | M-H / M |
| E. Enterprise AI platform | Unattributed / L | Very H / very H | L / very H | Months+ / very H | L-M / L |

Choose A + B first, C only at the week-2 gate. D is a later bounded optimisation experiment if simpler methods fail; E is rejected for this engagement. Stage 3 expansion is separately approved, funded and scoped. Treat the six weeks as one capped commercial pilot with stop gates, not a commitment to build every stage.

**Deliberate exclusions.** No bespoke generative-AI nesting engine, Strumis/PLM replacement, automatic CNC instructions, unapproved cross-project allocation, enterprise rollout or major ML/MLOps stack. Rules and deterministic search are inspectable and testable against physical constraints; deep learning has neither validated training evidence nor an established need. CarTrack and booking data deserve a separate utilisation diagnostic, including whether idle time overlaps actual demand; no equipment platform is included here.

<!-- PAGEBREAK -->

# Engineering that fits production
## 6 | Read-only by design; people retain control
Architecture: benchmark native tools before assisted candidates; operators review explanations before nesting lead and production approval.

A client-approved Python batch process uses immutable exports and SQLite. CSV is the default; geometry formats and export support require technical-owner confirmation. No Strumis API, writeback or CNC integration is assumed. Reports show stock, parts, revision, checks, rejection reasons and material/value deltas. Operators enter approved plans in existing software.

| Data group | Required for eligible comparison | Source / consequence of absence |
|---|---|---|
| Demand and release | Project, released drawing + revision, part ID, quantity, length or geometry, plate/profile, grade, thickness/section | Engineering/PLM export; missing or stale release blocks candidate |
| Inventory | Stock/offcut ID, measured dimensions, quantity, location, owner, availability and reservation; heat/lot where required | Strumis/yard attestation; unknown identity or traceability quarantined |
| Cut feasibility | Machine, kerf, spacing, edge/clamp margins, cutting restrictions, permitted rotations/orientation/grain where applicable | Nesting + production; absent applicable constraint blocks comparison |
| Timing and permissions | Due date, stock snapshot time, project permissions, plan approvals | Planning + finance; no unauthorised transfer or unavailable stock |
| Measurement and value | Input/part/scrap mass, returned offcuts, actual cut/consumption events, purchase or marginal displaced cost, scrap realisation, handling time/cost | Yard + production + finance; absent actuals permits simulation only, not cash claim |
| Optional enrichment | Photos, detailed yard route, machine telemetry, supplier alternatives, claim payment references | Useful after eligibility; paid claims become required if claiming realised recovery |

Use explicit units, stable IDs and timestamps. Quarantine missing critical data, duplicates, impossible dimensions, negative quantities and invalid references. Reconcile opening stock + receipts + approved transfers - closing stock against parts + scrap + other loss; retain unexplained variance. Compare identical stock/revision snapshots.

**Algorithm ladder.** First benchmark the native software heuristic with an experienced user and frozen settings. For straight profiles, transparent first-fit/best-fit decreasing heuristics account for length and kerf; bounded integer/constraint optimisation can prove or bound small instances with a time limit and feasible fallback. Irregular 2D plates need geometry, rotations, spacing, kerf, cutting-path and machine constraints: a rectangle packer is not a production plate solution. Use existing qualified nesting capability initially; engage specialist geometry work only if justified.

**Audit, access and recovery.** Each run stores file hashes, import time, source row, schema version, inventory snapshot, release IDs, algorithm/settings, proposed cuts, rejection codes and reviewers. IT grants least-privilege access; engineers prepare candidates, operators review, nesting lead and production approve; finance alone attests realised value and transfers. Encrypt client-approved storage, restrict exports, keep secrets outside files and agree retention/deletion at kickoff. Do not send data to external AI services.

Malformed batches fail atomically into quarantine with row-level reasons; valid prior runs remain available. Revision or inventory changes invalidate unexecuted approvals and require rechecking. Retain the manual plan as fallback; disabling the assistant restores the existing process without system rollback. Back up the ledger, test restore, revoke access and return/delete working data at close under the agreed retention policy.

**Focused proof.** The synthetic Python demo tests 1D length/kerf, ownership and grade/section rules; it validates neither CNC safety, irregular plates nor plant ROI. Executed evidence: prototype-results.md.

<!-- PAGEBREAK -->

# Prove improvement before execution
## 7 | A reproducible, paired evaluation
**Baseline and sample.** Pre-register at least 30 eligible jobs: target 15 plate and 15 profile jobs across at least three projects, stratified by mass, geometry complexity and revision exposure. Use a consecutive eligible window; record all exclusions and compare included/excluded mix. If fewer qualify, report an inconclusive readiness result rather than quietly shrinking the sample. Thirty jobs is a practical floor, not a statistical power guarantee; confirm variance and minimum detectable effect before expanding.

Freeze each job's released geometry/revision, quantities, stock/offcut availability at the decision time, project permissions, machine/kerf rules and due dates. Preserve the accepted manual plan. Run native Strumis once per job with a qualified operator and frozen settings: 60 plans total including manual. If feasible and justified, run the assisted method once per job: 90 plans total. Repeat 10 selected native/assisted jobs twice each (40 additional executions with three arms) to assess repeatability; use the first predeclared run in the primary comparison, never the best result. If only two arms, add 20 native repeats. Capture seeds/settings where applicable; charge equal planning-time budgets.

Engineering signs release identity; yard verifies stock; operators and production check feasibility blind to financial ranking where practical. Cost Control computes paired, mass-weighted results by material class and overall only at a supported production mix. Do not average job percentages. Report paired deltas with job-level bootstrap intervals and project sensitivity; require an interval excluding zero for reproducibility. Do not extrapolate an unrepresentative sample to 80,000 tonnes.

| Metric | Numerator / denominator; source and owner | Proposed acceptance criterion |
|---|---|---|
| Unrecoverable scrap | Weighed kerf/scrap mass / input stock mass; include used offcuts in input; production/yard + Cost Control | At least 0.5 percentage-point absolute reduction vs accepted manual, pooled by mass; no unexplained balance counted as saving |
| Recoverable offcuts / reuse | Returned eligible remnant kg / input kg; reused cohort kg / cohort's original returned kg within 90 days; yard | Track separately; zero cash credit at creation, follow through 90 days |
| Virgin consumption | New stock kg issued net of unused returns / good released-part kg; stock issue/return ledger | Improvement consistent with scrap benefit; no inventory depletion concealed |
| Net economic value | Displaced purchases + actual incremental scrap proceeds + separately paid claims - forgone salvage - extra handling/rework/delay; finance | Positive conservative benefit; annual steady-state benefit after running/friction costs at least USD 45k for <=12-month simple payback |
| Feasibility / quality | Feasible complete plans / reviewed plans; nesting lead + production | 100% of executed plans approved; zero grade, revision, traceability or quality violations |
| Acceptance / planning | Accepted suggestions / reviewed eligible suggestions; extra minutes / job; operators' logged reasons/time | >=80% acceptance; median extra time <=10 min and 90th percentile <=20 min |
| Schedule impact | Pilot-caused late jobs / executed jobs; downtime minutes; planning/production | Zero pilot-caused missed commitments or unplanned downtime |

These are illustrative criteria requiring agreement before testing, not promised outcomes. A scrap threshold alone cannot authorise a build: C must beat the best accepted existing method on net value or provide an agreed measurable workflow benefit. If native automation gives equivalent benefit (within 0.1 percentage point and no material time/value difference), adopt/configure it and stop custom development.

**Shadow then controlled execution.** Week 5 reviews at least 10 consecutive current jobs in shadow (minimum five in each in-scope class); no machine commands are emitted. Only after all feasibility checks pass may lead and production approve up to five supervised cuts in week 6. Real production outcomes are reported separately from historical simulations; a small execution sample cannot establish annual savings. Complete 90-day offcut follow-up under optional support or a named client owner.

**Stop/no-go.** No reproducible benefit over manual; inadequate reliable records; equivalent native performance; infeasible plans; negative net value; failed operator acceptance; unsafe disruption; or any unapproved transfer stops expansion. Quarantine individual infeasible candidates; systemic constraint failure stops trials. Reinstate the accepted manual process. Cost Control and finance sign measurement/value; engineering, yard, nesting and production sign validity; management owns the final go/no-go with IT approval for any continuing deployment.

<!-- PAGEBREAK -->

# Commercial case: assumptions, not a savings promise
## 8 | Value, cost, price and payback
Geography, currency, prices, actual input volume and scrap realisation are unknown. USD is solely an illustrative modelling currency. Reconfirm local currency, taxes, rates and scope before proposal acceptance. No client budget has been established. All annual values below describe a hypothetical steady-state year, not verified factory results.

**Base arithmetic.** Assumed annual input 80,000 t x 50% eligibility = 40,000 eligible t. Assumed unrecoverable scrap improves from 8.5% to 7.7%: 0.8 percentage points = 0.008. Recovered-equivalent material = 40,000 x 0.008 = 320 t/year. At USD 500/t marginal net value after displaced-material/salvage adjustment: 320 x 500 = USD 160,000/year gross value. This fixed-input proxy requires equal good output, no inventory drawdown and verified purchase displacement before it can become a cash forecast.

| Scenario | Input t x eligible share | Improvement / net USD/t | Gross value | Annual net after support + friction | Year-1 net after pilot* |
|---|---|---|---|---|---|
| Downside | 50,000 x 30% = 15,000 | 0.2 pp / 350 | 15,000 x .002 x 350 = 10,500 | 10,500 - 6,000 - 15,000 = -10,500 | -55,500 |
| Base | 80,000 x 50% = 40,000 | 0.8 pp / 500 | 40,000 x .008 x 500 = 160,000 | 160,000 - 6,000 - 10,000 = 144,000 | 99,000 |
| Upside | 80,000 x 70% = 56,000 | 1.2 pp / 600 | 56,000 x .012 x 600 = 403,200 | 403,200 - 6,000 - 15,000 = 382,200 | 337,200 |

*Year 1 here means 12 full operating months after enablement, charging the one-time pilot fee too. From kickoff, an optimistic six-week start delay leaves 46/52 of annual gross benefit: base 160,000 x 46/52 - 45,000 - 6,000 - 10,000 = USD 80,538.46. Actual ramp, purchase timing and client labour can reduce this further.

**Bottom-up internal delivery cost (loaded day rates).**

| Effort | Calculation | Internal cost USD |
|---|---|---|
| FDE / solution engineering | 15 days x 800 | 12,000 |
| Data / optimisation engineering | 12 days x 700 | 8,400 |
| Testing / operational validation | 5 days x 600 | 3,000 |
| Project oversight | 3 days x 1,000 | 3,000 |
| Direct labour subtotal | 35 person-days | 26,400 |
| Pilot infrastructure | Fixed allowance | 600 |
| Contingency | 15% x (26,400 + 600) | 4,050 |
| Total internal delivery cost | 27,000 + 4,050 | 31,050 |

**Price and structure.** Capped milestone fixed fee USD 45,000; expected contribution USD 13,950 = 45,000 - 31,050; delivery margin = 13,950 / 45,000 = 31.0%, before corporate overhead/tax. Stage 0/1 is USD 15,000: USD 7,500 kickoff and USD 7,500 at week-2 report acceptance. Optional Stage 2 is USD 30,000: USD 15,000 on signed build gate, USD 10,000 on shadow report acceptance, USD 5,000 at final handover. Payment buys accepted work, not a savings guarantee. Stop after week 2: no remaining USD 30,000 liability; deliver evidence and recommendations. Internal stage-0/1 cost budget USD 10,350; conditional balance USD 20,700.

**Running cost and return.** Optional lightweight support/approved hosting USD 500/month = USD 6,000/year (up to four support hours/month, no production SLA). Illustrative provider cost USD 300/month; extra integration or support separately scoped. Client first-year vendor spend = 45,000 + 6,000 = USD 51,000; add assumed USD 10,000 internal change/handling cost for USD 61,000 economic outlay. Simple base payback = 45,000 / (144,000/12) = 3.75 operating months, roughly 5.13 months from kickoff with six weeks' delay; downside never pays back.

First-year base break-even improvement = 61,000 / (40,000 x 500) = 0.00305 = **0.305 pp**; recurring-only break-even = 16,000 / 20,000,000 = **0.08 pp**. Six-week delay lifts first-year break-even to **0.345 pp**. Client mobilisation beyond the friction allowance, tax, vendor licences and travel are excluded and must be priced before signing. Track claim recovery separately; never add offcut book value or scrap proceeds already included in USD 500/t.

<!-- PAGEBREAK -->

# Delivery gates and risk ownership
## 9 | Six weeks, conditional on client readiness
Hiring deadline: 48 hours after receipt, separate from this pilot. Verify the actual invitation deadline.

| When / stage | Output and delivery owner | Client dependency / gate |
|---|---|---|
| Week 1 / Stage 0 | FDE + Cost Control: preliminary loss/readiness report | Sponsor convenes owners; exports within three working days. Missing data: readiness only |
| Week 2 / Stage 1 | FDE + nesting lead: 30-job manual/native benchmark and business case | Valid releases, stock and native mode. Management/finance authorise USD 30k balance only with evidence |
| Weeks 3-4 / conditional Stage 2 | FDE + engineer: file-based offcut checks, loss classification, suggestions | Verified within-project stock and rules; technical-owner review |
| Week 5 | Operators + production: >=10 shadow jobs and acceptance report | Review capacity; feasibility checks before any execution |
| Week 6 | Cost Control + finance: economics, handover; up to five approved cuts | Production availability; management chooses native adoption, measurement, narrow rollout or stop |

Scope: one site, two exports, one profile family, bounded plate benchmark; 35 person-days across overlapping contributors. Client owners: 1-2 hours/week plus benchmark time. Access delays pause dates; extra integrations, geometry work or remediation require written change control. Stage 3 needs separate finance/contract/technical/production approval; follow reuse for 90 days.

## 10 | Risk register and stop/rollback rules
Preliminary likelihood/impact: H = high, M = medium. Assign named owners at kickoff.

| Risk / L-I | Mitigation | Owner / stop or rollback |
|---|---|---|
| Bad data / wastage definition H-H | Separate scrap, returns, revisions, unknowns; reconcile mass | Cost Control + finance / <30 reliable jobs: no efficacy claim or build |
| Biased comparison M-H | Frozen paired inputs, first-run rule, exclusions, equal time | FDE + nesting lead / unequal inputs: invalidate pair |
| Infeasible cuts M-H | Signed constraints, shadow, existing CNC controls | Production / unsafe proposal: halt trial, manual fallback |
| Grade/geometry/lineage M-H | Physical identity, dimensions and required heat checks | Yard + engineering / uncertain material: quarantine |
| Drawing revisions H-H | Release lock, cause codes, invalidate old approvals | Engineering / changed release: cancel affected plan |
| Project cost transfers H-H | Same-project rule; future finance/contract consent | Finance / unapproved transfer: block and revert suggestion |
| Vendor/export limits M-H | Verify licence/settings and sample files; no API promise | Technical owner + IT / no reliable export: readiness-only |
| Operator resistance M-H | Co-design, fair tests, reasons and review-time budget | Nesting lead / <80% acceptance after one improvement cycle: stop rollout |
| Disruption M-H | Shadow first; supervised cuts and manual fallback | Production + planning / pilot delay or downtime: pause |
| Inflated savings H-H | Actual input, displacement, salvage and friction sensitivity | Finance / negative benefit or >12-month payback: no build gate |
| Confidentiality M-H | Approved storage, least privilege; no public repo/external AI upload | IT/security / suspected exposure: stop processing, client response |

**Likely failure:** incomplete baseline or unusable recorded offcuts. Fix measurement and workflow first. Equivalent native performance is a successful diagnostic: stop custom work. CarTrack/booking utilisation analysis is separate; idle time need not mean surplus equipment.

**Management decision:** approve USD 15,000, accountable owners and read-only access. Reserve USD 30,000 subject to evidence and operational acceptance.

