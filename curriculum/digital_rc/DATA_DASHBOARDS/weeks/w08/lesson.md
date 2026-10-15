# Week 8: Debug the pipeline — name the broken stage

Debugging starts by distinguishing an input failure from an implementation defect. A schema mismatch, unknown alias or duplicate observation ID can be a correct rejection. An incorrect filter result for a valid input indicates a different problem. Reading the first relevant error and reproducing the smallest failing case is more useful than changing unrelated lines.

A meaningful regression test fails when a real contract violation is introduced and passes after the defect is repaired. Test outputs document behavior of specified cases. They do not prove all possible inputs correct or establish that a learner worked independently.

## Guided practice

Run all 14 public contract tests in an unchanged copy. Expected result: all pass. Then change the SQL comparison from `headcount > ?` to `headcount >= ?`. Rerun the suite. The threshold-equality case must fail because v2=40 is now wrongly selected for the strict predicate. Preserve that failing output. Repair the comparison and rerun; the test should pass again. Do not modify expected values merely to hide the defect.

Try a second defect in a separate copy: treat an empty headcount as zero. Predict which cleanup, denominator and mean checks should change. Use the named assertion and input row to explain the failure. Restore the reference before continuing.

## Independent evidence and recovery

Choose a relevant defect in your independent program, predict a test that detects it, preserve failure and repair output, and explain the root cause. Include a stage diagram: bytes → schema → cleanup → SQL → summaries → export. A file-not-found error usually needs a folder or filename correction, not a new statistical formula. Keep the original source and distinguish data repair from code repair in the journal.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

Mutation: change > to >=. At threshold40, v2 must now wrongly appear; the strict-predicate test fails. Restore > and preserve the passing rerun alongside the failure.
