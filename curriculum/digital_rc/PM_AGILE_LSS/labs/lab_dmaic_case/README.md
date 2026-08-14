# lab_dmaic_case — dmaic case

Runnable validator for lab_dmaic_case. Empty/wrong/print-PASS fail.

## Student artifact
Fabricated outcomes fail. AI critique requires ai_disclosed true.
A file whose entire body is PASS is rejected by _fail_if_print_pass.

## How to run
From the Process Studio folder, submit artifact JSON with fixture counts only.
```
python3 scripts/run_course_labs.py --lab lab_dmaic_case --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_dmaic_case --empty
```

Wrong numeric or policy fields must fail.
