# Sequence — CLOUD_DEVOPS

Complete module/week sequence from `CLOUD_DEVOPS` `course.json`.

| Week | Title | Lesson ID | Lab ID |
|------|-------|-----------|--------|
| 1 | ForgeCloud — Linux permissions before the fancy YAML | `CLOUD_DEVOPS-w01` | `lab_linux_perms` |
| 2 | Git on ForgeCloud — history you can roll back | `CLOUD_DEVOPS-w02` | `lab_git_state` |
| 3 | Containers — Dockerfile that refuses :latest and root | `CLOUD_DEVOPS-w03` | `lab_dockerfile_lint` |
| 4 | CI/CD gates — lint then test then upload, never ungated deploy | `CLOUD_DEVOPS-w04` | `lab_cicd_gate` |
| 5 | Cloud primitives — compute, storage, network as costed blocks | `CLOUD_DEVOPS-w05` | `lab_cloud_cost` |
| 6 | IAM + secrets — least privilege and no plaintext tokens | `CLOUD_DEVOPS-w06` | `lab_iam_secrets` |
| 7 | Observability — error budgets before blame | `CLOUD_DEVOPS-w07` | `lab_slo_budget` |
| 8 | Deploy + rollback — digest pins and health gates | `CLOUD_DEVOPS-w08` | `lab_deploy_rollback_cloud` |
| 9 | Kubernetes fundamentals — probes before vanity replicas | `CLOUD_DEVOPS-w09` | `lab_k8s_probes` |
| 10 | DevSecOps + incident — automate recoveries without heroics | `CLOUD_DEVOPS-w10` | `lab_incident_runbook` |

## Syllabus excerpt (source)

```
# Cloud + DevOps — ForgeCloud Platform
## Who this is for
This is not a slideshow of cloud logos. It is the job of shipping a small service safely: 0600 keys, no force-push main, digest-pinned images, gated PR pipelines, private subnets, least-privilege IAM, error budgets, rollback digests, honest probes, and incident runbooks without heroics. AWS/Azure/CKA domain names are alignment labels only — no dumps, no fake certs.
## Tracks and academy
- Tracks: CLOUD_DEVOPS
- Academy: ACADEMY_SOFTWARE
## Duration
Ten ForgeCloud weeks with bastion permissions before YAML. Budget quiet time for pipeline red builds; do not ungated-deploy on pull_request.
## Weekly map
- Week 01: ForgeCloud — Linux permissions before the fancy YAML
- Week 02: Git on ForgeCloud — history you can roll back
- Week 03: Containers — Dockerfile that refuses :latest and root
- Week 04: CI/CD gates — lint then test then upload, never ungated deploy
- Week 05: Cloud primitives — compute, storage, network as costed blocks
- Week 06: IAM + secrets — least privilege and no plaintext tokens
- Week 07: Observability — error budgets before blame
- Week 08: Deploy + rollback — digest pins and health gates
- Week 09: Kubernetes fundamentals — probes before vanity replicas
- Week 10: DevSecOps + incident — automate recoveries without heroics
## Assessments
ForgeCloud assessment mix: weekly quizzes on FC tickets, mid (20 original) on perms/git/containers/CI/IAM, final (24 original) on SLO/rollback/k8s/incident, practical over ten labs, and an incident-runbook portfolio. No force-push main; no fake CKA/AWS cert claims.
## Claim boundary
Aligns to AWS Cloud Practitioner and CKA topic labels as PUBLIC_REFERENCE_ONLY. Does not grant those credentials. Instructor keys stay out of the learner packet.
## Kinesthetic hook
Run ForgeCloud Platform for ten weeks: Linux perms → git → containers → CI → IAM/secrets → SLO → rollback → k8s probes → incident runbook.
```

## Duration note

Package default is **10 weeks**. Program files may also list workshop/bootcamp/apprenticeship formats — those are alternate delivery envelopes, not alternate content claims.
