# Week 4: Experiment design — question, variables, controls before any run

Ticket SGC-6404 forbids running the controlled experiment until the design JSON exists. Learners state a testable research question, hypothesis, independent variable, dependent variable, controls, confounds, and claim/evidence matching. Example teaching scaffold: IV=mcs_index, DV=bler, control=snr_db on the SIMULATED table — not a claim that Gary pier closed a live loop. Confound examples include seed leakage and unlabeled vendor CSV merges. NO_AI week: hand-author the design. Consensus Ladder: observed = design fields; inferred = one IV change is planned; still need = run artifacts next week. Designs that promise MEASURED_FIELD without EXTERNAL_FIELD_GATE fail honesty. Apprentices speak Consensus Ladder rungs out loud: observed, inferred, still-need. SIMULATED fixtures stay labeled until a MEASURED_HARDWARE capture replaces them. Mentor approval stays EXTERNAL_HUMAN_GATE; portfolios never invent signatures.

## Worked example

iv=mcs_index; dv=bler; control=snr_db; confound=seed_leak; claim_match=true
