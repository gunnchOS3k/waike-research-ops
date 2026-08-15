# Week 3: Unsupervised clusters — failure modes without a teacher

Not every EdgeForge ticket has a label. Ticket EF-2309 dumps 60 anonymous fault vectors (temp_c, fan_rpm, usb_reset_count) from the three accelerators. Unsupervised work means choosing k and defending centroids — not inventing a story that 'cluster 2 is hackers.'

You will assign each point to the nearest of two centroids using Manhattan distance (|dx|+|dy|+|dz|). The lab checks your assignments and the sum of distances. If you relabel clusters to match a preferred narrative without recomputing, the sum fails.

Responsible AI note: clusters are hypotheses for the maintenance log, not accusations about staff.

Centroid A=(40,3000,0), B=(70,1200,5). Point p=(55,2000,2): distA=|15|+|1000|+|2|=1017; distB=|15|+|800|+|3|=818 → assign B.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

p=(55,2000,2) closer to B=(70,1200,5) with Manhattan 818 vs 1017.
