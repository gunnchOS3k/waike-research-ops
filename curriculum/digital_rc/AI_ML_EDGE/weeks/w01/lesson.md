# Week 1: EdgeForge Bench — Python tensors as civic tables

The EdgeForge Bench is a synthetic Gary teaching scenario, not a report of installed accelerators or measured community outcomes. Its occupancy CSV has 480 time-ordered rows: timestamp_iso, zone_id, people_count, and rssi_dbm. First ask what a row represents and what prediction would be made at deployment. A matrix shape alone cannot establish that the measurements are valid, representative, or ethically collected.

For a forecast evaluated on later observations, use the first 384 rows for training and the last 96 for validation. The training fraction is 384/480 = 0.80. Keep the order and document the boundary timestamp. If adjacent records share information, randomly mixing them can give an optimistic estimate of future performance. The appropriate split depends on the question: a new-building evaluation may instead need a building-level holdout. Time order reduces one risk; it does not prove that all leakage has been eliminated.

Leakage occurs when information unavailable at prediction time influences training or model selection. Fit learned preprocessing, such as a scaler, on training rows only, then apply it to validation. After choosing thresholds with validation data, an untouched final test set is still needed for an independent final estimate. Scikit-learn's Common pitfalls, section 11.2, explains this separation: https://scikit-learn.org/stable/common_pitfalls.html#data-leakage.

An observed forty-minute run of zero people_count values is an observation. Calling it a janitor sweep is an unverified explanation. A zero can indicate an empty area, a sensor error, or another cause; investigate before deleting records or inventing labels. F1 needs defined positive labels and predictions. Without them, no F1 value or effect of shuffling can be claimed.

Use Python's csv module to inspect the column names, count rows, and report the train/validation counts. Use zone letters A/B/C in the fixture. These codes alone would not guarantee privacy in a real dataset; time and location can also reveal patterns. Do not load real faces, accounts, or learner records into this exercise.

Independent practice: for 625 time-ordered rows, reserve the final 125 for validation. Report both counts, explain what information a future predictor is allowed to use, and describe one check for leakage across the boundary. Evaluate your explanation against the prediction task, rather than copying the words “never shuffle.”

## Worked example

480 rows × 0.80 = 384 train; 96 validation by time order (not shuffle).
