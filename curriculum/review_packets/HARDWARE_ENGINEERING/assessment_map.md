# Assessment map — HARDWARE_ENGINEERING

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

- `curriculum/digital_rc/HARDWARE_ENGINEERING/assessments/final_knowledge.json`
- `curriculum/digital_rc/HARDWARE_ENGINEERING/assessments/final_practical.json`
- `curriculum/digital_rc/HARDWARE_ENGINEERING/assessments/mid_course.json`

## Assignments → deliverables

| Assignment | Deliverable | Gap |
|------------|-------------|-----|
| `a01.md` | SPICE network JSON and show handwritten KCL at the mid node | ok |
| `a02.md` | lab_thevenin | ok |
| `a03.md` | RC JSON; sketch V(t) and mark sample time safe after 3 tau | ok |
| `a04.md` | truth table JSON and one sentence on why NOR is not a drop-in | ok |
| `a05.md` | budget JSON and note which load dominates | ok |
| `a06.md` | parse JSON; contrast SPI mode 0 vs I2C ACK | ok |
| `a07.md` | west/QEMU JSON and paste sanitized run log excerpt | ok |
| `a08.md` | overlay JSON/text; explain one wrong delete-node | ok |
| `a09.md` | ERC/DRC/BOM JSON; attach export paths only (no paywall bypass) | ok |
| `a10.md` | diagnosis JSON + subsystem validation packet linking labs 5–9 | ok |

## Rubrics → criteria

| Rubric | Criteria count | Sample | Gap |
|--------|----------------|--------|-----|
| `HARDWARE_ENGINEERING-assignment.md` | 3 | numbers, physical_pending, ai_disclosure | ok |
| `HARDWARE_ENGINEERING-final-knowledge.md` | 2 | original_stems, zephyr_pcb_fail | ok |
| `HARDWARE_ENGINEERING-lab.md` | 5 | network_math, mpn_budget, qemu_west, erc_drc, empty_fails | ok |
| `HARDWARE_ENGINEERING-mid.md` | 2 | original_stems, divider_rc_bus | ok |
| `HARDWARE_ENGINEERING-portfolio.md` | 3 | bom_budget, qemu_log, no_ocw_copy | ok |
| `HARDWARE_ENGINEERING-practical.md` | 3 | computed_nets, negatives, print_pass | ok |
| `HARDWARE_ENGINEERING-project.md` | 3 | artifact_chain, no_fake_yield, embedded_integration | ok |
| `HARDWARE_ENGINEERING-quiz.md` | 2 | original_stems, key_hidden | ok |

## Capstone / portfolio

- Portfolio path: `curriculum/digital_rc/HARDWARE_ENGINEERING/portfolio/`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
