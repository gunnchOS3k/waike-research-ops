# lab_ish_fault_isolation — Fault isolation — symptom to subsystem before any part swap

Classify tickets ISH-T1…T5 with the bench fault table and confirm replaced_parts_before_isolating is false.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_fault_isolation --submission path/to/student.json

Common miss: Replacing the motherboard for a reseat-able RAM fault fails.
