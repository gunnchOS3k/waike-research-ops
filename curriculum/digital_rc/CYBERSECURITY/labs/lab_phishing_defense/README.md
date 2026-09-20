# lab_phishing_defense — Phishing defense triage (defensive only)

Identify indicators and report_and_delete. Do not craft lures or harvest credentials.

## Student artifact
Keys: `indicators, action, report_path, no_credential_harvest`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_phishing_defense --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_phishing_defense --empty
```

no_credential_harvest=false fails.
