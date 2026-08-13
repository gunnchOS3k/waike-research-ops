# lab_dns_hosts — Split-horizon civic names

Answer desk/printer/library from the staff horizon. example.com must be nxdomain in this fixture resolver.

## Student artifact
Keys: `answers`.
An empty `{}` is a closed ticket with no work — it fails student_artifact.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Civic desk repo root, submit the operator JSON you actually filled in. Do not ask staff to run the reference store and call it yours.
```
python3 scripts/run_course_labs.py --lab lab_dns_hosts --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_dns_hosts --empty
```

Inventing 8.8.8.8 for example.com fails no_public_leak.
