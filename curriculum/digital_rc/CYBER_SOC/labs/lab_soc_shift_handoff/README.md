# lab_soc_shift_handoff — Shift handoff — open incidents, phases, metrics, boundaries

labs_passed ≥ 6; each open incident has an ATT&CK technique ID, a NIST SP 800-61 phase, and a next owner; MTTD/MTTR match the shift; no customer data, no offensive tooling.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_shift_handoff --submission path/to/student.json

Common miss: Free-text technique names, invented phases, or offensive tooling fail.
