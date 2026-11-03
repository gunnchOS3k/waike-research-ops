# lab_soc_triage_queue — Triage queue — severity × asset criticality, then SLA due times

Order A1–A6 by severity weight × asset criticality (ties: earliest received) and give each alert's due minute (received + SLA).

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_triage_queue --submission path/to/student.json

Common miss: Sorting by severity alone puts the kiosk's critical alert first and fails.
