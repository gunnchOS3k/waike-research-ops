# Week 7: GitHub Actions — CI that blocks bad merges

Workflow forge-ci must run on pull_request, lint, test, and upload the report artifact. Lab validates workflow JSON: triggers, ordered jobs, and deploy not on PR without environment gate. Echo PASS fails.

GitHub Actions docs are PUBLIC_REFERENCE_ONLY. We write our own workflow model. AI mode DEBUG_WITH_ME allowed on red workflows with disclosure.

Compose and CI logs for week 7 are evidence; adjectives are not. Keep digest and status fields typed.

Workflow forge-ci runs on pull_request, runs lint then test, and uploads the report artifact. Deploy must not run on PR without an environment gate. The lab validates triggers, ordered jobs, and that gate. Echoing PASS as the job script fails the print-PASS ban. GitHub Actions docs are PUBLIC_REFERENCE_ONLY; write ForgeDesk's own workflow model. DEBUG_WITH_ME is allowed on red workflows with disclosure.

## Worked example

on:[pull_request]; jobs lint → test → upload-report; no ungated deploy on PR.
