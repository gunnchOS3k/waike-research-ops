# Week 6: Baseline vs model — paired interval over seeds

SGA-1606 asks whether the model actually beats the baseline or merely got a lucky seed. Run both on the same five seeds and subtract run by run; pairing removes the shared difficulty of each seed, which is usually the largest source of spread. The fixture differences are 0.05, 0.02, 0.07, 0.02 and 0.04, with mean 0.04 and sample standard deviation about 0.0212. With only five pairs you need Student's t, not the normal 1.96: t at 0.975 with four degrees of freedom is 2.776, so the half-width is 2.776 × 0.0212 / √5 ≈ 0.0263 and the 95 percent interval runs from about 0.0137 to 0.0663. It excludes zero, so the poster may say the model improved top-3 accuracy on this synthetic scenario, and should print the interval beside the claim. Had the interval crossed zero, the honest sentence would be that five seeds cannot distinguish the two. Notice what the interval does not license: it says nothing about another scenario, a real cell, or a different codebook. That limitation goes into next week's external-validity row, not into a caveat nobody reads.

## Worked example

diffs = [0.05,0.02,0.07,0.02,0.04]; mean 0.04; sd 0.0212; 95% CI = 0.04 ± 2.776·0.0212/√5 = [0.0137, 0.0663]
