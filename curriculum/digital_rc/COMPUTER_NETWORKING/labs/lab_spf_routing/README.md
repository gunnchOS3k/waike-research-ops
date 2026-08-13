# lab_spf_routing — Four-router town SPF

A-B-D costs 4. A-C-D costs 10. Submit cost_a_to_d=4 and path A-B-D.

## Student artifact
Keys: `cost_a_to_d, path`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_spf_routing --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_spf_routing --empty
```

Reporting 10 / A-C-D fails not_long_way.
