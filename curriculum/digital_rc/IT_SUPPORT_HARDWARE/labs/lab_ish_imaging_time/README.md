# lab_ish_imaging_time — Imaging a lab — unicast versus multicast

Compute minutes to push one image to N machines one at a time (unicast) and as one shared stream (multicast) at the given link efficiency.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_imaging_time --submission path/to/student.json

Common miss: Using bytes where the link is in bits is off by eight.
