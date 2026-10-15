# Pier Ledger: from source bytes to an explainable result

This is the runnable worked example for DATA_DASHBOARDS Weeks 1–10. Start with Digital Confidence's file and capacity activities and Software Builder's first-program guide if saving files, functions or terminal commands are unfamiliar. You need Python 3.11 or later with its standard `csv` and `sqlite3` modules, a text editor and a folder you control. There are no downloads from package registries, credentials, network calls or system changes. SQLite uses a temporary in-memory database. All six observations are original fictional teaching data. Nothing here measures real visitors, learns a model or changes a production database.

Save these four resources together: `case_data.py`, `ledger.py`, `test_ledger.py`, and this guide. Display filename extensions so `.py.txt` does not masquerade as a program. Open a terminal in that folder, then run:

```
python3 --version
python3 case_data.py visits.csv
python3 ledger.py visits.csv report.json
python3 -m unittest -v test_ledger.py
```

On Windows with the Python launcher already installed, replace `python3` with `py -3`. Expected result: a six-row CSV, computed JSON evidence and 14 passing tests. Generated outputs are created exclusively: an existing `visits.csv` or `report.json` is never overwritten. Choose a new output name for a retry, such as `report-retry.json`. The program reads at most 65537 input bytes and rejects inputs over 65536 bytes or 1000 rows. These limits make local practice manageable; they are not a production upload or sandbox service. Do not run untrusted programs simply because they have a `.py` extension.

## Read the data before the report

Open `visits.csv` as plain text. A row represents a fictional observation, not a unique person. The five columns identify an observation, its pier bay, timestamp, headcount and declared source filename. A filename is provenance text, not proof of origin. `source_sha256` hashes the exact input bytes; a line-ending change also changes that hash. Matching hashes supports byte identity, not truth or authorship.

Predict the six input rows, one missing count and one negative count. The cleanup rule retains zero, rejects a missing count, and rejects a negative count. Four valid rows remain: 20, 40, 60 and 80. The missing rate is **1/6 of the raw rows**. The mean of valid rows is **50**, and nearest-rank p95 is **80**. Neither is a causal impact measure. The labels `Bay-A`, `bay_a` and `BAY A` deliberately normalize to one key. Unknown aliases cause a rejection for review.

The actual SQLite query selects headcounts strictly greater than the bound threshold. With 40, rows v3 and v4 are selected; v2 equals 40 and is excluded. Recompute with a different value:

```
python3 ledger.py visits.csv report-threshold60.json --threshold 60
```

Expected result: only v4 remains in `selected_rows`; the overall mean stays 50 because the KPI describes all cleaned rows, not the filtered subset. Inspect `ledger.py` to find both the selection and grouping queries. Input data is passed through SQL parameters. No API executes visitor-supplied code or SQL.

## Work through the weekly sequence

1. Week 1: declare the exact schema, count the rows and compare hashes after changing one copied input byte.
2. Week 2: predict selection for thresholds 40, 60 and 100, then compare actual SQL results.
3. Week 3: trace every row to retained or rejected status; distinguish missing, negative and zero.
4. Week 4: calculate mean and nearest-rank p95 before reading the computed results.
5. Week 5: draw an accessible labeled bar chart from `group_summary`; include counts and an equivalent text table.
6. Week 6: inspect join cardinality, then remove one metadata key in a copy and observe explicit orphans.
7. Week 7: explain why approved-column projection is useful but does not establish anonymity.
8. Week 8: demonstrate a defect caught by a test, repair it and preserve both outputs.
9. Week 9: compute age using explicit timestamps and distinguish within-policy from actual operational availability.
10. Week 10: prepare a source-bound portfolio with limitations and an independent variation for review.

Return to the corresponding course week using the lesson navigation. Use the canonical Hub assignment attached to that week for instructor-authorized evidence intake. This local report does not submit anything or set a course-completion flag. Do not paste code or personal data into an unrelated quiz answer.

## Independent variation: a different input and your own implementation

An instructor can choose a seed from 0 through 999999 after practice. A self-study learner can choose a seed and honestly label the exercise self-directed. Generate inputs only:

```
python3 case_data.py independent.csv --seed 731
```

The generated case has twelve fictional rows with changing counts and labels. Do not treat the practice report's numbers as answers for it. In a separate `my_ledger.py`, implement schema validation, explicit cleanup accounting, a SQL or equivalent clearly documented filter, per-bay summaries and source hashing. Produce your own evidence with the source bytes, version, policy choices and expected-results table. A reference run may be used **after** predicting results for comparison, but it is not evidence that you authored an independent program. Record all assistance, including reference code and AI.

Then change one count, one threshold and one metadata key. Predict what must change and what must remain stable; run your tests and compare. Include a test detecting a deliberate incorrect `>=` predicate, a missing-versus-zero error, an unweighted mean of group means, a duplicate join key, and a stale timestamp. Preserve a failing run and the repaired run. A reviewer may issue different inputs or ask for a live explanation.

The review criteria are: (1) byte/source and row-accounting integrity; (2) mathematically correct cleanup, filtering and summaries; (3) explicit join, timestamp and privacy limitations; (4) tests that detect relevant defects; (5) an explanation connecting choices to the original question. Each criterion is pending until evaluated by an authorized person. Revise unmet criteria and keep attempt histories. Passing the public contract tests alone cannot establish independence or course mastery.

## Troubleshooting and recovery

`ModuleNotFoundError` means a companion file may be missing or the terminal is in another folder; check filenames before changing code. `File exists` protects an earlier artifact; select another output filename. A schema rejection can come from reordered, missing or extra columns, or from saving a spreadsheet in a different delimiter format. Preserve the rejected original, inspect it as text, and document any intentional conversion. A missing timezone is rejected instead of silently assumed local. A duplicate visit ID or metadata key requires investigation; do not delete rows merely to make a check green. An empty valid set produces no normal KPI rather than a misleading zero average.

Never use real identifiers, contact details, access tokens or institutional datasets here. Exact columns and normalization alone do not make a release safe: free text, small groups and timestamps can still identify people in real datasets. A safe local fictional exercise does not grant permission to process real records. If a file contains private information, stop, keep it out of uploads and follow the appropriate institutional handling process.

Technical references: Python's [`csv`](https://docs.python.org/3.11/library/csv.html) and [`sqlite3`](https://docs.python.org/3.11/library/sqlite3.html) documentation, and SQLite's [`SELECT`](https://www.sqlite.org/lang_select.html) language specification. The percentile method and teaching freshness policy are defined here; they are not universal software defaults. AI assistance contributed to this original guide, code, tests and lesson expansions. No third-party data or artwork is included. Human technical and educational acceptance remains pending. Repository software licensing and educational-publication rights remain separate release decisions.
