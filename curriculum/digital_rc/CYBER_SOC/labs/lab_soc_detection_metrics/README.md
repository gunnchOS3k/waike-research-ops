# lab_soc_detection_metrics — Detection quality — precision, recall, false-positive rate

Counts: TP 18, FP 42, FN 6, TN 934. Report precision, recall, false_positive_rate, alert volume, and needs_tuning (true when precision < 0.5).

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_detection_metrics --submission path/to/student.json

Common miss: Swapping precision and recall, or calling a 30%-precise rule healthy, fails.
