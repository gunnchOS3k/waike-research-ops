# Week 2: Identity lifecycle — Naiya, Omar, and harbor-bot

Naiya is an analyst: read and comment. Omar is a lead: may close. harbor-bot is an AI triage helper: read only. Provisioning is a ticket. Deprovisioning is a ticket. Orphan accounts are incidents waiting for a calendar.

Non-human identities are first-class in the 2026 CC guidance. Service accounts and bots get least privilege, rotation, and an owner. 'The script needs root' is not an owner.

AAA: authenticate the person or bot, authorize the action, account for it in the case log. MFA for humans. For bots, a scoped token in a secret store — never in the lesson markdown.

NICE work-role language (open) helps you say 'this is operate-and-maintain / protect-and-defend adjacent' without claiming a federal job. Harbor's access review is monthly: Omar prints the binding table, Naiya spots the intern who left in June still listed as analyst, and harbor-bot is rotated or revoked if its owner went on leave. Reviews that never happen are how service accounts become folklore.

## Concept and scope

Identity lifecycle includes creation, authorized use, review and revocation. Authentication and authorization are distinct. An access matrix is a policy specification; it becomes enforcement only when a trusted system applies it using established identities.

## Guided practice

Run the triage example tests. Predict whether analyst may read redacted records and propose containment, then compare. Expected result: read is allowed and containment proposal denied for that role. The function takes role strings as teaching inputs and does not authenticate anyone or change actual account permissions.

## Independent evidence

Add a volunteer role with an expiry requirement and define how an authorized service would enforce it. Test an unknown role. Include offboarding and session-revocation checks in the design rather than merely hiding menu items.

## Worked example

allow(naiya, case.close)=false; allow(omar, case.close)=true; allow(harbor-bot, case.close)=false.
