# Week 2: OFDM numerology intuition — symbols without a fake 6G waveform

Ticket WR-4202 ships a toy OFDM numerology card: Δf=30 kHz, N_sc=12 subcarriers per PRB,
symbol duration ≈ 1/Δf ignoring CP. Pier operators compute PRB bandwidth = 12*30e3 = 360 kHz
for scheduling math — not a marketing badge.

One slot with 14 symbols at μ=1 is a teaching fixture, not a claim the pier ships Rel-18.
The lab asks for n_sc, delta_f_hz, prb_bw_hz, and symbol_duration_s. Empty JSON fails.
A print('PASS') string raises AssertionError.

Consensus Ladder: observed = numerology table; inferred = larger Δf shortens symbols;
still need = measured Doppler on the pier.

Failure mode: renaming the week '6G waveform lab' and pasting a vendor constellation
screenshot with no math. Cyclic prefix is a named omission this week — honesty is skill.

Draw one resource block as twelve vertical tones and mark Δf=30 kHz between them.
Compute PRB bandwidth again with μ=0 (15 kHz) as a contrast case: 12*15e3=180 kHz.
Write both results side by side so learners stop treating 'PRB' as a brand badge.

Call out the cyclic-prefix omission in one sentence: CP is real on air interfaces and
deliberately not scored this week. Anyone pasting a constellation PNG without
n_sc/delta_f_hz/prb_bw_hz/symbol_duration_s fields fails the lab contract.

## Worked example

PRB BW = 12×30e3 = 360000 Hz; T_sym ≈ 1/30000 ≈ 33.33 μs (no CP).
