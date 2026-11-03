# lab_soc_shift_metrics — Shift metrics — MTTD, MTTR, and the median that resists one bad night

From I1–I4 compute mean time to detect, mean time to resolve (from detection), and median time to detect, in minutes.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_shift_metrics --submission path/to/student.json

Common miss: Measuring resolution from occurrence, or swapping mean and median, fails.
