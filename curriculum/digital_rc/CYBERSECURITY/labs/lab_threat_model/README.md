# lab_threat_model — Defensive threat model for Harbor SIEM fixture

List assets, threats, controls. offensive_scope must be none.

## Student artifact
Keys: `asset, threats, controls, offensive_scope`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_threat_model --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_threat_model --empty
```

offensive_scope other than none fails.
