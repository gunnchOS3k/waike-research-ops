# Week 8: Debug the pipeline — name the broken stage

DL-3822 pipeline failed: ingest→transform→calc→chart. Students name failed_stage, error_code, and fix_action. Guessing 'AI broke it' without a stage fails. Re-run evidence must show stage_rerun_ok true after the fix.

This is real tool-debug literacy for data operators.

Pier Ledger Bench ticket DL-3822 refuses screenshot-only evidence: the grader reads JSON fields from `lab_debug_pipeline`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.

Work the numbers for DL-3822 on paper before opening a GUI. Empty {} fails; a file whose body is only PASS raises.

Pier Ledger Bench ticket DL-3822 refuses screenshot-only evidence: the grader reads JSON fields from `lab_debug_pipeline`.

## Worked example

failed_stage=transform; error_code=NULL_HEADCOUNT; fix_action=drop nulls; stage_rerun_ok=true.
