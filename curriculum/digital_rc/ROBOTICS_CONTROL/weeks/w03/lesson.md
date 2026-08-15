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

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 3: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

Compute u_last from fixture gains; document anti-windup note.
