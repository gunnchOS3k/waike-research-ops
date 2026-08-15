# Week 6: IAM + secrets — least privilege and no plaintext tokens

Ticket FC-4614 reviews a role that can deploy but not iam:CreateUser. A secret found in plaintext in the fixture repo fails. You will mark actions_allowed and plaintext_secrets_found=false after moving the token to a vault stub path.

allowed=['ecr:Upload','ecs:UpdateService']; denied includes iam:CreateUser; plaintext_secrets_found=false.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

Deploy role without CreateUser; vault path replaces plaintext token.
