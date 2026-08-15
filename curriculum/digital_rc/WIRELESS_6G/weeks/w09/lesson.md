# Week 9: O-RAN interface map — vocabulary without fake RIC production

Ticket WR-4909 maps A1/E2/O1/O2 to pier roles. Submit interfaces including A1,E2,O1 and
deployed_full_ric=false. Production Near-RT RIC claims without E2 logs fail.

Stay RESEARCH_LAB_SCALE. Consensus Ladder: observed = flashcards; inferred = control split
exists in O-RAN talk; still need = E2 subscription logs (PHYSICAL_PENDING).

Failure mode: noun-swapping a Cloud/DevOps deck. Empty {} fails. PASS raises.

Map A1, E2, and O1 onto pier roles with one sentence each. deployed_full_ric stays
false until E2 subscription logs exist (PHYSICAL_PENDING). Noun-swapping a Cloud or
DevOps slide deck into O-RAN vocabulary fails the week.

O2 may appear as optional vocabulary but does not unlock a production RIC claim.
RESEARCH_LAB_SCALE is the only honest size label for WR-4909.

Sketch A1 policy advice, E2 near-RT control, and O1/O2 management as separate arrows on
the pier whiteboard for WR-4909. Require deployed_full_ric=false until an E2 subscription
log path exists. Write one sentence explaining why a Cloud/DevOps deck cannot be
noun-swapped into O-RAN interfaces. Cap the honesty note at RESEARCH_LAB_SCALE and refuse
production RIC claims without PHYSICAL_PENDING evidence.

## Worked example

interfaces include A1,E2,O1; deployed_full_ric=false.
