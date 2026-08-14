# Week 9: Security review — findings with severity bands

Review ForgeDesk for IDOR on checkout ids, missing login rate limit, verbose 500s. Lab scores findings: id, severity band, evidence. At least one high/critical for intentional IDOR fixture. Empty 'looks fine' fails.

OWASP ASVS themes are domain labels — no copied item banks. Practical assessment mode: NO_AI.

Compose and CI logs for week 9 are evidence; adjectives are not. Keep digest and status fields typed.

Score findings with id, severity band, and evidence. At least one high or critical must name the intentional IDOR fixture on checkout ids. Empty looks-fine reviews fail. Also watch missing login rate limits and verbose 500s that leak stack traces. OWASP ASVS themes are domain labels — no copied item banks. Practical assessment mode: NO_AI.

Journal week 9 (Security review — findings with severity bands): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

## Worked example

Findings include FORGE-IDOR-1 severity=high with evidence lacking owner check.
