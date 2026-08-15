# lab_rag_redact — rag redact

Runnable validator for lab_rag_redact. Empty/wrong/print-PASS fail.

## Student artifact
Empty {} fails. PASS string raises.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the EdgeForge repo root, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_rag_redact --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_rag_redact --empty
```

Wrong numeric or policy fields must fail.
