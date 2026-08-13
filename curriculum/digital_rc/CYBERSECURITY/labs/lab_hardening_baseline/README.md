# lab_hardening_baseline — Harbor image baseline

No guest, no password SSH, unattended upgrades on, ports ⊆ {22,443}, home not 777, ai_agent_sudo false.

## Student artifact
Keys: `guest_login, ssh_password_auth, unattended_upgrades, open_ports, world_writable_home, ai_agent_sudo`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_hardening_baseline --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_hardening_baseline --empty
```

ai_agent_sudo true is an automatic baseline fail.
