# Objectives — CLOUD_DEVOPS

## Program learning outcomes

_GAP: no numbered learning outcomes extracted from program file — use package week contracts._

## Week-level objectives (from package lessons)

### Week 1: ForgeCloud — Linux permissions before the fancy YAML
  - Complete the week contract: ForgeCloud — Linux permissions before the fancy YAML.
  - Reproduce worked example: 0666 world-writable deploy key fails; 0600 passes.
  - ForgeCloud Platform starts on a Linux bastion that deploys nothing until permissions make sense.
### Week 2: Git on ForgeCloud — history you can roll back
  - Complete the week contract: Git on ForgeCloud — history you can roll back.
  - Reproduce worked example: ahead 2 / behind 0; conflict on services/api/health.py; no force-push main.
  - Ticket FC-4206 needs a release branch that is 2 commits ahead of main with a known conflict path services/api/health.py.
### Week 3: Containers — Dockerfile that refuses :latest and root
  - Complete the week contract: Containers — Dockerfile that refuses :latest and root.
  - Reproduce worked example: digest-pinned base, USER app, uses_latest=false → lint_ok.
  - Ticket FC-4303 reviews a Dockerfile: FROM python:3.12-slim@sha256:abc..., USER app, no :latest.
### Week 4: CI/CD gates — lint then test then upload, never ungated deploy
  - Complete the week contract: CI/CD gates — lint then test then upload, never ungated deploy.
  - Reproduce worked example: PR pipeline lint→test→upload; deploy_on_pr must be false.
  - Ticket FC-4410 encodes a pipeline: on pull_request → lint → test → upload-report.
### Week 5: Cloud primitives — compute, storage, network as costed blocks
  - Complete the week contract: Cloud primitives — compute, storage, network as costed blocks.
  - Reproduce worked example: 16 vCPU-hours + 50GB → 16.5 cost_units; private subnet required.
  - Ticket FC-4508 estimates a lab stack: 2 vCPU × hours + 50GB storage.
### Week 6: IAM + secrets — least privilege and no plaintext tokens
  - Complete the week contract: IAM + secrets — least privilege and no plaintext tokens.
  - Reproduce worked example: Deploy role without CreateUser; vault path replaces plaintext token.
  - Ticket FC-4614 reviews a role that can deploy but not iam:CreateUser.
### Week 7: Observability — error budgets before blame
  - Complete the week contract: Observability — error budgets before blame.
  - Reproduce worked example: 40/10000 → 0.996 availability; under 50-failure cap → budget_ok.
  - Ticket FC-4719 sets SLO availability 99.5% over 10_000 requests.
### Week 8: Deploy + rollback — digest pins and health gates
  - Complete the week contract: Deploy + rollback — digest pins and health gates.
  - Reproduce worked example: Pin current digest; rollback digest differs; health healthy; migrate ok.
  - Ticket FC-4822 deploys image sha256:fc4822aa and must roll back to sha256:fc4810bb if health≠healthy.
### Week 9: Kubernetes fundamentals — probes before vanity replicas
  - Complete the week contract: Kubernetes fundamentals — probes before vanity replicas.
  - Reproduce worked example: probes /readyz+/healthz, replicas=2, cpu request 100m → probe_ok.
  - Ticket FC-4916 defines a Deployment with readinessProbe and livenessProbe HTTP paths and replicas=2.
### Week 10: DevSecOps + incident — automate recoveries without heroics
  - Complete the week contract: DevSecOps + incident — automate recoveries without heroics.
  - Reproduce worked example: RB-FC-rollback; heroics=false; token_rotated=true; three timeline stamps.
  - Capstone: an incident playbook that rolls back, rotates a leaked stub token, and records timeline timestamps.

## Honesty note

Objectives above are extracted or derived from existing package/program text.  
Where lesson bodies are thin, treat week objectives as **provisional** until authors expand lesson contracts.
