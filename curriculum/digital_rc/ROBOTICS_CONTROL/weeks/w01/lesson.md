# Week 1: HarborBot frames — SE(2) pose without cinematic hype

HarborBot Bay ticket RB-5101: a diff-drive cart on taped pier coordinates. Pose is (x,y,theta)
in meters/radians. Students compute a planar transform of a tool point and refuse 'AI nabbed
the box' stories without a frame diagram.

Lab checks x, y, theta, tool_x, tool_y after a yaw rotation. Empty {} fails. PASS raises.

Consensus Ladder: observed = tape origin and tool offset; inferred = rotation mixes x/y;
still need = wheel slip model (later). Accessibility: ASCII frame diagrams required in journals.

Tape the pier origin, mark +x along the aisle, and sketch the tool offset arrow before
any code. With theta=π/2, show how the offset rotates into pier axes using cos/sin.
Journals without an ASCII frame diagram fail accessibility expectations for HarborBot.

Refuse 'AI nabbed the box' narratives that skip the SE(2) fields. Lab JSON must carry
x, y, theta, tool offsets, and mapped tool_x/tool_y that match the rotation math.

## Worked example

theta=π/2, tool offset (0.2,0) → tool maps to pier axes with sin/cos.
