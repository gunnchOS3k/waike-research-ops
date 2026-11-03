# lab_dco_entropy — Password strength — bits from pool size and length

List at least three generation schemes with pool and length, compute bits = length × log2(pool), name the strongest, and set reuse_allowed and forced_rotation_without_cause to false.

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_entropy --submission path/to/student.json

Common miss: Scoring a dictionary word with symbol swaps as if it were random fails.
