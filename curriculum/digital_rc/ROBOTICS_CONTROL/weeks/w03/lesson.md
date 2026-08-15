# Week 3: PID on a fixture plant — gains with anti-windup note

Ticket RB-5303: discrete PID on e=[1.0,0.6,0.2] with Kp=1.2, Ki=0.4, Kd=0.1, dt=0.1.
Compute u for the last step with simple rectangular integral and backward diff. Include
anti_windup_note length ≥8 when integral magnitude is large.

Consensus Ladder: observed = error series; inferred = D term reacts to slope; still need =
real motor plant ID. Empty fails. Wrong u fails.

Expand the PID step: integrate the error series with rectangular rule, form the
backward difference for D, and compute u on the last sample. When |integral| is large,
anti_windup_note must be a real mitigation sentence (≥8 characters), not an empty string.

Plant identification remains unfinished. Wrong u fails even if the motor 'sounds right'
on a phone video.

Walk RB-5303 with the full e series [1.0,0.6,0.2], accumulate rectangular integral, form
backward Δe/dt, and publish u for the last sample with Kp=1.2, Ki=0.4, Kd=0.1, dt=0.1.
When |integral| grows, anti_windup_note must name a mitigation (clamp, back-calculation)
in ≥8 characters. Wrong u fails even if a phone video of the motor looks smooth.

## Worked example

Compute u_last from fixture gains; document anti-windup note.
