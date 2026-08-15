# Week 5: Cloud primitives — compute, storage, network as costed blocks

Ticket FC-4508 estimates a lab stack: 2 vCPU × hours + 50GB storage. You will compute cost_units = vcpu_hours*1.0 + storage_gb*0.01 on the fixture rates (toy currency). No claiming real AWS invoices. Networking is a private subnet flag must_be_private=true.

vcpu_hours=16, storage_gb=50 → cost_units=16+0.5=16.5; must_be_private=true.

Toy cost_units = vcpu_hours×1.0 + storage_gb×0.01. Example: 16 + 50×0.01 = 16.5. must_be_private=true for secret-bearing paths — public subnets fail the lab.

Do not claim these units as a real AWS invoice. Fixture rates only. Networking here is the private-subnet flag, not a BGP lab.

Journal the cost line and the subnet requirement together so finance and security reviews see the same artifact.

Week 5 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_cloud_cost` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

16 vCPU-hours + 50GB → 16.5 cost_units; private subnet required.
