# Week 3: Containers — Dockerfile that refuses :latest and root

Ticket FC-4303 reviews a Dockerfile: FROM python:3.12-slim@sha256:abc..., USER app, no :latest. Running as root in the container fails the lab. Pin digests; do not worship floating tags on ForgeCloud.

pinned_digest=true, user_non_root=true, uses_latest=false → lint_ok.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

digest-pinned base, USER app, uses_latest=false → lint_ok.
