# lab_siem_triage — Harbor AUTH_FAIL bursts

Count failures. ada ≥ 3 is a burst. Your note must contain the word burst and must not contain attacker. Empty notes fail.

## Student artifact
Keys: `bursts, note`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_siem_triage --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_siem_triage --empty
```

A note that says 'ada is the attacker' fails no_attacker_word.
