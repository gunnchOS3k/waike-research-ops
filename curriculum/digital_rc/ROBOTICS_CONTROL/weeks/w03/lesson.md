# Week 3: PID on a fixture plant — gains with anti-windup note

Ticket RB-5303: discrete PID on e=[1.0,0.6,0.2] with Kp=1.2, Ki=0.4, Kd=0.1, dt=0.1.
Compute u for the last step with simple rectangular integral and backward diff. Include
anti_windup_note length ≥8 when integral magnitude is large.

Consensus Ladder: observed = error series; inferred = D term reacts to slope; still need =
real motor plant ID. Empty fails. Wrong u fails.

Operators keep a numbered ticket trail for w3-lab_pid_step and refuse noun-swapped decks from other academies. Detail mark w3-lab_pid_step-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w3-lab_pid_step-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w3-lab_pid_step-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w3-lab_pid_step-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w3-lab_pid_step-4.

## Worked example

Compute u_last from fixture gains; document anti-windup note.
