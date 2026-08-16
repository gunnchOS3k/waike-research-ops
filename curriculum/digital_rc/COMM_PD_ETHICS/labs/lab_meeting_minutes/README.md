# lab_meeting_minutes — meeting minutes

Runnable validator for lab_meeting_minutes. Empty/wrong/print-PASS fail. Harbor Desk Voice.

## Student artifact
Empty {} fails. PASS raises. Harbor Desk Voice ethics/PD fields must be honest.

## How to run
From the Harbor Desk Voice folder, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_meeting_minutes --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_meeting_minutes --empty
```

Wrong ethics/PD policy fields must fail.
