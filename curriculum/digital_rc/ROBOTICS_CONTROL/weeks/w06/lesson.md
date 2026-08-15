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

Assert RB-5606 E-stop fields motors_disabled, brake_engaged, and resume_requires_human
as a triple-true contract. Contrast against a soft 'slow eventually' story that must fail.
Note that demo-video bypass is an ethics fail, and SIL certification is not claimed.
Keep the printable large-text E-stop sheet in the student packet path for tabletop drills.

## Worked example

motors_disabled, brake_engaged, resume_requires_human all true.
