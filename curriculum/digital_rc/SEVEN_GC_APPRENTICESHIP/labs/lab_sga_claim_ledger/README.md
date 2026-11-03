# lab_sga_claim_ledger — Claim ledger — label every claim's evidence class

List at least three research claims. Label each SYNTHETIC_SIM, CITED_SPEC (with source_id), or MEASURED (with dataset_ref). affiliation_claim must be false.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_claim_ledger --submission path/to/student.json

Common miss: A MEASURED claim without dataset_ref, or affiliation_claim true, fails.
