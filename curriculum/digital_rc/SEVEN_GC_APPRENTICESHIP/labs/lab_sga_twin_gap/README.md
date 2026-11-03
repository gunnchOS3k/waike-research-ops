# lab_sga_twin_gap — Digital-twin gap — RMSE vs reference sim is not calibration

twin = [-95,-97,-99,-101] dBm, reference_sim = [-94,-98,-100,-103] dBm. Compute RMSE. With measured_samples = 0, status is UNCALIBRATED_NO_MEASUREMENTS and calibrated_claim false.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_twin_gap --submission path/to/student.json

Common miss: Calling a twin-vs-sim comparison calibrated fails.
