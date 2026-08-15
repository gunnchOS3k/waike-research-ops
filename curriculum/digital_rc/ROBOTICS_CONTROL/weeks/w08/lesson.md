# Week 8: State estimation toy — fuse odom + range with covariance honesty

Ticket RB-5808: scalar fuse x_odom and x_range with variances. Compute Kalman-ish gain
K = p/(p+r) and x_hat. Lab checks K, x_hat, and refuses cov_zero_lie=true.

Consensus Ladder: observed = two measurements; inferred = lower variance dominates;
still need = full EKF on SE2. Failure: claiming perfect certainty (P=0).

Scalar fuse uses K=p/(p+r) and refuses cov_zero_lie. Walk a numeric example with
p=0.04, r=0.01 and show how lower variance pulls x_hat. Full SE(2) EKF is not claimed
after this toy.

Finite K and two measurements are required; certainty theater fails honesty.

For RB-5808, compute K=p/(p+r) with p=0.04, r=0.01, form x_hat, and refuse cov_zero_lie.
Show how the lower-variance measurement pulls the estimate. State explicitly that full
SE(2) EKF is not earned by this scalar toy. Certainty theater (P=0) fails honesty.
Repeat with p=0.09, r=0.01 and note how K shrinks when prior variance rises, still
refusing any submission that asserts zero covariance as a lie flag.

Plot K versus r for fixed p=0.04 across r in {0.01,0.04,0.16} and write one sentence on why
cov_zero_lie cannot be true for any of those points on RB-5808.

## Worked example

K=p/(p+r); x_hat = x_odom + K*(x_range-x_odom); no zero-cov lie.
