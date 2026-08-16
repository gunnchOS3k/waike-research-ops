# lab_ai_disclosure_modes — AI disclosure modes

PD-2822 AI mode honesty. mode ∈ {AI_ALLOWED, AI_RESTRICTED, AI_DISCLOSED, NO_AI}. disclosed=true, used_instructor_keys=false, learner_facing=true. Learner tutors never open the instructor key store. NO_AI rationale must say human-only/no ai.

## Student artifact
Required keys: mode, disclosed, used_instructor_keys, learner_facing, rationale.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
Declare the PD-2822 AI mode without opening the instructor key store.
```
python3 scripts/run_course_labs.py --lab lab_ai_disclosure_modes --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_ai_disclosure_modes --empty
```

## Wrong submissions
Key access true, disclosed false, or invalid mode fail.
