# Filled submission form - confidential

File upload fields: Case study* -> submission/case-study.pdf; One-page client note* -> submission/client-note.pdf. The original written field wording and order below are preserved.

## 1. In two sentences: what is the client's real problem, and how is it different from what they asked for?*

The client cannot reliably attribute material loss, distinguish reusable inventory from scrap, or quantify the avoidable cost of its cutting decisions. It asked where to apply AI, especially nesting, but first needs reconciled material evidence and a fair comparison of manual planning with automation it already owns.

## 2. Who are the people in this deal, and what does each of them need to hear from you?*

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

I would tell Cost Control that the pilot is designed to make variance explainable rather than assign blame. Management hears a capped first commitment and credible stop decisions; operators hear that their real constraints and accepted plans are the benchmark. Finance hears that project ownership and salvage treatment govern every value claim. The operational and IT owners hear that read-only files and the existing approval workflow preserve their control. No named economic buyer, decision-maker or signed sponsor commitment is established.

## 3. The five questions you would ask on the next call, ranked.** For each one: why it matters, and what you assumed while you wait for the answer.*

**1. Can we reconcile 30 representative jobs from released drawings and stock issues through cut parts, returned offcuts, weighed scrap and project costs, and show the denominators behind the reported loss and throughput figures?** Why: establish whether avoidable loss is measurable at all. Decision: start a benchmark or a measurement repair engagement. Until answered: records are fragmented but a bounded sample is recoverable. If false: stop software work, deliver a capture/reconciliation plan and reprice only by agreement.

**2. Will the nesting lead and production manager walk us through one plate job and one profile job, including kerf, spacing, margins, rotations, grade, heat traceability, machine limits, due dates and why plans are rejected?** Why: a high-yield but uncuttable layout has no value. Decision: eligible job types and operational acceptance rules. Assumption: operators can document a stable subset and review plans. If false: narrow further or stop; never infer machine safety constraints.

**3. Which Strumis/PLM versions, nesting licences, settings and supported read-only exports are available, and can an experienced operator run native automatic nesting on the same jobs under the same constraints?** Why: existing automation may already solve the problem; integration is unverified. Decision: configure/train versus build, and whether file ingestion is viable. Assumption: client-approved CSV or comparable files and a runnable native mode are available. If false: vendor-assisted manual extraction or a readiness-only result; no invented API or hidden integration commitment.

**4. Can the yard and engineering owners trace each candidate stock/offcut to its physical location, dimensions, grade/section, required heat/lot, reservation, project owner and the latest released drawing revision, including who caused each change?** Why: phantom stock and stale drawings can invalidate savings and claims. Decision: safe eligibility and whether offcut visibility or revision control is the priority. Assumption: a small verified subset exists. If false: quarantine uncertain records and improve identification/release controls before suggestions.

**5. Who can approve material reuse within a project and transfers between projects, and how do finance and contracts price transfers, salvage, client revision claims and incremental handling?** Why: technical fit does not establish permission or cash benefit. Decision: project boundary and economic value. Assumption: within-project reuse is allowed subject to reservation checks; cross-project allocation is prohibited. If false: tighten to explicitly approved stock only; expand across projects solely after written finance, contract and production approval.

## 4. Which options did you consider, and why did you pick the one you did?** What did you rule out, and why?*

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

## 5. How will the client know the pilot worked?** Metric, baseline, threshold, how many runs, who measures, and what result would make you stop.*

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

A measured improvement must have an uncertainty interval excluding zero before being called reproducible; otherwise the result is inconclusive. Proposed reconciliation tolerances are <=1% unexplained mass per job and <=0.5% pooled, subject to weighing precision. If the measurement uncertainty exceeds the expected improvement, fix measurement first. The prototype is not one of the client benchmark jobs; its synthetic result actually increases scrap despite opening less virgin stock.

## 6. What does this cost the client, and what does it cost us to deliver?** Show the arithmetic and name the pricing structure. What value does the client get, in their money?*

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

## 7. Timeline.** What is the first result the client sees, and when? Which steps depend on the client rather than on us?*

Hiring deadline: 48 hours after receipt, separate from this pilot. Verify the actual invitation deadline.

| When / stage | Output and delivery owner | Client dependency / gate |
|---|---|---|
| Week 1 / Stage 0 | FDE + Cost Control: preliminary loss/readiness report | Sponsor convenes owners; exports within three working days. Missing data: readiness only |
| Week 2 / Stage 1 | FDE + nesting lead: 30-job manual/native benchmark and business case | Valid releases, stock and native mode. Management/finance authorise USD 30k balance only with evidence |
| Weeks 3-4 / conditional Stage 2 | FDE + engineer: file-based offcut checks, loss classification, suggestions | Verified within-project stock and rules; technical-owner review |
| Week 5 | Operators + production: >=10 shadow jobs and acceptance report | Review capacity; feasibility checks before any execution |
| Week 6 | Cost Control + finance: economics, handover; up to five approved cuts | Production availability; management chooses native adoption, measurement, narrow rollout or stop |

Scope: one site, two exports, one profile family, bounded plate benchmark; 35 person-days across overlapping contributors. Client owners: 1-2 hours/week plus benchmark time. Access delays pause dates; extra integrations, geometry work or remediation require written change control. Stage 3 needs separate finance/contract/technical/production approval; follow reuse for 90 days.


The first useful finding is the week-1 readiness/loss report, not a software demo. We own ingestion, analysis and reports; the client owns source access, accurate releases, stock checks, native-tool access, operator availability, approval authority and production scheduling. The 48-hour assessment deadline is not the implementation timeline.

## 8. Where did you push back on the client, narrow their ask, or tell them not to do something?** **[can only raise your score]***

I narrowed an open-ended request for AI across nesting, revisions, warehouse/yard, trailers and equipment to measurement and existing-tool validation. The initial recommendation is USD 15,000 of discovery/native benchmarking, not an automatic USD 45,000 build. Equivalent native performance should end custom development and redirect effort toward settings, training and reporting.

I challenged the unverified 20-25% plate, 5-10% profile and 7-10% overall waste estimates and refused to turn 80,000 tonnes of reported capacity into verified annual input. I did not accept either operator superiority or automatic nesting superiority without matched evidence. I also rejected the premise that there is no offcut process: offcuts are already recorded and checked.

I excluded unapproved sharing because project-specific cost loading, ownership and contracts can prevent physically feasible allocation. I separated client revisions and internal engineering errors, with claim entitlement and payment requiring evidence. Reusable offcuts are inventory, not automatically scrap; simulated yield, reduced stock issues and realised cash are different outcomes.

I would not build a bespoke generative AI nesting engine, replace Strumis or PLM, issue unvalidated CNC instructions, buy major MLOps infrastructure or deploy an enterprise platform before baseline validation. Deterministic rules, existing heuristics and bounded optimisation are more appropriate first tools. A simple 1D prototype does not solve irregular 2D plates. CarTrack and booking information deserves a separate diagnostic before proposing equipment software or fleet changes.

This pushback creates a commercial obligation to stop when native tools suffice, data is unreliable, operators reject the workflow, production is disrupted or conservative net value is negative. It does not use the pilot to justify an already-decided software sale.

## 9. What is most likely to go wrong with your plan, and what in these notes did you not trust?** **[can only raise your score]***

The most likely failure is an unreconstructable matched baseline: missing historical inventory snapshots, incomplete release lineage or mixed definitions of scrap and offcuts. A second likely failure is that recorded offcuts are inaccessible, incorrectly identified, reserved or unavailable when needed. Software recommendations then become infeasible or merely move inventory accounting around. We quarantine incomplete records, reconcile mass, involve yard/engineering/operators early and stop at measurement repair when necessary.

I did not treat the waste percentages as audited facts or assume their periods and denominators match. The plate/profile mix can reconcile some combinations, but the notes supply no weighted mix. I did not accept 80,000 tonnes as actual annual raw input: call 2 calls it capacity, and 7,000-8,000 monthly would imply 84,000-96,000 annually. I did not infer geography, currency, steel prices, scrap realisation or client budget.

I did not trust the claim that manual outperforms automatic nesting without observing settings and equal constraints; the operator assertion comes through a contact who says he does not know nesting well. I did not equate offcuts being recorded/checked with complete inventory or effective reuse, nor treat checking offcuts for new projects as transfer approval. I did not interpret client revision losses as guaranteed recoverable cash or infer engineering-caused loss from missing records.

Low equipment utilisation and extra trailer hires can both occur because peaks, location, equipment type or booking quality differ; no fleet reduction claim is justified. Strumis export/API capabilities and PLM interfaces are unverified. Other significant risks are biased benchmark selection, stale drawings, grade/heat mismatch, machine infeasibility, operator review overhead, schedule disruption and confidential data exposure. The risk register assigns owners and specific pause/rollback rules.

A negative or inconclusive result is commercially acceptable. The actual synthetic example issues less virgin material but increases scrap: it is not a client saving and does not satisfy the proposed factory scrap target.

## 10. What did you use AI for?** Which tools, where they helped, where they misled you, and what you threw away.*

ChatGPT was used to structure the execution prompt. OpenAI Codex assisted with reading and organising both supplied sources, developing the business recommendation and assumptions, drafting the case study, management note and form, designing the evaluation and financial arithmetic, implementing the synthetic Python prototype and tests, generating PDFs and creating local validation/submission instructions. No independent client interviews, vendor access or real factory experiments occurred. No web research was used to establish vendor capabilities or market prices; those remain explicitly unverified or hypothetical.

Codex helped turn messy evidence into explicit decision gates and a reproducible, human-approved engineering scope. Its generated code and document layouts required execution and review, not trust. The first terminal launcher failed with a process-setup error, and Python was not on PATH. A local Node file/process interface and bundled Python runtime were used. The PDF artifact marker initially hit a Windows path-permission error and then succeeded with Node symlink-preservation flags. One later tool call timed out; the runtime was reinitialised and saved files inspected.

The first unittest invocation failed because three test modules imported src from the wrong package path. Imports were corrected; all 17 tests then passed. Initial PDF exports exceeded six pages (nine, then eight, then seven); those layouts were superseded by tighter prose and table spacing, retaining readable type and all required sections. The final PDFs are checked programmatically for page counts and content bounds and visually inspected after rendering. Financial values are recomputed by a Python model, and original-file hashes checked. A result-display callback also failed; its saved outputs were retrieved. Poppler logged missing Symbol/ArialUnicode display-font warnings; the rendered Helvetica pages were visually checked. These are local consistency checks, not independent business verification.

The synthetic assisted plan reduced virgin stock issued but increased scrap. That adverse result was retained and explained instead of presenting it as a savings win. No production-ready plate engine, invented Strumis API, external publication or fabricated repository URL was produced. No actual model hallucination or independent human editing is claimed where none was observed. The recommendation rejects an unsupported large AI build; that is a design decision, not a fabricated failed experiment.

## 11. Github Repo URL

Not yet created. No GitHub repository was created or pushed for this assessment. The local prototype is in prototype/. If a URL is required by the live form, use a separately reviewed synthetic-only repository, or a private access-controlled repository with employer reviewer access, subject to confidentiality approval. Do not publish the source notes or confidential submission materials.

