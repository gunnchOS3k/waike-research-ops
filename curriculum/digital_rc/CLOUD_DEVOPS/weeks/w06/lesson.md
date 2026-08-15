# Week 6: IAM + secrets — least privilege and no plaintext tokens

Ticket FC-4614 reviews a role that can deploy but not iam:CreateUser. A secret found in plaintext in the fixture repo fails. You will mark actions_allowed and plaintext_secrets_found=false after moving the token to a vault stub path.

allowed=['ecr:Upload','ecs:UpdateService']; denied includes iam:CreateUser; plaintext_secrets_found=false.

Least privilege: allow ecr:Upload and ecs:UpdateService; deny iam:CreateUser on the deploy role. plaintext_secrets_found must be false after moving tokens to a vault stub path.

A token in git is an incident precursor. Vault path length ≥4 is the stub contract — empty strings fail. Admin-by-default roles fail even when deploys 'work.'

Pair IAM review with secrets hygiene every time you touch a deploy role. One without the other is cosplay DevSecOps.

Week 6 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_iam_secrets` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

Deploy role without CreateUser; vault path replaces plaintext token.
