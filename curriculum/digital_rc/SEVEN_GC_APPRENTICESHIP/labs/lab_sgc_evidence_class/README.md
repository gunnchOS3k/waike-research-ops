# lab_sgc_evidence_class — evidence classification

Classify evidence snippets; pii_in_notes must be false.

execution_mode: LOCAL_SOFTWARE
evidence_class: SIMULATED

Empty {} fails. PASS raises. No fabricated mentor/field completion.

python3 scripts/run_course_labs.py --lab lab_sgc_evidence_class --submission path/to/student.json

Wrong/empty/print-PASS / fabricated field-mentor claims fail.
