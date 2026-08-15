# Week 9: Kubernetes fundamentals — probes before vanity replicas

Ticket FC-4916 defines a Deployment with readinessProbe and livenessProbe HTTP paths and replicas=2. replicas=20 without resource requests fails the lab's sanity check. This is fundamentals — not a claim of CKA certification.

readiness=/readyz liveness=/healthz replicas=2 requests_cpu=100m → probe_ok.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

Evidence for this week lives in the submitted lab JSON and the numbered fixture cases — not in a screenshot of a green checkmark.

## Worked example

probes /readyz+/healthz, replicas=2, cpu request 100m → probe_ok.
