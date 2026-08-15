# Week 6: E-stop policy — hard interrupt beats soft hope

Ticket RB-5606: E-stop must assert motors_disabled=true, brake_engaged=true, and
resume_requires_human=true. Software 'slow down' without disable fails.

Consensus Ladder: observed = E-stop wiring card; inferred = safety power path; still need =
SIL certification (not claimed). Ethics: never bypass E-stop for a demo video.

Operators keep a numbered ticket trail for w6-lab_estop_policy and refuse noun-swapped decks from other academies. Detail mark w6-lab_estop_policy-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w6-lab_estop_policy-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w6-lab_estop_policy-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w6-lab_estop_policy-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w6-lab_estop_policy-4.

## Worked example

motors_disabled, brake_engaged, resume_requires_human all true.
