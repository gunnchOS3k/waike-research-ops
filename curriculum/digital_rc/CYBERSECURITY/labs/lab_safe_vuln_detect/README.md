# lab_safe_vuln_detect — Toy length-prefixed parser

targets must be exactly [course_ctf_fixture]. Opening a socket during the lab fails no_network. The safe parser must reject an oversize length byte. No shellcode, no campus nmap.

## Student artifact
Keys: `targets, safe_rejects_lie, honest_payload`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_safe_vuln_detect --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_safe_vuln_detect --empty
```

targets=['10.0.0.1'] fails no_network even if you did not connect.
