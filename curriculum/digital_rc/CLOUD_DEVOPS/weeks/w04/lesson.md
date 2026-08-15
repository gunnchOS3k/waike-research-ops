# Week 4: CI/CD gates — lint then test then upload, never ungated deploy

Ticket FC-4410 encodes a pipeline: on pull_request → lint → test → upload-report. A job that deploys on pull_request without gates fails. You will submit the job order and deploy_on_pr=false.

jobs=['lint','test','upload-report']; deploy_on_pr=false; on=['pull_request'].

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

PR pipeline lint→test→upload; deploy_on_pr must be false.
