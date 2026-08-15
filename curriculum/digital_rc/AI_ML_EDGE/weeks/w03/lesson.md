# Week 3: Unsupervised clusters — failure modes without a teacher

Not every EdgeForge ticket has a label. Ticket EF-2309 dumps 60 anonymous fault vectors (temp_c, fan_rpm, usb_reset_count) from the three accelerators. Unsupervised work means choosing k and defending centroids — not inventing a story that 'cluster 2 is hackers.'

You will assign each point to the nearest of two centroids using Manhattan distance (|dx|+|dy|+|dz|). The lab checks your assignments and the sum of distances. If you relabel clusters to match a preferred narrative without recomputing, the sum fails.

Responsible AI note: clusters are hypotheses for the maintenance log, not accusations about staff.

Centroid A=(40,3000,0), B=(70,1200,5). Point p=(55,2000,2): distA=|15|+|1000|+|2|=1017; distB=|15|+|800|+|3|=818 → assign B.

Choose k like you choose a maintenance bucket count: enough to separate thermal throttle from USB reset storms, not enough to invent a villain. Manhattan distance keeps the arithmetic audible — no kernel mythology required for three telemetry axes.

After assignment, recompute total distance from scratch. Relabeling clusters to match a preferred story without recomputing is the same fraud as rewriting a restore hash. The lab’s sum is the honesty check.

Write one sentence in the journal that refuses staff blame: clusters are hypotheses for the rack log. If someone wants 'cluster 2 = intern error,' send them back to the Consensus Ladder — observation first, accusation never from unlabeled points.

## Worked example

p=(55,2000,2) closer to B=(70,1200,5) with Manhattan 818 vs 1017.
