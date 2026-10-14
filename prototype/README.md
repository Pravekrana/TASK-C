# Synthetic 1D profile cutting and accounting demo

Purpose: show why material eligibility and inventory accounting matter before treating a cutting-layout improvement as money. This is a small standard-library Python 3.10+ demonstrator, not a production optimiser or a model of the client's actual manual/Strumis performance.

From the TASK C directory:

```powershell
python prototype/run_demo.py
python -m unittest discover -s prototype/tests -v
```

On this laptop Python is not on PATH. The verified bundled interpreter can be used instead:

```powershell
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" prototype/run_demo.py
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m unittest discover -s prototype/tests -v
```

No pip install is required. Paths to data/results are resolved relative to run_demo.py. Run the unittest command from TASK C. results/demo.json contains full assignments, row-level rejection reasons, remaining lengths and metrics; test-results.txt records the executed test output.

## Inputs and logic

All records are invented and marked by synthetic filenames. Each stock/offcut row represents one uniquely identified physical piece. Stock contract: id, project, grade, section, length_mm (positive integer), kg_per_m (positive finite number). Stock and offcut IDs share one namespace. Demand: id, project, grade, section, length_mm, quantity (positive integer). CSV parser rejects malformed numeric fields and missing headers; validator rejects duplicate IDs, blank eligibility fields and inconsistent densities for a grade/section family.

Both strategies check eligible offcuts first, recognising that the client's offcut process already exists. Baseline: demand input order, first-fit by file order within offcut/virgin priority. Assisted: descending part length, best-fit remaining space within the same priority. Ties use stable IDs; there is no random seed. Neither is globally optimal, and assisted can be worse. Negative results must remain visible.

Hard constraints: same project, exact grade/section, sufficient remaining length plus kerf. No cross-project override. A piece that cannot be allocated is rejected with a reason; complete=false blocks complete-demand metrics. Each produced piece consumes length + 3mm kerf, including a cut at the end; this conservative convention is explicit and does not model real sawing exceptions. Remaining length >=500mm is called recoverable solely for this demonstration, with no claim of future usability. Density converts mm to kg: mm/1000 x kg_per_m.

Metrics: issued input mass includes virgin stock and used existing offcuts; good part mass; virgin stock issued (net of no uncut returns in this example); kerf + sub-threshold tails as unrecoverable scrap; recoverable returned remnants; scrap/input ratio and virgin/good-part ratio. Unused stock is excluded from input and stays inventory. Do not confuse gross issued virgin mass with irreversible consumption or cash savings. For equal demand, both plans must conserve issued mass exactly within floating-point tolerance.

## Actual result and interpretation

Both plans fulfil four parts totalling 119.8kg. Baseline issues 120kg virgin plus 60kg existing offcut, returns 60.08kg recoverable remnants and produces 0.12kg scrap. Assisted issues 60kg virgin plus 60kg existing offcut, returns no recoverable remnant and produces 0.20kg scrap. One 60kg virgin piece remains unopened. Scrap rate worsens from 0.0667% to 0.1667%; there is no scrap-reduction success. The example demonstrates fewer opened stock pieces and a remnant fragmentation tradeoff, not realised money. The baseline's recoverable inventory cannot be written off to make the assisted result look better.

## Tests and limitations

17 unittest tests cover bad data, duplicates, ownership/grade/section restrictions, kerf boundary, exhausted stock, deterministic output, offcut-first behaviour, 27 small length combinations under both strategies, mass balance, incomplete-plan rejection, remnant threshold and the observed adverse scrap tradeoff.

No CAD, irregular 2D nesting, rotations, cut path, clamp margins, end trim, machine approval, released drawing lineage, heat/certificate checks, due dates, physical yard access, reservation concurrency, UI, integration, prices or financial optimisation is implemented. These remain required production gates in the proposal. Never send this output to CNC machinery. No real client data is included in this prototype directory.
