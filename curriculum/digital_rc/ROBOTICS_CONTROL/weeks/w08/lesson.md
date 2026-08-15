# Week 8: State estimation toy — fuse odom + range with covariance honesty

Ticket RB-5808: scalar fuse x_odom and x_range with variances. Compute Kalman-ish gain
K = p/(p+r) and x_hat. Lab checks K, x_hat, and refuses cov_zero_lie=true.

Consensus Ladder: observed = two measurements; inferred = lower variance dominates;
still need = full EKF on SE2. Failure: claiming perfect certainty (P=0).

Operators keep a numbered ticket trail for w8-lab_fuse_scalar and refuse noun-swapped decks from other academies. Detail mark w8-lab_fuse_scalar-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w8-lab_fuse_scalar-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w8-lab_fuse_scalar-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w8-lab_fuse_scalar-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w8-lab_fuse_scalar-4.

## Worked example

K=p/(p+r); x_hat = x_odom + K*(x_range-x_odom); no zero-cov lie.
