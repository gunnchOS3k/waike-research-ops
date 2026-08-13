# lab_backup — Checksummed civic archive

Hash the restored civic tree (ticket_4417.txt + notes.md). Submit SHA256. includes_ssn must be false. An empty hash or 64 zeros fails.

## Student artifact
Keys: `restored_hash, includes_ssn`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_backup --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_backup --empty
```

A hash that does not match the restored tree fails even if the tar exists.
