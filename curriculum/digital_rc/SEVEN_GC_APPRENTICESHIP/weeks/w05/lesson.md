# Week 5: Controlled SIMULATED experiment — one permitted variable

Ticket SGC-6505 executes the week-4 design on the SIMULATED MCS/BLER table. Change only the permitted independent variable (mcs_index) while holding snr_db. Preserve raw artifact paths and label evidence_class=SIMULATED. Distinguish observation (table values) from inference (higher MCS needs headroom). Do not invent pier throughput. Auto-apply AI-RAN policies without human_gate language fail research ethics even in simulation. Consensus Ladder: observed = two JSON digests; inferred = DV moved with IV; still need = MEASURED_HARDWARE confirmation. Empty {} fails. Apprentices speak Consensus Ladder rungs out loud: observed, inferred, still-need. SIMULATED fixtures stay labeled until a MEASURED_HARDWARE capture replaces them. Mentor approval stays EXTERNAL_HUMAN_GATE; portfolios never invent signatures. Gary 7GC Research Desk tickets refuse vendor throughput theater without provenance. Repo SHAs and fixture hashes belong in journals before any slide deck claim.

## Worked example

baseline_mcs=2; trial_mcs=3; snr_db=8; evidence_class=SIMULATED; raw_preserved=true
