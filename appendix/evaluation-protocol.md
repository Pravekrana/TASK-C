# Evaluation protocol - proposed acceptance contract

## 1. Register before seeing results

Cost Control owns the scorecard; finance owns monetary benefit; engineering certifies releases; yard certifies material identity and availability; nesting lead and production certify feasibility; IT approves data handling; management signs go/no-go. Record named delegates and approval authority at kickoff. Thresholds below are provisional until those owners accept them.

Choose a consecutive eligible window with >=30 jobs, targeting 15 plates and 15 profiles across >=3 projects. Pre-stratify mass, complexity and revision exposure. Publish all exclusions with reasons, original denominator and excluded mass. If this scope cannot support 30 reliable comparisons within the capped engagement, report readiness/inconclusive and agree any extension; do not replace missing cases selectively. There is no claim that n=30 gives sufficient power for any effect.

## 2. Freeze the counterfactual

Archive each manual plan as accepted at its original decision time. Freeze released geometry/revision, quantities, stock/offcut identities available then, ownership/reservations, machine rules, grade/section, heat restrictions, due dates and maximum planning effort. Do not give a historical algorithm access to future arrivals, later revisions or offcuts not yet created. Engineer and yard sign the snapshot. Missing historical availability is a disqualifier for retrospective efficacy, though a current shadow job may qualify separately.

On all 30 jobs, retain one manual plan and execute one native automatic plan: 60 primary plans. If the assisted arm is technically feasible, add one per job: 90 primary plans. Select 10 jobs for repeatability before running: repeat native and assisted twice more = 40 extra executions, 130 plans/executions including the 30 manual records. If two arms only, repeat native twice on 10 jobs = 20 extra, 80 total. First registered run is the primary result; no best-of-run selection. Log seeds/settings/version, elapsed machine time, operator setup and review time. Native operator receives the same constraints and a documented time budget. Manual historical effort may be unknown; then planning-time comparison uses shadow observations and is reported separately.

## 3. Feasibility before ranking

Demand must be fulfilled exactly once; lengths/geometries, grade/section, ownership, traceability, kerf, clamp/edge margins, orientation, rotations, cutting paths and machine-specific rules must hold. No overlap or duplicated stock use. Operators inspect candidates without financial ranking where practical; production retains unconditional stop authority. A rejected plan is recorded, not silently excluded to improve algorithm averages. Systemic infeasibility stops trials.

## 4. Measurement dictionary

- Scrap rate = total unrecoverable scrap/kerf kg divided by total issued input stock kg, including input offcuts, across eligible jobs. Calculate pooled totals and class-specific totals, not a mean of job percentages. Improvement in percentage points = 100 x (manual rate - candidate rate).
- Recoverable remnant rate = newly returned eligible remnant kg / issued stock kg. Reuse rate = physically verified reused kg from a dated cohort / original cohort kg within 90 days. Do not count repeated cycling of the same mass twice. Remnant creation is inventory, not realised cash.
- Virgin intensity = new stock kg issued net of uncut returns / good released-part kg. Show finished-output equality and opening/closing inventory. Gross stock issued is not the same as irreversible material consumption.
- Economic value = actually displaced purchases at marginal cost + incremental scrap proceeds - forgone salvage - extra handling, rework, planning and delay cost. Report paid revision claims separately. The USD 500/t scenario is a net-value proxy; do not add scrap or claims already embedded in it.
- Feasibility = complete feasible plans / all reviewed plans. Acceptance = operator-accepted candidates / eligible suggestions reviewed; rejected candidates remain in the denominator.
- Planning = candidate setup/review time minus comparable manual planning time; report median and p90 minutes/job and total labour cost. Schedule = pilot-attributed missed commitments / executed jobs; log downtime minutes and reason.

Stock mass is from verified weights or agreed dimensional calculations with measured variance. Proposed closure tolerances: <=1% unexplained input mass per job and <=0.5% pooled, subject to instrument precision and client agreement. Outside tolerance: investigate; no savings claim on that job. Weighing uncertainty must not exceed the expected improvement without a more precise measurement method.

## 5. Analysis and gates

Report paired raw deltas, pooled mass-weighted rates, per-class results and job-level bootstrap intervals with fixed seed 2026 and 10,000 resamples, recomputing ratios from sampled totals. Include project leave-one-out sensitivity because jobs may share inventory/teams; naive independence can understate uncertainty. Preserve negative outcomes. Require the interval for measured scrap improvement to exclude zero before claiming reproducible improvement; otherwise inconclusive, even if the point estimate exceeds target. Prospective sample-size expansion requires change control.

Proposed target: >=0.5 pp pooled absolute scrap improvement vs accepted manual; 100% of executed plans feasible/approved, zero grade/revision/traceability or quality failures; >=80% operator acceptance; median added planning <=10 min/job and p90 <=20; zero pilot-caused missed commitments/unplanned downtime. Net conservative benefit must be positive and at least USD 45k/year after recurring costs/friction for <=12-month simple operating payback. Native equivalence (within 0.1 pp with no material time/value difference) is an operational decision rule, not a statistical equivalence proof; agree what material economic difference means before testing. A custom assistant must beat the best existing approach in net value or a separately measured workflow outcome, not merely satisfy the manual comparison.

Week 2 is a decision to fund further validation, not production proof. Stop at native configuration if equivalent or better. Week 5 uses >=10 consecutive current shadow jobs, at least five of each in-scope class; evaluate all metrics with no live instruction. Week 6 allows up to five cuts only after lead/production approval. Mark retrospective, shadow and executed observations separately. Production result count can be zero if approvals or schedules do not permit; annual ROI remains unvalidated. Track 90-day reuse with named client owner or optional support.

## 6. Stop and recover

Stop expansion for insufficient reliable data, no reproducible manual improvement, equivalent native benefit, failed operator acceptance, negative conservative value, unauthorised transfer, infeasible cuts or unacceptable disruption. Quarantine record-level faults and invalidated approvals immediately. Restart only on corrected records/constraints and signed re-review. Disable candidate reporting and use the accepted manual/native process. Finance and Cost Control sign results; operational owners sign validity; management selects stop, improve measurement, adopt native or a separately authorised rollout.
