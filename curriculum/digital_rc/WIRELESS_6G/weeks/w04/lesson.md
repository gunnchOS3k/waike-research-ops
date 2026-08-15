# Week 4: Link adaptation toy — MCS vs BLER on a fixture

Ticket WR-4404 gives BLER for MCS 0..4 at SNR=8 dB: [0.40,0.22,0.09,0.18,0.35]. Pick the
highest MCS with BLER ≤ 0.1 → MCS 2 at 0.09. Lab checks snr_db, bler_cap, chosen_mcs,
bler_at_choice.

Consensus Ladder: observed = table; inferred = higher MCS needs headroom; still need =
outer-loop CQI mapping (not claimed).

Failure mode: always max MCS for 'throughput.' Empty {} fails. PASS string raises.
Operators speak `fixtures/wr4404/bler_table.json` and defend the choice on a whiteboard.

Walk the BLER table left to right and mark every MCS whose BLER ≤ 0.1 before picking
the maximum eligible index. At SNR=8 dB the eligible set is {2}; chosen_mcs=2 with
bler_at_choice=0.09. Document why MCS 3 and 4 are rejected even if throughput stories
sound better in marketing.

Outer-loop CQI mapping stays in the 'still need' ladder rung — do not claim the pier
runs a live link-adaptation closed loop from this fixture alone.

## Worked example

SNR=8 dB, cap 0.1 → chosen_mcs=2 (BLER 0.09).
