# lab_soc_ioc_match — Indicator handling — hash, defang, match

Hash sample_text with SHA-256, defang the URL (hxxp, [.] in the host), and report whether either indicator is on the desk's IOC list.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_ioc_match --submission path/to/student.json

Common miss: A pasted hash or a clickable URL in the ticket fails.
