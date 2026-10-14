# Executed prototype results - synthetic only

Executed locally on 14 October 2026 using Python at C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe. From C:\Users\prave\Downloads\TASK C:

```powershell
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" prototype/run_demo.py
& "C:\Users\prave\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" -m unittest discover -s prototype/tests -v
```

Demo exit code: 0. Tests: 17 passed, OK (final recorded run 0.003 seconds). Actual initial root-directory test invocation failed to import src in three test modules; package imports were corrected and the same discovery command rerun successfully. No failed tests were removed. Output: prototype/results/demo.json and prototype/results/test-results.txt.

| Metric | Baseline | Assisted |
|---|---|---|
| Complete demanded parts | 4 | 4 |
| Good part mass | 119.8kg | 119.8kg |
| Virgin stock issued | 120kg | 60kg |
| Existing offcut input | 60kg | 60kg |
| Total stock input | 180kg | 120kg |
| Recoverable returned remnants | 60.08kg | 0kg |
| Kerf mass | 0.12kg | 0.12kg |
| Unrecoverable scrap including short tails | 0.12kg | 0.20kg |
| Scrap/input | 0.0667% | 0.1667% |
| Opened stock pieces | 3 | 2 |

Both methods check offcuts first and prohibit cross-project/grade/section mismatches. The assisted descending-length best-fit method opens one fewer virgin piece. **It does not improve scrap:** scrap worsens by 0.10 percentage point and 0.08kg. The first-fit baseline's 60.08kg returned material remains recoverable inventory under the assumed 500mm rule, while the assisted method retains one unopened 60kg virgin piece. This cannot be booked as 60kg of saved purchases without subsequent inventory and consumption evidence. No price or cash benefit is assigned.

The transparent strategies are teaching comparators, not a substitute for the client's actual manual or Strumis plans. Tests demonstrate synthetic 1D eligibility, kerf and accounting consistency only. They do not validate irregular plates, real CNC constraints, plant data, statistical benefit, feasibility approvals or annual ROI. The example deliberately preserves the adverse metric rather than redefining waste to obtain a positive result.
