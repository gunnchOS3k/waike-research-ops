# lab_forensics_timeline — USB fixture timeline

Sort by t. First event is login. You cannot claim a named human from this fixture.

## Student artifact
Keys: `first_event, cannot_claim_identity`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_forensics_timeline --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_forensics_timeline --empty
```

Claiming ada from the USB stick fails cannot_claim.
