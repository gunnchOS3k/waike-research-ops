# Week 2: SQL SELECT with pier filters — honest predicates

SQL SELECT describes which columns and rows to retrieve. FROM names a table; WHERE filters individual rows. A predicate is a condition that evaluates for each row. `headcount > 40` excludes a count of exactly 40, whereas `>= 40` includes it. Query semantics must match the question before a chart is designed.

The runnable example creates an in-memory SQLite table from validated observations. Parameter placeholders separate a query's fixed structure from its threshold value. This is a local authored program, not a service for executing arbitrary visitor SQL. An ordered result makes comparisons reproducible; without ORDER BY, row order should not be assumed.

## Guided practice

Run the Pier Ledger example at thresholds 40 and 60 with different output filenames. Read the actual SQL in ledger.py: it selects visit_id and headcount where headcount is strictly greater than a bound value, then orders by visit_id. Expected result: v3=60 and v4=80 for 40; only v4=80 for 60. At 100 the selected list is empty. Empty selection is an accurate answer, not necessarily a pipeline failure.

Notice that the overall mean remains 50 in all three reports. That KPI is computed over all cleaned rows, not just the selection. Name the population for every number so a reader can interpret it. A WHERE clause can silently change that population if moved into a summary query.

## Independent evidence and recovery

Predict results for a different threshold before running your own query. Include an exactly-at-threshold case and a no-match case. Temporarily change `>` to `>=` in a copy; the public SQL contract test must detect the defect. Restore the predicate and rerun. The old lab_sql_select checks declaration fields and query text; text containing WHERE is not proof that a query executed correctly. Preserve SQL, source identity, predicted row IDs and actual output for review.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

Strict headcount > 40 selects v3=60 and v4=80. With > 60 only v4 remains. The whole-cleaned-population mean stays 50 because this query does not redefine that KPI.
