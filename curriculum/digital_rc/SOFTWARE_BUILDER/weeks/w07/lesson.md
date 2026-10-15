# Week 7: GitHub Actions — CI that blocks bad merges

Workflow forge-ci must run on pull_request, lint, test, and upload the report artifact. Lab validates workflow JSON: triggers, ordered jobs, and deploy not on PR without environment gate. Echo PASS fails.

GitHub Actions docs are PUBLIC_REFERENCE_ONLY. We write our own workflow model. AI mode DEBUG_WITH_ME allowed on red workflows with disclosure.

Compose and CI logs for week 7 are evidence; adjectives are not. Keep digest and status fields typed.

Workflow forge-ci runs on pull_request, runs lint then test, and uploads the report artifact. Deploy must not run on PR without an environment gate. The lab validates triggers, ordered jobs, and that gate. Echoing PASS as the job script fails the print-PASS ban. GitHub Actions docs are PUBLIC_REFERENCE_ONLY; write ForgeDesk's own workflow model. DEBUG_WITH_ME is allowed on red workflows with disclosure.

## Concept and boundary

Continuous integration runs configured checks against a particular source revision. It does not by itself prevent merges: repository protection must require the relevant checks. Passing tests do not establish that dependencies, secrets handling or deployment permissions are safe.

## Guided implementation

Write a CI job that checks out the source, selects a documented Python version and runs the example tests from their directory. Rehearse that command locally in a fresh folder containing only the two downloaded files. Expected result: the same six tests pass without a hidden local dependency. Keep credentials out of the workflow.

## Independent evidence and recovery

Introduce the same controlled authorization defect and show that the CI test command exits unsuccessfully. Document the exact commit and command. If no authorized CI service is available, label the result a local rehearsal rather than a remote CI run.

If a result differs, preserve the failing output and the exact file revision. Change one assumption at a time, rerun the relevant check, and explain what the new evidence supports. Do not mark an unperformed step complete.

## Worked example

on:[pull_request]; jobs lint → test → upload-report; no ungated deploy on PR.
