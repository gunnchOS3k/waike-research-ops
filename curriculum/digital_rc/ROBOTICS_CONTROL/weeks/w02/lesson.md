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

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 2: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

L1=0.35, L2=0.30; point beyond 0.65 m → reachable=false.
