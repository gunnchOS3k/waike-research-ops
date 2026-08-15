# Week 8: State estimation toy — fuse odom + range with covariance honesty

Ticket RB-5808: scalar fuse x_odom and x_range with variances. Compute Kalman-ish gain
K = p/(p+r) and x_hat. Lab checks K, x_hat, and refuses cov_zero_lie=true.

Consensus Ladder: observed = two measurements; inferred = lower variance dominates;
still need = full EKF on SE2. Failure: claiming perfect certainty (P=0).

Scalar fuse uses K=p/(p+r) and refuses cov_zero_lie. Walk a numeric example with
p=0.04, r=0.01 and show how lower variance pulls x_hat. Full SE(2) EKF is not claimed
after this toy.

Finite K and two measurements are required; certainty theater fails honesty.

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 8: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

K=p/(p+r); x_hat = x_odom + K*(x_range-x_odom); no zero-cov lie.
