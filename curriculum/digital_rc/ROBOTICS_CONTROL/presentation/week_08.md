# Week 8: State estimation toy — fuse odom + range with covariance honesty

## Slide 1 — Hook
State estimation toy — fuse odom + range with covariance honesty

## Slide 2 — Worked example
K=p/(p+r); x_hat = x_odom + K*(x_range-x_odom); no zero-cov lie.

## Slide 3 — Lab contract
`lab_fuse_scalar` rejects empty/wrong/print-PASS.

## Speaker notes
Stay in ROBOTICS_CONTROL vocabulary. Do not noun-swap another academy's deck.
Assignment: Fuse RB-5808. Submit lab_fuse_scalar....
