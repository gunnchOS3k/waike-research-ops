# Week 5: Authz matrix — desk vs reader vs forge-bot

Roles: desk can create and close checkouts. reader can GET only. forge-bot can annotate but cannot close. The lab evaluates an action matrix. Granting forge-bot checkout.close is the package negative.

AI-use mode REVIEW_MY_WORK: assistants may critique your matrix; the submitted JSON is yours and AI assistance must be disclosed (AI_DISCLOSED).

Distinct vocabulary from Harbor SOC avoids noun-swapped templates across batches.

desk may create and close checkouts; reader may GET only; forge-bot may annotate but never close. The lab evaluates an action matrix against those rules. Granting forge-bot checkout.close is the package negative and must fail. REVIEW_MY_WORK assistants may critique your matrix; the submitted JSON is yours and must carry AI_DISCLOSED when used. Keep vocabulary distinct from Harbor SOC so batch-001 and batch-002 authz labs are not noun-swapped clones.

## Worked example

desk:{create,close,read}; reader:{read}; forge-bot:{annotate}. Bot close fails.
