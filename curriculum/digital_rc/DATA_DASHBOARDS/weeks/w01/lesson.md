# Week 1: Schema first — ingest without inventing columns

A dashboard begins with a question and a declared unit of observation. In the Pier Ledger teaching fixture, each row is one fictional count observation at a named bay and time. A headcount is not a unique visitor identity, so adding counts across times does not establish how many different people visited. Before analysis, declare which fields the source really contains and which question they can support.

A CSV header is a sequence of column names. It does not enforce types or uniqueness. This exercise expects visit_id, pier_bay, ts_utc, headcount and source_file, in that order. The parser checks exact columns and row width, then validates identifiers, known aliases and timestamps. It rejects extra columns rather than assuming they are harmless. Integers arrive as text and need validation before arithmetic.

## Guided practice

Download all four Pier Ledger learner resources and follow their README commands. `case_data.py visits.csv` creates six original fictional rows. `ledger.py visits.csv report.json` reads actual bytes and creates evidence. Expected result: rows_in is 6 and rows_out is 4. Open the CSV and count manually before reading the report. source_sha256 identifies the exact bytes; it does not prove their accuracy or ownership.

Save a copy, change v1's count from 20 to 21, and regenerate under a new output name. Expected result: the hash changes, but row counts do not. If your hash differs only because line endings changed, explain that byte identity and equivalent table meaning are different tests.

## Independent evidence and recovery

Declare the observation unit, schema, raw count and file hash for an instructor-issued case. Include a rejected extra-column example. Preserve the original input if validation fails; inspect delimiters and filename extensions rather than inventing missing fields. The historical lab_schema_ingest checks a declared artifact shape and broad constraints; it does not itself read a CSV or independently verify its hash. Use the new computed report and reviewer inspection for source-bound evidence. Neither a self-reported hash nor a successful practice run establishes mastery.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

Six raw fictional rows contain one missing and one negative count. The computed report retains four rows and hashes the actual bytes. A changed count changes the hash; a declaration alone does not verify provenance.
