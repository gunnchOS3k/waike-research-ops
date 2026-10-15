# Week 5: Dashboard chart contract — labeled axes

A chart is an argument about data, so its encoding and caption must make the underlying population clear. For a per-bay average, place the canonical bay names on the categorical axis and mean headcount per valid observation on the numeric axis. A bar chart starts its magnitude axis at zero in this exercise so bar length preserves the intended comparison. Include counts because a mean from one observation and a mean from many observations have different evidential limits.

An accessible chart does not rely on color alone. Direct labels, a text explanation and an equivalent data table let readers retrieve essential values without sight, precise color discrimination or a particular pointing device. Decorative three-dimensional bars can obscure rather than clarify the comparison.

## Guided practice

From the practice report draw two bars: bay_a mean 40 (n=3), bay_b mean 80 (n=1). Label the title “Fictional pier headcount per valid observation.” Give the axis unit and define exclusions: one missing count and one negative count were removed. Add the text table with those same values. Expected interpretation: the second observed group mean is larger in this fixture; the chart does not establish that more unique people visited that bay.

Write alt text conveying the comparison and its tiny sample rather than listing colors. A suitable explanation states that bay_a's three valid observations average 40, while bay_b's single valid observation is 80. The table carries exact values.

## Independent evidence and recovery

Produce a chart and equivalent table for the new case, tracing every plotted value to group_summary or your verified independent implementation. Ask a reviewer to recover the values using the text alternative alone. Correct clipped labels, missing units or contradictory values. A JSON flag such as chart_ok is a declaration, not a visual or accessibility review. Preserve human acceptance as pending until a reviewer actually inspects the artifact.

## Runnable resources

Open the Pier Ledger README in this course’s downloadable learner resources. Save case_data.py, ledger.py and test_ledger.py together. The guide specifies execution, expected results, troubleshooting, independent criteria and return navigation.

## Worked example

Text table: bay_a, n=3, mean=40; bay_b, n=1, mean=80. Caption: fictional observations, one missing and one negative count excluded; no unique-person or causal claim.
