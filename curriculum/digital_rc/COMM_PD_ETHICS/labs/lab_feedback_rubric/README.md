# lab_feedback_rubric — feedback rubric

PD-2615 peer feedback: criterion, evidence (≥24 on journal behavior), score 0..4, next_action ≥16. identity_attack must be false. Educator HITL still required before any grade publish.

## Student artifact
Required keys: criterion, evidence, score, next_action, identity_attack.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Score the peer journal for PD-2615 with evidence, not identity attacks.
```
python3 scripts/run_course_labs.py --lab lab_feedback_rubric --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_feedback_rubric --empty
```

## Wrong submissions
Score outside 0..4, identity_attack true, or thin evidence/next_action fail.
