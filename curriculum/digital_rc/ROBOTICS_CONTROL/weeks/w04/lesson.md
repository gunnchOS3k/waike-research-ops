# Week 4: Trajectory limits — vmax/amax before cinematic paths

Ticket RB-5404: move 1.2 m with vmax=0.4 m/s and amax=0.5 m/s². Compute minimum time for a
trapezoid/triangle profile bound and reject path_ok if commanded speed exceeds vmax.

NO_AI week. Consensus Ladder: observed = limits card; inferred = time bounded by v/a;
still need = curvature limits. Failure: spline that ignores vmax 'because it looks smooth.'

For distance 1.2 m, vmax=0.4, amax=0.5, derive whether the profile is triangle or
trapezoid, then compute t_min. path_ok is false when cmd_speed exceeds vmax. Smooth
splines that ignore limits fail the NO_AI week.

Curvature limits are deferred. Whiteboard the numbers; screenshots of path planners
without t_min/path_ok fields do not pass.

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 4: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

Distance 1.2 m, vmax 0.4, amax 0.5 → compute t_min; path_ok respects vmax.
