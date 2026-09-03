# Ethics-Gated Learning Data

## Red-line statement

> No human participant, minor, school, wearable/body, precise location, or vulnerable-community data will be collected until ethics review, local governance, consent/assent where required, and permissions are complete.

## Ethics-gated categories

| Data category | Risk level | Gate condition | Fallback |
|---------------|-----------|----------------|----------|
| Learner records (progress, grades) | Medium | Institutional ethics review + informed consent | Synthetic workload patterns |
| Minors as participants | High | Ethics board + parental consent + child assent | Simulate with adult participants or synthetic traces |
| School partnerships | Medium-High | School governance approval + ethics review | Community/adult learners or simulation |
| Photos/video of participants | Medium | Informed consent + data management plan | Device telemetry only |
| Location data | Medium | Ethics review + data minimization | Anonymized mobility patterns |
| Wearable/body data | High | Ethics review + informed consent + minimization | Synthetic sensor traces |
| Community data (interviews) | Medium | Ethics review + community governance | Published demographic data |
| AI tutor interaction logs | Medium | Ethics review + informed consent | Synthetic conversation patterns |

## What can proceed without ethics review

- Synthetic workload generation from curriculum structure
- Workload profile definition from activity descriptions
- Connectivity requirement mapping (technical exercise only)
- Curriculum document analysis (no student involvement)
- Technical simulation using derived workload patterns

## What requires ethics review before proceeding

- Any activity involving real learners
- Any data collection from participants
- Any deployment in educational settings
- Any observation of learning activities
- Any wearable/sensing data from humans
