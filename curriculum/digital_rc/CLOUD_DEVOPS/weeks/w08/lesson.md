# Week 8: Deploy + rollback — digest pins and health gates

Ticket FC-4822 deploys image sha256:fc4822aa and must roll back to sha256:fc4810bb if health≠healthy. rollback_to must differ from current. migrate must be ok before traffic switch in the fixture policy.

current=sha256:fc4822aa rollback_to=sha256:fc4810bb health=healthy migrate=ok.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

Pin current digest; rollback digest differs; health healthy; migrate ok.
