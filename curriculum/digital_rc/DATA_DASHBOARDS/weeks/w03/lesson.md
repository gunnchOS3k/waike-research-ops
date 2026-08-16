# Week 3: Normalize and transform — clean before KPI

DL-3307 receives messy bay labels ('Bay-A', 'bay_a', 'BAY A'). Transform maps them to canonical bay_a before any KPI. Null headcounts drop; negatives drop. null_rate and negatives_dropped must be honest.

DATA_VIZ_BI might hide messy labels behind a legend; Pier Ledger refuses to chart until normalize_map covers every alias. Fabricating null_rate=0 while fixture shows nulls fails.

Pier Ledger Bench ticket DL-3307 refuses screenshot-only evidence: the grader reads JSON fields from `lab_normalize_transform`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.

Work the numbers for DL-3307 on paper before opening a GUI. Empty {} fails; a file whose body is only PASS raises.

Pier Ledger Bench ticket DL-3307 refuses screenshot-only evidence: the grader reads JSON fields from `lab_normalize_transform`.

## Worked example

Map three aliases→bay_a; drop null/negative headcounts; report null_rate and rows_out.
