# lab_accessibility_comm — accessibility communication

PD-2925 accessible professional communication (NO_AI walkthrough). captions, plain_language, large_print_available true; color_only_signals false; alt_text ≥12. Fabricated disability quotes forbidden.

## Student artifact
Required keys: captions, plain_language, alt_text, color_only_signals, large_print_available.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Walk the PD-2925 flyer checklist under NO_AI.
```
python3 scripts/run_course_labs.py --lab lab_accessibility_comm --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_accessibility_comm --empty
```

## Wrong submissions
Missing captions, color-only signals, or tiny alt_text fail.
