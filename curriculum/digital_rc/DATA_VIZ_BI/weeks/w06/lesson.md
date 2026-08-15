# Week 6: Dashboard design — one question per screen

Ticket CM-3605 builds a desk dashboard with three tiles: median wait by zone, open ticket count, and data freshness timestamp. A fourth tile of stock photos fails. Layout JSON must list required tiles and max_tiles=3 for the first screen.

required_tiles=[median_by_zone, open_count, freshness]; max_tiles=3.

First screen, three tiles: median_by_zone, open_count, freshness. max_tiles=3. A stock-photo fourth tile fails layout even if the PNG is beautiful.

Freshness is trust infrastructure — without a timestamp the board cannot know whether the median is from this hour or last month. ASCII sketches are acceptable; missing freshness is not.

One question per screen means the three tiles argue the same desk question. Unrelated KPI collages belong on later pages, not the civic opening view.

Week 6 close for DATA_VIZ_BI: ticket work ends when the lab JSON fields for `lab_dashboard_layout` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

Three tiles only; freshness timestamp mandatory.
