# Week 2: REST for checkout — status codes that mean something

## Slide 1 — Hook
REST for checkout — status codes that mean something

## Slide 2 — Worked example
POST as reader with device_id → 403. POST as desk missing device_id → 400. GET missing → 404. Create → 201.

## Slide 3 — Lab contract
`lab_rest_api` rejects empty/wrong/print-PASS.

## Speaker notes
Stay in SOFTWARE_BUILDER vocabulary. Do not noun-swap another academy's deck.
Assignment: Author five route cases for ticket 8802 covering 201/400/403/404 and store-length=1 after idempotent PUT....
