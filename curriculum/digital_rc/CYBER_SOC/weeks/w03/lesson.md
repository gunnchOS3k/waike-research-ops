# Week 3: Detection quality — precision, recall, and the analyst's hour

SOC-2303 is a NO_AI week: do the fractions on paper and show each line, because these four numbers decide whether a rule stays on. A month of the brute-force rule produced 60 alerts. Eighteen were real attacks, true positives, and forty-two were not, false positives. Six real attacks slipped through without an alert, false negatives, and 934 quiet events were correctly left alone. Precision asks how often an alert is worth opening: 18 out of 60, or 0.30. Recall asks how many real attacks the rule caught: 18 out of 24, or 0.75. The false-positive rate compares wrong alerts with all benign events, 42 out of 976, about 0.043, which sounds tiny and still costs forty-two investigations. At ten minutes each that is seven analyst-hours spent proving nothing happened. A precision under one half means most alerts are noise, so the honest call is needs tuning, not 'the rule works'. Tuning that raises precision often lowers recall, so record both before and after a change, and never report recall alone because it flatters a noisy rule.

## Worked example

TP 18, FP 42, FN 6, TN 934 → precision 18/60 = 0.30, recall 18/24 = 0.75, FPR 42/976 = 0.043 → needs tuning
