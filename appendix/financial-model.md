# Financial model - USD illustration only

Executable source: scripts/financial_model.py; computed output: financial-model.json. No currency, plant geography, input tonnage, steel price, actual scrap proceeds, local salary rate or budget is established. Rates and amounts below are modelling choices, not quotations based on client procurement evidence. Confirm currency, tax, licences, travel, scope and client staff availability before acceptance.

## Units and value equation

T = annual raw input tonnes, not installed capacity or shipped tonnes. e = eligible share of input. d = absolute improvement as a fraction: 0.8 percentage points = 0.008, not 0.8 or 8%. v = marginal net economic value per avoided tonne, after displaced material and salvage opportunity cost. Gross proxy G = T x e x d x v. The proxy assumes an equal-output counterfactual; inventory and purchases must be reconciled to validate it. It is not an industrial yield model or a prediction.

At fixed good output Q, a more exact mass-only comparison is required input Q/(1-s), where s is the scrap fraction, assuming all other flows identical. Returned offcuts, stock restrictions and time-dependent reuse violate this simple model; use the event ledger. Do not claim both avoided input and increased output as separate benefits of the same metal. Retained offcuts have no immediate realised cash value.

A plausible USD 500/t illustration could be USD 800/t displaced purchase less USD 300/t forgone salvage; both prices are hypothetical. Extra handling/planning friction is deducted separately, never twice. Actual purchase displacement timing, residual offcut value and rework change this spread. Claim receipts are excluded from scenarios and tracked separately to avoid attributing revision recoveries to nesting.

## Scenarios and timing

| Case | Eligible tonnes | Delta | Net value/t | Recovered-equivalent t | Annual gross | Recurring net | Full operating-year net after pilot |
|---|---|---|---|---|---|---|---|
| Downside | 50,000 x 30% = 15,000 | 0.2 pp | 350 | 30 | 10,500 | -10,500 | -55,500 |
| Base | 80,000 x 50% = 40,000 | 0.8 pp | 500 | 320 | 160,000 | 144,000 | 99,000 |
| Upside | 80,000 x 70% = 56,000 | 1.2 pp | 600 | 672 | 403,200 | 382,200 | 337,200 |

Recurring net = gross - USD 6,000 support - friction (USD 15,000 downside/upside, USD 10,000 base). Full operating-year net subtracts USD 45,000 pilot fee. These are hypothetical 12 full operating months after enablement; all results are before tax/financing and exclude unspecified travel/vendor licences.

Kickoff-year base, with zero benefit for six weeks and full rate for 46 weeks: 160,000 x 46/52 - 45,000 - 6,000 - 10,000 = USD 80,538.46. Support and friction remain conservatively charged for a full year. This still assumes immediate steady-state adoption after six weeks; it is an optimistic timing convention, not a deployment commitment. A 50% realisation factor reduces base full-year net to 80,000 - 61,000 = USD 19,000; at 25% it is -USD 21,000.

## Internal delivery economics and fee

| Role/cost | Total calculation | Stage 0/1 | Conditional Stage 2 |
|---|---|---|---|
| FDE | 15 x 800 = 12,000 | 5 x 800 = 4,000 | 10 x 800 = 8,000 |
| Data/optimisation | 12 x 700 = 8,400 | 4 x 700 = 2,800 | 8 x 700 = 5,600 |
| Test/validation | 5 x 600 = 3,000 | 1 x 600 = 600 | 4 x 600 = 2,400 |
| Oversight | 3 x 1,000 = 3,000 | 1 x 1,000 = 1,000 | 2 x 1,000 = 2,000 |
| Infrastructure | 600 | 600 | 0 |
| Subtotal | 27,000 | 9,000 | 18,000 |
| 15% contingency | 4,050 | 1,350 | 2,700 |
| Internal cost | 31,050 | 10,350 | 20,700 |
| Client fixed fee | 45,000 | 15,000 | 30,000 |
| Delivery contribution | 13,950 | 4,650 | 9,300 |

35 person-days, including 11 in the first two weeks and 24 in the remaining four. Costs are loaded direct delivery assumptions, not company-wide net profit. Margin = (45,000 - 31,050)/45,000 = 31.0%. No contingency is added again to client price.

Payment: 7,500 kickoff + 7,500 acceptance of week-2 report + conditional 15,000 signed build gate + 10,000 shadow report acceptance + 5,000 handover = 45,000. Stage 2 is optional and requires a written decision; stopping after week 2 limits fees to 15,000. Acceptance is against agreed deliverables and honest evaluation, not a guaranteed positive savings result. Proposed review window: five working days, documented deficiencies corrected within scope; no implied acceptance from silence. New sites/connectors, geometry engines, significant data remediation or changed samples require written change control.

Support: optional USD 500/month with at most four support hours and lightweight approved hosting, no 24/7 SLA. Illustrative provider cost USD 300/month = USD 250 labour + USD 50 infrastructure; USD 200/month contribution before overhead. Client first-year vendor spend = 45,000 + 6,000 = 51,000. Base economic spend adds USD 10,000 client friction = 61,000. Actual mobilisation, licence, travel and tax costs beyond these allowances remain to be priced.

## Payback and break-even

Base simple operating payback = 45,000/(160,000 - 6,000 - 10,000) x 12 = 3.75 months. From kickoff add 6/52 x 12 = 1.3846 months: 5.13 months total. This amortises friction across the year; an upfront-heavy cost profile needs monthly cash-flow modelling. Downside recurring net is negative, so no payback.

First full-year break-even d = 61,000/(40,000 x 500) = 0.00305 = 0.305 pp. Recurring-only threshold = 16,000/(40,000 x 500) = 0.08 pp. With six-week delay: 61,000/(40,000 x 500 x 46/52) x 100 = 0.344783 pp. At the proposed 0.5 pp scrap threshold, base gross = USD 100,000, recurring net = USD 84,000, simple payback = 6.43 operating months. The financial gate still fails if low volume, salvage spread or handling changes those inputs.

## Sensitivity: full operating-year net, USD 500/t and USD 61k total spend

| Eligible t / delta | 0.2 pp | 0.5 pp | 0.8 pp | 1.2 pp |
|---|---|---|---|---|
| 15,000 | -46,000 | -23,500 | -1,000 | 29,000 |
| 40,000 | -21,000 | 39,000 | 99,000 | 179,000 |
| 56,000 | -5,000 | 79,000 | 163,000 | 275,000 |

Sensitivity holds all other assumptions fixed; it is not the three-scenario table. At base volume/delta, USD 250/t net spread produces USD 80,000 gross and USD 19,000 full-year net. Raising friction to USD 50,000 at base value reduces full-year net to USD 59,000. A 0.2 pp gain at 15,000 eligible tonnes is commercially unattractive: stop rather than hide this outcome.
