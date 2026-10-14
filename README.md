# Client B FDE hiring assessment - confidential local package

Recommendation: approve measurement and a fair native-tool benchmark first; build narrow operator-approved assistance only if it adds measurable economic value. USD 15,000 first gate, USD 45,000 total conditional pilot cap, six weeks subject to readiness. All currency/volume/value assumptions are illustrative. No client savings, integrations or approvals are claimed.

## Contents

- submission/case-study.pdf and .md: six-page client-facing proposal.
- submission/client-note.pdf and .md: one-page management message.
- submission/submission-form.md: all eleven written fields in original order.
- submission/form-answers-copy-paste.md: individually marked answers.
- submission/prototype-results.md: actual synthetic result and tests.
- appendix/: architecture, contracts, evidence register, evaluation and financial model (Markdown plus executable JSON output).
- prototype/: standard-library Python demo, synthetic CSV, unit tests and audit output.
- scripts/: PDF builder, financial calculation, submission validator and original-source checksums.
- SUBMISSION_INSTRUCTIONS.md and QUALITY_CHECK.md: handoff and verification record.

The two original source files remain unmodified. Both were read completely. Notes are confidential. No Git repository was created and nothing was pushed, published, uploaded or submitted externally. .gitignore defaults to excluding everything except the synthetic prototype and its ignore policy; this is defence against accidents, not a substitute for reviewing a proposed commit.

## Run locally from this directory

Python 3.10+ is sufficient for the prototype. No external Python packages are needed for it.

```powershell
python prototype/run_demo.py
python -m unittest discover -s prototype/tests -v
python scripts/financial_model.py
python scripts/build_pdfs.py
python scripts/validate_submission.py
```

Python is not on PATH on the observed laptop. Replace python with:

```powershell
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
```

For example:

```powershell
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" prototype/run_demo.py
```

PDF build/validation needs reportlab, pypdf and pdfplumber, available in the bundled interpreter used here. On another machine, install these into a local virtual environment: python -m pip install -r scripts/requirements.txt. PDF rendering instructions are in QUALITY_CHECK.md. No Microsoft Word or LaTeX dependency.

## Interpretation

The financial model separates client value, internal cost, fee, support and client friction. USD 160k gross annual value is a hypothetical scenario, not a forecast. The prototype reduces stock issued but increases scrap and does not establish cash benefit. Existing auto-nesting, manual workflow improvement or better data may be the entire solution. Operational proof requires client records, signed constraints and a matched evaluation.

Read the PDFs and form before submission. No public sharing of sources or client-specific documents. The invitation link and true deadline are not in this workspace and must be checked personally.
