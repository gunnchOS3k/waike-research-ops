# Week 1: ForgeCloud — Linux permissions before the fancy YAML

ForgeCloud Platform starts on a Linux bastion that deploys nothing until permissions make sense. Ticket FC-4101 shows a deploy key file mode 0666 — world writable. You will compute the correct mode 0600 and refuse to continue CI until the lab's mode check passes. Cloud YAML cannot save a secret that every login can rewrite.

deploy_key mode 0666 → must be 0600; owner read/write only.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

0666 world-writable deploy key fails; 0600 passes.
