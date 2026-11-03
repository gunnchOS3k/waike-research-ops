# lab_ish_memory_bandwidth — Memory channels — slots decide bandwidth

From the transfer rate (MT/s) and the populated slots, count channels (distinct slot letters) and compute GB/s = MT/s × 8 × channels / 1000.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_memory_bandwidth --submission path/to/student.json

Common miss: Two sticks in A1 and A2 share one channel; claiming dual-channel fails.
