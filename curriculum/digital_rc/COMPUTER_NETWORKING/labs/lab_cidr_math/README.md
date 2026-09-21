# lab_cidr_math — Pier /26 and /28

10.20.30.40/26 network is 10.20.30.0, not .40. Usable 62 and 14. This is bitwise work, not a GUI.

## Student artifact
Keys: `cases`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_cidr_math --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_cidr_math --empty
```

Using the host address as the network on /26 is the package negative.
