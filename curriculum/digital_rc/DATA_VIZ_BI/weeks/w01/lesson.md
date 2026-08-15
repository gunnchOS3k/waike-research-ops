# Week 1: Civic Metrics Studio — dirty rows before pretty charts

The Civic Metrics Studio in Ghana/Gary partnership hours starts with a dirty CSV of desk tickets: ticket_id, opened_at, closed_at, zone, wait_min. Ticket CM-3102 has 5% null wait_min and two impossible negatives. Cleaning is not optional décor — dashboards that average negatives invent 'negative waits' for the mayor.

You will compute null_rate and drop/impute policy in JSON. Pretty Power BI themes come later; this week refuses to chart garbage.

200 rows, 10 null wait_min → null_rate=0.05. Negatives must be dropped, not absolute-valued into fake success.

Cleaning is a publish gate. CM-3102’s 10 nulls in 200 rows are a 0.05 null_rate; two negative waits are invalid measurements, not clever outliers to abs() into success.

Decide drop vs impute in writing before you open a charting tool. Imputing zero for null wait_min invents instantaneous service and will be read as propaganda by the mayor’s staff.

Studio rule: no theme packs, no Power BI wallpaper, until null_rate and negatives_dropped are honest in lab_clean_nulls. Pretty lies fail harder than ugly truths.

## Worked example

200 rows, 10 nulls → null_rate=0.05; negatives dropped (not abs).
