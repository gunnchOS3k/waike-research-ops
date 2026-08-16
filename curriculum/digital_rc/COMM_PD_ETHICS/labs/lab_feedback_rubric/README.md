# lab_feedback_rubric — feedback rubric

Runnable validator for lab_feedback_rubric. Empty/wrong/print-PASS fail. Harbor Desk Voice.

## Student artifact
Empty {} fails. PASS raises. Harbor Desk Voice ethics/PD fields must be honest.

## How to run
From the Harbor Desk Voice folder, submit computed JSON.
```
python3 scripts/run_course_labs.py --lab lab_feedback_rubric --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_feedback_rubric --empty
```

Wrong ethics/PD policy fields must fail.
