# lab_nif_availability — Availability — redundant pair in series with single parts

A_pair = 1 − (1 − A1)(1 − A2); multiply by each serial part; downtime = (1 − A) × 525,600 minutes per year.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_availability --submission path/to/student.json

Common miss: Adding availabilities, or treating the pair as serial, fails.
