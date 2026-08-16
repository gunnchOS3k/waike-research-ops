# Week 9: Freshness SLA — stale tiles fail (NO_AI)

NO_AI walkthrough. DL-3925 enforces freshness_minutes ≤ 60 for pier dashboards. Stale data with sla_ok true fails. lag_minutes must be computed from watermark vs now_fixture.

Operators refuse to publish a 'live' tile when lag exceeds SLA.

Pier Ledger Bench ticket DL-3925 refuses screenshot-only evidence: the grader reads JSON fields from `lab_freshness_sla`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

Commercial 'AI dashboard magic' claims fail the claim boundary even when arithmetic is correct.

Keep PAN/SSN out of fixture CSVs. Fabricated citywide KPI lifts fail.

Work the numbers for DL-3925 on paper before opening a GUI. Empty {} fails; a file whose body is only PASS raises.

Pier Ledger Bench ticket DL-3925 refuses screenshot-only evidence: the grader reads JSON fields from `lab_freshness_sla`.

Distinct from DATA_VIZ_BI chart storytelling — this week owns schema, SQL, or pipeline honesty before any dashboard tile.

## Worked example

lag_minutes=12; sla_minutes=60; sla_ok=true; claim_live_when_stale=false.
