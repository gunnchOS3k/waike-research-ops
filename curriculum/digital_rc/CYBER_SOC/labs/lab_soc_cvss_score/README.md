# lab_soc_cvss_score — CVSS v3.1 base score from a vector string

Score at least two CVSS:3.1 vectors with the FIRST v3.1 equations and Roundup, and name each severity band.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_cvss_score --submission path/to/student.json

Common miss: Rounding to nearest instead of Roundup, or guessing 10.0, fails.
