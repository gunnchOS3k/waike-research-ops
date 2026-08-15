# Week 9: Kubernetes fundamentals — probes before vanity replicas

Ticket FC-4916 defines a Deployment with readinessProbe and livenessProbe HTTP paths and replicas=2. replicas=20 without resource requests fails the lab's sanity check. This is fundamentals — not a claim of CKA certification.

readiness=/readyz liveness=/healthz replicas=2 requests_cpu=100m → probe_ok.

Probes: readiness=/readyz, liveness=/healthz, replicas=2, requests_cpu=100m. replicas=20 without requests fails sanity. This is fundamentals — no CKA credential is granted.

Probes gate traffic and restarts honestly. Vanity replica counts without CPU requests are how clusters thrash under desk load.

State the claim boundary in the assignment: alignment labels only. Portfolio text that says 'CKA complete' fails even if YAML validates.

Week 9 close for CLOUD_DEVOPS: ticket work ends when the lab JSON fields for `lab_k8s_probes` are filled with fixture math you can recompute aloud, and when you refuse one out-of-scope shortcut named in this week's pitfall list. The next shift must continue from your numbers without a private sidebar.

## Worked example

probes /readyz+/healthz, replicas=2, cpu request 100m → probe_ok.
