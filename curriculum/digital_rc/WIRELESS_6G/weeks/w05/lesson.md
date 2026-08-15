# Week 5: NTN LEO delay honesty — light-time, not sci-fi maps

Ticket WR-4505: LEO altitude 550 km, slant ≈700 km. Light-time ≈ d/c; RTT ≈ 2*d/c.
c=3e8, d=7e5 → one_way≈2.333 ms, RTT≈4.667 ms. Not GEO-class (~250 ms). Lab fails if
geo_comparable=true or ntn_as_6g_standard=true.

Consensus Ladder: observed = altitude card; inferred = ms-class RTT for this toy slant;
still need = feeder/gateway scheduling (out of scope).

Marketing fail: 'global 6G NTN' heatmap with no delay math. No constellation sim downloads —
fixture arithmetic only while Stream A runs.

Recompute light-time with a second slant (650 km) so learners practice d/c without
memorizing one number. Compare both RTTs to a GEO-class ~250 ms figure and keep
geo_comparable=false. ntn_as_6g_standard remains false: NTN features in 5G-Advanced
talk are not a commercial standardized 6G ratification.

Refuse constellation-sim downloads while Stream A QEMU is active. Fixture milliseconds
are the graded artifact; heatmaps without delay math are marketing fails.

## Worked example

d=700 km → one_way≈2.333 ms, RTT≈4.667 ms; geo_comparable=false.
