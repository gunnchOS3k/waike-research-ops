# Objectives — DATA_DASHBOARDS

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: Schema first — ingest without inventing columns
  - Complete the week contract: Schema first — ingest without inventing columns.
  - Reproduce worked example: Declare pier_visits columns; load DL-3101 CSV; report row_count and sha256 of source.
  - Pier Ledger Bench opens with schema discipline, not a dashboard mock.
### Week 2: SQL SELECT with pier filters — honest predicates
  - Complete the week contract: SQL SELECT with pier filters — honest predicates.
  - Reproduce worked example: SELECT pier_bay, headcount FROM pier_visits WHERE headcount>40 AND hour>=18; filter_count matches fixture.
  - Ticket DL-3204 asks which bays exceeded headcount 40 after 18:00 UTC.
### Week 3: Normalize and transform — clean before KPI
  - Complete the week contract: Normalize and transform — clean before KPI.
  - Reproduce worked example: Map three aliases→bay_a; drop null/negative headcounts; report null_rate and rows_out.
  - DL-3307 receives messy bay labels ('Bay-A', 'bay_a', 'BAY A').
### Week 4: KPI calc — arithmetic before tiles (NO_AI)
  - Complete the week contract: KPI calc — arithmetic before tiles (NO_AI).
  - Reproduce worked example: avg=sum/n; p95 from sorted list; fabricated_lift=false.
  - NO_AI authorship week.
### Week 5: Dashboard chart contract — labeled axes
  - Complete the week contract: Dashboard chart contract — labeled axes.
  - Reproduce worked example: bar chart; x=pier_bay; y=avg_headcount; alt_text describes bars; color_only=false.
  - DL-3511 ships a chart contract JSON: chart_type, x_field, y_field, title, and alt_text ≥12 chars.
### Week 6: Join integrity — keys that match
  - Complete the week contract: Join integrity — keys that match.
  - Reproduce worked example: inner join on pier_bay; orphan_count=0 on fixture; duplicate_meta_keys=false.
  - DL-3615 joins pier_visits to pier_meta on pier_bay.
### Week 7: ETL PII redaction — desks keep secrets out
  - Complete the week contract: ETL PII redaction — desks keep secrets out.
  - Reproduce worked example: Redact emails/phones; redactionsions≥1; pii_remaining=false; biometric_claim=false.
  - DL-3718 ETL must redact email and phone from volunteer notes before warehouse load.
### Week 8: Debug the pipeline — name the broken stage
  - Complete the week contract: Debug the pipeline — name the broken stage.
  - Reproduce worked example: failed_stage=transform; error_code=NULL_HEADCOUNT; fix_action=drop nulls; stage_rerun_ok=true.
  - DL-3822 pipeline failed: ingest→transform→calc→chart.
### Week 9: Freshness SLA — stale tiles fail (NO_AI)
  - Complete the week contract: Freshness SLA — stale tiles fail (NO_AI).
  - Reproduce worked example: lag_minutes=12; sla_minutes=60; sla_ok=true; claim_live_when_stale=false.
### Week 10: Dashboard capstone — ship the ledger path
  - Complete the week contract: Dashboard capstone — ship the ledger path.
  - Reproduce worked example: labs_passed≥6; honesty flags true; fabricated_lift false; no_key_leak true.
  - DL-3A30 closes Pier Ledger Bench: labs_passed ≥6, schema_ok, kpi_ok, chart_ok, pii_ok, freshness_ok true, fabricated_lift false, no_key_leak true.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
