# Week 8: Testing & CI gate tokens (a11y-aware)

**Ticket:** GPL-5808  
**Lab:** `lab_gpl_ci_tokens`

## Objectives
- Report tokens_passed/tokens_total
- fabricated_green=false
- Include a11y-related gate tokens when present in fixture

## Body
Testing is CI tokens with honest pass/fail. Accessibility gates (when listed in fixture) count — color-only UI failures are product defects. fabricated_green must be false.

## Worked example
tokens_passed=4, tokens_total=4, fabricated_green=false

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No fabricated green CI
- No skipping a11y token when fixture requires it

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_ci_tokens` and `GPL-5808`. Empty {} fails. A file whose body is only PASS raises.
