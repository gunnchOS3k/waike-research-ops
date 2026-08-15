# Week 10: RAG, privacy, responsibility — retrieve without leaking patrons

Capstone week: a tiny RAG over EdgeForge runbooks. Ticket EF-2A01 retrieves top-k chunks for 'USB reset storm' and must redact any accidental email/phone patterns before display. Responsible AI means disclosing AI assistance, refusing biometric identification, and documenting who is harmed by a false quiet alarm.

The lab checks retrieval hit ids, redaction count, and that biometric_claim is false.

Query retrieves chunks [R12,R19]. Redact 2 emails. biometric_claim must be false.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

top_k hits R12,R19; redactions=2; biometric_claim=false.
