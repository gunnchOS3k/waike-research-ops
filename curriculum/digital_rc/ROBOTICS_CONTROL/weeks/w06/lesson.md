# Week 6: E-stop policy — hard interrupt beats soft hope

Ticket RB-5606: E-stop must assert motors_disabled=true, brake_engaged=true, and
resume_requires_human=true. Software 'slow down' without disable fails.

Consensus Ladder: observed = E-stop wiring card; inferred = safety power path; still need =
SIL certification (not claimed). Ethics: never bypass E-stop for a demo video.

E-stop is hard: motors_disabled, brake_engaged, and resume_requires_human all true.
Soft 'slow down eventually' stories fail. Bypass for demo video is an ethics fail, not
a style choice. SIL certification is not claimed by this course.

Practice the printable large-text E-stop sheet path even when the cart is powered down
for the classroom tabletop.

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 6: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

motors_disabled, brake_engaged, resume_requires_human all true.
