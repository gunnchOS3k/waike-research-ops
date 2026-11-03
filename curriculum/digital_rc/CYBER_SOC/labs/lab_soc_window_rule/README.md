# lab_soc_window_rule — Brute-force rule — threshold inside a sliding window

Choose an integer threshold and window_s. Report alerts as {source: first_alert_second} for FAIL_EVENTS. The grader replays the window with your parameters.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_window_rule --submission path/to/student.json

Common miss: Counting all failures ever, instead of those inside the window, flags 198.51.100.7 at 60 s.
