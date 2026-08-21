# R5-S1 behavior contract — waike-research-ops

## A. Evaluation metrics

### Symbol
`waike_curriculum.evaluation.metrics.completion_rate`

### Callers
Curriculum evaluation package (`waike_curriculum.evaluation`); generated alongside schemas/report stubs for issue-completion readiness.

### Inputs / expected outputs
- Falsy progress (`None`, `[]`, `{}`, `""`, `0`) → `0.0`
- Truthy progress (any non-empty container / non-zero value) → `0.5`

Hand-computed expectations; tests must not derive expected values by calling `completion_rate` itself.

### Failure conditions
Returning a non-zero rate for empty progress, or changing the documented stub constants without an intentional product change.

### Why mutation matters
`flip_return_zero` turns the empty-progress `return 0.0` into `return 1.0`. Without a direct assertion on the empty boundary, the suite stays green.

## B. Batch002 exam size validation

### Symbol
`waike_course_ready.batch002.exams.extra_assessment_items_002`

### Callers
`waike_course_ready.content.extra_assessment_items` and `waike_course_ready.exams` lazy imports for COURSE-READY-002 mid/final banks.

### Inputs / expected outputs
- Valid `course_id` present in `exams_data.json` → `{"mid": [...], "final": [...]}` with `len(mid)==20` and `len(final)==24` after `rebalance_mcq`.
- If rebalanced banks are the wrong length → raise `ValueError` mentioning exam sizes (validation must not be removed).

### Failure conditions
Silent acceptance of wrong-sized mid/final banks.

### Why mutation matters
`remove_validation` replaces the `raise ValueError(...)` with `pass`. Happy-path length asserts still pass on good fixtures; only a forced undersized bank reveals the missing guard.

## C. Labs (preserve existing kill)

### Symbol
`waike_course_ready.batch002.labs` — first `if ... == ...:` guard (`_fail_if_print_pass`).

### Existing coverage
Learner journey / digital RC lab tests already kill `invert_condition` on this file. R5-S1 must keep that kill (`WAIKE_EXISTING_LABS_MUTATION_STILL_KILLED`).
