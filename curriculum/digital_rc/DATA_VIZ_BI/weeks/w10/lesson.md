# Week 10: Quality + repro portfolio — hash the dashboard inputs

Capstone: ship a portfolio dashboard pack with cleaned CSV sha256, KPI snapshot, and a data-quality checklist (null_rate, negatives_dropped, freshness). Ticket CM-3A07 rejects portfolios that only contain a PNG with no hashes.

quality_ok when null_rate≤0.05, negatives_dropped=true, freshness_minutes≤15, csv_sha256 present.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

null_rate=0.04, negatives_dropped=true, freshness=8, sha256 present → quality_ok.
