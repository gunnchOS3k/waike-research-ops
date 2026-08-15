# Week 5: Sensor noise — mean/std and reject wild outliers

Ticket RB-5505: lidar range samples [1.01,1.00,0.99,1.02,3.50] m. Compute mean/std after
dropping values beyond 1.5×IQR or a hard gate >2.0 m. Lab checks cleaned_n, mean, outlier_dropped.

Consensus Ladder: observed = samples; inferred = 3.50 is outlier for pier aisle; still need =
calibrated bias. Failure: trusting raw max as truth.

Apply the hard gate (>2.0 m drop) to the lidar list and recompute mean on the cleaned
set. outlier_dropped must be true when 3.50 is removed. Trusting the raw maximum as
aisle truth fails sensing discipline.

Bias calibration remains a later ladder rung. Empty submissions fail student_artifact.

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 5: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

Drop 3.50; cleaned_n=4; mean≈1.005.
