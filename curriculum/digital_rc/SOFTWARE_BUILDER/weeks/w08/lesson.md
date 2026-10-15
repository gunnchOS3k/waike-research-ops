# Week 8: Deploy and rollback on Device Lab compose

Deploy pins image digest sha256:… to local compose and writes rollback pointer to previous digest. Lab checks rollback_to != current and health healthy only after migrate=ok. Skipping migrate fails.

Physical flashing out of scope; Device Lab here is digital compose. Capstone preview: issue through deploy artifact path.

Compose and CI logs for week 8 are evidence; adjectives are not. Keep digest and status fields typed.

Deploy pins image digest sha256:… into local compose and writes rollback_to to the previous digest. Health may read healthy only after migrate=ok. Skipping migrate, leaving rollback_to equal to current, or claiming a physical flash for this digital compose target fails. Capstone preview: follow one issue fixture through branch, CI, migrate, deploy. PHYSICAL flashing stays out of scope for Software Builder.

Journal week 8 (Deploy and rollback on Device Lab compose): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

## Concept and boundary

Deployment moves a specific build into an environment. Rollback selects or restores a previously usable state, but an older application may be incompatible with a newer database. A version label without an immutable artifact or source identifier is insufficient for reproduction.

## Guided implementation

Prepare two disposable folders with known source revisions and a manifest recording their hashes. Rehearse switching a local test command between them. Expected result: you can identify which version was tested and reproduce its result. Simulate a failed check, then select the earlier version and repeat the check. No production service is affected.

## Independent evidence and recovery

Write a release gate that includes tests, schema compatibility, authorization, observability and a rollback trigger. Specify who has authority to release. A paper runbook is a design artifact, not proof that a live deployment or rollback succeeded.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

current=sha256:aaa rollback_to=sha256:bbb migrate=ok health=healthy.
