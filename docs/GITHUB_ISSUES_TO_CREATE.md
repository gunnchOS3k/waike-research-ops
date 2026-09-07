# GitHub Issues to Create — WAIKE Research Ops

## Issue 1: Review PhD application readiness doc

**Title:** Review PhD application readiness documentation for WAIKE research-ops

**Labels:** documentation, phd-application

**Body:**

Review `docs/PHD_APPLICATION_READINESS.md` for accuracy and completeness.

- [ ] Confirm repository role statement accurately describes WAIKE as workload generator
- [ ] Verify status reflects current state (concept-complete)
- [ ] Confirm all metrics are relevant to 6G service-continuity research
- [ ] Verify evidence list matches what actually exists in the repository
- [ ] Confirm "must not claim" list is complete and enforced
- [ ] Verify definition of done criteria are actionable

---

## Issue 2: Complete simulation fallback documentation

**Title:** Document simulation fallback strategy for WAIKE workload evaluation

**Labels:** documentation, simulation, phd-application

**Body:**

All WAIKE workload evaluations currently use synthetic traces. Document the simulation fallback strategy.

- [ ] Define synthetic workload generation methodology from curriculum activities
- [ ] Document how Learn, Mobile, Create, Sense, Community, Presentation, and Support profiles translate to simulation parameters
- [ ] Specify trace format and generation approach for each workload profile
- [ ] Confirm no real learner data is required for initial research phases
- [ ] Document path from simulation to real-world validation (ethics-gated)
- [ ] Align fallback strategy with connectivity workload mapping in `docs/connectivity-workload-mapping.md`

---

## Issue 3: Formalize ethics boundary for WAIKE learning data

**Title:** Formalize ethics boundary and data governance for WAIKE learning data

**Labels:** ethics, documentation, phd-application

**Body:**

Formalize the ethics boundary for all WAIKE-related data collection per `docs/ethics-gated-learning-data.md`.

- [ ] Confirm red-line statement covers all ethics-gated categories
- [ ] Verify gate conditions are appropriate for each data category (learner records, minors, schools, wearables, location, AI tutor logs)
- [ ] Document which research activities can proceed without ethics review
- [ ] Confirm fallback strategies exist for every gated data category
- [ ] Verify no implied collection of data from minors, schools, or vulnerable communities without review
- [ ] Align ethics boundary with `docs/phd-workload-role.md` non-negotiables

---

## Issue 4: Validate WAIKE metrics against 6G service-continuity scope

**Title:** Validate WAIKE workload metrics against 6G service-continuity research scope

**Labels:** metrics, documentation, phd-application

**Body:**

Validate that WAIKE-derived metrics (throughput, continuity, accessibility, mobility, handover, jitter, local edge latency, sync delay, haptics latency) are correctly scoped for 6G service-continuity research.

- [ ] Confirm each metric maps to at least one WAIKE workload profile
- [ ] Verify metrics are measurable via simulation or technical instrumentation
- [ ] Confirm no metric requires validated educational outcome data
- [ ] Cross-reference metrics with `docs/connectivity-workload-mapping.md` activity-to-metric table
- [ ] Verify metrics align with Communications Engineering PhD scope (not education PhD)
- [ ] Document any metrics that require additional definition or refinement

---

## Issue 5: Conduct red-line review across WAIKE documentation

**Title:** Red-line review of all WAIKE PhD application documentation

**Labels:** review, phd-application, ethics

**Body:**

Conduct a red-line review across all WAIKE PhD application readiness documents to ensure no overclaims.

- [ ] Review `docs/PHD_APPLICATION_READINESS.md` — no claim of validated curriculum or student results
- [ ] Review `docs/phd-workload-role.md` — WAIKE framed as workload generator, not dissertation
- [ ] Review `docs/connectivity-workload-mapping.md` — workload profiles are specifications, not validated measurements
- [ ] Review `docs/curriculum-status-matrix.md` — honest status, no implication of completion where draft
- [ ] Review `docs/ethics-gated-learning-data.md` — red-line statement enforced, no implied data collection
- [ ] Confirm no document claims community impact without evidence
- [ ] Confirm no document implies school partnerships are established
- [ ] Confirm curriculum is disclosed as draft/under development throughout
