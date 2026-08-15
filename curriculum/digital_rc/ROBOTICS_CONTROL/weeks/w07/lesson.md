# Week 7: Diff-drive ICC — wheel speeds to body twist

Ticket RB-5707: wheel base B=0.40 m, r=0.05 m, wheel rates ω_l, ω_r. Compute v and ω_body.
Lab checks v, omega, and rejects if someone sets B=0.

Consensus Ladder: observed = encoder rates; inferred = ICC geometry; still need = slip
compensation. Wrong kinematics fail even if the cart 'looks right' on video.

Diff-drive: v=(r/2)(ω_l+ω_r), ω=(r/B)(ω_r−ω_l) with B>0. B=0 is rejected before any
division. Video of the cart without v/omega fields is insufficient evidence.

Slip compensation stays in 'still need'. Encoder rates come from the fixture, not from
invented fleet telemetry.

Ticket arithmetic checkpoint for ROBOTICS_CONTROL week 7: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

v=(r/2)*(ω_l+ω_r); ω=(r/B)*(ω_r-ω_l).
