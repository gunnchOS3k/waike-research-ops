# Week 10: Observability and issue→deploy capstone

SLO: checkout API availability 99.5% over fixture window. Compute error budget from failed/total. Capstone: real ForgeDesk issue fixture through branch, CI, migrate, deploy, observability note. No fabricated community impact numbers.

Career map: junior software builder / Device Lab integrator. Certs aligned not granted. Academic: CS50/CS50 Web structure citations only.

AI modes used across the course must appear in the capstone disclosure table: EXPLAIN/HINT/QUESTION_ME/DEBUG_WITH_ME/REVIEW_MY_WORK/COMPARE_APPROACHES/PRACTICE mapped to assessment modes AI_ALLOWED / AI_RESTRICTED / AI_DISCLOSED / NO_AI.

SLO availability is 99.5% over the fixture window. Error budget = 1 − availability from failed/total counts the lab recomputes. Capstone ships a real ForgeDesk issue fixture through branch, CI, migrate, deploy, and an observability note — no fabricated community impact numbers. Career map: junior software builder / Device Lab integrator; certs aligned not granted. Capstone disclosure table must map EXPLAIN/HINT/QUESTION_ME/DEBUG_WITH_ME/REVIEW_MY_WORK/COMPARE_APPROACHES/PRACTICE to AI_ALLOWED / AI_RESTRICTED / AI_DISCLOSED / NO_AI.

## Concept and boundary

Observability connects external outcomes to internal events without exposing unnecessary information. Counts, timings and logs answer different questions. A log that merely exists is not evidence that the application met the user need or that an incident was resolved.

## Guided implementation

Run one allowed checkout, one repeated checkout and one denied checkout in a fresh fixture. Inspect its event list. Expected result: status and outcome are recorded, while no patron name, password or item text is logged. Count the outcomes and explain which request sequence produced them. Distinguish the fictional event trace from real service telemetry.

## Independent evidence and recovery

Assemble the capstone: issue description, requirement-to-test map, exact source version, test output including a controlled failure, authorization matrix, migration plan, release/rollback rehearsal and redacted findings. A reviewer must rerun the example and inspect your independent tests. Record completion as pending until actual practical evidence and authorized review meet the course criteria.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

failed=50 total=10000 → availability=0.995; budget_ok true.
