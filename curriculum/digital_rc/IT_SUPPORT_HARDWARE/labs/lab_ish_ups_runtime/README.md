# lab_ish_ups_runtime — UPS runtime — watt-hours, inverter efficiency, load

runtime_min = Wh × efficiency / load × 60. Schedule graceful shutdown no later than 80% of that runtime.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_ups_runtime --submission path/to/student.json

Common miss: Ignoring inverter loss, or shutting down at the last minute, fails.
