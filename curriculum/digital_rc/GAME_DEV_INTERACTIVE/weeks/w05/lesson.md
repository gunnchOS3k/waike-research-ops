# Week 5: Level data — JSON tiles with checksum, NO_AI

Ticket GA-6505: level JSON with width, height, tiles length = width*height, and sha256 of
canonical bytes. NO_AI week. Lab checks dims, len match, checksum_ok.

Consensus Ladder: observed = level file; inferred = checksum pins edits; still need =
streaming chunks. Failure: editor GUI screenshot as only artifact.

Level JSON: tiles length equals width*height; checksum pins canonical bytes.
NO_AI week. Editor GUI screenshots alone are not artifacts. Streaming chunks stay in
'still need'.

checksum_ok must be true only when the digest matches the canonical serialization.

For GA-6505, prove tiles.length == width*height and pin checksum to canonical bytes.
NO_AI week: hand-edit JSON; editor screenshots alone are not artifacts. Streaming chunks
stay still-need. checksum_ok is true only on digest match. Mutate one tile intentionally
and show checksum_ok flip to false before restoring the canonical bytes.

## Worked example

tiles len = width*height; checksum_ok true.
