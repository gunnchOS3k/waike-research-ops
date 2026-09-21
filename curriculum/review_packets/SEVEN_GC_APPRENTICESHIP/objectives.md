# Objectives — SEVEN_GC_APPRENTICESHIP

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: Research apprenticeship intuition — vocabulary, safety, claim boundaries
  - Complete the week contract: Research apprenticeship intuition — vocabulary, safety, claim boundaries.
  - Reproduce worked example: classes=[SIMULATED,DIGITAL_REPRODUCTION,MEASURED_HARDWARE,MEASURED_FIELD,HUMAN_REVIEW]; pii_in_notes=false
  - At the Gary 7GC Research Desk, week 1 is ticket SGC-6101: name what kind of evidence you hold before arguing about AI-RAN gains.
### Week 2: Tools setup — repository reconnaissance without hardware
  - Complete the week contract: Tools setup — repository reconnaissance without hardware.
  - Reproduce worked example: repo_id=waike-research-ops; purpose=reproducible_research_map; has_tests=true; evidence_path=results/
  - Ticket SGC-6202 teaches repo navigation as research skill.
### Week 3: Baseline reproduction — measurement literacy on SIMULATED fixtures
  - Complete the week contract: Baseline reproduction — measurement literacy on SIMULATED fixtures.
  - Reproduce worked example: fixture=fixtures/sgc_baseline/kpi_window.json; evidence_class=SIMULATED; output_sha256_len=64
  - Ticket SGC-6303 runs a deterministic SIMULATED KPI window under fixtures/sgc_baseline/.
### Week 4: Experiment design — question, variables, controls before any run
  - Complete the week contract: Experiment design — question, variables, controls before any run.
  - Reproduce worked example: iv=mcs_index; dv=bler; control=snr_db; confound=seed_leak; claim_match=true
  - Ticket SGC-6404 forbids running the controlled experiment until the design JSON exists.
### Week 5: Controlled SIMULATED experiment — one permitted variable
  - Complete the week contract: Controlled SIMULATED experiment — one permitted variable.
  - Reproduce worked example: baseline_mcs=2; trial_mcs=3; snr_db=8; evidence_class=SIMULATED; raw_preserved=true
  - Ticket SGC-6505 executes the week-4 design on the SIMULATED MCS/BLER table.
### Week 6: Industry/vendor reality — standards vs products vs your fixture
  - Complete the week contract: Industry/vendor reality — standards vs products vs your fixture.
  - Reproduce worked example: vendor_claim=6G ready; fixture_supports=false; commercial_6g_exists=false; docs_cited=true
  - Ticket SGC-6606 is documentation literacy week.
### Week 7: Research frontier + ethics — claim audit and validity limits
  - Complete the week contract: Research frontier + ethics — claim audit and validity limits.
  - Reproduce worked example: supports=['local_sim_delta']; does_not_support=['field_bler','mentor_signoff']; human_gate=EXTERNAL_HUMAN_GATE
  - Ticket SGC-6707 is the claim-audit week.
### Week 8: Digital capstone package — reproducible research without mentor fiction
  - Complete the week contract: Digital capstone package — reproducible research without mentor fiction.
  - Reproduce worked example: labs_passed>=6; mentor_signed=false; evidence_class=SIMULATED; includes_limitations=true
  - Ticket SGC-6808 assembles the digital course capstone: research question, environment, provenance, method, fixture description, result digests, limitations, SIMULATED/DIGITAL_REPRODUCTION labels, README, evidence hashes,
### Week 9: Apprenticeship extension — cross-repo map and clean handoff
  - Complete the week contract: Apprenticeship extension — cross-repo map and clean handoff.
  - Reproduce worked example: independent_repro=true; map_rows>=3; unavailable_ok=true; mutated_prod=false
  - Ticket SGC-6909 starts the 12-week apprenticeship extension digitally: a clean independent invocation reproduces the baseline digest, and learners map at least three entries from course_repo_map.yaml (digital twin, AI-RA
### Week 10: Robustness iteration — sensitivity without fabricated field gains
  - Complete the week contract: Robustness iteration — sensitivity without fabricated field gains.
  - Reproduce worked example: snr_db_variants=[6,8,10]; claim_stable=false_unless_documented; field_gain_invented=false
  - Ticket SGC-6A10 iterates the controlled experiment across snr_db variants on the SIMULATED table.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
