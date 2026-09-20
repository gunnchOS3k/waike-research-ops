# Data handling

## Allowed data in digital course
- Course fixtures under `fixtures/` (SIMULATED).
- Learner-generated lab JSON without PII.
- Public documentation citations.

## Disallowed without separate authorization
- Production RAN traces, subscriber identifiers, private competition IQ.
- Patron/library personal data from civic desks.
- Partner NDA materials pasted into coursework.

## Retention
- Learner portfolios should minimize personal data; prefer digests over raw captures.
- Instructor keys never enter learner sync packs.
- Field datasets, if later collected, need EXTERNAL_FIELD_GATE + consent plan.

## Classification reminder
SIMULATED fixtures stay labeled until replaced by MEASURED_HARDWARE / MEASURED_FIELD under gates.
