# lab_ish_psu_budget — Power supply budget — sum the parts, add 25% headroom, pick the smallest adequate unit

List at least four components with watts, total them, multiply by 1.25, and choose the smallest PSU from 450/550/650/750/850 W that covers it.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_psu_budget --submission path/to/student.json

Common miss: Buying a PSU equal to the raw total leaves no headroom and fails.
