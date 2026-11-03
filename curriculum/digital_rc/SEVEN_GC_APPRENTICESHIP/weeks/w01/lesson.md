# Week 1: Research question and claim ledger

Research Bench ticket SGA-1101 opens the apprenticeship with a question small enough to answer: does a codebook prior raise top-3 beam accuracy on a synthetic LEO scenario? Before any code runs, write a claim ledger. Every sentence you might later put in a poster gets one row and one evidence class. SYNTHETIC_SIM means your own simulator produced it, so the claim is only as strong as the model's assumptions. CITED_SPEC means a standards document states it, and the row must name the source_id, for example the 3GPP NTN study TR 38.811. MEASURED means field or bench data exist and the row points at a dataset_ref you can hand to a reviewer. A MEASURED row with no dataset is not a weak claim; it is an open question, and the ledger should say OPEN rather than quietly drop it. The 7GC campuses share one more rule: no row may imply that a university, operator, or vendor endorses the work, so affiliation_claim stays false. Mentors read the ledger before the results, because a tidy chart built on an unlabeled claim is the most common way an apprenticeship poster goes wrong.

## Worked example

claim A: SYNTHETIC_SIM; claim B: CITED_SPEC source_id=3GPP_TR_38_811_NTN; claim C: MEASURED dataset_ref=none-yet status=OPEN
