# lab_ethics_ladder — ethics ladder

PD-2409 observation→inference→need→action ladder (NO_AI authorship week). Each rung has a minimum length. fabricated_impact must be false — invented citywide harm stats fail.

## Student artifact
Required keys: observation, inference, need, action, fabricated_impact.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Fill the PD-2409 ladder under NO_AI authorship rules.
```
python3 scripts/run_course_labs.py --lab lab_ethics_ladder --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ethics_ladder --empty
```

## Wrong submissions
Short rungs or fabricated_impact=true fail the ladder honesty gate.
