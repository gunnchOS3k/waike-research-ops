# lab_meeting_minutes — meeting minutes

PD-2718 minutes: attendees_count ≥2; parallel decisions/owners/due_dates arrays (≥2 each); pii_redacted true. Unequal array lengths fail. Patron PANs must not appear.

## Student artifact
Required keys: attendees_count, decisions, owners, due_dates, pii_redacted.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Publish redacted PD-2718 minutes with owners and due dates.
```
python3 scripts/run_course_labs.py --lab lab_meeting_minutes --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_meeting_minutes --empty
```

## Wrong submissions
Solo attendees, misaligned arrays, or pii_redacted false fail.
