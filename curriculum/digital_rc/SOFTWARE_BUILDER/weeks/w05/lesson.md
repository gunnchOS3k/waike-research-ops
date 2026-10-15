# Week 5: Authz matrix — desk vs reader vs forge-bot

Roles: desk can create and close checkouts. reader can GET only. forge-bot can annotate but cannot close. The lab evaluates an action matrix. Granting forge-bot checkout.close is the package negative.

AI-use mode REVIEW_MY_WORK: assistants may critique your matrix; the submitted JSON is yours and AI assistance must be disclosed (AI_DISCLOSED).

Distinct vocabulary from Harbor SOC avoids noun-swapped templates across batches.

desk may create and close checkouts; reader may GET only; forge-bot may annotate but never close. The lab evaluates an action matrix against those rules. Granting forge-bot checkout.close is the package negative and must fail. REVIEW_MY_WORK assistants may critique your matrix; the submitted JSON is yours and must carry AI_DISCLOSED when used. Keep vocabulary distinct from Harbor SOC so batch-001 and batch-002 authz labs are not noun-swapped clones.

## Concept and boundary

Authorization must be checked where the protected action is performed. Hiding a UI control is not enforcement. A caller-supplied role is untrusted unless an authenticated, authorized system established it. The local example uses role strings solely to make the policy visible.

## Guided implementation

Read the reader denial test, run it, then temporarily remove the POST authorization check in your disposable copy. Expected result: the denial test fails. Restore the check and rerun. Explain why the test distinguishes an enforced policy from an interface convention. No real accounts are created.

## Independent evidence and recovery

Draw an access matrix for reader, desk and automation roles. Add a test for an unknown role. Explain how an actual server would resolve identity from its established session rather than accepting a JSON field as proof of authority.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

desk:{create,close,read}; reader:{read}; forge-bot:{annotate}. Bot close fails.
