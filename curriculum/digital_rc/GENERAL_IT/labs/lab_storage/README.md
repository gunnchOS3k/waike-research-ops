# lab_storage — Civic volume free ratio

Compute free = size - used - reserved on the 256 GiB civic volume. Policy is 15% free. You must submit the ratio you computed; a guessed 0.50 fails.

## Student artifact
Keys: `size_bytes, used_bytes, reserved_bytes, free_ratio`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_storage --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_storage --empty
```

210+12 on 256 GiB is under 15% — do not mark pass.
