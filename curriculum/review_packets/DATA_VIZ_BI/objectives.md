# Objectives — DATA_VIZ_BI

## Program learning outcomes

_GAP: no numbered learning outcomes extracted from program file — use package week contracts._

## Week-level objectives (from package lessons)

### Week 1: Civic Metrics Studio — dirty rows before pretty charts
  - Complete the week contract: Civic Metrics Studio — dirty rows before pretty charts.
  - Reproduce worked example: 200 rows, 10 nulls → null_rate=0.05; negatives dropped (not abs).
  - The Civic Metrics Studio in Ghana/Gary partnership hours starts with a dirty CSV of desk tickets: ticket_id, opened_at, closed_at, zone, wait_min.
### Week 2: SQL joins — tickets to zones without cartesian accidents
  - Complete the week contract: SQL joins — tickets to zones without cartesian accidents.
  - Reproduce worked example: inner join matching 95; cartesian 100×5=500 is the accident to refuse.
  - Ticket CM-3208 needs a join from tickets to zone_dim on zone_id.
### Week 3: Relational modeling — stop repeating zone addresses
  - Complete the week contract: Relational modeling — stop repeating zone addresses.
  - Reproduce worked example: Move zone_address into zone_dim; tickets keep zone_id FK only.
  - Ticket CM-3311 shows zone address repeated on every ticket row.
### Week 4: Applied stats — median wait beats a vanity mean
  - Complete the week contract: Applied stats — median wait beats a vanity mean.
  - Reproduce worked example: median=12, IQR=10; mean rises when 120-min outlier included.
  - Ticket CM-3404 asks for mean, median, and IQR of wait_min on the cleaned fixture.
### Week 5: Visualization principles — encode waits, don't decorate
  - Complete the week contract: Visualization principles — encode waits, don't decorate.
  - Reproduce worked example: bar/zone/median_wait valid; pie(ticket_id) invalid encoding.
  - Ticket CM-3519 grades a chart spec: mark=bar, x=zone, y=median_wait.
### Week 6: Dashboard design — one question per screen
  - Complete the week contract: Dashboard design — one question per screen.
  - Reproduce worked example: Three tiles only; freshness timestamp mandatory.
  - Ticket CM-3605 builds a desk dashboard with three tiles: median wait by zone, open ticket count, and data freshness timestamp.
### Week 7: BI workflows — refresh SLA without pirating licenses
  - Complete the week contract: BI workflows — refresh SLA without pirating licenses.
  - Reproduce worked example: refresh 10min meets ≤15 SLA; license_ok with attribution, no binary redistribute.
  - Industry workflows mention Tableau/Power BI patterns as PUBLIC_REFERENCE_ONLY.
### Week 8: pandas groupby — zone medians in reproducible scripts
  - Complete the week contract: pandas groupby — zone medians in reproducible scripts.
  - Reproduce worked example: groupby median → A:10 B:14 C:12 with input digest pinned.
  - Ticket CM-3818 computes median wait by zone with pandas-style groupby on the fixture (plain Python OK if pandas absent).
### Week 9: Storytelling + KPIs — a formula the board can audit
  - Complete the week contract: Storytelling + KPIs — a formula the board can audit.
  - Reproduce worked example: 6*12/3=24 desk_pressure.
  - Ticket CM-3909 defines KPI desk_pressure = open_count * median_wait / staff_on_duty.
### Week 10: Quality + repro portfolio — hash the dashboard inputs
  - Complete the week contract: Quality + repro portfolio — hash the dashboard inputs.
  - Reproduce worked example: null_rate=0.04, negatives_dropped=true, freshness=8, sha256 present → quality_ok.
  - Capstone: ship a portfolio dashboard pack with cleaned CSV sha256, KPI snapshot, and a data-quality checklist (null_rate, negatives_dropped, freshness).

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
