# Week 7: Diff-drive ICC — wheel speeds to body twist

Ticket RB-5707: wheel base B=0.40 m, r=0.05 m, wheel rates ω_l, ω_r. Compute v and ω_body.
Lab checks v, omega, and rejects if someone sets B=0.

Consensus Ladder: observed = encoder rates; inferred = ICC geometry; still need = slip
compensation. Wrong kinematics fail even if the cart 'looks right' on video.

Operators keep a numbered ticket trail for w7-lab_diff_drive and refuse noun-swapped decks from other academies. Detail mark w7-lab_diff_drive-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w7-lab_diff_drive-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w7-lab_diff_drive-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w7-lab_diff_drive-3.

When tools disagree, name the observation first, then the inference, then what is still needed. Detail mark w7-lab_diff_drive-4.

## Worked example

v=(r/2)*(ω_l+ω_r); ω=(r/B)*(ω_r-ω_l).
