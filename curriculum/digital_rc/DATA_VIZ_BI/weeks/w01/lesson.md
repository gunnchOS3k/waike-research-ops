# Week 1: Civic Metrics Studio — dirty rows before pretty charts

The Civic Metrics Studio in Ghana/Gary partnership hours starts with a dirty CSV of desk tickets: ticket_id, opened_at, closed_at, zone, wait_min. Ticket CM-3102 has 5% null wait_min and two impossible negatives. Cleaning is not optional décor — dashboards that average negatives invent 'negative waits' for the mayor.

You will compute null_rate and drop/impute policy in JSON. Pretty Power BI themes come later; this week refuses to chart garbage.

200 rows, 10 null wait_min → null_rate=0.05. Negatives must be dropped, not absolute-valued into fake success.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

200 rows, 10 nulls → null_rate=0.05; negatives dropped (not abs).
