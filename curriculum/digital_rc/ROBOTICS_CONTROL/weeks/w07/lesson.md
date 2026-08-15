# Week 7: Diff-drive ICC — wheel speeds to body twist

Ticket RB-5707: wheel base B=0.40 m, r=0.05 m, wheel rates ω_l, ω_r. Compute v and ω_body.
Lab checks v, omega, and rejects if someone sets B=0.

Consensus Ladder: observed = encoder rates; inferred = ICC geometry; still need = slip
compensation. Wrong kinematics fail even if the cart 'looks right' on video.

Diff-drive: v=(r/2)(ω_l+ω_r), ω=(r/B)(ω_r−ω_l) with B>0. B=0 is rejected before any
division. Video of the cart without v/omega fields is insufficient evidence.

Slip compensation stays in 'still need'. Encoder rates come from the fixture, not from
invented fleet telemetry.

Derive RB-5707 v=(r/2)(ω_l+ω_r) and ω=(r/B)(ω_r−ω_l) with B=0.40, r=0.05 and reject B=0
before division. Publish finite v and omega from fixture encoder rates only. Video without
those fields is insufficient. Slip compensation remains still-need; invented fleet
telemetry is forbidden. Work a second numeric pair (ω_l=2.0, ω_r=2.4) on the whiteboard
and show how ω_body changes sign when the wheel rates swap, still with B>0 enforced.

## Worked example

v=(r/2)*(ω_l+ω_r); ω=(r/B)*(ω_r-ω_l).
