# Week 5: Level data — JSON tiles with checksum, NO_AI

Ticket GA-6505: level JSON with width, height, tiles length = width*height, and sha256 of
canonical bytes. NO_AI week. Lab checks dims, len match, checksum_ok.

Consensus Ladder: observed = level file; inferred = checksum pins edits; still need =
streaming chunks. Failure: editor GUI screenshot as only artifact.

Level JSON: tiles length equals width*height; checksum pins canonical bytes.
NO_AI week. Editor GUI screenshots alone are not artifacts. Streaming chunks stay in
'still need'.

checksum_ok must be true only when the digest matches the canonical serialization.

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 5: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

tiles len = width*height; checksum_ok true.
