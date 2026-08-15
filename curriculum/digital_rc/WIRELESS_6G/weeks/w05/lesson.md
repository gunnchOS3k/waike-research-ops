# Week 5: NTN LEO delay honesty — light-time, not sci-fi maps

Ticket WR-4505: LEO altitude 550 km, slant ≈700 km. Light-time ≈ d/c; RTT ≈ 2*d/c.
c=3e8, d=7e5 → one_way≈2.333 ms, RTT≈4.667 ms. Not GEO-class (~250 ms). Lab fails if
geo_comparable=true or ntn_as_6g_standard=true.

Consensus Ladder: observed = altitude card; inferred = ms-class RTT for this toy slant;
still need = feeder/gateway scheduling (out of scope).

Marketing fail: 'global 6G NTN' heatmap with no delay math. No constellation sim downloads —
fixture arithmetic only while Stream A runs.

Operators keep a numbered ticket trail for w5-lab_ntn_delay and refuse noun-swapped decks from other academies. Detail mark w5-lab_ntn_delay-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w5-lab_ntn_delay-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w5-lab_ntn_delay-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w5-lab_ntn_delay-3.

## Worked example

d=700 km → one_way≈2.333 ms, RTT≈4.667 ms; geo_comparable=false.
