# Week 1: Schema first — ingest without inventing columns

Pier Ledger Bench opens with schema discipline, not a dashboard mock. Ticket DL-3101 drops a pier foot-traffic CSV into the desk warehouse. Before any chart, you declare table pier_visits with columns visit_id, pier_bay, ts_utc, headcount, and source_file — and you refuse invented columns like vibe_score that were never in the file.

Ingest means: count rows loaded, hash the source bytes, and record schema_version. Empty submissions fail. A submission that claims row_count without matching the fixture fails. DATA_VIZ_BI may later style the tile; this course owns the table contract first.

Pier Ledger Bench ticket DL-3101 refuses screenshot-only evidence: the grader reads JSON fields from `lab_schema_ingest`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

## Worked example

Declare pier_visits columns; load DL-3101 CSV; report row_count and sha256 of source.
