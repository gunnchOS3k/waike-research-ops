# Week 6: Feature windows — telemetry that respects time

Feature engineering on EdgeForge is mostly windows. Ticket EF-2607 needs a 5-sample trailing mean of rssi_dbm before the classifier sees raw noise. You will compute rolling means on a length-12 series and refuse future leakage (a window that includes t+1 when predicting t).

Causal windows only look backward. The lab verifies your series and that uses_future is false.

Series [10,12,11,13,12,14,13,15,14,16,15,17]. Trailing mean at index 4 (0-based) with w=5 is mean(10,12,11,13,12)=11.6.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

w=5 at index 4 → mean(10,12,11,13,12)=11.6.
