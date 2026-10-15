# Week 9: Security review — findings with severity bands

Review ForgeDesk for IDOR on checkout ids, missing login rate limit, verbose 500s. Lab scores findings: id, severity band, evidence. At least one high/critical for intentional IDOR fixture. Empty 'looks fine' fails.

OWASP ASVS themes are domain labels — no copied item banks. Practical assessment mode: NO_AI.

Compose and CI logs for week 9 are evidence; adjectives are not. Keep digest and status fields typed.

Score findings with id, severity band, and evidence. At least one high or critical must name the intentional IDOR fixture on checkout ids. Empty looks-fine reviews fail. Also watch missing login rate limits and verbose 500s that leak stack traces. OWASP ASVS themes are domain labels — no copied item banks. Practical assessment mode: NO_AI.

Journal week 9 (Security review — findings with severity bands): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

## Concept and boundary

A security finding connects an observed weakness to a possible impact, affected scope, evidence and remediation. Severity depends on context; a tool label alone does not establish exploitability. Review within a defined authorization boundary and avoid real personal data.

## Guided implementation

Inspect the worked example for its explicit trust limits. Identify parameter-bound SQL as one defense against treating item IDs as executable SQL, and caller-supplied role strings as a reason the fixture cannot serve as real authentication. Run the quotation-containing input test. Expected result: the input is treated as a missing ID, not as a query that returns all rows.

## Independent evidence and recovery

Write two findings: one about using the role argument in a real service without authentication, and one about missing operational controls. Include evidence, limits, a proposed fix and a retest. Do not turn the exercise into scanning or exploitation of another system.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

Findings include FORGE-IDOR-1 severity=high with evidence lacking owner check.
