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

On RB-5404, decide triangle vs trapezoid for 1.2 m with vmax=0.4 and amax=0.5, then compute
t_min from the chosen profile. Set path_ok false for any cmd_speed>vmax and explain the
reject in one sentence. NO_AI week: hand-derive on paper; GUI path screenshots without
t_min/path_ok fields do not pass. Curvature limits remain deferred.

## Worked example

Distance 1.2 m, vmax 0.4, amax 0.5 → compute t_min; path_ok respects vmax.
