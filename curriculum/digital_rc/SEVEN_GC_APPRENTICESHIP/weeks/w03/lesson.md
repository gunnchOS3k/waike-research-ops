# Week 3: Baseline reproduction — measurement literacy on SIMULATED fixtures

Ticket SGC-6303 runs a deterministic SIMULATED KPI window under fixtures/sgc_baseline/. Learners record command, python version, cwd, output digest, and evidence_class=SIMULATED. The fixture is labeled for replacement by MEASURED_HARDWARE later — never rename it as field measured. Variables and controls stay named: seed, window_id, kpi_names. Stochastic storytelling without a seed fails. Hashes must be 64 hex characters. Consensus Ladder: observed = fixture bytes; inferred = baseline reproducible locally; still need = pier SDR capture. Empty {} fails. print-PASS raises. Do not invent bler curves or beamforming gains beyond fixture fields. Apprentices speak Consensus Ladder rungs out loud: observed, inferred, still-need. SIMULATED fixtures stay labeled until a MEASURED_HARDWARE capture replaces them. Mentor approval stays EXTERNAL_HUMAN_GATE; portfolios never invent signatures. Gary 7GC Research Desk tickets refuse vendor throughput theater without provenance.

## Worked example

fixture=fixtures/sgc_baseline/kpi_window.json; evidence_class=SIMULATED; output_sha256_len=64
