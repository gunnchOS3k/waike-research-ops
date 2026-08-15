# Week 4: Trajectory limits — vmax/amax before cinematic paths

Ticket RB-5404: move 1.2 m with vmax=0.4 m/s and amax=0.5 m/s². Compute minimum time for a
trapezoid/triangle profile bound and reject path_ok if commanded speed exceeds vmax.

NO_AI week. Consensus Ladder: observed = limits card; inferred = time bounded by v/a;
still need = curvature limits. Failure: spline that ignores vmax 'because it looks smooth.'

Operators keep a numbered ticket trail for w4-lab_traj_limits and refuse noun-swapped decks from other academies. Detail mark w4-lab_traj_limits-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w4-lab_traj_limits-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w4-lab_traj_limits-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w4-lab_traj_limits-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w4-lab_traj_limits-4.

## Worked example

Distance 1.2 m, vmax 0.4, amax 0.5 → compute t_min; path_ok respects vmax.
