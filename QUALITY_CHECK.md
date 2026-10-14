# Quality check - completed local assessment package

Completed 14 October 2026. This is an executed local engineering/document QA record, not independent validation of client data, financial assumptions or production performance.

## Actual execution results

Working directory: C:\Users\prave\Downloads\TASK C. Python executable: C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe. Python is not on PATH on the observed laptop.

Commands executed, in PowerShell-compatible form:

```powershell
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" prototype/run_demo.py
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m unittest discover -s prototype/tests -v
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts/financial_model.py
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts/build_pdfs.py
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" scripts/validate_submission.py
```

| Check | Actual result |
|---|---|
| Prototype execution | Exit 0; both strategies fulfil four synthetic parts, 119.8kg good output |
| Unit tests | 17 tests, OK; final recorded run 0.003 seconds; full output in prototype/results/test-results.txt |
| Synthetic material result | Virgin issues 120 -> 60kg; recoverable remnants 60.08 -> 0kg; scrap 0.12 -> 0.20kg. Scrap rate worsens 0.0667% -> 0.1667%. No claimed cash saving |
| Financial script | Exit 0; USD 31,050 internal cost, 31% margin, USD 160k base hypothetical gross, USD 99k full operating-year net, USD 80,538.46 kickoff-year net |
| Case-study PDF | Exactly 6 pages, pypdf verified |
| Client-note PDF | Exactly 1 page, pypdf verified |
| PDF bounds | All text within safe page bounds; minimum main text/table/diagram font >=8.3pt; body 9.5pt, note body 10.2pt |
| PDF text retention | Every authored paragraph and table cell found in exported text after punctuation/whitespace normalisation |
| Visual review | All six case pages and the note rendered and inspected; changed pages inspected again. No observed clipped/overlapping text, missing table cells or unreadable glyphs |
| Source preservation | Both original SHA-256 hashes unchanged; scripts/source-checksums.json |
| Required files | All 35 paths checked by validator exist and are nonempty; additional supporting files also exist |
| Form | All 11 original written fields in original order; copy-and-paste answers exactly match |
| Submission validator | PASS; detailed machine-readable result in scripts/validation-results.json |
| Confidentiality | No repository created, push, external upload or employer submission performed |

Rendering command used for visual inspection:

```powershell
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe" -scale-to 1500 -png submission/case-study.pdf tmp/pdfs/case
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe" -scale-to 1500 -png submission/client-note.pdf tmp/pdfs/note
```

## Actual problems and revisions

- The standard terminal launcher failed before source reading with a process-setup error. Both sources were then read completely through the available local Node filesystem interface. Child processes used bundled Python.
- The PDF skill operation marker initially hit a Windows path permission error, then succeeded with --preserve-symlinks and --preserve-symlinks-main. The marker was run successfully once before authoring.
- One tool call timed out; the local JavaScript runtime was reinitialised and persisted files inspected before proceeding. A separate result-display callback misuse was corrected by reading the stored results.
- First unittest run reported three import errors because src was not resolvable from the workspace root. Package imports were corrected; all 17 actual tests passed. No failing test was removed or waived.
- First case-study export had 9 pages, then intermediate revisions had 8 and 7. Prose/table spacing was tightened; final count is 6. The note stayed at one page and its body font was increased for readability. Initial layouts were superseded, not submitted.
- Poppler printed missing display-font warnings for Symbol and ArialUnicode but exited 0 and produced every image. Documents use Helvetica; visual inspection found no affected glyphs. Text extraction and safe-bound checks also passed.
- The synthetic assisted plan did not improve scrap. The adverse result and retained-inventory explanation are preserved in the results, tests and form disclosure.

## Sceptical operations-client review

The proposal does not ask production to trust an unverified optimiser. It keeps project ownership, release lineage, material compatibility and human approval as gates. Existing offcut practices and native automation are credited rather than ignored. A no-build recommendation is an acceptable paid outcome. No CNC instructions are generated; the manual/native workflow remains available. Low equipment utilisation is not treated as evidence that owned equipment can be removed.

The biggest practical limitation is reconstruction of the matched baseline. Thirty jobs is a minimum practical sample, not proof of statistical power. Current stock cannot be substituted for historical availability. Shadow and up to five cuts cannot establish annual savings. Ninety-day reuse must be followed by a named client owner or optional support. These limits are stated rather than concealed by a favourable annual model.

## Senior FDE interviewer review

The six-page case includes all ten requested sections, exactly five ranked questions with decisions/assumptions/contradictory-answer consequences, five options, end-to-end engineering, a matched evaluation, explicit stop gates, bottom-up internal cost, client fee, margin, sensitivities, milestones and risk owners. Form answers include pushback, potential failure and actual AI/tool use. Client note uses the same price, dates and gated recommendation.

Commercial sanity checks: first authorised exposure is USD 15k; conditional balance USD 30k; full margin 31%; downside full-year loss USD 55.5k; no guaranteed ROI. Gross annual value is labelled hypothetical and uses assumed input, not verified capacity. First operating year is separated from first year after kickoff. Offcut book value, salvage, claims and displaced purchases are not combined indiscriminately. The synthetic example demonstrates why a single 'yield' metric is insufficient.

## Completion checklist

- [x] Both source files fully read and preserved.
- [x] No invented client facts, names, approvals, historical data or supported Strumis API.
- [x] Native automation and operator objections evaluated.
- [x] Project cost boundaries, revision causes and material lineage addressed.
- [x] Exactly five ranked questions; major assumptions/evidence classified.
- [x] Complete architecture, data contracts, approvals, error recovery and permissions.
- [x] Matched inputs, sample size, run counts, measurement owners and metrics specified.
- [x] Success thresholds, failure conditions, shadow mode and go/no-go explicit.
- [x] Financial arithmetic executed; internal cost, price, running cost and value distinct.
- [x] Hypothetical annualisations, poor-ROI scenarios and first-year timing clear.
- [x] Timeline, early result and client dependencies concrete.
- [x] Risk likelihood, impact, mitigation, owners and stop/rollback conditions present.
- [x] Case <=6 pages; management note exactly 1 page; final visual inspection complete.
- [x] Every written form field answered; AI assistance and actual revisions disclosed.
- [x] Synthetic-only prototype runs; 17 tests pass; adverse result reported honestly.
- [x] Cross-document figures, gates and form copies checked.
- [x] All required deliverables exist; nothing published or submitted.

## Remaining review items for the candidate

Confirm the actual invitation deadline and live form limits; the copied timer is not authoritative. Review the proposal and disclosure so you can defend them in interview. Determine whether the GitHub URL field is mandatory in the live form; no repository exists. USD rates, 80k input assumption, material mix, loss rates, salvage values, opportunity size, client authority and integration capability remain provisional by design. No client or vendor access occurred. No real production tests were performed. The model and prototype cannot remove those uncertainties during this assessment window.
