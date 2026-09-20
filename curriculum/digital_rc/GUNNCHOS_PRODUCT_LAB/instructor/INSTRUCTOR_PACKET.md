# Instructor packet — GUNNCHOS_PRODUCT_LAB

## Purpose
Run the gunnchOS Product Lab Bench (charter → compatibility → checkout) without fabricating EVT, field, or adoption evidence.

## Keys and HITL
- Keys: `instructor/answer_keys.json` (not in learner ingest)
- Do not publish scores without human review of portfolio claims
- Reject physical-device claims without Device Lab evidence class

## Labs
- Run `python3 scripts/run_course_labs.py` — empty `{}`, wrong fixtures, and print-PASS must fail
- Emphasize product charter honesty, compat matrix, and checkout flow JSON
- Classification default: DIGITAL / SIMULATED; PHYSICAL only with evidence class

## AI policy modes
- Tutoring: EXPLAIN / HINT / QUESTION_ME / DEBUG_WITH_ME / REVIEW_MY_WORK / COMPARE_APPROACHES / PRACTICE
- Assessment: AI_ALLOWED / AI_RESTRICTED / AI_DISCLOSED / NO_AI
- Graded charter metrics and compat matrices: prefer AI_DISCLOSED or NO_AI

## Prep and pacing
1. Weeks 1–2: charter scope without fabricated impact numbers
2. Weeks 3–5: compatibility matrix + checkout latency fixtures
3. Weeks 6–8: release notes honesty + rollback narrative
4. Weeks 9–10: portfolio packet with claim boundary checklist

## Common misconceptions
- Product lab ≠ EVT complete
- Compatibility rows need fixture IDs, not marketing adjectives
- Checkout improvements must cite median_wait_minutes from lab JSON

## UDL / accessibility
- Prefer text + JSON artifacts over color-only status
- Offer keyboard-only paths for UI checklists
- Cost assumption: existing laptop; Device Lab hardware opt-in

## Claim refusals
- No PMI / vendor cert grants
- No institutional adoption claims
- No fabricated community-impact percentages
