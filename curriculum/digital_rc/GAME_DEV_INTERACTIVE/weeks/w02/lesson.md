# Week 2: AABB collision — overlap math before particle fireworks

Ticket GA-6202: two AABBs. Compute overlap on x and y; hit if both overlap. Lab checks
hit, overlap_x, overlap_y. Failure: particle VFX as 'proof' of collision without math.

Consensus Ladder: observed = rects; inferred = separating-axis for AABB; still need = swept
tests for tunnels. Empty fails.

Compute overlap_x and overlap_y explicitly; hit requires both positive. Particle VFX
cannot replace the arithmetic. Swept tests for tunneling stay in 'still need'.

Submit both rectangles and the overlap fields. Empty {} fails. Wrong signs fail.

Compute GA-6202 overlap_x and overlap_y for two axis-aligned boxes with deliberate miss and
hit cases; require both overlaps positive for hit. Particle VFX cannot replace the signs.
Swept tunneling tests remain still-need. Empty {} and wrong signs fail the lab. Include a
third rectangle pair where overlap_x>0 but overlap_y≤0 and mark hit=false with the arithmetic
written beside the boxes.

## Worked example

hit = overlap_x and overlap_y; report both overlaps.
