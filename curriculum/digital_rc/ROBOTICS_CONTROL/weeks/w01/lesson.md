# Week 1: HarborBot frames — SE(2) pose without cinematic hype

HarborBot Bay ticket RB-5101: a diff-drive cart on taped pier coordinates. Pose is (x,y,theta)
in meters/radians. Students compute a planar transform of a tool point and refuse 'AI nabbed
the box' stories without a frame diagram.

Lab checks x, y, theta, tool_x, tool_y after a yaw rotation. Empty {} fails. PASS raises.

Consensus Ladder: observed = tape origin and tool offset; inferred = rotation mixes x/y;
still need = wheel slip model (later). Accessibility: ASCII frame diagrams required in journals.

Operators keep a numbered ticket trail for w1-lab_se2_pose and refuse noun-swapped decks from other academies. Detail mark w1-lab_se2_pose-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w1-lab_se2_pose-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w1-lab_se2_pose-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w1-lab_se2_pose-3.

## Worked example

theta=π/2, tool offset (0.2,0) → tool maps to pier axes with sin/cos.
