# Week 4: CI/CD gates — lint then test then upload, never ungated deploy

Ticket FC-4410 encodes a pipeline: on pull_request → lint → test → upload-report. A job that deploys on pull_request without gates fails. You will submit the job order and deploy_on_pr=false.

jobs=['lint','test','upload-report']; deploy_on_pr=false; on=['pull_request'].

PR pipeline: on pull_request → lint → test → upload-report. deploy_on_pr must be false. Ungated PR deploy is how fixtures become incidents.

upload-report persists evidence; deleting it to hide a red build fails the gate spiritually even if JSON is hand-edited. Order matters — deploy-first pipelines fail cicd checks.

Explain in two lines why PR deploy is forbidden: unreviewed code must not mutate the ForgeCloud runtime the desk depends on.

Week 4 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_cicd_gate` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

PR pipeline lint→test→upload; deploy_on_pr must be false.
