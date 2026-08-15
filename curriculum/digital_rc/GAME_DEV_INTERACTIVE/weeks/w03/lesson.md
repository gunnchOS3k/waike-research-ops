# Week 3: Audio clock — beat grid without pirated sample packs

Ticket GA-6303: BPM=120 → beat period 0.5 s. Map t=1.25 s to beat index and phase.
license_ok must be true; pirated_sample_pack=false.

Consensus Ladder: observed = BPM card; inferred = phase in [0,1); still need = device latency
calibration. Failure: cracked sample libraries in the portfolio.

BPM 120 → period 0.5 s. Map t=1.25 to beat_index=2 and phase=0.5. license_ok true and
pirated_sample_pack false are hard gates. Cracked sample libraries in the portfolio
fail the week regardless of beat math.

Device latency calibration remains unfinished; do not invent millisecond offsets.

Map GA-6303 t=1.25 at BPM 120 to beat_index and phase with period 0.5 s. Enforce
license_ok true and pirated_sample_pack false as hard gates. Cracked sample packs fail
regardless of beat math. Do not invent device-latency millisecond offsets this week.
Also map t=0.0 and t=2.0 and show beat_index continuity without claiming a DAW license.

## Worked example

BPM 120 → period 0.5; t=1.25 → beat 2 with phase 0.5.
