# Week 8: Deploy + rollback — digest pins and health gates

Ticket FC-4822 deploys image sha256:fc4822aa and must roll back to sha256:fc4810bb if health≠healthy. rollback_to must differ from current. migrate must be ok before traffic switch in the fixture policy.

current=sha256:fc4822aa rollback_to=sha256:fc4810bb health=healthy migrate=ok.

Deploy current sha256:fc4822aa with rollback_to sha256:fc4810bb, migrate=ok, health=healthy. rollback_to == current is theater and fails.

Health gates traffic; migrate=ok before switch is fixture policy. starting forever is not healthy. Digest pins identify the exact artifact you can roll back to.

Document the health gate in two lines in the journal. Screenshots of a green UI without digest fields do not satisfy lab_deploy_rollback_cloud.

Week 8 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_deploy_rollback_cloud` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

Pin current digest; rollback digest differs; health healthy; migrate ok.
