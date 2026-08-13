# Week 8: Deploy and rollback on Device Lab compose

Deploy pins image digest sha256:… to local compose and writes rollback pointer to previous digest. Lab checks rollback_to != current and health healthy only after migrate=ok. Skipping migrate fails.

Physical flashing out of scope; Device Lab here is digital compose. Capstone preview: issue through deploy artifact path.

Compose and CI logs for week 8 are evidence; adjectives are not. Keep digest and status fields typed.

Deploy pins image digest sha256:… into local compose and writes rollback_to to the previous digest. Health may read healthy only after migrate=ok. Skipping migrate, leaving rollback_to equal to current, or claiming a physical flash for this digital compose target fails. Capstone preview: follow one issue fixture through branch, CI, migrate, deploy. PHYSICAL flashing stays out of scope for Software Builder.

Journal week 8 (Deploy and rollback on Device Lab compose): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

## Worked example

current=sha256:aaa rollback_to=sha256:bbb migrate=ok health=healthy.
