# Week 10: RAG, privacy, responsibility — retrieve without leaking patrons

Capstone week: a tiny RAG over EdgeForge runbooks. Ticket EF-2A01 retrieves top-k chunks for 'USB reset storm' and must redact any accidental email/phone patterns before display. Responsible AI means disclosing AI assistance, refusing biometric identification, and documenting who is harmed by a false quiet alarm.

The lab checks retrieval hit ids, redaction count, and that biometric_claim is false.

Query retrieves chunks [R12,R19]. Redact 2 emails. biometric_claim must be false.

RAG retrieves runbook chunks R12 and R19 for 'USB reset storm,' then redacts contact strings before any display path. biometric_claim must remain false — occupancy models do not identify humans.

Responsible AI is operational: disclose assistance on the harm note, name who is hurt by false quiet alarms (patrons waiting / understaffed desk), and ship metrics+digest+budget+RAG JSON in the portfolio.

Capstone refusal list: face galleries, unredacted emails, vendor cert claims, and any narrative that the model 'knows' a person. Fixture counts only; no fabricated city savings.

## Worked example

top_k hits R12,R19; redactions=2; biometric_claim=false.
