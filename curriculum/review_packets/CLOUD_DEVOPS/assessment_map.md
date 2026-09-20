# Assessment map — CLOUD_DEVOPS

## Philosophy

WAIKE assessments prefer **artifacts + runnable checks** over exam-heavy gates.  
Quizzes (if present) are practice/formative unless explicitly labeled summative.

## Assessment artifacts on disk

- `curriculum/digital_rc/CLOUD_DEVOPS/assessments/final_knowledge.json`
- `curriculum/digital_rc/CLOUD_DEVOPS/assessments/final_practical.json`
- `curriculum/digital_rc/CLOUD_DEVOPS/assessments/mid_course.json`

## Assignments → deliverables

| Assignment | Deliverable | Gap |
|------------|-------------|-----|
| `a01.md` | lab_linux_perms with mode_octal=384 (0600) and rationale | ok |
| `a02.md` | lab_git_state; paste a merge plan that does not force-push main | ok |
| `a03.md` | lab_dockerfile_lint with the three flags and base image name | ok |
| `a04.md` | lab_cicd_gate; explain in two lines why ungated PR deploy fails | ok |
| `a05.md` | lab_cloud_cost with cost_units and must_be_private=true | ok |
| `a06.md` | lab_iam_secrets; show vault path string and denied action | ok |
| `a07.md` | lab_slo_budget; one paragraph with numbers, no name-calling | ok |
| `a08.md` | lab_deploy_rollback_cloud; document the health gate in two lines | ok |
| `a09.md` | lab_k8s_probes; state claim boundary: no CKA granted | ok |
| `a10.md` | lab_incident_runbook and ship ForgeCloud portfolio (perms, CI, SLO, rollback, probes, incident) with no cert claims | ok |

## Rubrics → criteria

| Rubric | Criteria count | Sample | Gap |
|--------|----------------|--------|-----|
| `CLOUD_DEVOPS-assignment.md` | 3 | ticket_ids, no_force_push, no_secrets | ok |
| `CLOUD_DEVOPS-final-knowledge.md` | 2 | original_stems, slo_k8s_incident | ok |
| `CLOUD_DEVOPS-lab.md` | 5 | perms_git_ci, slo_rollback, empty_fails, wrong_fails, print_pass | ok |
| `CLOUD_DEVOPS-mid.md` | 2 | original_stems, linux_git_ci_iam | ok |
| `CLOUD_DEVOPS-portfolio.md` | 3 | artifacts, secrets_hygiene, claim_boundary | ok |
| `CLOUD_DEVOPS-practical.md` | 3 | student_json, negatives, print_pass | ok |
| `CLOUD_DEVOPS-project.md` | 3 | runbook_id, timeline, no_cert_claim | ok |
| `CLOUD_DEVOPS-quiz.md` | 2 | forge_numbers, key_hidden | ok |

## Capstone / portfolio

- Portfolio path: `curriculum/digital_rc/CLOUD_DEVOPS/portfolio/`
- Group/project paths under package `projects/` if present.

## Claim boundary

This map inventories files; it does **not** assert psychometric validity or that a live cohort was graded.
