# Week 6: Join integrity — keys that match

A join combines records using a key, but matching keys alone do not guarantee the intended cardinality. Each cleaned observation belongs to one bay. The metadata table must have at most one row per bay for this many-observations-to-one-label relationship. Duplicate metadata keys would multiply joined observations and can inflate aggregates.

An inner join retains only matching observations. A left join retains every observation and supplies NULL for missing metadata. Choosing an inner join without counting unmatched rows can hide data loss. The worked example uses a left join to identify orphans separately and reports the number an inner join would retain.

## Guided practice

The default metadata includes bay_a and bay_b. Expected result: inner_rows=4 and orphan_ids is empty. In a copy of ledger.py remove bay_b from DEFAULT_META, then create a new report. Expected result: inner_rows=3 and orphan_ids contains v4. The overall source report still has four cleaned observations: the join audit exposes the unmatched row instead of erasing it.

Add a duplicate bay_a metadata row in a separate copy. Expected result: a clear duplicate-metadata rejection before SQL insertion. The rule prevents an accidental fan-out; it does not resolve which real-world record would be authoritative. Restore the original file and rerun the contract tests.

## Independent evidence and recovery

Define the intended join relationship for the issued case. Include a missing key, a duplicate key and a fully matched example. Predict row counts before execution and show the actual differences. Investigate the source and metadata before modifying either; never delete an orphan solely to pass a check. Preserve the original tables, chosen policy and output for reviewer inspection. The historical lab's declared orphan count is not itself a re-execution of the join.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

With both metadata keys, inner_rows=4 and no orphans. Remove bay_b: inner_rows=3 and orphan_ids=[v4]. A duplicate bay_a key is rejected before it can multiply rows.
