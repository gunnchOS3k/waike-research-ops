# Week 4: Applied stats — median wait beats a vanity mean

Ticket CM-3404 asks for mean, median, and IQR of wait_min on the cleaned fixture. One 120-minute outlier pulls the mean; the median stays honest for the board. You will compute all three. Generative fill of statistics under NO_AI week policy fails.

Sorted waits [...]; median=12; Q1=8; Q3=18; IQR=10; mean inflated by 120 outlier.

Mean chases the 120-minute outlier; median stays near 12 for the board. IQR = Q3−Q1 = 10 on the fixture. Prefer median (+ IQR) when you brief wait times.

NO_AI week: no generative fill of the statistics. Compute mean, median, and IQR on the provided values; calculator OK. A model that invents a 'smoothed mean' fails honesty.

Journal two sentences that explain why the board should not lead with the mean this week. Numbers first, adjectives never as a substitute for the sorted list.

Week 4 close for DATA_VIZ_BI: ticket work ends when the lab JSON fields for `lab_stats_summary` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

median=12, IQR=10; mean rises when 120-min outlier included.
