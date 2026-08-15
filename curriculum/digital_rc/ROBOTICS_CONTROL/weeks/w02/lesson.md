# Week 2: 2R kinematics — reachability before torque myths

Ticket RB-5202: planar 2R arm with L1=0.35 m, L2=0.30 m. Forward kinematics to a target and
a reachability flag when hypot(x,y) > L1+L2. Lab checks x,y, reachable.

Consensus Ladder: observed = link lengths; inferred = workspace is an annulus/disk bound;
still need = joint limits map. Failure: claiming infinite reach because 'servos are strong.'

Operators keep a numbered ticket trail for w2-lab_fk_2r and refuse noun-swapped decks from other academies. Detail mark w2-lab_fk_2r-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w2-lab_fk_2r-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w2-lab_fk_2r-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w2-lab_fk_2r-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w2-lab_fk_2r-4.

## Worked example

L1=0.35, L2=0.30; point beyond 0.65 m → reachable=false.
