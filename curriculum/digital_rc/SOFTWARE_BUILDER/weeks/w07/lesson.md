# Week 7: GitHub Actions — CI that blocks bad merges

Workflow forge-ci must run on pull_request, lint, test, and upload the report artifact. Lab validates workflow JSON: triggers, ordered jobs, and deploy not on PR without environment gate. Echo PASS fails.

GitHub Actions docs are PUBLIC_REFERENCE_ONLY. We write our own workflow model. AI mode DEBUG_WITH_ME allowed on red workflows with disclosure.

Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. Operator note: record evidence before changing shared systems. 

## Worked example

on:[pull_request]; jobs lint → test → upload-report; no ungated deploy on PR.
