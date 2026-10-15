# Week 6: Automated tests that catch the silent 200

Parse a JUnit-like JSON report: total, failed, skipped. Acceptance requires failed==0, total>=8, and a named test test_reader_post_forbidden with status passed. A green badge PNG is not evidence. Aligns to CS50 Web testing themes and secure-dev prove-the-negative-path without copying those item banks. NO_AI applies to the practical portion of any quiz makeup that reuses this week's fixture.

Journal week 6 (Automated tests that catch the silent 200): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

Acceptance for week 6 still names ticket-linked digests, HTTP status fields, schema_version, DOM contracts, role actions, JUnit counts, workflow gates, digests, severity bands, or error-budget arithmetic the next shift can reopen without tribal knowledge.

Acceptance for week 6 still names ticket-linked digests, HTTP status fields, schema_version, DOM contracts, role actions, JUnit counts, workflow gates, digests, severity bands, or error-budget arithmetic the next shift can reopen without tribal knowledge.

## Concept and boundary

A test compares an observation with an expected result. A passing test supports only the cases and assertions it exercises. Tests can be wrong or incomplete. A negative test deliberately checks that an invalid action is rejected without changing protected state.

## Guided implementation

Read all six worked-example tests. For each assertion, name the requirement it checks. Change the expected conflict status to 200 and run the suite; the deliberate failure confirms that the assertion is being executed. Restore it. Next remove the authorization condition and observe a different failure. Expected result: both controlled defects are detected.

## Independent evidence and recovery

Add tests for unsupported methods and unrecognized roles. Include an assertion on stored state after rejection. Explain one behavior your tests still do not establish, such as concurrent requests, network delivery or recovery after a disk failure.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

Report total=10 failed=0 skipped=1 includes test_reader_post_forbidden passed=true.
