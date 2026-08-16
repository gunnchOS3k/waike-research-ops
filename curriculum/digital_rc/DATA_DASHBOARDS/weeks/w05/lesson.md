# Week 5: Dashboard chart contract — labeled axes

DL-3511 ships a chart contract JSON: chart_type, x_field, y_field, title, and alt_text ≥12 chars. Color-only encodings without labels fail. This is still Pier Ledger — the chart must cite the KPI fields from week 4, not invent a second dataset.

Distinct from DATA_VIZ_BI deep visual rhetoric: here the bar is machine-verifiable fields + a11y alt_text.

Pier Ledger Bench ticket DL-3511 refuses screenshot-only evidence: the grader reads JSON fields from `lab_dashboard_chart`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.

Work the numbers for DL-3511 on paper before opening a GUI. Empty {} fails; a file whose body is only PASS raises.

Pier Ledger Bench ticket DL-3511 refuses screenshot-only evidence: the grader reads JSON fields from `lab_dashboard_chart`.

## Worked example

bar chart; x=pier_bay; y=avg_headcount; alt_text describes bars; color_only=false.
