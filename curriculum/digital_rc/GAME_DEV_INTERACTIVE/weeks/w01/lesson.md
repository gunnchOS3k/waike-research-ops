# Week 1: Game loop — fixed dt honesty on Forge Arcade

Ticket GA-6101: fixed timestep dt=1/60 with accumulator pattern. Lab checks dt, steps,
spiral_of_death_guard=true when frame_time exceeds 0.25 s clamp. Variable rendering may
interpolate; simulation steps stay fixed.

Consensus Ladder: observed = clock card; inferred = fixed dt stabilizes physics; still need =
profiling on target handheld (PHYSICAL_PENDING). Failure: 'just use delta everywhere' without guard.

Implement the accumulator mental model: fixed dt=1/60, clamp spiral when frame_time
exceeds 0.25 s, keep spiral_of_death_guard true on the reference path. Variable render
interpolation is allowed; simulation steps stay fixed.

Handheld profiling remains PHYSICAL_PENDING. 'Just use delta everywhere' without a
guard fails the loop contract.

On GA-6101, simulate three frame_time samples (0.016, 0.040, 0.30) through the accumulator
with dt=1/60 and show when spiral_of_death_guard clamps. Keep simulation steps fixed while
allowing render interpolation. Handheld profiling stays PHYSICAL_PENDING; delta-everywhere
without a guard fails the loop contract.

## Worked example

dt=1/60; clamp frame_time; spiral_of_death_guard true.
