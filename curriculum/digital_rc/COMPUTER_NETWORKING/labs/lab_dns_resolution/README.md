# lab_dns_resolution — Stub then cache

First lookup walks auth (203.0.113.14). Second is cache.

## Student artifact
Keys: `first_how, second_how, ip`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_dns_resolution --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_dns_resolution --empty
```

Calling the first hit a cache miss-order fails.
