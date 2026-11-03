# lab_sga_ntn_delay — NTN propagation delay — nadir one-way and round trip

For your chosen altitude_km compute one_way_ms = altitude / c and rtt_ms = 2 × one_way. State geometry = nadir.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_ntn_delay --submission path/to/student.json

Common miss: Reusing the LEO 600 km delay for a GEO altitude fails the recompute.
