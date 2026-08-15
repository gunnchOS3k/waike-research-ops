# Week 3: Audio clock — beat grid without pirated sample packs

Ticket GA-6303: BPM=120 → beat period 0.5 s. Map t=1.25 s to beat index and phase.
license_ok must be true; pirated_sample_pack=false.

Consensus Ladder: observed = BPM card; inferred = phase in [0,1); still need = device latency
calibration. Failure: cracked sample libraries in the portfolio.

BPM 120 → period 0.5 s. Map t=1.25 to beat_index=2 and phase=0.5. license_ok true and
pirated_sample_pack false are hard gates. Cracked sample libraries in the portfolio
fail the week regardless of beat math.

Device latency calibration remains unfinished; do not invent millisecond offsets.

Ticket arithmetic checkpoint for GAME_DEV_INTERACTIVE week 3: restate the worked example in your own symbols, list the JSON keys the lab will reject when missing, and name one claim you will not make (commercial standardized 6G, vendor cert grant, unmerged Product-Use dependency, or fabricated field trial). Defend the numbers on a whiteboard before submitting student JSON. Empty objects fail; a file whose body is only PASS raises. Keep prose specific to this week's fixture paths and ticket IDs rather than recycling another academy's nouns.

## Worked example

BPM 120 → period 0.5; t=1.25 → beat 2 with phase 0.5.
