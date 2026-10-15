# Week 7: ETL PII redaction — desks keep secrets out

Privacy review begins before a dataset is gathered or shared. This teaching CSV contains fictional aliases and counts; do not replace them with real names, contact details, identifiers or operational records. Permission to run a local example is not permission to process institutional data.

Projection means selecting only approved columns. An exact schema can reject an unexpected email column, but approved columns can still contain private text. A filename, free-text label or precise timestamp might identify someone. Removing a name does not establish anonymity, especially for small groups. Data minimization, access control and release review address different risks.

## Guided practice

Inspect every input column and every output field. The cleaned rows retain only visit ID, normalized bay, timestamp and numeric headcount. The generated evidence also includes rejected fictional visit IDs for traceability. Expected interpretation: this is a bounded data-flow description, not an anonymization certification. Draw the path from original bytes to validated rows, summary and exported evidence. Mark where a real system would need access restrictions and retention rules.

In a local copy add a fictional email column with a value ending in example.invalid. Expected result: exact schema validation rejects the new column. Explain why a private value hidden in source_file could still evade that column-name check. Use invented text only; the example is not a PII detector.

## Independent evidence and recovery

Prepare a release review for a fictional expanded schema. Identify needed fields, unneeded fields, likely indirect identifiers, intended readers and deletion policy. Supply a redacted sample and explain what uncertainty remains. An authorized reviewer decides whether a real release is appropriate; automated booleans cannot replace that decision. If real private material appears accidentally, stop sharing it, preserve required handling evidence securely and follow the applicable institutional process.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

An added fictional email column is rejected by the exact five-column schema. A private value placed inside an approved text column could still pass; schema validation does not prove anonymization.
