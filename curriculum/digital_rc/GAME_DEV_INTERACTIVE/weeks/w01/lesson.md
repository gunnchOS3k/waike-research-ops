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

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 1: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

dt=1/60; clamp frame_time; spiral_of_death_guard true.
