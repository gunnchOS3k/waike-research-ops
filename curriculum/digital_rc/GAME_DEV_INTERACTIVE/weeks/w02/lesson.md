# Week 2: AABB collision — overlap math before particle fireworks

Ticket GA-6202: two AABBs. Compute overlap on x and y; hit if both overlap. Lab checks
hit, overlap_x, overlap_y. Failure: particle VFX as 'proof' of collision without math.

Consensus Ladder: observed = rects; inferred = separating-axis for AABB; still need = swept
tests for tunnels. Empty fails.

Compute overlap_x and overlap_y explicitly; hit requires both positive. Particle VFX
cannot replace the arithmetic. Swept tests for tunneling stay in 'still need'.

Submit both rectangles and the overlap fields. Empty {} fails. Wrong signs fail.

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 2: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

hit = overlap_x and overlap_y; report both overlaps.
