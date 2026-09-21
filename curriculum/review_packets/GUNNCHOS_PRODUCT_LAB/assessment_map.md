# Assessment map — GUNNCHOS_PRODUCT_LAB

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

- `curriculum/digital_rc/GUNNCHOS_PRODUCT_LAB/assessments/final_knowledge.json`
- `curriculum/digital_rc/GUNNCHOS_PRODUCT_LAB/assessments/final_practical.json`
- `curriculum/digital_rc/GUNNCHOS_PRODUCT_LAB/assessments/mid_course.json`

## Assignments → deliverables

| Assignment | Deliverable | Gap |
|------------|-------------|-----|
| `a01.md` | lab_gpl_product_charter JSON for GPL-5101. Charter Device Lab product scope; no invented community numbers | ok |
| `a02.md` | lab_gpl_compat_matrix JSON for GPL-5202. Versioned compatibility check on accepted-main pair only | ok |
| `a03.md` | lab_gpl_checkout_flow JSON for GPL-5303. Model checkout FSM without opening unmerged device-os PRs | ok |
| `a04.md` | lab_gpl_compose_health JSON for GPL-5404. NO_AI week: digest pin and rollback pointer honesty | ok |
| `a05.md` | lab_gpl_privacy_bom JSON for GPL-5505. Privacy BOM digital inventory; no biometric claim | ok |
| `a06.md` | lab_gpl_guest_protocol JSON for GPL-5606. Guest agent protocol fields; obsolete click-collector rejected | ok |
| `a07.md` | lab_gpl_release_notes JSON for GPL-5707. Semver bump with explicit breaking_change false unless true | ok |
| `a08.md` | lab_gpl_ci_tokens JSON for GPL-5808. Report CI tokens; fabricated_green must be false | ok |
| `a09.md` | lab_gpl_dep_pin JSON for GPL-5909. NO_AI week: refuse preview SHA in accepted-main pin | ok |
| `a10.md` | lab_gpl_product_capstone JSON for GPL-5A10. Assemble gunnchOS product lab packet; do not merge device-os #103 | ok |

## Rubrics → criteria

| Rubric | Criteria count | Sample | Gap |
|--------|----------------|--------|-----|
| `GUNNCHOS_PRODUCT_LAB-assignment.md` | 3 | ticket_ids, no_pii, ai_disclosure | ok |
| `GUNNCHOS_PRODUCT_LAB-final-knowledge.md` | 2 | original_stems, capstone_boundary | ok |
| `GUNNCHOS_PRODUCT_LAB-lab.md` | 4 | machine_fields, no_key_leak, empty_fails, print_pass | ok |
| `GUNNCHOS_PRODUCT_LAB-mid.md` | 2 | original_stems, honesty | ok |
| `GUNNCHOS_PRODUCT_LAB-portfolio.md` | 3 | claim_boundary, machine_artifacts, career_map | ok |
| `GUNNCHOS_PRODUCT_LAB-practical.md` | 3 | student_json, negatives, print_pass | ok |
| `GUNNCHOS_PRODUCT_LAB-project.md` | 3 | capstone_flags, six_labs, no_key_leak | ok |
| `GUNNCHOS_PRODUCT_LAB-quiz.md` | 2 | original_stems, key_hidden | ok |

## Capstone / portfolio

- Portfolio path: `curriculum/digital_rc/GUNNCHOS_PRODUCT_LAB/portfolio/`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
