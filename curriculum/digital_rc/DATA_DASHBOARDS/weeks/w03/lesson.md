# Week 3: Normalize and transform — clean before KPI

Normalization maps different representations of the same intended key to a canonical value. It is a policy, not a license to merge any similar-looking labels. This fixture explicitly maps Bay-A, bay_a and BAY A to bay_a, and Bay-B and bay_b to bay_b. An unknown label is rejected for review so a spelling guess cannot silently move an observation.

Missing, zero and invalid values differ. A missing headcount says the count is unavailable. Zero is an observed count of none under the fixture's rules. A negative count is invalid in this model. Replacing missing with zero would change the question and bias a mean downward. Dropping invalid rows also changes the analyzed population and must be reported.

## Guided practice

Trace all six CSV rows. Four rows with counts 20, 40, 60 and 80 remain. v5 is rejected as missing and v6 as negative. Expected result: missing_rate_raw is 1/6, using every raw row as the denominator; rows_out is 4. The negative row is excluded from the missing numerator. Do not use the cleaned denominator for this defined metric.

In a copy change v1's count to 0. Expected result: four valid rows remain and the mean becomes 45. Change it to an empty cell instead: only three valid rows remain. Explain why those transformations cannot be substituted for each other. Inspect the rejected list to follow each excluded row.

## Independent evidence and recovery

For a new case, produce a row-accounting table with raw, retained and rejected counts and reasons. Define any normalization extension before using it. Test an unknown alias, a negative count, zero and a missing value. Keep rejected source bytes and explain a legitimate repair rather than deleting an inconvenient record. The legacy validator's declared normalization flags do not independently establish that a transformation was performed.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

Missing=1 of 6 raw rows, so missing_rate_raw=1/6. Negative=1 separately. Retained values 20,40,60,80. Replacing 20 with zero retains four rows and changes the mean to 45.
