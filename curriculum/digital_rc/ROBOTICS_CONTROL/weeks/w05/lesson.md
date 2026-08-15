# Week 5: Sensor noise — mean/std and reject wild outliers

Ticket RB-5505: lidar range samples [1.01,1.00,0.99,1.02,3.50] m. Compute mean/std after
dropping values beyond 1.5×IQR or a hard gate >2.0 m. Lab checks cleaned_n, mean, outlier_dropped.

Consensus Ladder: observed = samples; inferred = 3.50 is outlier for pier aisle; still need =
calibrated bias. Failure: trusting raw max as truth.

Apply the hard gate (>2.0 m drop) to the lidar list and recompute mean on the cleaned
set. outlier_dropped must be true when 3.50 is removed. Trusting the raw maximum as
aisle truth fails sensing discipline.

Bias calibration remains a later ladder rung. Empty submissions fail student_artifact.

Clean RB-5505 lidar [1.01,1.00,0.99,1.02,3.50] with the >2.0 m hard gate, recompute mean
and cleaned_n, and set outlier_dropped true when 3.50 is removed. Show why trusting the
raw max as aisle truth breaks sensing discipline. Bias calibration stays on the still-need
rung; empty student_artifact still fails.

## Worked example

Drop 3.50; cleaned_n=4; mean≈1.005.
