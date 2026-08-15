# Week 1: Game loop — fixed dt honesty on Forge Arcade

Ticket GA-6101: fixed timestep dt=1/60 with accumulator pattern. Lab checks dt, steps,
spiral_of_death_guard=true when frame_time exceeds 0.25 s clamp. Variable rendering may
interpolate; simulation steps stay fixed.

Consensus Ladder: observed = clock card; inferred = fixed dt stabilizes physics; still need =
profiling on target handheld (PHYSICAL_PENDING). Failure: 'just use delta everywhere' without guard.

Operators keep a numbered ticket trail for w1-lab_game_loop and refuse noun-swapped decks from other academies. Detail mark w1-lab_game_loop-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w1-lab_game_loop-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w1-lab_game_loop-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w1-lab_game_loop-3.

## Worked example

dt=1/60; clamp frame_time; spiral_of_death_guard true.
