# Week 10: Quality + repro portfolio — hash the dashboard inputs

Capstone: ship a portfolio dashboard pack with cleaned CSV sha256, KPI snapshot, and a data-quality checklist (null_rate, negatives_dropped, freshness). Ticket CM-3A07 rejects portfolios that only contain a PNG with no hashes.

quality_ok when null_rate≤0.05, negatives_dropped=true, freshness_minutes≤15, csv_sha256 present.

quality_ok requires null_rate≤0.05, negatives_dropped=true, freshness_minutes≤15, and a csv_sha256. PNG-only portfolios without hashes are rejected.

Ship the checklist beside the dashboard pack. No PL-300 or Tableau credential claims — alignment labels only. No patron PII in screenshots.

Capstone is reproducibility under civic scrutiny: another analyst must rebuild the median story from your hash and script notes without calling you at midnight.

Week 10 close for DATA_VIZ_BI: ticket work ends when the lab JSON fields for `lab_repro_hash` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

null_rate=0.04, negatives_dropped=true, freshness=8, sha256 present → quality_ok.
