# Week 4: KPI calc — arithmetic before tiles (NO_AI)

A key performance indicator is a defined summary chosen to address a question. The arithmetic mean adds values and divides by their count. Its denominator matters: the mean of four valid observations differs from the mean after treating two invalid observations as zero. State exclusions alongside the result.

A percentile requires a convention. This lab defines nearest-rank p95: sort n valid values in ascending order and choose the value at one-based rank ceil(0.95*n). For four values the rank is 4, so p95 is the maximum. Other software can interpolate instead; a difference is not automatically a bug until methods are aligned. Four observations are too few for a stable characterization of a real population tail.

## Guided practice — calculate before running

The valid counts are 20, 40, 60 and 80. Their sum is 200; mean is 200/4=50. Sorted order is unchanged; ceil(0.95*4)=4, so nearest-rank p95=80. Expected result: the computed report matches both 50 and 80. Compare with your calculations. There are three bay_a observations averaging 40 and one bay_b observation of 80. The unweighted mean of those two group means is 60, which is not the all-observation mean. Weighting group means by counts restores 50.

## Independent evidence and recovery

Choose a small changed dataset and hand-calculate its sum, denominator, mean and percentile rank. Include tied values and zero. If no valid observations remain, report that the KPI is undefined under this contract; ledger.py rejects a normal report instead of emitting zero. Preserve your calculations for the existing NO_AI assessment policy; do not submit AI-produced arithmetic as unaided performance. Practice examples do not override that policy. Explain why these synthetic summaries establish neither citywide trends nor causal improvement.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

(20+40+60+80)/4=50. Nearest-rank p95 uses rank ceil(.95*4)=4, hence 80. Bay means 40(n=3) and 80(n=1) have weighted mean 50, not unweighted mean 60.
