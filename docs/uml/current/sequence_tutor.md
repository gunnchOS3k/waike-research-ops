# Sequence — tutor interaction (current)

gunnchAI3k is a **consumer**. Live Discord lesson bodies in that repo are mocked; mastery discovery of `course.json` is real when the sibling checkout exists.

```mermaid
sequenceDiagram
  participant L as Learner
  participant W as waike-research-ops
  participant G as gunnchAI3k LEARNER_TUTOR
  participant E as EDUCATOR_COPILOT
  L->>W: open SOFTWARE_BUILDER student packet
  L->>G: ask for a hint (no keys)
  G->>W: discoverCoursesFromContract
  W-->>G: course.json + labs (no answer_keys)
  G-->>L: Socratic / fixture help
  E->>W: read instructor/answer_keys.json
  E-->>E: HITL required — do not publish grades
```

Contract: `docs/17_WAIKE_TO_GUNNCHAI3K_API_CONTRACT.md`, `docs/GUNNCHAI3K_TUTOR_INTEGRATION.md`. Modes enforced in gunnchAI3k `src/waike-mastery/modes.ts`.
