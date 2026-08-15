# Week 3: Containers — Dockerfile that refuses :latest and root

Ticket FC-4303 reviews a Dockerfile: FROM python:3.12-slim@sha256:abc..., USER app, no :latest. Running as root in the container fails the lab. Pin digests; do not worship floating tags on ForgeCloud.

pinned_digest=true, user_non_root=true, uses_latest=false → lint_ok.

Dockerfile lint: digest-pinned base, USER non-root, uses_latest=false. Floating :latest and root runtime fail lint_ok even when the image 'runs on my laptop.'

Pinning is reproducibility for ops the way model digests are reproducibility for EdgeForge. Document the base name and the three flags in lab_dockerfile_lint.

This week is not a full Kubernetes cluster. It is image hygiene that later probes depend on. Skip the meme FROM ubuntu:latest AS root.

Week 3 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_dockerfile_lint` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

digest-pinned base, USER app, uses_latest=false → lint_ok.
