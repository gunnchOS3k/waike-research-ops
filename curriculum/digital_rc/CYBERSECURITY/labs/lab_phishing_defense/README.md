# lab_phishing_defense — Phishing defense on Harbor fixture mail

DEFENSIVE ONLY. Identify ≥2 indicators on fixture mail. Report — do not harvest credentials. No phishing kits.

## Student artifact
Keys: `indicators, action, report_path, no_credential_harvest`.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_phishing_defense --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_phishing_defense --empty
```

## Safety
Defensive educational lab only. No malware, no exploit PoCs, no unauthorized access.

