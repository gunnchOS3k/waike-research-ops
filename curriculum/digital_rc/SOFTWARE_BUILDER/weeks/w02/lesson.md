# Week 2: REST for checkout — status codes that mean something

ForgeDesk exposes /api/v1/checkouts. GET inventing a device returns 404 with a stable error body, not 200 with null. POST without device_id returns 400. POST from reader role against a write route returns 403. Successful POST returns 201 and Location /api/v1/checkouts/{id}.

You will build a route table in JSON and prove each case. The lab computes expected status from method, path, role, and body keys. Idempotent PUT on the same checkout id must not mint a second row.

Secure-development practice: validate input before storage, return problem-style errors without stack traces, never echo secrets. GitHub Actions will later call these routes in CI against an in-memory store.

Status codes are evidence. Inventing a device_id must yield 404 with a problem body that names the missing resource, never a 200 with null. A reader POST to a write route yields 403; a desk POST without device_id yields 400; a successful desk POST yields 201 plus Location /api/v1/checkouts/{id}. The lab recomputes expected status from method, path, role, and body keys — a screenshot of Postman is not acceptance. Idempotent PUT on the same checkout id must not mint a second row. Secure-dev habit: validate before storage, never echo secrets, keep error bodies stable for CI asserts.

## Worked example

POST as reader with device_id → 403. POST as desk missing device_id → 400. GET missing → 404. Create → 201.
