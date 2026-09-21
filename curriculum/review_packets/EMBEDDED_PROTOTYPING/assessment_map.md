# Assessment map — EMBEDDED_PROTOTYPING

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

- `curriculum/digital_rc/EMBEDDED_PROTOTYPING/assessments/final_knowledge.json`
- `curriculum/digital_rc/EMBEDDED_PROTOTYPING/assessments/final_practical.json`
- `curriculum/digital_rc/EMBEDDED_PROTOTYPING/assessments/mid_course.json`

## Assignments → deliverables

| Assignment | Deliverable | Gap |
|------------|-------------|-----|
| `a01.md` | lab_ep_memory_map JSON for EP-4101. Map the nRF52840-class memory regions for ForgeSense subsystem firmware | ok |
| `a02.md` | lab_ep_gpio_contract JSON for EP-4202. Author GPIO contract JSON before any Zephyr pinmux call | ok |
| `a03.md` | lab_ep_i2c_timing JSON for EP-4303. SSD1306-class address 0x3C at 100 kHz with explicit NACK plan | ok |
| `a04.md` | lab_ep_spi_flash JSON for EP-4404. NO_AI week: hand-author SPI read frame fields | ok |
| `a05.md` | lab_ep_adc_scale JSON for EP-4505. Convert 12-bit ADC count to millivolts with stated vref | ok |
| `a06.md` | lab_ep_isr_vs_poll JSON for EP-4606. Choose ISR when edge latency must stay under 250 µs | ok |
| `a07.md` | lab_ep_zephyr_qemu JSON for EP-4707. west build -b qemu_cortex_m0; no board flash claim without EVT | ok |
| `a08.md` | lab_ep_dt_overlay JSON for EP-4808. Overlay enables &i2c1 and led0; deleting &soc is unsafe | ok |
| `a09.md` | lab_ep_sleep_mode JSON for EP-4909. NO_AI week: document wake source without inventing uA draw | ok |
| `a10.md` | lab_ep_subsystem_capstone JSON for EP-4A10. Assemble ForgeSense subsystem packet from prior lab digests | ok |

## Rubrics → criteria

| Rubric | Criteria count | Sample | Gap |
|--------|----------------|--------|-----|
| `EMBEDDED_PROTOTYPING-assignment.md` | 3 | ticket_ids, no_pii, ai_disclosure | ok |
| `EMBEDDED_PROTOTYPING-final-knowledge.md` | 2 | original_stems, capstone_boundary | ok |
| `EMBEDDED_PROTOTYPING-lab.md` | 4 | machine_fields, no_key_leak, empty_fails, print_pass | ok |
| `EMBEDDED_PROTOTYPING-mid.md` | 2 | original_stems, honesty | ok |
| `EMBEDDED_PROTOTYPING-portfolio.md` | 3 | claim_boundary, machine_artifacts, career_map | ok |
| `EMBEDDED_PROTOTYPING-practical.md` | 3 | student_json, negatives, print_pass | ok |
| `EMBEDDED_PROTOTYPING-project.md` | 3 | capstone_flags, six_labs, no_key_leak | ok |
| `EMBEDDED_PROTOTYPING-quiz.md` | 2 | original_stems, key_hidden | ok |

## Capstone / portfolio

- Portfolio path: `curriculum/digital_rc/EMBEDDED_PROTOTYPING/portfolio/`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
