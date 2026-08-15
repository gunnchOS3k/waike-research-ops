# Week 6: Feature windows — telemetry that respects time

Feature engineering on EdgeForge is mostly windows. Ticket EF-2607 needs a 5-sample trailing mean of rssi_dbm before the classifier sees raw noise. You will compute rolling means on a length-12 series and refuse future leakage (a window that includes t+1 when predicting t).

Causal windows only look backward. The lab verifies your series and that uses_future is false.

Series [10,12,11,13,12,14,13,15,14,16,15,17]. Trailing mean at index 4 (0-based) with w=5 is mean(10,12,11,13,12)=11.6.

Causal windows look backward only. A trailing mean that includes t+1 when predicting t is future leakage dressed as smoothing. The lab’s uses_future flag must stay false.

Walk the length-12 RSSI series index by index. At index 4 with w=5 the mean is 11.6 — write the five addends. If your notebook prints a vector of NaNs for the first w-1 steps, that is expected; do not impute with future samples to 'make the plot pretty.'

Feature engineering here is operational: denoise before classify, preserve time, refuse lookahead. The journal names the window width and the forbidden future frame explicitly.

## Worked example

w=5 at index 4 → mean(10,12,11,13,12)=11.6.
