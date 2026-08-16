# Week 2: SQL SELECT with pier filters — honest predicates

Ticket DL-3204 asks which bays exceeded headcount 40 after 18:00 UTC. You write a SELECT with WHERE pier_bay IN (...) AND headcount > 40 AND ts_utc >= '18:00', not a SELECT * dump pasted into Slack.

The lab grades predicate honesty: filter_count must equal the fixture answer, and sql_text must include WHERE. Omitting filters while claiming 'all busy bays' fails. This is database literacy for operators, not BI storytelling.

Pier Ledger Bench ticket DL-3204 refuses screenshot-only evidence: the grader reads JSON fields from `lab_sql_select`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.

Work the numbers for DL-3204 on paper before opening a GUI. Empty {} fails; a file whose body is only PASS raises.

## Worked example

SELECT pier_bay, headcount FROM pier_visits WHERE headcount>40 AND hour>=18; filter_count matches fixture.
