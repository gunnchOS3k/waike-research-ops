# lab_ish_service_report — Refurb service report

labs_passed ≥ 6; every device has a fault class from the table, the fix, a sanitization method, and verification; customer_data_retained false.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_service_report --submission path/to/student.json

Common miss: A report without sanitization proof fails.
