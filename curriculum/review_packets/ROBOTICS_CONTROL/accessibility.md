# Accessibility — ROBOTICS_CONTROL

## Repo principles (from ACCESSIBILITY_AND_LOW_COST.md)

1. Phone-first / hardware learners already own
2. Offline-first where possible
3. Low-bandwidth / synthetic paths documented
4. Plain-language docs; structured headings
5. No paywall on core learning path

## Track-specific checks

- Package UI/lab text must not rely on **color alone** for meaning (see SOFTWARE_BUILDER board pattern as reference quality bar).
- Instructor packet should state keyboard / low-vision alternatives when UI labs exist.
- Cost assumption: existing laptop; cloud optional; field hardware **opt-in**.

## Gaps to confirm in human review

- [ ] Student packet states real vs synthetic vs planned for any Device Lab / radio / robot gear
- [ ] Error messages in labs are human-readable
- [ ] Multilingual needs documented if campus requires them

Prerequisites (package): `{"course_id": "ROBOTICS_CONTROL", "required": ["Treat e-stop / safe-state as non-negotiable in every lab", "Digital-first: physical robot motion is out of scope unless EVT is scheduled"], "recommended": ["HARDWARE_ENGINEERING GPIO/I2C vocabulary"]}`
