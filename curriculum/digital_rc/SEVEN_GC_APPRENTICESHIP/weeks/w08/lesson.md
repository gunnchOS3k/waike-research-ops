# Week 8: Digital-twin gap — comparison is not calibration

SGA-1808 confronts the gap the 7GC papers keep honest. A digital twin predicts received power across a site; the lab's twin gives -95, -97, -99 and -101 dBm at four points, and a separate reference simulator gives -94, -98, -100 and -103 dBm. The errors are -1, 1, 1 and 2 dB, their squares sum to 7, and the root-mean-square error is sqrt(7/4), about 1.32 dB. That number is useful: it says two models of the same site agree to roughly a decibel. It is not calibration. Calibration compares the twin with measurements from the real site, and in this course the count of field samples is zero. With zero measured samples the status must read UNCALIBRATED_NO_MEASUREMENTS and calibrated_claim must be false, however good the agreement looks. Two simulators can share the same wrong assumption, such as an optimistic clutter model, and agree perfectly while both miss reality. Paper I in the research spine records exactly this open gap. The apprentice's job is to state it clearly enough that the next cohort with radio access knows which measurements to collect.

## Worked example

twin − reference = [-1, 1, 1, 2] dB → RMSE = sqrt(7/4) = 1.3229 dB; measured_samples=0 → UNCALIBRATED_NO_MEASUREMENTS
