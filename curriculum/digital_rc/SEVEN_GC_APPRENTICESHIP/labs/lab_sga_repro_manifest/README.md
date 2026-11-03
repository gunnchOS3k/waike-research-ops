# lab_sga_repro_manifest — Reproducibility manifest — digest, seed, command, rerun

Record config_text and its sha256, an integer seed, the exact command, and two reruns of the metric. The grader recomputes the digest.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_repro_manifest --submission path/to/student.json

Common miss: A digest that does not match config_text, a non-integer seed, or reruns that differ fail.
