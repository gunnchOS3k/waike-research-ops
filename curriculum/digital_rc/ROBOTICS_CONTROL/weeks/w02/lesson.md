# Week 2: 2R kinematics — reachability before torque myths

Ticket RB-5202: planar 2R arm with L1=0.35 m, L2=0.30 m. Forward kinematics to a target and
a reachability flag when hypot(x,y) > L1+L2. Lab checks x,y, reachable.

Consensus Ladder: observed = link lengths; inferred = workspace is an annulus/disk bound;
still need = joint limits map. Failure: claiming infinite reach because 'servos are strong.'

Plot the reachable disk of radius L1+L2=0.65 m and mark a forbidden point beyond it.
Forward kinematics must report both Cartesian tip and reachable=false when outside.
Strong-servo myths do not enlarge the workspace.

Joint-limit maps stay in 'still need'. Learners defend L1/L2 numbers from the fixture
card, not from a cinematic robot trailer.

For RB-5202, compute tip pose at θ1=0.4 rad, θ2=−0.2 rad with L1=0.35, L2=0.30 and mark
reachable vs hypot(x,y)>0.65. Include a second target beyond the disk and show
reachable=false without inventing extra link length. Defend L1/L2 from the fixture card
only; cinematic reach claims are out of scope. Joint-limit maps stay listed under still-need.

## Worked example

L1=0.35, L2=0.30; point beyond 0.65 m → reachable=false.
