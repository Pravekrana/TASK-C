# Data contracts - proposed, not verified vendor schemas

UTF-8 CSV; ISO-8601 timestamps with timezone; lengths mm, masses kg, currency explicit ISO code. Never infer project permission or material equivalence from similar text. Adapter mapping must be signed off using actual exports; these are our proposed canonical fields, not Strumis API fields.

| Entity / key | Required fields | Validation |
|---|---|---|
| Job / project_id + job_id | release_id, drawing_id, revision, status, due_at, material_class | Released status, valid project, immutable snapshot |
| Part / project + release + part_id | quantity, grade, section or thickness, length or geometry_ref + geometry_hash | Positive integer quantity; positive dimensions; geometry complete for intended nesting class |
| Stock / stock_id | project_owner, grade, section/thickness, length or shape, available_qty, location, status, reservation, measured_at | Unique physical identity; available and project eligible; no duplicated offcut also counted as stock |
| Lineage / stock_id | parent_stock_id for offcuts, heat_id/lot_id/certificate_ref where required | No cycles; required traceability complete; returned remainder receives a new ID |
| Constraint / machine + version | kerf_mm, margins, spacing, min_remnant, allowed_rotation, grain/orientation policy, clamp/path restrictions | Non-negative numeric limits; all applicable production rules signed off |
| Plan / run_id | job snapshot hash, stock snapshot hash, algorithm/version/settings, created_at, assigned parts and stock IDs | Complete demand exactly once; no grade/section/owner conflict or overlapping reservations |
| Review / event_id | run_id, reviewer role/ID, decision, reason, timestamp | Required approvers; source change invalidates approval |
| Actual / event_id | plan_id, source stock_id, cut time, good_part_kg, scrap_kg, offcut_id and kg, operator, cause_code | Mass balance within agreed weighing tolerance; duplicates blocked; unknown remains unknown |
| Value / project + date | currency, marginal displaced purchase_cost_per_t, scrap_realisation_per_t, handling cost, claim status | Finance attestation; paid vs claimed distinguished; consistent date and units |

Optional: photo URI, yard route, telemetry, supplier stock sizes and detailed cutting-path simulation. Heat/certificates, orientation and grain are conditional mandatory fields when the job requires them, never optional merely because a column is missing.

Example stock record (entirely synthetic): stock_id=S01, project_owner=P1, grade=S355, section=RHS100, length_mm=6000, available_qty=1, location=Y1, status=available. A production record would additionally need its applicable certificate, reservation status and attested measurement timestamp. Prototype contracts are intentionally smaller and documented separately.

Batch protocol: client exports to staging; retain bytes and SHA-256; validate schema version/units/types, uniqueness, foreign keys and cut feasibility; produce accepted/rejected counts; commit a fully valid batch atomically. Missing economics allows feasibility analysis but no value conclusion; missing actuals permits simulation only. Quarantined records are excluded visibly, not imputed. Fix source and reimport with a new run ID; keep the original failure history.

Mass equation per cutting event: issued stock kg = good cut parts kg + measured scrap/kerf kg + returned remnant kg + explicit variance kg. Plant stock equation: opening + receipts + authorised inward transfers - closing - outward transfers = consumed stock. Reconcile these against good output, scrap and other classified losses; avoid double-counting returned offcuts as both consumption and waste. Threshold proposal: unexplained variance <=1% per job and <=0.5% pooled; client metrology owners must validate scale precision before adopting it.

Cause codes: nesting/cut loss; client revision; internal engineering revision/error; damage/rework; inventory correction; recoverable return; unknown. Cause and recoverability are separate axes; finance determines recoverability of client claims.
