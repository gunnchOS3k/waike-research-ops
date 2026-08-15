# Week 8: pandas groupby — zone medians in reproducible scripts

Ticket CM-3818 computes median wait by zone with pandas-style groupby on the fixture (plain Python OK if pandas absent). The lab checks the group map and that the script hash is recorded for reproducibility. Notebooks without a pinned input hash fail the portfolio later.

zones A/B/C medians {A:10,B:14,C:12} on fixture; input_sha256 recorded.

groupby median waits: A:10, B:14, C:12 on the fixture. Pin input_sha256 so a later rerun proves the same bytes. Screenshots without hashes are portfolio risk.

Plain Python aggregation is allowed if pandas is absent — the contract is the medians and the digest, not the import name. Dirty inputs still require last week’s clean gate first.

If you change the CSV, rotate the hash. Reusing yesterday’s digest after an edit is the same class of failure as a mismatched model digest on EdgeForge.

Week 8 close for DATA_VIZ_BI: ticket work ends when the lab JSON fields for `lab_pandas_group` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

groupby median → A:10 B:14 C:12 with input digest pinned.
