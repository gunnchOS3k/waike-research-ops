# lab_secure_config_audit — Secure config audit vs Harbor baseline fixture

Audit fixture JSON only. live_scan must be false. No scanning of networks you do not own.

## Student artifact
Keys: `findings, severity_max, remediation, live_scan`.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_secure_config_audit --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_secure_config_audit --empty
```

## Safety
Defensive educational lab only. No malware, no exploit PoCs, no unauthorized access.

