# lab_sga_oran_loops — O-RAN control loops — real-time, near-RT RIC, non-RT RIC

Classify at least three tasks by loop latency: <10 ms real_time, 10 ms–1 s near_real_time (xApp), ≥1 s non_real_time (rApp). The A1 policy target is near_rt_ric.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_oran_loops --submission path/to/student.json

Common miss: Putting rApp training in the real-time loop or targeting A1 at the DU fails.
