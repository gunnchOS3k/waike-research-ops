# lab_sga_leo_doppler — LEO Doppler upper bound from orbital speed

Compute v = sqrt(μ/(R+h)) with μ = 398600.4418 km³/s², R = 6371 km, then the bound f_d ≤ (v/c)·f_c in kHz. bound_is_upper must be true.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_leo_doppler --submission path/to/student.json

Common miss: Escape-speed guesses or treating the bound as a measured shift fail.
