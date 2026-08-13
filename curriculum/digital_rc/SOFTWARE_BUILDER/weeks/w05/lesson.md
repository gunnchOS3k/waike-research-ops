# Week 5: Authz matrix — desk vs reader vs forge-bot

Roles: desk can create and close checkouts. reader can GET only. forge-bot can annotate but cannot close. The lab evaluates an action matrix. Granting forge-bot checkout.close is the package negative.

AI-use mode REVIEW_MY_WORK: assistants may critique your matrix; the submitted JSON is yours and AI assistance must be disclosed (AI_DISCLOSED).

Distinct vocabulary from Harbor SOC avoids noun-swapped templates across batches.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

## Worked example

desk:{create,close,read}; reader:{read}; forge-bot:{annotate}. Bot close fails.
