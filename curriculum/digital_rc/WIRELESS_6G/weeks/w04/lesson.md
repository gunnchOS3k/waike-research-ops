# Week 4: Link adaptation toy — MCS vs BLER on a fixture

Ticket WR-4404 gives BLER for MCS 0..4 at SNR=8 dB: [0.40,0.22,0.09,0.18,0.35]. Pick the
highest MCS with BLER ≤ 0.1 → MCS 2 at 0.09. Lab checks snr_db, bler_cap, chosen_mcs,
bler_at_choice.

Consensus Ladder: observed = table; inferred = higher MCS needs headroom; still need =
outer-loop CQI mapping (not claimed).

Failure mode: always max MCS for 'throughput.' Empty {} fails. PASS string raises.
Operators speak `fixtures/wr4404/bler_table.json` and defend the choice on a whiteboard.

Operators keep a numbered ticket trail for w4-lab_mcs_bler and refuse noun-swapped decks from other academies. Detail mark w4-lab_mcs_bler-0.

Whiteboard the worked numbers before opening any GUI; the validator grades fields, not vibes. Detail mark w4-lab_mcs_bler-1.

If a volunteer asks for a certificate selfie, point them at career_mapping.json: aligned, not granted. Detail mark w4-lab_mcs_bler-2.

Keep journals free of patron faces, passwords, and fabricated impact statistics. Detail mark w4-lab_mcs_bler-3.

## Worked example

SNR=8 dB, cap 0.1 → chosen_mcs=2 (BLER 0.09).
