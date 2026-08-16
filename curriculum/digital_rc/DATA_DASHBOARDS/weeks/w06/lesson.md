# Week 6: Join integrity — keys that match

DL-3615 joins pier_visits to pier_meta on pier_bay. Orphan visit rows and duplicate meta keys fail. join_type must be inner or left with orphan_count reported honestly.

A dashboard that silently drops orphans without saying so fails the honesty gate.

Pier Ledger Bench ticket DL-3615 refuses screenshot-only evidence: the grader reads JSON fields from `lab_join_integrity`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.

Work the numbers for DL-3615 on paper before opening a GUI. Empty {} fails; a file whose body is only PASS raises.

Pier Ledger Bench ticket DL-3615 refuses screenshot-only evidence: the grader reads JSON fields from `lab_join_integrity`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

## Worked example

inner join on pier_bay; orphan_count=0 on fixture; duplicate_meta_keys=false.
