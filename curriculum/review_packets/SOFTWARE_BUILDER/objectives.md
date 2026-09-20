# Objectives — SOFTWARE_BUILDER

## Program learning outcomes

1. Explain core concepts using plain-English intuition (WAIKE Consensus Ladder layer 1).
2. Apply academic foundations with labs (layer 2–3).
3. Map work to industry standards (layer 4–5) — *needs source review for exact objectives*.
4. Connect to gunnchOS research/product where applicable (layer 7–8).

## Week-level objectives (from package lessons)

### Week 1: ForgeDesk ticket 8801 — git conflict on the deploy branch
  - Complete the week contract: ForgeDesk ticket 8801 — git conflict on the deploy branch.
  - Reproduce worked example: Parents A and B both touch def open_hours. A adds require_role('desk'). B adds HOURS={...}. Survivor must include both tokens.
  - The WAIKE Software ForgeDesk is a two-person civic issue tracker for Device Lab checkouts.
### Week 2: REST for checkout — status codes that mean something
  - Complete the week contract: REST for checkout — status codes that mean something.
  - Reproduce worked example: POST as reader with device_id → 403. POST as desk missing device_id → 400. GET missing → 404. Create → 201.
  - ForgeDesk exposes /api/v1/checkouts.
### Week 3: Migrations that do not strand the Device Lab
  - Complete the week contract: Migrations that do not strand the Device Lab.
  - Reproduce worked example: Forward adds returned_at TIMESTAMP NULL; schema_version=3; down drops returned_at only.
  - Checkout rows live in SQLite for local Device Lab and Postgres in staging.
### Week 4: Frontend contract — accessible checkout board
  - Complete the week contract: Frontend contract — accessible checkout board.
  - Reproduce worked example: Tree includes button Filter overdue, table, OVERDUE text for ring-7, and role=alert.
  - The ForgeDesk board is a single HTML page with a table of checkouts.
### Week 5: Authz matrix — desk vs reader vs forge-bot
  - Complete the week contract: Authz matrix — desk vs reader vs forge-bot.
  - Reproduce worked example: desk:{create,close,read}; reader:{read}; forge-bot:{annotate}. Bot close fails.
  - Roles: desk can create and close checkouts.
### Week 6: Automated tests that catch the silent 200
  - Complete the week contract: Automated tests that catch the silent 200.
  - Reproduce worked example: Report total=10 failed=0 skipped=1 includes test_reader_post_forbidden passed=true.
  - Parse a JUnit-like JSON report: total, failed, skipped.
### Week 7: GitHub Actions — CI that blocks bad merges
  - Complete the week contract: GitHub Actions — CI that blocks bad merges.
  - Reproduce worked example: on:[pull_request]; jobs lint → test → upload-report; no ungated deploy on PR.
  - Workflow forge-ci must run on pull_request, lint, test, and upload the report artifact.
### Week 8: Deploy and rollback on Device Lab compose
  - Complete the week contract: Deploy and rollback on Device Lab compose.
  - Reproduce worked example: current=sha256:aaa rollback_to=sha256:bbb migrate=ok health=healthy.
  - Deploy pins image digest sha256:… to local compose and writes rollback pointer to previous digest.
### Week 9: Security review — findings with severity bands
  - Complete the week contract: Security review — findings with severity bands.
  - Reproduce worked example: Findings include FORGE-IDOR-1 severity=high with evidence lacking owner check.
  - Review ForgeDesk for IDOR on checkout ids, missing login rate limit, verbose 500s.
### Week 10: Observability and issue→deploy capstone
  - Complete the week contract: Observability and issue→deploy capstone.
  - Reproduce worked example: failed=50 total=10000 → availability=0.995; budget_ok true.
  - SLO: checkout API availability 99.5% over fixture window.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
